from django.contrib.auth.models import User
from django import forms

class SignupForm(forms.ModelForm):

    password = forms.CharField(label ='Password', widget=forms.PasswordInput)
    Confirm_password = forms.CharField(label='Confirm_password', widget=forms.PasswordInput)
    class Meta:
        model = User
        
        fields = ['username', 'password', 'Confirm_password','first_name','last_name','email',]
    
    def clean_Confirm_password(self): #clean_[필드명]을 통해 cleaned_data를 받아오고 받아온 데이터들 중 password와 confirm password를 확인해서 일치하지 않으면 에러메시지
        cd = self.cleaned_data
        if cd['password'] != cd['Confirm_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다')
        return cd['Confirm_password'] #일치하면 confirmpassword반환