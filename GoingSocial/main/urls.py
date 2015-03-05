from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from views.views import home, splash, about, SignUp

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', splash),
    url(r'^home', home),
    url(r'^about', about),
    url(r'^SignUp', SignUp),
    

    url(r'^admin/', include(admin.site.urls)),
)
