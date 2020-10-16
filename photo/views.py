from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Photo
from django.http import HttpResponseRedirect
from django.contrib import messages

class PhotoList(ListView): #메인에서 보여줌, 북마크 모델 불러와서 데이터 활용할 것
    model = Photo
    template_name_suffix = '_list'

class PhotoCreate(CreateView): #성공하면 메인페이지로 돌아가도록
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_create'
    success_url = '/'

    def form_valid(self, form): 
        form.instance.author_id = self.request.user.id
        if form.is_valid():
           form.instance.save()
            
           return redirect('/')
        else:
            return self.render_to_response({'form': form})

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['author','text', 'image']
    template_name_suffix = '_update'

    def dispatch(self, request, *args, **kwargs): #사용자가 접속했을 때 get인지 post인지를 결정하고 분기를 자동으로 해줌
        object = self.get_object()
        if object.author != request.user: #작성자와 요청자가 다르면 
            messages.warning(request, '수정할 권한이 없습니다.')  #메시지를 주고
            return HttpResponseRedirect('/') #메인페이지로 이동
    # success_url = '/'
        else: 
            return super(PhotoUpdate, self).dispatch(request, *args,**kwargs) #else: super을 써서 원래 UpdateView가 실행되도록 해주며 super을 쓰게 되면 실행시 absolute_url로 자동적으로 이동. 
class PhotoDelete(DeleteView):
    model = Photo
    template_name_suffix = '_delete' #혼자 confirm delete기 때문
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '삭제할 권한이 없습니다')
            return HttpResponseRedirect('/')
        else:
            return super(PhotoDelete, self).dispatch(request, *args, **kwargs)

class PhotoDetail(DetailView):
    model = Photo
    template_name_suffix = '_detail'
