from django.urls import path

from report import views 
 
urlpatterns = [ 
    path('api/customers', views.customers_list),
    #path('api/tutorials/(?P<pk>[0-9]+)$', views.customer_detail),
    #path('api/tutorials/published$', views.tutorial_list_published)
]