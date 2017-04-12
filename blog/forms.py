from django import forms
from .models import Post

class RegistrationForm(forms.Form):
	username = forms.CharField(label='Username', max_length=30)
	email = forms.EmailField(label='Email')
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
	password2 = forms.CharField(label='Password (Again)', widget=forms.PasswordInput())
	
	def get_username(self):
		return self.cleaned_data['username']
	
	def get_email(self):
		return self.cleaned_data['email']
	
	def get_password(self):
		if 'password1' in self.cleaned_data:
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']
			if password1 == password2:
				return password2
			else:
				return False
		
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text',)