from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import RegistrationForm
from .forms import LoginForm
from .models import Profile
from jobs.models import Job
from jobs.utils import get_adzuna_jobs
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from .decorators import seeker_required, recruiter_required
from django.shortcuts import get_object_or_404
from jobs.models import Application


def home_view(request):
    return render(request, 'home.html')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        if self.request.user.profile.user_type == 'seeker':
            return '/seeker/dashboard/'
        else:
            return '/recruiter/dashboard/'

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirect based on user type
            if hasattr(user, 'profile') and user.profile.user_type == 'seeker':
                return redirect('seeker_dashboard')
            else:
                return redirect('recruiter_dashboard')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            # 🧪 Add debug print here
            print(f"Before: {user.profile.user_type}")  # Should be empty

            user.profile.user_type = form.cleaned_data['user_type']
            user.profile.save()  # ✅ Make sure to save the profile
            user.save()

            # 🧪 Check after setting
            print(f"After: {user.profile.user_type}")  # Should print 'seeker' or 'recruiter'

            login(request, user)
            if user.profile.user_type == 'seeker':
                return redirect('seeker_dashboard')
            else:
                return redirect('recruiter_dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})




@login_required
@seeker_required
def seeker_dashboard(request):
    local_jobs = Job.objects.all().order_by('-created_at')
    adzuna_jobs = get_adzuna_jobs()
    return render(request, 'dashboard/seeker_dashboard.html', {
        'local_jobs': local_jobs,
        'adzuna_jobs': adzuna_jobs
    })

@login_required
@recruiter_required
def recruiter_dashboard(request):
    jobs = Job.objects.filter(posted_by=request.user).order_by('-created_at')
    return render(request, 'dashboard/recruiter_dashboard.html', {'jobs': jobs})

@login_required
def applicants_list(request, job_id):
    job = get_object_or_404(Job, id=job_id, posted_by=request.user)
    applicants = Application.objects.filter(job=job)
    return render(request, 'dashboard/applicants_list.html', {
        'job': job,
        'applicants': applicants
    })