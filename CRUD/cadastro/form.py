from django.forms import ModelForm
from .models import Pessoas

# Formulario para adicionar pessoas novas ao db.
# usa um metodo proprio do django pra criar forms.
class pessoasform(ModelForm):
    class Meta:
        model = Pessoas
        fields = ['cpf', 'nome', 'profissão']
