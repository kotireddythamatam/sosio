from wishapp import views
from django.urls import path
urlpatterns =[
    path('wish',views.wish),
    path('display',views.display),
]
