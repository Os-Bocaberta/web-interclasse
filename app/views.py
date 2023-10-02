from django.shortcuts import render
from .models import Teams, Players, PlayerModality, Match, TeamMatchInfo, Penalties, Rewards, Assistances

# Create your views here.

def index(request):
    pass

def game(request, id):
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

    return render(request, 'games_list.html', {'match_info': ongoing_match[0],'team_A': team_match_info[0], 'team_B': team_match_info[1], 'team_a_score': team_a_score, 'team_b_score': team_b_score, "next_matchs": next_matchs_data, "past_matchs": past_matchs_data})

def list_volleyball(request):
    ongoing_match = Match.objects.all().filter(status=1).filter(modality=1)
    if(ongoing_match):
        team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match[0].id).select_related('team')

        team_a_score = Rewards.objects.all().filter(team_match=team_match_info[0].id).count()
        team_b_score = Rewards.objects.all().filter(team_match=team_match_info[1].id).count()
    else:
        ongoing_match = [""]
        team_match_info = ["", ""]

        team_a_score = []
        team_b_score = []

    next_matchs = Match.objects.all().filter(status=0).filter(modality=1)

    next_matchs_data = []
    for i in next_matchs:
        team_match_into_temp = TeamMatchInfo.objects.all().filter(match=i.id).select_related("team")
        if team_match_into_temp:
            team_a_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[0].id).count()
            team_b_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[1].id).count()
        temp_match = [i, list(team_match_into_temp), team_a_score_temp, team_b_score_temp]
        next_matchs_data.append(temp_match)

    past_matchs = Match.objects.all().filter(status=2).filter(modality=1)

    past_matchs_data = []
    for i in past_matchs:
        team_match_into_temp = TeamMatchInfo.objects.all().filter(match=i.id).select_related("team")
        if team_match_into_temp:
            team_a_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[0].id).count()
            team_b_score_temp = Rewards.objects.all().filter(team_match=team_match_into_temp[1].id).count()
        temp_match = [i, list(team_match_into_temp), team_a_score_temp, team_b_score_temp]
        past_matchs_data.append(temp_match)

    return render(request, 'games_list.html', {'match_info': ongoing_match[0],'team_A': team_match_info[0], 'team_B': team_match_info[1], 'team_a_score': team_a_score, 'team_b_score': team_b_score, "next_matchs": next_matchs_data, "past_matchs": past_matchs_data})
