from django.urls import path
from . import views


urlpatterns = [
    path('list',views.car_list_view,name='car_list'),
    path('<int:pk>',views.car_detail_view,name='car_detail'),
    path("showroom",views.showroom_view.as_view(),name='showroom_view'),
    path('showroom/<int:pk>',views.showroom_details.as_view(),name='showroom_details'),   
]
