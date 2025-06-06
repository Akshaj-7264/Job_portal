from django.shortcuts import redirect
from django.http import HttpResponseForbidden

def seeker_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.profile.user_type == 'seeker':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Access denied: Seekers only.")
    return _wrapped_view

def recruiter_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.profile.user_type == 'recruiter':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Access denied: Recruiters only.")
    return _wrapped_view
