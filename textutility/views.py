# Text Analyzation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def error(request):
    return render(request, 'error.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    #CHECK CHECKBOX value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numberofcharacter = request.POST.get('numberofcharacter', 'off')

    #which checkbox is on
    if removepunc == "on":
        punctuations = '''()-[]~`!@#$%^&*_=+}{\|/>.?<,:;'"'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    #capitalization
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    #lower case
    if lowercase =="on":
        analyzed=""
        for char in djtext:
            analyzed =analyzed + char.lower()
        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    #new line remover
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove Newlines', 'analyzed_text': analyzed}
        djtext = analyzed

    #number of character
    if numberofcharacter == "on":
        analyzed = 0
        c = 0
        for index, char in enumerate(djtext):
            if djtext[index] == " ":
                c = c + 1
            analyzed = len(djtext) - c
        params = {'purpose': 'Number of Characters', 'analyzed_text': f'Number of Characters {analyzed}'}
        djtext = analyzed

    #extra space remover
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
    if (extraspaceremover != "on" and numberofcharacter != "on" and newlineremover != "on" and fullcaps != "on" and lowercase !="on" and removepunc != "on"):
        return render(request, 'error.html')

    return render(request, 'analyze.html', params)

def searchbar(request):
    post = ""
    djtext = request.POST.get('text', 'default')
    if request.method == 'get':
        searchbar = request.GET.get('searchbar')
        for index, char in enumerate(djtext):
            if char == djtext[index]:
                post = post + djtext
        params = {'purpose': 'Searching Character', 'analyzed_text': post}
        return render(request, 'analyze.html', params)