from myapp.views import *
from django.urls import path , include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people', Peopleviewset, basename='people')
urlpatterns = router.urls

urlpatterns= [
    path('index/', index),
    path('person/', person),
    path('',include(router.urls))
]