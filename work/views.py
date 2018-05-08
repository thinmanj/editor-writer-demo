from hamlpy.views.generic import ListView, DetailView
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout
from .models import Article


class ArticleList(ListView):
    model = Article


class ArticleDetail(DetailView):
    model = Article


def can_take(user):
    return user.is_writer


def can_send(user):
    return user.is_writer


def can_publish(user):
    return user.is_editor


@user_passes_test(can_take)
def take(request, pk):
    user = request.user

    article = get_object_or_404(Article, pk=pk)
    article.status = Article.StatusChoice.ASSIGNED
    article.writer = user

    article.save()

    return redirect(reverse('home'))


@user_passes_test(can_send)
def send(request, pk):
    article = get_object_or_404(Article, pk=pk)
    document = request.POST['document']
    article.document = document
    article.status = Article.StatusChoice.FOR_REVIEW

    article.save()

    return redirect(reverse('home'))


@user_passes_test(can_publish)
def publish(request, pk):
    user = request.user

    article = get_object_or_404(Article, pk=pk)
    article.status = Article.StatusChoice.APPROVED
    article.editor = user

    article.save()

    return redirect(reverse('home'))


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))
