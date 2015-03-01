from django.http import HttpResponse
from django.template import RequestContext, loader

from person.models import Participant
def index(request):
    participants_list = Participant.objects.all()
    template = loader.get_template('person/index.html')
    context = RequestContext(request, {
            'participants_list': participants_list,
        })
    return HttpResponse(template.render(context))