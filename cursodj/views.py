from django.http import HttpResponse

def hello_django(request):
    return HttpResponse("Chao mundo 3.1.14.")
