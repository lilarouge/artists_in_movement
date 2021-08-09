from django.shortcuts import render

def Videos_ori(request):
    return render(request, 'ori.html')

def Videos_grisha(request):
    return render(request, 'grisha.html')

def Videos_inbar(request):
    return render(request, 'inbar.html')

def Videos_sonia(request):
    return render(request, 'sonia.html')

def Videos_lila(request):
    return render(request, 'lila.html')