from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include("homepage.urls")),
    path('accounts/', include("allauth.urls")),

]
