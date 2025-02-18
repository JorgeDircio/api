from rest_framework.views import APIView
from django.http import JsonResponse

# Create your views here.
class Class_Register(APIView):
    
    def post(self, request):
        print(self)
        print(request)
        return JsonResponse({'message': 'Hello, world!'})