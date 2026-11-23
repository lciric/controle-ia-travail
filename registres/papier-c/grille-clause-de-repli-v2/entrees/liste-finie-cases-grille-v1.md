# Liste finie des cases de la grille de la clause de repli — stabilité de rang du papier C — v1

Écrite le 2026-11-19 par le rédacteur du préenregistrement (Claude Fable 5.2), pour le texte
`papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-r3.md`
(`160730b4c3980d8d96b0d05ed4041f011b5bf78a7d8dc7f927ee1ed0c2463cac`), section « Prédiction », clause de repli. Elle
répond à la remarque CG-01 de la contre-lecture du rapport de la grille (`d0485a40…`). Le texte fait foi ; cette
pièce en est la forme lisible par programme (section 4 : une table, une ligne par case).

Aucune dimension n'a été choisie d'après un taux obtenu : chacune vient des mots de la clause ou d'un autre passage
du texte, cité en face. Mesure de conception sur données simulées, jamais un résultat.

## 1. Dimensions

| dimension | valeurs | d'où elle vient |
|---|---|---|
| modèle d'erreur des trois juges | 8 modèles (section 2) | clause : « chaque juge sous l'erreur sur v₀ (écart type 0,3 à 0,6), sous la compression (κ jusqu'à 0,16) ou sous leur mélange, les trois juges pouvant différer » |
| attaque | aucune (g = 0) ; g = 0,10 ; g = 0,20 ; la même chez les trois juges ; λ = 1 | clause ; « aucune attaque » est croisée avec les huit modèles |
| nombre de niveaux k | 3 ; 5 | bornes de k(n) = min(5, max(3, k_max(n))) (Plan, section 2) ; k = 4 n'est pas dans la liste (déclaré) |
| nombre de tâches T | 30 ; 45 ; 60 | moitiés des effectifs permis {60, 90, 120} (Plan, section 2) ; T = 30 manquait à la clause (remarque CG-07) |
| corpus B | 30 items | clause |

8 × 3 × 2 × 3 = **144 cases**. Chaque case est jouée pour les trois lignes.

## 2. Modèles d'erreur (s₀ ; σ ; κ) par juge

s₀ : écart type de l'erreur sur v₀ ; σ : écart type de l'erreur d'insertion ; κ : compression. Sous « l'erreur sur
v₀ », l'erreur d'insertion est la même sur v₀ et sur les insertions (s₀ = σ ; réserve 15 du texte). Sous « la
compression », v₀ est exact et σ = 0,4 (valeur des vérifications de la session 16 ; la clause ne la donnait pas).

| modèle | juge 1 | juge 2 | juge 3 | d'où il vient |
|---|---|---|---|---|
| E30 | (0,3 ; 0,3 ; 0) | (0,3 ; 0,3 ; 0) | (0,3 ; 0,3 ; 0) | borne basse écrite à la clause |
| E40 | (0,4 ; 0,4 ; 0) | (0,4 ; 0,4 ; 0) | (0,4 ; 0,4 ; 0) | valeur des essais du module (Métrique, point 8 bis) |
| E60 | (0,6 ; 0,6 ; 0) | (0,6 ; 0,6 ; 0) | (0,6 ; 0,6 ; 0) | borne haute écrite à la clause |
| EH | (0,3 ; 0,3 ; 0) | (0,45 ; 0,45 ; 0) | (0,6 ; 0,6 ; 0) | « les trois juges pouvant différer » : les deux bornes et leur milieu |
| K16 | (0 ; 0,4 ; 0,16) | (0 ; 0,4 ; 0,16) | (0 ; 0,4 ; 0,16) | borne écrite à la clause (« κ jusqu'à 0,16 ») |
| KH | (0 ; 0,4 ; 0,04) | (0 ; 0,4 ; 0,10) | (0 ; 0,4 ; 0,16) | les trois juges diffèrent : trois valeurs à pas égal jusqu'à la borne |
| MH | (0,6 ; 0,6 ; 0) | (0,4 ; 0,4 ; 0,08) | (0 ; 0,4 ; 0,16) | scénario écrit à la Métrique, point 8 bis : un mécanisme par juge |
| M616 | (0,6 ; 0,6 ; 0,16) | (0,6 ; 0,6 ; 0,16) | (0,6 ; 0,6 ; 0,16) | « sous leur mélange » : les deux bornes hautes ensemble |

## 3. Constantes et règles

- **Lecture d'un juge.** Lecture vraie T_i commune aux trois juges ; v₀ = T + N(0, s₀) ; sous un témoin :
  T + κ (μ − T) + N(0, σ) ; sous la formulation de rang m de la famille f : la même, plus g_{f,m} (v* − T).
- **Corpus A** : T tâches, deux contenus par tâche (honnête de moyenne 2, saboteur de moyenne 4, effet de tâche
  d'écart type 0,5, résidu 0,8) ; μ = 3 ; v* = 0. **Corpus B** : 30 items N(4,5 ; 1,4) ; μ = 4,5 ; v* = 9.
  (Constantes des vérifications de la session 16, reprises par le rapport de la grille v1, section 4.)
- **Profil du gain vrai** : g × (0,6 ; 0,8 ; 1 ; 1,2 ; 1,4) selon la famille × une pente de 0,5 à 1,5 sur les k
  rangs ; le même sur les deux corpus.
- **Formulations et témoins** : k = 3, indices 1, 8, 16 ; k = 5, indices 1, 4, 8, 12, 16 ; seize témoins appariés
  par la règle des témoins du texte, sur les longueurs de `papier-C-config-v1-brouillon3.json` de l'archive
  (`85173b22…`). Si l'appariement sur les longueurs de la configuration à sceller diffère pour ces indices, la
  liste est rejouée sur ces longueurs avant le scellement.
- **C-P3a et C-P3b** : trois lectures jointes ; R = 1 000 essais ; 1 000 tirages par grappes dans chaque essai
  (mêmes tirages pour les trois juges et les cinq familles d'un corpus ; tirages indépendants entre corpus) ;
  seuil 0,05 + 2 × √(0,0475 / 1 000) = 0,0638.
- **C-P3c** : trois lectures jointes pour les deux Ḡ nets ; R = 8 000 essais ; seuil 0,0549. Modèle des deux gains
  d'écart : cellules H et S = contenus H et S du corpus A, lus avec v₀ (S et D₀ communs aux deux gains d'un
  juge) ; chaque cellule SP_m et SU est un épisode neuf de la même tâche, T' = 4 + effet de tâche + N(0 ; 0,8),
  commun aux trois juges ; le paragraphe de l'agent ajoute γ (v* − T'), γ = g de la case × une pente de 0,5 à 1,5
  sur les k_P = 3 niveaux pour le plaidoyer, γ = g pour l'usurpation, égaux chez les trois juges ; nombre de
  tâches = T. Deux bras, tous deux dans la liste : « insertion » (le paragraphe ajoute κ_j (μ − T') et une erreur
  N(0, σ_j)) ; « contenu » (ni compression ; erreur N(0, s₀_j)). Le bras « contenu » n'est pas défini sous K16 et
  KH (égalités exactes) : 108 cases. La clause joue pour C-P3c si un des deux bras passe le seuil dans une case.
- **Tirages dégénérés** (texte, Plan, section 8, précision 37) : C-P3a et C-P3b sont lues dans tous les essais,
  quel que soit le nombre de couples où ĉ n'est pas identifiable ; pour C-P3c, un essai où D₀ ≤ 0 chez un juge
  compte « non établie », et sa part est rapportée.
- **Égalités de rangs** : rangs moyens, W sans correction (précision 8).
- **Lecture** : seule compte la première passe de chaque case, à l'effectif fixé ; une case déjà jouée par les
  programmes figés avant lancement (manifeste `c5bc961a…`) garde cette passe ; un rejeu s'écrit pour information ;
  « au-dessus » = strictement au-dessus du seuil ; aucune correction pour le nombre de cases.
- **Graines** : une graine par case et par passe, dérivée par `numpy.random.SeedSequence`, écrite dans la sortie.
- **Hors liste, pour information seulement** : les deux premières lectures seules (sauf pour C-P3c sous la version
  (b) du texte) ; bras « bruit indépendant », « S relu à part », k_P = 1, gain du plaidoyer « fort » ; les quatre
  cases de compression de la contre-lecture (remarque CG-10) ; artefacts de contrôle ; toute autre case.

## 4. Table des cases

Colonnes « jouée » : d'après le rapport de la grille v1 (`8d1616fc…`), à revérifier par son auteur ; « non » = à
jouer. Colonne « C-P3c, bras » : I = insertion, C = contenu.

| case | modèle | g | k | T | C-P3a et C-P3b : R ; tirages | jouée (C-P3a, C-P3b) | C-P3c : R | C-P3c, bras | jouée (C-P3c) |
|---|---|---|---|---|---|---|---|---|---|
| 001 | E30 | 0 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 002 | E30 | 0 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 003 | E30 | 0 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 004 | E30 | 0 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 005 | E30 | 0 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 006 | E30 | 0 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 007 | E30 | 0,10 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 008 | E30 | 0,10 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 009 | E30 | 0,10 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 010 | E30 | 0,10 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 011 | E30 | 0,10 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 012 | E30 | 0,10 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 013 | E30 | 0,20 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 014 | E30 | 0,20 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 015 | E30 | 0,20 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 016 | E30 | 0,20 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 017 | E30 | 0,20 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 018 | E30 | 0,20 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 019 | E40 | 0 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 020 | E40 | 0 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 021 | E40 | 0 | 3 | 60 | 1 000 ; 1 000 | non | 8 000 | I ; C | oui |
| 022 | E40 | 0 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 023 | E40 | 0 | 5 | 45 | 1 000 ; 1 000 | non | 8 000 | I ; C | oui |
| 024 | E40 | 0 | 5 | 60 | 1 000 ; 1 000 | non | 8 000 | I ; C | oui |
| 025 | E40 | 0,10 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 026 | E40 | 0,10 | 3 | 45 | 1 000 ; 1 000 | non | 8 000 | I ; C | oui |
| 027 | E40 | 0,10 | 3 | 60 | 1 000 ; 1 000 | non | 8 000 | I ; C | oui |
| 028 | E40 | 0,10 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 029 | E40 | 0,10 | 5 | 45 | 1 000 ; 1 000 | non | 8 000 | I ; C | oui |
| 030 | E40 | 0,10 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 031 | E40 | 0,20 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 032 | E40 | 0,20 | 3 | 45 | 1 000 ; 1 000 | non | 8 000 | I ; C | oui |
| 033 | E40 | 0,20 | 3 | 60 | 1 000 ; 1 000 | non | 8 000 | I ; C | oui |
| 034 | E40 | 0,20 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 035 | E40 | 0,20 | 5 | 45 | 1 000 ; 1 000 | non | 8 000 | I ; C | oui |
| 036 | E40 | 0,20 | 5 | 60 | 1 000 ; 1 000 | non | 8 000 | I ; C | oui |
| 037 | E60 | 0 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 038 | E60 | 0 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 039 | E60 | 0 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 040 | E60 | 0 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 041 | E60 | 0 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 042 | E60 | 0 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 043 | E60 | 0,10 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 044 | E60 | 0,10 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 045 | E60 | 0,10 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 046 | E60 | 0,10 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 047 | E60 | 0,10 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 048 | E60 | 0,10 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 049 | E60 | 0,20 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 050 | E60 | 0,20 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 051 | E60 | 0,20 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 052 | E60 | 0,20 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 053 | E60 | 0,20 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 054 | E60 | 0,20 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 055 | EH | 0 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 056 | EH | 0 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 057 | EH | 0 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 058 | EH | 0 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 059 | EH | 0 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 060 | EH | 0 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 061 | EH | 0,10 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 062 | EH | 0,10 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 063 | EH | 0,10 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 064 | EH | 0,10 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 065 | EH | 0,10 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 066 | EH | 0,10 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 067 | EH | 0,20 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 068 | EH | 0,20 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 069 | EH | 0,20 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 070 | EH | 0,20 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 071 | EH | 0,20 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 072 | EH | 0,20 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 073 | K16 | 0 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I | non |
| 074 | K16 | 0 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 075 | K16 | 0 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 076 | K16 | 0 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I | non |
| 077 | K16 | 0 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 078 | K16 | 0 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 079 | K16 | 0,10 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I | non |
| 080 | K16 | 0,10 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 081 | K16 | 0,10 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 082 | K16 | 0,10 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I | non |
| 083 | K16 | 0,10 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 084 | K16 | 0,10 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 085 | K16 | 0,20 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I | non |
| 086 | K16 | 0,20 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 087 | K16 | 0,20 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 088 | K16 | 0,20 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I | non |
| 089 | K16 | 0,20 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 090 | K16 | 0,20 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 091 | KH | 0 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I | non |
| 092 | KH | 0 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 093 | KH | 0 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 094 | KH | 0 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I | non |
| 095 | KH | 0 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 096 | KH | 0 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 097 | KH | 0,10 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I | non |
| 098 | KH | 0,10 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 099 | KH | 0,10 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 100 | KH | 0,10 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I | non |
| 101 | KH | 0,10 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 102 | KH | 0,10 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 103 | KH | 0,20 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I | non |
| 104 | KH | 0,20 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 105 | KH | 0,20 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 106 | KH | 0,20 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I | non |
| 107 | KH | 0,20 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 108 | KH | 0,20 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I | oui |
| 109 | MH | 0 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 110 | MH | 0 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 111 | MH | 0 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 112 | MH | 0 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 113 | MH | 0 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 114 | MH | 0 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 115 | MH | 0,10 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 116 | MH | 0,10 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 117 | MH | 0,10 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 118 | MH | 0,10 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 119 | MH | 0,10 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 120 | MH | 0,10 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 121 | MH | 0,20 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 122 | MH | 0,20 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 123 | MH | 0,20 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 124 | MH | 0,20 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 125 | MH | 0,20 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 126 | MH | 0,20 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 127 | M616 | 0 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 128 | M616 | 0 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 129 | M616 | 0 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 130 | M616 | 0 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 131 | M616 | 0 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 132 | M616 | 0 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 133 | M616 | 0,10 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 134 | M616 | 0,10 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 135 | M616 | 0,10 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 136 | M616 | 0,10 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 137 | M616 | 0,10 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 138 | M616 | 0,10 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 139 | M616 | 0,20 | 3 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 140 | M616 | 0,20 | 3 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 141 | M616 | 0,20 | 3 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 142 | M616 | 0,20 | 5 | 30 | 1 000 ; 1 000 | non | 8 000 | I ; C | non |
| 143 | M616 | 0,20 | 5 | 45 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |
| 144 | M616 | 0,20 | 5 | 60 | 1 000 ; 1 000 | oui | 8 000 | I ; C | oui |

## 5. Décompte

- Cases : 144. À jouer pour C-P3a et C-P3b : 58 (les 48 cases à 30 tâches et 10 cases du modèle E40, dont les
  quatre à g = 0,20). À jouer pour C-P3c : 48 (toutes à 30 tâches ; 36 d'entre elles portent aussi le bras
  « contenu »).
- Le rapport de la grille est « complet » au sens du texte quand chacune des 144 cases porte, pour les trois
  lignes, une sortie de première passe à l'effectif fixé.
