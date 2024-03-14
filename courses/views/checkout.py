from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from courses.models.course import Course
from courses.models.video import Video
import stripe
from courses.models.payment import Payment
from courses.models.user_course import UserCourse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def checkout(request, slug):
    course = Course.objects.get(slug=slug)
    total_videos = Video.objects.filter(course=course).count()
    
    
    
    
    course = Course.objects.get(slug=slug)
    user = request.user
    
    # Check if UserCourse already exists
    if UserCourse.objects.filter(user=user, course=course).exists():
        # error = messages.error(request, "You are Already Enrolled in this Course")
        return redirect('my_courses')
    
    context = {
        "course": course,
        "total_videos":total_videos
    }

    return render(request, template_name="courses/check_out.html", context=context)



stripe.api_key='sk_test_51OpZiJFHs1Gmgtcb4tfLJoVlcY6c15ZasfouYa4U0Pp4688mU7ZpwHrq1NcyjP9jnWnshfsPTFQ41kuZNxDTctLI00WW1PCIuT'
def checkout_session(request, slug):
    course = Course.objects.get(slug=slug)
    
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'MAD',
                'product_data': {
                    'name': course.name,
                },
                'unit_amount': int(round(course.price - (course.price * course.discount * 0.01)) * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/pay_success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='http://127.0.0.1:8000/pay_cancel',
        client_reference_id=request.user.id
    )
    
    Payment.objects.create(
        order_id=session.created,
        payment_id=session.id,
        user=request.user,
        course=course
    )

    return redirect(session.url, code=303)


def pay_success(request):
    session_id = request.GET.get('session_id')
    payment = Payment.objects.get(user=request.user, payment_id=session_id)
    payment_id = payment.payment_id[10:30]
    
    # Try to get the existing UserCourse object
    try:
        userCourse = UserCourse.objects.get(user=payment.user, course=payment.course)
    except UserCourse.DoesNotExist:
        # If UserCourse does not exist, create a new one
        userCourse = UserCourse(user=payment.user, course=payment.course)
        userCourse.save()
    
    # Update payment status and user_course
    payment.status = True
    payment.user_course = userCourse
    payment.save()
    
    return render(request, 'courses/payment-success.html', {'payment': payment, 'payment_id':payment_id})



def pay_cancel(request):
    return render(request, 'courses/payment-failed.html')