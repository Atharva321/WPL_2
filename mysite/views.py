from django.http import HttpResponse
from django.template import Context, loader


def index(request):

    return HttpResponse(
        '<h2>Hello  I am Atharva.My PRN is 1841038 and studying TY Computer in GCOEJ</h2>'
    )
