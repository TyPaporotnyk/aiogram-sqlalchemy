from src.bot.repositories.admin import AdminRepository
from src.bot.services.admin import AdminService


def get_admin_service():
    return AdminService(AdminRepository)
