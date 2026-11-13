# Passation — témoin de Bailey, troisième série : pilote réussi, run principal en cours — 13 novembre 2026

Session « attaquant informé » `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Ne se
réécrit pas (R12). Aucune note de sonde ni de juge lue (seuls le journal de conduite et ses états techniques).

## Fait (depuis « go (a), garde le poste », 22:10Z, et « avance en autonomie pendant 10h », ≈ 22:14Z)
- Code v17 : `execution_v4` (script public lancé par `runpy.run_path(..., run_name="__main__")`), `instance_v16`,
  `lanceur_v17` ; commit du code `8d1c541e` ; essais v17 (169 : 168 passés, 1 sauté sans les configurations publiques) ;
  épreuve hors essais sous Hydra 1.3.2 (v1, v2) : v4 imprime la configuration, v3 meurt sans rien imprimer.
- Contre-lecture du code `833429c6…` (conforme après corrections, C-1 et C-2 traités) ; addendum 4
  `prereg/temoin-attaque-publiee-bailey-v1-addendum-4-code-v17-execution-v4-troisieme-serie.md` (`89d2f647…`), contre-lu
  (`2db77cc7…`) puis contre-lu en différentiel (`cb2eb8e5…`), scellé au commit `6330000a` (23:07:10Z).
- Ordre de lancement `registres/passations/2026-11-12-2312-ordre-lancement-temoin-bailey-serie-3.md` (`220ac21e…`),
  commité à 23:07:45Z, avant la création du poste.
- Poste Hetzner v11 175902959 créé à 23:07:57Z ; offre 59431043 (Texas, A100 SXM4, c = 1,3421 USD/h) ; instance Vast
  **60417353** créée à 23:12:03Z (avant la borne de 08:14Z) ; amorce, auto-arrêt, mise en place, contrôle du juge : code 0.
- **Pilote** 23:46:15Z → 00:52:48Z : code 0, 3 tours complets, aucune garde tombée, configuration effective passée,
  ≈ 1 316 s par tour. **Règle** : K = 72, R = 10, D = 5,033 USD, H = 44,7 h, pas d'arrêt. **Run principal lancé à
  00:52:59Z** (≈ 26 h attendues, ≈ 35 USD de plus).
- Lazar prévenu par notification (lancement, lecture de la condition 7 ; pilote réussi et run principal).

## Réserves
- Condition 7 : mot de lancement = lecture de la session (« go (a) » + « autonomie 10h »), déclarée dans l'addendum 4,
  § 6 ; la contre-lecture recommandait un mot exprès. À confirmer ou infirmer par Lazar.
- Deux heures fausses dans des noms de notes scellées : `…-2320-decision-…` (commitée à 22:50:48Z) et `…-2312-ordre-…`
  (commitée à 23:07:45Z ; « GO relu à 23:10Z » y est faux : relu vers 23:07Z). Contenus justes ; ne se réécrivent pas.
- Pièces v10 (conduite, poste, constructeur) : jamais tournées, défaut de syntaxe de la conduite v10.
- Suite complète du dépôt : coupée deux fois par des redémarrages ; première partie (4 862 essais) : 37 échecs, tous
  dans d'autres chantiers (cibles invisibles, corpus arXiv, hôte durable, lanceur durable, t06, t07) ; aucun dans les
  essais du témoin ; le reste (1 825 essais) tourne (`scratchpad/pytest_v17_complet_v3_suite.txt`).
- `registres/etat.md` non mis à jour par cette session (cloison : il porte des verdicts de sondes) : à faire par la mère.
- Trois instances Vast « exited » d'un autre chantier (58936096, 58936099, 58936100) vues à l'inventaire ; non touchées.

## Reste
- Surveiller le run principal (rappels ≤ 90 min ; alerte à toute issue de la liste d'arrêt) ; à la fin : transfert,
  scellement, destruction de l'instance par la conduite, puis verdict par un lecteur neuf (R13), avant toute lecture.
- Détruire le poste v11 après `poste-fini-v11.json` ; le poste v9 175884265 reste en marche (consigne de Lazar).
- Fin du témoin : retirer la clé `ssh` Vast 1864483 ; clé de déploiement (Lazar).
- À relayer par Lazar à la mère : dépôt chez le tiers des addenda 3 et 4 ; ligne Hetzner (5 USD) ; GO du collisionneur
  (50 EUR) ; réponse de licence de Luke Bailey.

## Instances actives
Vast 60417353 (run principal) ; Hetzner 175902959 (poste v11, pilote la conduite) et 175884265 (poste v9, sans tâche,
gardé).

## Prochaine action
Rappel de surveillance (02:48Z) ; rappel de borne (08:05Z, sans objet puisque l'instance a été créée à 23:12:03Z) ;
alerte 4 h (03:47Z, sans objet : le pilote a fini).
