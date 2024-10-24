from django.db import models

# Create your models here.

class Create(models.Model):
    text_title = models.CharField(max_length=20, db_column='text_title')
    text_body = models.CharField(max_length=500, db_column='text_body')
    creater = models.CharField(max_length=10, db_column='creater') # 글쓴이 입력 칸 마련 (기본 익명)
    create_date = models.DateTimeField(auto_now_add=True) # 글 생성일
    update_date = models.DateTimeField(auto_now=True) # 글 수정일
    
    def __str__(self):
        return f"{self.text_title}, {self.text_body}, {self.creater}, {self.id}"
    

class Comment(models.Model):
    comment_id = models.ForeignKey(Create, on_delete=models.CASCADE, db_column='comment_id') # Create 클래스의 id를 외래키로 참조
    comment_text = models.CharField(max_length=100, db_column='comment_text') 
    create_date = models.DateTimeField(auto_now_add=True) # 댓글 수정 불가, 글 생성일
    
    def __str__(self):
        return self.comment_text