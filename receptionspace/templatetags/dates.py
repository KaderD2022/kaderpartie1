from datetime import datetime
from django import template

register = template.Library()

@register.filter
def age(birthday:datetime, today=datetime.today().date()):
    age = today-birthday
    return round(age.days/365)