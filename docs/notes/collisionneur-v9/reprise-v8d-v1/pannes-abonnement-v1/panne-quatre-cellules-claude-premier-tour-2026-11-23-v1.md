# Panne des quatre cellules Claude du premier tour (23 novembre 2026), deux dossiers du collisionneur — v1

- Écrit le 2026-11-24 vers 15:40Z (`date -u` : 15:29Z au relevé). Classe C. Session des collisionneurs (`session_016QhUrsc1rhjmmiLEmqPygF`). Une panne technique n'est pas un résultat (GO-2026-11-22-77) : faux échec, issue codée **« non évaluable »**, relance de droit sur le même accord, sans dépense d'interface (voie abonnement).

## Ce qui s'est passé (lu dans l'événement « result » de chaque session, `list_events`, sorte `result`)

| dossier | cellule | session | modèle, effort | sortie | dont réflexion | plafond de sortie | fin |
|---|---|---|---|---|---|---|---|
| conscience et émergence | E3-T1-conception-A | session_016QhUrrwW6XcMNuzt65E2RZ | claude-fable-5-2, max | 128 625 | 128 556 | 128 000 par message | 2026-11-23T14:10:55Z, erreur 429 « usage_limit_reached » |
| conscience et émergence | Opus hors dossier, premier tour | session_016QhUrtWmczSXdcAwnAJrvM | claude-opus-5-5, max | 128 991 | 128 922 | 128 000 | 14:15:06Z, 429 |
| idées intéressantes | E3-T1-conception-A | session_016QhUrs5tt1qDr6YaAtj1rW | claude-fable-5-2, max | 128 645 | 128 576 | 128 000 | 14:12:38Z, 429 |
| idées intéressantes | E3-T1-conception-B | session_016QhUrvSKXW7btNsyrSMjEh | claude-opus-5-5, max | 128 651 | 128 582 | 128 000 | 14:12:58Z, 429 |

- Dans chaque session, le premier message a dépensé tout le plafond de sortie (« output_tokens » 128 000 dans l'unique itération) **en réflexion** : il reste 69 jetons ou moins de texte, aucune réponse au texte servi. La suite automatique s'est ensuite heurtée à la limite de cinq heures de l'abonnement (« You've hit your 5-hour limit · resets 6:10pm (UTC) · out of usage credits » ; `terminal_reason` : `api_error`).
- Deux causes, toutes deux techniques : **(1) troncature par la réflexion à l'effort maximal** (4 cas sur 4), **(2) quota** (quatre sessions à l'effort maximal lancées à quatre minutes d'intervalle, environ 512 000 jetons de réflexion en vingt minutes).
- Rien n'est recueilli : `recueil_session_v6.py` refuserait une réponse vide en fin coupée, et il n'y a pas de réponse. Aucun fichier n'est versé dans `abonnement/reponses/` des deux dossiers ; les portes restent fermées (code 2) après le premier tour.
- Coût d'interface : zéro. Coût d'abonnement : environ 512 000 jetons de sortie au total ; le compteur hebdomadaire de l'abonnement est passé en alerte (`allowed_warning`, limite sur sept jours, remise à zéro le 2026-11-28 vers 04:00Z), lu le 24 novembre à 15:28Z dans `get_session` de la session des collisionneurs.

## Leçon (pour la relance et pour la suite)
- L'en-tête de la voie abonnement v6 (GO-2026-11-22-114) recommandait déjà « high » pour une cellule de collisionneur, « max » pour un texte décisif à sceller. L'effort maximal a été demandé expressément par Lazar pour ces dossiers (GO-2026-11-23-21 : « fable max en session pas api, opus 5.5 max aussi »). Dans une session de l'abonnement, le plafond de sortie par message est de 128 000 jetons, réflexion comprise, et il ne se règle pas ; à l'effort maximal, la réflexion l'a rempli quatre fois sur quatre.
- Une relance à l'effort maximal a de fortes chances de refaire la même panne. Changer l'effort est un écart à la consigne de Lazar : décision à lui.
- Lancer les sessions de l'abonnement une à une, non en parallèle.
- La fiche de chaque kit (`fiche.json`, scellée) porte « effort : max » et la voie la recopie dans la fiche de recueil. Si l'on relance à un autre effort, l'écart sera déclaré dans `sessions-abonnement-v1.md` du dossier et dans la note de sortie (effort lu dans `get_session`), sans réécrire la fiche scellée.
