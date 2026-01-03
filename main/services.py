from .repositories import PackageRepository

class WarehouseService:
    def __init__(self):
        self.repo = PackageRepository()

    def register_new_package(self, data):
        weight = float(data.get('weight', 0))
        data['shipping_cost'] = weight * 10000
        return self.repo.create_package(data)

    def mark_as_ready(self, package_id):
        package = self.repo.get_package_by_id(package_id)
        if package and package.status == 'PENDING':
            return self.repo.update_package(package, {'status': 'READY'})
        return None