from django.shortcuts import render, get_object_or_404
from .models import Profession,Presentations, Engineering_Processes
from django.http import HttpResponse, Http404
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required



@login_required
def vibor(req):
    return render(req, 'profession/profession_vibor.html')

@login_required
def engineering_processes_index(req):
    eng_proc=Engineering_Processes.objects.all()
    return render(req, 'profession/engineering_processes_index.html', {'eng_proc':eng_proc} )

@login_required
def engineering_processes(req, post_slug):
    eng_proc=get_object_or_404(Engineering_Processes, slug=post_slug)
    return render(req, 'profession/engineering_processes.html', {'eng_proc':eng_proc} )

@login_required
def profession_index(req):
    professions=Profession.objects.all()
    return render(req, 'profession/profession_index.html', {'professions':professions})

@login_required
def show_post(req,post_slug):
    post=get_object_or_404(Profession, slug=post_slug)
    return render(req,'profession/show_post.html', {'post': post})

@login_required
def presintations_list(req):
    presintations=Presentations.objects.all()
    return render(req, 'profession/presintations_list.html', {'presintations':presintations})

@login_required
def download_presentation(request, pk):
    try:
        pres = Presentations.objects.get(pk=pk)
        file_path = pres.file.path
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.presentationml.presentation")
                response['Content-Disposition'] = f'attachment; filename="{pres.file.name.split("/")[-1]}"'
                return response
        else:
            raise Http404("Файл не найден")
    except Presentations.DoesNotExist:
        raise Http404("Презентация не найдена")
