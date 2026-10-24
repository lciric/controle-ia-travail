"""Table statique des espèces (les trois « lignées souveraines » de Gemini) et de leurs familles de fournisseur.

Fable et Opus sont de la même famille : leurs verdicts ne sont pas indépendants (constat 39 de l'essaim
d'inspection). Les identifiants de modèle sont ceux du collisionneur v2.5 de Lazar.
"""
ESPECES = {
    "CLAUDE_FABLE_5_1": {"modele": "claude-fable-5-1", "famille": "anthropic"},
    "CLAUDE_OPUS_5_5": {"modele": "claude-opus-5-5", "famille": "anthropic"},
    "GEMINI_ARGON": {"modele": "gemini-4-argon", "famille": "gemini"},
}


def famille_de(espece: str) -> str:
    return ESPECES[espece]["famille"]
