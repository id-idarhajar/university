from odoo import models, fields, api
from odoo.exceptions import ValidationError

class UniversityStudent(models.Model):
     _name = 'university.student'
     _rec_name = 'nom'

     prenom=fields.Char("Prénom", required=True)
     nom=fields.Char("Nom" , required=True)
     genre=fields.Selection([('homme','Homme'),('femme','Femme')], string="Genre")
     identite=fields.Char("Carte d'identité")
     adresse=fields.Text("Adresse")
     naissance=fields.Date("Date de naissance")
     date_inscription=fields.Datetime("Date d'inscription")
     num_tel=fields.Char("Téléphone")
     email=fields.Char("Email")
     active = fields.Boolean("Actif", default=True)
     niveau = fields.Selection([('l1','L1'),('l2','L2'),('m1','M1')], string="Niveau")
     moyenne = fields.Float("Moyenne")
     photo = fields.Image("Photo") 
     state = fields.Selection([
               ('draft', 'Brouillon'),
               ('inscrit', 'Inscrit'),
               ('archive', 'Archivé') ], default='draft')

     departement_id = fields.Many2one(comodel_name='university.department')
     classe_id = fields.Many2one(comodel_name='university.classroom')
     
     matiere_ids = fields.Many2many(related='classe_id.matiere_ids',string="Matières")

     @api.constrains('email')
     def _check_email(self):
          for record in self:
                if record.email and '@' not in record.email:
                  raise ValidationError("Email invalide!")
    
     # def name_get(self):
     #    result=[]
     #    for etudiant in self:
     #         name = '[' + etudiant.classe_id.classe_name_class + ']' +etudiant.prenom + ' ' +etudiant.nom
     #         result.append((etudiant.id, name))
     #    return result
     
     def action_inscrire(self):
      self.state = 'inscrit'
     
     def action_archive(self):
      self.state = 'archive'

