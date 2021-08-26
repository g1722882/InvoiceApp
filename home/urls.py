from django.contrib import admin
from django.urls import path
from .views import  createInvoice, render_pdf_view, view_PDF

app_name = 'invoice'
urlpatterns = [ 
    path('', createInvoice, name="invoice-create"),
    path('invoice-download/<id>', render_pdf_view, name='invoice-download')
]
