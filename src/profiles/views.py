from django.conf import settings
from django.shortcuts import render_to_response,RequestContext,Http404,HttpResponseRedirect,HttpResponse
from django.template.defaultfilters import slugify
from django.forms.models import modelformset_factory

from.models import UserPurchase


def library(request):
    if request.user.is_authenticated():
        products = request.user.userpurchase.products.all()
        return render_to_response("profiles/library.html", locals(),context_instance=RequestContext(request))


    else:
        raise Http404
