from odoo import models, fields, api


class UniversityStudent(models.Model):
     _name = 'university.student'
     _rec_name = 'nom'

     prenom=fields.Char("Prénom")
     nom=fields.Char("Nom")
     genre=fields.Selection([('homme','Homme'),('femme','Femme')], string="Genre")
     identite=fields.Char("Carte d'identité")
     adresse=fields.Text("Adresse")
     naissance=fields.Date("Date de naissance")
     date_inscription=fields.Datetime("Date d'inscription")
     num_tel=fields.Char("Téléphone")
     email=fields.Char("Email")

     departement_id = fields.Many2one(comodel_name='university.department')
     classe_id = fields.Many2one(comodel_name='university.classroom')
     matiere_ids = fields.One2many(comodel_name='university.subject' , inverse_name='etudiant_id')

    
     # def name_get(self):
     #    result=[]
     #    for etudiant in self:
     #         name = '[' + etudiant.classe_id.classe_name_class + ']' +etudiant.prenom + ' ' +etudiant.nom
     #         result.append((etudiant.id, name))
     #    return result
     

