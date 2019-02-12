# -*- coding: utf-8 -*-
{
    'name': "Academy",
    'sequence':2,

    'summary': """
        Pagina web responsive""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Alexander",
    'website': "http://www.overclocktech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'webpage',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','gancedo'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/contacto.xml',
        'views/acerca.xml',
        'views/horario.xml',
        'views/servicios.xml',
        'views/noticias.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'css':['static/src/css/estilos.css',
    'static/src/css/inicio/index.css',
    'static/src/css/inicio/acerca.css',
    'static/src/css/inicio/horario.css',
    'static/src/css/inicio/servicios.css',
    'static/src/css/inicio/noticias.css',
    'static/src/css/inicio/contacto.css',
    'static/src/js/jQuery-TE/jquery-te-1.4.0.css',
    ],
    'js':[
    'static/src/js/script.js',
    'static/src/js/jq.js',
    'static/src/js/inicio/index.js',
    'static/src/js/contacto/index.js',
    'static/src/js/servicios/index.js',
    'static/src/js/noticias/index.js',
    'static/src/js/horario/index.js',
    'static/src/js/acerca/index.js',   
    'static/src/js/jQuery-TE/jquery-te-1.4.0.min.js'
    ],
}
