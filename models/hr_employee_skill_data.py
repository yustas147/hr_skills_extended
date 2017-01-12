# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging

_logger = logging.getLogger(name='YUSTAS')

class hr_employee_skill_data(models.Model):
    _name = 'hr.employee.skill.data'    
    
    #name = fields.Char('Name')
    percentage = fields.Integer(string='Grade of owning')
    description = fields.Text(string='Full skill owning employee description')    
    employee_id = fields.Many2one(comodel_name='hr.employee', string=None)
    skill_id = fields.Many2one(comodel_name='hr.skill', string=None)
    
    @api.model
    def sync_skills(self,obj):
        _logger.info('self is %s' % (unicode(self)))
        emp = obj.employee_id
        emp.update({"skill_ids":[(4,obj.skill_id.id)]})
        
class hr_employee(models.Model):
    _name = 'hr.employee'    
    _inherit = 'hr.employee'    
    
    hr_employee_skill_data_ids = fields.One2many(comodel_name='hr.employee.skill.data', 
                                                inverse_name='employee_id', 
                                                string='Skills')                                                
