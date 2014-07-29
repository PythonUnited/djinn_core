from django.conf.urls.defaults import patterns, include, url
from views.admin import AdminView


_urlpatterns = patterns(
    "",

    url(r"^admin/?$",
        AdminView.as_view(),
        name="djinn_core_index"),
)


urlpatterns = patterns(
    '',
    (r'^djinn/', include(_urlpatterns)),
    )
