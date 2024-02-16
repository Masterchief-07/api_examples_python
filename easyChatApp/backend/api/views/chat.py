from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from api.database import Session, get_db
from api.services import (
    chat as chatsvc
)

chat_router = APIRouter()
chat_manager = chatsvc.ConnectionManager()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="user_id" autocomplete="off" placeholder="user_id"/>
            <input type="text" id="groupe_id" autocomplete="off" placeholder="groupe_id"/>
            <input type="text" id="messageText" autocomplete="off" placeholder="message"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket(`ws://localhost:8000/api/v1/chat/groupe/${client_id}/1/ws`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""
@chat_router.get("/test")
async def test_chat_interface():
    return HTMLResponse(
        content=html,
        status_code=200,
    )

# @chat_router.websocket("/user/ws/{client_id}")
# async def chat_with_user(client_id:int, websocket: WebSocket, db:Session = Depends(get_db)):
#     await chat_manager.connect_user(user_id=client_id)

@chat_router.websocket("/groupe/{user_id}/{groupe_id}/ws", "groupe")
async def chat_with_groupe(user_id:int, groupe_id:int, websocket: WebSocket, db:Session = Depends(get_db)):
    # await websocket.accept()
    await chat_manager.connect_groupe(user_id=user_id, groupe_id=groupe_id, socket=websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await chat_manager.send_groupe(user_id=user_id, groupe_id=groupe_id, message=data, db=db)
    except WebSocketDisconnect:
        pass