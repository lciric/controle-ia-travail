# Application pas à pas de la règle du gabarit (grille des gestes de rédaction des billets, section 8) à l'analyse de la moitié tenue à l'écart — v1

Écrit par le rédacteur neuf du gabarit (agent Fable 5.2 lancé par la session mère `session_013QMayjsoZJFBUCqcnvD5h1`), le 2026-11-18T22:23:16Z (heure relevée par `date -u`). Le rédacteur n'a écrit ni la grille, ni le tri, ni un codage, ni un arbitrage, ni l'analyse. Il n'a ouvert aucune copie de billet, aucun commentaire, aucun dépôt de codeur, aucun fichier d'arbitrage.

## 0. Ce qui a été lu, et comment ce fichier est fait

- Grille gelée : `docs/notes/billets-v1/grille-gestes-v1.md`, empreinte `14cf4de9429bcc08dbe88a4f76f61badbadc1b3ff234163d21f5f573f6dbf6f0` (recalculée, égale au compagnon).
- Analyse de la moitié tenue à l'écart : `docs/notes/billets-v1/analyse-tenue-v1/analyse-tenue-v1.json`, empreinte `e29c0613127feee9e26d72d664d9d21b76c9602a0bd44619eeef944d0f1c2a5e` (recalculée, égale au compagnon `analyse-tenue-v1.json.sha256`). L'analyse nomme elle-même la grille par cette empreinte (`entrees.grille.sha256`), `synthetique` = false, `numpy` = "2.4.6", `entropie` = 17963430407690202368587404665739133625 (la graine écrite en section 5.3 de la grille).
- Note de gel : `docs/notes/billets-v1/gel-grille-v1.md`, `6148b1297dfe7372430dcb5f046b4572ba3d2cdeda447b9b649b520e7f4915d5` (compagnon vérifié). Procédure de codage par lots : `docs/notes/billets-v1/procedure-codage-par-lots-v1.md`, `62c25abc805754d0bf1e08c40bf41273a7c664540c36d14c25914d33475af605` (compagnon vérifié).
- Script d'analyse en vigueur selon la note de gel : `docs/notes/billets-v1/pieces-grille-v3/analyser_codage_v4.py`, `fb77dd100c4e5c3b969fde468b3e033f124c52ed0f5b497c08f0fdb639889020` (empreinte recalculée ; script non ouvert par le rédacteur).
- Registre des décisions : lignes R-3413, R-3415, R-3419, R-3420, R-3422, R-3423, R-3425, R-3426, R-3430, R-3434, R-3441, R-3469, R-3483 de `registres/decisions.md` (celles, entre R-3413 et R-3483, qui parlent des billets).

**Méthode.** La règle de la section 8 de la grille est appliquée à la lettre, dans l'ordre de ses neuf points, le premier qui convient l'emportant. Chaque chiffre est recopié de l'analyse sans arrondi, avec sa clé exacte. Notation des clés : pour un geste, `ensembles.<ensemble>.gestes.<geste>.<clé>` ; l'ensemble est écrit entre parenthèses après la clé (`tous` : 62 billets, 23 paires ; `sans_marquage_1` : 44 billets, 13 paires ; `sans_marquage_2` : 58 billets, 20 paires ; `sans_reunion` : 42 billets, 11 paires). Pour une classe d'objection : `objections.<ensemble>.classes.<classe>.<clé>`. Les tableaux et les pas de ce fichier sont produits par un petit programme du rédacteur qui lit l'analyse et la grille (pour éviter toute faute de recopie) ; ce programme ne calcule aucune statistique : il compare les valeurs de l'analyse aux seuils écrits dans la grille.

**Contrôle croisé.** L'analyse porte déjà deux champs calculés par le script scellé : `fiabilite.<geste>.statut` et `consignes.<geste>`. L'application ci-dessous a été faite sans les lire, puis comparée : **les 25 statuts de fiabilité et les 25 qualificatifs sont identiques** (aucun écart). Le nombre de comparaisons de la correction de Holm retrouvé à la main (gestes comparés et fiables) est 17, égal à `m_comparaisons` = 17. Pour les objections, les classes retrouvées à la main sont celles dont `objections.tous.classes.<classe>.objection_a_prevenir` vaut true.

## 1. La règle, telle qu'elle est écrite (grille, sections 5.2 et 8)

