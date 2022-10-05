from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_profile),
    path('upload_book/', views.upload_book),
    path('<int:id>/', views.display_book),
    path('<int:id>/update/', views.update_book),
    path('<int:id>/delete/', views.delete_book),
    path('add_to_favorites/<int:id>/', views.add_to_favorites),
    path('remove_favoraite/<int:id>', views.remove_favoraite),
    path('show_user_profile/', views.show_user_profile),
]