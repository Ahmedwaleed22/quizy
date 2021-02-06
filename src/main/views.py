from django.shortcuts import render
from django.views import View
import requests
import json

# Create your views here.

class index(View):
    def get(self, request):
        # Request The Api And Get Data
        response = requests.get('https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple')
        apidata = response.json()
        # Get The Data
        res = apidata['results']
        answers = [] # List To Add Answers
        # Extends The Incorrect Answers List To The Answers List
        answers.extend(res[0]['incorrect_answers'])
        # Append The Correct Answer To The Answers List
        answers.append(res[0]['correct_answer'])
        return render(request, "index.html", {
            "questions": json.dumps(res),
        })

class scored(View):
    def post(self, request):
        return render(request, "scored.html", {
            "points": request.POST['totalpoints']
        })