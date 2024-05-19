from django.shortcuts import render
from django.views.generic  import TemplateView

def home(request):
    return render(request, 'pages/home.html')

class HomeView(TemplateView):
    template_name = "pages/home.html" 

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
