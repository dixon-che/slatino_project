from slatino.apps.Institute.models import Institute


def person_processor(request):
    all_institute = Institute.objects.filter(published=True)
    return {"all_institute": all_institute}
