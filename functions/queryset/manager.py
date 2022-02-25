# -*- coding: utf-8 -*-
from django.db import models


class CustomManager(models.Manager):
    
    def company_all(self,*args,**kwargs):
        if "company_id" in kwargs:
            return self.filter(company_id=kwargs.get("company_id"))
        else:
            return self.filter(company_id=None)
    
    def branch_all(self,*args,**kwargs):
        if "branch_id" in kwargs:
            return self.filter(branch_id=kwargs.get("branch_id"))
        else:
            return self.filter(branch_id=None)

        

