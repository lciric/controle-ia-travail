# Vérification du lot 11 v4 (passe X, groupes) — v1

Aucun appel hors 127.0.0.1, aucune clé lue, aucune dépense. Mes essais : `/tmp/claude-0/-home-user-controle-ia-travail/e2c3ce0b-40f3-55d3-a6bf-333c05f6ccd1/scratchpad/v4_artefacts.py` (21 essais, tous passent ; deux d'entre eux constatent des réserves, voir R1 et R2).

## Verdict : CONFORME AVEC RÉSERVES. Aucun point bloquant ; la garde ne laisse passer aucune réponse coupée dans les 14 coupures que j'ai écrites.

## Rejeu
- 74 essais passés. Mutations : 1 témoin + 56 tuées = 57 lignes (la consigne disait « 57 tuées » : c'est 56 + T0), `conforme: true`.
- Textes : le programme rejoué rend une sortie identique (`cmp`) à `sortie-former-textes-groupes-v1.json`, et les neuf textes sont identiques octet pour octet aux textes scellés. Préambule lu dans le programme : « Voici {n} questions… titre « Réponse k » (k = numéro de pièce)… 600 mots au plus… ligne seule : FIN DES RÉPONSES. »
- Configuration v3 et v4 : empreintes égales à leurs compagnons ; v4 = v3 sans « max » pour Opus 5.5 et Fable 5.1 (efforts : xhigh, high), rien d'autre (`diff`). Neuf proposeurs, Neon à xhigh (réflexion 49 152, garde v3 passée), sous-parts 90,75 + 66,55 + 24,20 + 18,15 = 199,65, tous pires de tentative ≤ 4,89 (< 6,05), couples (clé, modèle) du plan = ceux de la configuration (9).

## Garde de coupure contre les cinq contrôles de B.4
Les contrôles 1 à 4 sont tenus (raison d'arrêt, ligne finale unique et dernière, titres « Réponse k » dans l'ordre exact des rangs, au moins 240 mots par section, modèle servi par la classe) ; le 5 donne des alertes sans rejet. Mes coupures, toutes rejetées : dernière section coupée sans ligne finale ; section sautée avec ligne finale ; ligne finale au milieu puis coupure ; plan de titres en tête puis coupure ; sections vides avec ligne ; ordre inversé ; titre doublé ; fin max_tokens avec texte complet ; fin absente ; texte après la ligne finale ; 239 mots (rejetée) contre 240 (acceptée, par construction à 40 %).
Limite de principe : un texte dont chaque section a 240 mots et que le modèle clôt lui-même par la ligne finale passe ; rien ne le distingue d'un texte court voulu.

## Relance, barrière, arrêt n° 12, texte
- Relance : une seule par unité (R2 : toujours coupé → 1 + 2 moitiés par groupe, 9 appels en tout, six lignes marquées « relance », unités « sans réponse ») ; cause lue (transport, réflexion épuisée si moins de 1 440 mots, sinon texte coupé) ; cran d'effort : xhigh → high pour OpenAI (R3) ; moitiés servies avec leurs propres rangs ; la relance ne part pas si l'arrêt n° 13 est levé.
- Barrière : trois modèles en erreur de réglage sur neuf ferment, deux laissent passer (R4).
- Arrêt n° 12 avec relances : sous-parts de 13,00 et toutes les unités coupées : des tentatives sont « refusées avant envoi », chaque clé ≤ 13,00 et le total ≤ 52,00 (R5, huit fils). La réservation est à 6,05 et le cumul au coût réel : les relances s'ajoutent sans dépasser la sous-part.
- Aucun texte de réponse au journal ni au rapport (R6) : seuls causes, comptes, alertes fixes.

## Réserves
- R1. **Flux fermé proprement sans événement final** (aucune exception) : classé « réponse illisible », fin absente, unité « fermée », **aucune relance** (constaté : 3 appels, 3 unités fermées). B.4 le range en coupure de transport (même requête relancée). Sûr (jamais lu comme réponse) mais perd la réponse. Correction : dans `_juger`, classe « réponse illisible » avec fin absente → défaut, cause « transport ».
- R2. Ligne finale stricte : « FIN DES RÉPONSES. » (avec point) est rejetée, d'où une relance payante pour une réponse complète. Retirer la ponctuation finale avant la comparaison. Même remarque pour un titre non en « Réponse k » (« ### 3. »).
- R3. `défaut Google` hors MAX_TOKENS (zéro pensée, texte vide) et les erreurs sous statut 200 ne relancent pas ; la barrière ne compte que « erreur de requête » et « modèle substitué », non « défaut Google ». À dire si c'est voulu.
- R4. **Sonnet 4.6 et Kimi à 96 000 jetons de sortie** : Fable (B, de mémoire) donne 64 000 à Sonnet 4.6, et la v1 notait 24 000 pour Kimi. L'essai de réglages envoie 16 jetons et n'attrape pas ce défaut ; il apparaîtrait au groupe 1 comme « erreur de requête » (deux défauts admis par la barrière). À éprouver ou à corriger avant l'envoi.
- R5. Non tenu de B.3, non déclaré au LISEZMOI : Google à 40 960 de réflexion si le texte mesuré dépasse 12 000 ; budget de tâche et mode d'arrière-plan sont déclarés. La section C.3 n'est pas dans les lignes que j'étais autorisé à lire : concordance avec C.3 non vérifiée ; avec A et B : oui.
- R6. Un coût réel au-dessus de 6,05 en cours de tentative n'est pas coupé (réserve déjà consignée) ; pires calculés au plus 4,89.

## Script de lancement `lancer_passe_x_v4.sh`
Conforme au LISEZMOI pour ce qu'il lance : l'exécutant v4 avec `--textes` (neuf textes), la configuration v4, le plan v3, `--reel`, journal sous le dossier de lancement, quarantaine `$A/flux` dans l'arbre sous le dossier de travail de la session (hors des deux dépôts, donc acceptée par la garde R4), sortie et erreurs redirigées vers des fichiers du dossier de travail ; `-I` n'ôte pas les clés de l'environnement ; il refuse si la branche de l'arbre n'est pas `prep/quarantaine-passe-x-reponses-v1` ou si `flux` existe ; il pose le fichier d'arrêt et attend le versement, même si l'exécutant refuse. Il n'affiche ni clé ni texte, hormis la dernière ligne du fichier de versement.
**Non vérifié** : il lance en arrière-plan `verser_quarantaine_v1.py` (lot v2), qui ne figure ni dans mes fichiers ni dans le LISEZMOI v4. Ce que ce programme écrit ou envoie (dépôt, réseau) est hors de ma vérification : à faire lire avant l'envoi, car il manipule les flux bruts, c'est-à-dire des textes de réponse.
