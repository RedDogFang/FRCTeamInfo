from django.shortcuts import render
from django.http import HttpResponse

from .models import Message

def example_endpoint(request):
    # Retrieve the first message stored in the database
    message = Message.objects.first()
    content = f"<div>{message.content}</div>" if message else "<div>No message found.</div>"
    return HttpResponse(content)


# Create your views here.
def index(request): 
    return render(request, 'myapp/index.html')
