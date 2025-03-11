-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        8.0.29 - MySQL Community Server - GPL
-- 服务器操作系统:                      Linux
-- HeidiSQL 版本:                  12.0.0.6468
-- --------------------------------------------------------

-- 导出 db_auth 的数据库结构
CREATE DATABASE IF NOT EXISTS `db_auth`;
USE `db_auth`;


-- 正在导出表  db_auth.sys_online 的数据：~2 rows (大约)
INSERT INTO `sys_online` (`ID`, `created_time`, `IP`, `login_name`, `TYPE`)
VALUES (1, '2022-05-22 12:00:43', '127.0.0.1', 'admin', '1'),
       (2, '2023-05-16 19:49:12', '127.0.0.1', 'admin', '1');

-- 正在导出表  db_auth.sys_organization 的数据：~3 rows (大约)
INSERT INTO `sys_organization` (`ID`, `ADDRESS`, `CODE`, `created_time`, `icon`, `NAME`, `SEQ`, `updated_time`,
                                `organization_id`, `LEADER`, `PHONE`, `EMAIL`, `STATUS`)
VALUES (1899325318242635776, NULL, NULL, '2016-11-28 10:34:54', 'ext-icon-bricks', '总部', 100, '2016-11-28 10:35:12', NULL, NULL, NULL,
        NULL, '0'),
       (1899325440150081536, NULL, NULL, '2022-05-22 09:59:33', NULL, '南京分公司', 1,
        '2023-05-16 19:52:10', '0', 'dd', '18905189016', 'ss@ada.com', '0'),
       (1899325489336684544, NULL, NULL, '2022-05-24 23:54:10', NULL, '上海分公司', 2,
        '2022-05-24 23:56:21', '0', 'jack', NULL, NULL, '0');


-- 正在导出表  db_auth.sys_resource_type 的数据：~3 rows (大约)
INSERT INTO `sys_resource_type` (`id`, `created_time`, `DESCRIPTION`, `NAME`, `updated_time`)
VALUES (1, '2015-08-25 10:34:53', '菜单类型会显示在系统首页左侧菜单中', '菜单', '2015-08-25 10:34:53'),
       (2, '2015-08-25 10:34:53', '功能类型不会显示在系统首页左侧菜单中', '功能', '2015-08-25 10:34:53'),
       (3, '2022-05-15 10:27:08', NULL, '目录', '2022-05-15 10:27:18');

-- 正在导出表  db_auth.sys_resource 的数据：~44 rows (大约)
INSERT INTO `sys_resource` (`id`, `created_time`, `DESCRIPTION`, `icon`, `NAME`, `SEQ`, `TARGET`, `updated_time`,
                            `PATH`, `URL`, `PERMS`, `resource_id`, `resource_type_id`, `STATUS`)
