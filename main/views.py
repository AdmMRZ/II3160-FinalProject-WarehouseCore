import json
import os
import functools
from dotenv import load_dotenv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import PackageService

service = PackageService()
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

def token_required(view_func):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header == f"Bearer {API_TOKEN}":
            return view_func(request, *args, **kwargs)
        return JsonResponse({"error": "Unauthorized"}, status=401)
    return wrapper

@csrf_exempt
@token_required
def package_list_create(request):
    if request.method == 'GET':
        packages = service.repo.get_all_packages()
        return JsonResponse(list(packages.values()), safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        new_pkg = service.register_new_package(body)
        return JsonResponse({"id": new_pkg.id, "status": new_pkg.status}, status=201)

@csrf_exempt
@token_required
def package_detail(request, pk):
    if request.method == 'GET':
        pkg = service.repo.get_package_by_id(pk)
        return JsonResponse({"id": pkg.id, "name": pkg.name, "shipping_cost": pkg.shipping_cost, "status": pkg.status}) if pkg else JsonResponse({}, status=404)
    elif request.method == 'PATCH':
        body = json.loads(request.body)
        updated = service.repo.update_package(pk, body)
        return JsonResponse({"message": "Updated", "status": updated.status}) if updated else JsonResponse({}, status=404)