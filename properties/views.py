from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property

@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all()
    if request.GET.get("format") == "json":
        data = [
            {
                "id": prop.id,
                "title": prop.title,
                "description": prop.description,
                "price": str(prop.price),
                "location": prop.location,
                "created_at": prop.created_at.isoformat(),
            }
            for prop in properties
        ]
        return JsonResponse({"data": data})
    return render(request, 'properties/property_list.html', {'properties': properties})
