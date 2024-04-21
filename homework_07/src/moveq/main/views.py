from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, UpdateView

from main.models import Engineer


# Create your views here.
class EngineersListView(ListView):
    model = Engineer


class EngineerUpdateView(UpdateView):
    model = Engineer
    fields = "__all__"
    success_url = "/engineers/"


def index(request):
    return redirect("/engineers/")
