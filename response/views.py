from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import Response as SubjectResponse
from .serializers import ResponseSerializer as SubjectResponseSerializer
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ReponseView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		responses = SubjectResponse.objects.all()
		response_serial = SubjectResponseSerializer(responses, many=True)
		return Response(response_serial.data)

	def post(self, request):
		response = request.data
		response_serial = SubjectResponseSerializer(data=response)

		if response_serial.is_valid():
			response_serial.save()
			send_mail(
				response_serial.data['title'],
				response_serial.data['body'] + f"\n rating link: http://localhost:5000/rate/{response_serial.data['subjectID']}",
				'42KLAUTOMAIL@gmail.com',#from
				[response_serial.data['to_email'],],#to
				fail_silently=False,
			)
			return Response(response_serial.data, status=204)
		else :
			return Response({"error" : response_serial.errors}, status=400)