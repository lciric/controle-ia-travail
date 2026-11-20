# Rapport du rédacteur — corrections L1 à L8, préenregistrement court de la course « nouvelles attaques », v3 — v1

- Rédacteur neuf, modèle F. Écrit le 2026-11-20 ; relevé de `date -u` : 05:53:28Z, après l'outil, le différentiel et le validateur, avant l'écriture de ce rapport.
- Mandat : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v2/mandat-redacteur-preenregistrement-court-v3-v1.md`, `bf2243267749299044ce2633d4938bd1c977d018687fc672293e8fec75d0d922`, vérifié contre son compagnon.
- Processeur seul : aucun appel à un fournisseur de modèles, aucune dépense. Rien écrit dans le dépôt, aucun commit. Rien ouvert sous `archives-reponses-modeles/`, ni au coffre, ni sous `/root/.claude/`. Réseau : un `git fetch origin main`.
- **Aucun refus de permission, de classifieur ni de garde.** Aucun refus de l'outil de remplacement non plus.

## 0. Verdict

**L1 à L8 sont portées à la lettre dans la v3 : 14 remplacements, un seul appel de l'outil, « FAIT ». Le validateur ne trouve aucun problème à la v3.** La v3 n'est ni scellée ni versée : c'est à la mère. Un écart de moyen est à connaître (§ 4, point 1), et cinq points sont signalés sans être corrigés (§ 5).

## 1. Pièces rendues

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-preenregistrement-court-v3/`. Chaque pièce a son compagnon `.sha256` à côté d'elle.

| pièce | fichier | empreinte |
|---|---|---|
| préenregistrement v3 | `preenregistrement-court-course-nouvelles-attaques-v3.md` | `2ea5ad53de565f912992128a9113da59e5462b561ed258b151d519b193f85787` |
| remplacements (JSON) | `remplacements-preenregistrement-court-v2-v3-v1.json` | `32658dbf1d6cfd1a5ea13a4e1b8b910895616ce4b67127f4bd0b5fa090764036` |
| journal de l'outil | `preenregistrement-court-course-nouvelles-attaques-v3.md.journal-remplacements-v1.json` | `9cdcdb2d6e9011340654b7479ccd1d8a1f4c917a0ea2e3aa6b909b4edf603287` |
| différentiel `diff -u` v2 → v3 | `differentiel-preenregistrement-court-v2-v3.diff` | `e46d962a9d6187d720c2177ef2f188ddd61c12d7e36f34e7b5d36fab5e29903a` |
| script d'appel du validateur | `valider_prereg_v1.py` | `f50245fa5c6ac9cdc5441c9aa42e3d5d84843848cd6be945a41e512d5c796a9c` |
| ce rapport | `rapport-redacteur-corrections-preenregistrement-court-v3-v1.md` | dans son compagnon |

Copies de travail, non rendues : `main/go.md`, `main/decisions.md` (commit relu) et `main/go-3c9ef9cf.md`, `main/decisions-3c9ef9cf.md` (commit du contrôle).

## 2. Ce qui faisait foi, vérifié

