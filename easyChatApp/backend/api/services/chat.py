from api.database import Message, Session


def send_message_user(
        db:Session,
        from_user_id:int,
        to_user_id:int,
        message:str,
        past_message_id:int,
):
    """
        send message to an user
    """
    pass

def send_message_groupe(
        db:Session,
        from_user_id:int,
        to_groupe_id:int,
        message:str,
        past_message_id:int,
):
    """
        send message to a groupe
    """
    pass

def receive_message_user(
        db:Session,
        from_user_id:int,
        past_message_id:int,
):
    """
        receive message from a user
    """
    pass

def receive_message_groupe(
        db:Session,
        from_user_id:int,
        past_message_id:int,
):
    """
        receive message from a groupe
    """
    pass

def modify_message_user(
        db:Session,
        from_user_id:int,
        to_user_id:int,
        message_id:int,
        new_message:str,
):
    """
        modify message to an user
    """
    pass

def modify_message_groupe(
        db:Session,
        from_user_id:int,
        to_groupe_id:int,
        message_id:int,
        new_message:str,
):
    """
        modify message in a groupe
    """
    pass

def delete_message_user(
        db:Session,
        from_user_id:int,
        to_user_id:int,
        message_id:int,
        new_message:str,
):
    """
        delete message to an user
    """
    pass

def delete_message_groupe(
        db:Session,
        from_user_id:int,
        to_groupe_id:int,
        message_id:int,
        new_message:str,
):
    """
        delete message in a groupe
    """
    pass
