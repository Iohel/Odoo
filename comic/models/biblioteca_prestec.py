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
    _name = 'biblioteca.prestec'
    #Hereda de "base.archive" (el modelo abstracto creado antes)
    
    _description = 'Prestec de biblioteca'

    #Parametros de ordenacion por defecto
    _order = 'fecha_retorno  desc, nombreComic'

    #ATRIBUTOS

    #PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    #Indicamos que atributo sera el que se usara para mostrar nombre.
    #Por defecto es "name", pero si no hay un atributo que se llama name, aqui lo indicamos
    #Aqui indicamos que se use el atributo "nombre"
    _rec_name = 'nombreComic'
    #Atributo nombre
    nombreComic = fields.Many2one('biblioteca.comic','Comic', required=True, index=True)
    nombreSocio = fields.Many2one('biblioteca.socio','Socio', required=True, index=True)
    fecha_prestada = fields.Date('Fecha Prestada')
    fecha_retorno = fields.Date('Fecha Retorno')


    @api.constrains('fecha_prestada')
    def _check_release_date(self):
        # Recorremos el modelo
        for record in self:
            #Comprobamos de cada registro, primero que haya una fecha_publicacion
            #y tras ello, que la fecha no sea posterior a la actual.
            if record.fecha_prestada and record.fecha_prestada < fields.Date.today():
                #Si procede, lanzamos una excepcion
                raise models.ValidationError('La fecha de lanzamiento no debe ser mayor a hoy')
    
    @api.constrains('fecha_retorno')
    def _check_release_date(self):
        # Recorremos el modelo
        for record in self:
            #Comprobamos de cada registro, primero que haya una fecha_publicacion
            #y tras ello, que la fecha no sea posterior a la actual.
            if record.fecha_retorno and record.fecha_retorno > record.fecha_prestada:
                #Si procede, lanzamos una excepcion
                raise models.ValidationError('La fecha de retorno debe ser mayor a la prestada')
    

   
 
  
    

   


