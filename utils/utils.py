import jwt

from users.models import User
from kokoafriendsgolf.settings import JWT_SECRET_KEY, JWT_ALGORITHM

def get_name_list(model):
    return list(map(lambda c: c.name, model.objects.all()))

def decode_jwt(token):
    return jwt.decode(token, JWT_SECRET_KEY, JWT_ALGORITHM)

    
def get_user_from_jwt(token):
    payload = decode_jwt(token)
    user    = User.objects.get(pk=payload.get('user_id'))
    return user