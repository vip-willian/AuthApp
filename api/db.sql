-- auto-generated definition
create table sys_online
(
    id           bigint(20) auto_increment                                      not null comment '主键ID'
        primary key,
    login_name   varchar(100)                                                   not null comment '登录名称',
    login_ip     varchar(100)                                                   null comment '登录IP',
    type         varchar(1)                                                     null comment '类型',
    created_time datetime default current_timestamp                             not null comment '创建时间',
    updated_time datetime default current_timestamp on update current_timestamp not null comment '更新时间'
)
    collate = utf8mb4_bin comment '登录在线信息表';

-- auto-generated definition
create table sys_organization
(
    id              bigint(20) auto_increment                                      not null comment '主键ID'
        primary key,
    organization_id bigint(20)                                                     null comment '机构ID',
    code            varchar(200)                                                   null comment '机构编码',
    name            varchar(200)                                                   null comment '机构名称',
    address         varchar(200)                                                   null comment '机构地址',
    icon            varchar(100)                                                   null comment '图标',
    seq             int                                                            null comment '序号',
    created_time    datetime default current_timestamp                             not null comment '创建时间',
    updated_time    datetime default current_timestamp on update current_timestamp not null comment '更新时间'
)
    collate = utf8mb4_bin comment '机构信息表';

-- auto-generated definition
create table sys_organization_resource
(
    id              bigint(20) auto_increment                                      not null primary key comment '主键ID',
    organization_id bigint(20)                                                     not null comment '机构ID',
    resource_id     varchar(36)                                                    not null comment '资源ID',
    created_time    datetime default current_timestamp                             not null comment '创建时间',
    updated_time    datetime default current_timestamp on update current_timestamp not null comment '更新时间',
    unique key `uk_organization_resource_id` (organization_id, resource_id)
)
    collate = utf8mb4_bin comment ='机构资源信息表';

-- auto-generated definition
create table sys_resource
(
    id               varchar(36)                                                    not null comment '主键ID'
        primary key,
    resource_id      varchar(36)                                                    null comment '资源ID',
    resource_type_id bigint(20)                                                     null comment '资源类型ID',
    name             varchar(100)                                                   not null comment '资源名称',
    url              varchar(200)                                                   null comment '资源URL',
    description      varchar(200)                                                   null comment '描述',
    icon             varchar(100)                                                   null comment '图标',
    seq              int                                                            null comment '序号',
    target           varchar(100)                                                   null comment '资源目标',
    created_time     datetime default current_timestamp                             not null comment '创建时间',
    updated_time     datetime default current_timestamp on update current_timestamp not null comment '更新时间'
)
    collate = utf8mb4_bin comment ='资源信息表';

-- auto-generated definition
create table sys_resource_type
(
    id           bigint(20) auto_increment                                      not null comment '主键ID'
        primary key,
    name         varchar(100)                                                   not null comment '类型名称',
    description  varchar(200)                                                   null comment '类型描述',
    created_time datetime default current_timestamp                             not null comment '创建时间',
    updated_time datetime default current_timestamp on update current_timestamp not null comment '更新时间'
)
    collate = utf8mb4_bin comment ='资源类型表';

-- auto-generated definition
create table sys_role
(
    id           bigint(20)                                                     not null comment '主键ID'
        primary key,
    name         varchar(100)                                                   not null comment '角色名称',
    description  varchar(200)                                                   null comment '角色描述',
    icon         varchar(100)                                                   null comment '图标',
    seq          int                                                            null comment '序号',
    created_time datetime default current_timestamp                             not null comment '创建时间',
    updated_time datetime default current_timestamp on update current_timestamp not null comment '更新时间'
)
    collate = utf8mb4_bin comment ='角色信息表';

-- auto-generated definition
create table sys_role_resource
(
    id           bigint(20) auto_increment                                      not null primary key comment '主键ID',
    role_id      bigint(20)                                                     not null comment '角色ID',
    resource_id  varchar(36)                                                    not null comment '资源ID',
    created_time datetime default current_timestamp                             not null comment '创建时间',
    updated_time datetime default current_timestamp on update current_timestamp not null comment '更新时间',
    unique key `uk_role_resource_id` (resource_id, role_id)
)
    collate = utf8mb4_bin comment ='角色资源关联表';

