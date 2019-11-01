from django.views.generic import View, ListView
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Persona, Codigo
from .models import PersonaForm
from .filters import SnippetFilter


class PersonaList(ListView):
    template_name = "pruebaformularios/personas_list.html"
    model = Persona

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['filter'] = SnippetFilter(self.request.GET, queryset=self.get_queryset())
        return context


def add_persona(request):

    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():

            new_persona = form.save()
        form = PersonaForm()
        return render(request, 'pruebaformularios/gracias.html')
    else:
        form = PersonaForm()
    return render(request, 'pruebaformularios/persona_form.html', {'form': form})

