from .repositories import PackageRepository

class PackageService:
    def __init__(self):
        self.repo = PackageRepository()

    def register_new_package(self, data):
        weight = float(data.get('weight', 0))
        data['shipping_cost'] = weight * 10000
        return self.repo.create_package(data)