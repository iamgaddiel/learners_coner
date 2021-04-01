from django.db import models

from classroom.models import Subject


class MockTest(models.Model):
    TERMS = [
        (1, 1),
        (2, 2),
        (3, 3),
    ]
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    term = models.PositiveIntegerField(default=1, choices=TERMS)
    level = ""

    def __str__(self) -> str:
        return super().__str__()

class MockTestQuestion(models.Model):
    mock_test = models.ForeignKey(MockTest, on_delete=models.CASCADE)
    correct_answer = models.Ca

    def __str__(self) -> str:
        return super().__str__()
