from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from views.views import splash, home, dashboard, about, sign_up, thanks, sign_in, sign_out, profile, profiles, blog, \
    PostList, PostDetail, moo
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^moo/$', moo, name='moo'),
                       url(r'^$', splash, name='splash'),
                       url(r'^home/$', home, name='home'),
                       url(r'^blog/$', dashboard, name='dashboard'),
                       url(r'^sign_in/$', sign_in, name='sign_in'),
                       url(r'^sign_out/$', sign_out, name='sign_out'),
                       url(r'^about/$', about, name='about'),
                       url(r'^sign_up/$', sign_up, name='sign_up'),
                       url(r'^thanks/$', thanks, name='thanks'),
                       # url(r'^blog/$', blog, name='blog'),
                       url(r'^profile/(?P<id>\d+)/$', profile, name='profile'),
                       url(r'^profiles/$', profiles, name='profiles'),
                       url(r'^posts/$', PostList.as_view()),
                       url(r'^posts/(?P<pk>[0-9]+)/$', PostDetail.as_view()),
                       url(r'^admin/$', include(admin.site.urls)),
                       )