from django.shortcuts import render

from app.models import CowsayModel


# Create your views here.
def index(request):
    # data = CowsayModel.objects.all()
    return render(request, 'index.html')


def history_view(request):
    return render(request, 'history.html')
