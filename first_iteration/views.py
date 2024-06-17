

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from first_iteration.models import DataForANRP
from main import main_function

def index(request):
    return render(request, 'first_iteration/index.html')

def index_page(request):
    all_workers = DataForANRP.objects.all()
    return render(request, 'first_iteration/index.html')


def about_page(request):
    return render(request, 'first_iteration/index.html')

def process_data(request):
    if request.method == 'POST':
        # Получаем данные из формы
        date = request.POST.get('date')
        hour_start = request.POST.get('hour_start')
        hour_end = request.POST.get('hour_end')
        camera_number = request.POST.get('camera_number')

        result = main_function(date, hour_start, hour_end, camera_number)

        return HttpResponse(result)
    else:
        # Если метод не POST, перенаправляем обратно на главную страницу
        return redirect('first_iteration/index.html')
