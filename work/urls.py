from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', login_required(views.ArticleList.as_view()), name='home'),
    path('<int:pk>/', login_required(views.ArticleDetail.as_view()),
         name='article-detail'),
    path('<int:pk>/take', views.take, name='take'),
    path('<int:pk>/send', views.send, name='send'),
    path('<int:pk>/publish', views.publish, name='publish'),
    path('logout', views.logout_view, name='logout')
]
