import jwt

from django.http import JsonResponse

from users.models import User
from kokoafriendsgolf.settings import JWT_SECRET_KEY, JWT_ALGORITHM

def get_name_list(model):
    return list(map(lambda c: c.name, model.objects.all()))

def decode_jwt(token):
    return jwt.decode(token, JWT_SECRET_KEY, JWT_ALGORITHM)
    
def get_user_from_jwt(token):
    try:
        payload = decode_jwt(token)
        user    = User.objects.get(pk=payload.get('user_id'))
        return user

    except jwt.exceptions.ExpiredSignatureError as e:
        return JsonResponse({"status": "TOKEN_ERROR", "message": e.args[0]}, status=401)

    except jwt.exceptions.InvalidSignatureError as e:
        return JsonResponse({"status": "TOKEN_ERROR", "message": e.args[0]}, status=401)

    except jwt.exceptions.DecodeError as e:
        return JsonResponse({"status": "TOKEN_ERROR", "message": e.args[0]}, status=401)