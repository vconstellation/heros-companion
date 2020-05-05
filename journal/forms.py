from django import forms
from .models import CharSheet
from .validators import validate_attrs

#choices for the radio buttons in CharSheetCreation class
prof_choices = [
    ('Fighter', 'Fighter'),
    ('Paladin', 'Paladin'),
    ('Ranger', 'Ranger'),
    ('Monk', 'Monk'),
    ('Druid', 'Druid'),
    ('Rogue', 'Rogue'),
    ('Bard', 'Bard'),
    ('Wizard', 'Wizard'),
    ('Sorcerer', 'Sorcerer'),
    ('Warlock', 'Warlock')
]

class CharSheetCreation(forms.ModelForm):
    prof = forms.ChoiceField(choices=prof_choices, widget=forms.RadioSelect())
    attrs_str = forms.IntegerField(validators=[validate_attrs])
    attrs_dex = forms.IntegerField(validators=[validate_attrs])
    attrs_con = forms.IntegerField(validators=[validate_attrs])
    attrs_int = forms.IntegerField(validators=[validate_attrs])
    attrs_wis = forms.IntegerField(validators=[validate_attrs])
    attrs_cha = forms.IntegerField(validators=[validate_attrs])

    class Meta:
        model = CharSheet
        exclude = ['author']