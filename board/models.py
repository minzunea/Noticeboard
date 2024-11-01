from django.db import models

# Create your models here.

class Create(models.Model):
    title = models.CharField(max_length=20, db_column='title')
    contents = models.TextField(max_length=1000, db_column='contents')
    author = models.CharField(max_length=10, db_column='author') # 글쓴이 입력 칸 마련 (기본 익명)
    create_date = models.DateTimeField(auto_now_add=True) # 글 생성일
    
    def __str__(self):
        return f"{self.title}, {self.author}, {self.contents}, {self.id}, {self.create_date}"

    

class Comment(models.Model):
    comment_id = models.ForeignKey(Create, on_delete=models.CASCADE, db_column='comment_id') # Create 클래스의 id를 외래키로 참조
    contents = models.CharField(max_length=100, db_column='contents')
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=10, db_column='author')
    
    def __str__(self):
        return f"{self.contents},{self.create_date}"