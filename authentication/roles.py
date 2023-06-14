from rolepermissions.roles import AbstractUserRole


class User(AbstractUserRole):
    available_permissions = {
        "view_profile": True,
    }


class Admin(AbstractUserRole):
    available_permissions = {
        "view_profile": True,
    }
