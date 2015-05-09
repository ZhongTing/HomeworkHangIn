from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.user',
    url(r'^api/user/login', 'login'),
)
