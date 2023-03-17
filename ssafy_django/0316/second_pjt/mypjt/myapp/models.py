from django.db import models

# Create your models here.
class Article(models.Model):
    # 길이 제한이 있는 텍스트 형태
    title = models.CharField(max_length=20)
    # 길이 제한이 없는 텍스트 형태
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.created_at.month}/{self.created_at.day}에 생성된 {self.id}번글 - {self.title} : {self.content}"
        
