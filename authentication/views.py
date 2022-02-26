# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.views.generic import FormView,ListView,DetailView
from functions.template.custom_view import CustomListView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm,AuthenticationUserForm,AuthenticationGroupForm
from .models import AuthenticationUserModel,AuthenticationGroupModel,BranchModel,CompanyModel,UserGroupModel

class MyLoginView(LoginView):
	def form_valid(self, form):
		self.request.session.set_expiry(14400)
		if self.request.method == 'POST':
			login_form = self.request.POST
			if 'remember_me' in login_form:
				if login_form['remember_me'] == 'on':
					self.request.session.set_expiry(2592000)
		return super(MyLoginView, self).form_valid(form)


class MyLogOutView(LogoutView):

	def get_success_url_allowed_hosts(self):
		return redirect('/')


class MyRegisterView(FormView):
	template_name = 'authentication/form/register.html'
	form_class = RegisterForm

	def get_success_url(self):
		return '/authentication/login/'
	
	def form_valid(self,form):
		form.save()
		return super(MyRegisterView, self).form_valid(form)


class ListAuthenticationUser(CustomListView):
	template_name = "authentication/list/AuthenticationUser.html"
	model = AuthenticationUserModel
	title = "Kullanıcı Listesi"


class ListAuthenticationGroup(CustomListView):
	template_name = "authentication/list/AuthenticationGroup.html"
	model = AuthenticationGroupModel
	title = "Grup Listesi"
	
class ListBranch(CustomListView):
	template_name = "authentication/list/Branch.html"
	model = BranchModel
	title = "Şube Listesi"

	
class ListCompany(ListView):
	template_name = "authentication/list/Company.html"
	model = CompanyModel
	title = "Firma Listesi"

	def get_queryset(self):
		return self.model.objects.all()

class CreateAuthenticationUser(FormView):
	template_name = 'authentication/form/AuthenticationUser.html'
	form_class = AuthenticationUserForm

	def get_success_url(self):
		return '/authentication/list/AuthenticationUser'
	
	def form_valid(self,form):
		form.save(self.request.user.user_info.company_id)
		return super(CreateAuthenticationUser, self).form_valid(form)

class CreateAuthenticationGroup(FormView):
	template_name = 'authentication/form/AuthenticationGroup.html'
	form_class = AuthenticationGroupForm

	def get_success_url(self):
		return '/authentication/list/Authenticationgroup'
	
	def form_valid(self,form):
		form.save(self.request.user.user_info.company_id)
		return super(CreateAuthenticationUser, self).form_valid(form)

	def get_form(self,form_class=None):
		form = super(CreateAuthenticationGroup, self).get_form(form_class)
		form.fields["branch_id"].queryset=BranchModel.objects.company_all(company_id=self.request.user.user_info.company_id)
		return form