-- auto-generated definition
create table sys_user
(
    id           bigint(20)                                                     not null comment '主键ID'
        primary key,
    login_name   varchar(100)                                                   not null comment '登录名',
    name         varchar(100)                                                   null comment '用户名',
    password     varchar(100)                                                   not null comment '密码',
    photo        varchar(200)                                                   null comment '照片',
    age          smallint(4)                                                    null comment '年龄',
    phone        varchar(11)                                                    not null comment '手机号',
    email        varchar(30)                                                    null comment '邮箱',
    sex          varchar(1)                                                     null comment '性别',
    employ_date  datetime                                                       null comment '工作日期',
    created_time datetime default current_timestamp                             not null comment '创建时间',
    updated_time datetime default current_timestamp on update current_timestamp not null comment '更新时间',
    unique key uk_phone (phone),
    unique key uk_login_name (login_name)
)
    collate = utf8mb4_bin comment '用户信息表';

-- auto-generated definition
create table sys_user_organization
(
    id              bigint(20) auto_increment                                      not null primary key comment '主键ID',
    organization_id bigint(20)                                                     not null comment '机构ID',
    user_id         bigint(20)                                                     not null comment '用户ID',
    created_time    datetime default current_timestamp                             not null comment '创建时间',
    updated_time    datetime default current_timestamp on update current_timestamp not null comment '更新时间',
    unique key `uk_organization_user_id` (organization_id, user_id)
)
    collate = utf8mb4_bin comment '用户机构管理表';

-- auto-generated definition
create table sys_user_role
(
    id           bigint(20) auto_increment                                      not null primary key comment '主键ID',
    user_id      bigint(20)                                                     not null comment '用户ID',
    role_id      bigint(20)                                                     not null comment '角色ID',
    created_time datetime default current_timestamp                             not null comment '创建时间',
    updated_time datetime default current_timestamp on update current_timestamp not null comment '更新时间',
    unique key `uk_user_role_id` (user_id, role_id)
)
    collate = utf8mb4_bin comment '用户角色关联表';

INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('jgbj', 'jggl', 1, '编辑机构', '/base/syorganization!update', '编辑机构', 'ext-icon-bullet_wrench', 2, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('jgck', 'jggl', 1, '查看机构', '/base/syorganization!getById', '查看机构', 'ext-icon-bullet_wrench', 4, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('jggl', 'xtgl', 0, '机构管理', '/securityJsp/base/Syorganization.jsp', '管理系统中用户的机构',
        'ext-icon-group_link', 3, '', '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('jglb', 'jggl', 1, '机构列表', '/base/syorganization!treeGrid', '查询机构列表', 'ext-icon-bullet_wrench', 0, '',
        '2015-08-25 10:34:53', '2016-11-28 14:09:52');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('jgsc', 'jggl', 1, '删除机构', '/base/syorganization!delete', '删除机构', 'ext-icon-bullet_wrench', 3, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('jgsq', 'jggl', 1, '机构授权', '/base/syorganization!grant', '机构授权', 'ext-icon-bullet_wrench', 5, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('jgtj', 'jggl', 1, '添加机构', '/base/syorganization!save', '添加机构', 'ext-icon-bullet_wrench', 1, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('jsbj', 'jsgl', 1, '编辑角色', '/base/syrole!update', '编辑角色', 'ext-icon-bullet_wrench', 2, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('jsck', 'jsgl', 1, '查看角色', '/base/syrole!getById', '查看角色', 'ext-icon-bullet_wrench', 4, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('jsgl', 'xtgl', 0, '角色管理', '/securityJsp/base/Syrole.jsp', '管理系统中用户的角色', 'ext-icon-tux', 2, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('jslb', 'jsgl', 1, '角色列表', '/base/syrole!grid', '查询角色列表', 'ext-icon-bullet_wrench', 0, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('jssc', 'jsgl', 1, '删除角色', '/base/syrole!delete', '删除角色', 'ext-icon-bullet_wrench', 3, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('jssq', 'jsgl', 1, '角色授权', '/base/syrole!grant', '角色授权', 'ext-icon-bullet_wrench', 5, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('jstj', 'jsgl', 1, '添加角色', '/base/syrole!save', '添加角色', 'ext-icon-bullet_wrench', 1, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('online', 'xtjk', 0, '用户登录历史监控', '/securityJsp/base/Syonline.jsp', '监控用户登录、注销',
        'ext-icon-chart_line', 4, '', '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('onlineGrid', 'online', 1, '用户登录历史列表', '/base/syonline!grid', '用户登录、注销历史记录列表',
        'ext-icon-bullet_wrench', 0, '', '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('xtgl', null, 0, '系统管理', '/welcome.jsp', '管理系统的资源、角色、机构、用户等信息',
        'ext-icon-application_view_tile', 5, '', '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('xtjk', null, 0, '系统监控', '/welcome.jsp', '监控系统运行情况等信息', 'ext-icon-monitor', 6, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('yhbj', 'yhgl', 1, '编辑用户', '/base/syuser!update', '编辑用户', 'ext-icon-bullet_wrench', 2, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('yhck', 'yhgl', 1, '查看用户', '/base/syuser!getById', '查看用户', 'ext-icon-bullet_wrench', 4, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('yhgl', 'xtgl', 0, '用户管理', '/securityJsp/base/Syuser.jsp', '管理系统中用户的用户', 'ext-icon-user_suit', 4,
        '', '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('yhjg', 'yhgl', 1, '用户机构', '/base/syuser!grantOrganization', '编辑用户机构', 'ext-icon-bullet_wrench', 6,
        '', '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('yhjs', 'yhgl', 1, '用户角色', '/base/syuser!grantRole', '编辑用户角色', 'ext-icon-bullet_wrench', 5, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('yhlb', 'yhgl', 1, '用户列表', '/base/syuser!grid', '查询用户列表', 'ext-icon-bullet_wrench', 0, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('yhsc', 'yhgl', 1, '删除用户', '/base/syuser!delete', '删除用户', 'ext-icon-bullet_wrench', 3, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('yhtj', 'yhgl', 1, '添加用户', '/base/syuser!save', '添加用户', 'ext-icon-bullet_wrench', 1, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('zybj', 'zygl', 1, '编辑资源', '/base/syresource!update', '编辑资源', 'ext-icon-bullet_wrench', 2, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('zyck', 'zygl', 1, '查看资源', '/base/syresource!getById', '查看资源', 'ext-icon-bullet_wrench', 4, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('zygl', 'xtgl', 0, '资源管理', '/securityJsp/base/Syresource.jsp', '管理系统的资源', 'ext-icon-newspaper_link',
        1, '', '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('zylb', 'zygl', 1, '资源列表', '/base/syresource!treeGrid', '查询资源', 'ext-icon-bullet_wrench', 0, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('zysc', 'zygl', 1, '删除资源', '/base/syresource!delete', '删除资源', 'ext-icon-bullet_wrench', 3, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource (id, resource_id, resource_type_id, name, url, description, icon, seq, target,
                          created_time, updated_time)
VALUES ('zytj', 'zygl', 1, '添加资源', '/base/syresource!save', '添加资源', 'ext-icon-bullet_wrench', 1, '',
        '2015-08-25 10:34:53', '2015-08-25 10:34:53');

INSERT INTO sys_resource_type (id, name, description, created_time, updated_time)
VALUES (0, '菜单', '菜单类型会显示在系统首页左侧菜单中', '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_resource_type (id, name, description, created_time, updated_time)
VALUES (1, '功能', '功能类型不会显示在系统首页左侧菜单中', '2015-08-25 10:34:53', '2015-08-25 10:34:53');

INSERT INTO sys_role (id, name, description, icon, seq, created_time, updated_time)
VALUES (0, '超管', '拥有系统所有权限', null, 0, '2015-08-25 10:34:53', '2015-08-25 10:34:53');
INSERT INTO sys_role (id, name, description, icon, seq, created_time, updated_time)
VALUES (1, '管理员', null, null, 100, '2016-11-28 14:24:00', '2016-11-28 14:24:00');

INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'jgbj');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'jgck');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'jggl');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'jglb');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'jgsc');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'jgsq');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'jgtj');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'jsbj');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'jsck');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'jsgl');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'jslb');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'jssc');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'jssq');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'jstj');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'online');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'onlineGrid');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'xtgl');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'xtjk');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'yhbj');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'yhck');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'yhgl');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'yhjg');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'yhjs');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'yhlb');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'yhsc');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'yhtj');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'zybj');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'zyck');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'zygl');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'zylb');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'zysc');
INSERT INTO sys_role_resource (role_id, resource_id)
VALUES ('0', 'zytj');

INSERT INTO sys_user (id, login_name, name, password, photo, age, phone, email, sex, employ_date, created_time,
                      updated_time)
VALUES (0, 'admin', '超级管理员', 'e10adc3949ba59abbe56e057f20f883e', '', 30, '15857108029', null, '1', null,
        '2015-08-25 10:34:54', '2016-09-27 15:41:11');

INSERT INTO sys_user_organization (user_id, organization_id)
VALUES (0, 0);
INSERT INTO sys_user_organization (user_id, organization_id)
VALUES (1, 0);

INSERT INTO sys_user_role (user_id, role_id)
VALUES (0, 0);
INSERT INTO sys_user_role (user_id, role_id)
VALUES (0, 1);
INSERT INTO sys_user_role (user_id, role_id)
VALUES (1, 1);