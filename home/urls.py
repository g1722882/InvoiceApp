from django.contrib import admin
from django.urls import path
from .views import InvoiceListView, createInvoice, render_pdf_view, view_PDF

app_name = 'invoice'
urlpatterns = [
    path('', InvoiceListView.as_view(), name="invoice-list"),
    path('create/', createInvoice, name="invoice-create"),
    path('invoice-detail/<id>', view_PDF, name='invoice-detail'),
    path('invoice-download/<id>', render_pdf_view, name='invoice-download')
]
