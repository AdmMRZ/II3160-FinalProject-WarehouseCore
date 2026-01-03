from .models import Package

class PackageRepository:
    @staticmethod
    def create_package(data):
        return Package.objects.create(**data)

    @staticmethod
    def get_all_packages():
        return Package.objects.all().order_by('-created_at')

    @staticmethod
    def get_package_by_id(package_id):
        try:
            return Package.objects.get(id=package_id)
        except Package.DoesNotExist:
            return None

    @staticmethod
    def update_package(package, data):
        for key, value in data.items():
            setattr(package, key, value)
        package.save()
        return package