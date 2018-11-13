from django.shortcuts import render


def link(request):
    request.session['lang'] = 'en'
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'senawebsite/index.html', {"language": language})

    return render(request, 'senawebsite/index.html', {"language": language})