- **Fiable** : `kappa_indicateur` au moins 0,60 sur les 62 billets (`tous`) **et** sur les 44 hors marquage 1 (`sans_marquage_1`).
- **Prévalence extrême** : `prevalence_indicateur` (deux codeurs réunis) au-dessus de 0,90 ou sous 0,10 **sur l'un des deux ensembles** : le geste est non évaluable ; haut : quasi universel ; bas : rare.
- Ordre des qualificatifs (le premier qui convient l'emporte) : 1. non évaluable, quasi universel → « convention du genre (fiabilité non mesurée) » si le geste est comparé, sinon rapporté seulement ; 2. non évaluable, rare, ou non fiable → exclu ; 3. descriptif → rapporté, jamais consigne ; 4. à éviter : `d` < 0 après correction de Holm sur les 23 paires ; 5. consigne distinctive : présent chez au moins la moitié des 39 bien notés, `d` ≥ 0 sur les 23 paires et sur les 11 paires hors réunion des marquages, et `d` > 0 après correction de Holm sur les 23 paires ; 6. consigne — pratique majoritaire, non contredite : présent chez au moins la moitié des 39 bien notés, `d` ≥ 0 sur les 23 paires et sur les 11 ; 7. consigne sous réserve : présent chez au moins la moitié des bien notés, `d` ≥ 0 sur les 23 paires, `d` < 0 sur les 11 ; 8. piste (jamais consigne) : présent chez moins de la moitié des bien notés, borne basse de l'intervalle non ajusté de `d` > 0 sur les 23 paires ; 9. aucune consigne : tout le reste.
- Lecture des conditions sur les clés : « présent chez au moins la moitié des 39 bien notés » → `freq_bien_notes` (tous) ≥ 0,5 ; « `d` sur les 23 paires » → `d` (tous) ; « sur les 11 » → `d` (sans_reunion) ; « après correction de Holm » → `p_holm` (tous) sous 0,05, niveau familial écrit en section 5.3 ; « intervalle non ajusté » → `ic95_d` (tous).

## 2. Fiabilité, geste par geste

| Geste | `kappa_indicateur` (tous) | `ic95_kappa_indicateur` (tous) | `kappa_indicateur` (sans_marquage_1) | `prevalence_indicateur` (tous) | `prevalence_indicateur` (sans_marquage_1) | `accord_brut_indicateur` (tous) | Statut par la règle | `fiabilite.<geste>.statut` de l'analyse |
|---|---|---|---|---|---|---|---|---|
| Forme du titre (G01) | 0.9261904761904762 | [0.8074534161490682, 1.0] | 0.8908188585607941 | 0.3225806451612903 | 0.29545454545454547 | 0.967741935483871 | fiable | fiable |
| Place de la thèse (G02) | 0.8700209643605872 | [0.6409266409266414, 1.0] | 0.8472222222222223 | 0.8548387096774194 | 0.8181818181818182 | 0.967741935483871 | fiable | fiable |
| Polarité du résultat principal (G03) | 0.9499192245557351 | [0.8287292817679559, 1.0] | 1.0 | 0.20161290322580644 | 0.22727272727272727 | 0.9838709677419355 | fiable | fiable |
| Résumé dans les 250 premiers mots (G04) | 1.0 | [1.0, 1.0] | 1.0 | 0.6935483870967742 | 0.6818181818181818 | 1.0 | fiable | fiable |
| Chiffre de résultat en tête (G05) | 0.9261904761904762 | [0.8015364916773366, 1.0] | 0.8908188585607941 | 0.3225806451612903 | 0.29545454545454547 | 0.967741935483871 | fiable | fiable |
| Statut épistémique déclaré (G06) | 1.0 | [1.0, 1.0] | 1.0 | 0.06451612903225806 | 0.06818181818181818 | 1.0 | non évaluable, rare | non-evaluable-basse |
| Caractère préliminaire annoncé (G07) | 0.7155963302752294 | [0.5040000000000001, 0.8934707903780069] | 0.6927374301675977 | 0.2661290322580645 | 0.23863636363636365 | 0.8870967741935484 | fiable | fiable |
| Rapport à un article des auteurs (G08) | 1.0 | [1.0, 1.0] | 1.0 | 0.3064516129032258 | 0.29545454545454547 | 1.0 | fiable | fiable |
| Contexte de production nommé (G09) | 1.0 | [1.0, 1.0] | 1.0 | 0.5645161290322581 | 0.5 | 1.0 | fiable | fiable |
| Enjeu de sûreté explicite (G10) | 1.0 | [1.0, 1.0] | 1.0 | 0.3870967741935484 | 0.4318181818181818 | 1.0 | fiable | fiable |
| Figure légendée de résultat en tête (G11) | 0.9378757515030061 | [0.7737226277372264, 1.0] | 0.8962264150943398 | 0.1532258064516129 | 0.125 | 0.9838709677419355 | fiable | fiable |
| Base externe de comparaison du résultat principal (G12) | 0.7789661319073081 | [0.5230769230769229, 0.9499192245557351] | 0.8472222222222223 | 0.1774193548387097 | 0.18181818181818182 | 0.9354838709677419 | fiable | fiable |
| Choix justifié contre une option écartée (G13) | 0.8079306071871127 | [0.6315007429420506, 0.9587217043941412] | 0.7924528301886792 | 0.7016129032258065 | 0.6818181818181818 | 0.9193548387096774 | fiable | fiable |
| Dispositif nommé (G14) | 0.7842227378190255 | [0.5960912052117262, 0.9280742459396752] | 0.8040089086859687 | 0.6612903225806451 | 0.6363636363636364 | 0.9032258064516129 | fiable | fiable |
| Incertitude statistique (G15) | 0.9466437177280551 | [0.8065522620904834, 1.0] | 0.9271523178807948 | 0.18548387096774194 | 0.19318181818181818 | 0.9838709677419355 | fiable | fiable |
| Non-revendications (G16) | 0.6733403582718652 | [0.4769090504807407, 0.8383817148239092] | 0.673728813559322 | 0.43548387096774194 | 0.42045454545454547 | 0.8387096774193549 | fiable | fiable |
| Limites (G17) | 0.7339055793991417 | [0.0, 1.0] | 0.6562500000000003 | 0.9354838709677419 | 0.9659090909090909 | 0.967741935483871 | non évaluable, quasi universel | non-evaluable-haute |
| Impasses rapportées (G18) | 0.769394261424017 | [0.5960912052117262, 0.903225806451613] | 0.7629310344827586 | 0.5725806451612904 | 0.6022727272727273 | 0.8870967741935484 | fiable | fiable |
| Explication concurrente anticipée (G19) | 0.7096774193548387 | [0.5220966084275436, 0.8698845750262328] | 0.683127572016461 | 0.5403225806451613 | 0.48863636363636365 | 0.8548387096774194 | fiable | fiable |
| Appel à poursuivre (G20) | 0.8530805687203791 | [0.6930693069306931, 0.9657458563535912] | 0.7924528301886792 | 0.6774193548387096 | 0.6818181818181818 | 0.9354838709677419 | fiable | fiable |
| Code, modèles et données des auteurs (G21) | 1.0 | [1.0, 1.0] | 1.0 | 0.6290322580645161 | 0.6136363636363636 | 1.0 | fiable | fiable |
| Note d'édition visible (G22) | 1.0 | [1.0, 1.0] | 1.0 | 0.22580645161290322 | 0.20454545454545456 | 1.0 | fiable | fiable |
| Analogie pour le non-spécialiste (G23) | 0.8530805687203791 | [0.6930693069306931, 0.9657458563535912] | 0.8954869358669835 | 0.3225806451612903 | 0.3181818181818182 | 0.9354838709677419 | fiable | fiable |
| Déclaration d'usage d'une intelligence artificielle dans l'écriture (G24) | 1.0 | [1.0, 1.0] | 1.0 | 0.04838709677419355 | 0.045454545454545456 | 1.0 | non évaluable, rare | non-evaluable-basse |
| Appel aux retours (G25) | 1.0 | [1.0, 1.0] | 1.0 | 0.0967741935483871 | 0.13636363636363635 | 1.0 | non évaluable, rare | non-evaluable-basse |

Bilan : 21 gestes fiables ; aucun geste non fiable ; 4 gestes non évaluables — un quasi universel (les limites, G17) et trois rares (le statut épistémique déclaré, G06 ; la déclaration d'usage d'une intelligence artificielle dans l'écriture, G24 ; l'appel aux retours, G25).

Trois remarques de lecture, sans effet sur le statut :
- **L'appel aux retours (G25)** est non évaluable par la seule prévalence sur les 62 billets, `prevalence_indicateur` (tous) = 0.0967741935483871, sous 0,10 de peu ; sur les 44 hors marquage 1 elle vaut 0.13636363636363635 et `fiabilite.G25.sans_marquage_1` = "fiable". La règle dit « sur l'un des deux ensembles » : non évaluable.
- **Les limites (G17)** : le `kappa_indicateur` (tous) = 0.7339055793991417 dépasse 0,60, mais son intervalle `ic95_kappa_indicateur` (tous) = [0.0, 1.0] couvre tout ; la règle dit qu'à prévalence extrême ni le kappa ni l'accord brut ne mesurent la fiabilité.
- Parmi les gestes fiables, la borne basse de `ic95_kappa_indicateur` (tous) est sous 0,60 pour : caractère préliminaire annoncé (G07) : 0.5040000000000001, base externe de comparaison du résultat principal (G12) : 0.5230769230769229, dispositif nommé (G14) : 0.5960912052117262, non-revendications (G16) : 0.4769090504807407, impasses rapportées (G18) : 0.5960912052117262, explication concurrente anticipée (G19) : 0.5220966084275436. La règle lit le kappa estimé, pas sa borne ; la grille (section 5.2) dit d'avance que l'intervalle est large.

## 3. Les neuf points, geste par geste

### Forme du titre (G01) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Énoncer le résultat dans le titre. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.3225806451612903 (tous), 0.29545454545454547 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 0.9261904761904762 (tous), 0.8908188585607941 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = 0.2608695652173913 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.38461538461538464 au moins 0,5 : non ; `d` (tous) = 0.2608695652173913 positif ou nul : oui ; `d` (sans_reunion) = 0.36363636363636365 positif ou nul : oui ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **non**.
- Point 7 — consigne sous réserve ? `freq_bien_notes` au moins 0,5 : non ; `d` (tous) positif ou nul : oui ; `d` (sans_reunion) = 0.36363636363636365 strictement négatif : non → **non**.
- Point 8 — piste ? `freq_bien_notes` (tous) = 0.38461538461538464 sous 0,5 : oui ; borne basse de `ic95_d` (tous) = -0.0010869565217381419 strictement positive : non → **non**.
- Point 9 — aucune consigne : tout le reste → **oui**.
- **Qualificatif : aucune consigne.** Champ `consignes.G01` de l'analyse : « aucune consigne ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.38461538461538464 / 0.2608695652173913 / 0.1875. `d` et `ic95_d` : (tous) 0.2608695652173913 [-0.0010869565217381419, 0.5217391304347826] ; (sans_marquage_1) 0.3076923076923077 [0.0, 0.6153846153846154] ; (sans_marquage_2) 0.3 [0.0, 0.6] ; (sans_reunion) 0.36363636363636365 [0.0, 0.7272727272727273]. `p_signe_exact` (tous) : 0.14599609375 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.17391304347826086, 0.6521739130434783]. Sensibilités : `d_codeur_1` (tous) = 0.30434782608695654, `d_codeur_2` (tous) = 0.21739130434782608 ; `aveugle.sensibilite_sans_reconnus.d.G01` = 0.0 (4 paires).

### Place de la thèse (G02) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Énoncer le résultat principal dans les 250 premiers mots. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.8548387096774194 (tous), 0.8181818181818182 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 0.8700209643605872 (tous), 0.8472222222222223 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = 0.043478260869565216 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.8717948717948718 au moins 0,5 : oui ; `d` (tous) = 0.043478260869565216 positif ou nul : oui ; `d` (sans_reunion) = 0.0 positif ou nul : oui ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **oui**.
- **Qualificatif : consigne — pratique majoritaire, non contredite.** Champ `consignes.G02` de l'analyse : « consigne — pratique majoritaire, non contredite ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.8717948717948718 / 0.8260869565217391 / 0.875. `d` et `ic95_d` : (tous) 0.043478260869565216 [-0.13043478260869565, 0.21739130434782608] ; (sans_marquage_1) 0.07692307692307693 [-0.15384615384615385, 0.3076923076923077] ; (sans_marquage_2) 0.0 [-0.2, 0.2] ; (sans_reunion) 0.0 [-0.2727272727272727, 0.2727272727272727]. `p_signe_exact` (tous) : 1.0 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.2608695652173913, 0.34782608695652173]. Sensibilités : `d_codeur_1` (tous) = -0.043478260869565216, `d_codeur_2` (tous) = 0.043478260869565216 ; `aveugle.sensibilite_sans_reconnus.d.G02` = -0.25 (4 paires).

### Polarité du résultat principal (G03) — analyse descriptive — fiable

La grille n'écrit pas de ligne « Consigne si retenue » (geste descriptif).

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.20161290322580644 (tous), 0.22727272727272727 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 0.9499192245557351 (tous), 1.0 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : descriptive → **oui**.
- **Qualificatif : descriptif : rapporté, jamais consigne.** Champ `consignes.G03` de l'analyse : « descriptif : jamais consigne ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.15384615384615385 / 0.2608695652173913 / 0.1875. `d` et `ic95_d` : (tous) -0.13043478260869565 [-0.391304347826087, 0.13043478260869565] ; (sans_marquage_1) -0.23076923076923078 [-0.6153846153846154, 0.15384615384615385] ; (sans_marquage_2) -0.1 [-0.35, 0.15] ; (sans_reunion) -0.18181818181818182 [-0.5454545454545454, 0.2727272727272727]. `p_signe_exact` (tous) : 0.5078125 ; `p_holm` (tous) : clé absente de l'analyse pour ce geste ; `ic_bonferroni_d` (tous) : clé absente de l'analyse pour ce geste. Sensibilités : `d_codeur_1` (tous) = -0.08695652173913043, `d_codeur_2` (tous) = -0.13043478260869565 ; `aveugle.sensibilite_sans_reconnus.d.G03` = -0.25 (4 paires).

### Résumé dans les 250 premiers mots (G04) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Ouvrir sur un résumé des résultats (bloc étiqueté ou liste) dans les 250 premiers mots. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.6935483870967742 (tous), 0.6818181818181818 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 1.0 (tous), 1.0 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = 0.0 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.6666666666666666 au moins 0,5 : oui ; `d` (tous) = 0.0 positif ou nul : oui ; `d` (sans_reunion) = 0.0 positif ou nul : oui ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **oui**.
- **Qualificatif : consigne — pratique majoritaire, non contredite.** Champ `consignes.G04` de l'analyse : « consigne — pratique majoritaire, non contredite ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.6666666666666666 / 0.7391304347826086 / 0.5625. `d` et `ic95_d` : (tous) 0.0 [-0.21739130434782608, 0.2608695652173913] ; (sans_marquage_1) 0.07692307692307693 [-0.23076923076923078, 0.38461538461538464] ; (sans_marquage_2) 0.0 [-0.25, 0.25] ; (sans_reunion) 0.0 [-0.36363636363636365, 0.36363636363636365]. `p_signe_exact` (tous) : 1.0 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.34782608695652173, 0.34782608695652173]. Sensibilités : `d_codeur_1` (tous) = 0.0, `d_codeur_2` (tous) = 0.0 ; `aveugle.sensibilite_sans_reconnus.d.G04` = 0.0 (4 paires).

### Chiffre de résultat en tête (G05) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Donner au moins un chiffre de résultat dans les 250 premiers mots. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.3225806451612903 (tous), 0.29545454545454547 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 0.9261904761904762 (tous), 0.8908188585607941 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = -0.043478260869565216 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.28205128205128205 au moins 0,5 : non ; `d` (tous) = -0.043478260869565216 positif ou nul : non ; `d` (sans_reunion) = -0.09090909090909091 positif ou nul : non ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **non**.
- Point 7 — consigne sous réserve ? `freq_bien_notes` au moins 0,5 : non ; `d` (tous) positif ou nul : non ; `d` (sans_reunion) = -0.09090909090909091 strictement négatif : oui → **non**.
- Point 8 — piste ? `freq_bien_notes` (tous) = 0.28205128205128205 sous 0,5 : oui ; borne basse de `ic95_d` (tous) = -0.30434782608695654 strictement positive : non → **non**.
- Point 9 — aucune consigne : tout le reste → **oui**.
- **Qualificatif : aucune consigne.** Champ `consignes.G05` de l'analyse : « aucune consigne ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.28205128205128205 / 0.34782608695652173 / 0.25. `d` et `ic95_d` : (tous) -0.043478260869565216 [-0.30434782608695654, 0.21739130434782608] ; (sans_marquage_1) -0.07692307692307693 [-0.38461538461538464, 0.23076923076923078] ; (sans_marquage_2) 0.0 [-0.3, 0.25] ; (sans_reunion) -0.09090909090909091 [-0.45454545454545453, 0.2727272727272727]. `p_signe_exact` (tous) : 1.0 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.43478260869565216, 0.34782608695652173]. Sensibilités : `d_codeur_1` (tous) = 0.0, `d_codeur_2` (tous) = -0.043478260869565216 ; `aveugle.sensibilite_sans_reconnus.d.G05` = -0.25 (4 paires).

### Statut épistémique déclaré (G06) — analyse comparée — non évaluable, rare

Ligne « Consigne si retenue » de la grille : « Déclarer le statut épistémique sous une étiquette, ou chiffrer ses crédences. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.06451612903225806 (tous), 0.06818181818181818 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 1.0 (tous), 1.0 (sans_marquage_1) → **oui**.
- **Qualificatif : exclu (rare, non évaluable).** Champ `consignes.G06` de l'analyse : « exclu (rare, non évaluable) ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.10256410256410256 / 0.0 / 0.125. `d` et `ic95_d` : (tous) 0.08695652173913043 [0.0, 0.21739130434782608] ; (sans_marquage_1) 0.07692307692307693 [0.0, 0.23076923076923078] ; (sans_marquage_2) 0.1 [0.0, 0.25] ; (sans_reunion) 0.09090909090909091 [0.0, 0.2727272727272727]. `p_signe_exact` (tous) : 0.5 ; `p_holm` (tous) : clé absente de l'analyse pour ce geste ; `ic_bonferroni_d` (tous) : clé absente de l'analyse pour ce geste. Sensibilités : `d_codeur_1` (tous) = 0.08695652173913043, `d_codeur_2` (tous) = 0.08695652173913043 ; `aveugle.sensibilite_sans_reconnus.d.G06` = 0.25 (4 paires).

### Caractère préliminaire annoncé (G07) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Dire franchement quand le travail est préliminaire. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.2661290322580645 (tous), 0.23863636363636365 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 0.7155963302752294 (tous), 0.6927374301675977 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = -0.043478260869565216 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.28205128205128205 au moins 0,5 : non ; `d` (tous) = -0.043478260869565216 positif ou nul : non ; `d` (sans_reunion) = -0.09090909090909091 positif ou nul : non ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **non**.
- Point 7 — consigne sous réserve ? `freq_bien_notes` au moins 0,5 : non ; `d` (tous) positif ou nul : non ; `d` (sans_reunion) = -0.09090909090909091 strictement négatif : oui → **non**.
- Point 8 — piste ? `freq_bien_notes` (tous) = 0.28205128205128205 sous 0,5 : oui ; borne basse de `ic95_d` (tous) = -0.2608695652173913 strictement positive : non → **non**.
- Point 9 — aucune consigne : tout le reste → **oui**.
- **Qualificatif : aucune consigne.** Champ `consignes.G07` de l'analyse : « aucune consigne ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.28205128205128205 / 0.30434782608695654 / 0.3125. `d` et `ic95_d` : (tous) -0.043478260869565216 [-0.2608695652173913, 0.17391304347826086] ; (sans_marquage_1) -0.07692307692307693 [-0.3076923076923077, 0.15384615384615385] ; (sans_marquage_2) -0.05 [-0.3, 0.2] ; (sans_reunion) -0.09090909090909091 [-0.36363636363636365, 0.18181818181818182]. `p_signe_exact` (tous) : 1.0 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.391304347826087, 0.30434782608695654]. Sensibilités : `d_codeur_1` (tous) = -0.043478260869565216, `d_codeur_2` (tous) = -0.08695652173913043 ; `aveugle.sensibilite_sans_reconnus.d.G07` = 0.25 (4 paires).

### Rapport à un article des auteurs (G08) — analyse descriptive — fiable

La grille n'écrit pas de ligne « Consigne si retenue » (geste descriptif).

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.3064516129032258 (tous), 0.29545454545454547 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 1.0 (tous), 1.0 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : descriptive → **oui**.
- **Qualificatif : descriptif : rapporté, jamais consigne.** Champ `consignes.G08` de l'analyse : « descriptif : jamais consigne ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.3333333333333333 / 0.2608695652173913 / 0.25. `d` et `ic95_d` : (tous) 0.13043478260869565 [-0.13043478260869565, 0.391304347826087] ; (sans_marquage_1) 0.23076923076923078 [0.0, 0.46153846153846156] ; (sans_marquage_2) 0.1 [-0.15, 0.35] ; (sans_reunion) 0.18181818181818182 [0.0, 0.45454545454545453]. `p_signe_exact` (tous) : 0.5078125 ; `p_holm` (tous) : clé absente de l'analyse pour ce geste ; `ic_bonferroni_d` (tous) : clé absente de l'analyse pour ce geste. Sensibilités : `d_codeur_1` (tous) = 0.13043478260869565, `d_codeur_2` (tous) = 0.13043478260869565 ; `aveugle.sensibilite_sans_reconnus.d.G08` = 0.0 (4 paires).

### Contexte de production nommé (G09) — analyse descriptive — fiable

La grille n'écrit pas de ligne « Consigne si retenue » (geste descriptif).

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.5645161290322581 (tous), 0.5 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 1.0 (tous), 1.0 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : descriptive → **oui**.
- **Qualificatif : descriptif : rapporté, jamais consigne.** Champ `consignes.G09` de l'analyse : « descriptif : jamais consigne ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.6666666666666666 / 0.391304347826087 / 0.6875. `d` et `ic95_d` : (tous) 0.2608695652173913 [-0.043478260869565216, 0.5652173913043478] ; (sans_marquage_1) 0.23076923076923078 [-0.15384615384615385, 0.6153846153846154] ; (sans_marquage_2) 0.35 [0.0, 0.65] ; (sans_reunion) 0.2727272727272727 [-0.18181818181818182, 0.6363636363636364]. `p_signe_exact` (tous) : 0.1795654296875 ; `p_holm` (tous) : clé absente de l'analyse pour ce geste ; `ic_bonferroni_d` (tous) : clé absente de l'analyse pour ce geste. Sensibilités : `d_codeur_1` (tous) = 0.2608695652173913, `d_codeur_2` (tous) = 0.2608695652173913 ; `aveugle.sensibilite_sans_reconnus.d.G09` = 0.75 (4 paires).

### Enjeu de sûreté explicite (G10) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Dire dans les 250 premiers mots pourquoi le résultat compte pour la sûreté. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.3870967741935484 (tous), 0.4318181818181818 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 1.0 (tous), 1.0 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = 0.0 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.358974358974359 au moins 0,5 : non ; `d` (tous) = 0.0 positif ou nul : oui ; `d` (sans_reunion) = 0.18181818181818182 positif ou nul : oui ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **non**.
- Point 7 — consigne sous réserve ? `freq_bien_notes` au moins 0,5 : non ; `d` (tous) positif ou nul : oui ; `d` (sans_reunion) = 0.18181818181818182 strictement négatif : non → **non**.
- Point 8 — piste ? `freq_bien_notes` (tous) = 0.358974358974359 sous 0,5 : oui ; borne basse de `ic95_d` (tous) = -0.30434782608695654 strictement positive : non → **non**.
- Point 9 — aucune consigne : tout le reste → **oui**.
- **Qualificatif : aucune consigne.** Champ `consignes.G10` de l'analyse : « aucune consigne ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.358974358974359 / 0.43478260869565216 / 0.25. `d` et `ic95_d` : (tous) 0.0 [-0.30434782608695654, 0.30434782608695654] ; (sans_marquage_1) 0.07692307692307693 [-0.3076923076923077, 0.46153846153846156] ; (sans_marquage_2) 0.05 [-0.3, 0.35] ; (sans_reunion) 0.18181818181818182 [-0.2727272727272727, 0.6363636363636364]. `p_signe_exact` (tous) : 1.0 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.43478260869565216, 0.43478260869565216]. Sensibilités : `d_codeur_1` (tous) = 0.0, `d_codeur_2` (tous) = 0.0 ; `aveugle.sensibilite_sans_reconnus.d.G10` = -0.75 (4 paires).

### Figure légendée de résultat en tête (G11) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Placer dans les 250 premiers mots une figure de résultat, légendée. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.1532258064516129 (tous), 0.125 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 0.9378757515030061 (tous), 0.8962264150943398 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = 0.17391304347826086 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.1794871794871795 au moins 0,5 : non ; `d` (tous) = 0.17391304347826086 positif ou nul : oui ; `d` (sans_reunion) = 0.09090909090909091 positif ou nul : oui ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **non**.
- Point 7 — consigne sous réserve ? `freq_bien_notes` au moins 0,5 : non ; `d` (tous) positif ou nul : oui ; `d` (sans_reunion) = 0.09090909090909091 strictement négatif : non → **non**.
- Point 8 — piste ? `freq_bien_notes` (tous) = 0.1794871794871795 sous 0,5 : oui ; borne basse de `ic95_d` (tous) = -0.043478260869565216 strictement positive : non → **non**.
- Point 9 — aucune consigne : tout le reste → **oui**.
- **Qualificatif : aucune consigne.** Champ `consignes.G11` de l'analyse : « aucune consigne ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.1794871794871795 / 0.13043478260869565 / 0.0. `d` et `ic95_d` : (tous) 0.17391304347826086 [-0.043478260869565216, 0.391304347826087] ; (sans_marquage_1) 0.0 [-0.3076923076923077, 0.3076923076923077] ; (sans_marquage_2) 0.25 [0.0, 0.5] ; (sans_reunion) 0.09090909090909091 [-0.18181818181818182, 0.36363636363636365]. `p_signe_exact` (tous) : 0.2890625 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.17391304347826086, 0.5217391304347826]. Sensibilités : `d_codeur_1` (tous) = 0.13043478260869565, `d_codeur_2` (tous) = 0.17391304347826086 ; `aveugle.sensibilite_sans_reconnus.d.G11` = 0.5 (4 paires).

### Base externe de comparaison du résultat principal (G12) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Comparer le résultat principal, chiffres à l'appui, à une méthode concurrente, une base naïve nommée ou un résultat antérieur. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.1774193548387097 (tous), 0.18181818181818182 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 0.7789661319073081 (tous), 0.8472222222222223 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = 0.08695652173913043 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.20512820512820512 au moins 0,5 : non ; `d` (tous) = 0.08695652173913043 positif ou nul : oui ; `d` (sans_reunion) = 0.2727272727272727 positif ou nul : oui ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **non**.
- Point 7 — consigne sous réserve ? `freq_bien_notes` au moins 0,5 : non ; `d` (tous) positif ou nul : oui ; `d` (sans_reunion) = 0.2727272727272727 strictement négatif : non → **non**.
- Point 8 — piste ? `freq_bien_notes` (tous) = 0.20512820512820512 sous 0,5 : oui ; borne basse de `ic95_d` (tous) = -0.13043478260869565 strictement positive : non → **non**.
- Point 9 — aucune consigne : tout le reste → **oui**.
- **Qualificatif : aucune consigne.** Champ `consignes.G12` de l'analyse : « aucune consigne ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.20512820512820512 / 0.13043478260869565 / 0.1875. `d` et `ic95_d` : (tous) 0.08695652173913043 [-0.13043478260869565, 0.30434782608695654] ; (sans_marquage_1) 0.23076923076923078 [0.0, 0.46153846153846156] ; (sans_marquage_2) 0.1 [-0.15, 0.35] ; (sans_reunion) 0.2727272727272727 [0.0, 0.5454545454545454]. `p_signe_exact` (tous) : 0.6875 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.21739130434782608, 0.391304347826087]. Sensibilités : `d_codeur_1` (tous) = 0.17391304347826086, `d_codeur_2` (tous) = 0.043478260869565216 ; `aveugle.sensibilite_sans_reconnus.d.G12` = -0.25 (4 paires).

### Choix justifié contre une option écartée (G13) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Justifier au moins un choix du dispositif contre une option écartée, nommée. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.7016129032258065 (tous), 0.6818181818181818 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 0.8079306071871127 (tous), 0.7924528301886792 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = 0.08695652173913043 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.7692307692307693 au moins 0,5 : oui ; `d` (tous) = 0.08695652173913043 positif ou nul : oui ; `d` (sans_reunion) = 0.18181818181818182 positif ou nul : oui ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **oui**.
- **Qualificatif : consigne — pratique majoritaire, non contredite.** Champ `consignes.G13` de l'analyse : « consigne — pratique majoritaire, non contredite ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.7692307692307693 / 0.6956521739130435 / 0.75. `d` et `ic95_d` : (tous) 0.08695652173913043 [-0.17391304347826086, 0.34782608695652173] ; (sans_marquage_1) 0.3076923076923077 [0.0, 0.6153846153846154] ; (sans_marquage_2) 0.0 [-0.3, 0.25] ; (sans_reunion) 0.18181818181818182 [-0.18181818181818182, 0.5454545454545454]. `p_signe_exact` (tous) : 0.75390625 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.30434782608695654, 0.4782608695652174]. Sensibilités : `d_codeur_1` (tous) = 0.0, `d_codeur_2` (tous) = 0.08695652173913043 ; `aveugle.sensibilite_sans_reconnus.d.G13` = 0.25 (4 paires).

### Dispositif nommé (G14) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Nommer dans le billet le modèle, les données et l'effectif de l'expérience principale. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.6612903225806451 (tous), 0.6363636363636364 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 0.7842227378190255 (tous), 0.8040089086859687 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = 0.08695652173913043 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.6666666666666666 au moins 0,5 : oui ; `d` (tous) = 0.08695652173913043 positif ou nul : oui ; `d` (sans_reunion) = 0.09090909090909091 positif ou nul : oui ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **oui**.
- **Qualificatif : consigne — pratique majoritaire, non contredite.** Champ `consignes.G14` de l'analyse : « consigne — pratique majoritaire, non contredite ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.6666666666666666 / 0.6521739130434783 / 0.5625. `d` et `ic95_d` : (tous) 0.08695652173913043 [-0.13043478260869565, 0.30434782608695654] ; (sans_marquage_1) 0.0 [-0.38461538461538464, 0.38461538461538464] ; (sans_marquage_2) 0.1 [-0.15, 0.35] ; (sans_reunion) 0.09090909090909091 [-0.2727272727272727, 0.45454545454545453]. `p_signe_exact` (tous) : 0.7265625 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.2737212276214834, 0.43478260869565216]. Sensibilités : `d_codeur_1` (tous) = 0.043478260869565216, `d_codeur_2` (tous) = 0.13043478260869565 ; `aveugle.sensibilite_sans_reconnus.d.G14` = 0.0 (4 paires).

### Incertitude statistique (G15) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Donner l'incertitude des chiffres : intervalle, barres d'erreur dites dans le texte, ou test. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.18548387096774194 (tous), 0.19318181818181818 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 0.9466437177280551 (tous), 0.9271523178807948 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = -0.21739130434782608 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.10256410256410256 au moins 0,5 : non ; `d` (tous) = -0.21739130434782608 positif ou nul : non ; `d` (sans_reunion) = -0.09090909090909091 positif ou nul : non ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **non**.
- Point 7 — consigne sous réserve ? `freq_bien_notes` au moins 0,5 : non ; `d` (tous) positif ou nul : non ; `d` (sans_reunion) = -0.09090909090909091 strictement négatif : oui → **non**.
- Point 8 — piste ? `freq_bien_notes` (tous) = 0.10256410256410256 sous 0,5 : oui ; borne basse de `ic95_d` (tous) = -0.43478260869565216 strictement positive : non → **non**.
- Point 9 — aucune consigne : tout le reste → **oui**.
- **Qualificatif : aucune consigne.** Champ `consignes.G15` de l'analyse : « aucune consigne ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.10256410256410256 / 0.34782608695652173 / 0.0625. `d` et `ic95_d` : (tous) -0.21739130434782608 [-0.43478260869565216, -0.042391304347841906] ; (sans_marquage_1) -0.07692307692307693 [-0.3076923076923077, 0.15384615384615385] ; (sans_marquage_2) -0.25 [-0.5, 0.0] ; (sans_reunion) -0.09090909090909091 [-0.36363636363636365, 0.18181818181818182]. `p_signe_exact` (tous) : 0.125 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.5217391304347826, 0.08695652173913043]. Sensibilités : `d_codeur_1` (tous) = -0.17391304347826086, `d_codeur_2` (tous) = -0.21739130434782608 ; `aveugle.sensibilite_sans_reconnus.d.G15` = 0.0 (4 paires).

### Non-revendications (G16) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Dire en toutes lettres ce que le travail ne montre pas. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.43548387096774194 (tous), 0.42045454545454547 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 0.6733403582718652 (tous), 0.673728813559322 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = 0.08695652173913043 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.46153846153846156 au moins 0,5 : non ; `d` (tous) = 0.08695652173913043 positif ou nul : oui ; `d` (sans_reunion) = 0.18181818181818182 positif ou nul : oui ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **non**.
- Point 7 — consigne sous réserve ? `freq_bien_notes` au moins 0,5 : non ; `d` (tous) positif ou nul : oui ; `d` (sans_reunion) = 0.18181818181818182 strictement négatif : non → **non**.
- Point 8 — piste ? `freq_bien_notes` (tous) = 0.46153846153846156 sous 0,5 : oui ; borne basse de `ic95_d` (tous) = -0.21739130434782608 strictement positive : non → **non**.
- Point 9 — aucune consigne : tout le reste → **oui**.
- **Qualificatif : aucune consigne.** Champ `consignes.G16` de l'analyse : « aucune consigne ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.46153846153846156 / 0.391304347826087 / 0.4375. `d` et `ic95_d` : (tous) 0.08695652173913043 [-0.21739130434782608, 0.391304347826087] ; (sans_marquage_1) 0.07692307692307693 [-0.15384615384615385, 0.3076923076923077] ; (sans_marquage_2) 0.2 [-0.1, 0.5] ; (sans_reunion) 0.18181818181818182 [0.0, 0.45454545454545453]. `p_signe_exact` (tous) : 0.7744140625 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.391304347826087, 0.5217391304347826]. Sensibilités : `d_codeur_1` (tous) = 0.08695652173913043, `d_codeur_2` (tous) = 0.0 ; `aveugle.sensibilite_sans_reconnus.d.G16` = 0.0 (4 paires).

### Limites (G17) — analyse comparée — non évaluable, quasi universel

Ligne « Consigne si retenue » de la grille : « Énoncer les limites du dispositif, de préférence dans une section titrée. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.9354838709677419 (tous), 0.9659090909090909 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **oui**.
- **Qualificatif : convention du genre (fiabilité non mesurée).** Champ `consignes.G17` de l'analyse : « convention du genre (fiabilité non mesurée) ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.9230769230769231 / 0.9565217391304348 / 0.9375. `d` et `ic95_d` : (tous) -0.043478260869565216 [-0.21739130434782608, 0.08695652173913043] ; (sans_marquage_1) -0.07692307692307693 [-0.23076923076923078, 0.0] ; (sans_marquage_2) -0.05 [-0.25, 0.1] ; (sans_reunion) -0.09090909090909091 [-0.2727272727272727, 0.0]. `p_signe_exact` (tous) : 1.0 ; `p_holm` (tous) : clé absente de l'analyse pour ce geste ; `ic_bonferroni_d` (tous) : clé absente de l'analyse pour ce geste. Sensibilités : `d_codeur_1` (tous) = -0.043478260869565216, `d_codeur_2` (tous) = -0.043478260869565216 ; `aveugle.sensibilite_sans_reconnus.d.G17` = -0.25 (4 paires).

### Impasses rapportées (G18) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Rapporter aussi ce qui n'a pas marché. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.5725806451612904 (tous), 0.6022727272727273 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 0.769394261424017 (tous), 0.7629310344827586 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = -0.13043478260869565 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.5128205128205128 au moins 0,5 : oui ; `d` (tous) = -0.13043478260869565 positif ou nul : non ; `d` (sans_reunion) = -0.36363636363636365 positif ou nul : non ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **non**.
- Point 7 — consigne sous réserve ? `freq_bien_notes` au moins 0,5 : oui ; `d` (tous) positif ou nul : non ; `d` (sans_reunion) = -0.36363636363636365 strictement négatif : oui → **non**.
- Point 8 — piste ? `freq_bien_notes` (tous) = 0.5128205128205128 sous 0,5 : non ; borne basse de `ic95_d` (tous) = -0.43478260869565216 strictement positive : non → **non**.
- Point 9 — aucune consigne : tout le reste → **oui**.
- **Qualificatif : aucune consigne.** Champ `consignes.G18` de l'analyse : « aucune consigne ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.5128205128205128 / 0.6521739130434783 / 0.5. `d` et `ic95_d` : (tous) -0.13043478260869565 [-0.43478260869565216, 0.21739130434782608] ; (sans_marquage_1) -0.3076923076923077 [-0.6923076923076923, 0.07692307692307693] ; (sans_marquage_2) -0.15 [-0.5, 0.2] ; (sans_reunion) -0.36363636363636365 [-0.7272727272727273, 0.0]. `p_signe_exact` (tous) : 0.60723876953125 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.6086956521739131, 0.34782608695652173]. Sensibilités : `d_codeur_1` (tous) = -0.08695652173913043, `d_codeur_2` (tous) = -0.13043478260869565 ; `aveugle.sensibilite_sans_reconnus.d.G18` = 0.25 (4 paires).

### Explication concurrente anticipée (G19) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Nommer une autre cause possible du résultat et la contrôler par une expérience. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.5403225806451613 (tous), 0.48863636363636365 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 0.7096774193548387 (tous), 0.683127572016461 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = 0.0 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.5897435897435898 au moins 0,5 : oui ; `d` (tous) = 0.0 positif ou nul : oui ; `d` (sans_reunion) = -0.09090909090909091 positif ou nul : non ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **non**.
- Point 7 — consigne sous réserve ? `freq_bien_notes` au moins 0,5 : oui ; `d` (tous) positif ou nul : oui ; `d` (sans_reunion) = -0.09090909090909091 strictement négatif : oui → **oui**.
- **Qualificatif : consigne sous réserve.** Champ `consignes.G19` de l'analyse : « consigne sous réserve ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.5897435897435898 / 0.6086956521739131 / 0.5625. `d` et `ic95_d` : (tous) 0.0 [-0.2608695652173913, 0.21847826086954938] ; (sans_marquage_1) -0.07692307692307693 [-0.3076923076923077, 0.15384615384615385] ; (sans_marquage_2) 0.05 [-0.2, 0.3] ; (sans_reunion) -0.09090909090909091 [-0.36363636363636365, 0.18181818181818182]. `p_signe_exact` (tous) : 1.0 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.34782608695652173, 0.34782608695652173]. Sensibilités : `d_codeur_1` (tous) = -0.08695652173913043, `d_codeur_2` (tous) = -0.043478260869565216 ; `aveugle.sensibilite_sans_reconnus.d.G19` = -0.25 (4 paires).

### Appel à poursuivre (G20) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Inviter les lecteurs à poursuivre : questions ouvertes ou projets proposés. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.6774193548387096 (tous), 0.6818181818181818 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 0.8530805687203791 (tous), 0.7924528301886792 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = 0.0 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.717948717948718 au moins 0,5 : oui ; `d` (tous) = 0.0 positif ou nul : oui ; `d` (sans_reunion) = -0.09090909090909091 positif ou nul : non ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **non**.
- Point 7 — consigne sous réserve ? `freq_bien_notes` au moins 0,5 : oui ; `d` (tous) positif ou nul : oui ; `d` (sans_reunion) = -0.09090909090909091 strictement négatif : oui → **oui**.
- **Qualificatif : consigne sous réserve.** Champ `consignes.G20` de l'analyse : « consigne sous réserve ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.717948717948718 / 0.6956521739130435 / 0.75. `d` et `ic95_d` : (tous) 0.0 [-0.21739130434782608, 0.2608695652173913] ; (sans_marquage_1) -0.07692307692307693 [-0.46153846153846156, 0.3076923076923077] ; (sans_marquage_2) 0.0 [-0.25, 0.25] ; (sans_reunion) -0.09090909090909091 [-0.45454545454545453, 0.2727272727272727]. `p_signe_exact` (tous) : 1.0 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.34782608695652173, 0.34782608695652173]. Sensibilités : `d_codeur_1` (tous) = -0.043478260869565216, `d_codeur_2` (tous) = 0.0 ; `aveugle.sensibilite_sans_reconnus.d.G20` = -0.25 (4 paires).

### Code, modèles et données des auteurs (G21) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Donner un lien vers le code, les modèles ou les données. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.6290322580645161 (tous), 0.6136363636363636 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 1.0 (tous), 1.0 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = 0.0 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.6153846153846154 au moins 0,5 : oui ; `d` (tous) = 0.0 positif ou nul : oui ; `d` (sans_reunion) = -0.09090909090909091 positif ou nul : non ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **non**.
- Point 7 — consigne sous réserve ? `freq_bien_notes` au moins 0,5 : oui ; `d` (tous) positif ou nul : oui ; `d` (sans_reunion) = -0.09090909090909091 strictement négatif : oui → **oui**.
- **Qualificatif : consigne sous réserve.** Champ `consignes.G21` de l'analyse : « consigne sous réserve ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.6153846153846154 / 0.6521739130434783 / 0.5625. `d` et `ic95_d` : (tous) 0.0 [-0.30434782608695654, 0.30434782608695654] ; (sans_marquage_1) -0.23076923076923078 [-0.6153846153846154, 0.15384615384615385] ; (sans_marquage_2) 0.1 [-0.2, 0.4] ; (sans_reunion) -0.09090909090909091 [-0.45454545454545453, 0.2727272727272727]. `p_signe_exact` (tous) : 1.0 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.43478260869565216, 0.43478260869565216]. Sensibilités : `d_codeur_1` (tous) = 0.0, `d_codeur_2` (tous) = 0.0 ; `aveugle.sensibilite_sans_reconnus.d.G21` = 0.25 (4 paires).

### Note d'édition visible (G22) — analyse descriptive — fiable

La grille n'écrit pas de ligne « Consigne si retenue » (geste descriptif).

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.22580645161290322 (tous), 0.20454545454545456 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 1.0 (tous), 1.0 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : descriptive → **oui**.
- **Qualificatif : descriptif : rapporté, jamais consigne.** Champ `consignes.G22` de l'analyse : « descriptif : jamais consigne ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.3076923076923077 / 0.08695652173913043 / 0.3125. `d` et `ic95_d` : (tous) 0.21739130434782608 [0.0, 0.43478260869565216] ; (sans_marquage_1) 0.07692307692307693 [-0.15384615384615385, 0.3076923076923077] ; (sans_marquage_2) 0.2 [0.0, 0.45] ; (sans_reunion) 0.09090909090909091 [-0.18181818181818182, 0.36363636363636365]. `p_signe_exact` (tous) : 0.125 ; `p_holm` (tous) : clé absente de l'analyse pour ce geste ; `ic_bonferroni_d` (tous) : clé absente de l'analyse pour ce geste. Sensibilités : `d_codeur_1` (tous) = 0.21739130434782608, `d_codeur_2` (tous) = 0.21739130434782608 ; `aveugle.sensibilite_sans_reconnus.d.G22` = 0.25 (4 paires).

### Analogie pour le non-spécialiste (G23) — analyse comparée — fiable

Ligne « Consigne si retenue » de la grille : « Éclairer le mécanisme ou le résultat par une analogie hors du sous-domaine. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.3225806451612903 (tous), 0.3181818181818182 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 0.8530805687203791 (tous), 0.8954869358669835 (sans_marquage_1) → **non**.
- Point 3 — descriptif ? ligne « Analyse » de la grille : comparée → **non**.
- Point 4 — à éviter ? `d` (tous) = -0.043478260869565216 strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non**.
- Point 5 — consigne distinctive ? `freq_bien_notes` (tous) = 0.3333333333333333 au moins 0,5 : non ; `d` (tous) = -0.043478260869565216 positif ou nul : non ; `d` (sans_reunion) = -0.36363636363636365 positif ou nul : non ; `d` (tous) strictement positif et `p_holm` (tous) = 1.0 sous 0,05 : non → **non**.
- Point 6 — pratique majoritaire, non contredite ? les trois premières conditions du point 5 (mêmes valeurs) → **non**.
- Point 7 — consigne sous réserve ? `freq_bien_notes` au moins 0,5 : non ; `d` (tous) positif ou nul : non ; `d` (sans_reunion) = -0.36363636363636365 strictement négatif : oui → **non**.
- Point 8 — piste ? `freq_bien_notes` (tous) = 0.3333333333333333 sous 0,5 : oui ; borne basse de `ic95_d` (tous) = -0.34782608695652173 strictement positive : non → **non**.
- Point 9 — aucune consigne : tout le reste → **oui**.
- **Qualificatif : aucune consigne.** Champ `consignes.G23` de l'analyse : « aucune consigne ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.3333333333333333 / 0.34782608695652173 / 0.375. `d` et `ic95_d` : (tous) -0.043478260869565216 [-0.34782608695652173, 0.21739130434782608] ; (sans_marquage_1) -0.23076923076923078 [-0.6153846153846154, 0.15384615384615385] ; (sans_marquage_2) -0.1 [-0.4, 0.2] ; (sans_reunion) -0.36363636363636365 [-0.7272727272727273, 0.0]. `p_signe_exact` (tous) : 1.0 ; `p_holm` (tous) : 1.0 ; `ic_bonferroni_d` (tous) : [-0.4782608695652174, 0.36067774936062685]. Sensibilités : `d_codeur_1` (tous) = 0.0, `d_codeur_2` (tous) = -0.043478260869565216 ; `aveugle.sensibilite_sans_reconnus.d.G23` = 0.0 (4 paires).

### Déclaration d'usage d'une intelligence artificielle dans l'écriture (G24) — analyse descriptive — non évaluable, rare

La grille n'écrit pas de ligne « Consigne si retenue » (geste descriptif).

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.04838709677419355 (tous), 0.045454545454545456 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 1.0 (tous), 1.0 (sans_marquage_1) → **oui**.
- **Qualificatif : exclu (rare, non évaluable).** Champ `consignes.G24` de l'analyse : « exclu (rare, non évaluable) ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.02564102564102564 / 0.08695652173913043 / 0.0625. `d` et `ic95_d` : (tous) -0.08695652173913043 [-0.21739130434782608, 0.0] ; (sans_marquage_1) -0.07692307692307693 [-0.23076923076923078, 0.0] ; (sans_marquage_2) -0.1 [-0.25, 0.0] ; (sans_reunion) -0.09090909090909091 [-0.2727272727272727, 0.0]. `p_signe_exact` (tous) : 0.5 ; `p_holm` (tous) : clé absente de l'analyse pour ce geste ; `ic_bonferroni_d` (tous) : clé absente de l'analyse pour ce geste. Sensibilités : `d_codeur_1` (tous) = -0.08695652173913043, `d_codeur_2` (tous) = -0.08695652173913043 ; `aveugle.sensibilite_sans_reconnus.d.G24` = -0.5 (4 paires).

### Appel aux retours (G25) — analyse comparée — non évaluable, rare

Ligne « Consigne si retenue » de la grille : « Demander explicitement critiques et corrections. »

- Point 1 — non évaluable, quasi universel ? `prevalence_indicateur` = 0.0967741935483871 (tous), 0.13636363636363635 (sans_marquage_1) ; seuil : plus de 0,90 sur l'un des deux → **non**.
- Point 2 — non évaluable, rare (prévalence sous 0,10 sur l'un des deux ensembles) ou non fiable (`kappa_indicateur` sous 0,60 sur l'un des deux) ? `prevalence_indicateur` ci-dessus ; `kappa_indicateur` = 1.0 (tous), 1.0 (sans_marquage_1) → **oui**.
- **Qualificatif : exclu (rare, non évaluable).** Champ `consignes.G25` de l'analyse : « exclu (rare, non évaluable) ».
- Chiffres rapportés. `freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` (tous) : 0.10256410256410256 / 0.08695652173913043 / 0.125. `d` et `ic95_d` : (tous) 0.0 [-0.17391304347826086, 0.17391304347826086] ; (sans_marquage_1) 0.0 [-0.3076923076923077, 0.3076923076923077] ; (sans_marquage_2) -0.05 [-0.2, 0.1] ; (sans_reunion) -0.09090909090909091 [-0.36363636363636365, 0.18181818181818182]. `p_signe_exact` (tous) : 1.0 ; `p_holm` (tous) : clé absente de l'analyse pour ce geste ; `ic_bonferroni_d` (tous) : clé absente de l'analyse pour ce geste. Sensibilités : `d_codeur_1` (tous) = 0.0, `d_codeur_2` (tous) = 0.0 ; `aveugle.sensibilite_sans_reconnus.d.G25` = 0.0 (4 paires).

## 4. Bilan des gestes

| Qualificatif | Gestes |
|---|---|
| convention du genre (fiabilité non mesurée) | Limites (G17) |
| exclu (rare, non évaluable) | Statut épistémique déclaré (G06) ; Déclaration d'usage d'une intelligence artificielle dans l'écriture (G24) ; Appel aux retours (G25) |
| exclu (non fiable) | aucun |
| descriptif : rapporté, jamais consigne | Polarité du résultat principal (G03) ; Rapport à un article des auteurs (G08) ; Contexte de production nommé (G09) ; Note d'édition visible (G22) |
| à éviter | aucun |
| consigne distinctive | aucun |
| consigne — pratique majoritaire, non contredite | Place de la thèse (G02) ; Résumé dans les 250 premiers mots (G04) ; Choix justifié contre une option écartée (G13) ; Dispositif nommé (G14) |
| consigne sous réserve | Explication concurrente anticipée (G19) ; Appel à poursuivre (G20) ; Code, modèles et données des auteurs (G21) |
| piste (jamais consigne) | aucun |
| aucune consigne | Forme du titre (G01) ; Chiffre de résultat en tête (G05) ; Caractère préliminaire annoncé (G07) ; Enjeu de sûreté explicite (G10) ; Figure légendée de résultat en tête (G11) ; Base externe de comparaison du résultat principal (G12) ; Incertitude statistique (G15) ; Non-revendications (G16) ; Impasses rapportées (G18) ; Analogie pour le non-spécialiste (G23) |

Aucun geste n'est « à éviter », aucun n'est « consigne distinctive », aucun n'est « piste ». **Aucune consigne du gabarit ne dit donc qu'un geste distingue les billets bien notés.**

Quatre cas à signaler parce qu'ils sont près d'une frontière ou qu'ils paraissent nets (règle de symétrie du dépôt, R4), sans que la règle en soit changée :
- **La forme du titre (G01)** : `freq_bien_notes` (tous) = 0.38461538461538464, sous la moitié ; borne basse de `ic95_d` (tous) = -0.0010869565217381419, négative de très peu : pas « piste ». `d` (tous) = 0.2608695652173913, `p_signe_exact` (tous) = 0.14599609375, `p_holm` (tous) = 1.0.
- **L'incertitude statistique (G15)** : `d` (tous) = -0.21739130434782608, `ic95_d` (tous) = [-0.43478260869565216, -0.042391304347841906], tout entier négatif, mais `p_signe_exact` (tous) = 0.125 et `p_holm` (tous) = 1.0 : pas « à éviter » ; « aucune consigne ». `freq_bien_notes` (tous) = 0.10256410256410256 contre `freq_apparies` (tous) = 0.34782608695652173. La grille (section 5.5) dit que l'incertitude est mesurée sur le texte, sans les images, donc sous-estimée.
- **Les impasses rapportées (G18)** : `freq_bien_notes` (tous) = 0.5128205128205128, au-dessus de la moitié de peu (20 billets sur 39 donnent cette valeur), mais `d` (tous) = -0.13043478260869565 est négatif : ni le point 5, ni le 6, ni le 7 ; pas le point 8 (fréquence au moins égale à la moitié) ; « aucune consigne ».
- **Trois consignes « sous réserve » dont `d` (tous) vaut exactement 0** : l'explication concurrente anticipée (G19), l'appel à poursuivre (G20), le code, les modèles et les données (G21). La règle écrit `d` ≥ 0 : zéro convient. Pour les deux premières, les deux codeurs pris seuls donnent une différence négative ou nulle (`d_codeur_1`, `d_codeur_2`, section 3).

## 5. Objections à prévenir (grille, sections 5.2, 5.4 et 8)

Règle : classe qui n'est ni O0, ni O12, ni O13 ; fiable (`kappa_binaire` ≥ 0,60, prévalence non extrême) ; au moins 10 % des commentaires codables (`part` ≥ 0,10) ; au moins un quart des 39 bien notés touchés (`part_des_bien_notes_touches` ≥ 0,25) ; sur l'ensemble « tous ». `objections.tous.commentaires_codables` = 238 ; `objections.tous.accord_brut_classe` = 0.8529411764705882 ; `objections.tous.kappa_classe` = 0.8285302593659943.

| Classe | `kappa_binaire` (tous) | `accord_brut` (tous) | `prevalence` (tous) | Fiabilité par la règle | `part` (tous) | `ic95_part` (tous) | `part_des_bien_notes_touches` (tous) | Hors typologie ou signal favorable | À prévenir par la règle | `objection_a_prevenir` (tous) |
|---|---|---|---|---|---|---|---|---|---|---|
| Hors typologie (O0) | 0.8753689422069886 | 0.9537815126050421 | 0.24579831932773108 | fiable | 0.25630252100840334 | [0.19313304721030042, 0.3288303303303303] | 0.8205128205128205 | oui | non | false |
| Explication concurrente du résultat (O1) | 0.82450965934228 | 0.957983193277311 | 0.13865546218487396 | fiable | 0.13445378151260504 | [0.09163346613545817, 0.1810344827586207] | 0.5384615384615384 | non | **oui** | true |
| La mesure ne mesure pas le concept revendiqué (O2) | 0.8284478616049975 | 0.9747899159663865 | 0.07983193277310924 | non évaluable (prévalence extrême) | 0.08403361344537816 | [0.050907550077041605, 0.12184873949579832] | 0.41025641025641024 | non | non | false |
| Exactitude d'un chiffre, d'un calcul ou du code (O3) | 0.7466737626397021 | 0.9663865546218487 | 0.07142857142857142 | non évaluable (prévalence extrême) | 0.06302521008403361 | [0.02586206896551724, 0.10909090909090909] | 0.2564102564102564 | non | non | false |
| Antériorité, travaux et techniques voisins (O4) | 0.9217191097467382 | 0.9747899159663865 | 0.20168067226890757 | fiable | 0.19747899159663865 | [0.1417910447761194, 0.2530612244897959] | 0.5641025641025641 | non | **oui** | true |
| Cadrage surdimensionné ou mal hiérarchisé (O5) | 0.3248226950354547 | 0.9831932773109243 | 0.012605042016806723 | non évaluable (prévalence extrême) | 0.01680672268907563 | [0.003936621892851629, 0.034482758620689655] | 0.10256410256410256 | non | non | false |
| Pertinence ou effet pour le risque (O6) | 0.5914163090128753 | 0.9831932773109243 | 0.02100840336134454 | non évaluable (prévalence extrême) | 0.01680672268907563 | [0.0, 0.03862660944206009] | 0.07692307692307693 | non | non | false |
| Généralisation hors du cadre étudié (O7) | 0.8506900878293608 | 0.9873949579831933 | 0.04411764705882353 | non évaluable (prévalence extrême) | 0.046218487394957986 | [0.020242914979757085, 0.07755102040816327] | 0.23076923076923078 | non | non | false |
| Coût caché ou effet secondaire de la méthode (O8) | 0.7459978655282826 | 0.9915966386554622 | 0.01680672268907563 | non évaluable (prévalence extrême) | 0.02100840336134454 | [0.0, 0.04897959183673469] | 0.07692307692307693 | non | non | false |
| Expérience suivante proposée (O9) | 0.7949790794979078 | 0.9705882352941176 | 0.07773109243697479 | non évaluable (prévalence extrême) | 0.07563025210084033 | [0.037310829573064905, 0.11628157578187646] | 0.28205128205128205 | non | non | false |
| Critique de la forme et de la présentation (O10) | 1.0 | 1.0 | 0.012605042016806723 | non évaluable (prévalence extrême) | 0.012605042016806723 | [0.0, 0.027559055118110236] | 0.07692307692307693 | non | non | false |
| Demande de précision ou de matériel (O11) | 0.6562680531484688 | 0.9789915966386554 | 0.031512605042016806 | non évaluable (prévalence extrême) | 0.029411764705882353 | [0.01195219123505976, 0.05063291139240506] | 0.1794871794871795 | non | non | false |
| Réplication ou prolongement par le lecteur (O12) | 0.9069585613760756 | 0.9957983193277311 | 0.023109243697478993 | non évaluable (prévalence extrême) | 0.02100840336134454 | [0.00411522633744856, 0.04329004329004329] | 0.10256410256410256 | oui | non | false |
| Éloge argumenté (classe nouvelle au brouillon 3) (O13) | 0.7208756841282266 | 0.9873949579831933 | 0.023109243697478993 | non évaluable (prévalence extrême) | 0.025210084033613446 | [0.008298755186721992, 0.04602510460251046] | 0.15384615384615385 | oui | non | false |

**Retenues : Explication concurrente du résultat (O1) ; Antériorité, travaux et techniques voisins (O4).** Toutes les autres classes hors O0 ont une `prevalence` (tous) sous 0,10 : elles sont non évaluables par la règle de prévalence extrême, et leur `part` (tous) est aussi sous 0,10. Parmi elles, deux ont en plus un `kappa_binaire` (tous) sous 0,60 : le cadrage surdimensionné ou mal hiérarchisé (O5), 0.3248226950354547, et la pertinence ou l'effet pour le risque (O6), 0.5914163090128753.

Sur les trois autres ensembles (rapportés, sans effet sur la règle, qui lit « tous ») : les deux classes retenues le sont aussi partout (`objection_a_prevenir` = true sur `sans_marquage_1`, `sans_marquage_2`, `sans_reunion`). **La mesure qui ne mesure pas le concept revendiqué (O2)** porte `objection_a_prevenir` = true sur `sans_marquage_1` et `sans_reunion` (`part` = 0.1111111111111111, `prevalence` = 0.10130718954248366, `kappa_binaire` = 0.8207171314741036, `part_des_bien_notes_touches` = 0.5 ; mêmes valeurs sur `sans_reunion`, 153 commentaires codables dans les deux cas) mais false sur « tous » (`part` = 0.08403361344537816, `prevalence` = 0.07983193277310924) : par la règle, elle n'est **pas** retenue.

## 6. Mesure de l'aveugle (rapportée ; aucun point de la section 8 ne la lit)

- `aveugle.codeur_1` : `paris` = 41, `part_juste` = 0.9512195121951219, `ic95` = [0.8780487804878049, 1.0], `reconnus` = 31.
- `aveugle.codeur_2` : `paris` = 57, `part_juste` = 0.9122807017543859, `ic95` = [0.8245614035087719, 0.9824561403508771], `reconnus` = 40.
- `aveugle.sensibilite_sans_reconnus` : `billets` = 21, `paires` = 4 ; les `d` par geste sont en section 3.
- `aveugle.description_sans_reconnus_ni_devines` : `billets` = 2, `paires` = 0 ; `freq_bien_notes`, `freq_apparies` et `d` valent null pour les 25 gestes ; `avertissement` = « sous-ensemble choisi sur une variable qui dépend du statut : description seulement ». Cette description est vide : elle ne dit rien.
- Pour comparaison (section 5.5 de la grille) : `ensembles.tous.billets` = 62, `ensembles.tous.bien_notes` = 39, `ensembles.tous.paires` = 23 (donc 23 appariés), `ensembles.tous.sans_apparie` = 16.

## 7. Règles ambiguës : deux lectures côte à côte, rien de tranché

**Ambiguïté 1 — la condition de lecture liée à l'aveugle (grille, section 5.5).** Texte : « si les paris justes de la tenue dépassent nettement la part des appariés et des bien notés, toute consigne est à lire comme "pratique des billets que les lecteurs reconnaissent pour bons", pas comme effet de la rédaction. » La grille dit elle-même que ce seuil n'est pas chiffré, que la lecture « n'est pas gelée au sens d'un préenregistrement et ne commande aucune décision ».
- Lecture A : la condition est remplie (parts de paris justes 0.9512195121951219 et 0.9122807017543859, contre 39 bien notés et 23 appariés sur 62 billets) ; chaque consigne porte le libellé « pratique des billets que les lecteurs reconnaissent pour bons ».
- Lecture B : « nettement » n'ayant pas de seuil écrit, la condition ne peut être déclarée ni remplie ni non remplie par la règle ; les consignes gardent leur seul qualificatif de la section 8, et les chiffres de l'aveugle sont donnés à côté.
- Dans le gabarit : les deux lectures figurent en tête, avec les chiffres ; aucune n'est choisie. Aucun qualificatif de la section 8 n'en dépend.

**Ambiguïté 2 — la déclaration d'usage d'une intelligence artificielle dans l'écriture (G24).** La ligne « Analyse » du geste dit : « descriptive (la consigne vient de la politique du site, pas de la mesure ; `docs/sources/lesswrong-politique-ia-v1/`) » ; la section 8 dit, point 2, « exclu » (le geste est rare, non évaluable : `prevalence_indicateur` (tous) = 0.04838709677419355) et, point 3, « rapporté, jamais consigne ».
- Lecture A : le gabarit ne porte aucune ligne sur ce geste ; il est seulement rapporté.
- Lecture B : le gabarit rappelle, hors mesure et sous ce libellé, que la politique du site commande cette déclaration ; ce rappel ne s'appuie sur aucun chiffre de l'étude.
- Dans le gabarit : aucune consigne tirée de la mesure (les deux lectures s'accordent là-dessus) ; les deux lectures sont écrites dans la section des gestes sans consigne. Le rédacteur n'a pas ouvert le dossier de la politique du site (hors mandat) et n'en reprend aucun contenu. Sous-point de forme : pour ce geste, à la fois rare et descriptif, l'ordre de la section 8 donne « exclu » (point 2, avant le point 3) alors que la section 5.2 dit « rapporté, jamais consigne » pour une prévalence basse ; les deux mènent à « pas de consigne », seule l'étiquette diffère.

**Ambiguïté 3 — le texte d'une « objection à prévenir ».** La section 8 dit quelles classes sont « à prévenir » mais n'écrit d'avance aucun texte de consigne pour elles (au contraire des gestes) ; la section 5.4 dit que les liens entre gestes et objections sont exploratoires, « jamais au gabarit ».
- Lecture A : le gabarit nomme la classe par sa définition de la grille, mot pour mot, comme objection que les lecteurs font le plus souvent, sans dire quel geste la prévient.
- Lecture B : le gabarit en tire une consigne de rédaction ; aucun texte n'existe d'avance, l'écrire serait un choix neuf, et le relier à un geste est interdit par la section 5.4.
- Dans le gabarit : la forme A est écrite, parce que la forme B ne peut pas l'être sans choix neuf ; l'ambiguïté est signalée et la décision revient à la session mère ou à Lazar.

**Ambiguïté 4 — l'ensemble sur lequel la fiabilité d'une classe d'objection se juge.** La section 5.2 dit pour les objections « même seuil ; même règle de prévalence extrême » (pour les gestes : deux ensembles, « tous » et « sans marquage 1 ») ; la section 8 dit « sur l'ensemble "tous" ».
- Lecture A : fiabilité jugée sur « tous » seulement. Lecture B : sur « tous » et sur « sans marquage 1 ».
- Effet : aucun. Les deux lectures retiennent les mêmes classes (O1, O4).

**Ambiguïté 5 — « l'ensemble sur lequel elle tient » (section 8, libellé honnête).** Chaque consigne doit être suivie de « l'ensemble sur lequel elle tient ».
- Lecture A : les ensembles que la règle lit (23 paires, et 11 paires hors réunion des marquages). Lecture B : ceux des quatre ensembles rapportés où `d` ≥ 0.
- Dans le gabarit : `d` est donné sur les quatre ensembles pour chaque consigne ; les deux lectures s'y lisent. Pour les quatre consignes « pratique majoritaire, non contredite », `d` ≥ 0 sur les quatre ensembles ; pour les trois « sous réserve », le détail est dans le tableau.

**Ambiguïté 6 — un renvoi qui ne correspond plus (section 5.2).** Le geste quasi universel « n'entre au gabarit que sous le libellé "convention du genre (fiabilité non mesurée)", hors des points 1 à 4 de la section 8 ». Or, dans la section 8 gelée, la convention du genre **est** le point 1, et les consignes sont les points 5 à 7.
- Lecture A : le renvoi veut dire « hors des qualificatifs de consigne et de piste ». Lecture B : à la lettre, « hors des points 1 à 4 » de la liste gelée, ce qui contredit le point 1.
- Effet : aucun sur le libellé ; dans les deux lectures les limites (G17) entrent sous « convention du genre (fiabilité non mesurée) », jamais « distinctif » ni « à éviter ».

**Ambiguïté 7 — « la moitié des bien notés » aux points 7 et 8.** Les points 5 et 6 écrivent « des 39 bien notés » ; les points 7 et 8 écrivent « des bien notés » sans nombre.
- Lecture A : les 39 (`freq_bien_notes` sur « tous »). Lecture B : les bien notés de l'ensemble lu.
- Effet : aucun ; pour les trois consignes sous réserve, `freq_bien_notes` dépasse 0,5 sur les quatre ensembles (section 3 ne donne que « tous » ; valeurs sur `sans_reunion` : G19 0.5384615384615384, G20 0.7307692307692307, G21 0.5769230769230769).

**Deux points de forme que la règle ne fixe pas** (ni ambiguïté de fond, ni chiffre) : l'ordre des consignes dans le gabarit (le rédacteur garde l'ordre des gestes dans la grille) ; et le fait que le texte gelé d'une consigne peut dire plus que l'indicateur mesuré — « de préférence dans une section titrée » pour les limites (G17), dont l'indicateur réunit les modalités `dispersées` et `section` et pour lesquelles l'analyse ne donne aucune fréquence par modalité. Le texte gelé est recopié tel quel, comme la section 8 l'ordonne, et la réserve est écrite à côté.

## 8. Ce que le rédacteur n'a pas fait

Aucune statistique recalculée ; aucun seuil neuf ; aucun geste redéfini ; aucun lien entre un geste et une objection ; aucune lecture des copies, des commentaires, des dépôts, des arbitrages, de la table de correspondance, de la moitié développement ; aucune lecture du script d'analyse (seule son empreinte est recalculée) ; aucun fichier écrit sous `registres/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; ni commit ni poussée. Ce fichier n'a pas été contre-lu : la contre-lecture par un agent neuf est prévue par la session mère (ligne R-3483 du registre).
