from rest_framework.views import APIView
from django.http import HttpResponseRedirect, JsonResponse
from http import HTTPStatus
from django.contrib.auth.models import User
import os
from dotenv import load_dotenv
from utils import utils
import uuid

from .models import UserMetadata

# Create your views here.
class Class_Register(APIView):
    
    def post(self, request):
        required_fields = ['first_name', 'last_name','email', 'password']

        missing_fields = [field for field in required_fields if not field in request.data]
        if missing_fields:
            return JsonResponse({'message': f"El campo: {', '.join(missing_fields)} es obligatorio"}, status=HTTPStatus.BAD_REQUEST)

        if(User.objects.filter(email=request.data['email']).exists()):
            return JsonResponse({'message': 'User already'}, status=HTTPStatus.BAD_REQUEST)
        
        token = uuid.uuid4()
        url = f"{os.getenv('BASE_URL')}/{os.getenv('API_URL')}/auth/activate/{token}"
        try:
            user = User.objects.create_user(
                username=request.data['email'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                email=request.data['email'],
                password=request.data['password'],
                is_active=0
            )

            UserMetadata.objects.create(token=token, user_id=user.id)

            html = f"""
                <h1>¡Bienvenido a la plataforma!</h1>
                <p>Para activar tu cuenta, haz clic en el siguiente enlace:</p>
                <a href="{url}">{url}</a>
                <br/>
                <p>Si el enlace no funciona, copia y pega la siguiente URL en tu navegador:</p>
            """

            utils.sendMail(html, "Verificación", request.data['email'])

            return JsonResponse({ "message": "Usuario creado correctamente" }, status=HTTPStatus.CREATED)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=HTTPStatus.BAD_REQUEST)

class Class_Activate(APIView):

    def get(self, request, token):
        try:
            data = UserMetadata.objects.filter(token=token).filter(user__is_active=0).get()
            UserMetadata.objects.filter(token=token).update(token="")

            User.objects.filter(id=data.user_id).update(is_active=1)

            return HttpResponseRedirect(f"{os.getenv('BASE_URL_FRONTEND')}")

        except UserMetadata.DoesNotExist:
            return JsonResponse({'message': 'Token no válido'}, status=HTTPStatus.BAD_REQUEST)
        