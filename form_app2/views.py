# formularz metoda GET
from django.shortcuts import render

TASKS = []

def task_create_view(request):

    task = request.GET.get('task')
    if task is not None:
        TASKS.append(task)

    return render(
        request,
        'form_app2/task_form.html',
        {
            'task':TASKS
        }
    )
