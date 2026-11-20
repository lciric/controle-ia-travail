# Vérification des corrections du brouillon 2 de la décision de resserrement des revendications 9, 14 et 12 (b) — v1

**Verdict : conforme.** Les seize couples sont appliqués : treize sont conformes et trois s'écartent de façon acceptable. Ces trois écarts (couples 2, 4 et 6) sont exacts sur les PDF empreintés, à la page citée. Les changements faits hors des couples n'introduisent aucune erreur. Deux remarques de forme, sans effet sur la soumission, figurent au § 3.

- **Vérifié par** le même contre-lecteur, Claude Opus 5.5 (`claude-opus-5-5`), le 20 novembre 2026.
- **Pièce vérifiée** : `docs/decisions/brouillons/decision-resserrement-revendications-apres-lecture-entiere-v1-brouillon2.md` (`04873446f8edeeaab057f8b56df2701f878bfdef0fd984809f2feb3525ad2e04`). Son empreinte est contrôlée par `sha256sum -c` contre son fichier compagnon : « OK ».
- **Couples de référence** : `docs/decisions/brouillons/contre-lecture-decision-resserrement-revendications-v1.md` (`7ffc9d89844e5a9a6c19745c4cc8884c01e5165ab1afa21bdf20b303976002bc`).
- **Méthode** : texte des PDF de `docs/notes/veille-organismes-ideation-v2/pdf/` tiré par `pdftotext`, page par page. Leurs empreintes ont déjà été vérifiées lors de la contre-lecture.
- **Non ouvert** : CONFIRM ; la note d'entretien v2 et son erratum, dont j'ai seulement constaté l'existence par la liste du dossier.

## 1. Les seize couples

| Couple | Objet | Sort | Vérification |
|---|---|---|---|
| 1 | Titre et fondement : quatre travaux | conforme | Tampon d'Escher-Loop, p. 1 : « arXiv:2604.23472v2 [cs.AI] 27 May 2026 ». 21 pages selon `pdfinfo`. |
| 2 | 1.1 : coût du vote à k | écart acceptable | La p. 19 dit « For all methods the scaffold was limited to use up to 10 LLM calls per question ». La formule « pour l'échafaudage de toute méthode » est plus fidèle que ma lettre. Votes à 5 et à 10 : légende de la figure 3, p. 6. |
| 3 | 1.1 : le test A/A, pratique courante | conforme | — |
| 4 | 1.1 bis : lettre du point 9 | écart acceptable | La lettre citée en entier est identique, au mot près, à revendications-v1, point 9. Le point ajouté pour Lazar sur « coût apparié » est juste et reste au conditionnel. |
| 5 | 1.2 : ligne 6, une probabilité et non une espérance | conforme | p. 15-16. |
| 6 | 1.3 : la borne, et les deux domaines défavorables | écart acceptable | Les mots « worse chiefly due to poor performance on problem ahc039 » sont exacts (p. 9). La légende de la figure 5 dit que les deux témoins « have a higher average score » que la chaîne. Le terme de comparaison est donc bien les tirages indépendants, et le brouillon présente justement cela comme une lecture. « seemingly » est exact (légende de la figure 3, p. 6). |
| 7 | 1.4 : le jour du dépôt contre le contenu | conforme | — |
| 8 | 2.1 : les notes du juge et de la vérité approchée | conforme | p. 42-43 : « weak=… strong=… combined=… ». |
| 9 | 2.1 : la réserve dans la phrase même | conforme | — |
| 10 | 2.1 : le point sur CONFIRM | conforme | Repris à la lettre ; repris aussi au § 6, point 1. |
| 11 | § 3, constat : un modèle de base par réglage | conforme | p. 21 : « generator and guide model choices are fixed across all eight benchmarks under each backbone ». |
| 12 | 3.1 : la réserve dans la phrase même | conforme | — |
| 13 | 3.3 : ce que fait Liu et al. | conforme | La page ajoutée est exacte : Liu et al. figure à la bibliographie p. 11, AgentTTS p. 12, BAMAS p. 3 et p. 12. |
| 14 | Ne pas écrire : notices, mauvaises lectures, bruit | conforme | — |
| 15 | Ne pas écrire : revendication 14 | conforme | — |
| 16 | Ne pas écrire : revendication 12 (b) | conforme | — |

## 2. Changements faits hors des couples

Aucun n'introduit d'erreur :

- **En-tête : objet de l'accord.** L'objet cité est un extrait exact de la ligne `GO-2026-11-20-29` de `registres/go.md`, que j'ai lue.
- **En-tête : mot de Lazar.** L'extrait est exact, double espace compris.
- **Constat du § 1.** Il est corrigé comme le couple 5 et vérifié aux p. 15-16.
- **Renvoi du 2.4.** Les fichiers `note-entretien-controle-diffus-v2.md` et `-v2-erratum-1.md` existent ; je n'ai pas lu leur contenu.
- **§ 5.** L'ajout de Chen et al. 2021 aux textes non lus est exact.
- **§ 6, « Points pour Lazar ».** Tout y reste au conditionnel ; rien n'est tranché.

## 3. Remarques de forme, sans effet sur la soumission

- **Le mot de Lazar.** La ligne de l'accord rapporte un message plus long, qui commence par « À noter aussi : le papier sur le contrôle diffus […] ». Faire précéder l'extrait de « […] » serait plus exact.
- **§ 4, dernière ligne.** « tout chiffre de ces trois papiers » pourrait devenir « de ces quatre papiers » : le § 5 cite un tableau d'Escher-Loop.
