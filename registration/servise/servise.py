import bcrypt
import random
from datetime import date
from ..models import User,Session

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def registrate(first_name,last_name,password):
    heshed_password = hash_password(password)
    user_id = save_user(first_name,last_name,heshed_password)
    session_code = create_session(user_id)
    return {
        "state":True,
        "session_code":session_code
    }

def check(first_name,last_name,password):
    try:
        # 1. Шукаємо користувача ТІЛЬКИ за ім'ям та прізвищем
        user = User.objects.get(
            first_name=first_name, 
            last_name=last_name
        )
        
        # 2. Беремо його хеш з бази даних (поле hash_password у вашій БД)
        db_hash = user.hash_password.encode('utf-8')
        
        # 3. Перевіряємо, чи введений пароль відповідає хешу з бази
        if bcrypt.checkpw(password.encode('utf-8'), db_hash):
            user_id = user.id
            session_code = create_session(user_id)
            return {
                "state": True,
                "session_code": session_code
            }
        else:
            # Пароль не підійшов
            return {
                "state": False,
                "message": "User not found or invalid credentials"
            }
            
    except User.DoesNotExist:
        return {
            "state": False,
            "message": "User not found or invalid credentials"
        }


def save_user(first_name,last_name,hesh_password):
    now = date.today()
    user = User.objects.create(
        first_name = first_name,
        last_name = last_name,
        hash_password = hesh_password,
        created_at = now,
        updated_at = now
    )
    return user.id

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
    session_code = generate_session_code()
    Session.objects.create(
        session_code = session_code,
        user = user,
        created_at = now,
        updated_at = now
    )
    return session_code

def delete_session(session_code):
    session = Session.objects.get(pk=session_code)

    if(session == None):
        return False
    
    session.delete()
    return True

def check_session_code(session_code):
    session = Session.objects.get(pk=session_code)
    if(session == None):
        return False
    return True


