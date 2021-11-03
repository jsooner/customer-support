from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .serializers import SubjectsSerializer
from .models import Subjects
from pprint import pprint
from django.core.mail import send_mail

# Create your views here.
# def subjects_list(request):
# 	return render(request, 'subjects/subjects_list.html')

@csrf_exempt
@api_view(['GET'])
def hello (request) :
	subjects = Subjects.objects.all()
	subjects_serial = SubjectsSerializer(subjects, many=True)
	return Response(subjects_serial.data)

# @csrf_exempt
# @api_view(['POST'])
# def createSubject (request) :
# 	print("data" + request.data)
# 	subjects_serial = SubjectsSerializer(data=request.data)
# 	if subjects_serial.is_valid() :
# 		subjects_serial.save()
# 		return Response(subjects_serial.data, status=201)
# 	else :
# 		return Response(subjects_serial.errors, status=400)

class SubjectView(APIView):
	def post(self, request) :
			subjects_serial = SubjectsSerializer(data=request.data)
			if subjects_serial.is_valid() :
				subjects_serial.save()
				send_mail(
					subjects_serial.data['title'],
					subjects_serial.data['body'] + " reply to: " + subjects_serial.data['email'],
					'42KLAUTOMAIL@gmail.com',#from
					['jiongsoon@gmail.com',],#to
					fail_silently=False,
				)
				return Response(subjects_serial.data, status=201)
			else :
				return Response(subjects_serial.errors, status=400)