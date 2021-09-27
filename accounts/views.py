from accounts.models import UserAccount as User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions


# Create your views here.
class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password != password2:
            return Response({'error': 'Password do not match'})
        else:

            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email Already Exists'})

            else:
                if len(password) < 6:
                    return Response({'error': 'Password must be at least 6 character'})

                else:

                    user = User.objects.create_user(email=email, password=password, name=name)

                    user.save()

                return Response({'success': 'User Successfully Created'})
