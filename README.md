进入到api目录下，添加如下内容：

from models.user import SysUser, SysUserRole, SysUserOrganization

from models.organization import SysOrganization, SysOrganizationResource

from models.role import SysRole, SysRoleResource, SysRoleOrganization

from models.resource import SysResource, SysResourceType

from models.sys_dict import SysDictType, SysDictData, SysOnline, SysConfig

from models.account import Account

执行poetry install命令安装以来

进入poetry环境 poetry env activate

设置FLASK_APP

set/export FLASK_APP=app.py

执行初始化

flask db init

flask db migrate -m 'init-table'

flask db upgrade

最后执行db-init.sql

awk -v key="$(openssl rand -base64 42)" '/^SECRET_KEY=/ {sub(/=.*/, "=" key)} 1' .env > temp_env && mv temp_env .env

