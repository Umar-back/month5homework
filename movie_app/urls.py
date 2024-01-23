from django.urls import path
from movie_app import views

urlpatterns = [
    # path('director/', views.director_list),
    path('director/', views.DirectorAPIview.as_view()),
    # path('director/<int:id>', views.director_detail),
    path('director/<int:id>', views.DirectorDetailAPIview),

    # path('movie/', views.movie_list),
    path('movie/', views.MovieAPIview.as_view()),
    # path('movie/<int:id>', views.movie_detail),
    path('movie/<int:id>', views.MovieDetailAPIview),

    # path('review/', views.review_list),
    path('review/', views.ReviewAPIview.as_view()),
    # path('review/<int:id>', views.review_detail),
    path('review/<int:id>', views.ReviewDetailAPIview),
]