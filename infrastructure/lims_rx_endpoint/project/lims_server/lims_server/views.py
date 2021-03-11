from django.http import HttpResponse


def welcome(request):
    # return HttpResponse("Hello from LIMS Server")
    return HttpResponse(r"Welcome")
