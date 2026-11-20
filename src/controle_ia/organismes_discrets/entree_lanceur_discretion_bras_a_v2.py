"""Module d'entrée du lanceur de l'étape de discrétion, bras A — version 2.

Le lanceur n'importe que ce module. Il n'a aucun module de graines à ouvrir, et ce module ne tire rien.

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

- `EPISODES_PAR_TACHE`, `PAS_PAR_EPISODE` : deux entiers. Une tâche a `EPISODES_PAR_TACHE` × `PAS_PAR_EPISODE`
  positions (épisode, pas).

- `GardeArret` : l'exception levée par tout refus.
"""
from ..gardes import GardeArret
from .graines_bras_a_v12 import (ECART_A_R9_ACCORDE, EPISODES_PAR_TACHE, PAS_PAR_EPISODE,
                                 admettre_l_entropie_propre_de_la_table_des_identifiants)

__all__ = ("ECART_A_R9_ACCORDE", "admettre_l_entropie_propre_de_la_table_des_identifiants", "EPISODES_PAR_TACHE",
           "PAS_PAR_EPISODE", "GardeArret")
