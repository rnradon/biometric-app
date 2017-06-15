from django.shortcuts import render
from .models import EmergencyContact
from .serializers import EmergencyContactSerializer

from rest_framework.decorators import api_view

from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.




def index(request):
    return HttpResponse("<h1>YO! It's Pizza Time!!</h1>")


@api_view(['GET'])

def emergency_contact_list(request):
    """
    List all queries of the table, or create a new query.
    """

    if request.method == 'GET':
        contacts = EmergencyContact.objects.all()
        serializer = EmergencyContactSerializer(contacts, many=True)
        return Response(serializer.data)

    