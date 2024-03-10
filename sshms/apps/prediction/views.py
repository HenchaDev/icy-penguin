from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
from django.conf import settings
from apps.users.models import UserProfile

# Create your views here.
def generate_text(request):
    if request.method == 'POST':
        try:
            profile = request.user.userprofile
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'User profile does not exist!'})
        
        prompt_parts = []
        for field in profile._meta.fields:
            if field.name != 'user':
                field_value = getattr(profile, field.name)
                prompt_parts.append(f"{field.verbose_name}: {field_value}")
        prompt = ". ".join(prompt_parts)        
            
        genai.configure(api_key=getattr(settings, 'GOOGLE_API_KEY', ''))
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        generated_text = response.text
        return JsonResponse({'response': generated_text})
    else:
        return render(request, 'prediction/prompt.html')
    
def format_response(response_text):
    sections = response_text.split('\n\n')
    
    html_sections = []
    for section in sections:
        paragraphs = ['<p>{}</p>'.format(p.strip()) for p in section.split('\n')]
        html_section = '\n'.join(paragraphs)
        html_sections.append(html_section)
    
    formatted_response = '\n'.join(html_sections)
    return formatted_response