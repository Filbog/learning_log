from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    privacy_choices = [
        (True, "Public"),
        (False, "Private"),
    ]

    public = forms.ChoiceField(
        choices=privacy_choices, widget=forms.RadioSelect, initial=False
    )

    class Meta:
        model = Topic
        fields = ["text", "public"]
        labels = {"text": ""}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
