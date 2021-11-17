from django.http import JsonResponse
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404

from notes.models import *
from .serializers import *

@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            "Endpoint":"/notes/",
            "method":"GET",
            "body":None,
            "description":"Returns an array of notes"
        },
        {
            "Endpoint":"/notes/id",
            "method":"GET",
            "body":None,
            "description":"Returns a single note object"
        },
        {
            "Endpoint":"notes/create/",
            "method":"POST",
            "body":{"body":""},
            "description":"Creates new note with data sent in post request"
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(["GET","POST"])
def getNotes(request):
    if request.method == "GET":
        notes = Note.objects.all().order_by("-updated")
        serializers = NoteSerializer(notes,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

    if request.method == "POST":
        serializers = NoteSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_403_FORBIDDEN)

@api_view(["GET","PUT","DELETE"])
def getNote(request,pk):
    if request.method == "GET":
        note = get_object_or_404(Note,pk=pk)
        serializers = NoteSerializer(note)
        return Response(serializers.data,status=status.HTTP_200_OK)

    if request.method == "PUT":
        note = get_object_or_404(Note,pk=pk)
        serializers = NoteSerializer(note,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_403_FORBIDDEN)

    if request.method == "DELETE":
        note = get_object_or_404(Note,pk=pk)
        note.delete()
        return Response({"message":"Note deleted successfully!"},status=status.HTTP_202_ACCEPTED)

