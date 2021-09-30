from django.shortcuts import get_object_or_404
from .forms import HowDoYouFeel

def getInfoForm(request):
    formInst = get_object_or_404()
