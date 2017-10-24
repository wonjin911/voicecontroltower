# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

from django.shortcuts import render
from .transcribe import transcribe_file
import requests, json
import subprocess

# Create your views here.
def stt(request, file_id):
    if file_id == '':
        return HttpResponse('no file_id')

    audio_file = './media/upload/%s.wav' % file_id
    audio_raw = './media/upload/%s.raw' % file_id

    wav2raw(audio_file, audio_raw)

    tts_text = transcribe_file(audio_raw)
    print(tts_text)
    #tts_text='하드캐리'
    response = sendDialogflow(tts_text)
    print(response)

    result = {'request': tts_text, 'response': response}
    #result='테스트입니다'
    return JsonResponse(result)

def wav2raw(audio_file, out_file):
    #ffmpeg -i 21.wav -f s16le -acodec pcm_s16le out.raw
    subprocess.call(['ffmpeg', '-y', '-i', audio_file, '-f', 's16le', \
        '-acodec', 'pcm_s16le', out_file])

def sendDialogflow(user_text):
    #PAGE_ACCESS_TOKEN = 'INSERT_FACEBOOK_PAT'
    #VERIFY_TOKEN = 'INSERT_TOKEN'

    CLIENT_ACCESS_TOKEN='Bearer 35ae8ccb368f4223b878a31f7180023a'
    url = 'https://api.dialogflow.com/v1/query'
    query = user_text
    params = {'query': query, 'sessionId': '12321', 'lang': 'ko', 'v':'20170712'}
    headers = {'Authorization': CLIENT_ACCESS_TOKEN}
    response = requests.request("GET", url, headers=headers, params=params).json()

    responseStatus = response['status']['code']

    if (responseStatus == 200):
        return (response['result']['fulfillment']['speech'])
    else:
        return ("Sorry, I couldn't understand that question")