VALUES ('xtgl', '2015-08-25 10:34:53', '管理系统的资源、角色、机构、用户等信息', 'system', '系统管理', 1, '',
        '2023-05-16 20:03:02', '/system', NULL, NULL, NULL, 3, 0),
       ('jggl', '2015-08-25 10:34:53', '管理系统中用户的机构', 'tree', '机构管理', 4, '', '2022-05-25 00:40:04', 'dept',
        'system/dept/index', 'system:dept:list', 'xtgl', 1, 0),
       ('jgbj', '2015-08-25 10:34:53', '编辑机构', 'ext-icon-bullet_wrench', '编辑机构', 2, '', '2022-05-25 00:39:56',
        NULL, '/base/syorganization!update', 'system:dept:edit', 'jggl', 2, 0),
       ('jgck', '2015-08-25 10:34:53', '查看机构', 'ext-icon-bullet_wrench', '查看机构', 4, '', '2015-08-25 10:34:53',
        NULL, '/base/syorganization!getById', 'system:dept:query', 'jggl', 2, 0),
       ('jglb', '2015-08-25 10:34:53', '查询机构列表', 'ext-icon-bullet_wrench', '机构列表', 0, '',
        '2016-11-28 14:09:52', NULL, '/base/syorganization!treeGrid', 'system:dept:list', 'jggl', 2, 0),
       ('jgsc', '2015-08-25 10:34:53', '删除机构', 'ext-icon-bullet_wrench', '删除机构', 3, '', '2015-08-25 10:34:53',
        NULL, '/base/syorganization!delete', 'system:dept:remove', 'jggl', 2, 0),
       ('jgsq', '2015-08-25 10:34:53', '机构授权', 'ext-icon-bullet_wrench', '机构授权', 5, '', '2015-08-25 10:34:53',
        NULL, '/base/syorganization!grant', NULL, 'jggl', 2, 0),
       ('jgtj', '2015-08-25 10:34:53', '添加机构', 'ext-icon-bullet_wrench', '添加机构', 1, '', '2015-08-25 10:34:53',
        NULL, '/base/syorganization!save', 'system:dept:add', 'jggl', 2, 0),
       ('jsgl', '2015-08-25 10:34:53', '管理系统中用户的角色', 'peoples', '角色管理', 2, '', '2015-08-25 10:34:53',
        'role', 'system/role/index', 'system:role:list', 'xtgl', 1, 0),
       ('jsbj', '2015-08-25 10:34:53', '编辑角色', 'ext-icon-bullet_wrench', '编辑角色', 2, '', '2015-08-25 10:34:53',
        NULL, '/base/syrole!update', 'system:role:edit', 'jsgl', 2, 0),
       ('jsck', '2015-08-25 10:34:53', '查看角色', 'ext-icon-bullet_wrench', '查看角色', 4, '', '2015-08-25 10:34:53',
        NULL, '/base/syrole!getById', 'system:role:query', 'jsgl', 2, 0),
       ('jslb', '2015-08-25 10:34:53', '查询角色列表', 'ext-icon-bullet_wrench', '角色列表', 0, '',
        '2015-08-25 10:34:53', NULL, '/base/syrole!grid', 'system:role:list', 'jsgl', 2, 0),
       ('jssc', '2015-08-25 10:34:53', '删除角色', 'ext-icon-bullet_wrench', '删除角色', 3, '', '2015-08-25 10:34:53',
        NULL, '/base/syrole!delete', 'system:role:remove', 'jsgl', 2, 0),
       ('jssq', '2015-08-25 10:34:53', '角色授权', 'ext-icon-bullet_wrench', '角色授权', 5, '', '2015-08-25 10:34:53',
        NULL, '/base/syrole!grant', NULL, 'jsgl', 2, 0),
       ('jstj', '2015-08-25 10:34:53', '添加角色', 'ext-icon-bullet_wrench', '添加角色', 1, '', '2015-08-25 10:34:53',
        NULL, '/base/syrole!save', 'system:role:add', 'jsgl', 2, 0),
       ('xtjk', '2015-08-25 10:34:53', '监控系统运行情况等信息', 'monitor', '系统监控', 2, '', '2022-06-10 00:48:47',
        '/system/log', '', '', NULL, 1, 0),
       ('online', '2015-08-25 10:34:53', '监控用户登录、注销', 'ext-icon-chart_line', '登录历史', 1, '',
        '2022-06-10 00:53:22', 'logininfor', 'monitor/logininfor/index', 'monitor:logininfor:list', 'xtjk', 1, 0),
       ('onlineGrid', '2015-08-25 10:34:53', '用户登录、注销历史记录列表', 'ext-icon-bullet_wrench', '用户登录历史列表',
        1, '', '2022-05-28 13:16:37', NULL, '/base/syonline!grid', 'monitor:logininfor:list', 'online', 2, 0),
       ('yhgl', '2015-08-25 10:34:53', '管理系统中用户的用户', 'user', '用户管理', 1, '', '2023-05-16 20:08:40', 'user',
        'system/user/index', 'system:user:list', 'xtgl', 1, 0),
       ('yhbj', '2015-08-25 10:34:53', '编辑用户', 'ext-icon-bullet_wrench', '编辑用户', 2, '', '2015-08-25 10:34:53',
        NULL, '/base/syuser!update', 'system:user:edit', 'yhgl', 2, 0),
       ('yhck', '2015-08-25 10:34:53', '查看用户', 'ext-icon-bullet_wrench', '查看用户', 4, '', '2015-08-25 10:34:53',
        NULL, '/base/syuser!getById', 'system:user:query', 'yhgl', 2, 0),
       ('yhjg', '2015-08-25 10:34:53', '编辑用户机构', 'ext-icon-bullet_wrench', '用户机构', 6, '',
        '2015-08-25 10:34:53', NULL, '/base/syuser!grantOrganization', 'system:dept:edit', 'yhgl', 2, 0),
       ('yhjs', '2015-08-25 10:34:53', '编辑用户角色', 'ext-icon-bullet_wrench', '用户角色', 5, '',
        '2015-08-25 10:34:53', NULL, '/base/syuser!grantRole', 'system:role:edit', 'yhgl', 2, 0),
       ('yhlb', '2015-08-25 10:34:53', '查询用户列表', 'ext-icon-bullet_wrench', '用户列表', 0, '',
        '2015-08-25 10:34:53', NULL, '/base/syuser!grid', 'system:user:list', 'yhgl', 2, 0),
       ('yhsc', '2015-08-25 10:34:53', '删除用户', 'ext-icon-bullet_wrench', '删除用户', 3, '', '2015-08-25 10:34:53',
        NULL, '/base/syuser!delete', 'system:user:remove', 'yhgl', 2, 0),
       ('yhtj', '2015-08-25 10:34:53', '添加用户', 'ext-icon-bullet_wrench', '添加用户', 1, '', '2015-08-25 10:34:53',
        NULL, '/base/syuser!save', 'system:user:add', 'yhgl', 2, 0),
       ('zygl', '2015-08-25 10:34:53', '管理系统的资源', 'tree-table', '资源管理', 3, '', '2022-05-25 00:48:32', 'menu',
        'system/menu/index', 'system:menu:list', 'xtgl', 1, 0),
       ('zybj', '2015-08-25 10:34:53', '编辑资源', 'ext-icon-bullet_wrench', '编辑资源', 2, '', '2015-08-25 10:34:53',
        NULL, '/base/syresource!update', 'system:menu:edit', 'zygl', 2, 0),
       ('zyck', '2015-08-25 10:34:53', '查看资源', 'ext-icon-bullet_wrench', '查看资源', 4, '', '2015-08-25 10:34:53',
        NULL, '/base/syresource!getById', 'system:menu:query', 'zygl', 2, 0),
       ('zylb', '2015-08-25 10:34:53', '查询资源', 'ext-icon-bullet_wrench', '资源列表', 0, '', '2015-08-25 10:34:53',
        NULL, '/base/syresource!treeGrid', 'system:menu:query', 'zygl', 2, 0),
       ('zysc', '2015-08-25 10:34:53', '删除资源', 'ext-icon-bullet_wrench', '删除资源', 3, '', '2015-08-25 10:34:53',
        NULL, '/base/syresource!delete', 'system:menu:remove', 'zygl', 2, 0),
       ('zytj', '2015-08-25 10:34:53', '添加资源', 'ext-icon-bullet_wrench', '添加资源', 1, '', '2015-08-25 10:34:53',
        NULL, '/base/syresource!save', 'system:menu:add', 'zygl', 2, 0),
       ('27fda67f-61d1-4fe6-8eea-d796a848ab67', '2022-05-28 12:54:39', NULL, 'edit', '参数设置', 6, '',
        '2022-05-28 12:54:39', 'config', 'system/config/index', 'system:config:list', 'xtgl', 3, 0),
       ('37ac3cd3-560b-49b3-ae86-96d1963e9db6', '2022-05-28 12:55:59', NULL, NULL, '参数修改', 3, NULL,
        '2022-05-28 12:55:59', NULL, NULL, 'system:config:edit', '27fda67f-61d1-4fe6-8eea-d796a848ab67', 2, 0),
       ('4621e9f8-e7c6-4c2b-8172-3d8c8ea75371', '2022-05-28 12:55:24', NULL, NULL, '参数新增', 2, NULL,
        '2022-05-28 12:55:24', NULL, NULL, 'system:config:add', '27fda67f-61d1-4fe6-8eea-d796a848ab67', 2, 0),
       ('cssc', '2022-05-28 12:56:23', NULL, NULL, '参数删除', 4, NULL, '2022-05-28 12:56:23', NULL, NULL,
        'system:config:remove', '27fda67f-61d1-4fe6-8eea-d796a848ab67', 2, 0),
       ('d60df8ae-86ee-4879-b9b9-2fe79f146d31', '2022-05-28 12:55:02', NULL, NULL, '参数查询', 1, NULL,
        '2022-05-28 12:55:02', NULL, NULL, 'system:config:query', '27fda67f-61d1-4fe6-8eea-d796a848ab67', 2, 0),
       ('dd41b52b-272c-49ac-b045-b05392890a8d', '2022-05-28 12:56:49', NULL, NULL, '参数导出', 5, NULL,
        '2022-05-28 12:56:49', NULL, NULL, 'system:config:export', '27fda67f-61d1-4fe6-8eea-d796a848ab67', 2, 0),
       ('ffb8cf26-1049-43ee-9dd5-16e5742ce9d5', '2022-05-28 12:50:37', NULL, 'dict', '字典管理', 5, '',
        '2022-05-28 12:50:37', 'dict', 'system/dict/index', 'system:dict:list', 'xtgl', 3, 0),
       ('726c7c1e-06f8-4c3e-b9e1-95778a430c07', '2022-05-28 12:51:16', NULL, NULL, '字典查询', 1, NULL,
        '2022-05-28 12:51:16', NULL, NULL, 'system:dict:query', 'ffb8cf26-1049-43ee-9dd5-16e5742ce9d5', 2, 0),
       ('b95cae69-6389-4ebc-b613-bee7aac5f730', '2022-05-28 12:52:26', NULL, NULL, '字典修改', 3, NULL,
        '2022-05-28 12:52:26', NULL, NULL, 'system:dict:edit', 'ffb8cf26-1049-43ee-9dd5-16e5742ce9d5', 2, 0),
       ('cc7ff599-a588-40b3-951d-ce9dd2490482', '2022-05-28 12:53:26', NULL, NULL, '字典导出', 5, NULL,
        '2022-05-28 12:53:26', NULL, NULL, 'system:dict:export', 'ffb8cf26-1049-43ee-9dd5-16e5742ce9d5', 2, 0),
       ('zdsc', '2022-05-28 12:52:58', NULL, NULL, '字典删除', 4, NULL, '2022-05-28 12:52:58', NULL, NULL,
        'system:dict:remove', 'ffb8cf26-1049-43ee-9dd5-16e5742ce9d5', 2, 0),
       ('edc3358e-b9c5-462f-8a70-7b1c7d7f2c26', '2022-05-28 12:51:53', NULL, NULL, '字典新增', 2, NULL,
        '2022-05-28 12:51:53', NULL, NULL, 'system:dict:add', 'ffb8cf26-1049-43ee-9dd5-16e5742ce9d5', 2, 1);

