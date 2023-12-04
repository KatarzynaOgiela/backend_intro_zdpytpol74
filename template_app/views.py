from django.shortcuts import render
from datetime import datetime

def isitnewyear(request):
    now = datetime.now()
    if now.month == 1 and now.day == 1:
        result = "TAK"
    else:
        result = "NIE"

    return render(
        request,
        'is_it_new_year.html',
        {
            'result' :result
        }
    )