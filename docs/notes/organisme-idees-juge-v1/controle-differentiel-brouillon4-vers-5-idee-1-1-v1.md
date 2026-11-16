# Contrôle (R2) — différentiel brouillon 4 → brouillon 5 du préenregistrement v2 de l'idée 1.1 (poids du nul) — v1

- Lecteur : contre-lecteur neuf, sous-agent ; je n'ai écrit ni les brouillons, ni la preuve, ni aucune contre-lecture ni
  vérification de ces pièces, ni le programme des couples.
- Rédigé le 2026-11-15 à 22:12 (`date -u`) ; lecture seule ; aucun commit, aucun appel réseau, rien sous `diag/`, `runs/`,
  `donnees/`.
- Pièces lues (empreintes recalculées, toutes conformes à leur compagnon `.sha256`) :
  - brouillon 4 : `docs/notes/organisme-idees-juge-v1/organisme-idee-1-1-poids-du-nul-v2-brouillon4.md`
    (`4adac754a3e90c4c2dedaaf3cf2ed83bde04761670c6c67cfbdd2f5ac21ede26`) ;
  - brouillon 5 : `docs/notes/organisme-idees-juge-v1/organisme-idee-1-1-poids-du-nul-v2-brouillon5.md`
    (`3ffe1739aa83ea8de613d07855db52d16c82ad6247fca22e833ee7f6ff8305ff`) ;
  - vérification : `docs/notes/organisme-idees-juge-v1/verification-preuve-v3-et-brouillon4-idee-1-1-v1.md`
    (`b2f92646eea8a80051c798685c2ae00f013008acda26e6f214d115b0cb2705b9`), § 0 et § 4 ;
  - programme : `docs/notes/organisme-idees-juge-v1/organisme-idee-1-1-poids-du-nul-v2-outils/appliquer_couples_brouillon4_vers_5_v1.py`
    (`d1d825ad292852554fdef644d262a719c4febf8db1554116abc78b7a4e6a6600`) ;
  - pour le seul point (3) : `…/correction-poids-v1/projection/refutation-projection-v1.md` (`7bfaa88e…`), § 5, tableau des
    neuf réglages.

## Verdict

**Conforme, scellable tel quel.** Le différentiel est exactement les 20 couples du programme ; les neuf couples de [VER]
§ 4.2 et § 4.3 sont appliqués mot pour mot ; les ajouts de l'auteur ne font que durcir (un blocage de plus, une condition
de réouverture du préalable 2), sans toucher aucun critère, seuil ni plan d'analyse, et n'ouvrent aucune voie vers un signe
positif. Une remarque de forme, non bloquante, sans couple exigé (point 3).

## 1. Rejeu du programme

Copie du brouillon 4 dans un sous-dossier neuf du bloc-notes, programme lancé depuis ce sous-dossier par
`python3 -I -B <chemin du programme> "22:09"` : contrôle d'empreinte de la source passé, 20 couples appliqués, chacun trouvé
exactement une fois. Sortie **égale à l'octet** au brouillon 5 versé (`cmp` sans écart ; `3ffe1739…`).

## 2. Couples du rapport, mot pour mot

Comparaison par programme (lecture des couples du programme par arbre syntaxique, extraction des « ancien » et « nouveau » de
[VER] § 4.2 et § 4.3, espaces et retours à la ligne ramenés à une espace) : N-1, N-2, n1 (deux couples), n2, n3, n4, n5, n6 —
**neuf sur neuf identiques**, seuls les retours à la ligne diffèrent (ils suivent le texte du brouillon, comme l'annonce le
programme). n7 n'a pas de couple dans [VER] ; ses trois passages (pièces, « Réserves communes », préalable 2) sont mis à jour
et citent [VER] ; plus aucune occurrence de « pas encore vérifiée » ni « pas encore relue » dans le brouillon 5.

## 3. Ajouts de l'auteur

- **n7, par renvoi** : statut « vérifiée par un lecteur neuf, verdict « suffit » » conforme à [VER] § 0 ; « aucun énoncé de
  taille changé » et « sept mineurs de texte, non bloquants » : conformes à [VER] § 0. Pièces ajoutées [B4] et [VER] :
  empreintes exactes ; R-2938 existe au registre des décisions ; la tête `e18563f9` est un commit du dépôt.
- **Préalable 2** : « levé par ce rapport, à l'empreinte `a481c873…` de la preuve » (préfixe exact de [PREUVE3]) ; la phrase
  « toute version neuve de la preuve le rouvre » est une condition de plus, jamais une porte ; la phrase bloquante qui suit
  (« tant que cette vérification manque … pas de jeu ») et la ligne d'arrêt « préalable 1 ou 2 non levé » sont gardées.
  Elle n'est pas nommée dans l'entrée « Contre-lecture 5 » ; elle découle de n7 : sans conséquence.
- **Hn sous gel (titre et suite)** : seul changement de plan, annoncé au statut et à « Contre-lecture 5 ». Il ajoute un
  blocage (« 3 promotions ou plus sur 200 » sous gel → pas de jeu, compte à l'addendum, texte neuf) ; le compte sans garde
  reste non bloquant. Aucun seuil, aucune cellule de Holm, ni ρ, ni I, ni la principale, ni la liste d'arrêt ne changent
  (le blocage passe par la ligne existante « un essai échoue ; une mutation survit → pas de jeu », comme pour H7). R3 : il ne
  peut que rendre le jeu plus difficile.
  **Cohérence avec le cas sain de H7** : le cas sain écrit est « au plus 2 fois sur 200 » sous gel, et « un cas sain manqué
  (3 ou plus) bloque » ; le seuil de Hn, « 3 ou plus sur 200 », en est exactement le complément ; 3/200 = 0,015 reste sous
  P12 (≤ 0,02), d'où « plus dur que le jeu ». Appui exploratoire propre à la loi de Hn : témoin gelé 0/2 000 au réglage 0
  (`sans_remise` [70, 70, 70], monde uniforme) de [R-PROJ] § 5, dans le 0/13 000 cité. Cohérent.
  **Remarque, non bloquante** : « mêmes suites, que pour H7 » renvoie à un passage où les suites de H7 mêlent le cas sain
  sous gel et la survie sans garde (« moins de 20 ») ; le titre en gras exclut sans ambiguïté le blocage sans garde pour Hn,
  la lecture est donc fixée. Si l'auteur veut l'écrire, couple facultatif : « Même choix « plus dur que le jeu », mêmes suites,
  que pour H7. » → « Même choix « plus dur que le jeu », mêmes suites, que pour le cas sain de H7. »
- **En-tête, statut, « Contre-lecture 5 », « À venir »** : de forme ; le statut garde « scellé par empreinte seulement (R6) :
  il ne vaut pas préenregistrement au sens de R1 ». L'entrée « Contre-lecture 4 », historique, garde « et sans bloquer » pour
  Hn : c'est le choix du brouillon 4, corrigé par l'entrée 5 ; ne pas le réécrire.

## 4. Rien d'autre

19 blocs de `diff` (n1 (a) et (b) sur la même ligne du tableau), chacun égal à un couple ; le rejeu à l'octet l'établit.

## 5. Validateur

`controle_ia.prereg.problemes` sur le brouillon 5 : **0 problème**.

## 6. Identifiants de modèle

Recherche sur les noms de familles et de fournisseurs dans le brouillon 5, le différentiel et le programme : aucun.
