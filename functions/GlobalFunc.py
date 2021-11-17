# -*- coding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination
from django.core.mail import EmailMessage


class StandardListPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'


class MailService:
	def __init__(self,from_email):
		self.my_email=EmailMessage()
		self.my_email.from_email=from_email
	
	def set_recipient_list(self,recipient_list):
		self.my_email.to=recipient_list
		
	def set_subject(self,subject):
		self.my_email.subject=subject
	def set_body(self,body):
		self.my_email.body=body
	def set_cc(self,cc):
		self.my_email.cc=cc
	def set_bcc(self,bcc):
		self.my_email.bcc=bcc
	def set_connection(self,connection):
		self.my_email.connection=connection
	def set_attachment(self,attachment):
		self.my_email.attach_file(attachment)
	def set_headers(self,headers):
		self.my_email.headers=headers
	def set_reply_to(self,reply_to):
		self.my_email.reply_to=reply_to
	def message(self):
		return self.my_email.message()
	
	def send_email(self):
		self.my_email.send()