# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render
from transcribe import transcribe_file

# Create your views here.
def stt(request, audio_file):
    if audio_file == '':
        audio_file = 'audio.raw'
    audio_file = './media/upload/' + audio_file 
    print audio_file

    result = transcribe_file(audio_file)
    return HttpResponse(result)