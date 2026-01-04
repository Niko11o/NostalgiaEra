from django.shortcuts import render

# Create your views here.


def starter_test(request):
    return render(request, 'music/index.html', )


