from django.core import paginator
from django.shortcuts import render
from .forms import UserRegistrationForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import LeagueTeam, Match, News, Player, Squad
# Create your views here.

def home(request):

    matches = Match.objects.all()[:4]
    news = News.objects.all()[:4]
    main_news = news[0]
    other_news = news[1:4]


    return render(request, 'home/index.html', {'matches': matches, 'main_news': main_news, 'other_news': other_news,})


def club_directory(request):
    squad = Squad.objects.all()
    players = Player.objects.all()

    return render(request, 'home/club_squad.html', {'squad': squad, 'players': players})



def result( request):
    results = Match.objects.all()
    print(results)

    return render(request, 'home/results.html', {'results': results})


def point_table(request):
    league_teams = LeagueTeam.objects.all()
    d = {}
    for i in range(1,len(league_teams)+1):
        d[i] = league_teams[i-1]

    return render(request, 'home/point_table.html', {'league_teams': d})



def news(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, 4)
    page = request.GET.get('page')

    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list = paginator.page(1)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)



    return render(request, 'home/news.html', {'news_list':news_list, 'page': page})


def news_detail(request, news_id):
    news = News.objects.get(id=news_id)

    return render(request, 'home/news_detail.html', {'news':news})


def dashboard(request):

    return render(request, 'home/dashboard.html')


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'home/register_done.html', {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()

        return render(request, 'home/register.html', {'user_form': user_form})
