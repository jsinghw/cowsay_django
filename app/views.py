from django.shortcuts import render

from app.models import CowsayModel
from app.forms import CowsayForm

from subprocess import run


def index(request):
    html = "index.html"
    output = ''

    if request.method == "POST":
        form = CowsayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowsayModel.objects.create(
                text=data['text']
            )
            output = run(['cowsay', data["text"]], capture_output=True).stdout
            output = output.decode('utf-8')
    form = CowsayForm()
    return render(request, html, {'form': form, 'output': output})


def history_view(request):
    data = []
    cowOutput = CowsayModel.objects.all()
    for i in cowOutput:
        data.append(i)
    data = data[-10:][::-1]
    return render(request,
                  'history.html',
                  {'data': data}
                  )
