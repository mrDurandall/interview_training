from .models import HitCount


def hit_count_middleware(get_response):

    def middleware(request):
        if request.user.is_authenticated:
            hc, created = HitCount.objects.get_or_create(path=request.path, user=request.user)
            if not created:
                hc.hits += 1
            hc.save()

        response = get_response(request)
        return response

    return middleware

