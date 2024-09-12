
from rest_framework import serializers
from .models import *


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recruiters
        fields='__all__'
        depth=1



class Recruiter_EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recruiter_Education
        fields='__all__' 
        depth=1

