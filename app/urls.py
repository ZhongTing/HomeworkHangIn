from app import settings
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'api.user',
    url(r'^api/user/login$', 'login'),
)

urlpatterns += patterns(
    'api.homework',
    url(r'^api/homework/create$', 'create'),
    url(r'^api/homework/list$', 'list_homework'),
    url(r'^api/homework/upload$', 'upload'),
    url(r'^api/homework/download$', 'download'),
)

urlpatterns += patterns(
    '',
    url(r'^HomeworkHangIn/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
)