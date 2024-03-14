from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from courses.forms.registration_form import RegistrationForm
from courses.forms.login_form import LoginForm
from django.contrib.auth import login, logout
from django.views import View
from django.contrib import messages
from django.views.generic.edit import FormView


class SignupView(FormView):
    template_name = 'courses/signup.html'
    form_class = RegistrationForm
    success_url = '/login'

    def form_valid(self, form):
        # Save form data
        form.save()
        messages.success(self.request, 'Registration successful! Please log in.')
        return redirect('/login')  # Send success response

    def form_invalid(self, form):
        # Handle invalid form submission
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    
    
    
class LoginView(FormView):
    template_name='courses/login.html'
    form_class=LoginForm
    success_url='/'
    
    def form_valid(self, form):
        login(self.request, form.cleaned_data)
        
        next_page = self.request.GET.get('next')
        if next_page is not None:
            return redirect(next_page)
            
        messages.success(self.request, 'You have successfully logged in!')
        return super().form_valid(form)
    

'''
class SignupView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'courses/signup.html', {'form':form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'You have successfully logged in!')
            if user is not None:
                return redirect('login')
        return render(request, 'courses/signup.html', {'form':form})
'''
    
    
'''
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            "form": form
        }
        return render(request, 'courses/login.html', context=context)
        
    def post(self, request):
        form = LoginForm(request=request, data=request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')
        # else:
        #     messages.error(request, 'Invalid username or password. Please try again.')

        return render(request, 'courses/login.html', context=context)
'''
    
    
    
from django.contrib.auth import logout
    
def logoutfunc(request):
    logout(request)
    messages.error(request, 'You have successfully logged out.')
    return redirect('login')


from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'courses/user/password_change.html', {'form': form})