from app import settings
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'api.user',
    url(r'^HomeworkHangIn/api/user/login$', 'login'),
)

urlpatterns += patterns(
    'api.homework',
    url(r'^HomeworkHangIn/api/homework/create$', 'create'),
    url(r'^HomeworkHangIn/api/homework/list$', 'list_homework'),
    url(r'^HomeworkHangIn/api/homework/upload$', 'upload'),
    url(r'^HomeworkHangIn/api/homework/download$', 'download'),
)

urlpatterns += patterns(
    '',
    url(r'^HomeworkHangIn/$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
        'path': 'index.html'
    }),
    url(r'^HomeworkHangIn/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
)