"""
Definition of urls for PurchaseManagementSystem.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views
import PurchaseOrder.views
import PurchaseRequisition.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    #admin
    url(r'^admin/', admin.site.urls, name="admin"),

    #app
    url(r'^$', app.views.userlogin, name='userlogin'),
    url(r'^menu', app.views.menu, name="menu"),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    #purchase requisition
    url(r'^purchaserequisitionform$', PurchaseRequisition.views.purchaserequisitionform, name="purchase_requisition_form"),
    url(r'^purchaserequisitionconfirmation', PurchaseRequisition.views.purchaserequisitionconfirmation, name="confirm_purchase_requisition"),
    url(r'^purchaserequisitiondetails', PurchaseRequisition.views.purchaserequisitiondetails, name="purchase_requisition_details"),
    url(r'^purchaserequisitionhistorydetails', PurchaseRequisition.views.purchaserequisitionhistorydetails, name='purchase_requisition_history_details'),
    url(r'^purchaserequisitionhistory', PurchaseRequisition.views.purchaserequisitionhistory, name="purchase_requisition_history"),


    #purchase order
    url(r'^purchaseorderform$', PurchaseOrder.views.purchaseorderform, name="purchase_order_form"),
    url(r'^fillingpurchaseorder', PurchaseOrder.views.fillingpurchaseorder, name="fill_purchase_order_form"),
    url(r'^purchaseorderconfirmation', PurchaseOrder.views.purchaseorderconfirmation, name="confirm_purchase_order"),
    url(r'^purchaseorderdetails', PurchaseOrder.views.purchaseorderdetails, name="purchase_order_details"),
    url(r'^purchaseorderhistorydetails', PurchaseOrder.views.purchaseorderhistorydetails, name='purchase_order_history_details'),
    url(r'^purchaseorderhistory', PurchaseOrder.views.purchaseorderhistory, name="purchase_order_history"),
]
