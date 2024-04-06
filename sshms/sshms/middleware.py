from django.utils import timezone
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect, render

MAX_INACTIVITY_DURATION = getattr(settings, 'SESSION_EXPIRE_SECONDS', 3600)
LOGIN_URL = getattr(settings, 'LOGIN_URL', 'users:login')
LOGIN_REDIRECT_URL = getattr(settings, 'LOGIN_REDIRECT_URL', 'main:home')

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_paths = ['/users/login/', '/users/signup/', '/']

    def __call__(self, request):
        if request.path in self.allowed_paths:
            return self.get_response(request)
        
        if request.user.is_authenticated:
            try:
                last_activity = request.session['last_activity']
            except KeyError:
                request.session['last_activity'] = timezone.now().timestamp()
            else:
                current_time = timezone.now().timestamp()
                inactivity_duration = current_time - last_activity
                if inactivity_duration >= MAX_INACTIVITY_DURATION:
                    logout(request)
                    request.session.flush()
                    return redirect('users:login')
                request.session['last_activity'] = timezone.now().timestamp()
        else:
            # If the user is not authenticated, check if the requested path is allowed
            if request.path != '/' and request.path != LOGIN_URL and request.path != '/users/sign_up/':
                return redirect(LOGIN_URL)

        response = self.get_response(request)
        return response