from django import template
import math

from django.shortcuts import redirect

from courses.models.user_course import UserCourse, Course



register = template.Library()

# 100 -> 10% -> 100 - ( 100 * 10 * 0.01 ) = 90 
@register.simple_tag
def call_sellprice(price, discount):
    try:
        price = float(price)
        discount = float(discount)
    except ValueError:
        # Handle the case where either price or discount is not a valid number
        return price  # or return some default value
        
    if discount == 0:
        return price
    sellprice = price - (price * discount * 0.01)
    return math.floor(sellprice)


@register.filter
def rupee(price):
    return f'${price}'





@register.simple_tag
def is_enrolled(request, course):
    user = None
    if not request.user.is_authenticated:
        return False
    user = request.user
    try:
        user_course = UserCourse.objects.get(user=user, course=course)
        return True
    except:
        return False

