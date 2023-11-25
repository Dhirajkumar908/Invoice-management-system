from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('invoice',views.index, name='index'),
    path('invoice/<int:id>',views.invoice, name='invoice'),
    path('invoice/add',views.create_invoice, name='create_invoice'),
    path('add_product',views.add_product, name='add_product'),
    path('client',views.client, name='client'),
    path('userinvoicedata', views.userinvoicedata, name="userinvoicedata")

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
