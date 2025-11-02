from django.shortcuts import render, get_object_or_404
from .models import Profession,Presentations, EngineeringProcessesAtaps, EngineeringProcessesTitle
from django.http import HttpResponse, Http404, FileResponse
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required



@login_required
def vibor(req):
    return render(req, 'profession/profession_vibor.html')

@login_required
def engineering_processes_index(req):
    eng_ataps=EngineeringProcessesAtaps.objects.all()
    eng_proc = EngineeringProcessesTitle.objects.all()
    eng_proc_or_ataps= {
        'eng_proc':eng_proc,
        'eng_ataps':eng_ataps
    }
    return render(req, 'profession/engineering_processes_index.html', eng_proc_or_ataps)

@login_required
def engineering_processes(req, post_slug):
    professions = Profession.objects.all()
    eng_a=get_object_or_404(EngineeringProcessesAtaps, slug=post_slug)
    data={
        'eng_a': eng_a,
        'professions': professions
    }
    return render(req, 'profession/engineering_processes.html', data )

@login_required
def show_post(req,post_slug):
    post=get_object_or_404(Profession, slug=post_slug)
    return render(req,'profession/show_post.html', {'post': post})

@login_required
def presintations_list(req):
    presintations=Presentations.objects.all()
    return render(req, 'profession/presintations_list.html', {'presintations':presintations})

@login_required
def download_presentation_file(request, pk):
    try:
        pres = Presentations.objects.get(pk=pk)
        file_path = pres.file.path
        if not os.path.exists(file_path):
            raise Http404("Файл не найден")
        response = FileResponse(
            open(file_path, 'rb'),
            content_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            as_attachment=True,
            filename=pres.file.name.split("/")[-1]
        )
        return response

    except Presentations.DoesNotExist:
        raise Http404("Презентация не найдена")

@login_required
def download_presentation_file_met(request, pk):
    try:
        pres = Presentations.objects.get(pk=pk)
        file_path = pres.file_met.path
        if not os.path.exists(file_path):
            raise Http404("Файл не найден")

        response = FileResponse(
            open(file_path, 'rb'),
            content_type="application/pdf",
            filename=pres.file_met.name.split("/")[-1]
        )
        return response

    except Presentations.DoesNotExist:
        raise Http404("Презентация не найдена")
