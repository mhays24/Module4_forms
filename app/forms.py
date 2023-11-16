from django import forms    
class HeyYouForm(forms.Form):
    name = forms.CharField()

class AgeInForm(forms.Form):
    year = forms.CharField()
    BYear = forms.CharField()

class OrderTotalForm(forms.Form):
    burgers = forms.IntegerField()
    fries = forms.IntegerField()
    drinks = forms.IntegerField()


class FontTimesForm(forms.Form):
    text = forms.CharField()
    number = forms.IntegerField()