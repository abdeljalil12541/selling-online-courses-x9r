from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class ProfileForm(UserChangeForm):
	class Meta:
		model=User
		fields=('username', 'email')