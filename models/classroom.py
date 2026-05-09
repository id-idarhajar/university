from odoo import models, fields, api
from odoo.exceptions import ValidationError

class UniversityClassroom(models.Model):
     _name = 'university.classroom'
     _rec_name = 'name_class'


     name_class=fields.Char("Nom" ,required=True)
     code=fields.Char("Code")
     nombre_etudiants = fields.Integer(compute="_compute_nombre", store=True)
     nombre_prof = fields.Integer(compute="_compute_prof", store=True)
     


     etudiant_ids = fields.One2many(comodel_name='university.student' , inverse_name='classe_id')

    

     matiere_ids = fields.Many2many(comodel_name='university.subject',
                                        relation='sub_class_rel',
                                        column1='name_class',
                                        column2='name')
     
     professeur_ids = fields.Many2many(comodel_name='university.professor',
                                        relation= 'class_prof_rel',
                                        column1='name_class',
                                        column2='prenom')
                                    
     
     @api.depends('etudiant_ids')
     def _compute_nombre(self):
          for rec in self:
             rec.nombre_etudiants = len(rec.etudiant_ids)

     @api.depends('professeur_ids')
     def _compute_prof(self):
          for rec in self:
             rec.nombre_prof = len(rec.professeur_ids)

     
     @api.constrains('professeur_ids')
     def _check_professeur(self):
         for rec in self:
             if not rec.professeur_ids:
               raise ValidationError("la classe doit avoir au moins un professeur !")
             
     @api.constrains('etudiant_ids')
     def _check_capacity(self):
         for rec in self:
             if len(rec.etudiant_ids) > 3:
               raise ValidationError("Max 3 etudiants!")
             
 