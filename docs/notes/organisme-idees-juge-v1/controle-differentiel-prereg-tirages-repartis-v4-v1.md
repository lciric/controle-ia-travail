# Contrôle mécanique du différentiel v3 → v4 du préenregistrement « tirages répartis par blocs avec arrêt anticipé » (idée 1.2) — v1

- Lecteur : sous-agent neuf ; je n'ai écrit ni le préenregistrement (v1 à v4), ni ses contre-lectures, ni la vérification
  courte, ni la relecture du différentiel v2 → v3, ni le banc, ni la preuve, ni le juge.
- Date (UTC) : 2026-11-15, vers 09:39 (`date -u`). Dépôt lu sur `main` (tête `159d04c3`). Aucun commit, aucune poussée, aucun
  appel payant ; rien écrit sous `diag/`, `donnees/`, `docs/verdicts/` ; aucun code exécuté hors le validateur ; le programme
  d'essai de la contre-lecture a été lu, non joué. **Aucun résultat du banc n'existe, je n'en ai produit aucun** (R1).
- Pièces, dans `docs/notes/organisme-idees-juge-v1/`, toutes égales à leur compagnon (recalcul `sha256sum`) :
  - v3 `prereg-tirages-repartis-arret-anticipe-v3.md` : `28aab53951c9911586113d9acffcdca319ab67554ae08f93804154dcee04707e` ;
  - v4 `prereg-tirages-repartis-arret-anticipe-v4.md` : `bdabf2bc9b2c9b78939660f7f7053576a145e165927cafd23e14a798d07d790e` ;
  - relecture [RD] `relecture-differentiel-prereg-tirages-repartis-v3-v1.md` :
    `6a71e24d6f764b0a43639fd03f03a3a49e92eb2d7dd51d8837fc5e57e4cf7cbe` ;
  - lu pour recoupement : `contre-lecture-prereg-tirages-repartis-v1-outils/essai_validite_v1.py`
    (`01c648a0f5a65a578e95f73836666d0e55d837ee72438e15b0d37443cbfff205`, égal à l'empreinte citée) ; `registres/decisions.md`,
    R-2885.
- Les numéros de ligne renvoient à la v4, sauf mention.

## Verdict

**Scellable.** Le différentiel est borné aux lignes du tableau « Différentiel v3 → v4 » et aux mentions administratives ;
aucun seuil, aucune prédiction, aucun bras, aucune liste d'arrêt ne change ; P1 et P2 sont fermés par les couples de [RD],
repris mot pour mot ; les sept remarques sont portées ; le validateur rend `[]`. Six observations non bloquantes suivent
(aucune ne demande une v5 ; O1 à O3 sont à écrire dans l'addendum du code avant tout jeu).

## (1) Différentiel exact

`diff` v3 → v4 : **16 blocs, 25 lignes retirées, 72 ajoutées** (625 → 672 lignes). Lu en entier.

| # | bloc (lignes v4) | changement | rattachement |
|---|---|---|---|
| 1 | 1 | titre « v4 » | administratif |
| 2 | 3-8 | auteur « de la v1 à la v3 », n'a pas écrit [RD] ; date de la v4 ; tête `ed6ff5bb` ; « après le contrôle du différentiel v3 → v4 » | administratif |
| 3 | 21-25 | v3 et [RD] ajoutées aux documents qui font foi, empreintes entières | remarque 7 |
| 4 | 62 | R-2885 au registre cité | remarque 7 |
| 5 | 69-73 | Statut : version 4 ; « sa réserve R-a, en deux parts » ; attend ce contrôle | remarque 1 ; administratif |
| 6 | 78-93 | tableau « Différentiel v3 → v4 » neuf | (tableau) |
| 7 | 270-271 | quatrième issue : Q3 vraie, Q4 et Q5 fausses ensemble | remarque 4 |
| 8 | 301-302 | lecture (3) : par bras, toutes cartes réunies, et par sorte dans chaque bras (six sortes, désignées au Seuil) | P1 |
| 9 | 312-315 | jeu d'essai synthétique : sans allocation, maximum sur les 32 instants, intervalle percentile à 95 %, 10 000 rééchantillons | remarque 3 |
| 10 | 333-337 | six sortes nommées ; 7 + 42 = 49 intervalles, seuls à compter ; fausse alerte du côté prudent, dite | P1 |
| 11 | 410-412 | M₀′ jamais tirée d'une loi `si_sinon` | remarque 5 |
| 12 | 420-423 | règle des deux fausses construites de la famille N ; nulles : softmax aléatoires | P2 |
| 13 | 455-456 | clé `(97, g)` à la section Graines | remarque 2 |
| 14 | 488 | étage 1 : « dans l'un des 49 intervalles désignés au Seuil : par bras, ou par sorte dans un bras » | P1 |
| 15 | 522-524 | jeu de 20 000 générations au Coût | remarque 6 |
| 16 | 576-586 | « Contre-lecture 4 » ; « À venir » mis à jour | remarque 7 |

1. **Aucun bloc sans rattachement** : seize blocs, treize sur une ligne du tableau (l. 84-92), le tableau lui-même, deux
   administratifs (blocs 1 et 2 ; la part « statut de la v4 » du bloc 5 est annoncée à la ligne 1 du tableau, l. 86).
2. **Aucun seuil changé** : 13, 39, 14 à 38, 0,05/7, 0,02, 0,05, 0,95, 50, 800, 4 800, 6 000, niveaux et confiances sont hors
   du différentiel. Chiffres neufs, tous déclarés au tableau : six sortes, 7, 42 et 49 intervalles (l. 84) ; 10 000
   rééchantillons du jeu d'essai (l. 88) ; « 1 000 valeurs e » (2 cartes × 500 générations, arithmétique).
3. **Aucune prédiction changée** : le tableau Q1 à Q9 (l. 257-267) est hors du différentiel ; le bloc 7 ajoute une phrase à
   « Ce que serait chaque issue », qui nomme une issue déjà écrite au Seuil (l. 343-345) et à l'étage 4 (l. 492).
4. **Aucun bras changé** : section « Bras » (l. 430-448) hors du différentiel ; le « sans allocation » du bloc 9 décrit le
   jeu d'essai du banc de mutations, non un bras du jeu.
5. **Aucune liste d'arrêt changée** : étapes, liste d'arrêt, plan d'analyse, annexes A et B, Garantie, Hypothèse, écarts,
   citations : hors du différentiel, inchangés à l'octet.
6. **Retraits** : trois formules remplacées, toutes déclarées — « deux de ses réserves (R-a) » (remarque 1) ; « par bras et
   par sorte de carte » et « par bras ou par sorte » (P1) ; « relecture du seul différentiel v2 → v3 » dans « À venir »
   (remarque 7).

## (2) P1 et P2

7. **P1 fermé**, proposition de [RD] reprise mot pour mot (l. 333-335). Comptes refaits : les six sortes partagent les 24
   cartes de la famille N sans reste ni recouvrement — 8 voisines (l. 413), 8 membres exacts (l. 416), 2 porteuses
   construites, 2 copies par morceaux, 2 fausses construites, 2 nulles (l. 418-423) : 8 + 8 + 2 + 2 + 2 + 2 = 24 ; sept bras
   (F, F-arrêt, A, P, P′, F125, G, l. 326) ; 7 × (1 + 6) = 7 + 42 = **49**.
8. **Cohérence Métrique, Seuil, étage 1** : la Métrique (l. 301-302) dit « par bras (toutes cartes réunies) et par sorte dans
   chaque bras (six sortes de la famille N, désignées au Seuil) » ; le Seuil (l. 333-335) désigne les sortes et les 49
   intervalles ; l'étage 1 (l. 488) dit « dans l'un des 49 intervalles désignés au Seuil : par bras, ou par sorte dans un
   bras ». Même mot aux trois endroits ; même intervalle (percentile à 95 %, rééchantillonnage des générations, sur les 500
   générations). Le plan d'analyse (l. 481, inchangé) dit « lectures (2) et (3) sans correction (un seul dépassement
   suffit) », égal au « sans correction de multiplicité » de la l. 335-336. Q9 (l. 267, inchangée) reste compatible.
9. **La phrase sur la fausse alerte (l. 335-337) ne change pas le critère** : une borne basse > 1 dans l'un des 49
   intervalles reste « garantie mise en défaut » (l. 488) ; « l'audit écrit avant le prononcé » est l'audit de symétrie déjà
   exigé pour toute issue (l. 495).
10. **P2 fermé**, proposition de [RD] reprise mot pour mot (l. 420-423). La règle se code sans invention : loi (S1 portant
    une composante), type et dose (ceux de la cellule g mod 10), tirage (indépendant), retrait (cosinus > 0), référence du
    cosinus (la composante de la cellule, celle des porteuses construites), formule (l. 399-400 : f(x) = p(· | x) − S1(· | x)
    sur les 20 000 instances de l'oracle, lequel existe pour la famille N, graine `(famille, g, 2000)`, l. 285 et 455),
    plafond (1 000 tirages, l. 400), cas V4 (même règle), nulles (softmax aléatoires). Voir O1 et O2 pour deux lectures que
    le renvoi « qu'en famille T » porte sans les récrire.

## (3) Les sept remarques

| # | état | où (v4) | contrôle |
|---|---|---|---|
| 1 | portée | l. 69-70 | « sa réserve R-a, en deux parts » |
| 2 | portée | l. 455-456 | clé `(97, g)` ; ne heurte aucune clé (premier élément 97, contre 0, 1 et 99) |
| 3 | portée | l. 312-315 | égal au programme lu, l. 105 : maximum cumulé de log W sur les 32 instants, sans règle d'allocation ; intervalle dit. Voir O3 |
| 4 | portée | l. 270-271 | même nom qu'au Seuil (l. 344-345) et à l'étage 4 (l. 492) |
| 5 | portée | l. 410-412 | dit ; cohérent avec « tirée parmi S1 et S2 » (l. 408) et avec les membres exacts « parmi S1 à S4 » (l. 417) |
| 6 | portée | l. 522-524 | processeur seul, sans juge, durée non mesurée, dans la borne de 24 heures |
| 7 | portée | l. 21-25, 62, 576-586 | [RD] et v3 par empreinte entière (égales aux fichiers) ; R-2885 existe au registre (l. 2845) ; « À venir » mis à jour |

## (4) Validateur

```
PYTHONPATH=src .venv/bin/python -c "from controle_ia import prereg; print(prereg.problemes('docs/notes/organisme-idees-juge-v1/prereg-tirages-repartis-arret-anticipe-v4.md'))"
```

Sortie : **`[]`** (aucun défaut).

## Observations non bloquantes

- **O1 (l. 422, contre l. 400)** : le repli au plafond (« sinon la carte de plus petit cosinus est gardée et signalée ») n'est
  pas récrit pour la famille N ; il vient par « même plafond de 1 000 tirages qu'en famille T ». Lecture naturelle, à écrire
  telle quelle dans le code.
- **O2 (l. 421-422)** : les deux porteuses construites portent la composante à force × 1 et × 0,5 ; la référence du cosinus
  est « la composante de la cellule », donc à la dose de la cellule (force × 1), comme la « composante du monde » en famille
  T. Sans effet sur un critère (toute carte de la famille N est fausse).
- **O3 (l. 312-313)** : la mutation X2 du programme lu plafonne log W à 50 avant de moyenner (garde numérique, l. 105 du
  programme) ; la v4 ne le dit pas. Le code d'essai, gelé par l'addendum avant tout jeu, doit dire s'il garde ce plafond ;
  échec du côté sûr (« pas de jeu »).
- **O4 (l. 332-333)** : le bout de phrase d'origine « dans un bras ou une sorte : défaut » reste devant la désignation ; il
  est borné par « seuls ces 49 intervalles comptent » (l. 335) : pas d'ambiguïté résiduelle.
- **O5 (l. 301-302)** : le nombre de rééchantillons de la lecture (3) sur les 500 générations n'est pas écrit à cet endroit
  (10 000 est dit pour les différences appariées, l. 294, et pour le jeu d'essai, l. 314). Hors du différentiel, présent en
  v3 ; à fixer à 10 000 dans le code, comme partout ailleurs.
- **O6 (l. 73, 302, 337)** : trois lignes non repliées à la largeur du texte ; cosmétique.

## Ce que je n'ai pas fait

Contrôle borné au différentiel : je n'ai relu ni la preuve, ni la Garantie, ni les annexes, ni les parties inchangées au-delà
de ce que les seize blocs touchent ; je n'ai rejoué ni l'essai de la contre-lecture ni aucun code du juge ; aucun calcul sur
donnée.
