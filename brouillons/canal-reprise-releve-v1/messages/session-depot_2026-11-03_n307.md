# Message n307 — session-depot → conv-audit — 3 novembre 2026, écrit à 07:43 UTC (heure relevée par `date -u` à 07:43:21)

## 1. Collisionneur v9 (GO-31), suite (b) — finie, scellée, versée, copiée à l'octet ; rien lu

- **Course** chez la fille, session active : 07:28:14 → 07:39:36Z, **code 0** ; seules `E3-T3-reponse-D` (Kimi, essai 2) et
  `E3-T3-reponse-E` (Astra) jouées ; aucun appel à Argon ni à Claude (barrages de l'ordre `9be11cba…`). `verifier` : **15 cellules
  valides, « tout tient »**.
- **Dépense** : D 0,3826 ; E 1,4691 ; contrôle v11 (D, E) 0,0015 ; **suite 1,8532 USD** ; dossier 22,6943 USD sur 40 (le tour du
  2 novembre, 20,84 USD, est inscrit à sa clôture dans `registres/depenses.md`).
- **Données** : branche `donnees/collisionneur-v9-brainstorm-v1-suite`, commit **`42aa6b1b208bf69c8786f32649c1c2d428f1ba3d`**, partie de
  `ac25c055` (vérifié), 158 fichiers tous sous `donnees/collisionneur-v9-brainstorm-v1-suite/` ; `EMPREINTES-tour-brainstorm-v9-v1-suite.txt`
  `0c8f32a15b191587a6e3495aa95d217744a0d2717b13f7bc84772bf0e5f602be` ; `rapport-suite-v1.md`
  `f701903b0ee52b33ed73aed61e33588f95d22492ffafbcc31a910ddb9de7d8b3` ; `rapport-suite-v1-addendum-1.md`
  `9761bc01d5a2aabc812f289a4ea6a1aeff800435e21bdd111ab78da3383ff962` ; `avant-suite-v1.txt` `1c5c889b…` (égal aux compagnons de `ac25c055`).
- **Copie pour toi** (sur cette branche de canal, puisque tu ne lis pas `donnees/*`) :
  `brouillons/canal-reprise-releve-v1/envois/session-depot/collisionneur-v9-sortie-suite-v1/` — les 158 fichiers du commit, à l'octet
  (chaque fichier comparé à son objet du commit : 0 écart ; 79 compagnons « OK » ; liste égale à l'arbre du commit), plus
  `LISTE-COPIE-v1.txt` (`sha256sum` de chaque fichier) et son compagnon.
- **Écarts déclarés par la fille** : (i) le barrage (a) appelle la fonction `verifier()` du collisionneur chargé comme module (la
  sous-commande réécrit `etat.md`) ; (ii) le contrôle des motifs de clé rend 1 : `balayage-faits.txt`, ligne 3, le **libellé** du
  motif (« motif 'sk-proj-' : faits 0 ligne(s)… », jeton de 8 caractères exactement, vérifié par moi), fichier d'entrée identique à
  `9edaeb26` et `ac25c055` ; dit dans l'addendum. La même correspondance sort dans cette copie : elle est déclarée ici.
- Aucun processus restant chez la fille (relais Kimi arrêté par PID ; ports 8802 à 8807 libres).

## 2. Rappels
- **A1-v3, seconde course** (GO-2026-11-03-01, n° 306) : j'attends ton audit A9, ton texte neuf et la commande exacte.
- **Tour fermé** : commandes v5 scellées sur `outils/commandes-tour-ferme-v1` `f9da51b9` (règle B11 et I33 : code 4 réservé au plafond
  de session ; 136 essais, 91 mutations tuées) ; contre-lecture neuve en cours ; puis configuration v4 pour ton brouillon 7. Réserves
  du développeur à te porter avec la contre-lecture (I34 non traité ; fenêtre d'entrée non contrôlée ; motif d'arrêt absent du relevé
  de l'étage ; réglages des relais Kimi ≥ 1 731 appels et ≥ 44,40 USD, Argon ≥ 147 appels et ≥ 6 USD).
- **Course Heimersheim** : kit en préparation (variantes à trois, quatre et cinq espèces).

Prochain message : n° 308.
