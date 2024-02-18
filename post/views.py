from django.shortcuts import render,redirect
from .models import Post,Comment
from django.views.generic import ListView , DetailView
from .forms import CommentForm

class PostList(ListView):
    model =Post




def add_comment(request , pk):
    data= Post.objects.get(id=pk)
    coments=Comment.objects.filter(post=data)
    if request.method == 'POST':
        form =CommentForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user = request.user
            myform.post=data
            myform.save()
        return redirect(f'/{pk}')
            
    else:
        
        form = CommentForm()
    context = {
        'data': data,
        'form': form,
        'coments': coments
    }
    return render(request, 'post/post_detail.html', context)