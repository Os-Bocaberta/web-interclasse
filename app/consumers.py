from channels.generic.websocket import JsonWebsocketConsumer
import channels.layers
from channels.layers import get_channel_layer
from django.db.models import signals
from django.dispatch import receiver
from asgiref.sync import async_to_sync

from .serializers import RewardsSerializer
from datetime import datetime, timezone
from .models import Teams, Players, PlayerModality, Match, TeamMatchInfo, Penalties, Rewards, Assistances

channel_layer = get_channel_layer()

class DashboardConsumer(JsonWebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'ongoing_game',
            self.channel_name
        )
        
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'ongoing_game',
            self.channel_name
        )
        self.close()

    def receive_json(self, content, **kwargs):
        print(f"Received event: {content}")

        if(Match.objects.all().filter(status=1).exists()):
            ongoing_match = Match.objects.get(status=1)
    
            this_moment = datetime.now(timezone.utc)
            game_time = this_moment - ongoing_match.start_time

            if(TeamMatchInfo.objects.all().filter(match=ongoing_match.id).select_related('team').count() == 2):
                team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match.id).select_related('team')
        
                team_a_score = Rewards.objects.all().filter(team_match=team_match_info[0].id).count()
                team_b_score = Rewards.objects.all().filter(team_match=team_match_info[1].id).count()
        
                team_a_score_players = Rewards.objects.all().filter(team_match=team_match_info[0].id).order_by('-id' )[:3]
                team_b_score_players = Rewards.objects.all().filter(team_match=team_match_info[1].id).order_by('-id' )[:3]
        
                team_a_serializer_score_players = RewardsSerializer(instance=team_a_score_players, many=True)
                team_b_serializer_score_players = RewardsSerializer(instance=team_b_score_players, many=True)
        
                team_a_fauls = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=0).count()
                team_b_fauls = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=0).count()
                
                team_a_reds = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=2).count()
                team_b_reds = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=2).count()
        
                team_a_yellows = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=1).count()
                team_b_yellows = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=1).count()
        
                team_a_blocks = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=3).count()
                team_b_blocks = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=3).count()
        
                team_a_errors = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=4).count()
                team_b_errors = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=4).count()
        
                layer = channels.layers.get_channel_layer()
                async_to_sync(layer.group_send)('ongoing_game', {
                    'type': 'events.alarm',
                    'data': {
                        'team_a_score': str(team_a_score),
                        'team_b_score': str(team_b_score),
                        'game_time': str(game_time),
                        'team_a_players_scores': team_a_serializer_score_players.data,
                        'team_b_players_scores': team_b_serializer_score_players.data,
                        'team_a_fauls': team_a_fauls,
                        'team_b_fauls': team_b_fauls,
                        'team_a_reds': team_a_reds,
                        'team_b_reds': team_b_reds,
                        'team_a_yellows': team_a_yellows,
                        'team_b_yellows': team_b_yellows,
                        'team_a_blocks': team_a_blocks,
                        'team_b_blocks': team_b_blocks,
                        'team_a_errors': team_a_errors,
                        'team_b_errors': team_b_errors
                    }
                })
        

    def events_alarm(self, event):
        self.send_json(event['data'])

    @staticmethod
    @receiver(signals.post_save)
    def order_offer_observer(sender, instance, **kwargs):
        if(Match.objects.all().filter(status=1).exists()):
            ongoing_match = Match.objects.get(status=1)
    
            this_moment = datetime.now(timezone.utc)
            game_time = this_moment - ongoing_match.start_time

            if(TeamMatchInfo.objects.all().filter(match=ongoing_match.id).select_related('team').count() == 2):
                team_match_info = TeamMatchInfo.objects.all().filter(match=ongoing_match.id).select_related('team')
        
                team_a_score = Rewards.objects.all().filter(team_match=team_match_info[0].id).count()
                team_b_score = Rewards.objects.all().filter(team_match=team_match_info[1].id).count()
        
                team_a_score_players = Rewards.objects.all().filter(team_match=team_match_info[0].id).order_by('-id' )[:3]
                team_b_score_players = Rewards.objects.all().filter(team_match=team_match_info[1].id).order_by('-id' )[:3]
        
                team_a_serializer_score_players = RewardsSerializer(instance=team_a_score_players, many=True)
                team_b_serializer_score_players = RewardsSerializer(instance=team_b_score_players, many=True)
        
                team_a_fauls = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=0).count()
                team_b_fauls = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=0).count()
                
                team_a_reds = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=2).count()
                team_b_reds = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=2).count()
        
                team_a_yellows = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=1).count()
                team_b_yellows = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=1).count()
        
                team_a_blocks = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=3).count()
                team_b_blocks = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=3).count()
        
                team_a_errors = Penalties.objects.all().filter(team_match=team_match_info[0].id).filter(type=4).count()
                team_b_errors = Penalties.objects.all().filter(team_match=team_match_info[1].id).filter(type=4).count()
        
                layer = channels.layers.get_channel_layer()
                async_to_sync(layer.group_send)('ongoing_game', {
                    'type': 'events.alarm',
                    'data': {
                        'team_a_score': str(team_a_score),
                        'team_b_score': str(team_b_score),
                        'game_time': str(game_time),
                        'team_a_players_scores': team_a_serializer_score_players.data,
                        'team_b_players_scores': team_b_serializer_score_players.data,
                        'team_a_fauls': team_a_fauls,
                        'team_b_fauls': team_b_fauls,
                        'team_a_reds': team_a_reds,
                        'team_b_reds': team_b_reds,
                        'team_a_yellows': team_a_yellows,
                        'team_b_yellows': team_b_yellows,
                        'team_a_blocks': team_a_blocks,
                        'team_b_blocks': team_b_blocks,
                        'team_a_errors': team_a_errors,
                        'team_b_errors': team_b_errors
                    }
                })