-- 正在导出表  db_auth.sys_role 的数据：~3 rows (大约)
INSERT INTO `sys_role` (`ID`, `created_time`, `DESCRIPTION`, `icon`, `NAME`, `SEQ`, `updated_time`, `role_key`,
                        `data_scope`, `STATUS`)
VALUES (1899326131962777600, '2015-08-25 10:34:53', '拥有系统所有权限', NULL, '超管', 0, '2022-06-10 00:27:23', 'superadmin', '1', '0'),
       (1899326872110632960, '2016-11-28 14:24:00', NULL, NULL, '管理员', 100, '2022-06-10 00:27:41',
        'admin', '1', '0'),
       (1899327065082171392, '2022-05-29 13:29:38', NULL, NULL, '只读用户', 1, '2022-06-10 00:13:55',
        'readonly', '2', '0');

-- 正在导出表  db_auth.sys_role_organization 的数据：~1 rows (大约)
INSERT INTO `sys_role_organization` (`role_id`, `organization_id`)
VALUES (1899327065082171392, 1899325440150081536);

-- 正在导出表  db_auth.sys_role_resource 的数据：~57 rows (大约)
INSERT INTO `sys_role_resource` (`role_id`, `resource_id`)
VALUES (1899326131962777600, '27fda67f-61d1-4fe6-8eea-d796a848ab67'),
       (1899327065082171392, '27fda67f-61d1-4fe6-8eea-d796a848ab67'),
       (1899326131962777600, '37ac3cd3-560b-49b3-ae86-96d1963e9db6'),
       (1899326131962777600, '4621e9f8-e7c6-4c2b-8172-3d8c8ea75371'),
       (1899326131962777600, '726c7c1e-06f8-4c3e-b9e1-95778a430c07'),
       (1899327065082171392, '726c7c1e-06f8-4c3e-b9e1-95778a430c07'),
       (1899326131962777600, 'b95cae69-6389-4ebc-b613-bee7aac5f730'),
       (1899326131962777600, 'cc7ff599-a588-40b3-951d-ce9dd2490482'),
       (1899326131962777600, 'cssc'),
       (1899326131962777600, 'd60df8ae-86ee-4879-b9b9-2fe79f146d31'),
       (1899327065082171392, 'd60df8ae-86ee-4879-b9b9-2fe79f146d31'),
       (1899326131962777600, 'dd41b52b-272c-49ac-b045-b05392890a8d'),
       (1899326131962777600, 'edc3358e-b9c5-462f-8a70-7b1c7d7f2c26'),
       (1899326131962777600, 'ffb8cf26-1049-43ee-9dd5-16e5742ce9d5'),
       (1899327065082171392, 'ffb8cf26-1049-43ee-9dd5-16e5742ce9d5'),
       (1899326131962777600, 'jgbj'),
       (1899326131962777600, 'jgck'),
       (1899326131962777600, 'jggl'),
       (1899327065082171392, 'jggl'),
       (1899326131962777600, 'jglb'),
       (1899327065082171392, 'jglb'),
       (1899326131962777600, 'jgsc'),
       (1899326131962777600, 'jgsq'),
       (1899326131962777600, 'jgtj'),
       (1899326131962777600, 'jsbj'),
       (1899326131962777600, 'jsck'),
       (1899326131962777600, 'jsgl'),
       (1899327065082171392, 'jsgl'),
       (1899326131962777600, 'jslb'),
       (1899327065082171392, 'jslb'),
       (1899326131962777600, 'jssc'),
       (1899326131962777600, 'jssq'),
       (1899326131962777600, 'jstj'),
       (1899326131962777600, 'online'),
       (1899326131962777600, 'onlineGrid'),
       (1899326131962777600, 'xtgl'),
       (1899327065082171392, 'xtgl'),
       (1899326131962777600, 'xtjk'),
       (1899326131962777600, 'yhbj'),
       (1899326131962777600, 'yhck'),
       (1899326131962777600, 'yhgl'),
       (1899327065082171392, 'yhgl'),
       (1899326131962777600, 'yhjg'),
       (1899326131962777600, 'yhjs'),
       (1899326131962777600, 'yhlb'),
       (1899327065082171392, 'yhlb'),
       (1899326131962777600, 'yhsc'),
       (1899326131962777600, 'yhtj'),
       (1899326131962777600, 'zdsc'),
       (1899326131962777600, 'zybj'),
       (1899326131962777600, 'zyck'),
       (1899326131962777600, 'zygl'),
       (1899327065082171392, 'zygl'),
       (1899326131962777600, 'zylb'),
       (1899327065082171392, 'zylb'),
       (1899326131962777600, 'zysc'),
       (1899326131962777600, 'zytj');

