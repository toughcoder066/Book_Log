from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.

def index(request):
    return render(request, 'book_logs/index.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')
    context = {'topics':topics}
    return render(request, 'book_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entry = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entry':entry}
    return render(request, 'book_logs/topic.html', context)

@login_required
def add_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('book_logs:topics'))
    context = {'form':form}
    return render(request, 'book_logs/add_topic.html', context)

@login_required
def add_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()

            return HttpResponseRedirect(reverse('book_logs:topic',args=[topic_id]))
    context = {'form':form, 'topic':topic} 

    return render(request, 'book_logs/add_entry.html', context)

@login_required
def edit_entry(request,entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('book_logs:topic',args=[topic.id]))
    context = {'form':form,'entry':entry}
    return render(request, 'book_logs/edit_entry.html', context)

def delete_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic_id = entry.topic_id
    entry.delete()
    return HttpResponseRedirect(reverse('book_logs:topic', args=[topic_id]))
    #return #render(request, 'book_logs/topic/.html') because the delete view doesnt need to render or create
    #a new page. theres no need to return render

