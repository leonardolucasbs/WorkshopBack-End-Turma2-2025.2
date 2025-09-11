

from django.urls import path
from .views import ViaCepFormView, ViaCeplistView, ViaCepDetailView, ViaCepDeleteView

urlpatterns = [
   path('', ViaCepFormView.as_view(), name='consulta'),
   path('listagem/', ViaCeplistView.as_view(), name='listagem'),
   path('detalhar/<int:pk>/', ViaCepDetailView.as_view(), name='detalhar'),
   path('deletar/<int:pk>/', ViaCepDeleteView.as_view(), name='deletar'),
]
