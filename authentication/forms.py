# -*- coding: utf-8 -*-
import imp
from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import CompanyModel,BranchModel,AuthenticationGroupModel,AuthenticationUserModel,UserGroupModel
UserModel = get_user_model()


class RegisterForm(forms.Form):
	email = forms.EmailField(label='E-Mail', widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
	username = forms.CharField(label='Kullanıcı Adı', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	first_name = forms.CharField(label='Adı', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	last_name = forms.CharField(label='Soyadı', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	password = forms.CharField(label='Şifre', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
	password_confirm = forms.CharField(label='Şifre Onayı', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
	profile_pic = forms.CharField(label='Profil Fotoğrafı', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
	desc = forms.CharField(label='Açıklama', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

	company_status = forms.CharField(label='Durumu', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	registration_number = forms.CharField(label='Sicil No', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	chamber_registraion_sytem_no = forms.CharField(label='Oda Sicil No', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	company_title = forms.CharField(label='Firma Ünvanı', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	name = forms.CharField(label='Adı', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
	second_name = forms.CharField(label='İkincil Adı', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
	business_address = forms.CharField(label='İş Adresi', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	phone_number = forms.CharField(label='Telefon No', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	fax_number = forms.CharField(label='Fax No', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
	hyperlink = forms.CharField(label='Web Sayfası', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	date_of_registration = forms.DateField(label='Odaya Kayıt Tarihi', widget=forms.TextInput(attrs={'class': 'form-control datetimepicker form-date','data-toggle':'datetimepicker','data-target':'#id_date_of_registration'}), required=True)
	capital = forms.CharField(label='Sermaye', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	occupational_group = forms.CharField(label='Meslek Grubu', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	nace_codes = forms.CharField(label='Nace Kodları', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	desc2 = forms.CharField(label='Açıklama', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

	class Meta:
		fields = [
		 'email', 'username', 'first_name', 'last_name', 'password','password_confirm','profile_pic','desc'
		 'company_status','registration_number','chamber_registraion_sytem_no','company_title','name','second_name','business_address','phone_number','fax_number','hyperlink','date_of_registration','capital','occupational_group','nace_group','desc2']

	def clean_email(self):
		email = self.cleaned_data['email']
		email_list = UserModel.objects.filter(email=email)
		if len(email_list) > 0:
			raise ValidationError('Girdiğiniz Mail Adresi Kayıtlı!')
		return email

	def clean_username(self):
		username = self.cleaned_data['username']
		username_list = UserModel.objects.filter(username=username)
		if len(username_list) > 0:
			raise ValidationError('Girdiğiniz Kullanıcı Adı Kayıtlı!')
		return username

	def clean_password(self):
		password = self.cleaned_data["password"]
		int_list=["0","1","2","3","4","5","6","7","8","9"]
		l_str_list=["q","w","e","r","t","y","u","ı","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
		b_str_list=["Q","W","E","R","T","Y","U","I","O","P","L","K","J","H","G","F","D","S","A","Z","X","C","V","B","N","M"]
		sym_list=["_","-","*","+","?",".","/"]
		int_c=0
		l_str_c=0
		b_str_c=0
		sym_c=0
		for l in password:
			if l in int_list:
				int_c+=1
			if l in l_str_list:
				l_str_c+=1
			if l in b_str_list:
				b_str_c+=1
			if l in sym_list:
				sym_c+=1
		if int_c==0 or l_str_c==0 or b_str_c==0 or sym_c==0 or len(password)<8:
			raise ValidationError("Lütfen en az 1 rakam, en az 1 küçük harf, en az 1 büyük harf, en az 1 sembol (_-*+?./) ve en az 8 haneli bir şifre giriniz")
		return password
	
	def clean(self):
		password = self.cleaned_data['password']
		password_confirm = self.cleaned_data["password_confirm"]
		if password!=password_confirm:
			raise ValidationError("Şifre Onayı Yanlış Girilmiştir. Lütfen Şifre ve Şifre Onayını Aynı Giriniz.")
		super().clean()
	
	def save(self):
		email = self.cleaned_data['email']
		username = self.cleaned_data['username']
		first_name = self.cleaned_data['first_name']
		last_name = self.cleaned_data['last_name']
		password = self.cleaned_data['password']
		# New User Create
		user_id=UserModel.objects.create(username=username, email=email, password=(make_password(password)), first_name=first_name, last_name=last_name, is_superuser=True, is_active=False, is_staff=True)
		# New Company Create
		company_id = CompanyModel()
		company_id.company_status = self.cleaned_data['company_status']
		company_id.registration_number = self.cleaned_data['registration_number']
		company_id.chamber_registraion_sytem_no = self.cleaned_data['chamber_registraion_sytem_no']
		company_id.company_title = self.cleaned_data['company_title']
		company_id.name = self.cleaned_data['name']
		company_id.second_name = self.cleaned_data['second_name']
		company_id.business_address = self.cleaned_data['business_address']
		company_id.phone_number = self.cleaned_data['phone_number']
		company_id.fax_number = self.cleaned_data['fax_number']
		company_id.hyperlink = self.cleaned_data['hyperlink']
		company_id.date_of_registration = self.cleaned_data['date_of_registration']
		company_id.capital = self.cleaned_data['capital']
		company_id.occupational_group = self.cleaned_data['occupational_group']
		company_id.nace_codes = self.cleaned_data['nace_codes']
		company_id.desc = self.cleaned_data['desc2']
		company_id.save()
		# New Branch Create
		branch_id=BranchModel()
		branch_id.name="Genel"
		branch_id.code="00"
		branch_id.company_id=company_id
		branch_id.save()
		# New Group Create
		group_id=AuthenticationGroupModel()
		group_id.name="Yönetici"
		group_id.code="000"
		group_id.branch_id=branch_id
		group_id.save()
		# New User Info Create
		aum_id=AuthenticationUserModel()
		aum_id.user_id=user_id
		aum_id.company_id=company_id
		aum_id.profile_pic = self.cleaned_data['profile_pic']
		aum_id.desc = self.cleaned_data['desc']
		aum_id.save()
		# New User Group Create
		ug_id=UserGroupModel()
		ug_id.user_id=aum_id
		ug_id.company_id=company_id
		ug_id.group_id=group_id
		ug_id.save()
		# Her Tabloya Yetki
		# Her Tablo Alanına Yetki


class AuthenticationUserForm(forms.Form):
	email = forms.EmailField(label='E-Mail', widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
	username = forms.CharField(label='Kullanıcı Adı', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	first_name = forms.CharField(label='Adı', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	last_name = forms.CharField(label='Soyadı', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	profile_pic = forms.CharField(label='Profil Fotoğrafı', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
	desc = forms.CharField(label='Açıklama', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)


	class Meta:
		fields = [
		 'email', 'username', 'first_name', 'last_name','profile_pic','desc']

	def clean_email(self):
		email = self.cleaned_data['email']
		email_list = UserModel.objects.filter(email=email)
		if len(email_list) > 0:
			raise ValidationError('Girdiğiniz Mail Adresi Kayıtlı!')
		return email

	def clean_username(self):
		username = self.cleaned_data['username']
		username_list = UserModel.objects.filter(username=username)
		if len(username_list) > 0:
			raise ValidationError('Girdiğiniz Kullanıcı Adı Kayıtlı!')
		return username
	
	def save(self,company_id):
		email = self.cleaned_data['email']
		username = self.cleaned_data['username']
		first_name = self.cleaned_data['first_name']
		last_name = self.cleaned_data['last_name']
		password = "test12345"
		# New User Create
		user_id=UserModel.objects.create(username=username, email=email, password=make_password(password ),first_name=first_name, last_name=last_name, is_superuser=True, is_active=False, is_staff=True)
		# New User Info Create
		aum_id=AuthenticationUserModel()
		aum_id.user_id=user_id
		aum_id.company_id=company_id
		aum_id.profile_pic = self.cleaned_data['profile_pic']
		aum_id.desc = self.cleaned_data['desc']
		aum_id.save()
		# New User Group Create
		group_id= get_object_or_404(AuthenticationGroupModel,code="000",branch_id__code="00",branch_id__company_id=company_id)
		ug_id=UserGroupModel()
		ug_id.user_id=aum_id
		ug_id.company_id=company_id
		ug_id.group_id=group_id
		ug_id.save()

		
class AuthenticationGroupForm(forms.Form):
	branch_id = forms.ModelChoiceField(queryset=BranchModel.objects.all(),label='Şubesi', widget=forms.Select(attrs={'class': 'form-control form-dropdown-select2'}), required=True)
	name = forms.CharField(label='Adı', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	code = forms.CharField(label='Kodu', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	desc = forms.CharField(label='Açıklama', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

	class Meta:
		fields = ['branch_id', 'name', 'code', 'desc']

	def save(self):
		name = self.cleaned_data['name']
		code = self.cleaned_data['code']
		desc = self.cleaned_data['desc']
		branch_id = self.cleaned_data['branch_id']
		# New Group Create
		group_id = AuthenticationGroupModel()
		group_id.name=name
		group_id.code=code
		group_id.desc=desc
		group_id.branch_id=get_object_or_404(BranchModel,pk=branch_id)
		group_id.save()
