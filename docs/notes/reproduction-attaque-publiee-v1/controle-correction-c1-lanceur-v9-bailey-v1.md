# Contrôle de la correction C-1 (lanceur v8 → v9) — témoin Bailey — v1

- Lecteur : R2, sous-agent neuf. Je n'ai écrit ni le rapport source, ni le code, ni les essais, ni la liste des
  lectures. Date : `date -u` = Tue Nov 10 17:35:07 UTC 2026 (fin des sondes).
- Je reçois d'office le `CLAUDE.md` du dépôt (`b4cbc66a422a6246df0479fe0c886eccb92cd3410d6a8b742eddea5325098eae`).
- Dépôt : `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, commit `ed79b48d`, arbre
  propre avant ce rapport.
- Pièces lues et empreintes (SHA-256, sur disque) :
  - rapport source : `relecture-lignes-touchees-code-condition6-v8-bailey-v1.md` (`baa35511f48b881fa35e8a90db2cf707780027cefc1d92d62e7fddd5d781b4a6`), en entier ;
  - code, par `diff -u` : `src/controle_ia/temoin_bailey/lanceur_v8.py` (`5d85ca45387a33f5e3e85c9ff6ccfb3a35f9402d1cbba3eea165fc44537819b3`)
    → `lanceur_v9.py` (`324dee5aaee624a83af681613f12bcc70d423407683aa9c363eef2c2855456f3`) ; contexte v9 : en-tête
    d'imports, `INSTANCE_MODULE`, `CHEMINS_ARCHIVE`, `_tours_relus`, `_executer`, `conduire` (l. 1150-1240),
    `normaliser_execution` ;
  - essais, par `diff -u` : `tests/test_temoin_bailey_condition6_v8.py` (`c86091610ca2ac104a17f08adebcc05b14b7998c931dcb617ea87eeb3e243a4b`)
    → `…_v9.py` (`43736f05daf8df20d5d59018d52593acc700bec075968dea6ba5c9f3211f58cb`) ; aides du v9 :
    `FournisseurLocal`, `scenario`, `conduite_locale`, `_scenario_pilote_mort_coupe`, essais A-2 de bout en bout ;
  - lectures, par `diff` : `lectures-addendum-condition6-v5.md` (`5e423b504260ebf6125a6b734817b6363edd20502581b2128d74a7c0e0594502`)
    → `lectures-addendum-condition6-v6.md` (`2b0923e3271748d41a1989b4a64ff1c5e90d28fb78f253fc70a4b324217cdd4d`,
    compagnon `.sha256` conforme) ; v6 : en-tête (l. 1-36), lectures 17, 26, 31, 36, conclusion (l. 76-85).
- Non lu : tout le reste du dépôt ; aucun des répertoires ou lignes cloisonnés ; aucun journal, aucune note, aucun
  résultat ; aucune clé ; aucune requête réseau ; pas de `vastai`. Aucun refus de classifieur.
- Outils : `diff -u`, `grep`, `sed`, `awk`, `sha256sum` ; `pytest` (venv du dépôt) avec `TEMOIN_BAILEY_CLONE` du clone
  obfusqué. Copie hors dépôt : `/tmp/claude-0/-home-user-controle-ia-travail/157246e4-0739-5bb4-9302-ec187f3c5161/scratchpad/ctrl-c1/depot/`
  (`src/`, `tests/`, `versions-figees-temoin-bailey-v1.json`, `e21bccf6…`), essais v9 réimportant `lanceur_v8`.
  Sondes : `…/scratchpad/ctrl-c1/sondes/test_sonde_c1_reprise.py`
  (`f905451d3dbe4f6a5c3d85dbf6a4aa52eb287b84ff0967b91ac08171e7327488`). Aucune modification du dépôt hors de ce rapport.

## 1. Verdict

**Code et essais conformes ; la liste des lectures v6 demande trois corrections de texte (L-1 à L-3), puis conforme :
l'addendum de la condition 6 peut être écrit.** C-1 est reprise mot pour mot, au bon endroit ; elle couvre aussi la
reprise du pilote. La v6 a corrigé (f), mais pas la conclusion que C-1 nommait, ni l'en-tête « Code », ni le renvoi de
la lecture 26.

## 2. Lanceur v8 → v9

- `diff -u` : trois blocs seulement. (1) Docstring : « v8 » → « v9 », plus un paragraphe C-1 ; (2) commande du
  veilleur : `controle_ia.temoin_bailey.lanceur_v9` ; (3) bloc C-1, dans `conduire`, boucle du pilote, juste après
  `pilotes.append(r)`, **identique caractère pour caractère** au texte du rapport (§ 3 (2)), indentation comprise.
- Aucun autre `lanceur_v8` dans le code exécuté : la seule occurrence hors `lanceur_v8.py` et des essais v1 à v8 est la
  docstring de `lecture_v8` (l. 15, « la conduite (`lanceur_v8`) s'arrête de même ») : texte, sans effet ; à porter à la
  prochaine version de `lecture`, avec P-1.
- `INSTANCE_MODULE = "controle_ia.temoin_bailey.instance_v8"` et `CHEMINS_ARCHIVE` (`lecture_v8.py`, `instance_v8.py`,
  modules v3 communs) inchangés : justes, l'instance et la lecture ne changent pas, et le lanceur n'est pas envoyé.
- Portée du test `r.get("tours_complets") is None` : la valeur `None` n'est posée que par `_executer`, exécution morte
  **et** `_tours_relus` en échec ; `normaliser_execution` rend toujours un entier ailleurs (0 par défaut). Le test ne
  peut donc arrêter que le cas visé.

## 3. Essais v8 → v9

- `diff -u` : import `lanceur_v9 as la` ; essai du veilleur et essai « aucun module v5-v7 » portés sur `lanceur_v9.py` ;
  `test_C1_pilote_mort_tours_en_echec_arret_sans_reprise` ajouté. Rien d'autre.
- L'essai C-1 éprouve bien l'arrêt sans reprise : scénario de bout en bout de A-2 (pilote mort pendant l'écriture d'une
  ligne de garde, préfixe sans nom), première reconstitution du pilote forcée en échec ; affirme : ni `pilote-reprise` ni
  `principal` lancés, libellé C-1, instance détruite. La seconde tentative de `_finir` passe par le vrai `_tours_relus`.
- Résultats : v9 dans le dépôt, **55 passés** (68 s). Copie réimportant `lanceur_v8` : **54 passés, 1 échoué**, l'essai
  C-1 seul (`f.lance` = `[…, 'pilote', 'pilote-reprise', …]` : la reprise est lancée). S1 est donc inversée.
- Sonde (point du rapport non affirmé par l'essai) : dans le cas de l'essai, `valider` rend
  `ETAT_LIGNE_COUPEE_PILOTE` (« Pas de run principal ; ligne de garde coupée au pilote (garde inconnue) ; … ; nœud. »),
  aucun appel `regle` (`test_sonde_C1_valider_apres_arret`, passe). Ajouter ces deux affirmations à l'essai à la
  prochaine version serait mieux ; non bloquant.
- Remarques, sans effet : le remplacement automatique a changé `"lanceur_v8.py"` en `"lanceur_v9.py"` dans la liste
  d'exclusion de l'essai `CHEMINS_ARCHIVE` (toujours vraie, le lanceur n'est pas envoyé) et fait dire à la docstring
  « essais de la v7 rejoués sur `lanceur_v9` » (c'était `lanceur_v8`).

## 4. C-1 et la reprise du pilote (question 4)

- **Oui, C-1 s'applique à la reprise** : le bloc est dans la boucle `for phase in ("pilote", "pilote-reprise")`, avant
  `issue_pilote`. Sonde `test_sonde_reprise_morte_tours_en_echec` (pilote mort, état reconstitué, issue « chute » ;
  reprise morte, première reconstitution de la reprise en échec) : v9 → arrêt au libellé C-1, une seule reprise, aucun
  `regle`, aucun `principal`, instance détruite (passe).
- Sur la v8, le même cas finissait déjà en arrêt (« seconde chute du pilote : pas de run principal ») : à la reprise,
  C-1 ne change que le libellé du bilan, pas l'issue. Pas de défaut.
- `valider` rend alors « Pas de run principal, pas de verdict (seconde chute du pilote) ; nœud. » (sonde) : c'est le
  cas P-2, ici exact par hasard (il y a eu deux chutes) ; rien à ajouter.

## 5. Lectures v5 → v6

- `diff` : deux blocs seulement, la bannière v6 (l. 3) et la ligne de la lecture 36 ; rien d'autre changé.
- (f), fidèle à C-1 : « Point déclaré » remplacé par « v9 (C-1, rapport `baa35511…`) : un pilote mort dont l'état des
  gardes est illisible … arrête tout — ni reprise, ni règle, ni run principal ; nœud », libellé du bilan exact, coût
  déclaré (reprise perdue sans ligne coupée) ; « au pilote, aucun » complété (« et, depuis la v9, tout pilote mort à
  l'état des gardes illisible ») : désormais vrai. « Aucune lecture du pilote n'ouvre la reprise sur une ligne de garde
  coupée » : vrai (essai C-1, sonde).
- P-1, P-2, P-3 écrits, fidèles au rapport (P-2 au conditionnel « peut afficher » : juste, la sonde § 3 montre qu'avec
  la ligne coupée transférée le libellé est exact).
- **Écarts (omissions)** :
  - **L-1** : la conclusion (l. 85) garde « Point déclaré : 36 (pilote mort dont l'état n'a pu être reconstitué : nœud
    rendu à la lecture). » Le rapport (§ 5, C-1) demandait de la corriger « de même ». Elle contredit (f) v6.
  - **L-2** : l'en-tête « Code : » (l. 25-29) nomme encore `lanceur_v8.py` (`5d85ca45…`) et les essais v8
    (`c8609161…`) ; « Rapport appliqué depuis la v4 » ne nomme pas `baa35511…`. La bannière dit « code courant :
    `lanceur_v9` » : l'en-tête doit porter les empreintes du code lu (R6).
  - **L-3** : lecture 26 (actée « telles qu'écrites » à 16:57) : « tours illisibles → pas de relance, nœud ; au
    pilote : chute, une reprise, **sauf** si la ligne `ETAT` porte une ligne de garde coupée ». Lue seule, elle dit
    qu'un pilote mort aux tours illisibles est repris, ce que la v9 exclut. Un renvoi suffit (pas une lecture nouvelle :
    C-1 applique le même mot de 16:57).

## 6. Corrections exactes

Dans une v7 de la liste (`lectures-addendum-condition6-v7.md`, la v6 étant scellée, R12), rien d'autre changé :

- **L-1**, conclusion : remplacer « Point déclaré : 36 (pilote mort dont l'état n'a pu être reconstitué : nœud rendu à
  la lecture). » par « Arrêt déclaré : 36 (f), v9 (C-1) : pilote mort dont l'état des gardes est illisible : ni reprise,
  ni règle, ni run principal ; nœud. Précisions déclarées : P-1 à P-3 (lecture 36 (f)). »
- **L-2**, en-tête : « Code : `src/controle_ia/temoin_bailey/lanceur_v9.py`
  (`324dee5aaee624a83af681613f12bcc70d423407683aa9c363eef2c2855456f3`), `instance_v8.py` (…), `lecture_v8.py` (…) ;
  essais `tests/test_temoin_bailey_condition6_v9.py`
  (`43736f05daf8df20d5d59018d52593acc700bec075968dea6ba5c9f3211f58cb`) » ; et ajouter à « Rapport appliqué » :
  `relecture-lignes-touchees-code-condition6-v8-bailey-v1.md` (`baa35511f48b881fa35e8a90db2cf707780027cefc1d92d62e7fddd5d781b4a6`), C-1 (lecture 36 (f)).
- **L-3**, lecture 26, après « tours illisibles → pas de relance, nœud » : insérer « (au pilote comme à sa reprise, v9,
  C-1 : arrêt, pas de reprise, pas de run principal ; nœud ; lecture 36 (f)) ».

Après L-1 à L-3, sans nouvelle relecture du code : **conforme : l'addendum de la condition 6 peut être écrit.**
Hors lignes bloquantes, à la prochaine version du code : docstring de `lecture_v8` (`lanceur_v8` → lanceur courant,
P-1) ; essai C-1 complété par `valider` → `ETAT_LIGNE_COUPEE_PILOTE` et l'absence de `regle`.
