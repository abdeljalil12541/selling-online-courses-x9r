from django.contrib import admin
from django.urls import include, path
from courses.views import coursePage, home,search, SignupView, LoginView, logoutfunc, checkout, checkout_session, pay_success, pay_cancel, my_courses, load_more_data, about_us, contact_us, dashboard
from courses.views import user_courses_dash, my_orders, update_profile, password_change, my_contact_history, privacy_policy
from django.conf import settings
from django.conf.urls.static import static
from sellCoursesOnline.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL

urlpatterns = [
    path('', home, name='home'),
    path('about-us', about_us, name='about_us'),
    path('contact-us', contact_us, name='contact_us'),
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', logoutfunc, name="logout"),
    path('password-change/', password_change, name="password_change"),
    path('my-courses', my_courses, name="my_courses"),
    path('course/<str:slug>/', coursePage, name='coursepage'),
    path('load-more-data', load_more_data, name='load_more_data'),
    path('checkout/<str:slug>/', checkout, name='checkout'), # check-out
    path('checkout_session/<str:slug>/', checkout_session, name='checkout_session'),
    path('pay_cancel/', pay_cancel, name='pay_cancel'),
    path('pay_success/', pay_success, name='pay_success'),
    path('courses/', search, name='search'),
    path('dashboard/', dashboard, name='dashboard'),
    path('user-courses-dash/', user_courses_dash, name='user_courses_dash'),
    path('my-orders/', my_orders, name='my_orders'),
    path('update-profile/', update_profile, name='update_profile'),
    path('my-contact-history/', my_contact_history, name='my_contact_history'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)


urlpatterns += static(STATIC_URL, document_root=settings.STATIC_ROOT)