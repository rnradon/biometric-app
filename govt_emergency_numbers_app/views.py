from django.shortcuts import render
from .models import GovtEmergencyContact
from .serializers import GovtEmergencyContactSerializer

from rest_framework.decorators import api_view

from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.




def index(request):
    return HttpResponse("<h1>YO! It's Pizza Time!!</h1>")


@api_view(['GET'])

def govt_emergency_contact_list(request):
    """
    List all queries of the table, or create a new query.
    """

    if request.method == 'GET':
        contacts = GovtEmergencyContact.objects.all()
        serializer = GovtEmergencyContactSerializer(contacts, many=True)
        return Response(serializer.data)

    