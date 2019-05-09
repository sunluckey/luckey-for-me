from django.db import models
from django import forms
from captcha.fields import CaptchaField
# Create your models here.

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',
                               max_length=128,
                               min_length=1,
                               widget=forms.TextInput(attrs={'class': 'in-1', 'placeholder': "用户名不能为空"}))
    password = forms.CharField(label='密码',
                               max_length=256,
                               min_length=8,
                               widget=forms.PasswordInput(attrs={'class': 'in-1', 'placeholder': "密码大于8位"}))
    captcha = CaptchaField(label='验证码')
class User(models.Model):

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

class RegisterForm(forms.Form):

    username = forms.CharField(label="用户名",
                               max_length=128,
                               min_length=1,
                               widget=forms.TextInput(attrs={'class': 'in-1', 'placeholder': "用户名至少一个字符"}))
    password1 = forms.CharField(label="密码",
                                max_length=256,
                                min_length=8,
                                widget=forms.PasswordInput(attrs={'class': 'in-1', 'placeholder': "密码至少8位"}))
    password2 = forms.CharField(label="确认密码",
                                max_length=256,
                                min_length=8,
                                widget=forms.PasswordInput(attrs={'class': 'in-1', 'placeholder': "再次输入密码"}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'in-1'}))
    # captcha = CaptchaField(label='验证码')