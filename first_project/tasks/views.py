from django.shortcuts import HttpResponse
from datetime import datetime


# Create your views here.
def home_view(request):
    print("request", request)
    return HttpResponse("Hello from Django")


def welcome_page(request):
    return HttpResponse(f"Hello! I'm Arthur, 17 years old, Time is {datetime.now().time()}")
