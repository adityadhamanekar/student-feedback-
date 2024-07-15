from django.db import models

class Feedback(models.Model):
    BRANCH_CHOICES = [
        ('cs', 'Computer Science (CS)'),
        ('ec', 'Electronics and Communication (EC)'),
        ('ee', 'Electrical Engineering (EE)'),
        ('me', 'Mechanical Engineering (ME)'),
        ('cv', 'Civil Engineering (CV)'),
    ]

    RATING_CHOICES = [
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Poor', 'Poor'),
    ]

    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20)
    branch = models.CharField(max_length=2, choices=BRANCH_CHOICES)
    question1 = models.CharField(max_length=10, choices=RATING_CHOICES)
    question2 = models.CharField(max_length=10, choices=RATING_CHOICES)
    question3 = models.CharField(max_length=10, choices=RATING_CHOICES)
    question4 = models.CharField(max_length=10, choices=RATING_CHOICES)
    question5 = models.CharField(max_length=10, choices=RATING_CHOICES)
    additional_feedback = models.TextField()
    pdf_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name



class Question(models.Model):
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text