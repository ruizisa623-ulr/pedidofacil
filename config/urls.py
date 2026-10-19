"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path, reverse_lazy
from django.views.generic import CreateView, RedirectView


class RegistroView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/registro.html"
    success_url = reverse_lazy("login")


urlpatterns = [
    path("", RedirectView.as_view(pattern_name="listar_productos"), name="inicio"),
    path("admin/", admin.site.urls),
    path("productos/", include("productos.urls")),
    path("pedidos/", include("pedidos.urls")),
    path("cuentas/", RedirectView.as_view(pattern_name="login"), name="cuentas_root"),
    path("cuentas/", include("django.contrib.auth.urls")),
    path("cuentas/registro/", RegistroView.as_view(), name="registro"),
]
