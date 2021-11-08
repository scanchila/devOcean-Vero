from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/users/login/')
def getRecommendation(request):
    if request.method == 'GET':
        print("rec")
        recommendation = recomendacion.objects.all()
        context = {
            'recomendaciones': recommendation
        }
        return render(request, 'recomendaciones/index.html', context=context)
    return render(request, 'recomendaciones/index.html')
