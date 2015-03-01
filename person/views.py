from django.http import HttpResponse
from django.template import RequestContext, loader
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from person.models import Participant
from person.forms import ParticipantForm,MentorForm

def index(request):
    participants_list = Participant.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
            'participants_list': participants_list,
        })
    return HttpResponse(template.render(context))
def create_participant(request):
    if request.method == 'POST':
        formset = ParticipantForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = ParticipantForm()
    return render_to_response("participants.html", {"form": formset})
def create_mentor(request):
    if request.method == 'POST':
        formset = MentorForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = MentorForm()
    return render_to_response("mentors.html", {"form": formset})

        