from src.db.repositories.admin import AdminRepository
from src.db.services.admin import AdminService


def get_admin_service():
    return AdminService(AdminRepository)
