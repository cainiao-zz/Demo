from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'uploadfile.html')


def handle_file(request):
    img_data = request.FILES()
    print(img_data)
    return HttpResponse('ok')