-- 正在导出表  db_auth.SYS_CONFIG 的数据：~5 rows (大约)
INSERT INTO `sys_config` (`config_id`, `config_name`, `config_key`, `config_value`, `config_type`, `create_by`,
                          `created_time`, `update_by`, `updated_time`, `remark`)
VALUES (1, '主框架页-默认皮肤样式名称', 'sys.index.skinName', 'skin-blue', 'Y', 'admin', '2022-05-14 14:04:21', '',
        '2022-05-14 14:04:21', '蓝色 skin-blue、绿色 skin-green、紫色 skin-purple、红色 skin-red、黄色 skin-yellow'),
       (2, '用户管理-账号初始密码', 'sys.user.initPassword', '123456', 'Y', 'admin', '2022-05-14 14:04:21', '', '2022-05-14 14:04:21',
        '初始化密码 123456'),
       (3, '主框架页-侧边栏主题', 'sys.index.sideTheme', 'theme-dark', 'Y', 'admin', '2022-05-14 14:04:21', '', '2022-05-14 14:04:21',
        '深色主题theme-dark，浅色主题theme-light'),
       (4, '账号自助-验证码开关', 'sys.account.captchaOnOff', 'true', 'Y', 'admin', '2022-05-14 14:04:21', '', '2022-05-14 14:04:21',
        '是否开启验证码功能（true开启，false关闭）'),
       (5, '账号自助-是否开启用户注册功能', 'sys.account.registerUser', 'false', 'Y', 'admin', '2022-05-14 14:04:21',
        '', '2022-05-14 14:04:21', '是否开启注册用户功能（true开启，false关闭）');


