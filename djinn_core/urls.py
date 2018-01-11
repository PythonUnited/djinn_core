from django.conf.urls import include, url 
from .views.admin import AdminView


_urlpatterns = [
    url(r"^djinn_admin/?$", AdminView.as_view(), name="djinn_admin"),
]

urlpatterns = [
    url(r'^djinn/', include(_urlpatterns)),
]
