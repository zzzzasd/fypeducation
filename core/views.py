from django.shortcuts import render
from .models import Subject, List
from django.shortcuts import render, redirect

# Create your views here.


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'core/subject_list.html', {'subjects': subjects})


def subject_new(request):
    if request.method == "POST"
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.author = request.user
            subject.save()
            return redirect('subject_list', pk=subject.pk)
    else:
        form = SubjectForm()
        return render(request, 'core/subject_list.html', {'form': form})
