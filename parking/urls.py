from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing),
    path("statistic_list/", views.statistic),
    path("seoul_map/",views.seoul_map),
    path("contents/", views.contents),
    path("parking_count_detail_list/", views.parking_count_detail_list),
    path("parking_count_map/", views.parking_count_map),
    path("seoul_circle/", views.seoul_circle),
    path("parking_expose_corr/", views.parking_expose_corr),
    path("parking_expose_corr_detail_list/",views.parking_expose_corr_detail_list),
    path("transportation/", views.transportation),
    path("weather_corr/", views.weather_corr),
<<<<<<< HEAD
    path("reference/",views.reference),

=======
    path("weather_corr/4_1/", views.weather_corr4_1),
    path("reference/",views.reference)
>>>>>>> geon01
]