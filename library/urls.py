from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^home/(?P<id>.+)$', views.home, name='home'),

    url(r'^order/$', views.orderbook, name='order'),
    url(r'^Order/$', views.order1, name='order1'),

    url(r'^issue/$', views.issuebook, name='issue'),
    url(r'^Issue/$', views.issue1, name='issue1'),

    url(r'^donate/$', views.donatebook, name='donate'),
    url(r'^Donate/$', views.donate1, name='donate1'),

    url(r'^return/$', views.returnbook, name='return'),
    url(r'^Return/$', views.return1, name='return1'),

    url(r'^ffeedback/$', views.feedback, name='feedback'),
    url(r'^Feedback/$', views.feed1, name='feed1'),


    url('^index/(?P<token>.+)$',views.index,name='index'),

    url(r'^fine/$', views.fine, name='fine'),
    url(r'^Fine/$', views.fine1, name='fine1'),
    url(r'^lfine/$', views.fine2, name='fine2'),

    url(r'^search/$', views.search, name='search'),
    url(r'^Search/$', views.search1, name='search1'),

    url(r'^add/$', views.add, name='add'),
    url(r'^Add/$', views.add1, name='add1'),

    url(r'^nnewsfeed/$', views.news, name='news'),
    url(r'^NewsFeed/$', views.news1, name='news1'),



    # url(r'^index/search/$', views.searchbook, name='search'),
    # url(r'^index/feedback/$', views.feedback, name='feedback'),
]
