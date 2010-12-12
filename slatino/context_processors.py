from slatino.Institute.models import Institute, Room


def personalee_processor(request):
    all_institute = Institute.objects.all()
    return {"all_institute": all_institute}
