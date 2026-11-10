# Passation — session « attaquant informé » — refus de classifieur, arrêt sur les attaques inédites

10 novembre 2026, 08:16 UTC. Branche `claude/compassionate-meitner-d4ryyk`, dernier commit avant cette passation
`ca9287ed`. Aucun calcul, aucune dépense, aucune instance. Rien du coffre n'a été lu.

## 1. Le fait qui commande cette passation

- Vers 08:15 UTC, Lazar a donné son accord direct, dans la conversation, pour ouvrir le mandat complet du brief
  (`docs/procedures/brief-session-attaquant-informe-v1.md`, `55108eb897c6b8b7a743acb90d96cf4580ead26eac5782b530adb244b183371f`,
  branche `claude/upbeat-cray-dmauvv`) : le travail sur les attaques inédites, au-delà de la reproduction de Bailey.
- J'ai relu le brief scellé. Ma réponse suivante, la première sur ce travail, a été **arrêtée par un classifieur de
  sécurité**. Son contenu a été retenu ; je ne le reproduis pas, je ne le reformule pas, je ne le confie à aucune autre
  session ni à aucun sous-agent (brief, sections 4 et 9).
- Conséquence : **je m'arrête sur les attaques inédites.** Rien n'a été écrit sur ce travail : aucun fichier, aucun
  préenregistrement, aucun mode de sabotage, aucune recette.
- C'est le cinquième refus de classifieur lié au bras d'attaque, après les quatre que le brief cite en section 9
  (R-597, R-912, R-2045, réponse du 10 novembre dans la session-dépôt). Numéro de registre à attribuer par la session
  mère à la fusion.

## 2. Fait dans cette session (reproduction de Bailey seulement)

- Routine de reprise : empreintes des documents de lancement conformes ; `verifier-arbre` : une seule empreinte
  orpheline, connue (R-1600).
- Scellés et poussés : relevé des dépôts publics (`d804ad8e…`), devis v2 (`6a19b730…`, remplacé), brouillon 1 du
  préenregistrement (`3bcb466e…`), projet de courriel aux auteurs (`1522cb70…`, non envoyé), rapport de la
  contre-lecture 1 (`16f59a11…`).
- Poussés, **non scellés** : préenregistrement candidat `prereg/temoin-attaque-publiee-bailey-v1.md`
  (`a969dfa920a1e44044d57c9c9af5bb62fba38de968b47f1331fbad952ae0d605`), devis v3 (`335a92e0…`), erratum du relevé
  (`07bd7062…`).
- Contre-lecture 2 : la première tentative s'est perdue sans rapport ; relancée vers 08:05 UTC avec un sous-agent neuf
  (lecture seule, un rapport attendu dans
  `docs/notes/reproduction-attaque-publiee-v1/contre-lecture-2-prereg-temoin-bailey-v1.md`). Non rendue à l'heure de
  cette passation.

## 3. Reste

- Bailey : recevoir la contre-lecture 2, corriger, ajouter l'entrée « Contre-lecture 2 », sceller le préenregistrement,
  le devis v3, l'erratum et le rapport. Puis attendre les mots de Lazar sur les cinq nœuds du devis v3 (modèle ;
  licence ; prolongation et plafond de l'autorisation ; qui lance ; valeur du run pour le témoin). Rien ne tourne sans
  une ligne valide dans `registres/go.md` et son mot direct.
- Attaques inédites : **à l'arrêt**, décision à Lazar (section 5).

## 4. Réserves

- Les pièces du bras (brief, règle du jeu, note de choix, passations du 10 novembre) vivent sur
  `claude/upbeat-cray-dmauvv`, pas dans `main`.
- La note de choix de l'attaque dit que le modèle de l'article est celui du programme : c'est faux (article :
  Llama-3-8B-Instruct ; programme : Llama-3.1-8B-Instruct).
- Le code public de Bailey n'a pas de fichier de licence.
- Tests : la suite complète a été tuée au délai du conteneur, pas de total. Sur
  `tests/test_cibles_invisibles_v1.py` seul, au commit `483712e7` : 19 passés, 2 échoués.
  `test_inventaire_tout_constructeur_d_invite_est_examine` est l'échec connu (R-2042), mais il liste douze
  constructeurs d'invite non examinés au lieu d'un. `test_aucun_module_hors_mesures_ne_lit_la_cle_cibles`
  (`t06/lanceur_v5.py` et `lanceur_v6.py`, fonction `_executer_apres_manifeste`) n'est pas dans la liste des cinq échecs
  connus de R-2042. Mes commits ne touchent ni `src/` ni `tests/` ; je n'ai rien corrigé.
- Je n'ai écrit ni dans `registres/etat.md` ni dans `registres/decisions.md` : la session mère y écrit. À reporter à la
  fusion.

## 5. Décision pour Lazar

Décision : que devient le travail sur les attaques inédites après ce refus.
Enjeu : le brief interdit de contourner, de reformuler ou de transférer ; continuer dans cette session reviendrait à
reformuler.

- (a) Cette session reste sur la seule reproduction de Bailey ; les attaques inédites attendent une voie que Lazar
  choisit hors de cette session. Avantage : conforme au brief, le témoin d'ancrage avance. Inconvénient : le bras
  informé n'a pas d'auteur.
- (b) Cette session s'arrête entièrement, Bailey compris. Avantage : lecture la plus stricte de « tu le consignes et tu
  t'arrêtes ». Inconvénient : le préenregistrement reste non scellé à une contre-lecture de la fin.

Recommandation : (a), confiance 0,7. Pas de défaut à 48 heures : c'est un nœud.

## 6. Prochaine action

Recevoir la contre-lecture 2 et finir le scellement des pièces de Bailey, sauf mot contraire de Lazar. Ne rien écrire
sur les attaques inédites.

## 7. Instances actives

Aucune.
