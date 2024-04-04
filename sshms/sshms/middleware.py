from django.utils import timezone
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect

MAX_INACTIVITY_DURATION = getattr(settings, 'SESSION_EXPIRE_SECONDS', 3600)

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
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
                    return redirect('users:login')
            
            request.session['last_activity'] = timezone.now().timestamp()
        
        response = self.get_response(request)
        return response