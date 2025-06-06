# job_portal/context_processors.py

def show_navbar(request):
    hide_on_urls = [
        'login', 'register', 'password_reset',
        'password_reset_done', 'password_reset_confirm', 'password_reset_complete'
    ]
    try:
        current_url = request.resolver_match.url_name
    except AttributeError:
        current_url = None

    return {
        'show_navbar': current_url not in hide_on_urls
    }
