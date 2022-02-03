from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def hello(request):
    html = '''
        <h1>
            <center>
                Hello World, my name is Shubham
            </center>
        </h1>
    '''
    return HttpResponse(html)