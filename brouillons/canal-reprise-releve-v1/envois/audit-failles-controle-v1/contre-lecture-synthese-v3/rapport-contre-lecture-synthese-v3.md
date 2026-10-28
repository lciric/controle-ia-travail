# Contre-lecture de l'écart v2 → v3 de la synthèse de l'audit des failles — rapport — v3

Contre-lecteur : le même sous-agent (Fable 5.1 ; N-052), qui n'a écrit aucune pièce de l'audit. Écrit le 2026-10-26 à 14:27:59 UTC (heure
lue sur `date -u` dans la commande qui écrit ce fichier). Mes rapports v1 (`7b8a17c3…`) et v2 (`652a79cc…`) restent tels
quels. **Pièce confidentielle** ; aucun montant, financeur ni nom propre des rapports ici ; R-519 appliquée (aucune attaque
conçue ni étendue) ; aucun arrêt par filtre. Objet : **l'écart seulement**, `diff-v2-vers-v3.txt` (`7256ddbe…`, 226 lignes).

**Vérifications.** Compagnons de `synthese-v3/` : 4 sur 4 conformes (v3 `4f74b366…`, LISEZMOI `2ba4ee6a…`, calculs v4
`2fcbf997…` et sortie `76a4b4b6…`) ; l'écart n'a pas de compagnon (CLS3-01), son empreinte est celle annoncée. L'écart
**régénéré** par moi entre la v2 (`890130e8…`) et la v3 est **identique octet pour octet** à celui fourni : rien n'a changé
hors de lui (99 lignes ajoutées, 59 retirées ; le LISEZMOI dit 98 : CLS3-03). `calculs-synthese-v4.py` rejoué par
`python3 -I` : **sortie identique** ; ses nombres cités (0,72 à 1,45 % ; 2,09 % ; 0,73 à 1,71 % ; 9,75, 14,26, 22,62 %)
sont ceux de la sortie ; son estimateur de τ (variance des moyennes d'épisode moins variance intra sur T) est correct.
L'explication de CLS2-05 est vérifiée : `66787c14…` est l'empreinte de `provenance-voisin-panin-v1.md`, et `27f88ed7…`
celle du PDF. Confidentialité (mots de la page de titre, montants, surnom) sur l'écart, la v3 et son LISEZMOI : zéro
occurrence.

## 1. Verdict

**Transmissible.** Les douze constats CLS2 et les trois manques sont « fait » (table) ; l'écart ne porte que cela, plus
l'en-tête de version, la déclaration des calculs v4, la mise à jour de la section 9 (ajouts de la v2 désormais
contre-lus) et l'horodatage. Les deux phrases de prudence sont ramenées au niveau du détecteur. Trois constats mineurs
restent (CLS3-01 à 03), aucun ne touche le fond.

## 2. Table CLS2 → v3

| constat | verdict | ligne(s) de la v3 |
|---|---|---|
| CLS2-01 « non falsifiable » → sous-spécifiées, HR4 signe seul, HR3 signe acquis mais seuil qui peut échouer | fait | 128–132 ; 165–167 ; 1813–1815 ; 2053–2057, 2062 |
| CLS2-02 E : classe C pour le terme nouveau seulement, V_T entier garde l'ordre, « affaiblirait » retiré pour E | fait | 137–141 ; 165 ; 517–522, 530–532 ; 1232 ; 1427 ; 1815 ; 2056 |
| CLS2-03 F : HT-02 reformulée ; option (d) de D-18 avec avantage et inconvénient ; calcul v4 à τ estimé | fait | 742–746 ; 2045–2048 ; 565–567, 574–575 ; 160–161 ; 1796 |
| CLS2-04 D-19 : parades de la génération 1, pour l'essentiel du programme | fait | 2054–2055 ; 1237 |
| CLS2-05 empreinte de Panin | fait (vérifié sur disque) | 870 ; 2194 |
| CLS2-06 χ₂ différence mixte du second ordre | fait | 672–674 |
| CLS2-07 prudence : (1) RC-3.1 (e) en propriété du détecteur ; (2) HT-01 au niveau du détecteur, seul motif de HR1 | fait ; voir CLS3-02 | 517–518 ; 721–728 |
| CLS2-08 HT-09 : grappes par tâche | fait | 874–876 |
| CLS2-09 trois rapprochements marqués décoratifs | fait | 858–859 ; 1044–1045 ; 1133 |
| CLS2-10 HT-25 : bras d'attaque déclaré, sous GO | fait | 1079–1080 |
| CLS2-11 quatre PDF : provenance à compléter avant papier | fait | 2196–2197 |
| CLS2-12 « tombe sous effet épisode » | fait | 140 ; 165–166 |
| Manque 1 : multiplicité entre sondes (1 − 0,95ᵏ) dans D-07 (a) et 7.2 | fait | 1896–1898, 1900 ; 1795 |
| Manque 2 : normalisation à variance d'épisode | fait (= CLS2-03) | 2045–2048 ; 1796 |
| Manque 3 : forme du champ du coût avant le chiffre, HT-04 apparie aussi sur la forme | fait | 648–651 ; 784–785 ; 1797 |

**Prudence (R-519).** (1) l. 517–518 : « la somme cumulée n'a, par construction, aucune puissance contre une moyenne
sous κ » — propriété du détecteur, conforme. (2) HT-01, l. 721–728 : énoncé sur ce que la statistique voit et ne voit pas,
prédiction « contre le seul motif de HR1 tel que le rapport le donne (tout autre paramètre est laissé au préenregistrement
scellé) » — conforme ; rien dans l'écart ne décrit une stratégie au-delà du rapport.

## 3. Constats restants (mineurs)

- **CLS3-01** — `diff-v2-vers-v3.txt` est déposé sans compagnon `.sha256` (R6) ; en ajouter un (son empreinte, vérifiée :
  `7256ddbe…`).
- **CLS3-02** — HT-01, l. 731 : « Réfutée si : rappel de la combinée < 0,5 contre la compensation » renvoie à la famille
  retirée en l. 725–726 ; écrire « contre le motif de HR1 ».
- **CLS3-03** — LISEZMOI v3, écart 1 : « 98 lignes ajoutées » ; l'écart en compte 99 (la ligne de titre).

## 4. Hygiène

Rien lu ni écrit hors de `/var/tmp/contre-lecture-audit-synthese-v1/` et des dossiers de PDF nommés ; aucun `git`, clé,
sous-agent ni réseau ; Python avec `-I` ; `set -C` ; écriture sous `sortie/` seulement ; je n'ai pas corrigé la synthèse.

---
Horodatage : version close le 2026-10-26 à 14:27:59 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
