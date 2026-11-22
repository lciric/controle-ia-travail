# Garde de départ « prêt / manque » par clé et par modèle — v1

Écrite le 2026-11-22 (`date -u` : 12:11:44Z) par la session de l'organisme, sur la consigne de la mère de 12:00Z (GO-2026-11-22-49 et -50). Lazar veut être prévenu avant toute course et toute passe.

## Ce qu'elle fait
- **Un essai par couple (clé, modèle)**, avant toute course et toute passe. L'invite est fixe et neutre (« ok ») et la sortie est d'un jeton par défaut (64 au plus).
- **Le rendu** : « prêt » ou « manque » par couple, puis par clé. Un seul « manque » sur une clé rend la clé « manque ». La mère relaie ce rendu à Lazar avant le départ.
- **Raisons, en liste fermée** :
  - prêt ;
  - clé absente ;
  - accès refusé ;
  - crédit épuisé ;
  - quota ou débit ;
  - modèle inconnu ;
  - modèle substitué ;
  - réponse illisible ;
  - injoignable ;
  - plafond ;
  - sortie hors plafond ;
  - inconnu.
- **Aucun repli silencieux** : tout ce qui n'est pas un succès complet est « manque ». Un succès complet demande trois choses : un code 200, un usage lisible, et le modèle servi égal au modèle demandé.

## Gardes
- La clé est lue **par le nom de sa variable**. Elle n'est jamais affichée ni journalisée.
- Aucun texte d'erreur du fournisseur n'est gardé, car une erreur 401 peut contenir un fragment de clé. Seuls sont gardés le code HTTP et le type ou code d'erreur.
- L'hôte est fixé par fournisseur dans le code (Anthropic, OpenAI, Google, Kimi). Il n'est jamais lu du plan.
- **Pire par appel** : 32 jetons d'entrée et la sortie maximale, au tarif du plan. Au-delà de 0,02 USD, le couple est « manque (plafond) » et rien ne part.
- **Envoi réel** : il exige `--reel` et `--go GO-AAAA-MM-JJ-NN`, et ce GO doit être une ligne du registre des GO. Sans l'un ou l'autre, le refus porte le code 2 et rien ne part.
  - Sans `--reel`, la garde fait un contrôle à blanc : elle affiche le pire de chaque couple, sans envoi.
- Le journal JSONL n'est jamais écrasé.

## Épreuve (R5)
`test_garde_depart_cles_v1.py`, sur faux transport : **31 essais passés** (`test-garde-depart-cles-v1-pytest.txt`).
- **Cas sains** : un par fournisseur, chacun rendu « prêt ».
- **Artefacts**, chacun rendu « manque » avec sa raison :
  - crédit trop bas chez Anthropic ;
  - quota épuisé chez OpenAI et chez Kimi ;
  - code 402 ;
  - codes 401 et 403 ;
  - modèle introuvable (code 404, ou `model_not_found`) ;
  - débit limité (code 429) ;
  - codes 500 et 529 ;
  - corps non JSON ;
  - usage manquant ;
  - modèle substitué, ou modèle servi absent ;
  - sortie au-delà du plafond ;
  - clé absente ou vide, sans envoi ;
  - réseau coupé ;
  - plafond dépassé, sans envoi ;
  - un manque qui suffit à rendre la clé « manque » ;
  - journal déjà présent ;
  - plan mal formé ;
  - envoi réel sans GO, ou avec un GO mal formé ou absent du registre.
- Chaque artefact vérifie aussi qu'aucun fragment de clé ni texte d'erreur n'entre dans le rendu.

## Plan (forme)
Un fichier JSON, liste de couples :
`{"cle_var": "RR_ANTHROPIC_API_KEY_LUC", "fournisseur": "anthropic", "modele": "…", "tarif_entree_usd_par_million": 5, "tarif_sortie_usd_par_million": 25, "sortie_max": 1}`.
Les modèles et les tarifs se prennent au devis de la course ou de la passe, couple par couple. **Coût attendu** : moins de 0,001 USD par couple chez Anthropic.

## Limites, à dire à Lazar
1. **« Prêt » ne prouve pas que la recharge automatique est active.** La garde prouve seulement que la clé répond et qu'elle a du crédit à cet instant. L'arrêt n° 11 garde son relevé daté de la recharge (additif 2, § 3).
2. **Google** : l'essai sort de la garde `garde_google_v3`, qui impose au moins 16 000 jetons de texte aux requêtes de la course. Ce n'est pas une requête de la course. C'est un écart à déclarer, **point pour la mère**. Autre option : l'essai Google passe seulement `countTokens`, qui est gratuit et vérifie l'accès, mais pas le crédit.
3. **Le motif « crédit épuisé »** est reconnu par des mots du fournisseur (liste dans le code). Un libellé neuf tomberait sous « inconnu », c'est-à-dire « manque » quand même.
4. **Envoi réel** : c'est une dépense, à faire sous une ligne de GO. Il se fait clé par clé, au jour du départ. Les noms des variables Google, OpenAI et Kimi de la course sont à donner par la mère.
