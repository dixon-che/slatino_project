from slatino.apps.Institute.models import Institute


def personalee_processor(request):
    all_institute = Institute.objects.all()
    return {"all_institute": all_institute}
