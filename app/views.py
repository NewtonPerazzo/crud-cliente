from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from app.form import ClienteForm
from app.models import Cliente

@login_required
def home(request):
    cliente = Cliente.objects.all().order_by('data_cadastro').filter(user=request.user)
    return render(request, 'app/home.html', {'cliente': cliente})


@login_required
def editar(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(instance=cliente)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            cliente.save()
            return redirect('/')
        else:
            return render(request, 'app/editar.html', {'form': form, 'cliente': cliente})

    else:
        return render(request, 'app/editar.html', {'form': form, 'cliente': cliente})



@login_required
def cadastrar(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)

        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.user = request.user
            cliente.save()
            return redirect('/')

    else:
        form = ClienteForm()
        return render(request, 'app/cadastrar.html', {'form': form})

@login_required
def deletar(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    return redirect('/')