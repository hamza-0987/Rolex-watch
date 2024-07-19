from django.contrib import admin
from django.urls import path
from website.views import contact, product_details
from website.views import home  # import the view
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('product_details/<slug>', product_details, name='product_details'), 
    path('contact/',contact, name='contact'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)