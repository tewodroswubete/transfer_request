{
    'name': 'Transfer Request',
    'version': '1.1',
     'author': 'teddy',
    'summary': 'Request Creator for Transfers',
    'description': """ 
            """,
    'depends': ["product", "stock", "mail", "project"], 
    'category': 'Extra',
    'sequence': 1,
    'data': [
        'views/menus.xml',
        'views/project_project_views.xml',
        'security/ir.model.access.csv',
        'sequences/sequences.xml'
    ],
    'test': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': True,
    'application': True
}