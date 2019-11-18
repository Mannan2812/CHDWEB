from django.conf.urls import url,include
from busguide import views
urlpatterns = [
    url(r'^$',views.form_view,name = 'index'),
]
