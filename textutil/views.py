# this file created by me

from email.policy import default
from operator import le
import re
from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
    # third parameter of render is a dictionary of key valur pairs
    return render(request, 'index.html')
#return HttpResponse("Working.........;)")


def failed(request):
    return render(request, 'failed.html')
    
def analyze(request):
    # third parameter of render is a dictionary of key valur pairs
    text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    removextraspace = request.POST.get('removextraspace', 'off')
    removeextraline = request.POST.get('removeextraline', 'off')

    puncs = '''~`!@#$%^&*()-+=_{}[]|\;:"',<.>?/'''
    analyzed = ""

    wordcount = len(re.findall(r'\w+', text))

    if removepunc == "on":
        for char in text:
            if char not in puncs:
                analyzed = analyzed + char

        params = {'purpose':'Result...', 'analyzed_text': analyzed, 'word_count': wordcount}
        text = analyzed

    if uppercase == "on":
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Result...', 'analyzed_text': analyzed, 'word_count': wordcount}
        text = analyzed

    if removextraspace == "on":
        analyzed = ""
        analyzed = " ".join(text.split())

        params = {'purpose': 'Result...', 'analyzed_text': analyzed, 'word_count': wordcount}
        text = analyzed

    if (removeextraline == "on"):
        analyzed = ""
        for char in text:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Result...', 'analyzed_text': analyzed, 'word_count': wordcount}

    if(removepunc != "on" and removeextraline!="on" and removextraspace!="on" and uppercase!="on"):
        return failed(request)
        #return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)