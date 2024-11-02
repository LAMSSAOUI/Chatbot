from django.shortcuts import render , redirect
from django.http import JsonResponse
import requests
import os
from dotenv import load_dotenv
from .models import Users


load_dotenv()

EDAMAM_APP_ID = os.getenv('EDAMAM_APP_ID')
EDAMAM_APP_KEY = os.getenv('EDAMAM_APP_KEY')


def index(request):
    return render(request, 'chatbot/index.html')


def get_recipe(request):
    query = request.GET.get('query', '').strip()

    if not query:
        return JsonResponse({'error': 'Query parameter is required.'}, status=400)

    try:
        url = f"https://api.edamam.com/search?q={query}&app_id={EDAMAM_APP_ID}&app_key={EDAMAM_APP_KEY}&from=0&to=10"  # Fetch 10 recipes
        response = requests.get(url)
        data = response.json()

        if data.get("hits"):
            recipes = []
            for hit in data["hits"]:
                recipe = hit["recipe"]
                recipes.append({
                    'label': recipe['label'],
                    'ingredients': recipe['ingredientLines'],
                    'url': recipe['url']
                })
            return JsonResponse({'recipes': recipes})
        else:
            return JsonResponse({'error': 'No recipes found.'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def login(request) :
    return render(request, 'chatbot/login.html')
def signup(request) :
    return render(request, 'chatbot/signup.html')



def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Optional: Set some default favorites if desired, or let it be empty
        favorites = []

        # Create a new user
        new_user = Users(name=name, email=email, password=password, favorites=favorites)
        new_user.save()

        # Redirect to a success page or the same form with a success message
          # Replace 'success' with your actual success page URL name

        return render(request, 'chatbot/index.html')
    return redirect('chatbot/404.html') # Replace with your actual template name


# def success(request):
#     return render(request, 'success.html')