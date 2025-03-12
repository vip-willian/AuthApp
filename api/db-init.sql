-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        8.0.29 - MySQL Community Server - GPL
-- 服务器操作系统:                      Linux
-- HeidiSQL 版本:                  12.0.0.6468
-- --------------------------------------------------------

-- 导出 db_auth 的数据库结构
CREATE DATABASE IF NOT EXISTS `db_auth`;
USE `db_auth`;


-- 初始化用户数据
INSERT INTO db_auth.sys_user (id, username, alias, password, password_salt, phone, email, avatar, sex, age, tenant_code,
                              org_id, dept_id, is_superuser, last_login_at, last_login_ip, last_active_at, user_status,
                              created_time, updated_time)
VALUES (1, 'admin', 'admin', 'ZjgwNmQ4ODkwYmVmYjAzZDUxZGNiOGIyZjRiNjA4YzUwZTlmN2NmNWMyZjI4MDc5MDdkMzBiYmI4MDg5OGNjNQ==',
        'keCASjk3uHkHnn2QIGHw1Q==', '15907924501', 'admin@gmail.com',
        'https://avatars.githubusercontent.com/u/54677442?v=4', 1, 10, '0', 0, 0, 1, null, null, '2025-03-12 15:30:58',
        'active', '2025-03-12 15:30:58', '2025-03-12 15:30:58');

-- 初始化角色数据
INSERT INTO db_auth.sys_role (id, name, `desc`, created_time, updated_time)
VALUES (1, '管理员', '管理员角色', '2025-03-12 15:48:22', '2025-03-12 15:48:22');
INSERT INTO db_auth.sys_role (id, name, `desc`, created_time, updated_time)
VALUES (2, '普通用户', '普通用户角色', '2025-03-12 15:48:22', '2025-03-12 15:48:22');

-- 初始化菜单数据
INSERT INTO db_auth.sys_menu (id, parent_id, name, menu_type, icon, path, `order`, remark, is_hidden, component,
                              keepalive, redirect, created_time, updated_time)
VALUES (1, 0, '系统管理', 'MENU', 'carbon:gui-management', '/system', 1, null, 0, 'Layout', 0, '/system/user',
        '2025-03-12 15:53:34', '2025-03-12 15:53:34');
INSERT INTO db_auth.sys_menu (id, parent_id, name, menu_type, icon, path, `order`, remark, is_hidden, component,
                              keepalive, redirect, created_time, updated_time)
VALUES (2, 0, '一级菜单', 'MENU', 'material-symbols:featured-play-list-outline', '/top-menu', 2, null, 0, '/top-menu',
        0, '', '2025-03-12 15:53:34', '2025-03-12 15:53:34');
INSERT INTO db_auth.sys_menu (id, parent_id, name, menu_type, icon, path, `order`, remark, is_hidden, component,
                              keepalive, redirect, created_time, updated_time)
VALUES (3, 1, '用户管理', 'MENU', 'material-symbols:person-outline-rounded', 'user', 1, null, 0, '/system/user', 0,
        null, '2025-03-12 15:53:34', '2025-03-12 15:53:34');
INSERT INTO db_auth.sys_menu (id, parent_id, name, menu_type, icon, path, `order`, remark, is_hidden, component,
                              keepalive, redirect, created_time, updated_time)
VALUES (4, 1, '角色管理', 'MENU', 'carbon:user-role', 'role', 2, null, 0, '/system/role', 0, null,
        '2025-03-12 15:53:34', '2025-03-12 15:53:34');
INSERT INTO db_auth.sys_menu (id, parent_id, name, menu_type, icon, path, `order`, remark, is_hidden, component,
                              keepalive, redirect, created_time, updated_time)
VALUES (5, 1, '菜单管理', 'MENU', 'material-symbols:list-alt-outline', 'menu', 3, null, 0, '/system/menu', 0, null,
        '2025-03-12 15:53:34', '2025-03-12 15:53:34');
INSERT INTO db_auth.sys_menu (id, parent_id, name, menu_type, icon, path, `order`, remark, is_hidden, component,
                              keepalive, redirect, created_time, updated_time)
VALUES (6, 1, '部门管理', 'MENU', 'mingcute:department-line', 'dept', 4, null, 0, '/system/dept', 0, null,
        '2025-03-12 15:53:34', '2025-03-12 15:53:34');

-- 初始化用户角色数据
INSERT INTO db_auth.sys_user_role (id, user_id, role_id, created_time, updated_time)
VALUES (1, 1, 1, '2025-03-12 15:57:13', '2025-03-12 15:57:13');

-- 初始化角色菜单数据
INSERT INTO db_auth.sys_role_menu (id, role_id, menu_id, created_time, updated_time)
VALUES (1, 1, 1, '2025-03-12 15:56:31', '2025-03-12 15:56:31');
INSERT INTO db_auth.sys_role_menu (id, role_id, menu_id, created_time, updated_time)
VALUES (2, 1, 2, '2025-03-12 15:56:31', '2025-03-12 15:56:31');
INSERT INTO db_auth.sys_role_menu (id, role_id, menu_id, created_time, updated_time)
VALUES (3, 1, 3, '2025-03-12 15:56:31', '2025-03-12 15:56:31');
INSERT INTO db_auth.sys_role_menu (id, role_id, menu_id, created_time, updated_time)
VALUES (4, 1, 4, '2025-03-12 15:56:31', '2025-03-12 15:56:31');
INSERT INTO db_auth.sys_role_menu (id, role_id, menu_id, created_time, updated_time)
VALUES (5, 1, 5, '2025-03-12 15:56:31', '2025-03-12 15:56:31');
INSERT INTO db_auth.sys_role_menu (id, role_id, menu_id, created_time, updated_time)
VALUES (6, 1, 6, '2025-03-12 15:56:31', '2025-03-12 15:56:31');
INSERT INTO db_auth.sys_role_menu (id, role_id, menu_id, created_time, updated_time)
VALUES (7, 2, 1, '2025-03-12 15:56:31', '2025-03-12 15:56:31');
INSERT INTO db_auth.sys_role_menu (id, role_id, menu_id, created_time, updated_time)
VALUES (8, 2, 2, '2025-03-12 15:56:31', '2025-03-12 15:56:31');
INSERT INTO db_auth.sys_role_menu (id, role_id, menu_id, created_time, updated_time)
VALUES (9, 2, 3, '2025-03-12 15:56:31', '2025-03-12 15:56:31');
