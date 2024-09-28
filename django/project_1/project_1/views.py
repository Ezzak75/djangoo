from django.http import HttpResponse
def home(request):
     return HttpResponse("this is homepage")
    
def contact(request):
    return HttpResponse("this is contact page")