# Contre-lecture courte (R2 n° 3) — A1-v3, seconde course : préenregistrement v2, brouillon 1

3 novembre 2026, de 08:56 à 09:26 UTC (heures relevées par `date -u`), interrompue par un redémarrage du serveur vers 09:10 UTC
et reprise à 09:11 UTC (sorties déjà écrites retrouvées sur disque, pièces d'entrée de nouveau empreintées et égales ; rien refait).
Contre-lecteur neuf : il n'a écrit ni la v1, ni ses brouillons, ni ce brouillon, ni le code v3 ou v3.1, ni les contre-lectures
n° 1 et 2, ni l'audit A9. Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/a1-v3-v2-contre-lecture-courte-prompt.md`
(dépôt privé, `b4082a702dea375729d1e7a1a9bb684ac494cc09fa50ec3c053370a309d60008`, compagnon égal).

Règles tenues : aucun commit ; aucun fichier `.sha256` dans un dépôt (les seuls compagnons écrits l'ont été dans un dossier
temporaire hors de tout dépôt, `/tmp/cl-arbre-9776ed0-…`, puis retirés) ; aucun fichier existant modifié ; rien sous `donnees/` ;
aucun `git fetch`, `checkout`, `stash` ; commandes git en lecture seule (`show`, `log`, `rev-parse`, `archive`, `merge-base`),
toutes avec `-c gc.auto=0 -c maintenance.auto=false` (aucun tassement déclenché) ; aucun réseau, aucun modèle, jamais
`--moteur reel` ; calculs par `nice -n 10 python3 -I -B`.

**Pièces lues, empreintes recalculées** : brouillon `orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v2-brouillon1.md`
(`c76ac6bc9e1f94a05962bac3f0d4667f0705d2f2e07db7853923e43160370d29`, 1 856 lignes) ; différence
`…/diff-attaque-goodhart-v3-v1-vers-v2-brouillon1.txt` (`9dd6d2ffd6c789cb13e67b309ad4ce05a9a395ee9e19bc094241140ff551160e`) ;
rapport du rédacteur `…/rapport-redaction-attaque-goodhart-v3-v2-brouillon1.md` (`ec4e797f6a8b2a2c767da6662a09d807b8ae61b0f8702fa6598d6e404bb45192`),
ses scripts et sorties (`/home/claude/scratch/a1-v3-seconde-redacteur/`, empreintes égales à celles de son rapport) ; v1 scellée
(`898d5be414f1472dc5beb9c9e8d377698c6b1744e9b95bd188de5a157426a23e`, compagnon égal) ; audit A9
(`ed078aaa77e69a29a04bc2bbf198e5cac9906766677291b09154c22882d83e55`, compagnon égal, égal au fichier du commit `c8c34784` de
`canal/conv-audit-n04`) ; ligne GO-2026-11-03-01 du registre privé, lue en entier (ligne 79, registre `8223230c…`, 81 lignes) et
ligne GO-2026-11-02-21 (ligne 67) ; code au commit `9776ed0` (lanceur `87d52ace…`, cœur `cb9cffe7…`, cœur v2 `3c9de8b8…`,
lanceur v2 `58609e0c…`, `pole/outils.py` `966d9553…`, `pole/configuration_v55.py` `2e6237c0…`, `pole/configuration_v53.py`
`ef72ffbf…`, chacun égal à l'objet du commit). Lus en plus pour vérifier : R-1337, R-1340 et R-1341 (`registres/decisions.md`) ;
canal n° 407 ; la consigne du rédacteur (`a1-v3-seconde-course-redacteur-prompt.md`, `673a29e9…`) ; le message n° 305 de
session-depot (`/tmp/sd-n305.md`, `18d97508…`) ; la contre-lecture n° 2 et ses couples (`e5731746…`, `9662e573…`, égaux aux
empreintes que cite la section 14).

## 1. Verdict

**Scellable après couples.** Aucun bloquant ; **3 importants** — I-1 : la décision du directeur sur la source du registre
(R-1340) n'est pas dans le texte, qui laisse encore le choix ouvert ; I-2 : hôte gardé vivant, le délai de 2 h de l'attente n'est
pas la période et l'activité de la session n'est pas tracée ; I-3 : la relance de la v1 est déjà interdite par la v1, mais le texte
ne le dit pas et ne dit pas qui tient la règle — ; **4 mineurs avec couples** (M-1 à M-4) ; **6 mineurs sans couple** (M-5 à M-10).

**16 couples** (`couples-contre-lecture-attaque-goodhart-v3-v2-brouillon1.json`), chaque « ancien » présent exactement une fois
dans le brouillon et au moment de son application. Texte obtenu (`travail/brouillon1-avec-couples-cl.md`, `b28ed1de…`,
1 896 lignes) : bloc `empreintes-du-code` égal à la v1, bloc `plan-gele` égal au brouillon, aucun marqueur, `lire_plan` ne diffère
de la v1 que par `go` ; lu par le lanceur du commit `9776ed0` : refusé sans compagnon, accepté avec un vrai compagnon écrit dans le
dossier temporaire (73 empreintes vérifiées, entropie = entier de l'empreinte, ≥ 2⁶⁴) ; GO-2026-11-03-01 accepté sur le registre
de la tête de `canal/conv-audit-n04` (ligne 79, 400 USD).

## 2. Le delta, et rien d'autre (point 1 de la consigne)

- **Reconstruction** : la v1 plus la différence, par `patch`, donne le brouillon octet pour octet (`c76ac6bc…`) ; la différence que
  j'ai recalculée (`diff -u`) a le même corps que celle du rédacteur (en-têtes de dates mis à part) ; 19 blocs, 64 lignes retirées,
  401 ajoutées ; 1 519 → 1 856 lignes.
- **Les 36 changements, un par un** (lignes du brouillon ; bloc du diff) — tous présents, tous conformes à leur ligne de la
  section 0.6, et chacun des 19 blocs appartient à un changement listé :

| n° | lieu | ligne(s) | bloc |
|---|---|---|---|
| 1 | titre | 1 | 1 |
| 2 | paragraphe de tête (celui de la v1 recopié en 0.5) | 3-27 | 1 |
| 3 | fait (iii) | 84-91 | 2 |
| 4 | section 0.4, premier paragraphe | 300-302 | 3 |
| 5 | section 0.4 (e) | 345-347 | 4 |
| 6 | section 0.4 (h) | 355-356 | 5 |
| 7 | section 0.5 | 358-457 | 5 |
| 8 | section 0.6 | 459-529 | 5 |
| 9 | section 4, « Graines » | 778-790 | 6 |
| 10 | section 4, « Un scellement, une course » | 791-792 | 6 |
| 11 | section 4, « GO » | 852-873 | 7 |
| 12 | section 4, registre des GO (chemin, règle (1), point (1 bis)) | 874-896 | 7 |
| 13 | section 4, dossier de sortie | 905-909 | 8 |
| 14 | section 4, commande exacte | 912-922 | 8 |
| 15 | bloc `plan-gele`, ligne `go:` | 958 | 9 |
| 16 | notes du bloc | 983-988 | 10 |
| 17 | section 8, « Seconde course (v2) » | 1350-1373 | 11 |
| 18 | section 9, L17 et phrase finale | 1395-1400 | 12 |
| 19 | section 11 | 1435-1436 | 13 |
| 20 | section 12 | 1542-1545 | 14 |
| 21 | section 13, point 2 | 1598-1602 | 15 |
| 22 | section 13, point 3 | 1603 | 15 |
| 23 | section 13, point 4 | 1605-1608 | 15 |
| 24 | section 13, points 7 bis et 7 ter | 1646-1661 | 16 |
| 25 | section 13, point 9 | 1667-1668 | 16 |
| 26 | section 14 (titre, n° 2 rendue, n° 3 à faire) | 1670-1680, 1724-1757 | 16, 17 |
| 27 | annexe B | 1777-1786 | 18 |
| 28 | empreintes des fichiers du rédacteur de la v2 | 1806-1815 | 19 |
| 29 | période nettement inférieure à 5 min | 1355, 1649-1650 | 11, 16 |
| 30 | observation hors du conteneur | 1357-1359, 1651-1652 | 11, 16 |
| 31 | fin brutale acceptée | 1359-1365, 432 | 11, 5 |
| 32 | sortie neuve, renvoi à l'audit | 905-909 | 8 |
| 33 | 4,245753 USD non imputés | 423-428, 1542-1544 | 5, 14 |
| 34 | identifiant de processus du guetteur | 1653-1654 | 16 |
| 35 | hôte nommé | 377-379, 912, 1647-1648 | 5, 8, 16 |
| 36 | registre, point (1 bis), copie de la première course | 891-893 | 7 |

- **Inchangé** : aucun bloc ne touche les sections 1 (question), 2 (hypothèses), 3 (prédictions), 5 (métriques), 6 (critères
  gelés), 7 (audits) ni 10 (portée) ; en section 8, la table des gardes et le paragraphe de la règle (v1, l. 1105-1118) sont
  intacts — un paragraphe est ajouté après eux (changement 17), règles de conduite sans garde d'arrêt neuve, ce qu'il dit
  lui-même (« seuls arrêts admis, ceux de la règle des guetteurs » : c'est bien la liste de la ligne du guetteur, v1 l. 1047) ;
  bloc `empreintes-du-code` identique à la v1 (73 lignes = `FICHIERS_GELES` = objets du commit `9776ed0` = tête `eaa74ca`,
  0 écart) ; bloc `plan-gele` identique hors de `go:` ; configuration `e5306c47…` inchangée.
- **Paragraphe de scellement de la v1** (v1, lignes 3 à 24) : présent une seule fois dans le brouillon, caractère pour caractère,
  ligne 436, dans la section 0.5 (lignes 358 à 457).

## 3. Épreuve du lanceur rejouée (point 2)

Arbre à moi : `orchestrator/` du commit `9776ed0efee97146182ff2c4b409e5ec224a0bbf`, extrait par `git archive` dans
`/tmp/cl-arbre-9776ed0-ljHWI8/` sans aucun `.sha256` (lanceur `87d52ace…`, cœur `cb9cffe7…`, `pole` chargé depuis cet arbre).

**(a) Rejeu de `epreuve_lanceur_v2b1.py` du rédacteur** (`dc3a7fab…`) sur cet arbre, à 09:03:38 UTC : sortie
(`travail/epreuve-rejouee.json`) égale à la sienne (`sorties/epreuve-v2b1-final.json`, `386b6cd3…`), chemins et dates mis à part
(un seul écart, le chemin du registre factice ; mon registre factice est le sien octet pour octet, `19eb4860…`).

| cas | résultat |
|---|---|
| `lire_plan` du brouillon | accepté ; seule la clé `go` diffère de la v1 |
| copie au nom scellé, sans compagnon | refusé : « préenregistrement non scellé (compagnon .sha256 absent ou non conforme) » |
| compagnon simulé juste / faux | accepté (73 empreintes, entropie = entier de l'empreinte, ≥ 2⁶⁴) / refusé « non scellé » |
| même texte au nom du brouillon ; brouillon à son chemin dans la copie de travail | refusés : « mode réel : le texte est prereg/preenregistrement-attaque-goodhart-v3-v<N>.md (course) … » |
| une empreinte du bloc altérée | refusé : « code différent du code gelé : pole/attaque_goodhart_v3.py : gelé db9cffe77fb8…, présent cb9cffe77fb8… » |
| assemblage de 08:29 UTC (`2bed4c99…`), qui portait le jeton AUDIT_A9 entre doubles chevrons | refusé : « marqueur(s) non rempli(s) » |
| GO-2026-11-03-01, registre factice | accepté : calcul, Lazar, 2026-11-03 → 2026-11-17, 400 USD lus = 400 requis |
| GO-2026-11-02-21 en ligne de commande avec la v2 | refusé : « GO GO-2026-11-02-21 : le texte scellé nomme GO-2026-11-03-01 (aucun autre GO) » |
| plafond 399 / 401 USD | refusés : « A15 : la ligne GO-2026-11-03-01 porte 400 USD, pas exactement le plafond requis … » |
| dates 2026-11-02 / 2026-11-17 / 2026-11-18 | refusé / accepté / refusé (« hors de sa période de validité (2026-11-03 → 2026-11-17) ») |
| révocation qui nomme le GO ; décision qui le nomme | refusé (« révoqué par ») ; accepté |
| révocation de GO-2026-11-02-21 qui porte aussi GO-2026-11-03-01 ; qui ne le porte pas | GO neuf refusé ; GO neuf accepté (GO-2026-11-02-21 refusé) |
| registres entiers de `canal/conv-audit-n04` (arbre `8223230c…` ; `e4fd3690` `a5036824…` ; `3f132371` et `c8c34784` `45d56fa0…`) | GO neuf accepté (ligne 79) ; 0 doublon |
| `canal/conv-audit-n04` à `e9d7b78d` (`53985197…`, la copie de la première course) | GO neuf refusé (absent) ; GO-2026-11-02-21 accepté (ligne 67) |
| `main` à `e12540bf` (`7582a58e…`) et à `db454552` (`13d69db3…`) | tout refusé : « registre des GO : identifiant GO-2026-10-24-07 en double » (16 doublons) |
| renvois | 45 renvois des passages neufs conformes ; 151 renvois vers les deux fichiers v3 dans les bornes ; aucun marqueur |

**(b) Épreuve complémentaire** (`travail/epreuve_complementaire_cl.py`, sortie `travail/epreuve-complementaire-cl.json`,
09:05:09 UTC), avec de **vrais compagnons sur disque**, écrits dans le dossier temporaire puis retirés (le rédacteur avait simulé
la lecture en mémoire) :

| cas | résultat |
|---|---|
| v2, compagnon réel juste | accepté : `c76ac6bc…`, 73 empreintes, entropie = entier de l'empreinte ≥ 2⁶⁴, GO-2026-11-03-01, 400 USD, 259 200 s, 24 cartes, 24 unités par case, `relais_perdu_s` nul, configuration `e5306c47…` |
| v2, compagnon réel faux ; sans compagnon | refusés « non scellé » |
| **v1 avec son vrai compagnon** (copié du dépôt public dans le dossier temporaire) | **accepté** : `898d5be4…`, 73 empreintes, GO-2026-11-02-21 |
| registre de la tête de `canal/conv-audit-n04` (`d5ca44f7`, = `origin`, `8223230c…`, 81 lignes, 0 doublon, aucune révocation qui nomme l'un des deux GO) | v2 + GO neuf accepté (l. 79) ; v2 + GO-2026-11-02-21 refusé ; **v1 + GO-2026-11-02-21 accepté (l. 67)** ; v1 + GO neuf refusé ; GO-2026-11-02-21 le 2026-11-16 accepté, le 2026-11-17 refusé |
| registre de la tête de `origin/main` (`03c0d42a`, `8627dc4a…`, 223 lignes) | tout refusé, mêmes 16 doublons |
| texte avec mes couples (`b28ed1de…`) | sans compagnon refusé ; compagnon réel juste accepté (73 empreintes) ; GO neuf accepté sur la tête `6511bbf1` (registre inchangé, `8223230c…`) |

Non fait, déclaré : `--verifier-seulement` (il exige `--moteur reel` et la configuration chez session-depot).

## 4. Les points visés (point 3)

1. **Règle de la section 8, citée exactement** : oui. Les quatre morceaux de la citation (section 0.5) sont dans la v1
   (l. 1112-1116), dans l'ordre ; les « (…) » ne font que couper (la parenthèse des arrêts d'infrastructure, « issue 6 « bras
   perdu » d'infrastructure, », « ou arrêt décidé par Lazar par écrit ») ; seul le gras est retiré. Cas visé : « arrêt du lanceur
   hors de ses codes 0, 2 et 3 ». Argument de code : `:592` (manifeste), `:609-621` (code 3 et sortie), `:637-646` (code 0 et
   sortie), `:562-567` (code 2) sont justes ; l'audit cite `:562-566`, `:618-620`, `:640-648`, mêmes blocs ; en mode course,
   aucun code 2 après le manifeste (le seul, `:625-629`, est celui du mode essai).
   **Conclusion de l'audit A9** : chemin, commit `c8c34784` (R-1337) et empreinte vérifiés ; huit phrases reprises mot pour mot de
   sa section 7 ; deux glissements et un renvoi incomplet (M-1). Les « cinq points » sont les critères du brouillon lui-même
   (paragraphe du marqueur de l'assemblage de 08:29 UTC) ; l'audit y répond : (1) sections 2 et 7 ; (2) sections 2 et 6 (« aucun
   acteur n'a envoyé de signal », « ce n'est la faute de personne ») ; (3) section 3 ; (4) sections 3 et 4 ; (5) section 5.
2. **Graine neuve** : oui. Lignes vérifiées : lanceur `:288`, `:289`, `:540`, `:577`, `:583-588`, `:607`, `:637` ; cœur `:708`,
   `:729`, `:500`, `:769-770` ; cœur v2 `:104-108`, `:165-186`, `:170`, `:178`, `:442-444`, `:813`. 48 cartes = 24 par monde, W1 et
   W2. Aucune carte calculée par mes épreuves (aucune n'appelle `jouer_tout` ni `lire`).
3. **GO** : 400 USD exactement (`plafond_usd: 400` du bloc ; cellule « 400 USD » de la ligne ; égalité à 10⁻⁹ exigée par
   `verifier_go_v55`) ; échéance 2026-11-17 ; GO-2026-11-02-21 en ligne de commande refusé (message exact ci-dessus).
   GO-2026-11-03-01 à chaque lieu où le texte nomme le GO de la course (bloc l. 958, section 4 l. 852, commande l. 922, registre
   l. 880-895, section 12 l. 1542, section 13 l. 1603) ; les 41 lignes qui portent GO-2026-11-02-21 désignent toutes la première
   course ou l'historique (sections 0.1 et 0.1 bis, L15, L16 compris). I4 « ne tient plus » : juste, la ligne neuve ne cite aucun
   commit. Le piège de la révocation est dit (section 4, l. 862-865 ; section 14).
4. **Source du registre** : la décision du directeur n'est pas dans le texte (I-1).
5. **Hôte nommé, session active, observation du dehors** : la fille de session-depot est nommée (l. 377-379, 912, 1647) ;
   « période nettement inférieure à 5 min » écrite (l. 1355, 1649-1650) ; « jamais la seule relève horaire », « suivie de hors du
   conteneur » écrits (l. 1357-1359, 1651-1652) ; mais voir I-2.
6. **Fin brutale acceptée et dite** : oui (section 8, (3), l. 1359-1365 ; section 0.5, l. 432).
7. **4,245753 USD non imputés** : oui (section 0.5, l. 423-428 ; section 12, l. 1542-1544). C'est d'ailleurs la seule lecture
   compatible avec la ligne du GO (« exactement 400 USD ») : imputés, ils feraient un plafond de 395,754247 USD, que le lanceur
   refuserait (montant du GO égal au plafond, à 10⁻⁹ près).
8. **Identifiant de processus du guetteur** : « chacun pris du processus lui-même » (l. 1653-1654).
9. **« Rapportée avec la course arrêtée, jamais seule »** : oui (section 0.5, l. 421-423 ; section 13, point 9, l. 1667-1668).
10. **Aucun marqueur** : aucun jeton au motif du lanceur v3.1 (`<<[A-Z0-9_]+>>`), aucun double chevron dans tout le texte.
11. **Commande exacte** : ne changent que le dossier de sortie, `--preenregistrement …-v2.md` (au lieu de `…-vN.md`), le chemin de
    `--registre-go` et `--go GO-2026-11-03-01` ; `nice -n 10 python3 -I -B demonstrations/attaque_goodhart_v3.py`,
    `--configuration` et `--moteur reel --confirmer-moteur-reel` sont ceux de la v1 ; l'hôte est nommé.

## 5. Le danger : relance de la v1 (point 4)

**La v1 l'interdit déjà.** Sa section 8 (l. 1112-1116) n'admet une seconde course que « sur un texte nouveau et un GO nouveau » :
une relance sous la v1 est une course de plus sans texte nouveau ; et « un scellement, une course » (paragraphe de tête de la v1 ;
section 4 ; T, lignes 144 et 145), « aucun rejeu automatique ». Session-depot le lit de même (n° 305 : « le reste du GO-21
n'ouvre pas une course nouvelle, selon la section 8 »). **Mais le code ne l'empêche pas** : la v1 et son compagnon sont acceptés
par le lanceur, et GO-2026-11-02-21, non révoqué, est accepté avec elle sur le registre de `canal/conv-audit-n04` jusqu'au
2026-11-16 (épreuve (b)).

**Ce que le texte doit dire** (couples 4 et 14, I-3) : (1) aucune relance de la v1 ; toute autre course sous la v1 n'est pas une
course de ce programme mais un écart à un préenregistrement scellé (nœud de décision) ; (2) qui tient la règle : le directeur, qui
ne donne que la commande exacte de la section 4, et session-depot et sa fille, qui ne lancent qu'elle ; (3) la trace : l'empreinte
du texte passé à `--preenregistrement`, écrite au journal de lancement avant `--verifier-seulement`, et le manifeste qui la porte
(`preenregistrement.sha256`, `demonstrations/attaque_goodhart_v3.py:553`, `:578`) ; (4) une révocation de GO-2026-11-02-21 (posée à
Lazar, R-1341) ne porte pas l'identifiant GO-2026-11-03-01. Seule une telle révocation ferait tenir la règle par le code
(épreuve (a) : révocation de GO-2026-11-02-21 seule → GO-2026-11-02-21 refusé, GO neuf accepté).

## 6. Constats

### Bloquants

Aucun.

### Importants

**I-1 — Source du registre : la décision du directeur manque.** Le texte (section 4, règle (1), l. 879, et point (1 bis),
l. 893-896) laisse encore le choix (« un commit de `main` dont les doublons sont levés, ou un commit de `canal/conv-audit-n04` qui
porte la ligne — est une décision du directeur avant `--verifier-seulement` ») et ne demande le `grep -n` sur `main` que « si la
copie ne vient pas de `main` ». Décision du directeur (R-1340, 08:56 UTC ; canal n° 407) : copie prise sur `canal/conv-audit-n04`,
à un commit qui porte GO-2026-11-03-01, comme la première course (`e9d7b78d`), sans retouche, et sortie de
`grep -n "GO-2026-11-03-01"` sur la copie et sur le registre de `main` au journal de lancement avant la course. Faits vérifiés :
`main` refusé à `e12540bf`, `db454552` et `03c0d42a` (16 doublons) ; `canal/conv-audit-n04` accepté (tête passée de `93346b56` à
`d5ca44f7` puis `6511bbf1` pendant cette lecture, registre inchangé, `8223230c…`) ; `e9d7b78d` est sur cette branche, pas sur
`main`, et son registre est `53985197…`. Couples 8 et 9 (texte), 5 (changement 12 de la section 0.6) et 6 (ligne 37).

**I-2 — Hôte gardé vivant : le délai de 2 h n'est pas la période, et l'activité ne laisse aucune trace.** Le texte exige « une
attente suivie par le harnais qui ne la laisse jamais inactive plus de quelques minutes (période nettement inférieure à 5 min),
réarmée avant son délai (2 h au plus) » (section 8, l. 1354-1356 ; point 7 bis, l. 1648-1650). Le moyen vient de l'option (a) de
session-depot (n° 305 : « une attente en arrière-plan suivie par le harnais (…) commande qui attend la fin du processus, réarmée
avant son délai de 2 h ») ; l'exigence vient de l'audit A9 (section 8, point 1 : « période nettement inférieure à 5 min » ;
« un processus détaché ne garde pas le conteneur en vie »). Les deux ne tiennent ensemble que si la session reste active pendant
l'attente ; une attente en arrière-plan de 2 h ne l'assure pas d'elle-même (la première course est morte ≈ 5 min après
l'inactivité de la session). Observation du contre-lecteur, non vérifiée chez la fille : dans cet environnement d'exécution, la
documentation des outils dit qu'une commande en arrière-plan est probablement arrêtée quelques minutes après la fin de la réponse
de la session ; une attente de 2 h en arrière-plan ne garde donc l'hôte vivant que si le tour de la fille reste ouvert. Ensuite,
seuls les réarmements sont écrits au journal (l. 1654-1655) : la période de moins de 5 min, cœur du remède, ne laisse aucune pièce,
et l'audit A9 de la seconde course ne pourrait pas établir si la règle a tenu. Enfin « fin du lanceur (code 0, 2 ou 3) » laisse de
côté une fin par exception (code 1). Couples 10, 15 et 16 (ligne 38).

**I-3 — Relance de la v1** : section 5. Couples 4 et 14 (ligne 39).

### Mineurs, avec couples

- **M-1 — Conclusion de l'audit A9, au plus près** (section 0.5) : « sortie d'erreur de la course vide » pour « `course-stdout`
  vide » ; « mort » pour « morte (ou gelée) » (audit, section 2 : « signal ou gel d'infrastructure, sans qu'on puisse dire
  lequel ») ; « sections 2, 3, 4 et 7 » alors que l'écart vient de la section 5. L'audit dit d'ailleurs que les trois fins
  « écrivent toutes sur la sortie d'erreur » : inexact pour le code 0 (résumé sur la sortie standard, `:641-645`), sans effet
  puisque le code 0 écrit `attaque-goodhart-v3.json` (`:640`), absent ; le couple évite de porter cette inexactitude dans le
  texte. Couples 1 et 2 (ligne 40).
- **M-2 — « les deux courses » (section 0.5) et « les deux courses précédentes » (section 8)** : une seule course précède la
  seconde ; la reprise est en outre rapportée avec A1. Couples 3 et 11 (ligne 41).
- **M-3 — « sur la machine de session-depot (hôte de la course, la fille …) »** (section 4) : la machine est celle de l'hôte, la
  fille. Couple 7 (ligne 42).
- **M-4 — L17, règle R6** : la ligne cite « 150 renvois » et la sortie `sorties/epreuve-v2b1.json` ; ce fichier est l'épreuve de
  l'assemblage de 08:29 UTC (`9e9e84ac…`, 150 renvois, 44 passages, marqueur présent) ; l'épreuve finale est
  `sorties/epreuve-v2b1-final.json` (`386b6cd3…`, 151 renvois, 45 passages), que mon rejeu retrouve. Couples 12 et 13 (ligne 43).

### Mineurs, sans couple

- **M-5 — Section 13, point 1, inchangé** (« rejouer les essais v3.1, v4 et v2 et le banc sur ce commit ») : acceptable. Le code est
  celui de `9776ed0` (73 empreintes égales aux objets du commit), le lanceur refuse tout autre code ; un rejeu avant la seconde
  course coûterait peu mais le delta ne l'exige pas.
- **M-6 — Section 12** : un « pas une » seul sur sa ligne (l. 1545), coupure de mise en page sans effet sur le rendu.
- **M-7 — Section 13, point 7** commence encore par « **Chez session-depot** » ; le point 7 bis, explicite et qui suit, met la
  course, le relais et le guetteur chez la fille : pas d'ambiguïté sur l'hôte.
- **M-8 — « Argon seul »** (section 8, (4) ; point 7 ter) lit le « Argon seul » de la ligne du GO (l'instrument) aussi comme
  l'exclusivité d'Argon pendant la course (consigne ; relais à un seul fil) ; écart déclaré, pas un arrêt : cohérent avec la règle
  des guetteurs. Conséquence pour le directeur : la course Heimersheim (GO-2026-11-03-02), chez la fille depuis ≈ 08:31 UTC
  (R-1338), doit être finie et son relais arrêté par son identifiant avant `--verifier-seulement`, et aucune utilisation d'Argon ne
  peut être prévue pendant jusqu'à 72 h.
- **M-9 — Faits n° 305 et 306** cités comme faits de session-depot : ceux que j'ai pu confronter (n° 305, `/tmp/sd-n305.md` :
  option (a), ≈ 25 h, pire ≈ 36 h, chemin neuf) concordent ; la branche `donnees/…` n'est pas lue (interdit).
- **M-10 — Rapport du rédacteur, pas le texte** : D-B décrit GO-2026-11-03-03 comme « pour les deux appels seuls Astra et
  Argon » ; la ligne est « R1 rendu lisible (table v4) », dont la référence porte aussi le go de Lazar pour ces deux appels
  (registre, l. 81). Sans effet sur le texte, qui ne cite pas GO-2026-11-03-03.

## 7. Couples (16, dans l'ordre d'application)

Fichier : `/home/claude/scratch/a1-v3-v2-contre-lecture/couples-contre-lecture-attaque-goodhart-v3-v2-brouillon1.json` (liste de
`{"ancien", "nouveau"}`, même format que les couples des contre-lectures n° 1 et 2), produit par `travail/couples_cl.py`.

| n° | constat | lieu (ligne du brouillon) | en bref |
|---|---|---|---|
| 1 | M-1 | 0.5, l. 409 | « sections 2 à 5 et 7 » |
| 2 | M-1 | 0.5, l. 411-413 | « `course-stdout` de la course vide » ; « mort ou gel de la course (…) » |
| 3 | M-2 | 0.5, l. 431-432 | « rapporté avec la première course (et, comme elle, avec A1) » |
| 4 | I-3 | 0.5, l. 432-433 | + « **Aucune relance de la v1** » : règle, qui la tient, trace, révocation |
| 5 | I-1 | 0.6, l. 484 | changement 12 : « choix du directeur » → source fixée (R-1340 : changement 37) |
| 6 | (liste) | 0.6, l. 528-529 | + lignes 37 à 43 : les changements de cette contre-lecture, une ligne chacun |
| 7 | M-3 | 4, l. 874-875 | « sur la machine de l'hôte de la course (la fille de session-depot …) » |
| 8 | I-1 | 4, l. 879 | « de la branche privée `canal/conv-audit-n04` (point (1 bis)) » |
| 9 | I-1 | 4, l. 893-896 | décision du directeur (R-1340, canal n° 407) ; `grep -n` sur la copie et sur `main`, toujours |
| 10 | I-2 | 8, l. 1356 | « ce délai borne une attente, il n'est jamais la période » ; relevé d'activité au journal |
| 11 | M-2 | 8, l. 1364-1365 | « rapporté avec la première course (et, comme elle, avec A1) » |
| 12 | M-4 | 9, L17, l. 1395 | « 151 renvois » |
| 13 | M-4 | 9, L17, l. 1395 | sortie de l'épreuve finale `epreuve-v2b1-final.json`, `386b6cd3…` |
| 14 | I-3 | 13, point 3, l. 1603 | « qui ne sert à aucune autre course : aucune relance de la v1 » |
| 15 | I-2 | 13, point 7 bis, l. 1650 | « ce délai n'est jamais la période » ; « fin du lanceur, quel qu'en soit le code » |
| 16 | I-2 | 13, point 7 bis, l. 1654-1655 | heure UTC de chaque relevé d'activité de la session au journal de lancement |

Contrôles sur le texte obtenu (`travail/controles-couples-cl.json`) : chaque « ancien » unique dans le brouillon et à son
application ; le fichier des couples, réappliqué, redonne le même texte ; couples dans les seules sections 0 (0.5, 0.6), 4, 8, 9
et 13 ; blocs, marqueurs, `lire_plan` et lecture par le lanceur comme en section 1 ; renvois neufs `:553` et `:578` conformes ;
différence du brouillon au texte obtenu : 15 blocs, 20 lignes retirées, 60 ajoutées (1 856 → 1 896). La section 0.6 reste
exacte : avec la ligne 37 à 43, « la v1 avec, et seulement, les changements de la section 0.6 » reste vrai.

## 8. Pour le directeur, hors du texte

- Paragraphe de scellement : citer cette contre-lecture et ses couples (chemin, empreinte), comme la v1 l'a fait pour la n° 2.
- Éprouver avant la course le moyen retenu pour garder la session active, à coût nul : un processus factice sous ce moyen, la
  fille sans tour ouvert pendant au moins 15 min ; s'il meurt, le moyen ne tient pas (même esprit que R5).
- Révocation de GO-2026-11-02-21 (R-1341) : une ligne sans l'identifiant GO-2026-11-03-01 (pas de « remplacé par
  GO-2026-11-03-01 ») ; sinon la seconde course est refusée à `--verifier-seulement` (code 2, rien dépensé).
- La tête de `canal/conv-audit-n04` bouge sans cesse (trois têtes pendant cette lecture) : le hash complet du commit d'extraction
  au journal (déjà exigé, règle (1)) suffit.
- Hors de ma portée, laissé tel quel : `/tmp/cl-a1v3-1-b4/` contient huit compagnons `.sha256` d'une contre-lecture antérieure
  (dossier temporaire, hors de tout dépôt).

## 9. Fichiers et empreintes

| fichier (sous `/home/claude/scratch/a1-v3-v2-contre-lecture/`) | sha256 |
|---|---|
| `contre-lecture-courte-attaque-goodhart-v3-v2-brouillon1.md` (ce rapport) | donnée avec la remise |
| `couples-contre-lecture-attaque-goodhart-v3-v2-brouillon1.json` (16 couples) | `1e2a7295e49aa501ee877eeb8874a1af2ebf061f9558bb57a32049a3b3324b84` |
| `travail/brouillon1-avec-couples-cl.md` (brouillon + couples ; pièce de contrôle, non scellée) | `b28ed1de35d26919464777d2f38658acf32c76037762923b1fbca87ea811bca0` |
| `travail/couples_cl.py` | `b13072999f11754e59fb621917ebf022e4dfb8bc3bc4d1b30fb7bae989b72921` |
| `travail/controles-couples-cl.json` / `.txt` | `03e44476bf1c9d50b10f0b85a63c9198c340b15e8d8b38bf4c4b5eb59265e215` / `63e86eebab2214ea3c34c66d41b333bc6cf0bb4038cd2c770c0d286e8a80ddfb` |
| `travail/epreuve-rejouee.json` / `.txt` (rejeu du script du rédacteur) | `468b97402e8c7c790595e062b9c4989e1ea9a6d9b2aa2deb692ef57b5a25acc0` / `c24020b272daa091e030d84eac967a1c27146089ad40abbbfd93bc4ff7cf8ef8` |
| `travail/comparer_epreuves.py` | `cc5de91b71db5dd0bd788b55c3098f9fc2f7392478db21fd8556445e8a235dad` |
| `travail/registre-go-factice-rejeu.md` | `19eb48609643eee991cc6e82cf51c36cfa8935523923f4855f746444e782aa86` |
| `travail/epreuve_complementaire_cl.py` | `b5fd7b911e8a4c32709a625032c02ba0bace1a6615fb18cbf62d86dfe394c1b7` |
| `travail/epreuve-complementaire-cl.json` / `.txt` | `b496e5ab866fe19b57cae90f173c3b8b650007a03f0934c15642fc8eaad0836f` / `b004ea79743e15a8bad2d6fa56cd33658de992a85945c34974877059d33b42d8` |
| `travail/controles_citations_cl.py` / `controles-citations-cl.json` | `d705420f99a393c7f864ce824b98836cc9029ff9a34da97d2d9031874673461a` / `8b5fb0908574b997714e48e476f1640b99b079931eea17016a2fe6f425ea2bfb` |
| `travail/table_36_cl.py` / `table-36-cl.json` | `420bf28f04c0b9fd97e155e4a71805ee4862362dd07b2134946ff7184effb61c` / `398f8bd67cfd4384e67188d8c79e31c43d8fa9f31349bc5ef127747b1238b33b` |
| `travail/*.err` (quatre fichiers, vides) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

Dossiers temporaires à moi (`/tmp/cl-arbre-9776ed0-ljHWI8/`, arbre extrait, et `/tmp/cl-patch-xgOeAU/`, reconstruction par
`patch`) : aucun `.sha256` restant ; retirés à la fin.

## 10. Réserves

- Interruption vers 09:10 UTC (redémarrage du serveur) ; reprise à 09:11 UTC sur les fichiers déjà écrits, entrées de nouveau
  empreintées et égales.
- L'observation sur les commandes en arrière-plan (I-2) vient de la documentation de cet environnement, non de celui de la fille.
- `canal/conv-audit-n04` et `main` ont avancé pendant la lecture : chaque fait est daté par son commit.
- La routine de reprise du dépôt n'a pas été jouée : sous-agent à consigne bornée, elle revient à la session qui m'a lancé.
