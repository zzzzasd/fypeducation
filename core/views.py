from django.shortcuts import render
from .models import Subject, List
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from core.models import User
from core.serializers import UserSerializer, SignUpSerializer, SignInSerializer
from core.permissions import IsAuthenticatedOrCreate
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from .forms import SubjectForm
from rest_framework.authentication import BasicAuthentication
# Create your views here.


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'core/subject_list.html', {'subjects': subjects})


def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    return render(request, 'core/subject_detail.html', {'subject': subject})


def subject_publish(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.publish()
    return redirect('subject_detail', pk=pk)


def subject_new(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            return redirect('subject_detail', pk=subject.pk)
    else:
        form = SubjectForm()
        return render(request, 'core/subject_edit.html', {'form': form})


@csrf_exempt
def user_list(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(User)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)


class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

class SignIn(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = SignInSerializer
    authentication_classes = (BasicAuthentication,)


