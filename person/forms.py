from django.forms import ModelForm
from person.models import Participant

# Create the form class.
class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = ['first_name', 'last_name', 'email', 'birth_date',
                  'phone_number', 'english_level', 'gender', 'python_practice_since', 'django_practice_since', 'os']