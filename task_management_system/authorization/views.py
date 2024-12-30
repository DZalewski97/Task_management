from django.contrib.auth.hashers import check_password
from django.core.serializers import serialize
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Serializer import PeopleSerializer
from .models import People
from django.shortcuts import render


@api_view(['GET'])
def people_list(request):
    people = People.objects.all()
    return Response(list(people.values()), status=status.HTTP_200_OK)


@api_view(['GET'])
def find_id(request, pk):
    people = get_object_or_404(People, pk=pk)
    people_dict = model_to_dict(people)
    print(people_dict)
    return Response(people_dict, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_new_people(request):
    people = People.objects.create(name='johnny', password='johnny')
    serializer = PeopleSerializer(people)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete_people(request, pk):
    people = get_object_or_404(People, pk=pk)
    people.delete()
    return Response({'ok'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def registration_confirm(request):
    login = request.data.get('login')
    password = request.data.get('password')

    print(f"Received data - Login: {login}, Password: {password}")

    people = People.objects.create(name=login, password=password)
    serializer = PeopleSerializer(people)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


def registration(request):
    return render(request, 'Registration_page.html')

@api_view(['POST'])
def login_check(request):
    login = request.POST.get('login')
    password = request.POST.get('password')
    all_people = People.objects.all()
    common_user = get_object_or_404(People, name=login, password=password)

    if not login or not password:
        return JsonResponse({"detail": "Login and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # user = get_object_or_404(People, name=login)
        user = People.objects.get(name=login)
    except People.DoesNotExist:
        return JsonResponse({"detail": "Invalid login or password."}, status=status.HTTP_400_BAD_REQUEST)

    if user.password != password:
        return JsonResponse({"detail": "Invalid loginn or password."}, status=status.HTTP_400_BAD_REQUEST)

    return render(request, 'Main_page.html', {'all_people': all_people, 'common_user': common_user})


def login(request):
    return render(request, 'Login.html')
