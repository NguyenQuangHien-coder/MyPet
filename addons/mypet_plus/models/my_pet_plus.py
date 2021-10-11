# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
# my_pet.xml
class MyPetPlus(models.Model):
    _inherit = "my.pet"
    _description = "Extend mypet model"

    # add new field
    toy = fields.Char('Pet Toy', required=False)
    # desc_gender = fields.Char('Desc gender', compute="_desc_gender", store=True)

    # modify old fields
    age = fields.Integer('Pet Age', default=2) # change default age from 1 to 2
    gender = fields.Selection(selection_add=[('sterilization', 'Sterilization')]) # add one more selection

    # @api.depends("gender")
    # def _desc_gender(self):
    #     for rec in self:
    #         if rec.gender == 'male':
    #             rec.Desc_gender = 'You have strong pet'
    #         elif rec.gender == 'female':
    #             rec.Desc_gender = 'You have weak beautiful pet'
    #         else:
    #             rec.Desc_gender = "You have crazy pet"




