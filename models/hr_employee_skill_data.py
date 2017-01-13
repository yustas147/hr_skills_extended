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
#        emp.update({"skill_ids":[(4,obj.skill_id.id)]})
        sk_ids = emp.hr_employee_skill_data_ids.mapped('skill_id').mapped('id')
        _logger.info('sk_ids is %s' % (sk_ids)) 
        emp.update({"skill_ids":[(6,0,sk_ids)]})
        
        
class hr_skill(models.Model):
    _name = 'hr.skill'    
    _inherit = 'hr.skill'    
    
    hr_employee_skill_data_ids = fields.One2many(comodel_name='hr.employee.skill.data', 
                                                inverse_name='skill_id', 
                                                string='Employee data')                                                
    
    
class hr_employee(models.Model):
    _name = 'hr.employee'    
    _inherit = 'hr.employee'    
    
    hr_employee_skill_data_ids = fields.One2many(comodel_name='hr.employee.skill.data', 
                                                inverse_name='employee_id', 
                                                string='Skills')                                                
                                                
    @api.model
    def sync_skills_2(self,obj):
        _logger.info('self is %s' % (unicode(self)))
        emp = obj
#        emp.update({"skill_ids":[(4,obj.skill_id.id)]})
        sk_ids = emp.hr_employee_skill_data_ids.mapped('skill_id').mapped('id')
        _logger.info('sk_ids is %s' % (sk_ids)) 
        emp.update({"skill_ids":[(6,0,sk_ids)]})
    