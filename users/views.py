import time
import bcrypt
import jwt
import json
from json                       import JSONDecodeError

from django.views               import View
from django.http                import JsonResponse
from django.db.utils            import DataError
from django.core.exceptions     import ValidationError

from users.utils                import validate_email, validate_password, validate_gender
from users.models               import User
from utils.validators           import validate_duplicate, DuplicatedEntryError
from kokoafriendsgolf.settings  import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_DURATION_SEC
class SignInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']
            user     = User.objects.get(email=email)

            if not bcrypt.checkpw(password.encode('utf-8'),user.password.encode('utf-8')):
                return JsonResponse({"status": "INVALID_USER"}, status=401)

            new_token = jwt.encode(
                                    {
                                        'user_id': user.id,
                                        'iat'    : int(time.time()),
                                        'exp'    : int(time.time()) + JWT_DURATION_SEC
                                    }, 
                                    JWT_SECRET_KEY, 
                                    JWT_ALGORITHM
                                  )

            return JsonResponse({"status": "SUCCESS", "data": {"token": new_token}}, status=200)

        except JSONDecodeError as e: 
            return JsonResponse({"status": "JSON_DECODE_ERROR", "message": e.msg}, status=400)

        except KeyError as e: 
            return JsonResponse({"status": "KEY_ERROR", "message": f'Key Error in Field "{e.args[0]}"'}, status=400)
        
        except User.DoesNotExist: 
            return JsonResponse({"status": "INVALID_USER"}, status=401)
        
        except DataError as e:
            return JsonResponse({"status": "INVALID_DATA_ERROR", "message": e.args[1]}, status=400)

class SignUpView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = validate_email(data["email"])
            password = validate_password(data["password"])
            gender   = validate_gender(data.get('gender'))
            validate_duplicate(User, data)
            
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            user = User.objects.create(
                email           = email,
                password        = hashed_password,
                phone_number    = data['phone_number'],
                name            = data['name'],
                birthday        = data.get('birthday'),
                gender          = gender,
            )

            return JsonResponse({"status": "SUCCESS", "data": {"user": user.to_dict()}}, status=200)

        except JSONDecodeError as e:
            return JsonResponse({"status": "JSON_DECODE_ERROR", "message": e.msg}, status=400)

        except ValidationError as e:
            return JsonResponse({"status": "INVALID_DATA_ERROR", "message": e.message}, status=400)

        except KeyError as e:
            return JsonResponse({"status": "KEY_ERROR", "message": f'Key Error in Field "{e.args[0]}"'}, status=400)

        except DuplicatedEntryError as e:
            return JsonResponse({"status": "DUPLICATED_ENTRY_ERROR", "message": e.err_message}, status=409)

        except DataError as e:
            return JsonResponse({"status": "INVALID_DATA_ERROR", "message": e.args[1]}, status=400)