from django.views.generic import FormView , ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render 
from .forms import EnderecoForm 
from .models import Endereco 
import requests
import certifi 


# Define uma view baseada em classe que herda de FormView.
class ViaCepFormView(FormView):
    # Define o nome do arquivo de template que será renderizado por esta view.
    template_name = 'endereco.html'
    # Especifica a classe do formulário que esta view irá gerenciar (definida em forms.py).
    form_class = EnderecoForm
    # Define a URL para a qual o usuário será redirecionado após um envio bem-sucedido. '.' significa a página atual.
    success_url = '.'

    # Este método é chamado quando os dados do formulário são válidos.
    def form_valid(self, form):
        # Obtém o valor limpo e validado do campo 'cep' do formulário.
        cep = form.cleaned_data['cep'] 
        # Faz uma requisição GET para a API ViaCEP com o CEP fornecido. `verify=certifi.where()` garante a verificação SSL.
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json", verify=certifi.where())

        # Verifica se a requisição à API foi bem-sucedida (código de status 200).
        if response.status_code == 200:
            # Converte a resposta JSON da API em um dicionário Python.
            data = response.json()
            # Verifica se a API retornou um erro (ex: CEP não encontrado).
            if data.get('erro'):
                # Adiciona uma mensagem de erro ao contexto para ser exibida no template.
                return self.render_to_response(self.get_context_data(form=form, error_message='CEP não encontrado.'))
            
            # Cria uma nova instância do modelo Endereco com os dados retornados pela API.
            endereco, created = Endereco.objects.update_or_create(
                cep=data.get('cep').replace('-', ''), # Usa o CEP como chave para evitar duplicatas
                defaults={
                    'rua': data.get('logradouro'),
                    'bairro': data.get('bairro'),
                    'cidade': data.get('localidade'),
                    'estado': data.get('uf')
                }
            )
            # Renderiza novamente a página, passando o formulário e o objeto de endereço encontrado/criado para o contexto.
            return self.render_to_response(self.get_context_data(form=form, endereco=endereco))
        else:
            # Se a API falhar (status diferente de 200), adiciona uma mensagem de erro genérica.
            error_message = 'Não foi possível consultar o CEP. Tente novamente.'
            return self.render_to_response(self.get_context_data(form=form, error_message=error_message))

    # Este método é chamado se o formulário for inválido (ex: campo 'cep' vazio).
    def form_invalid(self, form):
        # Renderiza a página novamente, exibindo os erros de validação do formulário.
        return self.render_to_response(self.get_context_data(form=form))
    
class ViaCeplistView(ListView):
    template_name = 'listagem.html'
    model = Endereco
    context_object_name = 'enderecos'

class ViaCepDeleteView(DeleteView):
    template_name = 'deletar.html'
    model = Endereco
    success_url = reverse_lazy("listagem")  

class ViaCepDetailView(DetailView):
    template_name = 'detalhar.html'
    model = Endereco
    

