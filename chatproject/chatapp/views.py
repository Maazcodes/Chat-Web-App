from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from chatapp.forms import UserRegisterForm, MyForm, UserForm
from django.views.generic import ListView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def home(request):
    """Homepage"""
    return render(request, 'home.html')

@login_required # login is required to chat
def room(request, room_name="hello"):
    """ Public Chat room View"""
    return render(request, 'room.html', {
        'room_name': room_name
    })

def signup(request):
    """ Signup Function View"""
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            form  = UserRegisterForm(request.POST)
            form_captcha = MyForm(request.POST)
            if form.is_valid() and form_captcha.is_valid():
                form.save()
                messages.success(request, "You have successfully created your account")
                return redirect("home")
        else:
            form = UserRegisterForm()
            form_captcha = MyForm()
        return render(request, 'signup.html', context={'form':form, 'form_captcha':form_captcha})


class UserListView(ListView):
    """View to see the list of all users."""
    model = User
    template_name = 'user_list.html'
    queryset = User.objects.all()[:5]
    context_object_name = 'users'
    
class UserUpdateView(SuccessMessageMixin, UpdateView):
    """ View to edit user details. """
    model = User
    context_object_name = 'user'
    template_name = 'user_update.html'
    success_url = reverse_lazy('home')
    success_message = "User details updated successfully!"
    pk_url_kwarg = 'user_id'
    form_class = UserForm
