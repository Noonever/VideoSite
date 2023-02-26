from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateVideoForm
from .models import Video
from django.http import HttpResponseNotFound
from pathlib import Path

processed_videos_path = Path("processed_videos")

def start_page_view(request):

    form = CreateVideoForm()

    context = {'form': form, 'text': 'YOUR NAME'}

    if request.method == "POST":
        form = CreateVideoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            video = Video.generate(name=name)
            code = video.code
            return redirect(f'{code}/')
    else:
        form = CreateVideoForm()

    return render(request, 'start_page.html', context)

def video_view(request, code):


    _requested_video = Video.objects.filter(code=code)

    if not _requested_video:
        return HttpResponseNotFound('lol') #  TODO make an error 404 page

    context = {'video_path': _requested_video}

    return render(request, 'video_template.html', context)
