# -*- coding: utf-8 -*-
from django.apps import apps
from django.views.generic import FormView,ListView,DetailView


class CustomListView(ListView):
	def get_queryset(self):
		if self.get_user_type():
			return self.model.objects.company_all(company_id=self.request.user.user_info.branch_id.company_id)
		else:
			if hasattr(self.model,"branch_id"):
				return self.model.objects.branch_all(branch_id=self.request.user.user_info.branch_id)
			else:
				return self.model.objects.company_all(company_id=self.request.user.user_info.branch_id.company_id)

	
	def get_user_type(self):
		if self.request.user.user_info.branch_id.code=="00":
			#tüm şubeleri görebilir
			return True
		else:
			return False