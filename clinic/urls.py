from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from core.views import CreateEntry, GetHours


admin.autodiscover()

urlpatterns = [
    url(r'^$', CreateEntry.as_view(), name='create_entry'),
    url(r'^get_hours/$', GetHours.as_view(), name='get_hours'),
    url(r'^success/$', TemplateView.as_view(template_name='success.html')),
    # Admin urls
    url(r'^admin/', include(admin.site.urls)),
]
