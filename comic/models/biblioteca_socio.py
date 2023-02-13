# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# Modelo base, creado como modelo abstracto 
# Este modelo lo heredarara el modelo BibliotecaComic
# Y se ha creado puramente con fin didáctico para ver herencia entre modelos



#Definimos modelo Biblioteca comic
class Socio(models.Model):

    #Nombre y descripcion del modelo
    _name = 'biblioteca.socio'
    #Hereda de "base.archive" (el modelo abstracto creado antes)
    
    _description = 'Socio de biblioteca'

    #Parametros de ordenacion por defecto
    _order = 'cognom desc, nombre'

    #ATRIBUTOS

    #PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    #Indicamos que atributo sera el que se usara para mostrar nombre.
    #Por defecto es "name", pero si no hay un atributo que se llama name, aqui lo indicamos
    #Aqui indicamos que se use el atributo "nombre"
    _rec_name = 'nombre'
    #Atributo nombre
    nombre = fields.Char('Nombre', required=True, index=True)
    cognom = fields.Char('Cognom', required=True, index=True)
    identificador = fields.Char('Identificador', required=True, index=True)
    
    
    

   
 
  
    

   


