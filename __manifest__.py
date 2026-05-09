{
    'name': "université",

    'summary': "Gestion d'une univesité",

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'application':True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
         'views/student_views.xml',
         'views/professor_views.xml',
         'views/subject_views.xml',
         'views/department_views.xml',
         'views/classroom_views.xml',
    ],
}

