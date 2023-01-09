from .models import Student_Admission,College
from rest_framework import serializers


class StudentAdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Admission
        fields = ['id','student_id', 'student_age', 'student_name', 'student_email', 'student_amount', 'student_address','college_id']

class studentCollegeName(serializers.ModelSerializer):
    class Meta:
        model = College
        fields=['college_id','college_name','college_address']