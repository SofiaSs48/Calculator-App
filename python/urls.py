from django.urls import path
from . import views
urlpatterns = [
path("", views.index, name="index"),
path("calculate_average/", views.calculate_average, name="calculate_average"),
path("calculator/", views.calculator, name="calculator"),
]

from django.urls import path
from . import views
urlpatterns = [
path("", views.index, name="index"),
path("calculate_average/", views.calculate_average, name="calculate_average"),
path("calculator/", views.calculator, name="calculator"),
path("cat_images/", views.cat_images, name="cat_images"),
]