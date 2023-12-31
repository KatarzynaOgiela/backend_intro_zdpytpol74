from django.shortcuts import render


def first_view(request):
    return render(
        request,
        'first.html'
    )


def second_view(request):
    return render(
        request,
        'second.html'
    )


def third_view(request, param):
    return render(
        request,
        'third.html',
        {
            'param': param
        }
    )
