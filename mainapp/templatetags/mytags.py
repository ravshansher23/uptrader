from django import template
from django.urls import reverse
from mainapp.models import Mainmenu
register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def show_top_menu(context):
    menu_obj = Mainmenu.objects.all()
    return {
        "menu_obj": menu_obj,
        
    }
