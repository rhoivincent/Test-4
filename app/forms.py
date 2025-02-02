from django import forms
from .models import Feedback , Resource

class FeedbackUpdateForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comments']  # Exclude 'resource' as it's readonly

    def __init__(self, *args, **kwargs):
        # Pass the resource data explicitly from the view
        feedback_instance = kwargs.get('instance')
        if feedback_instance:
            # If the instance exists, we can set the resource manually
            kwargs['initial'] = kwargs.get('initial', {})
            kwargs['initial']['resource'] = feedback_instance.resource.name  # Set the initial resource value
        super().__init__(*args, **kwargs)
