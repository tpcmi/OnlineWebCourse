from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from apps.organizations.models import CourseOrg, City


class OrgView(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        org_nums = CourseOrg.objects.count()
        all_citys = City.objects.all()
        hot_orgs = all_orgs.order_by("-click_nums")[:3]

        category = request.GET.get("ct", "")
        if category:
            all_orgs = all_orgs.filter(category=category)

        city_id = request.GET.get("city", "")
        if city_id and city_id.isdigit():
            all_orgs = all_orgs.filter(city_id=int(city_id))

        sort_org = request.GET.get("sort", "")
        if sort_org == "students":
            all_orgs = all_orgs.order_by("-students")
        elif sort_org == "courses":
            all_orgs = all_orgs.order_by("-course_nums")

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, per_page=10, request=request)
        orgs = p.page(page)

        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "org_nums": org_nums,
            "all_citys": all_citys,
            "category": category,
            "city_id": city_id,
            "sort_org": sort_org,
            "hot_orgs": hot_orgs
        })
