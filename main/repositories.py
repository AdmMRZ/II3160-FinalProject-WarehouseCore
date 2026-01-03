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
        return Package.objects.filter(id=package_id).first()

    @staticmethod
    def update_package(package_id, data):
        package = Package.objects.filter(id=package_id).first()
        if package:
            for key, value in data.items():
                setattr(package, key, value)
            package.save()
        return package