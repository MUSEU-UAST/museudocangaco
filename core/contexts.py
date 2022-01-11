from django.urls import resolve


def url_name(request):
    return {'url_name': resolve(request.path).url_name}
