# formularz metoda post
from django.shortcuts import render, redirect, Http404

TASKS = []


# CRUD _ Create Read Update Delete
# C
def task_create_view(request):
    if request.method == "GET":
        return render(
            request,
            'form_app4/task_form.html',
            {
                'tasks': TASKS
            }
        )
    if request.method == "POST":
        task = request.GET.get('task')
        if task is not None:
            TASKS.append(task)

        return redirect('form_app4:task_list')


# R
def task_list_view(request):
    return render(
        request,
        'form_app4/task_list.html',
        {
            'tasks': TASKS
        }
    )


def task_detail_view(request, task_id):
    if task_id > len(TASKS):
        raise Http404()

    task =TASKS[task_id-1]
    return render(
        request,
        'form_app4/task_detail.html',
        {
            'task_id': task_id,
            'task': task
        }
    )