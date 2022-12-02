from django.shortcuts import HttpResponse
from datetime import datetime


# Create your views here.

def greeting(request):
    return HttpResponse("Hello there!")


def introduction(request):
    return HttpResponse("I'm Arthur, 17 years old. Just finished my exams and finally can do my courses.")


def current_date(request):
    return HttpResponse(f"So it's {datetime.now()}")


def square_keys(request):

    sample_dict = {}

    for i in range(1, 16):
        sample_dict[i] = i**2
    return HttpResponse(f"Here are squares of keys: {sample_dict}")
