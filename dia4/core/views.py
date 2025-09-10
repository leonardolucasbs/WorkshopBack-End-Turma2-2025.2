from django.shortcuts import render
from .models import Endereco
from .forms import EnderecoForm
import requests

# Create your views here.
def home(request):
    return render(request, 'home.html')

def consulta_cep(request):
    form = EnderecoForm(request.GET or None)
    if form.is_valid():
        cep = form.cleaned_data['cep']
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        
        if response.status_code == 200:
            data = response.json()
            endereco = Endereco.objects.create(
                cep=data.get('cep'),
                rua=data.get('logradouro'),
                bairro=data.get('bairro'),
                cidade=data.get('localidade'),
                estado=data.get('uf')
            )
            endereco.save()
            return render(request, 'endereco.html', {'form': form, 'endereco': endereco})
        
          