from .homepage import home, search, load_more_data, about_us
from .courses import coursePage, my_courses
from .auth import SignupView, LoginView, logoutfunc, password_change
from courses.views.checkout import checkout, checkout_session, pay_success, pay_cancel
from courses.views.contact_us import contact_us
from courses.views.dashboard import dashboard, user_courses_dash, my_orders, update_profile, my_contact_history, privacy_policy