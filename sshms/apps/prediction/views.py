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

        # Prepare the user's profile data as input
        input_data = [f"{field.verbose_name}: {getattr(profile, field.name)}" for field in profile._meta.fields if field.name != 'user']
        input_prompt = "\n".join(input_data)

        # Prepare a few examples for few-shot learning
        examples = [
            "Example 1:\nInput: Age: 45\nSex: Male\nEthnicity/Race: Caucasian\nSocioeconomic Status: Middle-class\nFamily History of Chronic Diseases: Heart disease, hypertension\nDiagnosed Chronic Conditions: None\nMedications: None\nSurgeries: None\nTypical Daily Diet: Moderate\nPhysical Activity Frequency: 2-3 times per week\nSmoking Habits: Non-smoker\nAlcohol Consumption: Occasional\nRecreational Drug Use: None\nStress Management Methods: Meditation\nHeight: 175\nWeight: 80\nBlood Pressure: 135/85\nCholesterol Levels: 210 mg/dL\nBlood Glucose Levels: 95 mg/dL\nOutput: Predicted Chronic Disease: Hypertension\nDietary Advice: Reduce sodium intake, increase potassium-rich foods, and follow a DASH diet. Limit saturated fats and cholesterol.",

            "Example 2:\nInput: Age: 62\nSex: Female\nEthnicity/Race: African American\nSocioeconomic Status: Low-income\nFamily History of Chronic Diseases: Type 2 diabetes, obesity\nDiagnosed Chronic Conditions: Type 2 diabetes\nMedications: Metformin\nSurgeries: None\nTypical Daily Diet: High in processed foods, sugary drinks\nPhysical Activity Frequency: Sedentary\nSmoking Habits: Former smoker\nAlcohol Consumption: None\nRecreational Drug Use: None\nStress Management Methods: None\nHeight: 160\nWeight: 95\nBlood Pressure: 145/90\nCholesterol Levels: 240 mg/dL\nBlood Glucose Levels: 180 mg/dL\nOutput: Predicted Chronic Disease: Type 2 Diabetes\nDietary Advice: Follow a low-carb, high-fiber diet with limited sugars and processed foods. Eat more fruits, vegetables, and lean proteins. Maintain a healthy weight through diet and exercise.",

            "Example 3:\nInput: Age: 35\nSex: Male\nEthnicity/Race: Asian\nSocioeconomic Status: Upper-class\nFamily History of Chronic Diseases: None\nDiagnosed Chronic Conditions: None\nMedications: None\nSurgeries: None\nTypical Daily Diet: Fast food, high in saturated fats\nPhysical Activity Frequency: Sedentary\nSmoking Habits: Smoker\nAlcohol Consumption: Heavy\nRecreational Drug Use: None\nStress Management Methods: None\nHeight: 170\nWeight: 95\nBlood Pressure: 130/80\nCholesterol Levels: 220 mg/dL\nBlood Glucose Levels: 105 mg/dL\nOutput: Predicted Chronic Disease: Risk of cardiovascular disease, obesity\nDietary Advice: Reduce intake of saturated fats, trans fats, and cholesterol. Increase consumption of fruits, vegetables, and whole grains. Limit alcohol consumption and quit smoking.",

            "Example 4:\nInput: Age: 50\nSex: Female\nEthnicity/Race: Hispanic\nSocioeconomic Status: Middle-class\nFamily History of Chronic Diseases: Breast cancer\nDiagnosed Chronic Conditions: None\nMedications: None\nSurgeries: None\nTypical Daily Diet: High in processed meats, red meat\nPhysical Activity Frequency: 1-2 times per week\nSmoking Habits: Non-smoker\nAlcohol Consumption: Moderate\nRecreational Drug Use: None\nStress Management Methods: Yoga\nHeight: 165\nWeight: 70\nBlood Pressure: 120/75\nCholesterol Levels: 180 mg/dL\nBlood Glucose Levels: 90 mg/dL\nOutput: Predicted Chronic Disease: Risk of breast cancer, colorectal cancer\nDietary Advice: Limit intake of processed and red meats. Increase consumption of fruits, vegetables, and whole grains. Maintain a healthy weight through diet and exercise."
        ]

        prompt = "\n\n".join(examples) + "\n\nInput: " + input_prompt + "\nOutput:"

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