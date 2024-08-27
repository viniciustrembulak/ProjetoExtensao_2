from django.shortcuts import render, redirect
from .forms import AgendamentoForm

def agendar_servico(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendamento:confirmacao')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamento.html', {'form': form})

def confirmacao(request):
    return render(request, 'agenda/confirmacao.html')
