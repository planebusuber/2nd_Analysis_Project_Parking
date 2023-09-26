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
    path("transportation/transportation_illegal/", views.trans_ill),
    path("transportation/public_illegal/", views.public_ill),
    path("transportation/gu_trans_illegal/", views.gu_trans_ill),
    path("transportation/parking_illegal/", views.count_ill),
    # path("transportation/parking_transportation/", views.count_trans),
    path("weather_corr/", views.weather_corr),
    path("weather_corr/4_1/", views.weather_corr4_1),
    path("weather_corr/4_2/", views.weather_corr4_2),
    path("weather_corr/4_3/", views.weather_corr4_3),
    path("weather_corr/4_4/", views.weather_corr4_4),
    path("reference/",views.reference),
    path("parking_expose/", views.parking_expose),
    path("parking_expose_corr_map/", views.parking_expose_corr_map),
    path("solution_plan/", views.solution_plan)
]