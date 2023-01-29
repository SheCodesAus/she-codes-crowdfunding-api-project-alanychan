from django.http import JsonResponse

def custom404(request, exception=None):
    return JsonResponse({
        'status_code': 404,
        'error': 'Page not found. Please try again.'
    })

def custom202(request,exception=None):
    return JsonResponse({
        'status_code': 202,
        'message': 'Request successful.'
    })

