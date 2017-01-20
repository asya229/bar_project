from django.shortcuts import render

def page_list(request):
    return render(request, 'barmetro/page_list.html', {})