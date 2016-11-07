from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import home, MailMeView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^index$', home),
    url(r'^email$', MailMeView.as_view(), name='mailme')
]
urlpatterns += staticfiles_urlpatterns()