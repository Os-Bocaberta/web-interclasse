from django.shortcuts import render
from django.shortcuts import redirect
from .models import Teams, Players, PlayerModality, VolleySets, Match, TeamMatchInfo, Penalties, Rewards, Assistances, Chaveamento

# Create your views here.

def index(request):
    return redirect('/volleyball/games/')

def game(request, id):
    print(request.get_full_path())
    # Jogo Masculido de Futsal que está Acontecendo
    if (Match.objects.all().filter(id=id).filter(status=1).filter(sex=0).filter(modality=0)):
        ongoing_match = Match.objects.get(id=id)
        team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match.id).select_related('team')

        team_a_players = PlayerModality.objects.all().filter(team=team_match_info[0].team.id).filter(modality=0).filter(sex=0).select_related('player')
        team_b_players = PlayerModality.objects.all().filter(team=team_match_info[1].team.id).filter(modality=0).filter(sex=0).select_related('player')

        return render(request, 'futsal_ongoing_game.html', {'match_info': ongoing_match,'team_A': team_match_info[0], 'team_B': team_match_info[1], 'team_a_players': team_a_players, 'team_b_players': team_b_players})
    
    # Jogo Feminino de Futsal que está Acontecendo
    elif (Match.objects.all().filter(id=id).filter(status=1).filter(sex=1).filter(modality=0)):
        ongoing_match = Match.objects.get(id=id)
        team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match.id).select_related('team')

        team_a_players = PlayerModality.objects.all().filter(team=team_match_info[0].team.id).filter(modality=0).filter(sex=1).select_related('player')
        team_b_players = PlayerModality.objects.all().filter(team=team_match_info[1].team.id).filter(modality=0).filter(sex=1).select_related('player')

        return render(request, 'futsal_ongoing_game.html', {'match_info': ongoing_match,'team_A': team_match_info[0], 'team_B': team_match_info[1], 'team_a_players': team_a_players, 'team_b_players': team_b_players})
    
    # Jogo Masculino de Futsal Finalizado
    elif (Match.objects.all().filter(id=id).filter(status=2).filter(sex=0).filter(modality=0)):
        ongoing_match = Match.objects.get(id=id)
        team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match.id).select_related('team')

        team_a_score = Rewards.objects.all().filter(team_match=team_match_info[0].id).count()
        team_b_score = Rewards.objects.all().filter(team_match=team_match_info[1].id).count()
          
        team_a_score_players = Rewards.objects.all().filter(team_match=team_match_info[0].id).order_by('-id' )[:3]
        team_b_score_players = Rewards.objects.all().filter(team_match=team_match_info[1].id).order_by('-id' )[:3]
        
        team_a_players = PlayerModality.objects.all().filter(team=team_match_info[0].team.id).filter(modality=0).filter(sex=0).select_related('player')
        team_b_players = PlayerModality.objects.all().filter(team=team_match_info[1].team.id).filter(modality=0).filter(sex=0).select_related('player')

        team_a_fauls = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=0).count()
        team_b_fauls = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=0).count()
                
        team_a_reds = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=2).count()
        team_b_reds = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=2).count()
        
        team_a_yellows = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=1).count()
        team_b_yellows = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=1).count()

        return render(request, 'futsal_finished_game.html', {'match_info': ongoing_match,'team_A': team_match_info[0], 'team_B': team_match_info[1], 'team_a_players': team_a_players, 'team_b_players': team_b_players, 'team_a_score': team_a_score, 'team_b_score': team_b_score, 'team_a_score_players': team_a_score_players, 'team_b_score_players': team_b_score_players, 'team_a_fauls': team_a_fauls, 'team_b_fauls': team_b_fauls, 'team_a_reds': team_a_reds, 'team_b_reds': team_b_reds, 'team_a_yellows': team_a_yellows, 'team_b_yellows': team_b_yellows})
    
    # Jogo Feminino de Futsal Finalizado
    elif (Match.objects.all().filter(id=id).filter(status=2).filter(sex=1).filter(modality=0)):
        ongoing_match = Match.objects.get(id=id)
        team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match.id).select_related('team')

        team_a_score = Rewards.objects.all().filter(team_match=team_match_info[0].id).count()
        team_b_score = Rewards.objects.all().filter(team_match=team_match_info[1].id).count()
          
        team_a_score_players = Rewards.objects.all().filter(team_match=team_match_info[0].id).order_by('-id' )[:3]
        team_b_score_players = Rewards.objects.all().filter(team_match=team_match_info[1].id).order_by('-id' )[:3]
        
        team_a_players = PlayerModality.objects.all().filter(team=team_match_info[0].team.id).filter(modality=0).filter(sex=1).select_related('player')
        team_b_players = PlayerModality.objects.all().filter(team=team_match_info[1].team.id).filter(modality=0).filter(sex=1).select_related('player')

        team_a_fauls = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=0).count()
        team_b_fauls = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=0).count()
                
        team_a_reds = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=2).count()
        team_b_reds = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=2).count()
        
        team_a_yellows = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=1).count()
        team_b_yellows = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=1).count()

        return render(request, 'futsal_finished_game.html', {'match_info': ongoing_match,'team_A': team_match_info[0], 'team_B': team_match_info[1], 'team_a_players': team_a_players, 'team_b_players': team_b_players, 'team_a_score': team_a_score, 'team_b_score': team_b_score, 'team_a_score_players': team_a_score_players, 'team_b_score_players': team_b_score_players, 'team_a_fauls': team_a_fauls, 'team_b_fauls': team_b_fauls, 'team_a_reds': team_a_reds, 'team_b_reds': team_b_reds, 'team_a_yellows': team_a_yellows, 'team_b_yellows': team_b_yellows})
    
    # Jogo Masculino de Vôlei que está Acontecendo
    elif (Match.objects.all().filter(id=id).filter(status=1).filter(sex=0).filter(modality=1)):
        ongoing_match = Match.objects.get(id=id)
        team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match.id).select_related('team')

        team_a_players = PlayerModality.objects.all().filter(team=team_match_info[0].team.id).filter(modality=1).filter(sex=0).select_related('player')
        team_b_players = PlayerModality.objects.all().filter(team=team_match_info[1].team.id).filter(modality=1).filter(sex=0).select_related('player')

        return render(request, 'volleyball_ongoing_game.html', {'match_info': ongoing_match,'team_A': team_match_info[0], 'team_B': team_match_info[1], 'team_a_players': team_a_players, 'team_b_players': team_b_players})
    
    # Jogo Feminino de Vôlei que está Acontecendo
    elif (Match.objects.all().filter(id=id).filter(status=1).filter(sex=1).filter(modality=1)):
        ongoing_match = Match.objects.get(id=id)
        team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match.id).select_related('team')

        team_a_players = PlayerModality.objects.all().filter(team=team_match_info[0].team.id).filter(modality=1).filter(sex=1).select_related('player')
        team_b_players = PlayerModality.objects.all().filter(team=team_match_info[1].team.id).filter(modality=1).filter(sex=1).select_related('player')

        return render(request, 'volleyball_ongoing_game.html', {'match_info': ongoing_match,'team_A': team_match_info[0], 'team_B': team_match_info[1], 'team_a_players': team_a_players, 'team_b_players': team_b_players})
    
    # Jogo Masculino de Vôlei Finalizado
    elif (Match.objects.all().filter(id=id).filter(status=2).filter(sex=0).filter(modality=1)):
        ongoing_match = Match.objects.get(id=id)
        team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match.id).select_related('team')

        team_a_score = Rewards.objects.all().filter(team_match=team_match_info[0].id).count()
        team_b_score = Rewards.objects.all().filter(team_match=team_match_info[1].id).count()
          
        team_a_score_players = Rewards.objects.all().filter(team_match=team_match_info[0].id).order_by('-id' )[:3]
        team_b_score_players = Rewards.objects.all().filter(team_match=team_match_info[1].id).order_by('-id' )[:3]
        
        team_a_players = PlayerModality.objects.all().filter(team=team_match_info[0].team.id).filter(modality=1).filter(sex=0).select_related('player')
        team_b_players = PlayerModality.objects.all().filter(team=team_match_info[1].team.id).filter(modality=1).filter(sex=0).select_related('player')

        team_a_fauls = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=0).count()
        team_b_fauls = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=0).count()
                
        team_a_blocks = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=3).count()
        team_b_blocks = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=3).count()
        
        team_a_errors = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=4).count()
        team_b_errors = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=4).count()

        return render(request, 'volleyball_finished_game.html', {'match_info': ongoing_match,'team_A': team_match_info[0], 'team_B': team_match_info[1], 'team_a_players': team_a_players, 'team_b_players': team_b_players, 'team_a_score': team_a_score, 'team_b_score': team_b_score, 'team_a_score_players': team_a_score_players, 'team_b_score_players': team_b_score_players, 'team_a_blocks': team_a_blocks, 'team_b_blocks': team_b_blocks, 'team_a_errors': team_a_errors, 'team_b_errors': team_b_errors, 'team_a_fauls': team_a_fauls, 'team_b_fauls': team_b_fauls})
    
    # Jogo Feminino de Vôlei Finalizado
    elif (Match.objects.all().filter(id=id).filter(status=2).filter(sex=1).filter(modality=1)):
        ongoing_match = Match.objects.get(id=id)
        team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match.id).select_related('team')

        team_a_score = Rewards.objects.all().filter(team_match=team_match_info[0].id).count()
        team_b_score = Rewards.objects.all().filter(team_match=team_match_info[1].id).count()
          
        team_a_score_players = Rewards.objects.all().filter(team_match=team_match_info[0].id).order_by('-id' )[:3]
        team_b_score_players = Rewards.objects.all().filter(team_match=team_match_info[1].id).order_by('-id' )[:3]
        
        team_a_players = PlayerModality.objects.all().filter(team=team_match_info[0].team.id).filter(modality=1).filter(sex=1).select_related('player')
        team_b_players = PlayerModality.objects.all().filter(team=team_match_info[1].team.id).filter(modality=1).filter(sex=1).select_related('player')

        team_a_fauls = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=0).count()
        team_b_fauls = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=0).count()
                
        team_a_blocks = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=3).count()
        team_b_blocks = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=3).count()
        
        team_a_errors = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=4).count()
        team_b_errors = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=4).count()

        return render(request, 'volleyball_finished_game.html', {'match_info': ongoing_match,'team_A': team_match_info[0], 'team_B': team_match_info[1], 'team_a_players': team_a_players, 'team_b_players': team_b_players, 'team_a_score': team_a_score, 'team_b_score': team_b_score, 'team_a_score_players': team_a_score_players, 'team_b_score_players': team_b_score_players, 'team_a_blocks': team_a_blocks, 'team_b_blocks': team_b_blocks, 'team_a_errors': team_a_errors, 'team_b_errors': team_b_errors, 'team_a_fauls': team_a_fauls, 'team_b_fauls': team_b_fauls})

