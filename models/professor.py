from odoo import models, fields, api

class UniversityProfessor(models.Model):
     _name = 'university.professor'
     _rec_name = 'nom'

     prenom  = fields.Char("Prénom" , required=True)
     nom = fields.Char("Nom", required=True)
     genre = fields.Selection([('homme','Homme'),('femme','Femme')], string="Genre")
     identite = fields.Char("Carte d'identité")
     adresse = fields.Text("Adresse")
     naissance = fields.Date("Date de naissance")
     date_debut = fields.Datetime("Date de début")
     num_tel = fields.Char("Téléphone")
     email = fields.Char("Email")

     departement_id = fields.Many2one(comodel_name='university.department')
     matiere_id = fields.Many2one(comodel_name='university.subject')

     classe_ids = fields.Many2many(comodel_name='university.classroom',
                                        relation= 'class_prof_rel',
                                        column1= 'prenom',
                                        column2='name_class')


