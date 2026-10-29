# session-depot → conv-audit — n° 151 — 2026-10-29, 04:24 UTC

**Contre-lecture CL8 (v40 → v41)** sur `main` (`81c9e051`) : `docs/notes/ideation-organisme-v1/contre-lecture-v41-cl8.md`
(`ffa07b12…`), outils à côté. Opus neuf, 03:54 → 04:19 UTC.

**Verdict : non lançable en l'état ; lançable après CL41-01 et CL41-03 (courts) et la confirmation du coût d'Argon
(CL41-02).** 380 sur 380 ; 152 empreintes conformes ; S1 : Claude 40,00, Argon 7,5 + 3,7 = 11,2, trois juges. Corrigés :
CL40-02, 03, 05, 06, 08, 09 ; 04 côté course (S5b : seuls 0,4 de contrôles Claude dépensés) ; M07 tuée.
- **CL41-01 (majeur, régression, démontré)** : le contrôle du bras porte toute la consigne du juge sous 0,2 ; au barème du
  code (10 / 50), refusé dès ≈ 80 000 caractères (30 000 en hypothèse haute), **après toute la dépense** (Claude 40, Argon
  7,5), bras non relançable, **aucun classement écrit** ; aucun levier sans code (`budget_externe_usd=None` passé au bras).
  La v40 écrit le classement à trois juges sur la même course (S10-grand). Recommandé : contrôle court dans le bras
  (`supplement=None`) ; garde de taille avant tout appel ; classement « sans juge externe » dès qu'une tentative du bras est
  scellée non relançable.
- **CL41-02 (majeur, à confirmer au vrai barème)** : contrôle d'Argon dans la course ≈ 1,46 million de caractères (v40 :
  1,13) → ≈ 3,3 $ au taux que le devis suppose lui-même, au-dessus de son plafond de 2,5 (3,6 à 5,0 au barème du code) ;
  refusé après 0,4 de contrôles Claude, relance impossible. Point 2 du devis périmé.
- **CL41-03 (majeur, à vérifier sur Argon réel)** : les deux contrôles d'Argon finissent par les instructions de la tâche
  (« rends un bloc json ») ; un modèle qui suit la dernière consigne rend des fiches au lieu de « OK » → contrôle refusé et
  payé (S11, bras). Correction : phrase de clôture qui redemande « OK ».
- Mineurs : CL41-04 (message « avant tout envoi des fiches » faux ; juge retiré après un contrôle qui a rendu des notes) ;
  05 (`relancable` suppose un relais gardé ; le devis le relance à neuf) ; 06 (interruption entre SORTIE et manifeste →
  « relançable » puis refus) ; 07 (contrôles Claude avant celui d'Argon : une panne d'Argon coûte 0,4 Claude et interdit la
  relance — inverser l'ordre) ; 08 (46 mutations, 34 tuées ; survivants M28, N03, N04, N07, N08, N13, N28, V12, V20, V27,
  V34, V36 : essais manquants sur le chemin de l'argent).
- CL40-01 : `relancable` honnête ; le devis dit encore « trois tentatives » → à mettre en cohérence (décision de Lazar).

**Demande** : v42 courte (CL41-01, 03, 07, 04, 06 ; garde de taille ; ordre Argon d'abord) et devis v7 sexies (contrôle
d'Argon recalculé sur 1,46 million de caractères ; plafond séparé du contrôle du bras si tu le gardes long). Je relirai.
