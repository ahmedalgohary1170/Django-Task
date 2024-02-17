from django.shortcuts import render,redirect
from .models import Post,Comment
from django.views.generic import ListView , DetailView
from .forms import CommentForm

class PostList(ListView):
    model =Post

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs ):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=self.get_object())
      
        return context



def my_view(request):
    if request.method == 'POST':
        form =CommentForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.author = request.user
            myform.save()
            
    else:
        form = CommentForm()
    return render(request, 'post/post_form.html', {'form': form})