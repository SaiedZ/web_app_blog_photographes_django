from django import forms
from . import models
from django.contrib.auth import get_user_model


class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']


class BlogForm(forms.ModelForm):
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Blog
        fields = ['title', 'content']


class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)


User = get_user_model()


class FollowUsersForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['follows']


class ChooseForm(forms.Form):

    def __init__(self, user, *args, **kwargs):
        super(ChooseForm, self).__init__(*args, **kwargs)
        self.fields['follows'].queryset = User.objects.exclude(user).filter(user__role='CREATOR')

    q_set = User.objects.all()

    follows = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=q_set)
