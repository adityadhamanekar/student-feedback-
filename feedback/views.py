from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feedback
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from .models import Question

def feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        usn = request.POST.get('usn')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        teacher = request.POST.get('teacher')
        question1 = request.POST.get('question1')
        question2 = request.POST.get('question2')
        question3 = request.POST.get('question3')
        question4 = request.POST.get('question4')
        question5 = request.POST.get('question5')
        additional_feedback = request.POST.get('feedback')

        feedback = Feedback.objects.create(
            name=name,
            usn=usn,
            branch=branch,
            semester=semester,
            teacher=teacher,
            question1=question1,
            question2=question2,
            question3=question3,
            question4=question4,
            question5=question5,
            additional_feedback=additional_feedback
        )

        # Ensure media directory exists
        media_root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media')
        if not os.path.exists(media_root):
            os.makedirs(media_root)

        # Generate PDF
        pdf_path = os.path.join('media', f'feedback_{feedback.id}.pdf')
        pdf_full_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), pdf_path)
        c = canvas.Canvas(pdf_full_path, pagesize=letter)
        c.drawString(100, 750, f"Name: {name}")
        c.drawString(100, 735, f"USN: {usn}")
        c.drawString(100, 720, f"Branch: {feedback.get_branch_display()}")
        c.drawString(100, 705, f"Semester: {feedback.get_semester_display()}")
        c.drawString(100, 690, f"Teacher: {feedback.get_teacher_display()}")
        c.drawString(100, 675, f"{Question.objects.get(pk=1).question_text}: {question1}")
        c.drawString(100, 660, f"{Question.objects.get(pk=2).question_text}: {question2}")
        c.drawString(100, 645, f"{Question.objects.get(pk=3).question_text}: {question3}")
        c.drawString(100, 630, f"{Question.objects.get(pk=4).question_text}: {question4}")
        c.drawString(100, 615, f"{Question.objects.get(pk=5).question_text}: {question5}")
        c.drawString(100, 600, f"Additional Feedback: {additional_feedback}")
        c.save()

        # Update feedback record with pdf_url
        feedback.pdf_url = pdf_path
        feedback.save()

        return redirect('feedback_success')

    return redirect('home')

def feedback_success_view(request):
    return render(request, 'feedback_success.html')


def view_all_feedback(request):
    teacher_filter = request.GET.get('teacher')
    if teacher_filter:
        all_feedback = Feedback.objects.filter(teacher=teacher_filter)
        show_graph = True
    else:
        all_feedback = Feedback.objects.all()
        show_graph = False

    teachers = Feedback.TEACHER_CHOICES

    # Get questions from the database
    question_objects = Question.objects.all()
    questions = [question.question_text for question in question_objects]
    question_dict = {question.question_text: f'question{i+1}' for i, question in enumerate(question_objects)}

    # Initialize data structures for rating counts
    rating_choices = ['Excellent', 'Good', 'Average', 'Poor']
    rating_counts = {question: {rating: 0 for rating in rating_choices} for question in questions}
    total_responses = {question: 0 for question in questions}

    # Aggregate rating data
    for feedback in all_feedback:
        for question_text, question_field in question_dict.items():
            rating = getattr(feedback, question_field)
            if rating in rating_counts[question_text]:
                rating_counts[question_text][rating] += 1
                total_responses[question_text] += 1

    # Calculate percentages for each question
    rating_percentages = {
        question: {rating: (count / total_responses[question]) * 100 if total_responses[question] else 0
                   for rating, count in rating_counts[question].items()}
        for question in questions
    }

    context = {
        'all_feedback': all_feedback,
        'teachers': teachers,
        'teacher_filter': teacher_filter,
        'questions': questions,
        'rating_percentages': rating_percentages,
        'show_graph': show_graph,
    }
    return render(request, 'view_all_feedback.html', context)