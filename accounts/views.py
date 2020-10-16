from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import SignUpForm

def signup(request): 
    if request.method == 'POST': #POST일 때 
        signup_form = SignUpForm(request.POST) #SignupForm(request.POST)인 객체를 생성하고

    if signup_form.is_valid(): #유효하다면
        user_instance = signup_form.save(commit=False) #user_instance에 signup_form를 저장한다. 중복을 피하기 위해 commit=false
        user_instance.set_password(signup_form.cleaned_data['password']) #유효한 문자만 남긴상태에서 저장. 암호화2
        user_instance.save()
        return render(request, 'accounts/signup_complete.html', {'username':user_instance.username}) #username 나오도록 구현

    else:
        signup_form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form':signup_form.as_p})
    # if request.method == 'POST':  #입력방식이 POST로 오면 해당 정보들을 get을 통해 받고 
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     password2 = request.POST.get('passowrd2')
    #     print(username, password, password2)

#회원 객체 생성

#         user = User()  #User객체를 만들어서 해당 정보들을 user에 넣고 저장 
#         user.username = username
#         user.set_password(password)  #user.password = password > user.set_password(password)로 수정함으로서 admin에 들어가 비밀번호가 잘 설정된것확인가능
        
#         user.save()
#         return render(request, 'accounts/signup_complete.html')
# else: 
#             #todo: from 객체 만들어서 전달
#             context_values = {'form': 'this is form'} #context_values를 dictionary 형태로 만들고
#             return render(request, 'accounts/signup.html', context_values) #render를 통해 signup.html로 옮기고 context_values를 signup.html에 포함시킨다. 
            #signup.html에 {{form}}의 형태가 있으면 'this is form' 불러옴

            #render란? 1. 템플릿 불러오기 2. 템플릿 렌더(context_value를 해당 템플릿에 끼움) 3. HTTP Response하기 1. 완료된 내용 화면에 출력