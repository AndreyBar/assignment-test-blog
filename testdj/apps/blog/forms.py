from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser, Comment


class SignUpForm(UserCreationForm):
    email 	  = forms.EmailField(max_length=254)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password again', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2', )


class CommentForm(forms.ModelForm):
	text = forms.CharField(max_length=500, widget=forms.Textarea())

	class Meta:
		model = Comment
		fields = ('text', )