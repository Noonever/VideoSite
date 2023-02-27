from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateVideoForm
from .models import Video
from loguru import logger

def start_page_view(request):

    logger.info("Start page visited")

    form = CreateVideoForm()

    if request.method == "POST":
        form = CreateVideoForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            logger.info(f'Form filled. Input: {name}')
            video = Video.generate(name=name)
            code = video.code

            return redirect(f'{code}/')
    else:
        form = CreateVideoForm()

    return render(request, 'start_page.html', {'form': form})


def video_view(request, code):

    logger.info(f"Video page visited. Code: {code}.")

    requested_video = Video.objects.filter(code=code)

    if not requested_video:
        logger.error(f'No such video with code: {code}. Redirecting to start page.')
        return redirect('start_page')

    context = {'videos': requested_video}

    return render(request, 'video_template.html', context)
