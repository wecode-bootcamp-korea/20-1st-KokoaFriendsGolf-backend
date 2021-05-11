import time
import bcrypt
import jwt
import json
from json                   import JSONDecodeError

from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ValidationError

from users.models           import User
from utils.validators       import validate_email, validate_password, validate_gender, validate_duplicate, DuplicatedEntryError
from my_settings            import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_DURATION_SEC

class SignInView(View):

    def post(self, request):
        
        try:
            data = json.loads(request.body)

            email = data['email']
            password = data['password']

            user = User.objects.get(email=email)

            if not bcrypt.checkpw(str(data.get('password')).encode('utf-8'),user.password.encode('utf-8')):
                return JsonResponse({"status": "INVALID_USER"}, status=401)

            new_token = jwt.encode({'user_id': user.id, 'iat': int(time.time()), 'exp': int(time.time()) + JWT_DURATION_SEC}, 
                                JWT_SECRET_KEY, 
                                JWT_ALGORITHM)

            return JsonResponse({"status": "SUCCESS", "token": new_token}, status=200)

        except JSONDecodeError as e:
            return JsonResponse({"status": "JSON_DECODE_ERROR", "message": e.msg}, status=400)

        except KeyError as e:
            return JsonResponse({"status": "KEY_ERROR", "message": f'Key Error in Field "{e.args[0]}"'}, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({"status": "INVALID_USER"}, status=401)