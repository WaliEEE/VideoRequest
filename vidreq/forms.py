from django import forms

class vform(forms.Form):
	name = forms.CharField(max_length=20, 
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Name',
			'id': 'inputName'
			}))

	comment = forms.CharField(widget=forms.Textarea({
		'class': 'form-control',
		'rows': '5',
		'id': 'inputComment',
		'placeholder': 'Comment'

		}))