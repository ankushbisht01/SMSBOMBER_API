from django.conf.urls import url, include


from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('SMSapi', views.SendSMS,basename='SMSapi')


urlpatterns = [
    url(r'^', include(router.urls)),
    
]