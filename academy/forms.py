from django import forms
from django.forms import formset_factory
from .models import Score, Term
from .models import Subject, Level

subject_choices = (
(i.id, i.subject) for i in Subject.objects.filter(active=True)
)
level_choices = (
(i.id, str(i.term) +' '+ str(i.level)) for i in Level.objects.all()
)

class PreScoreForm(forms.Form):
    subject = forms.ChoiceField(choices=subject_choices)
    level = forms.ChoiceField(choices=level_choices)



class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        exclude = []

ScoreFormSet = formset_factory(ScoreForm,)

class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        exclude = []