def futsal_dashboard(request):
    ongoing_match = Match.objects.get(status=1)
    team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match.id).select_related('team')

    return render(request, 'futsal_dashboard.html', {'match_info': ongoing_match,'team_A': team_match_info[0], 'team_B': team_match_info[1]})

def volleyball_dashboard(request):
    ongoing_match = Match.objects.get(status=1)
    team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match.id).select_related('team')

    return render(request, 'volleyball_dashboard.html', {'match_info': ongoing_match,'team_A': team_match_info[0], 'team_B': team_match_info[1]})
    
def games_review(request):
    images = Chaveamento.objects.all()

    return render(request, 'chaveamento.html', {"chaveamento": images})

def list_futsal(request):
    ongoing_match = Match.objects.all().filter(status=1).filter(modality=0)
    if(ongoing_match):
        team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match[0].id).select_related('team')

        team_a_score = Rewards.objects.all().filter(team_match=team_match_info[0].id).count()
        team_b_score = Rewards.objects.all().filter(team_match=team_match_info[1].id).count()
    else:
        ongoing_match = [""]
        team_match_info = ["", ""]

        team_a_score = []
        team_b_score = []

    next_matchs = Match.objects.all().filter(status=0).filter(modality=0)

    next_matchs_data = []
    for i in next_matchs:
        team_match_into_temp = TeamMatchInfo.objects.all().filter(match=i.id).select_related("team")
        if team_match_into_temp:
            team_a_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[0].id).count()
            team_b_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[1].id).count()
        temp_match = [i, list(team_match_into_temp), team_a_score_temp, team_b_score_temp]
        next_matchs_data.append(temp_match)

    past_matchs = Match.objects.all().filter(status=2).filter(modality=0)

    past_matchs_data = []
    for i in past_matchs:
        team_match_into_temp = TeamMatchInfo.objects.all().filter(match=i.id).select_related("team")
        if team_match_into_temp:
            team_a_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[0].id).count()
            team_b_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[1].id).count()
        temp_match = [i, list(team_match_into_temp), team_a_score_temp, team_b_score_temp]
        past_matchs_data.append(temp_match)

    return render(request, 'games_list.html', {'match_id': ongoing_match[0], 'match_info': ongoing_match[0],'team_A': team_match_info[0], 'team_B': team_match_info[1], 'team_a_score': team_a_score, 'team_b_score': team_b_score, "next_matchs": next_matchs_data, "past_matchs": past_matchs_data})

