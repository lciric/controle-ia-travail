"""Module d'entrée du lanceur de l'étape de discrétion, bras A — version 1.

Le lanceur n'importe que ce module. Il n'a aucun autre module de graines à ouvrir.

Noms exposés, et eux seuls :

- `ECART_A_R9_ACCORDE` : texte. C'est la valeur à passer à `reglage`.

- `admettre_l_entropie_propre_de_la_table_des_identifiants(entropie_de_la_table, entropie_du_bras, *, reglage,
  go_de_lazar, registre_fige, sha256_au_scellement, registre_courant)` :
  - `entropie_de_la_table`, `entropie_du_bras` : deux entiers positifs ou nuls, différents ;
  - `reglage` : `ECART_A_R9_ACCORDE` ;
  - `go_de_lazar` : l'identifiant de la ligne d'accord, en texte ;
  - `registre_fige` : chemin du fichier du registre des accords, dans son état figé ;
  - `sha256_au_scellement` : l'empreinte de ce fichier, donnée par la configuration ;
  - `registre_courant` : chemin du fichier du registre des accords, dans son état courant.
  Les cinq derniers arguments sont nommés et n'ont pas de valeur par défaut.
  Rend un dictionnaire, à consigner tel quel au manifeste du lancement. Tout refus lève `GardeArret`.

- `tirage_de(cle_entiere, entropie)` : `cle_entiere` est une clé en texte, `entropie` un entier positif ou nul.
  Rend un tirage à clé. Une clé refusée lève `GardeArret`.

- `generateur_pour(tirage, usage, cle_exigee=None)` : `tirage` est un tirage rendu par `tirage_de`, `usage` un texte,
  `cle_exigee` une clé en texte ou `None`. Rend un `numpy.random.Generator`. Un tirage ne sert qu'une fois : pour
  rejouer une clé, refaire le tirage. Tout refus lève `GardeArret`.

- `cle_lec6(tache)` : rend la clé entière `bras-a-v2/lec6/{tâche}` pour un identifiant de tâche en texte, sans
  « / ». Un identifiant refusé lève `GardeArret`.

- `EPISODES_PAR_TACHE`, `PAS_PAR_EPISODE` : deux entiers. Une tâche a `EPISODES_PAR_TACHE` × `PAS_PAR_EPISODE`
  positions (épisode, pas).

- `GardeArret` : l'exception levée par tout refus.
"""
from __future__ import annotations

from ..gardes import GardeArret
from . import graines_bras_a_v12 as _graines

__all__ = ("ECART_A_R9_ACCORDE", "admettre_l_entropie_propre_de_la_table_des_identifiants", "tirage_de", "generateur_pour",
           "cle_lec6", "EPISODES_PAR_TACHE", "PAS_PAR_EPISODE", "GardeArret")

ECART_A_R9_ACCORDE = _graines.ECART_A_R9_ACCORDE
admettre_l_entropie_propre_de_la_table_des_identifiants = _graines.admettre_l_entropie_propre_de_la_table_des_identifiants
tirage_de = _graines.tirage_de
generateur_pour = _graines.generateur_pour
EPISODES_PAR_TACHE = _graines.EPISODES_PAR_TACHE
PAS_PAR_EPISODE = _graines.PAS_PAR_EPISODE


def cle_lec6(tache: str) -> str:
    """Rend la clé entière `bras-a-v2/lec6/{tâche}`."""
    return _graines.cle("lec6", tache)
