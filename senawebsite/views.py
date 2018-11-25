from django.shortcuts import render


def link(request):
    from django.core.management import call_command
    call_command("migrate", interactive=False)
    request.session['lang'] = 'en'
    language = 'en'
    if request.method == 'POST':
        request.session['lang'] = request.POST.get('selector')
        language = request.POST.get('selector')
        return render(request, 'senawebsite/index.html', {"language": language})

    return render(request, 'senawebsite/index.html', {"language": language})

