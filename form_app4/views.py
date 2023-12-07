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

def task_update_view(request, task_id):
    if task_id > len(TASKS):
        raise Http404()


    if request.method == "GET":
        task = TASKS[task_id - 1]

        return render(
            request,
            'form_app4/task_update.html',
            {
                'task_id': task_id,
                'task': task
            }
        )

    if request.method == "POST":
        new_task = request.POST.get('task')
        if new_task is not None:
            TASKS[task_id-1] = new_task

# d z crud delete
def task_delete_view(request, task_id):
    if task_id > len(TASKS):
        raise Http404()

    if request.method == "GET":
        task = TASKS[task_id - 1]

        return render(
            request,
            'form_app4/task_delete.html',
            {
                'task_id': task_id,
                'task': task
            }
        )

    elif request.method == "POST":
        data = request.POST
        if 'yes' in data:
            TASKS.pop(task_id - 1)

        return redirect('form_app4:task_list')