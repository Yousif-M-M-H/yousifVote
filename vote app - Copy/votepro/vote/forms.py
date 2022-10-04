from django.forms import ModelForm

from .models import Voting


class VoteForm(ModelForm):
    class Meta:
        model = Voting
        fields = ['text', 'choice1', 'choice2', 'choice3',
                  'choice1_count', 'choice2_count', 'choice3_count']
