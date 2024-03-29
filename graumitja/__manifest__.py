# -*- coding: utf-8 -*-
{
    'name': "Institut Joan Ramis",  # Titulo del módulo
    'summary': "Gestionar Graus",  # Resumen de la funcionaliadad
    'description': """Gestor de Insitut""",  

    #Indicamos que es una aplicación
    'application': True,
    'author': "DAMB",
    'website': "http://iesjoanramis.org",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        #Estos dos primeros ficheros:
        #1) El primero indica grupo de seguridad basado en rol
        #2) El segundo indica la politica de acceso del modelo
        #Mas información en https://www.odoo.com/documentation/15.0/es/developer/howtos/rdtraining/05_securityintro.html
        #Y en www.odoo.yenthevg.com/creating-security-groups-odoo/ 
        'security/groups.xml',
        'security/ir.model.access.csv',
        #Cargamos la vista de la biblioteca de comics
        'views/institut_cicle.xml',
        'views/institut_modul.xml',
        'views/institut_alumne.xml',
        'views/institut_professor.xml'
        
        
        
          
    ],
    # Fichero con data de demo si se inicializa la base de datos con "demo data" (No incluido en ejemplo)
    # 'demo': [
    #     'demo.xml'
    # ],
}
