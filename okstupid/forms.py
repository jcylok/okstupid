from django import forms
from .models import Profile

class ProfileForm (forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('nickname', 'gender', 'age', 'height', 'location', 'job_title', 'education', 'hometown', 'drinker', 'smoker', 'photo_one', 'photo_two', 'photo_three', 'prompt_one', 'prompt_two', 'prompt_three', 'age_preference_max', 'age_preference_min', 'gender_preference')
