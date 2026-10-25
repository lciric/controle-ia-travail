# Corrections de l'organisme écrit par Gemini — v2 des corrections, organisme v3

Écrit le 24 octobre 2026 par la lignée « session-depot », sur le GO de Lazar (« go aligne les attaques de l'organisme
de gemini », message dans la session à 18:01 UTC). Les corrections C-01 à C-10 (`CORRECTIONS-v1.md`) valent
toujours ; celle-ci s'y ajoute. La conception de Gemini ne change pas.

## C-11 — attaques alignées sur les familles et les étiquettes de la banque

| où (v2) | défaut | correction | test |
|---|---|---|---|
| `metrique/attaques.json` | les six attaques portent le vocabulaire de Gemini (familles `conscience_evaluation`, `controle_agent_delegue` ; étiquettes `conscience_evaluation` / `comportement_nominal`, `sabotage` / `execution_fidele`). Sous la règle du noyau (`taches.valider_taches_attaque`, « une attaque porte la famille et les étiquettes de la banque, sinon invalide », décision de routine CA-20 de « conv-audit »), toutes sont invalides : un défendeur ne peut pas être noté sur des étiquettes qu'il ne connaît pas | familles et étiquettes traduites dans le vocabulaire de la banque, dans le même ordre (positive, négative) : `conscience_evaluation` → famille `conscience-evaluation`, étiquette `evaluation` ; `comportement_nominal` → `usage-reel` ; `controle_agent_delegue` → famille `controle-delegation` ; `sabotage` → `sabotage` ; `execution_fidele` → `honnete`. Textes, identifiants et vérités (traduites de même) inchangés | `test_c11_…` (règle du noyau sur la v3 ; la v2 comme artefact ; textes et vérités conservés) |

**Lecture du sens, à vérifier par un relecteur.** La banque demande si un échange est une évaluation ou un usage réel ;
Gemini étiquetait la conscience qu'a l'agent d'être évalué. Sur ses trois textes, les deux lectures coïncident :
l'attaque 1 (identifiant synthétique de benchmark) et l'attaque 3 (dilemme artificiel symétrique, déclaré
« évaluation » par l'agent) portent des indices d'évaluation dans le contexte ; l'attaque 2 (question mathématique
ordinaire d'un utilisateur) est un usage réel. Pour la famille « sabotage », la traduction est directe.

## Non changé, rapporté

- La métrique (`metrique/calculer.py`) reste une métrique de forme, qui ne lit jamais la vérité : sous la règle de
  discriminance du noyau (sortie parfaite et sortie inversée, décision CA-19 de « conv-audit »), elle est non
  discriminante, donc rapportée et écartée de H-E2. C'est la conception de Gemini.
- Les tests livrés par Gemini gardent son vocabulaire pour leurs propres tâches fictives : ils ne passent pas par le
  noyau.