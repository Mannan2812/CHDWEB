from django.conf.urls import url,include
from destination import views
urlpatterns = [
    url(r'^$',views.index,name = 'index')
]
