from odoo import models, fields, api

class UniversityDepartment(models.Model):
     _name = 'university.department'

     name=fields.Char("Nom" ,required=True)
     code=fields.Char("Code")

     professeur_ids = fields.One2many(comodel_name='university.professor' , inverse_name='departement_id')
     matiere_ids = fields.One2many(comodel_name='university.subject' , inverse_name='departement_id')
     etudiant_ids = fields.One2many(comodel_name='university.student' , inverse_name='departement_id')
