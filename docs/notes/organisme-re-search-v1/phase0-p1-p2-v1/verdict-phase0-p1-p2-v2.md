# Verdict (R13) — phase 0 de P1 et de P2, organisme d'idéation, sous le préenregistrement v2

**Préenregistrement appliqué : `preenregistrement-phase0-p1-p2-v2.md`, sha256 `bff8744edfb80201f0c97c58d54d8f409830707186613b8df2e96ecadd392d0a` (sceau vérifié, conforme à l'empreinte attendue).**

**Sorties brutes lues (dossier `execution-v1/`, versées au commit 5b6cd919 avant toute lecture ; sceaux vérifiés, quatre sur quatre conformes) :**

| fichier | sha256 |
|---|---|
| `manifeste-phase0-p1-p2-v2.json` | 4f78c58851ebf1c6c63bbcedc7186300c5bff791c73661691455cf82dfcf5eb9 |
| `sortie-phase0-p1-p2-v2.json` | 8a2a85920fe70be925aa96cb255374cd75bb78e5f2121780d02466442e7e4967 |
| `journal-fichiers-ouverts-phase0-p1-p2-v2.txt` | e30269fb7bbbd4e474c1f3a445f8f9843fbf6de6eb10f2b9fa0c98585be0378e |
| `sortie-standard-execution-v1.log` | 0e25f71362cbd64a1d5f901bdad30ddac63dc5316371c594e8ecd5e3be68edc3 |

Autres pièces lues, sceaux vérifiés : `verification-courte-phase0-p1-p2-v2.md` (c0b5c3c9bd139959bef1b62290a0f569f50a8a805e868d141f61c47b930cc8ca), dont les quatre consignes s'imposent ici ; `contre-lecture-phase0-p1-p2-v1.md` (48c1647ba3293ea911900b19056fb4a3256322fbee55587b82ed539c0356996e) ; le code nommé ci-dessous (sources seules, rien exécuté).

- Lecteur : modèle I, **instance neuve** ; n'a écrit ni le préenregistrement, ni le code, ni la contre-lecture, ni la vérification, ni l'analyse (R13). Lecture commencée à 2026-11-18T05:51:31Z, cette pièce écrite à 2026-11-18T05:53:05Z et suivantes (`date -u`).
- Rien relancé (aucune exécution du lanceur), aucune dépense, aucun appel de modèle ; aucun fichier existant modifié. Les chiffres ci-dessous sont lus dans `sortie-phase0-p1-p2-v2.json` ; les différences ponctuelles ont été recalculées à la main à partir des descriptions par bras de la même sortie (cohérentes à 1e-5 près).

**Issue de P1 : instrument discriminant** (gardes tenues, ordre tenu, A/A propre tenue, branchement de l'ordre de présentation tenu) ; une phase 1 peut être proposée à Lazar, sur devis, non engagée.

**Issue de P2 : la ligne C3 n'est pas refermée par la référence, sous la loi de tirage R1** (médiane R1 = 5/23 = 0,2174, pas strictement au-dessus de 0,25) ; audit de symétrie R4 déclenché ; réserves P-8 et A-1 écrites.

## 1. Sceaux et manifeste

| contrôle (consigne 3 de la vérification ; liste d'arrêt) | attendu | lu | conforme |
|---|---|---|---|
| `essai` (manifeste et sortie) | faux | `false` et `false` | oui |
| contre-lecture : empreinte | 48c1647b…996e | 48c1647ba329…996e | oui |
| contre-lecture : verdict ; texte relu | « scellable après corrections » ; 8c8240fa… | « scellable après corrections » ; 8c8240fa4b7d…3c0 | oui |
| préenregistrement | bff8744e… | bff8744edfb8…392d0a | oui |
| `lanceur_phase0_p1p2_v2.py` | compagnon da4312e7… | da4312e74d64…c47c | oui |
| `questionneurs_p1_v2.py` | compagnon 28705030… | 2870503014f3…ded3e | oui |
| `mondes_reponses_p1p2_v1.py` (réemployé) | compagnon 2c80a833… | 2c80a833e311…ab04 | oui |
| `mesure_forme_p2_v1.py` (réemployé) | compagnon b3da53aa… | b3da53aa5dd6…e932 | oui |
| bloc « effort et échantillonnage gelés » | d156f3e0…0f0a, porté par le texte | d156f3e0cd9f…0f0a, `porte_par_le_preenregistrement` vrai | oui |
| évaluateur de l'organisme | 26613fe7…8632 | 26613fe72da7…8632 | oui |
| sources (course v67 ; attaques v3 et v5) | 21bc75f4… ; e0b3145b… ; cff69d86… | identiques (manifeste et journal des fichiers ouverts) | oui |
| dossier du code modifié ou non suivi | aucun | `[]`, statut lu | oui |
| arrêt écrit dans la sortie | aucun attendu | aucune clé `arret` ; journal standard : deux lignes de verdict | — |

**Seul écart relevé, sans portée** : le manifeste porte le commit `b6fa79c1`, et la consigne 3 nomme les compagnons du commit `80f2851e`. Entre ces deux commits, seuls la vérification courte et son compagnon ont été ajoutés ; les cinq fichiers (texte v2 et quatre modules) ont, à l'un et à l'autre commit, les mêmes empreintes (recalculées par `git show <commit>:<chemin> | sha256sum`). Les empreintes de code du manifeste sont donc bien celles des compagnons de 80f2851e.

Durée du lancement : 2026-11-18T05:38:42Z → 05:50:48Z (725,7 s), un seul lancement (consigne 1 : aucune autre sortie présente dans `execution-v1/`).

## 2. P1 — lecture dans l'ordre gelé

### 2.1 Gardes C-P1-3 à C-P1-6 (elles priment)

| garde | règle gelée | chiffres | tient |
|---|---|---|---|
| C-P1-3 inversion de 10 % (bissection) | borne basse à 95 % de la différence des **moyennes** > 0 | moyennes 0,3963 [0,3306 ; 0,4675] ; médianes, rapportées sans décider, 0,3750 [0,2925 ; 0,4724] | oui |
| C-P1-4 répondeur au hasard (aléatoire − bissection) | borne basse ≤ 0 pour les deux statistiques | médianes −0,1994 [−0,3399 ; −0,0868] ; moyennes −0,2824 [−0,4024 ; −0,1625] | oui |
| C-P1-5 fuite | oracle > 0,05 et signalé ; autres bras ≤ 0,05 ; divergence de l'oracle nulle | oracle 1,0 (signalé), divergence nulle (KL 0 à 0 et à 16 questions) ; les neuf autres bras 0,0 | oui |
| C-P1-6 refus | aucun refus hors grammaire | 0 | oui |

Gardes : **tiennent**. (Portée de C-P1-4 rappelée par le texte, m-1 : elle ne détecte qu'un mode « hasard » non branché ; ici la bissection fait nettement pire que l'aléatoire sous le hasard, comme le texte l'annonçait.)

### 2.2 Ordre des questionneurs (C-P1-1), à T = 16, 200 mondes, 10 000 rééchantillonnages

| écart | médianes : point [ic95] | moyennes : point [ic95] | point et borne basse > 0 pour les deux |
|---|---|---|---|
| aléatoire − bissection | 0,2223 [0,1779 ; 0,2565] | 0,1687 [0,1338 ; 0,2039] | oui |
| répéteur − aléatoire | 0,2319 [0,1853 ; 0,2914] | 0,2403 [0,1867 ; 0,2990] | oui |

Ordre : **tient** (conjonction, aucune correction). Pour mémoire : médianes de KL à 16 questions, bissection 0,0 (carte exacte dans 56 % des parties), aléatoire 0,2223 (13 %), répéteur 0,4542 (8 %) ; moyennes 0,1015, 0,2703, 0,5105. La prémisse « l'aléatoire est meilleur que le répéteur » (confiance déclarée ≈ 55 %) n'a pas été mise en défaut.

### 2.3 Famille A/A (C-P1-2) : intervalle corrigé (niveau 1 − 0,05/6 = 0,99167) et critère de largeur

Écarts entre les bornes (mêmes mondes) : médianes 0,22228, moyennes 0,16874 ; largeurs maximales (0,5 ×) : **0,11114** (médianes) et **0,08437** (moyennes).

| comparaison | statistique | point | ic95 non corrigé | ic95 contient 0 ? | ic corrigé (99,17 %) | contient 0 (critère) | largeur95 | < largeur max ? | tient |
|---|---|---|---|---|---|---|---|---|---|
| A/A aléatoire (copie 2 − aléatoire) | médianes | −0,0102 | [−0,0636 ; 0,0291] | **oui** | [−0,0761 ; 0,0401] | oui | 0,0928 | oui (0,83 du maximum) | |
| | moyennes | −0,0216 | [−0,0547 ; 0,0099] | **oui** | [−0,0676 ; 0,0207] | oui | 0,0646 | oui (0,77 du maximum) | **oui** |
| ordre, aléatoire | médianes | 0,0004 | [−0,0363 ; 0,0355] | **oui** | [−0,0490 ; 0,0462] | oui | 0,0719 | oui | |
| | moyennes | −0,0135 | [−0,0431 ; 0,0165] | **oui** | [−0,0529 ; 0,0268] | oui | 0,0596 | oui | **oui** |
| ordre, bissection | médianes | 0,0 | [0,0 ; 0,0121] | **oui, à la borne** (borne basse exactement 0) | [−0,0121 ; 0,0394] | oui | 0,0121 | oui | |
| | moyennes | 0,0038 | [−0,0062 ; 0,0140] | **oui** | [−0,0093 ; 0,0180] | oui | 0,0202 | oui | **oui** |

- A/A propre (1re comparaison) : **tient**. Branchement de l'ordre de présentation (2e et 3e) : **tient**.
- **Aucun « contient 0 » ne tient par le seul intervalle corrigé** : les six intervalles à 95 % non corrigés contiennent 0 (consigne 3). La correction passée de trois à six entre v1 et v2 (V-1) n'a donc décidé d'aucune case ici.
- **Cas limite à écrire** : ordre de la bissection, médianes, l'intervalle à 95 % non corrigé est [0,0 ; 0,0121] ; 0 en est la borne basse exacte. Il contient 0 au sens fermé (`lo <= 0 <= hi`, règle du code), et l'intervalle corrigé le contient strictement ; c'est l'effet de la masse en 0 (la bissection recouvre le monde dans plus de la moitié des parties, sa médiane vaut 0 dans presque tous les rééchantillonnages), annoncé par le texte : la médiane y est muette, la moyenne décide, et la moyenne contient 0 strictement.
- Marge la plus faible du critère de largeur : A/A de l'aléatoire, médianes, 0,0928 contre 0,1111 (83 % du maximum). C'est sur ce même demi-critère que la famille échouait sur les petits mondes d'essai (0,2203 contre 0,0921) ; à l'échelle, il passe.

### 2.4 Verdict P1

Gardes tiennent ; ordre tient ; A/A propre tient ; branchement tient → ligne 5 de la table gelée : **« instrument discriminant » : une phase 1 peut être proposée à Lazar, sur devis (non engagée)**. Le verdict proposé par le code est le même.

Audit de symétrie R4 propre à P1 : **non déclenché**, à bon droit — l'aléatoire recouvre exactement le monde dans 13 % des parties à T = 16 (seuil 95 %) ; aucun intervalle d'ordre de largeur nulle (le plus étroit : 0,0701) ; aucun écart d'ordre inversé.

Rapporté sans décision (ne change pas le verdict) : A/A de la bissection, médianes 0,0 [−0,0043 ; 0,0021], moyennes 0,0049 [−0,0071 ; 0,0184] ; ordre du répéteur, médianes 0,0240 [−0,0148 ; 0,0744], moyennes 0,0318 [−0,0233 ; 0,0903] ; disperseur − aléatoire, médianes −0,0102 [−0,0538 ; 0,0357], moyennes −0,0157 [−0,0502 ; 0,0189] ; variante structurelle, aléatoire − bissection 0,2605 [0,2118 ; 0,3140] et 0,2401 [0,2047 ; 0,2768], répéteur − aléatoire 0,2042 [0,1324 ; 0,2974] et 0,2250 [0,1622 ; 0,2898] ; lois retirées par la garde de disjonction : 60 908 (limite d'arrêt 50 × 65 536) ; **dispersion de l'A/A sur 8 mondes : quantiles [−0,2602 ; 0,1634], largeur 1,91 fois l'écart aléatoire − bissection des médianes** (information pour P-3).

## 3. P2 — lecture gelée

- Garde de reproduction : 9 cartes répètent sur 23 (0,3913), égal au chiffre de l'analyse ; P2 n'est pas arrêtée. Types : 9 softmax (7 répètent), 5 transformée, 4 mélange, 3 par sous-population (1 répète), 2 si-sinon (1 répète) ; hors softmax, 2 sur 14 (0,1429) ; entiers gardés, 8 sur 23 (0,3478) et hors softmax 1 sur 14.
- **Référence R1** (forme principale, toutes cartes, 10 000 tirages) : médiane **0,2174 (5/23)**, moyenne 0,2119, quantiles 2,5 % et 97,5 % [0,0435 ; 0,3913] ; part des tirages au moins égale à l'observée **0,0458**.
- Seuil gelé : médiane R1 **strictement > 0,25** pour refermer. 0,2174 ≤ 0,25 → branche « ≤ 0,25 ».
- Avec et sans softmax, entiers gardés (23 cartes de la course v67) :

| référence | forme principale : médiane (part des tirages ≥ observée) | entiers gardés : médiane (part ≥ observée) | décision sous cette référence |
|---|---|---|---|
| R1 (base de la décision) | 0,2174 (0,0458 ; observée 0,3913) | 0,2174 (0,1024 ; observée 0,3478) | non refermée, dans les deux formes |
| R2 (racine aux fréquences observées) | 0,3043 (0,2721) | 0,3043 (0,4308) | **refermée** |
| HS (emplacements non softmax) | 0,0714 (0,47 ; observée 0,1429) | 0,0714 (0,7365 ; observée 0,0714) | non refermée |
| SEQ (sans générations) | 0,2609 (0,1119) | 0,2609 (0,2147) | au-dessus du seuil (rapportée, ne décide pas) |

- **Issue gelée** : **« C3 n'est pas refermée par la référence (sous la loi de tirage R1) »**, avec les lectures écrites par le code, conformes à la table : (a) « part observée au-dessus du quantile 95 % de la référence R1 » (0,0458 < 0,05) ; (b) « A-1 : hors softmax, la part observée ne dépasse pas un quart : dans la boucle de production, le seuil n'est franchi que par les softmax » (0,1429 ≤ 0,25) ; (c) réserve **P-8** : la décision change sous R2. Pas de réserve A-1 « décision différente sous HS » (HS ne referme pas non plus), pas de réserve A-3 (les entiers gardés ne changent pas la décision). Ligne non refermée : elle reste « change » à la lettre, avec ses réserves ; P2 ne rouvre rien et n'adopte rien.
- **Cas limite** : la lecture (a) tient à 0,0458 contre 0,05, et l'observée (9/23) est égale au quantile 97,5 % de R1 ; avec les entiers gardés, la même lecture ne tient pas (0,1024). La part observée n'est donc « au-dessus de R1 » que dans la forme principale, de peu.

### 3.1 Audit de symétrie R4 de P2 : **déclenché**

Motif (règle gelée) : la médiane de R1, 5/23, tombe dans [5/23 ; 7/23], à moins de 1/23 du seuil (0,25 − 0,2174 = 0,0326 < 0,0435). La sortie porte `declenche: true` sans motif écrit ; le motif ci-dessus est le seul que la règle prévoie, et je l'ai vérifié. Action gelée faite : R2, HS, SEQ et entiers gardés sont côte à côte au tableau ci-dessus. **Dépendance à la loi de tirage, dite** : la décision tient à la loi R1, choisie par l'auteur (types uniformes, un tiers des racines sur les deux types à forme unique), après avoir su que 7 des 9 répétitions sont des softmax. Sous R2 (types de racine aux fréquences des 23 cartes, 9 softmax sur 23), la médiane passe à 7/23 = 0,3043 et la ligne se refermerait ; sans les softmax (HS), la référence est très basse (1/14) et l'observée hors softmax (2/14) ne s'en distingue pas (0,47). La conclusion « non refermée » est donc fragile à la loi de tirage dans le sens qui referme, et la répétition observée est portée par les softmax.

### 3.2 Rejeu du quota et attaques de Goodhart — description seulement

- Quota (sans vérité, aucune décision) : q = 1 refuserait 5 cartes (toutes softmax), q = 2 (principal) 2 cartes (softmax), q = 3 aucune ; hors softmax, 0 refus pour chaque q.
- Attaques de Goodhart (parts M4 reproduites à l'analyse dans les quatre bras) : v3 « retour » 0,4146 (199/480 ; hors softmax 0,4183 ; R1 aux mêmes longueurs, médiane 0,1771, aucun tirage ≥ observée) ; v3 « témoin » 0,3204 (149/465 ; hors softmax 0,3195 ; R1 0,1763, aucun tirage ≥) ; v5 « retour » 0,3596 (269/748 ; aucune softmax ; R1 0,1925, aucun tirage ≥) ; v5 « témoin » 0,1659 (115/693 ; R1 0,1890, 93,6 % des tirages ≥ observée). Aucune lecture de décision, aucune composition de proposeurs qualifiée (N-058), aucune nouveauté attribuée (mention `aucune_nouveaute` présente).

## 4. Audit R4 général (résultat trop propre ?)

Le seul résultat contraire à l'attente déclarée est la famille A/A tenue (confiance de l'auteur ≈ 30 %, échec sur les petits mondes d'essai). Contrôles faits sans rien relancer :
- cohérence interne de la sortie : les différences ponctuelles des critères égalent les différences des médianes et des moyennes par bras (par exemple aléatoire − bissection, moyennes 0,27026 − 0,10152 = 0,16874 ; inversion, 0,49785 − 0,10152 = 0,39633 ; hasard, 1,07069 − 1,35307 = −0,28238 ; A/A aléatoire, médianes 0,21204 − 0,22228 = −0,01024) ;
- la largeur passe avec une marge modeste (83 % du maximum pour la plus serrée), pas de façon trop nette ; la carte à zéro question est la même pour tous les bras (KL 0,7122 en moyenne, part exacte 0) sauf l'oracle (0, 1,0), comme gelé ;
- les copies de la bissection ont les mêmes KL à 4 questions (déterminisme hors égalités), puis divergent légèrement à 8 et 16 : plausible, et compatible avec l'A/A de la bissection rapportée ;
- aucun intervalle de largeur nulle hors de la médiane de la bissection (masse en 0, attendue) ; l'audit R4 propre à P1 n'est pas déclenché.
Conclusion : rien de trop beau qui appelle une réserve au-delà des cas limites écrits. Cet audit ne remplace pas une relecture du code de la carte et des répondeurs, qui n'est exigée que si l'audit gelé de P1 se déclenche (il ne l'est pas).

## 5. Ce que l'issue ne dit pas

- **Le texte v2 n'a reçu qu'une vérification de différentiel** (R2 est tenue par la contre-lecture de la v1 plus la vérification courte), pas une contre-lecture entière.
- **La phase 0 ne dit de l'ordre de présentation que le branchement** (V-4) : la permutation est correctement branchée ; aucune sensibilité à l'ordre n'est mesurée, ni pour les questionneurs factices du critère (insensibles par construction), ni pour un proposeur réel.
- **La correction de Bonferroni est passée de 3 à 6 entre v1 et v2 (constat V-1 de la vérification), seul seuil modifié, qui facilite le « contient 0 ».** Ici, elle n'a décidé d'aucune case (les six intervalles non corrigés contiennent 0), mais elle reste un assouplissement.
- P1 : rien sur les proposeurs réels (aucun n'a joué), rien sur la boucle de production, rien sur une composition de proposeurs (N-058), rien hors de la grammaire et des prédicats écrits, rien sur la recherche en langue naturelle ; la divergence récompense aussi une carte centrale. « Instrument discriminant » permet de **proposer** une phase 1 sur devis ; il ne l'engage pas. Information pour son dessin : sur 8 mondes, la dispersion de l'A/A vaut 1,9 fois l'écart entre les bornes ; une phase 1 à 8 mondes ne lirait pas cet écart (P-3, P-4 : puissance à calculer avant tout devis).
- P2 : la ligne C3 non refermée ne dit pas que les proposeurs répètent par défaut ; elle dit seulement que, **sous la loi de tirage R1**, la grammaire seule n'atteint pas un quart en médiane. Sous R2 elle l'atteint (réserve P-8) ; hors softmax la répétition observée n'est pas distincte de la référence (A-1). Aucune forme n'est dite nouvelle ; les options (ii) et (iii) ne sont pas essayées en production ; les parties (c) et (d) de la phase 0 de P2 ne sont pas faites.
- Aucune dépense, aucune machine, aucun appel de modèle, aucun accès réseau dans le lancement ni dans cette lecture.

## 6. Incidents

Aucun refus de permission, de crochet ou de classifieur pendant cette lecture. Un fichier de travail jetable (aplatissement de la sortie JSON) dans le dossier temporaire de la session, non versé.
