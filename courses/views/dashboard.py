from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse
from courses.models.course import Course
from courses.models.video import Video
from django.contrib.auth.models import User
from courses.models.user_course import UserCourse
from courses.forms.profile_form import ProfileForm
from courses.models.payment import Payment
from courses.models.contact_us import ContactUs

def dashboard(request):
    
    user = User.objects.get(username=request.user)
    
    return render(request, 'courses/dashboard.html', {'user':user})


def user_courses_dash(request):
    user = request.user
    user_courses = UserCourse.objects.filter(user=user)
    return render(request, 'courses/user/user_coures.html', {'user_courses':user_courses})

from itertools import zip_longest

def my_orders(request):
    orders = Payment.objects.filter(user=request.user)
    payment_ids = [order.payment_id[5:25] for order in orders]
    # Make sure both lists are of equal length
    orders_length = len(orders)
    payment_ids_length = len(payment_ids)
    max_length = max(orders_length, payment_ids_length)
    orders = list(orders)
    payment_ids = list(payment_ids)
    if orders_length < max_length:
        orders.extend([None] * (max_length - orders_length))
    if payment_ids_length < max_length:
        payment_ids.extend([None] * (max_length - payment_ids_length))
    # Combine both lists using zip_longest to handle cases where one list is longer than the other
    combined_data = zip_longest(orders, payment_ids)
    return render(request, 'courses/user/my_orders.html', {'combined_data': combined_data})




from django.contrib import messages

def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "You've successfully updated your profile.")
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'courses/user/update-profile.html', {'form': form})





def my_contact_history(request):
    user = request.user
    contacts = ContactUs.objects.filter(user=user)
    return render(request, 'courses/user/my_contact_history.html', {'contacts':contacts})



def privacy_policy(request):
    return render(request, 'courses/user/privacy_policy.html')