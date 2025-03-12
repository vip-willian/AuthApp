from models.user import User, Menu, RoleMenu
from models import db


class UserService:

    @staticmethod
    def get_user_menus(*, user: User):
        menus: list[Menu] = []
        if user.is_superuser:
            menus = db.session.query(Menu).all()
        else:
            # 查询用户关联的角色
            role_ids = user.get_role_ids
            menu_ids = RoleMenu.get_menus_ids(role_ids)
            # 查询角色关联的菜单
            menus = Menu.get_menus(menu_ids)

        parent_menus: list[Menu] = []
        for menu in menus:
            if menu.parent_id == 0:
                parent_menus.append(menu)
        res = []
        for parent_menu in parent_menus:
            parent_menu_dict = dict(parent_menu)
            parent_menu_dict["children"] = []
            for menu in menus:
                if menu.parent_id == parent_menu.id:
                    parent_menu_dict["children"].append(dict(menu))
            res.append(parent_menu_dict)
        return res
