from django.db import models

# Create your models here.

class Modality(models.IntegerChoices):
    futsal = 0, "Futsal"
    volleyball = 1, "Volleyball"
    dodgeball = 2, "Queimado"

    __empty__ = ("Vazio")

class Activity(models.IntegerChoices):
    holder = 0, "Titular"
    reserve = 1, "Reserva"

    __empty__ = ("Vazio")

class Sex(models.IntegerChoices):
    masc = 0, "Masculino"
    fem = 1, "Feminino"

    __empty__ = ("Vazio")

class Status(models.IntegerChoices):
    soon = 0, "Em Breve"
    ongoing = 1, "Acontecendo"
    finished = 2, "Finalizado"

    __empty__ = ("Vazio")

class PenaltyTypes(models.IntegerChoices):
    faul = 0, "Falta"
    yellow = 1, "Cartão Amarelo"
    red = 2, "Cartão Vermelho"
    block = 3, "Bloqueio"
    error = 4, "Erro"

    __empty__ = ("Vazio")

class RewardTypes(models.IntegerChoices):
    goal = 0, "Gol"
    point = 1, "Ponto"
    ace = 2, "Ace"

    __empty__ = ("Vazio")

class Teams(models.Model):
    logo = models.ImageField(upload_to='teams/', default='defaults/team.png')
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Players(models.Model):
    photo = models.ImageField(upload_to='players/', default='defaults/player.png')
    name = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class PlayerModality(models.Model):
    modality = models.IntegerField(choices=Modality.choices, blank=True, null=True)
    activity = models.IntegerField(choices=Activity.choices, blank=True, null=True)
    sex = models.IntegerField(choices=Sex.choices, blank=True, null=True)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    player = models.ForeignKey(Players, on_delete=models.CASCADE)

    def __str__(self):
        return self.player.name
    
class Match(models.Model):
    modality = models.IntegerField(choices=Modality.choices)
    status = models.IntegerField(choices=Status.choices)
    start_time = models.DateTimeField(editable=True)
    mvp_player = models.ForeignKey(Players, on_delete=models.CASCADE, blank=True, null=True)
    sex = models.IntegerField(choices=Sex.choices, blank=True, null=True)
    winner = models.ForeignKey(Teams, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.winner != None:
            return f"{Modality(self.modality).label} | Jogo N°{self.id} | Vencedor {self.winner}"
        else:
            return f"{Modality(self.modality).label} | Jogo N°{self.id}"

class TeamMatchInfo(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    def __str__(self):
        return f"Time {self.team} | {self.match}"

class Penalties(models.Model):
    type = models.IntegerField(choices=PenaltyTypes.choices)
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    team_match = models.ForeignKey(TeamMatchInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player.name} | {PenaltyTypes(self.type).label} N°{self.id} | {self.team_match}"
    
class Rewards(models.Model):
    type = models.IntegerField(choices=RewardTypes.choices)
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    team_match = models.ForeignKey(TeamMatchInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player.name} | {RewardTypes(self.type).label} N°{self.id} | {self.team_match}"
    
class Assistances(models.Model):
    assist_to = models.ForeignKey(Rewards, on_delete=models.CASCADE)
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    team_match = models.ForeignKey(TeamMatchInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.player.name
    
class Chaveamento(models.Model):
    title = models.CharField(max_length=200, default='untitled')
    image = models.ImageField(upload_to='chaveamento/', blank=True, null=True)

    def __str__(self):
        return self.title