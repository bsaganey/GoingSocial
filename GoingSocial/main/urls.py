from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from views.views import splash, about, sign_up, home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', splash, name='splash'),
    url(r'^home', home, name= 'home'),
    url(r'^about', about, name='about'),
    url(r'^SignUp', sign_up, name='signup'),
    #url(r'^User/(?P<thanks_id>\d+)/$', User, name='user'),
    #url(r'^admin/', include(admin.site.urls)),
)