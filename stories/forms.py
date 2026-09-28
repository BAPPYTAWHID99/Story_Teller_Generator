from django import forms

from .story_data import GENRE_CHOICES, MOOD_CHOICES, STORY_LENGTH_CHOICES


class StoryForm(forms.Form):
    genre = forms.ChoiceField(choices=GENRE_CHOICES, label='Genre')
    main_character = forms.CharField(
        max_length=255,
        label='Main Character',
        widget=forms.TextInput(attrs={'placeholder': 'A young engineer'}),
    )
    location = forms.CharField(
        max_length=255,
        label='Location',
        widget=forms.TextInput(attrs={'placeholder': 'A mysterious city'}),
    )
    theme = forms.CharField(
        max_length=255,
        label='Theme',
        widget=forms.TextInput(attrs={'placeholder': 'Friendship'}),
    )
    mood = forms.ChoiceField(choices=MOOD_CHOICES, label='Mood')
    story_length = forms.ChoiceField(choices=STORY_LENGTH_CHOICES, label='Story Length')

    def clean_main_character(self):
        value = self.cleaned_data['main_character'].strip()
        if not value:
            raise forms.ValidationError('Main character is required.')
        if len(value) < 2:
            raise forms.ValidationError('Main character must be at least 2 characters long.')
        return value

    def clean_location(self):
        value = self.cleaned_data['location'].strip()
        if not value:
            raise forms.ValidationError('Location is required.')
        if len(value) < 2:
            raise forms.ValidationError('Location must be at least 2 characters long.')
        return value

    def clean_theme(self):
        value = self.cleaned_data['theme'].strip()
        if not value:
            raise forms.ValidationError('Theme is required.')
        if len(value) < 2:
            raise forms.ValidationError('Theme must be at least 2 characters long.')
        return value

    def clean_genre(self):
        value = self.cleaned_data['genre']
        valid_values = [choice[0] for choice in GENRE_CHOICES]
        if value not in valid_values:
            raise forms.ValidationError('Please select a valid genre.')
        return value

    def clean_mood(self):
        value = self.cleaned_data['mood']
        valid_values = [choice[0] for choice in MOOD_CHOICES]
        if value not in valid_values:
            raise forms.ValidationError('Please select a valid mood.')
        return value

    def clean_story_length(self):
        value = self.cleaned_data['story_length']
        valid_values = [choice[0] for choice in STORY_LENGTH_CHOICES]
        if value not in valid_values:
            raise forms.ValidationError('Please select a valid story length.')
        return value
