from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
from django.conf import settings

# Create your views here.
def generate_text(request):
    if request.method == 'POST':
        prompt = request.POST.get('user_prompt')
        genai.configure(api_key=getattr(settings, 'GOOGLE_API_KEY', ''))
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_text(prompt)
        return JsonResponse({'response': response})
    else:
        return render(request, 'prediction/prompt.html')