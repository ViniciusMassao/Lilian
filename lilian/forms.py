from django import forms

temas = [
    (0, 'Artes'),
    (1, 'Biologia'),
    (2, 'Arquitetura'),
    (3, 'Musica'),
    (4, 'Jogos')
]

class HomeForm(forms.Form):
    tema = forms.ChoiceField(label = 'Escolha o tema', choices=temas)
    #selection = forms.Select()