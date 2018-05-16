from django.conf.urls import url
import main.views

urlpatterns = [
    url(r'main', main.views.main_page, name="main_page"),
]