| pièce | empreinte | vérification |
|---|---|---|
| contrôle du différentiel v1 → v2 | `7ab69293f34e06c4a74db3c56156ffd525c8db99e52ea9881348f9e0833f8862` | compagnon : OK |
| préenregistrement v2 (cible) | `be4e3c4a6966400a801f34a4951226b313e54cd5af9ed37cc041b04fa08223a1` | compagnon : OK |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` | recalculée |

Relecture de `main` après `git fetch origin main`, commit **`d4ff30302af5b257c224f5b3dbaf8f53f1dbfae7`**, par `git show` redirigé vers un fichier :

- `registres/go.md` : `66dc24e3072df89129351e6bfb1beb474cf7a5f5d1380a8ef2cb85ecff3ef5ef`. GO-2026-11-20-22 y est (ligne 553) : X de 8,35 USD au plus retranché sur Rigaud ; le juge sur Minuit, l'aiguilleur et l'espèce 4 sur Luc, l'espèce 3 sur Rigaud ; borne des trois clés 423,56 − 8,35 USD.
- `registres/decisions.md` : `5226d6bff1a71a0b065a4c3e2f030db644ac90abad867ff2e729aaea7231cc69`. R-4110 y est (ligne 4248). **R-4117** y est (ligne 4255) : K21 acceptée par la mère, en routine ; le contenu de GO-2026-11-20-22 fait foi, « N2 (a) » de la fiche de la mère étant l'option (b) du rapport v2.
- `main` a avancé depuis le commit `3c9ef9cf…` du contrôle. J'ai retrouvé à ce commit les deux empreintes que le contrôle donne (`3fbfcd40…`, `d5a4df8f…`), puis comparé les deux états par `diff`. `go.md` ne gagne qu'une ligne, GO-2026-11-20-23 (une autre affaire). `decisions.md` ne gagne que les lignes R-4111 à R-4120. Aucune ligne n'est modifiée ni retirée : **les lignes nommées sont inchangées**, comme L3 l'exige.

## 3. Les 14 remplacements

Chaque ancre a été comptée par `grep -c -F -e` sur la v2 avant l'appel : 14 fois « 1 ».

| n° | correction | ligne de la v2 | ce qui remplit un crochet du contrôle |
|---|---|---|---|
| 1 | titre, « — v2 » devient « — v3 » | 1 | — |
| 2 | L1 | 7 | empreinte du contrôle : `7ab69293…` |
| 3 | L2 | 8 | empreinte du contrôle : `7ab69293…` |
| 4 | L3, accords | 21 | commit `d4ff3030…`, empreinte `66dc24e3…` |
| 5 | L3, décisions | 22 | empreinte `5226d6bf…` |
| 6 | L4 | 105 | — |
| 7 | L5 | 133 | — |
| 8 | L6 (a) | 139 | — |
| 9 | L6 (b) | 143 | — |
| 10 | L6 (c) | 144 | — |
| 11 | L6 (d) | 145 | — |
| 12 | L6 (e) | 245 | — |
| 13 | L7 | 211 | ligne du registre : R-4117 |
| 14 | L8 | 258 | empreinte du contrôle : `7ab69293…` ; chemin du rapport 2 (§ 4, point 3) |

Les numéros de ligne sont ceux du fichier v2 ; le contrôle compte autrement (sans doute la v1), les textes anciens sont les mêmes. Le différentiel ne montre aucune autre ligne changée. L'outil n'a émis aucun avertissement.

## 4. Choix et écarts

1. **Écart de moyen : le validateur n'a pas de ligne de commande.** `env -C /home/user/controle-ia-travail PYTHONPATH=src python3 -B -m controle_ia.prereg --help` ne rend rien, code 0 : le module `src/controle_ia/prereg.py` n'a pas de bloc d'entrée. J'ai donc écrit, avec l'outil d'écriture de fichiers et dans mon dossier, un script de quinze lignes utiles, `valider_prereg_v1.py`, qui appelle `controle_ia.prereg.problemes` sur un fichier et imprime la liste ; il n'écrit rien et ne scelle rien. Je l'ai appelé par son chemin, sans code en ligne. Le mandat ne prévoyait pas ce script : la mère dit s'il lui convient.
   - v3 : **« CONFORME (aucun problème) »**. Les deux entrées « Contre-lecture 1 » et « Contre-lecture 2 » portent chacune deux empreintes distinctes.
   - v2, passée comme témoin : « section Contre-lecture sans les deux empreintes exigées ». Le script distingue donc bien les deux cas.
2. **L3 se cite au commit relu, non à celui du contrôle**, comme L3 et le mandat le demandent.
3. **L8, chemin du rapport 2.** Le contrôle écrit le nom du fichier seul et dit : « le chemin du rapport 2 est celui où la mère le verse ». Il est versé dans le dossier `preenregistrement-court-v2/` ; j'ai écrit le chemin entier, comme pour le rapport 1. L1 et L2 gardent le nom seul, à la lettre.
4. **L3, liste des décisions.** Je m'en suis tenu à la lettre : la liste gagne R-4110 seulement. R-4117 est citée par L7 dans le corps du texte et n'est pas dans la table « Documents qui font foi ». L'empreinte du registre citée couvre bien R-4117.

## 5. Points signalés, non corrigés (hors de L1 à L8)

1. **La ligne « Date »** ne reçoit pas de relevé pour la version 3 : aucune correction ne le demande. La v3 est datée par le journal de l'outil (05:52:57Z).
2. **Restes écrits avec « X »**, justes une fois X lu à 8,35, mais non récrits : la ligne « somme » de la table des soldes (« moins le besoin du bras A sur Rigaud ») ; le paragraphe « Branche retenue » (« Rigaud 47 USD moins X », « au plus 423,56 USD moins X ») ; le titre « Répartition proposée » et ses deux tables, que L5 garde « comme la règle de choix ».
3. **Le point 4 de « Ce qui reste à écrire avant l'allumage »** dit encore « la contre-lecture de ce texte (règle R2) » comme à faire, alors que la section « Contre-lecture » est maintenant remplie.
4. **« file Claude »** figure une fois (paragraphe « Réserve sur Rigaud », venue de K5 (c)) : nom de famille, non identifiant de modèle ; le contrôle l'a jugé non bloquant.
5. **Les réserves du contrôle (§ 6) demeurent** : la lecture « go a » pour deux décisions est celle de la mère (R-4110), et L4 dit ce qui tombe si Lazar la restreint ; le reste de Rigaud, « environ 47 », est un calcul.

Aucun ajout ne porte de méthode, de procédé ni de détail opérant ; aucun identifiant de modèle n'est ajouté.

## 6. Ce qui reste

Le contrôle demande une vérification courte : rejeu de l'outil sur la v2 avec le JSON rendu, et lecture du différentiel. Puis le versement et le scellement par la mère. Pas de v3 du rapport, comme le contrôle le recommande.

— rédacteur neuf, modèle F
