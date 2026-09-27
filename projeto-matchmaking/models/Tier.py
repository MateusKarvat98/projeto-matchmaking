from enum import Enum

class Tier(Enum):
    unranked = "Sem rank"
    ferro = "Ferro"
    prata = "Prata"
    ouro = "Ouro"
    platina = "Platina"
    esmeralda = "Esmeralda"
    diamante = "Diamante"
    mestre = "Mestre"
    grao_mestre = "Grão-Mestre"
    desafiador = "Desafiador"

    def proximo(self):
        membros = list(Tier)
        indice_atual = membros.index(self)

        if indice_atual < len(membros) - 1:
            return membros[indice_atual + 1]
        
        return self

    def anterior(self):
            membros = list(Tier)
            indice_atual = membros.index(self)
    
            if indice_atual > 0:
                return membros[indice_atual - 1]
            
            return self