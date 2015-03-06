from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from views.views import splash, home, about, sign_up, thanks, sign_in, sign_out, profile, blog

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', splash, name='splash'),
    url(r'^home', home, name= 'home'),
    url(r'^sign_in/', sign_in, name='sign_in'),
    url(r'^sign_out/', sign_out, name='sign_out'),
    url(r'^about', about, name='about'),
    url(r'^sign_up', sign_up, name='sign_up'),
    url(r'^thanks', thanks, name='thanks'),
    url(r'^blog', blog, name='blog'),
    url(r'^profile/(?P<id>\d+)/$', profile, name='profile'),
    url(r'^admin/', include(admin.site.urls)),
)