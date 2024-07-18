from django.db import models

class Feedback(models.Model):
    BRANCH_CHOICES = [
        ('cs', 'Computer Science (CS)'),
        ('ec', 'Electronics and Communication (EC)'),
        ('ee', 'Electrical Engineering (EE)'),
        ('me', 'Mechanical Engineering (ME)'),
        ('cv', 'Civil Engineering (CV)'),
    ]

    SEMESTER_CHOICES = [
        (1, '1st Semester'),
        (2, '2nd Semester'),
        (3, '3rd Semester'),
        (4, '4th Semester'),
        (5, '5th Semester'),
        (6, '6th Semester'),
        (7, '7th Semester'),
        (8, '8th Semester'),
    ]

    TEACHER_CHOICES = [
        ('teacher1', 'Dr. John Doe'),
        ('teacher2', 'Dr. Jane Smith'),
        ('teacher3', 'Prof. Richard Roe'),
        ('teacher4', 'Prof. Mary Major'),
        ('teacher5', 'Dr. Alan Smithee'),
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
    semester = models.IntegerField(choices=SEMESTER_CHOICES, default=1)
    teacher = models.CharField(max_length=10, choices=TEACHER_CHOICES, default='teacher1')
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
