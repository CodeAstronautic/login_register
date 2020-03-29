from django.conf.urls import url
#from app import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views 
from django.contrib.auth import views as v

# SET THE NAMESPACE!
app_name = 'app'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',auth_views.register,name='register'),
    url(r'^user_login/$',auth_views.user_login,name='user_login'),

    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
