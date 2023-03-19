from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework import JSONParser
from rest_framework import status

from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializers
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_details(request, pk):
    # find tutorial by pk (id)
    try:
        tutorial = Tutorial.objects.get(pk=pk)
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    #  GET / PUT / DELETE tutorial


# @api_view(['GET'])
# def tutorial_list_published(request):
#     # GET all published tutorials

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    # retrieve objects (with condition)
    # retrieve all Tutorials / find by title from PostgreSQL database
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializers = TutorialSerializers(tutorials, many=True)
        return JsonResponse(tutorials_serializers.data, safe=False)
        # 'safe=False' for objects serializeation

    # create a new object
    # create and save a new Tutorial
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializers(data=tutorial_data)
        if (tutorial_serializer.is_valid()):
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
