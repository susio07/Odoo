# -*- coding: utf-8 -*- 

from odoo import models, fields


class TareaRecord(models.Model):

    _name = "tarea.tarea"
    nombre = fields.Char(string='Nombre')
    foto = fields.Binary(string='Foto')
    descripcion = fields.Char(string='Descripción', required=True)
    terminada = fields.Boolean(string='Terminada',required=True)
    activa = fields.Boolean(string='Activa',required=True)

