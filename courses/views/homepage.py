from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from courses.models.course import Course
from courses.models.video import Video
from django.contrib.auth.models import User
from django.db.models import Q

def home(request):
    total_data = Course.objects.filter(active=True).count()
    courses = Course.objects.filter(active=True)[:4]
    video = Video.objects.first()
    
    context = {
        'courses': courses,
        'video': video,
        'total_data': total_data,
        'request': request,  # Include the request object in the context
    }
    return render(request, 'courses/home.html', context)




from django.template.loader import render_to_string

def load_more_data(request):
    offset = int(request.GET.get('offset'))
    limit = int(request.GET.get('limit'))
    courses = Course.objects.filter(active=True)[offset:offset + limit]
    t = render_to_string('courses/course_item.html', {'courses': courses, 'request': request})
    return JsonResponse({'data': t})





def base(request):
    user = User.objects.get(username=request.user)
    return render(request, 'courses/base.html', {'user':user})


def search(request):
    query = request.GET.get("search")
    courses = Course.objects.all()
    if query:
        courses = courses.filter(Q(name__icontains=query)).distinct()

    return render(request, "courses/home.html", {'courses': courses, 'query': query})



def about_us(request):
    return render(request, 'courses/about_us.html')