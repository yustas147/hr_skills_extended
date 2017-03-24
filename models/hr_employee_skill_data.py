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
        _logger.info('from sync_skills: sk_ids is %s' % (sk_ids)) 
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
        sk_child_ids = emp.hr_employee_skill_data_ids.mapped('skill_id').mapped('child_ids').mapped('id')
        sk_ids = sk_ids + sk_child_ids
        sk_ids = set(sk_ids)
        
        _logger.info('sk_ids is %s' % (sk_ids)) 
        
        datas=[]
        _logger.info('hr_employee_skill_data_ids is %s' % (emp.hr_employee_skill_data_ids)) 
        _logger.info('hr_employee_skill_data_ids.mapped is %s' % (emp.hr_employee_skill_data_ids.mapped('skill_id').mapped('id'))) 
        for skid in [sk for sk in sk_ids if sk not in emp.hr_employee_skill_data_ids.mapped('skill_id').mapped('id')]:
#        for skid in sk_ids:
            datas.append((0,0,{'skill_id':skid, 'employee_id':emp.id}))
#            emp.update({"hr_employee_skill_data_ids":[(0,0,{'skill_id':skid, 'employee_id':emp.id})]})
    
        _logger.info('datas is %s' % (datas)) 
        emp.update({"skill_ids":[(6,0,sk_ids)], "hr_employee_skill_data_ids":datas})
#        emp.update({"skill_ids":[(6,0,sk_ids)]})
        #self.env['hr.employee.skill.data'].create(datas)
        
    