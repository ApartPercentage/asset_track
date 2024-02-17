from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'dashboard-index'),
    path('staff/', views.staff, name = 'dashboard-staff'),
    path('staff/details/<int:pk>', views.staff_details, name = 'dashboard-staff-details'),
    path('assets/', views.assets, name = 'dashboard-assets'),
    path('assets/borrow/', views.assets_borrow, name = 'dashboard-assets-borrow'),
    path('assets/return/<int:pk>/', views.assets_return, name = 'dashboard-assets-return'),
    path('chart-data/', views.calculate_chart_data, name='chart-data'),
]