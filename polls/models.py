from django.db import models


class Category(models.Model):
    # Polls Category Model
    category_text = models.TextField(verbose_name="질문목록", max_length=100, unique=True)
    create_time = models.DateTimeField(verbose_name="생성시간", auto_now_add=True)

    def __str__(self):  # 클래스의 정보를 name으로 호출하는 함수
        return f'{self.category_text}'


class Questions(models.Model):
    category = models.ForeignKey(to=Category, verbose_name="질문명", on_delete=models.CASCADE, related_name="Category_name", null=False)
    question_text = models.TextField(verbose_name="투표항목", max_length=50)
    votes = models.IntegerField(verbose_name="투표수", null=True, default=0)

    def __str__(self):  # 클래스의 정보를 name으로 호출하는 함수
        return f'{self.question_text}'
