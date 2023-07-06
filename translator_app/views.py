from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
import requests

def translate(request):
    if request.method == 'POST':
        text_to_translate = request.POST.get('text_to_translate', '')

        # Make API request using requests library
        api_url = 'https://api.mymemory.translated.net/get'
        apiKey = "23c58b602f76763d47b5"
        username = "apiuuagou@gmail.com"
        password = "Apiudaai"
        langpair = 'en|sw'  # English to Swahili translation example
        params = {
            'q': text_to_translate,
            'langpair': langpair,
            'key': apiKey,
            'user': username,
            'pass': password
        }
        response = requests.get(api_url, params=params)
        translation_data = response.json()

        translated_text = translation_data['responseData']['translatedText']

        # Save the translation in the database
        translation = Translation.objects.create(text_to_translate=text_to_translate, translated_text=translated_text)

        return JsonResponse({'translated_text': translated_text})
    else:
        return JsonResponse({'error': 'Invalid request method.'})
