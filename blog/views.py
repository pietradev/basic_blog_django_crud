from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Post

## Think of views as the logic that determines what content is displayed to the user when they visit a particular URL.
# Create your views here.

##Formulario para criar ou editar um post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post #Formulario baseado no modelo Post definido em models.py
        fields = ['title', 'content'] # Campos que serao exibidos no formulario

#View para criar um novo post
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo post no banco de dados
            return redirect('/')  # Redireciona para a página inicial após salvar
    else:
        form = PostForm()  # Exibe um formulário vazio para uma requisição GET
    
    # Aqui garantimos que sempre retornaremos uma resposta válida
    return render(request, 'blog/post_new.html', {'form': form})

# Exibe todos os posts de uma vez só 
def post_list(request):
    posts = Post.objects.all().order_by('created_at') ## fetches all the posts from the Post model 
    return render(request, 'blog/post_list.html', {'posts': posts})

# Exibe apenas um post
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post':post})

