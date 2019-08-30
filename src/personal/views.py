from django.shortcuts import render
from personal.models import Question

# Create your views here.
def home_screen_view(request):
    context = {}
    #context['some_string'] = "this is some string"
    #context['some_number'] = 213213
    #context = {
    #    'some_string': "this is some string",
    #    'some_number': 12312312
    #}
    #list_of_values = []
    #list_of_values.append("first entry")
    #list_of_values.append("second entry")
    #list_of_values.append("third entry")
    #list_of_values.append("fourth entry")
    #context['list_of_values'] = list_of_values
    questions = Question.objects.all()
    context["questions"] = questions
    return render(request, "personal/home.html", context)
