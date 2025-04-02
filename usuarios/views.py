from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from . import forms


def LoginApp(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/home/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def LogoutApp(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    if request.method == 'GET':
        logout(request)
        return redirect('login')


def profile_view(request):
    if request.method == 'POST':
        usuario = request.user.usuarios
        form = forms.UpdateUsuario(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return render(request, 'profile.html', {'form': form})
    usuario = request.user.usuarios
    form = forms.UpdateUsuario(instance=usuario, initial={'user_techra': usuario.user_techra,
                                                          'password_techra': usuario.password_techra})
    return render(request, 'profile.html', {'form': form})
