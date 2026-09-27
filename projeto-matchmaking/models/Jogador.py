from .Tier import Tier

class Jogador():
    def __init__(self, id_jogador: str, nick: str, tier: Tier):
        self.id_jogador = id_jogador
        self.nick = nick
        self.tier = tier
        self.vitorias = 0

    def __repr__(self):
        return f"Jogador(id='{self.id_jogador}', nome='{self.nick}', tier={self.tier.value})"