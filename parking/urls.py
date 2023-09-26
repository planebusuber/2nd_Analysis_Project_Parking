from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing),
    path("statistic_list/", views.statistic),
    path("seoul_map/",views.seoul_map),
    path("contents/", views.contents),
    path("parking_count_map/", views.parking_count_map),
    path("parking_expose_corr/", views.parking_expose_corr),
    path("transportation/", views.transportation),
    path("transportation/transportation_illegal/", views.trans_ill),
    path("transportation/public_illegal/", views.public_ill),
    path("transportation/gu_trans_illegal/", views.gu_trans_ill),
    path("transportation/parking_illegal/", views.count_ill),
    path("transportation/parking_transportation/", views.count_trans),
    path("weather_corr/", views.weather_corr),
    path("reference/",views.reference)
]