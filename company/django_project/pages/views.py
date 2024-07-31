from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

class AutoPageView(TemplateView):
  template_name = "about.html"
  
  def get_context_data(self, **kwargs) :
    context = super().get_context_data(**kwargs)
    context["contact_address"] = "123 main street"
    context["phone_number"] = "555-555-555"
    return context
    
    
def home_page_view(request) :
  context = {
    "inventory_list" : ["widget-1", "widget-2", "widget-3"],
    "greetings" : "Thank you for visiting"
  }
  return render(request, "home.html", context)