from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from courses.models.course import Course
from courses.models.video import Video
from courses.models.user_course import UserCourse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator


"""
@method_decorator(login_required('login'), name='dipatch')
class MyCoursesList(ListView):
    template_name='courses/my_courses.html'
    queryset=UserCourse.objects.all()
    context_object_name='user_courses'
    
    def get_queryset(self):
        return UserCourse.objects.filter(user=self.request.user)
"""



@login_required(login_url='login')
def my_courses(request):
    user = request.user
    user_courses = UserCourse.objects.filter(user=user)
    return render(request, 'courses/my_courses.html', {'user_courses':user_courses})



def coursePage(request , slug):
    course = Course.objects.get(slug  = slug)
    serial_number  = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")

    if serial_number is None:
        serial_number = 1 

    video = Video.objects.get(serial_number = serial_number , course = course)

    if (video.is_preview is False):

        if request.user.is_authenticated is False:
            return redirect("login")
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user = user  , course = course)
            except:
                return redirect("checkout" , slug=course.slug)
        
        
    context = {
        "course" : course , 
        "video" : video , 
        'videos':videos
    }
    return  render(request , template_name="courses/course_page.html" , context=context )    
    
    
    
    

# latest
'''
def coursePage(request, slug):
    course = get_object_or_404(Course, slug=slug)
    video_id = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")

    if video_id:
        try:
            video = Video.objects.get(id=video_id, course=course)
        except Video.DoesNotExist:
            video = None
    else:
        video = videos.first()
        
    first_video_id = videos.first().video_id if videos.exists() else None
    
    # Check if video exists before accessing its attributes
    if video and not video.is_preview:
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user=user, course=course)
            except:
                return redirect('checkout', slug=course.slug)

    context = {
        "course": course, 
        "video": video, 
        'videos': videos,
        'first_video_id': first_video_id
    }
    return render(request, template_name="courses/course_page.html", context=context)
'''



'''
def coursePage(request, slug):
    course = get_object_or_404(Course, slug=slug)
    video_id = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")

    if video_id:
        try:
            video = Video.objects.get(id=video_id, course=course)
        except Video.DoesNotExist:
            video = None
    else:
        video = videos.first()
        
    first_video_id = videos.first().video_id if videos.exists() else None
    
    
    # Perform actions that require the video object
    if not video.is_preview:
        if request.user.is_authenticated is False:
            return redirect('login')
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user=user, course=course)
            except:
                return redirect('checkout', slug=course.slug)

    
    context = {
        "course": course, 
        "video": video, 
        'videos': videos,
        'first_video_id': first_video_id
    }
    return render(request, template_name="courses/course_page.html", context=context)
'''


