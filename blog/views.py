from django.shortcuts import render
from django.http import HttpResponse 
from django.urls import reverse

from django.views.generic import ListView 		# class based views 
from django.views.generic import DetailView 	# detailed view for each post 
from django.views.generic import CreateView     # create view for post create 

from .models import Post

# def home(request):
# 	return render(request, 'blog/base.html', {'posts':Post.objects.all(), 'first':Post.objects.first()})


# Class based views
class PostListView(ListView):
	model = Post 						# name of the model to interact with 
	template_name = 'blog/base.html'    # name of the html page to render 
	context_object_name = 'posts'		# tell django which variable to loop over 
	ordering = ['-datePosted']			# order in which the posts are to be displayed 


# detailed view for each post 
class PostDetailView(DetailView):
	model = Post 
	# template_name = 'blog/Post_Detail.html'


class PostCreateView(CreateView):
	model = Post 
	fields = ['title', 'content']
	# template_name = 'blog/Post_Form.html'

	def form_valid(self, form):
		form.instance.author = self.request.user 
		return super().form_valid(form) 


