from api.database import Message, Session, select
from fastapi import WebSocket



def get_messages(
        db:Session,
        user_send_id:int|None = None,
        user_receive_id:int|None = None,
        groupe_id:int|None = None,
) -> list[Message]:
    data = select(Message)
    if user_send_id:
        data.filter(Message.send_by == user_send_id)
    if user_receive_id:
        data.filter(Message.send_to_user == user_receive_id)
    if groupe_id:
        data.filter(Message.send_to_groupe == groupe_id)
    result = db.scalars(data).all()

    return result

class ConnectionManager:
    def __init__(self):
        self.user_conn: dict[str, dict[int, WebSocket]] = {}
        self.groupe_conn: dict[int, dict[int, WebSocket]] = {}
    
    @staticmethod
    def genUserChatID(user_id:int, to_user_id:int) -> str:
        return f"{user_id}{to_user_id}" if user_id < to_user_id else f"{to_user_id}{user_id}"

    async def connect_user(self, user_id:int, to_user_id:int, socket:WebSocket):
        chat_id = self.genUserChatID(user_id, to_user_id)
        await socket.accept()
        if chat:=self.user_conn.get(chat_id):
            chat[user_id] = socket
        else:
            self.user_conn[chat_id] = {user_id: socket}

    async def send_user(self, user_id:int, to_user_id:int, message:str, db:Session):
        chat_id = self.genUserChatID(user_id, to_user_id)
        if chat:=self.user_conn.get(chat_id):
            for key, value in chat.items():
                value.send_json(data={user_id:message})
            Message(
                content=message,
                send_by=user_id,
                send_to_user=to_user_id,
                send_to_groupe=None,
            ).saveWithCommit(db)
    
    async def disconnect_user(self, user_id:int, to_user_id:int):
        chat_id = self.genUserChatID(user_id, to_user_id)
        if chat:=self.user_conn.get(chat_id):
            chat.pop(user_id)
        
    async def connect_groupe(self, user_id:int, groupe_id:int, socket:WebSocket):
        await socket.accept()
        if chat:=self.groupe_conn.get(groupe_id):
            chat[user_id] = socket
        else:
            self.groupe_conn[groupe_id] = {user_id:socket}

    async def send_groupe(self, user_id:int, groupe_id:int, message:str, db:Session):
        if chat:= self.groupe_conn.get(groupe_id):
            for key, value in chat.items():
                await value.send_json(data={user_id:message})
            # Message(
            #     content=message,
            #     send_by=user_id,
            #     send_to_user=None,
            #     send_to_groupe=groupe_id,
            # ).saveWithCommit(db)
    
    async def disconnect_groupe(self, user_id:int, groupe_id:int, message:str):
        if chat:= self.groupe_conn.get(groupe_id):
            chat.pop(user_id)

