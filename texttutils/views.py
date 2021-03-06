#I have Created this File - DINAKAR
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return   render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')

    #Check checkbox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

    #Check which checkbox in on
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed  = analyzed + char     
        params = {'purpose':'Removed Punctuations','analyazed_text': analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'change to uppercase','analyazed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'Remove New Lines','analyazed_text': analyzed}
        djtext = analyzed
    

    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char           
        params = {'purpose':'Extra Space Remover','analyazed_text': analyzed}
       
    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("Please Select any operation and try again..!")
 
    return render (request, 'analyze.html',params )     




