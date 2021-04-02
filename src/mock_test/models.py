from django.db import models

from classroom.models import Class, Subject


class MockTest(models.Model):
    TERMS = [
        (1, 1),
        (2, 2),
        (3, 3),
    ]
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    term = models.PositiveIntegerField(default=1, choices=TERMS)
    level = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()

class MockTestQuestion(models.Model):
    CORRECT_OPTIONS = [
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),
        ('d', 'd'),
    ]
    mock_test = models.ForeignKey(MockTest, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=1, choices=CORRECT_OPTIONS)
    a = models.CharField(max_length=400, default="")
    b = models.CharField(max_length=400, default="")
    c = models.CharField(max_length=400, default="")
    d = models.CharField(max_length=400, default="")

    def __str__(self) -> str:
        return super().__str__()
