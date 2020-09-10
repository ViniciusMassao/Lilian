from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from lilian.forms import HomeForm
from lilian.LilianPhrasesBased import main
import os

# Create your views here.
def myView(request):
    if request.method == 'POST':
        form = HomeForm(request.POST or None)
        if form.is_valid():
            phrase = ""
            answer = form.cleaned_data.get('tema')
            answer = int(answer)
            phrase = main(answer)
            args = {'form':form, 'phrase':phrase}
            return render(request, 'home/home.html',args)
    else:
        form = HomeForm()
        phrase = ""
        return render(request, 'home/home.html',{'form':form})
