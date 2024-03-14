from django.contrib import admin

from .models.course import Course, CourseProperty, Tag, Prerequisite, Learning
from .models.video import Video
from .models.user_course import UserCourse
from .models.payment import Payment
from .models.contact_us import ContactUs
from django.utils.html import format_html


# Register your models here.


class TagAdmin(admin.TabularInline):
    model = Tag
    
class VideoAdmin(admin.TabularInline):
    model = Video
    
class LearningAdmin(admin.TabularInline):
    model = Learning
    
class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite
    
class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearningAdmin, PrerequisiteAdmin, VideoAdmin]
    list_display = ["name", 'get_price', "get_discount", 'active']
    list_filter = ["discount", "active"]
    
    def get_discount(self, course):
        return f'{course.discount}%'
    
    def get_price(self, course):
        return f'${course.price}'
    
    get_discount.short_description = "Discounnt"
    get_price.short_description = "Price"
    
    
class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ('payment_id', 'get_user', 'get_course', 'status')
    list_filter = ['status', 'course']
    
    def get_user(self, payment):
        return format_html(f'<a target="_blank" href="/admin/auth/user/{payment.user.id}"><strong>{payment.user}</strong></a>')
    
    def get_course(self, payment):
        return format_html(f'<a target="_blank" href="/admin/courses/course/{payment.course.id}"><strong>{payment.course}</strong></a>')
    
    get_user.short_description = "User"
    get_course.short_description = "Course"
    
    
    
    
class UserrCourseAdmin(admin.ModelAdmin):
    model = UserCourse
    list_display = ('click', 'get_user', 'get_course')
    list_filter = ['course']
    
    def get_user(self, usercourse):
        return format_html(f'<a target="_blank" href="/admin/auth/user/{usercourse.user.id}"><strong>{usercourse.user}</strong></a>')
    
    def click(self, usercourse):
        return "Click to Open"
    
    def get_course(self, usercourse):
        return format_html(f'<a target="_blank" href="/admin/courses/course/{usercourse.course.id}"><strong>{usercourse.course}</strong></a>')
    
    get_user.short_description = "User"
    get_course.short_description = "Course"
    
    
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'message']
    
    
admin.site.register(Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(UserCourse, UserrCourseAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(ContactUs, ContactUsAdmin)