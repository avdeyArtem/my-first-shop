from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^search/$', views.search, name="search"),
    url(r'^(?P<id>[0-9]+)/$', views.item, name="item"),
    url(r'^category/(?P<slug>[\w-]+)/$', views.category, name="category"),
    url(r'^brand/(?P<slug>[\w-]+)/$', views.brand, name="brand"),
    url(r'^add_order/$', views.order, name="order"),

]
