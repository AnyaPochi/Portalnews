from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
# Модель Author
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.user.title()}: {self.rating}'

# Метод update_rating() модели Author, который обновляет рейтинг текущего автора

    def update_rating(self):
        post_rating = Post.objects.filter(author=self).aggregate(pr=Coalesce(Sum('rating'), 0))['pr']
        comments_rating = Comment.objects.filter(user=self.user).aggregate(cr=Coalesce(Sum('rating'), 0))['cr']
        post_comments_rating = Comment.objects.filter(post__user=self).aggregate(pcr=Coalesce(Sum('rating'), 0))['pcr']

        print(f'Рейтинг постов  -{post_rating}, \n '
              f'Рейтинг комментариев автора -{comments_rating}, \n'
              f' Рейтинг комментариев постов автора -{post_comments_rating}')
        self.rating = post_rating*3+comments_rating+post_comments_rating
        self.save()

# Модель Category
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name.title()
# #Модель Post

POSITIONS = [
    (1, 'Статья'),
    (2, 'Новость')
]

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=POSITIONS, default=2)
    time_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
# Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают рейтинг на единицу.
    def like(self):
        self.rating += 1
        return self.rating
    def dislike(self):
        self.rating -= 1
        return self.rating

# Метод preview() модели Post, который возвращает
# начало статьи (предварительный просмотр) длиной 124 символа и добавляет многоточие в конце.
    def __str__(self):
        return self.title.title()
    def preview(self):
        return f'{self.text[:123]}...'


#Модель PostCategory
class PostCategory(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


# Модель Comment
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        return self.rating
    def dislike(self):
        self.rating -= 1
        return self.rating
