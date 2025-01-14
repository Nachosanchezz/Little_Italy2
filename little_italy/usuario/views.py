from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'usuario/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'usuario/login.html')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'usuario/logout.html')


from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # Validaciones básicas
        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'usuario/register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return render(request, 'usuario/register.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está registrado.')
            return render(request, 'usuario/register.html')
        # Crea al usuario
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        # Especifica el backend manualmente antes de iniciar sesión
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        # Inicia sesión automáticamente después de registrarse
        login(request, user)
        messages.success(request, 'Te has registrado exitosamente.')
        return redirect('home')  # Cambia 'home' por la vista principal de tu aplicación
    # Si es una solicitud GET
    return render(request, 'usuario/register.html')

    
