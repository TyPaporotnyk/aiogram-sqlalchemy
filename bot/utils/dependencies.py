from bot.repositories.admin import AdminRepository
from bot.services.admin import AdminService


def get_admin_service():
    return AdminService(AdminRepository)
