from django.urls import path

from myapp.views import StartPageView

urlpatterns = [
    path('', StartPageView.as_view(), name='start_page')
]
