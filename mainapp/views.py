from django.views.generic import TemplateView
from mainapp import models as mainapp_models

class MainPageView(TemplateView):
    template_name = "mainapp/index.html"
    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context["menu_obj"] = mainapp_models.Menu.objects.all()
        context["in_menu"] = mainapp_models.InMenu.objects.all()
        return context 

class Page1View(TemplateView):
    template_name = "mainapp/1.html"

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context["menu_obj"] = mainapp_models.Mainmenu.objects.all()
        return context 



class Page2View(TemplateView):
    template_name = "mainapp/2.html"
    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context["menu_obj"] = mainapp_models.Mainmenu.objects.all()
        return context 


