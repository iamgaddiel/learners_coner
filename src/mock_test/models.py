from django.db import models

from classroom.models import Class, Subject


class MockTest(models.Model):
    TERMS = [
        (1, 1),
        (2, 2),
        (3, 3),
    ]
    title = models.CharField(max_length=50, unique=True, default="")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    term = models.PositiveIntegerField(default=1, choices=TERMS)
    level = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} | level: {self.level} | term: {self.term}"

class MockTestQuestion(models.Model):
    CORRECT_OPTIONS = [
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),
        ('d', 'd'),
    ]
    TIME_CHOICES = [
        ('30', '30'),
        ('45', '45'),
        ('60', '60'),
    ]
    mock_test = models.ForeignKey(MockTest, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=1, choices=CORRECT_OPTIONS)
    question = models.CharField(max_length=500, unique=True, blank=True)
    question_number = models.PositiveIntegerField(default=1)
    timer = models.CharField(max_length=2, choices=TIME_CHOICES, default=TIME_CHOICES[0])
    a = models.CharField(max_length=400, default="")
    b = models.CharField(max_length=400, default="")
    c = models.CharField(max_length=400, default="", blank=True)
    d = models.CharField(max_length=400, default="", blank=True)
    e = models.CharField(max_length=400, default="", blank=True)

    def __str__(self) -> str:
        return f"{self.mock_test.title} | No: {self.question_number} answer: {self.correct_answer}"
