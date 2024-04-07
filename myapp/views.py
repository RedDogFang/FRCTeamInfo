from django.shortcuts import render
from django.http import HttpResponse

def example_endpoint(request):
    # This is the content that will be inserted into the HTML page.
    content = "<div>This content was loaded with HTMX!</div>"
    return HttpResponse(content)


# Create your views here.
def index(request): 
    return render(request, 'myapp/index.html')
