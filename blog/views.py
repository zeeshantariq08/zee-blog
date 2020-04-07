from django.shortcuts import render
# from django.http import HttpResponse


posts = [
	{
		'author':'zeeshan Tariq',
		'title':'Blog Post 1',
		'content':'first Post Content',
		'date_posted':'April 8, 2020',
	},
	{
		'author':'ZT',
		'title':'Blog Post 2',
		'content':'Second Post Content',
		'date_posted':'April 8, 2020',
	}

]



def about(request):

	context = {
		'posts':posts
	}
	# return HttpResponse('Blog About')
	return render(request,'blog/about.html',context)



def home(request):
	context = {
		'posts':posts
	}
	# return HttpResponse('Blog Home')
	return render(request,'blog/home.html',context)