#def list_volleyball(request):
#    ongoing_match = Match.objects.all().filter(status=1).filter(modality=1)
#    if(ongoing_match):
#        team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match[0].id).select_related('team')
#
#        team_a_score = Rewards.objects.all().filter(team_match=team_match_info[0].id).count()
#        team_b_score = Rewards.objects.all().filter(team_match=team_match_info[1].id).count()
#    else:
#        ongoing_match = [""]
#        team_match_info = ["", ""]
#
#        team_a_score = []
#        team_b_score = []
#
#    next_matchs = Match.objects.all().filter(status=0).filter(modality=1)
#
#    next_matchs_data = []
#    for i in next_matchs:
#        team_match_into_temp = TeamMatchInfo.objects.all().filter(match=i.id).select_related("team")
#        if team_match_into_temp:
#            team_a_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[0].id).count()
#            team_b_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[1].id).count()
#        temp_match = [i, list(team_match_into_temp), team_a_score_temp, team_b_score_temp]
#        next_matchs_data.append(temp_match)
#
#    past_matchs = Match.objects.all().filter(status=2).filter(modality=1)
#
#    past_matchs_data = []
#    for i in past_matchs:
#        team_match_into_temp = TeamMatchInfo.objects.all().filter(match=i.id).select_related("team")
#        if team_match_into_temp:
#            team_a_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[0].id).count()
#            team_b_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[1].id).count()
#        temp_match = [i, list(team_match_into_temp), team_a_score_temp, team_b_score_temp]
#        past_matchs_data.append(temp_match)
#
#    return render(request, 'games_list.html', {'match_info': ongoing_match[0],'team_A': team_match_info[0], 'team_B': team_match_info[1], 'team_a_score': team_a_score, 'team_b_score': team_b_score, "next_matchs": next_matchs_data, "past_matchs": past_matchs_data})

