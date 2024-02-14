from django.urls import path
# Импортируем созданные нами представления
from .views import (

   PostsList, PostDetail, PostsSearch, PostCreate, PostUpdate, PostDelete
)

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostsList.as_view(), name = 'posts'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view(),name='post'),
   path('search/', PostsSearch.as_view(), name='post_search'),
   path('create/', PostCreate.as_view(), name='news_create'),
   path('articles/create/', PostCreate.as_view(), name='article_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('articles/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete')
   ]