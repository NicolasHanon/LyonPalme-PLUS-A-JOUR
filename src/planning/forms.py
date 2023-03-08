from django.forms import ModelForm
from .models import ENTRAINEMENT
from django import forms

class ENTRAINEMENTForm(ModelForm):
    class Meta:
        model = ENTRAINEMENT
        fields = ['Titre', 'DateEntrainement', 'NomPartie1', 'Partie1', 'TempsPartie1', 'DistancePartie1', 'NomPartie2', 'Partie2', 'TempsPartie2', 'DistancePartie2', 'NomPartie3', 'Partie3', 'TempsPartie3', 'DistancePartie3']
        widgets = {
            'Titre': forms.TextInput(attrs={'class': 'form-control'}),
            'DateEntrainement': forms.DateInput(attrs={'class': 'form-control'}),
            'NomPartie1': forms.TextInput(attrs={'class': 'form-control'}),
            'Partie1': forms.Textarea(attrs={'class': 'form-control'}),
            'TempsPartie1': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'DistancePartie1': forms.TextInput(attrs={'class': 'form-control'}),
            'NomPartie2': forms.TextInput(attrs={'class': 'form-control'}),
            'Partie2': forms.Textarea(attrs={'class': 'form-control'}),
            'TempsPartie2': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'DistancePartie2': forms.TextInput(attrs={'class': 'form-control'}),
            'NomPartie3': forms.TextInput(attrs={'class': 'form-control'}),
            'Partie3': forms.Textarea(attrs={'class': 'form-control'}),
            'TempsPartie3': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'DistancePartie3': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Titre'].label = 'Titre de l\'entrainement\r'
        self.fields['DateEntrainement'].label = 'Date de l\'entrainement'
        self.fields['NomPartie1'].label = 'Echauffement'
        self.fields['Partie1'].label = 'Contenu de l\'échauffement'
        self.fields['TempsPartie1'].label = 'Durée (hh:mm)'
        self.fields['DistancePartie1'].label = 'Distance (en m)'
        self.fields['NomPartie2'].label = 'Intitulé de l\'exercice 1'
        self.fields['Partie2'].label = 'Contenu de l\'exercice'
        self.fields['TempsPartie2'].label = 'Durée (hh:mm)'
        self.fields['DistancePartie2'].label = 'Distance (en m)'
        self.fields['NomPartie3'].label = 'Initulé de l\'exercice 2'
        self.fields['Partie3'].label = 'Contenu de l\'exercice'
        self.fields['TempsPartie3'].label = 'Durée (hh:mm)'
        self.fields['DistancePartie3'].label = 'Distance (en m)'