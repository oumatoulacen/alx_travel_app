from django.urls import path
from alx_travel_app.listings import views

urlpatterns = [
    path('listings/', views.test_view, name='test-view'),
]