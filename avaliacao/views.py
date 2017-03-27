import datetime
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import TemplateView

from avaliacao.models import QuestionarioForm, CandidatoForm, Email


def questionario(request):
    if request.method == "POST":
        form = QuestionarioForm(request.POST)
        if form.is_valid():
            questionario = form.save()
            questionario.create_at = datetime.datetime.now()
            questionario.save()
            Email(questionario).enviar()
            return redirect('finalizado')
    else:
        form = QuestionarioForm()
    return render(request, 'avaliacao/questionario.html', {'form': form})


class FinalizarView(TemplateView):
    template_name = "avaliacao/finalizar.html"

    def get_context_data(self, **kwargs):
        context = super(FinalizarView, self).get_context_data(**kwargs)
        return context


def candidato(request):
    if request.method == "POST":
        form = CandidatoForm(request.POST)
        if form.is_valid():
            candidato = form.save()
            candidato.create_at = datetime.datetime.now()
            candidato.save()
            return redirect('questionario')
    else:
        form = CandidatoForm()
    return render(request, 'avaliacao/candidato.html', {'form': form})
