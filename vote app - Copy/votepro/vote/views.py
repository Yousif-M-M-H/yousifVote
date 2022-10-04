from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Votetitle, Voting
from .forms import VoteForm


# Create your views here.


def index(request):
    return HttpResponse("Iam yousif.")


class ShowForm(ListView):
    model = Voting
    template_name = 'vote/show_form.html'


def create(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('show')
    else:
        form = VoteForm()
    context = {'form': form}
    return render(request, 'vote/show_vote.html', context)


def votedetails(request, poll_id):
    poll = Voting.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.choice1_count += 1
        elif selected_option == 'option2':
            poll.choice2_count += 1
        elif selected_option == 'option3':
            poll.choice3_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('show_form')

    context = {
        'poll': poll
    }
    return render(request, 'vote/voting_list.html', context)


def results(request, poll_id):
    poll = Voting.objects.get(pk=poll_id)

    context = {
        "poll": poll
    }
    return render(request, 'vote/results.html', context)
