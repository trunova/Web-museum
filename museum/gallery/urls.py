from django.urls import path
from .import views

urlpatterns = [
    path('', views.MuseumView.as_view(), name='gallery'),
    path('<int:piece_id>/detailed_piece/', views.PieceDetailed.as_view(), name='detailed_piece'),
    path('<int:exh_id>/detail_exh/', views.ExhibitionDetailed.as_view(), name='detail_exh'),
    path('<int:author_id>/detail_author/', views.AuthorDetailed.as_view(), name='detail_author'),
    path('<int:hall_id>/detail_hall/', views.HallDetailed.as_view(), name='detail_hall'),
    path('<int:piece_id>/change_piece/', views.PieceChange.as_view(), name='change_piece'),
    path('<int:exh_id>/change_exhibition/', views.ExhibitionChange.as_view(), name='change_exhibition'),
    path('<int:author_id>/change_author/', views.AuthorChange.as_view(), name='change_author'),
    path('<int:hall_id>/change_hall/', views.HallChange.as_view(), name='change_hall'),
    path('add_exhibition/', views.AddExhibition.as_view(), name='add_exhibition'),
    path('add_museum_piece/', views.AddMuseumPiece.as_view(), name='add_museum_piece'),
    path('add_author/', views.AddAuthor.as_view(), name='add_author'),
    path('add_hall/', views.AddHall.as_view(), name='add_hall'),
    path('visit/', views.VisitView.as_view(), name='visit'),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('about_me/', views.AboutMe.as_view(), name='about_me'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path("filter/", views.FilterPiecesView.as_view(), name='filter')
]