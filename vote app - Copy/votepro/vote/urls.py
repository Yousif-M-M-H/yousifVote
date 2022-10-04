from django.urls import path
from . import views
from .views import ShowForm, create, votedetails, results


urlpatterns = [
    path('', views.index, name='index'),
    path('show', ShowForm.as_view(), name='show_form'),
    path('create', views.create, name='show_vote'),
    path('vote/<poll_id>/', views.votedetails, name='vote'),
    path('results/<poll_id>/', views.results, name='results'),




]
