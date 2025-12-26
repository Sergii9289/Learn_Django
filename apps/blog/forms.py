from django import forms
from .models import Profile


class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

    # замінюємо поле name на вибір із БД
    author = forms.ModelChoiceField(
        queryset=Profile.objects.all(),
        label="Автор"
    )