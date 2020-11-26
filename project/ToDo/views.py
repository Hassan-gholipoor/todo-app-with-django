from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Todo
# Create your views here.


class ShowTodo(ListView):
    model = Todo
    template_name = 'todo/home.html'


class DetailTodo(DetailView):
    template_name = 'todo/detail.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(Todo, slug=slug)
        return obj


class DeleteTask(DeleteView):
    template_name = 'todo/delete.html'
    success_url = reverse_lazy('todo:home')

    def get_object(self):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(Todo, slug=slug)
        return obj


class AddTask(CreateView):
    model = Todo
    fields = ('title', 'slug', 'description', 'time')
    template_name = 'todo/add_task.html'
    success_url = reverse_lazy('todo:home')


class UpdateTodo(UpdateView):
    template_name = 'todo/add_task.html'
    model = Todo
    fields = ('title', 'slug', 'description', 'time')
    success_url = reverse_lazy('todo:home')

