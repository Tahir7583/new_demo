from rest_framework.response import Response
from .models import*
from .serializers import *
from rest_framework import viewsets 



# Create your views here.

class recuritorViewset(viewsets.ModelViewSet):    #combine CRUD operation using viewset
    queryset=Recruiters.objects.all()
    serializer_class=RecruiterSerializer 



class recuritor_education(viewsets.ModelViewSet):    #combine CRUD operation using viewset
    queryset=Recruiter_Education.objects.all()
    serializer_class=Recruiter_EducationSerializer 
    
