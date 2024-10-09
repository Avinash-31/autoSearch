# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
import pyautogui as rocky
import time
import random
import json
from .questions import question

def open_edge_with_run_command():
    rocky.hotkey('win', 'r')
    time.sleep(1)
    rocky.typewrite('msedge')
    time.sleep(1)
    rocky.press('enter')
    time.sleep(3)

def google_search(query):
    rocky.typewrite(query, interval=0.04)
    rocky.press('enter')
    time.sleep(random.uniform(1, 4))

def close_edge():
    rocky.hotkey('alt', 'f4')
    time.sleep(1)

def open_edge(request):
    open_edge_with_run_command()
    return JsonResponse({'message': 'Edge opened successfully!'})

def search(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        num_questions = data.get('num_questions')
        
        try:
            num_questions = int(num_questions)
        except ValueError:
            return JsonResponse({'error': 'Invalid number of questions'}, status=400)
        
        if num_questions < 1:
            return JsonResponse({'error': 'Number of questions should be greater than 0'}, status=400)
        
        open_edge_with_run_command()
        random_questions = random.sample(question, num_questions)
        for query in random_questions:
            google_search(" " + query)
            time.sleep(3)
        close_edge()
        return JsonResponse({'message': 'Search completed successfully!'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def search_mobile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        num_questions = data.get('num_questions')
        random_questions = random.sample(question, num_questions)
        for query in random_questions:
            # Simulate typing the query on a mobile device
            print(f"Please search for: {query}")
            time.sleep(3)
        return JsonResponse({'message': 'Search completed successfully on mobile!'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def Home(request):
    return render(request, 'auto_search/Home.html')
