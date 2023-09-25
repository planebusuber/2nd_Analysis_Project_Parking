from django.shortcuts import render
# Create your views here.



def landing(request):
    return render(request, template_name = "parking/single_page.html")

def statistic(request):
    return render(request, template_name = "parking/statistic_list.html")

def seoul_map(request):
    return render(request, template_name = "parking/seoul_map.html")

def contents(request):
    return render(request, template_name = "parking/contents.html")

def parking_count_map(request):
    return render(request, template_name = "parking/parking_count_map.html")

def parking_expose_corr(request):
    return render(request, template_name = "parking/parking_expose_corr.html")

def transportation(request):
    return render(request, template_name = "parking/transportation.html")

def weather_corr(request):
    return render(request, template_name = "parking/weather_corr.html")

def reference(request):
    return render(request, template_name = "parking/reference.html")
