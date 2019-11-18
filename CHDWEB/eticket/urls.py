from django.conf.urls import url,include
from eticket import views
urlpatterns = [
    url(r'^$',views.form_view,name = 'ticket'),

]
