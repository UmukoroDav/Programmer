from django.shortcuts import render
from django.shortcuts import redirect
from .models import Details
from .models import API
from django.http import Http404
from django.http import HttpResponse
from rest_framework import generics
from .serializer import APISerializers
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import requests

# Create your views here.

def appindex(request):
    details = Details.objects.all()
    context = {'key' : details}
    return render (request, 'index.html', context)

def appregistration(request):
    # return HttpResponse('<h1>Registration Page</h1>')
    return render(request, 'registration.html')

def appquery(request):
    # return HttpResponse('<h1>Query Page</h1>')
    return render(request, 'query.html')

def appinfo(request):
    # return HttpResponse('<h1>Info Page</h1>')
    return render(request, 'info.html')

def appsignup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login = (request, user)
            return redirect('appindex')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form' : form})

def appcontact(request, pr):
    try:
        std = API.objects.get(Pk = pr)
        stad = {'keys':std}
    except API.DoesNotExist:
        raise Http404()
    return render(request, 'contact.html', stad)
    
class appStudentcrateveiw(generics.ListCreateAPIView):
    display = API.objects.all()
    queryset = API.objects.all()
    convert = APISerializers
    serializer_class = APISerializers
    
class APIind(generics.RetrieveUpdateAPIView):
    value = API.objects.all()
    serializer_class = APISerializers
    queryset = API.objects.all()
     
    
def appprivate(request):
    if not request.user.is_authenticated:
        return redirect('appsignup')
    else:
        return render(request, 'private.html')

# class RestApiVeiw(APIView):
#     def appdisplayresr(self, request):
#         std = API.objects.filterg()
#         serializer = APISerializers(std, many=True)
#         return render(request, 'index.html', {'key' : serializer.data})


def RestApiVeiw(request):
    response = requests.get('http://127.0.0.1:8000/members/display/?format=json').json()
    return render(request, 'contact.html', {'tab': response})