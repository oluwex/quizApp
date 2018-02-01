from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserRegisterView

urlpatterns = [
    url(r'^user/register/$', UserRegisterView.as_view()),
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)