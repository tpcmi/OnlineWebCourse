from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from apps.organizations.models import CourseOrg


@csrf_exempt
def test_upload(requests):
    if requests.method == "GET":
        return HttpResponse("<P1>OK</P1>")
    name = requests.POST["name"]
    desc = requests.POST["desc"]
    tag = requests.POST["tag"]
    category = requests.POST["category"]
    click_nums = requests.POST["click_nums"]
    fav_nums = requests.POST["fav_nums"]
    logo = requests.FILES["logo"]
    CourseOrg.objects.create(name=name, desc=desc, tag=tag, category=category, click_nums=click_nums, fav_nums=fav_nums,
                             logo=logo)
    # CourseOrg.objects.create(requests.POST)
    return HttpResponse("NICE")
