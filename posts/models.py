from django.db import models

# Create your models here.
# 클래스를 정의할 것
# models.model을 상속시켜서 class만들기 (모델을 만들어 쓰려면 model 모듈을 가져다 써)
class Post(models.Model):
    # 저장하고 싶은 칼럼 이름 작성하기 (모든 데이터는 표)
    # 해당 칼럼에 들어가야 하는 데이터의 양식을 지정
    # models django 검색해서 필요한 함수, 옵션값 뽑아쓰기
    title = models.CharField(max_length=100)
    content = models.TextField()