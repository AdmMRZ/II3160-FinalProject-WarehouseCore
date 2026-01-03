import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import WarehouseService

service = WarehouseService()

@csrf_exempt
def package_list_create(request):
    if request.method == 'GET':
        packages = service.repo.get_all_packages()
        data = list(packages.values())
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        body = json.loads(request.body)
        new_package = service.register_new_package(body)
        return JsonResponse({
            "id": new_package.id,
            "name": new_package.name,
            "cost": float(new_package.shipping_cost)
        }, status=201)

@csrf_exempt
def set_package_ready(request, pk):
    if request.method == 'PATCH':
        updated = service.mark_as_ready(pk)
        if updated:
            return JsonResponse({"id": updated.id, "status": updated.status})
        return JsonResponse({"error": "Package not found or already processed"}, status=404)