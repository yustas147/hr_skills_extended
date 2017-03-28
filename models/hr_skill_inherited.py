# -*- coding: utf-8 -*-
from openerp import models, fields, api

import logging
_logger = logging.getLogger(name='YUSTAS')

class Skill(models.Model):
    _name = 'hr.skill'    
    _inherit = 'hr.skill'    
    
    #description = fields.Text(string='Short Description')    
    
    @api.multi
    def get_all_children_ids(self):
        res = []
        resi = self.child_ids.mapped('id')
        if (len(resi)>0):
            res += resi
            for child in self.child_ids:
                res += child.get_all_children_ids()
        _logger.info("res is %s" % (unicode(res))) 
        return set(res)