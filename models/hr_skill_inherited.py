# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Skill(models.Model):
    _name = 'hr.skill'    
    _inherit = 'hr.skill'    
    
    percentage = fields.Integer(string='Grade of owning')
    description = fields.Text(string='Short Description')