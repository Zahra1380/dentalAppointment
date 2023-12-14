from django import template
from doctor.models import Doctor

register = template.Library()

x, y, z = 0, 1, 2


@register.filter
def delay(num):
    global x, y, z
    num = num['counter0']
    if x == num:
        x += 3
        return '0.3s'

    elif y == num:
        y += 3
        return '0.6s'

    else:
        z += 3
        return '0.1s'


@register.filter
def rate(doctor):
    rate = Doctor.objects.get(id=doctor).star_rate.all()
    sum_ = 0
    for item in rate:
        sum_ += item.score
    return sum_ // rate.count()
