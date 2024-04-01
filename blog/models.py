from django.conf import settings                # from import = 다른 파일에 있는 것을 추가
from django.db import models
from django.utils import timezone


class Post(models.Model):                       # 모델 = 객체 = pbject 을 정의하는 코드, vs  변수 = 속성
    # Models = post가 장고 모델임을 의미. 이 코드 때문에 post가 DB에 저장되어야 한다고 알게 됨
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   # 다른 모델에 대한 링크
    title = models.CharField(max_length=200)    # 글자 수 제한된 텍스트 정의
    text = models.TextField()                   # 글자수 제한 없는 긴 텍스트
    created_date = models.DateTimeField(        # 날짜와 시간
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):                          # 메서드
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title                       # 값 되돌려줌 - 제목
