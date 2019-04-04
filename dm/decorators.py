from django.http import Http404
from functools import wraps, partial


def ajax_required(function):
    @wraps(ajax_required)
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404
        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    # wrap.__name__ = function.__name__
    return wrap
