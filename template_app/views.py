from django.shortcuts import render
from datetime import datetime

def isitnewyear(request):
    now = datetime.now()
    if now.month == 12 and now.day == 5:
        is_new_year = True
    else:
        is_new_year = False
    return render(
        request,
        'is_it_new_year.html',
        {
            'is_new_year': is_new_year
        }
    )


def template_view(request):
    fruits = [
        'apple',
        'banana',
        'cherry'
    ]
    user = {
        'name': "John",
        'surname': "DOE",
        'age': 10
    }

    class Cow:
        def __init__(self, name):
            self.name = name

    cow = Cow("Mucia")
    return render(
        request,
        'template.html',
        {
            'fruits': fruits,
            'user': user,
            'cow': cow
        }
    )