from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Organization



def organization(request):
    # key = 1
    # logged_in_user = Organization.objects.filter(key=organization.id)
    # logged_in_user_dict = {
    #     'Org': logged_in_user
    # }
    # return render(request, 'org.html', logged_in_user_dict)

    context = {
        'organizations': Organization.objects.all()
    }
    return render(request, 'org.html', context)


# from django.http import HttpResponse
#
#
# def organization(request):
#     return HttpResponse('Hello, World!')
