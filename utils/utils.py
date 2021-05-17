import functools

def get_name_list(model):
    return list(map(lambda c: c.name, model.objects.all()))

def login_required():
    def decorator(function):
        @functools.wraps(function)
        def wrapper_login_required(request, *args, **kwargs):
            print(request)
            return function(request, *args, *kwargs)
        
        return wrapper_login_required
    return decorator