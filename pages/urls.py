from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]

# We’re using Django’s TemplateView generic class-based view which means we only need to specify our template_name to use it.