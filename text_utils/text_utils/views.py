from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    given_text = request.POST.get('text', '')
    removepunc = request.POST.get('removepunc_opp', 'off')
    upper = request.POST.get('uppercase', 'off')
    lower = request.POST.get('lowercase', 'off')
    line_remover = request.POST.get('lineremove', 'off')
    space_remover = request.POST.get('sapceremove', 'off')
    text_length = request.POST.get('Noofchars', 'off')
    analyzed = ''
    operations = ''
    org_len = 0
    ana_len = 0

    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        operations += '+Removed Punctuations marks'
        for char in given_text:
            if char not in punctuations:
                analyzed = analyzed + char


    if upper == 'on':
        operations += '+Converted Into Upper Case'
        if analyzed == '':
            analyzed = given_text.upper()
        else:
            analyzed = analyzed.upper()


    if lower == 'on':
        operations += '+Converted Into Lower Case'
        if analyzed == '':
            analyzed = given_text.lower()
        else:
            analyzed = analyzed.lower()

    if line_remover == 'on':
        operations += '+Removed New Lines'
        if analyzed == '':
            analyzed = ''.join([char for char in given_text if char not in '\n\r'])
        else:
            analyzed = ''.join([char for char in analyzed if char not in '\n\r'])

    if space_remover == 'on':
        operations += '+Removed Extra Spaces'
        if analyzed == '':
            analyzed = ' '.join(given_text.split())
        else:
            analyzed = ' '.join(analyzed.split())

    if text_length == 'on':
        operations += '+No.of Characters'
        org_len = len(given_text)
        ana_len = len(analyzed)

    if operations != '':
        data_dict = {'operations': operations, 'Analyzed_text': analyzed, 'given_text': given_text, 'org_len': org_len,
                     'ana_len': ana_len}
        return render(request, 'analyze.html', data_dict)
    else:
        return HttpResponse("<p>Please check the option............!</p><a href='/' style = 'border : 1px solid #000'> Back </a>")