-- 正在导出表  db_auth.sys_dict_type 的数据：~11 rows (大约)
INSERT INTO `sys_dict_type` (`dict_id`, `dict_name`, `dict_type`, `status`, `create_by`, `created_time`, `update_by`,
                             `updated_time`, `remark`)
VALUES (1, '用户性别', 'sys_user_sex', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20', '用户性别列表'),
       (2, '菜单状态', 'sys_show_hide', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20', '菜单状态列表'),
       (3, '系统开关', 'sys_normal_disable', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20', '系统开关列表'),
       (4, '任务状态', 'sys_job_status', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20', '任务状态列表'),
       (5, '任务分组', 'sys_job_group', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20', '任务分组列表'),
       (6, '系统是否', 'sys_yes_no', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20', '系统是否列表'),
       (7, '通知类型', 'sys_notice_type', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20', '通知类型列表'),
       (8, '通知状态', 'sys_notice_status', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20', '通知状态列表'),
       (9, '操作类型', 'sys_oper_type', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20', '操作类型列表'),
       (10, '系统状态', 'sys_common_status', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20', '登录状态列表'),
       (11, '登录日志类型', 'sys_login_type', '0', 'admin', '2022-06-10 00:28:26', 'admin', '2022-06-10 00:28:26',
        NULL);

-- 正在导出表  db_auth.sys_dict_data 的数据：~30 rows (大约)
INSERT INTO `sys_dict_data` (`dict_code`, `dict_sort`, `dict_label`, `dict_value`, `dict_type`, `css_class`,
                             `list_class`, `is_default`, `status`, `create_by`, `created_time`, `update_by`,
                             `updated_time`, `remark`)
VALUES (1, 1, '男', '0', 'sys_user_sex', '', '', 'Y', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20', '性别男'),
       (2, 2, '女', '1', 'sys_user_sex', '', '', 'N', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20', '性别女'),
       (3, 3, '未知', '2', 'sys_user_sex', '', '', 'N', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20', '性别未知'),
       (4, 1, '显示', '0', 'sys_show_hide', '', 'primary', 'Y', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20',
        '显示菜单'),
       (5, 2, '隐藏', '1', 'sys_show_hide', '', 'danger', 'N', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20',
        '隐藏菜单'),
       (6, 1, '正常', '0', 'sys_normal_disable', '', 'primary', 'Y', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20',
        '正常状态'),
       (7, 2, '停用', '1', 'sys_normal_disable', '', 'danger', 'N', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20',
        '停用状态'),
       (8, 1, '正常', '0', 'sys_job_status', '', 'primary', 'Y', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20',
        '正常状态'),
       (9, 2, '暂停', '1', 'sys_job_status', '', 'danger', 'N', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20',
        '停用状态'),
       (10, 1, '默认', 'DEFAULT', 'sys_job_group', '', '', 'Y', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20',
        '默认分组'),
       (11, 2, '系统', 'SYSTEM', 'sys_job_group', '', '', 'N', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20',
        '系统分组'),
       (12, 1, '是', 'Y', 'sys_yes_no', '', 'primary', 'Y', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20',
        '系统默认是'),
       (13, 2, '否', 'N', 'sys_yes_no', '', 'danger', 'N', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20', '系统默认否'),
       (14, 1, '通知', '1', 'sys_notice_type', '', 'warning', 'Y', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20',
        '通知'),
       (15, 2, '公告', '2', 'sys_notice_type', '', 'success', 'N', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20',
        '公告'),
       (16, 1, '正常', '0', 'sys_notice_status', '', 'primary', 'Y', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20',
        '正常状态'),
       (17, 2, '关闭', '1', 'sys_notice_status', '', 'danger', 'N', '0', 'admin', '2022-05-14 14:04:20', '', '2022-05-14 14:04:20',
        '关闭状态'),
       (18, 1, '新增', '1', 'sys_oper_type', '', 'info', 'N', '0', 'admin', '2022-05-14 14:04:21', '', '2022-05-14 14:04:20',
        '新增操作'),
       (19, 2, '修改', '2', 'sys_oper_type', '', 'info', 'N', '0', 'admin', '2022-05-14 14:04:21', '', '2022-05-14 14:04:20',
        '修改操作'),
       (20, 3, '删除', '3', 'sys_oper_type', '', 'danger', 'N', '0', 'admin', '2022-05-14 14:04:21', '', '2022-05-14 14:04:20',
        '删除操作'),
       (21, 4, '授权', '4', 'sys_oper_type', '', 'primary', 'N', '0', 'admin', '2022-05-14 14:04:21', '', '2022-05-14 14:04:20',
        '授权操作'),
       (22, 5, '导出', '5', 'sys_oper_type', '', 'warning', 'N', '0', 'admin', '2022-05-14 14:04:21', '', '2022-05-14 14:04:20',
        '导出操作'),
       (23, 6, '导入', '6', 'sys_oper_type', '', 'warning', 'N', '0', 'admin', '2022-05-14 14:04:21', '', '2022-05-14 14:04:20',
        '导入操作'),
       (24, 7, '强退', '7', 'sys_oper_type', '', 'danger', 'N', '0', 'admin', '2022-05-14 14:04:21', '', '2022-05-14 14:04:20',
        '强退操作'),
       (25, 8, '生成代码', '8', 'sys_oper_type', '', 'warning', 'N', '0', 'admin', '2022-05-14 14:04:21', '', '2022-05-14 14:04:20',
        '生成操作'),
       (26, 9, '清空数据', '9', 'sys_oper_type', '', 'danger', 'N', '0', 'admin', '2022-05-14 14:04:21', '', '2022-05-14 14:04:20',
        '清空操作'),
       (27, 1, '成功', '0', 'sys_common_status', '', 'primary', 'N', '0', 'admin', '2022-05-14 14:04:21', '', '2022-05-14 14:04:20',
        '正常状态'),
       (28, 2, '失败', '1', 'sys_common_status', '', 'danger', 'N', '0', 'admin', '2022-05-14 14:04:21', '', '2022-05-14 14:04:20',
        '停用状态'),
       (100, 0, '登录', '1', 'sys_login_type', NULL, 'default', NULL, '0', 'admin', '2022-06-10 00:29:31', 'admin',
        '2022-06-10 00:29:58', NULL),
       (101, 1, '注销', '0', 'sys_login_type', NULL, 'default', NULL, '0', 'admin', '2022-06-10 00:29:48', NULL,
        '2022-06-10 00:29:48', NULL);

-- 正在导出表  db_auth.sys_user 的数据：~2 rows (大约)
INSERT INTO `sys_user` (`ID`, `AGE`, `created_time`, `login_name`, `NAME`, `PHOTO`, `password`, `SEX`, `updated_time`,
                        `employ_date`, `EMAIL`, `phone`, `STATUS`)
VALUES (1899323663447101440, 30, '2015-08-25 10:34:54', 'admin', 'admin', '', 'e10adc3949ba59abbe56e057f20f883e', '1',
        '2022-06-08 11:04:52', NULL, 'test@test.com', '18988888888', '0'),
       (1899323663447101441, NULL, '2022-05-29 09:28:57', 'test', 'test', NULL,
        'e10adc3949ba59abbe56e057f20f883e', '0', '2022-06-10 09:19:56', '2022-05-29 09:28:57', 'test@test.com',
        '18988888888', '0');

-- 正在导出表  db_auth.sys_user_organization 的数据：~3 rows (大约)
INSERT INTO `sys_user_organization` (`user_id`, `organization_id`)
VALUES (1899323663447101440, 1899325318242635776),
       (1899323663447101441, 1899325440150081536);

-- 正在导出表  db_auth.sys_user_role 的数据：~4 rows (大约)
INSERT INTO `sys_user_role` (`user_id`, `role_id`)
VALUES (1899323663447101440, 1899326131962777600),
       (1899323663447101440, 1899326872110632960),
       (1899323663447101440, 1899327065082171392);

insert into account(id, name, email, phone, password, password_salt, avatar, interface_language, interface_theme,
                    timezone, last_login_at, last_login_ip, last_active_at, status, initialized_at, created_time,
                    updated_time)
values (1899323663447101440, 'admin', 'admin@gmail.com', '15907554567', 'ZjI3MWIyYjNhZmY0ZTBmOGI1MTc2OGU1NzcwZmQ2Mzk2OTMyZDA3ZjhiZDczYTNjODJlMGI4ZDQyN2UxMmNhMw==', 'w4ONnSZiD0E+KaHJuP9xYw==', '', '', '', null, null, null, now(), 'active', now(), now(),
        now());