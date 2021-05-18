from django.views               import View
from django.utils.decorators    import method_decorator
from utils.decorators           import check_user
class OrderListView(View):
    @method_decorator(check_user())
    def get(self, request):
        pass

    @method_decorator(check_user())
    def post(self, request):
        pass