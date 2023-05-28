from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# from image_upload.views import StudentView
from products.views import ProductView
from rest_framework import routers 
# from products.views import send_emails
from products.views import *

route = routers.DefaultRouter()
route.register("", ProductView, basename="studentview")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('register/', RegisterAPI.as_view()),    
    # path('send-emails/', send_emails, name='send_emails'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







   
