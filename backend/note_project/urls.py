from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^api/v1/', include('note_app.urls')),
    re_path(r'^admin/', admin.site.urls),
]