from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt

# curl -L -i --form file=@audio.raw http://localhost:8000/upload/
# brew install sox --with-lame --with-flac --with-libvorbis
# sox audiotest.flac --channels=1 --rate 16k --bits 16 audiotest.raw

@csrf_exempt 
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        name = ""
        for filename, file in request.FILES.iteritems():
            name = request.FILES[filename].name
        print(name)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/voicecontrol/'+name)
            # TODO: Send File to STT App
            #return HttpResponse(name + ' uploaded successfully')
            #return render(request, 'voicecontrol', {'audio_file': name})

    else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html', {'form': form})