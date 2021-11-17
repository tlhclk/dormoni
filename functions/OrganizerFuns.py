# -*- coding: utf-8 -*-
from django.apps import apps


class TransactionOrganizer:
	def __init__(self):
		self.TransactionModel=apps.get_model("financial","TransactionModel")
		self.AccountModel=apps.get_model("financial","AccountModel")

	def get_transaction_list(self,account_id):
		return self.TransactionModel.objects.filter(account_id=account_id).order_by("-date","-time","id")

	def organize(self,sel_account_list=[]):
		account_list=self.AccountModel.objects.all()
		result_dict={}
		for account_id in account_list:
			if len(sel_account_list)>0:
				if account_id.id not in sel_account_list:
					continue
			last_account_amount=account_id.amount
			transaction_list=self.get_transaction_list(account_id)
			self.revise_transaction(transaction_list,last_account_amount)
			result_dict[str(account_id)]="Done"
		return result_dict

	def set_account_amount(self,transaction,old_account_amount):
		type_out=1
		type_in=2
		transaction.account_amount=old_account_amount
		if transaction.type_id_id == type_out:
			new_account_amount = old_account_amount + transaction.amount
		else:
			new_account_amount = old_account_amount - transaction.amount
		transaction.save()
		return new_account_amount
		
	def revise_transaction(self,transaction_list,account_amount):
		for transaction in transaction_list:
			account_amount=self.set_account_amount(transaction,account_amount)
		return account_amount