from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, Application
from .forms import JobForm, ApplicationForm
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})

@login_required
def post_job(request):
    if not request.user.profile.user_type == 'recruiter':
        return redirect('home')

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect('recruiter_dashboard')
    else:
        form = JobForm()
    
    return render(request, 'jobs/post_job.html', {'form': form})

def apply_to_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect('seeker_dashboard')  # or a "Thank you" page
    else:
        form = ApplicationForm()

    return render(request, 'jobs/apply_form.html', {'form': form, 'job': job})

@login_required
def view_applicant(request, job_id):
    job = get_object_or_404(Job, id=job_id, posted_by=request.user)
    applications = Application.objects.filter(job=job)
    return render(request, 'jobs/view_applicant.html', {
        'job': job,
        'applications': applications
    })

def update_application_status(request, app_id, action):
    application = get_object_or_404(Application, id=app_id)
    
    if action == 'approve':
        application.status = 'approved'
        subject = 'Job Application Approved'
        message = f"Dear {application.name},\n\nYour application for the job '{application.job.title}' has been approved."
    elif action == 'reject':
        application.status = 'rejected'
        subject = 'Job Application Rejected'
        message = f"Dear {application.name},\n\nYour application for the job '{application.job.title}' has been rejected."
    else:
        messages.error(request, "Invalid action.")
        return redirect('applicants_list', job_id=application.job.id)

    application.save()

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,  # Replace with your sender email
        [application.email],
        fail_silently=False,
    )

    messages.success(request, f"Application {action}ed and email sent.")
    return redirect('applicants_list', job_id=application.job.id)