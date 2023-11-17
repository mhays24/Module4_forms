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


class NoTeenSumForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()


class XyzThereForm(forms.Form):
    word = forms.CharField()


class CenteredAverageForm(forms.Form):
    numbers = forms.CharField(label="Enter numbers (comma separated)")
