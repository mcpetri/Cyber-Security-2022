from django import forms

class ShoutForm(forms.Form):
	shout_text = forms.CharField(label='shout_text', max_length=200)
	shout_author = forms.CharField(label='author_text', max_length=50)