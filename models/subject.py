from odoo import models, fields, api

class UniversitySubject(models.Model):
     _name = 'university.subject'

     name=fields.Char("Nom")
     code=fields.Char("Code")

     departement_id = fields.Many2one(comodel_name='university.department')
     etudiant_id = fields.Many2one(comodel_name='university.student')
     professeur_ids = fields.One2many(comodel_name='university.professor' , inverse_name='matiere_id') 
     classe_ids = fields.Many2many(comodel_name='university.classroom',
                                   relation= 'sub_class_rel',
                                   column1= 'name',
                                   column2='name_class')
