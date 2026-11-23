# Papier C — consigne de l'agent de la grille de la clause de repli (rapport v2) — v1

Date : 2026-11-22. Écrite par le rédacteur du brouillon 7 de relance du préenregistrement du papier C (session fille
`session_013QMayk1rjSZrn2u9UAVhEp`), à la demande de la session de conduite (message du 2026-11-22 vers 20:17Z :
jouer sur processeur, sans dépense, les cases de la grille que personne n'a jouées, et rendre le rapport scellé).
Classe C (mandat). Écrite et scellée avant tout lancement ; le rédacteur ne joue aucune case et ne lit aucun taux.

## But

Compléter le rapport de la grille de la clause de repli de la stabilité de rang (lignes C-P3a, C-P3b, C-P3c du
préenregistrement du papier C) : jouer, sur données simulées, les cases de la **liste finie** que le rapport v1 n'a
pas jouées, et écrire un rapport v2 qui couvre la liste entière pour les trois lignes.

## Pourquoi

Le directeur a retenu la version (a) du bloc de la stabilité de rang « sous réserve du rapport de la grille
entière » (décision D-9). Le texte exige que ce rapport vienne d'un agent neuf, qui n'est rédacteur d'aucune version
du texte, qu'il couvre toutes les cases de la liste finie pour les trois lignes, et qu'il soit contre-lu par un
autre modèle. Sans lui au scellement, la version (b) s'applique (issue 3). Tu es cet agent neuf.

## Ce qui est établi

- La lecture sous laquelle la grille se joue est fixée : précision 37 du texte (les statistiques de C-P3a et de
  C-P3b sont toujours lues), gardée par la ligne GO-2026-11-22-125 de `registres/go.md`. Tu n'as pas à la juger.
- Les effectifs sont fixés par le texte : C-P3a et C-P3b, R = 1 000 essais et 1 000 tirages par grappes ; C-P3c,
  R = 8 000 essais. **Ils ne se réduisent jamais.**
- D'après le texte (à revérifier par toi) : il manque 58 cases pour C-P3a et C-P3b et 48 cases pour C-P3c.

## Pièces à lire

Règles (dépôt, branche courante) :
- `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c5.md`
  (`0747f357c30335ec7c37192be7b0d827bdcb4c6e3287c27c000c9d9ee2de723d`), lu avec
  `registres/papier-c/redaction-brouillon7-relance-v1/erratum-1-version-c5-brouillon7-relance-v1.md`. Passages :
  verrou 10 ; section « Prédiction chiffrée et signe attendu », bloc « Stabilité de rang » en entier (versions (a)
  et (b), tableau, « Trois lectures », « Clause de repli mécanique », « Liste finie des cases de la clause »,
  effectifs, modèle des deux gains d'écart de C-P3c, « Règles de lecture du rapport », les trois issues) ; « Plan
  d'analyse », section 8, précisions 3, 5, 8 et 37 ; « Métrique », points 7 à 13 au besoin. Le reste du texte ne te
  sert pas.
- `src/controle_ia/manifeste.py` (manifeste de run).

Pièces du 19 novembre, dans une copie hors du dépôt (racine C =
`/tmp/claude-0/-home-user-controle-ia-travail/61e4d11a-8d28-5a5e-8f56-9a6c1ff76fbf/scratchpad/c19b`) :
- liste finie : `C/registres/papier-c/redaction-brouillon6-relance-v1/redacteur/liste-finie-cases-grille-v1.md`
  (`0c62072c8fe7ea76f0d3dbe190c0f994fb1aa8c58ca793dddf60f412bf5bfb94`) ;
- rapport v1, ses programmes, ses sorties, son archive et leurs listes d'empreintes :
  `C/registres/papier-c/redaction-brouillon6-relance-v1/grille/` ;
- contre-lecture du rapport v1 (1 bloquante, 3 majeures, 10 mineures) :
  `C/registres/papier-c/redaction-brouillon6-relance-v1/contre-lecteur-grille/` ;
- rejeu de 24 cases par le rédacteur du 19 novembre, pour information seulement (un rédacteur ne compte pas) :
  `C/registres/papier-c/redaction-brouillon6-relance-v1/redacteur/travail/rejeu-grille-c1/`.

## Interdits

- Rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; rien dont le nom contient « consigne-privee » ou
  « conception-ii-b » ; pas le dossier voisin `…/scratchpad/c19` (sans « b ») ; pas les branches `juge/…`,
  `prep/quarantaine-…`, `lot/compte-4-v1`.
- Aucune dépense, aucune machine louée, aucun appel payant ; jamais la suite d'essais complète du dépôt.
- Aucun commit, aucune poussée : tu écris, le rédacteur verse.
- Tu n'écris que sous `registres/papier-c/grille-clause-de-repli-v2/`.
- Au premier refus de permission : arrêt, texte exact rendu, aucun contournement.

## Règles du travail

1. **Avant tout lancement** : dis quelles cases de la liste manquent, par ligne, en comparant la liste finie aux
   sorties du rapport v1 ; une case de v1 n'est reprise que si elle a été jouée comme la liste et les effectifs du
   texte l'exigent (sinon elle est à jouer, et tu dis pourquoi). Copie les programmes sous ton dossier. S'ils jouent
   les cases manquantes tels quels, ne les change pas. Tout changement : nom neuf (R12), différence écrite et
   justifiée. **Empreintes des programmes figées dans un fichier avant le premier lancement** ; aucun programme ne
   change après la lecture d'un taux.
2. **Graines** (R9) : `numpy.random.SeedSequence`, dérivées par case, consignées. Si les programmes de v1 dérivent
   déjà une graine par case, garde leur règle. Un manifeste par run (configuration et empreinte, versions, graines,
   commit).
3. **Première passe seule** : chaque case est jouée une fois, à l'effectif fixé. Une case tombée pour une cause
   technique est relancée avec la même graine et consignée. Aucune case n'est rejouée pour un autre motif.
4. **Faisabilité d'abord** : mesure le temps d'une case de chaque sorte, estime le total sur cette machine
   (4 cœurs). Lance en arrière-plan. Si le total dépasse 8 heures d'horloge, arrête-toi après la mesure et rends
   l'estimation : la conduite décidera. Ne réduis ni les essais ni les tirages.
5. **Garde de complétude** (R5) : une fonction vérifie que chaque case de la liste finie est présente une fois et
   une seule, par ligne et par bras ; elle est essayée sur un cas sain et sur un artefact (une case manquante, une
   case en double).
6. **Remarques de la contre-lecture du rapport v1** : une table dit, pour chacune, ce que le rapport v2 en fait (le
   texte en a déjà traité plusieurs : liste finie, tirages dégénérés, effectifs, 30 tâches).
7. **Symétrie** (R3, R4) : aucun taux n'est visé ; tout est écrit, quel que soit son sens ; un résultat trop propre
   se signale comme un résultat gênant.

## Ce que tu rends

Dans `registres/papier-c/grille-clause-de-repli-v2/`, chaque fichier avec son compagnon `.sha256` (R6 ;
`PYTHONPATH=src python -m controle_ia.scellement sceller FICHIER…`, environnement `.venv`) :
- `programmes/`, `sorties/` (une sortie par case), manifeste(s), liste des empreintes figées avant lancement ;
- `rapport-grille-clause-de-repli-v2.md` : pièces et empreintes ; ce qui vient de v1 et ce qui est neuf ; par ligne
  (C-P3a ; C-P3b ; C-P3c, bras « insertion » et « contenu »), nombre de cases jouées sur le nombre de cases de la
  liste, taux de « établie » par case avec son effectif et son seuil, plus haut taux et sa case, cases au-dessus du
  seuil ; ce que le texte appelle l'issue, par ligne, **dite comme un constat** (le texte la recopie au scellement) ;
  table des remarques de la contre-lecture de v1 ; écarts et limites ; ce que tu as lu en fait ;
- un journal court (heures, commandes, durées).

**Dans ta réponse au rédacteur : aucun taux, aucune issue, aucun mot sur le sens des résultats.** Le rédacteur du
texte ne doit pas les lire. Rends seulement : chemin et empreinte du rapport ; par ligne, nombre de cases couvertes
sur le nombre de cases de la liste ; nombre de cases reprises de v1 et de cases neuves ; rapport complet ou non ;
durée ; changements de programme ; écarts de procédure. Si quelque chose t'empêche de finir, dis quoi.
