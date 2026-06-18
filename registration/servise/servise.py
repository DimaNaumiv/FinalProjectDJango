import bcrypt
import random
from datetime import date
from ..models import User,Session

def save_user(first_name,last_name,hesh_password):
    now = date.today()
    User.objects.create(
        first_name = first_name,
        last_name = last_name,
        hash_password = hesh_password,
        created_at = now,
        updated_at = now
    )
    return True

def generate_session_code():
    # Робимо простішу та безпечну генерацію на 16 символів
    # Твій алгоритм з перемішуванням списку:
    chars = []
    for _ in range(8):
        chars.append(chr(random.randint(65, 90))) # Літери A-Z
    for _ in range(8):
        chars.append(str(random.randint(0, 9)))   # Цифри 0-9
        
    random.shuffle(chars) # Перемішує список на місці
    return "".join(chars) # Склеює в рядок довжиною 16

def create_session(user_id):
    now = date.today()
    user = User.objects.get(pk=user_id)
    Session.objects.create(
        session_code = generate_session_code(),
        user = user,
        created_at = now,
        updated_at = now
    )
    return True

def delete_session(session_code):
    session = Session.objects.get(pk=session_code)

    if(session == None):
        return False
    
    session.delete()
    return True

def get_session_code(user_id):
    return Session.objects.filter(user_id = user_id)

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
