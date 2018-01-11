from django.shortcuts import render

import logging
log = logging.getLogger('djinn_core')

def djinn_server_error(request, template_name="500.html"):
    return render(request, template_name, {})
