from django.conf.urls import url,include
from lake import views
urlpatterns = [
    url(r'^$',views.index,name = 'index'),
]
