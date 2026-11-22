# Relevé de fin de la passe X, groupe 1 — v1

Écrit le 2026-11-22T13:56:36Z par la session de l'organisme. Il est fait de métadonnées seules : aucun texte de réponse n'a été lu.

- **Départ** : 13:04:54Z. Garde de départ : neuf couples prêts. Essai d'effort : Opus 5.5 et Fable 5.1 à xhigh, Opus 4.6 et Sonnet 4.6 à max, Astra à xhigh.
- **Arrêt** : SIGKILL au PID 14688 à 13:55:34.775Z, posé à la barrière par la garde `arret_a_la_barriere_v1.py` (sa sortie est dans ce dossier). C'est l'ordre de la mère de 13:21Z, sur le mot de Lazar : les appels Claude par l'abonnement, non par l'API.
- **Barrière** : neuf modèles sans défaut de réglage ; elle laissait passer. Avant l'arrêt, **15 lignes « envoi » des groupes 2 et 3 ont été écrites**, dont 6 pour des modèles Claude. Leurs 15 flux de quarantaine sont **vides, 0 octet** : aucune réponse n'est revenue. Le coût de ces envois est inconnu, probablement nul ou limité à l'entrée.
- **Unités du groupe 1** :
  - rendues saines : Opus 5.5, Fable 5.1, Opus 4.6, Kimi ;
  - sans réponse, par la garde de coupure, sans titre ni ligne finale reconnus malgré une fin normale : Argon, Carbon, Neon, Sonnet 4.6. Pour Sonnet 4.6, la moitié A a passé la garde ;
  - sans réponse, coupé deux fois à 300 secondes : Astra.
- **Dépense comptée par clé** :
  - RR_ANTHROPIC_API_KEY_LUC : 5,26 USD, déclarée ;
  - GEMINI_API_KEY : 7,19 USD, déclarée ;
  - KIMI_API_KEY : 0,20 USD, déclarée ;
  - OPENAI_API_KEY_2 : 12,10 USD, au pire, réel inconnu.
  - Total compté : 24,75 USD. Total réel sûr : 12,65 USD.
- **Quarantaine** : 19 tentatives closes versées sans lecture sur `prep/quarantaine-passe-x-reponses-v1` (dernier commit `6369ccff`). Les 15 flux vides des groupes 2 et 3 restent dans l'arbre local, sans compagnon, non versés.
- **Sondes par l'abonnement** : Fable 5.1, Opus 4.6 et Sonnet 4.6 ont été servis tels que demandés, à l'effort max déclaré. Opus 5.5 n'a pas été sondé : la création de sa session a été refusée par le classifieur. Les trois sessions sont archivées.