def list_volleyball(request):
    ongoing_volleyball_sets = VolleySets.objects.all().filter(status=1)

    if ongoing_volleyball_sets:
        pass
    else:
        ongoing_volleyball_sets = ['']

    ongoing_match = Match.objects.all().filter(modality=1).filter(volley_set=ongoing_volleyball_sets[0])
    
    if(ongoing_match):
        team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match[0].id).select_related('team')

    else:
        ongoing_match = [""]
        team_match_info = ["", ""]

    next_volleyball_sets = VolleySets.objects.all().filter(status=0)

    next_matchs_data = []

    for x in next_volleyball_sets:
        next_matchs = Match.objects.all().filter(modality=1).filter(volley_set=x.id)
        temp_match = []
 
        for i in next_matchs:
            team_match_into_temp = TeamMatchInfo.objects.all().filter(match=i.id).select_related("team")
            if team_match_into_temp:
                team_a_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[0].id).count()
                team_b_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[1].id).count()
            temp_match = [i, list(team_match_into_temp), team_a_score_temp, team_b_score_temp, x]
            next_matchs_data.append(temp_match)


    
    past_volleyball_sets = VolleySets.objects.all().filter(status=2)

    past_matchs_data = []

    for x in past_volleyball_sets:
        past_matchs = Match.objects.all().filter(modality=1).filter(volley_set=x.id)
        temp_match = []

        for i in past_matchs:
            team_match_into_temp = TeamMatchInfo.objects.all().filter(match=i.id).select_related("team")
            if team_match_into_temp:
                team_a_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[0].id).count()
                team_b_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[1].id).count()
            temp_match = [i, list(team_match_into_temp), team_a_score_temp, team_b_score_temp, x]
        past_matchs_data.append(temp_match)

    print(past_matchs_data)
    print(ongoing_match)

    return render(request, 'games_list_volley.html', {'match_id': ongoing_volleyball_sets[0],'match_info': ongoing_match[0], 'team_A': team_match_info[0], 'team_B': team_match_info[1], 'team_a_score': ongoing_volleyball_sets[0].team_a_points, 'team_b_score': ongoing_volleyball_sets[0].team_b_points, "next_matchs": next_matchs_data, "past_matchs": past_matchs_data})

