from django.db import models
from django.urls import reverse

from random import choices
from string import ascii_uppercase
from pathlib import Path
from loguru import logger

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *

BASE_DIR = Path(__file__).resolve().parent.parent

def genetate_unique_code():

        length = 6

        while True:
            code = ''.join(choices(ascii_uppercase, k=length))
            if Video.objects.filter(code=code).count() == 0:
                break

        return code


class Video(models.Model):

    code = models.CharField(verbose_name='code of video', default=genetate_unique_code, max_length=8, unique=True)
    file = models.FileField(upload_to='final_videos',null=True)

    def get_absolute_url(self):
        return reverse('', kwargs={'code': self.code})
    
    def __str__(self):
        return self.code
    
    @staticmethod
    def generate(name: str):

        
        code = genetate_unique_code()

        processed_video_file_path = f'{BASE_DIR}\\media\\processed_videos\\{code}.mp4'
        source_video_file_path = f'{BASE_DIR}\\media\\source_videos\\example vid.mp4'
        text_to_input = name + " hello!"

        logger.info(f"Started clip generation. Code:{code}. Text: {text_to_input}")
        # Load the video clip
        clip = VideoFileClip(source_video_file_path)

        # Define a function to add text to a single frame
        txt_clip = TextClip(text_to_input, fontsize=140, color='red', font='Arial')
        txt_clip = txt_clip.set_pos('center')

        # Define the output video settings
        fps = clip.fps

        final_clip = CompositeVideoClip([clip, txt_clip])
        final_clip.duration = clip.duration
        final_clip.write_videofile(processed_video_file_path, fps=fps, threads=4)

        logger.info(f"Ended clip generation. Code:{code}.")

        video = Video(code=code, file=processed_video_file_path)
        video.save()
        logger.info(f"Clip {code} was saced to db.")

        return video

