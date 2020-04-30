from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView
from .forms import PostForm,UpdatePostForm ,CommentForm, CommentRepliesForm
from .models import Post, Comment, CommentReplie
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
    posts = Post.objects.all().order_by('-id')

    # Filter
    if request.POST:
        if request.POST.get('filter') == "all":
            paginator = Paginator(posts, 8)
            page_post = paginator.get_page(request.GET.get('page'))
            return render(request, 'post/snippets/section.html', {'page_post':page_post})
        filter = Post.objects.filter(category=request.POST.get('filter'))
        paginator = Paginator(filter, 8)
        page_post = paginator.get_page(request.GET.get('page'))
        return render(request, 'post/snippets/section.html', {'page_post':page_post})

    # Search
    if request.GET:
        query = getQuerySet(request.GET.get('user_search', ''))
        paginator = Paginator(query, 8)
        page_post = paginator.get_page(request.GET.get('page'))
        return render(request, 'post/snippets/section.html', {'page_post':page_post})

    paginator = Paginator(posts, 8)
    page_post = paginator.get_page(request.GET.get('page'))
    return render(request, 'post/snippets/section.html', {'page_post':page_post})

def getQuerySet(query=None):
    query_set = []
    for q in query.split(" "): # Convert it to list
        posts = Post.objects.filter(Q(title__icontains=q)|
                                    Q(date_posted__icontains=q)|
                                    Q(category__icontains=q)|
                                    Q(url__icontains=q)).distinct()
        for post in posts:
            query_set.append(post)

    return list(set(query_set))

def postFormView(request):

    if not request.user.is_authenticated:
        return redirect('users:login')
    if request.POST:
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            form = PostForm()
            return redirect('index')
    else:
        form = PostForm()

    return render(request, 'post/post_form.html', {'form':form})

# Likes
def likesPostView(request, id):
    post = get_object_or_404(Post, id=id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('post:detail', post.slug)

# post and comments
def postDetailView(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)
    replies = CommentReplie.objects.all()
    display = True

    if request.POST:
        comment_form = CommentForm(request.POST or None)
        reply_form = CommentRepliesForm(request.POST or None)
        if comment_form.is_valid():
            cmt_obj = comment_form.save(commit=False)
            cmt_obj.author = request.user
            cmt_obj.post = post
            cmt_obj.save()
            comment_form = CommentForm()

            return redirect('post:detail', post.slug)

        if reply_form.is_valid():
            rpl_obj = reply_form.save(commit=False)
            rpl_obj.author = request.user
            rpl_obj.post = post
            rpl_obj.comment = Comment.objects.get(id=request.POST.get('comment'), post=post)
            rpl_obj.save()
            comment_form = CommentForm()

            return redirect('post:detail', post.slug)
        return redirect('post:detail', post.slug)

    else:
        comment_form = CommentForm()
        reply_form = CommentRepliesForm()

    return render(request, 'post/post_detail.html', {'post':post,
                                                    'comments':comments,
                                                    'comment_form':comment_form,
                                                    'replies':replies,
                                                    'reply_form':reply_form,
                                                    'display':display})

def userPostsView(request, id):
    user_posts = Post.objects.filter(author=id)
    return render(request, 'post/user_posts.html', {'user_posts':user_posts})

def postUpdateView(request, id):
    if not request.user.is_authenticated:
        return redirect('index')

    post = get_object_or_404(Post, id=id)

    if request.user != post.author:
        return HttpResponse("This is not your post!")

    if request.POST:
        form = UpdatePostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save(commit=True)
            return redirect('post:detail', post.slug)
    else:
        form = UpdatePostForm(initial={"title":post.title,
                                 "post_image":post.post_image,
                                 "category": post.category,
                                 "body":post.body,
                                 "url":post.url})

    return render(request, 'post/update_post.html', {'form':form})

class DeletePost(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'post/delete_confirm.html'
    success_url = '/'

    def test_func(self):
        if self.request.user == self.get_object().author:
            return True
        return False

def commentUpdateView(request, id):
    if not request.user.is_authenticated:
        return redirect('users:login')

    comment = get_object_or_404(Comment, id=id)

    if request.user != comment.author:
        return HttpResponse('You are not the author of this comment!')

    form = CommentForm(initial={'body':comment.body})
    if request.method == 'POST':
        form = CommentForm(request.POST or None, instance=comment)
        if form.is_valid():
            form.save(commit=True)
            return redirect('post:detail', comment.post.slug)

    return render(request, 'post/update_comment.html', {'form':form, 'comment':comment})

class DeleteComment(DeletePost, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = "post/comment_delete_confirm.html"
    success_url = "/"

    def test_func(self):
        if self.request.user == self.get_object().author:
            return True
        return False

def replyUpdateView(request, id):
    if not request.user.is_authenticated:
        return redirect('users:login')

    reply = get_object_or_404(CommentReplie, id=id)
    if request.user != reply.author:
        return HttpResponse('This is not your comment reply!')

    form = CommentRepliesForm(initial={'reply':reply.reply})
    if request.POST:
        form = CommentRepliesForm(request.POST or None, instance=reply)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.post = reply.post
            obj.comment = reply.comment
            obj.save()
            form = CommentRepliesForm()
            return redirect('post:detail', reply.post.slug)

    return render(request, 'post/update_reply.html', {'form':form, 'reply':reply})

class DeleteReply(DeleteView, UserPassesTestMixin, LoginRequiredMixin):
    model = CommentReplie
    template_name = "post/comment_reply_delete_confirm.html"
    success_url = '/'

    def test_func(self):
        if self.request.user == self.get_object().author:
            return True
        return False
