from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_article_form, name='create_article_form'),
    path('save/', views.save_article, name='save_article'),
    path('edit/<int:article_id>/', views.edit_article_form, name='edit_article_form'),
    path('update/', views.update_article, name='update_article'),
    path('delete/<int:article_id>/', views.delete_article, name='delete_article'),
    path('article/<int:article_id>/', views.detail, name='detail'),
]
