from django.conf.urls import url,include
from about import views
urlpatterns = [
    url(r'^$',views.index,name = 'index')
]
