# -*- coding: utf-8 -*-
{
    'name': "duuge_birthday",

    'summary': """
        odoo10.0的员工出生日期，取值身份证号码中的出生日期值。
        """,

    'description': """
生日取身份证号码中的出生日期之模块
============================
本模块必须依赖hr模块。


本模块主要功能：
----------------------------
* 引入hr模块
* 实现员工生日自动从身份证号码中取值
* (功能不再增加了...)

    """,

    'author': "珠海-杜哥@duuge.com(QQ：281388879)",
    'website': "https://github.com/leangjia/duugebirthday",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'duuge_birthday',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['hr','view'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/duuge_birthday_data.xml',
        'views/duuge_birthday_view.xml',
    ],
}