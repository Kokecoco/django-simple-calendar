from django.shortcuts import render

def seating(request):
    return render(request, 'seating.html')
