"""Conditions de monde (v1), fixées avant toute comparaison de méthodes. Chaque condition modifie BASE
(monde_v1.py) ; les contrôles partent du monde « bien observé » pour ne changer qu'une chose à la fois."""

CONDITIONS = {
    # mondes de décision et monde mal observé
    "M_bien": {"niveau": "bien"},
    "M_moyen": {"niveau": "moyen"},
    "M_mal": {"niveau": "mal"},
    # contrôle : aucun pont planté (vérité vide), précision mesurée contre un placebo tiré au hasard parmi les paires valides
    "SP_sans_pont": {"niveau": "bien", "sans_pont": True},
    # contrôles : hypothèse de la forme corrigée violée
    "V_domaines_mal_separes": {"niveau": "bien", "p_mot_global": 0.6, "p_mot_champ": 0.25},
    "V_etiquettes_absentes": {"niveau": "bien", "etiquettes_absentes": True},
    "V_moyeux_dominants": {"niveau": "bien", "n_moyeux": 2, "p_moyeu": 0.6},
    # contrôle : vérité inversée (les ponts relient des domaines proches ; groupes d'opérateurs transversaux = miroir)
    "INV_verite_inversee": {"niveau": "bien", "verite": "proches", "groupes": "transversal"},
}

# Sensibilité préenregistrée (descriptive, hors décision) : prévalence des moyeux dans le monde moyen
SENSIBILITE = {
    "S_moyen_moyeux_010": {"niveau": "moyen", "p_moyeu": 0.10},
    "S_moyen_moyeux_050": {"niveau": "moyen", "p_moyeu": 0.50},
}

IDENTIFIANTS = {nom: i + 1 for i, nom in enumerate(list(CONDITIONS) + list(SENSIBILITE))}

GRAINE_BASE_PRINCIPALE = 20261026_000000
GRAINE_BASE_VALIDATION = 19991231_000000


def graine_monde(base, condition, indice):
    """Graine random.Random d'un monde : base + 100 000 x identifiant de condition + indice du monde."""
    return base + 100_000 * IDENTIFIANTS[condition] + indice