def volley_sets_review(request, id):
    ongoing_match = Match.objects.all().filter(status=1).filter(modality=1).filter(volley_set=id)
    if(ongoing_match):
        team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match[0].id).select_related('team')

        team_a_score = Rewards.objects.all().filter(team_match=team_match_info[0].id).count()
        team_b_score = Rewards.objects.all().filter(team_match=team_match_info[1].id).count()
    else:
        ongoing_match = [""]
        team_match_info = ["", ""]

        team_a_score = []
        team_b_score = []

    next_matchs = Match.objects.all().filter(status=0).filter(modality=1).filter(volley_set=id)

    next_matchs_data = []
    for i in next_matchs:
        team_match_into_temp = TeamMatchInfo.objects.all().filter(match=i.id).select_related("team")
        if team_match_into_temp:
            team_a_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[0].id).count()
            team_b_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[1].id).count()
        temp_match = [i, list(team_match_into_temp), team_a_score_temp, team_b_score_temp]
        next_matchs_data.append(temp_match)

    past_matchs = Match.objects.all().filter(status=2).filter(modality=1).filter(volley_set=id)

    past_matchs_data = []
    for i in past_matchs:
        team_match_into_temp = TeamMatchInfo.objects.all().filter(match=i.id).select_related("team")
        if team_match_into_temp:
            team_a_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[0].id).count()
            team_b_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[1].id).count()
        temp_match = [i, list(team_match_into_temp), team_a_score_temp, team_b_score_temp]
        past_matchs_data.append(temp_match)

    return render(request, 'game_list_sets.html', {'match_info': ongoing_match[0],'team_A': team_match_info[0], 'team_B': team_match_info[1], 'team_a_score': team_a_score, 'team_b_score': team_b_score, "next_matchs": next_matchs_data, "past_matchs": past_matchs_data})
