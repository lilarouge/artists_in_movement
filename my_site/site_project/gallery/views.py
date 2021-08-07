from django.shortcuts import render

def Videos_ori(request):
    # videos_ori= Videos_ori.objects.all()

    return render(request, 'ori.html')
