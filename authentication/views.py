# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.views.generic import FormView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .models import UserIpModel
from .forms import RegisterForm
from functions.other.Global import MailService

class MyLoginView(LoginView):

    def get_perm(self, user_name, ip):
        perm_obj = UserIpModel.objects.get(ip_address=ip)
        user_obj = User.objects.get(username=user_name)
        if perm_obj:
            if perm_obj.permission:
                if user_obj:
                    return True
            elif user_obj:
                new_user_ip = UserIpModel.objects.create(ip=ip)
                new_user_ip.save()
                ms = MailService('admin@myerp.talhacelik.com')
                ms.set_recipient_list(['talhacelk@gmail.com'])
                ms.set_subject('Yeni Ip Ile Giris Denemesi')
                ms.set_headers('Yeni Ip Ile Giris Denemesi')
                message = 'Giris Benemesi Bilgileri:\n\nIp: %s\nKullanıcı Adı: %s\nKullanıcı Mail Adresi: %s\nKullanıcı Adı Soyadı: %s\nYetkilendirme Anahtarı: %s\n\nAdresinde yapılan kullanıcı girisi engellendi\nYetkilendirmek İcin <a href="https://myerp.talhacelik.com/register_validation/?validation_code=%s">Buraya Tıklayınız!</a>\n' % (ip, user_obj.username, user_obj.email, user_obj.get_full_name(), new_user_ip.auth_key, new_user_ip.auth_key)
                ms.set_body(message)
                ms.send_email()
        return False

    def form_valid(self, form):
        ip = self.request.META['REMOTE_ADDR']
        self.request.session.set_expiry(14400)
        if self.request.method == 'POST':
            login_form = self.request.POST
            user_name = login_form['username']
            if not self.get_perm(user_name, ip):
                return redirect('/login/?warning=NoPermission')
            if 'remember_me' in login_form:
                if login_form['remember_me'] == 'on':
                    self.request.session.set_expiry(2592000)
        return super(MyLoginView, self).form_valid(form)

    def get_success_url(self):
        return redirect('HomePage').url


class MyLogOutView(LogoutView):

    def get_success_url_allowed_hosts(self):
        return redirect('/').url


class MyRegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm

    def get_success_url(self):
        return '/login/'


class IpValidationView(View):

    def grant_permission(self, user_ip):
        user_ip.permission = True
        user_ip.save()

    def get(self, request):
        if 'validation_code' in request.GET:
            auth_key = request.GET['validation_code'].replace(' ', '+')
            user_ip = UserIpModel.objects.get(auth_key=auth_key)
            self.grant_permission(user_ip)
            return redirect('/LoginPage/')
        return redirect('/IndexPage/')