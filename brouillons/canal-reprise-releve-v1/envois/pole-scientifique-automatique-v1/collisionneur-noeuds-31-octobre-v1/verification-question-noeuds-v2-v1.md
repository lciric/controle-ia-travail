# Vérification de la question au collisionneur sur les nœuds du 31 octobre 2026, version 2 — v1

- **Auteur** : sous-agent neuf, Claude Sonnet 5.5 (`claude-sonnet-5-5`) ; je n'ai écrit ni la question (v1, v2), ni sa contre-lecture, ni la liste des faits, ni aucune pièce vérifiée. Même famille de modèle que le contre-lecteur de la v1 (instance différente) ; l'auteur de la v2 est Opus 5.5 (conv-audit).
- **Heure (UTC)** : relevé `date -u` 2026-10-31T06:34:00Z, après les lectures, avant l'écriture. Durée : environ vingt minutes.
- **Non fait** : rien lu sous `donnees/` ; aucun réseau ; aucun commit ; aucun `.sha256` écrit ; aucun fichier existant modifié. Les pièces de `origin/main` (R-866 à R-873, journaux des tours des questions 6 et 7, `docs/notes/gu-krenn-v1/`) ne sont pas sur la branche : tout ce qui n'existe que là est SUPPOSÉ ci-dessous.
- **Abréviations de chemin** : `ENV/` = `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/` ; `DOC/` = `docs/notes/ideation-organisme-v1/`. « l. » = numéro de ligne de la v2 (`ENV/collisionneur-noeuds-31-octobre-v1/question-noeuds-decisionnels-collisionneur-v2.md`).

## Verdict

**ENVOYABLE APRÈS (cinq corrections courtes, listées en fin de document).** Sur les douze constats : dix traités, deux partiellement (QN-06, QN-07), aucun ignoré. Aucun chiffre de la v2 n'est absent des pièces ; trois sont inexacts ou mal rattachés (à corriger). Le corps de la v2 ne contient plus de recommandation ni de confiance d'auteur, sauf deux fuites minuscules. Mais deux défauts font que l'annexe du tour 2 ne protège pas encore de l'ancrage : l'annexe est dans le même fichier que le corps, et la liste des faits servirait au tour 1 des pièces qui portent les recommandations et les confiances des auteurs.

## Empreintes (SHA-256 recalculées à la lecture)

| Pièce | SHA-256 |
|---|---|
| `ENV/collisionneur-noeuds-31-octobre-v1/question-noeuds-decisionnels-collisionneur-v2.md` (pièce vérifiée ; 2 497 mots) | `06b12b49492a96471dc16c20beef3c63a763f8ae8bcb650cf39bfe80f465a44c` |
| idem `…-v1.md` (1 070 mots) | `f11f4bf3203ca168e5726a0665aa6dd298ed11292dcacf55f88c71fc75fbc298` |
| idem `contre-lecture-question-noeuds-v1.md` | `ec58e65899d99bf9ec587a9f6e7d4d085be3991b3f925a13af8f154cc3907eaa` (égale à son compagnon) |
| idem `faits-a-assembler-noeuds-v1.md` | `aa230ae37d016f78b5e7a20de874c27f9353992dc6f64a6ee104428192c62fa6` |
| `ENV/bisociation-deux-espaces-v1/experience-v2/lancement-v2/verdict-validation-v1.md` | `f5bf86b9d5001f363d0768cd88bebcc1f8e842711fa0c4c578d40debf13e8675` |
| `ENV/bisociation-deux-espaces-v1/experience-v2/lancement-v2/diagnostic-v5-v1/diagnostic-v5-v1.md` | `2875f4adfd79ecb19143e9a583997c987686b9b2e9db4bbad35d2c8a68f064e8` |
| `ENV/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon7.md` | `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` |
| `ENV/pre-pilote-course-2-v1/annexe-bras-meta-v1-brouillon1.md` | `3a2e8dc2f8d764674941498ab0da9a977e7cbbd1478d868428efb8d1ca3441a0` |
| `ENV/pre-pilote-course-2-v1/contre-lecture-annexe-bras-meta-v1-brouillon1.md` | `db249b9356f8d19cd8c9811c3db184b0d7587eba97ed8386501e146434e24f1d` |
| `ENV/pre-pilote-course-2-v1/calcul-puissance-pre-pilote-course-2-v6.sortie.txt` | `7394ddae54e20aa527c615ff762719ed0a27ec591e08fbd93774536959d6ece3` |
| `ENV/bisociation-niches-v1/relecture-fable-reponse-3-v1.md` | `556bc9d5f7eb12ef12b4ba2b284eb2ef5fd52acac815a0b0ff26489264e04129` |
| `ENV/decisions-en-attente-lazar-2026-10-31-v1.md` (le mémo, lu pour la provenance des phrases) | `6968aeafded6373aca87cd23edbeab7b8032dea69b8ce5bd18e3da6b90ef6f3f` |
| `DOC/course-2/devis-course-2-et-pre-pilote-v6.md` | `13ef84f9fcee9f43914ba76748805a4f2bff2f30bc42de62f42a0600a97473ed` |
| `DOC/contre-lecture-cl19-orchestrateur-v54-v1.md` | `f1cc6c1a974fcbe4efe4d7dfe0087333ea1103b9ad6aa0e98f9016f6d7c3f31e` |
| `DOC/contre-lecture-cl18-orchestrateur-v53-v1.md` | `0ce1d0b5a8c5016fdcb7262db3597bcc0320ddcd884dfb3d8821fa467230c52b` |
| `DOC/orchestrateur-v55/LISEZMOI-orchestrateur-pole-v7-v55.md` | `bbfdcb3c30d174dd7feeee9ba8dd20aeb7777c5f0e65aeb087e3c4388c743aa3` |
| `DOC/orchestrateur-v54/LISEZMOI-orchestrateur-pole-v7-v54.md` | `a3290bc7237057af11dd8a320d631b73293ffb41e55aef65e11f0b90ff79beb2` |
| `prereg/brouillons/preenregistrement-identification-semi-reel-v1-brouillon3.md` | `1a229998fcbe7cd8dc45abeb559508ae8411f309059912c365bc02ae3b92e67c` |
| `docs/notes/bisociation-litterature-reelle-v1/collisionneur-bisociation-lot-v1/synthese-bisociation-lot-v2.md` | `23c2888ddd924b85a0bbd0009a17f64723399d69ffd17669f56c4fddf7d18a86` |
| `prereg/preenregistrement-bisociation-deux-espaces-v2.md` | `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea` |
| `registres/decisions.md` (fichier vivant ; lignes R-630, 635, 638, 643, 634, 660, 661, 674, 675, 678 à 680, 685, 686 lues) | `afcec0168f7597a233014cd3418de76d87509d4963b55c951b36db7920c91bed` |

Les empreintes des pièces citées par la contre-lecture sont celles qu'elle a relevées (brouillon 7, annexe, devis v6, CL19, LISEZMOI v55, brouillon 3, synthèse, préenregistrement) ; seul `registres/decisions.md` a changé (fichier vivant).

## 1. Les constats QN-01 à QN-12

| Constat | Statut | Où dans la v2, et ce qui reste |
|---|---|---|
| **QN-01** N5, choix de code mal décrits | **Traité** | l. 39 : numérotation CL19 § G annoncée ; 1 (arrêt au premier « non mesuré »), 5 (témoin négatif non vu exclu, A5), 8 (n = 2, pas de report, C12), 10 (indices S18/S19, crête) correspondent mot pour mot à CL19 § G et à la table du LISEZMOI v55. Le choix 4 n'est plus répété (c'est le nœud A21). `budget.portee_plafond` / CL18-11 gardé à part, comme demandé (CL18, choix 1 et CL18-11 : vérifié). |
| **QN-02** N2, modèles de budget | **Traité** | l. 25–28 : DEP4 et A15 (l. 26) ; 0,011 à 0,013 (sortie v6, citée par le brouillon 7) et 0,80 (brouillon 7, DEP4) ; 0,168, 0,063, 0,983 à 0,991 (devis) ; bases 28,4 / 30,6 et 32,6 / 34,6 ; options omises ajoutées (45 sans arrêt, 32 ; 28 avec porte 0,11 et sacrifices 0,92) ; « tout plafond autre que 32 ; 28 exige une ligne nouvelle » ; décision 2 du devis (110, 123, 140, 160, 180) et L4. **Réserves** : voir 3.1 (notation illisible ; configurations non étiquetées). |
| **QN-03** N7 au passé, sans options | **Traité (une fuite)** | l. 47 : trois options (a) retrait, (b) maintien à partir de cinq tailles, (c) suspension jusqu'à E2′ ; plus de « retirée … suspendue ». Le lien N1–N7 non étayé est remplacé (l. 59) par N1 et la décision 1 de la synthèse (six garde-fous, dont l'étiquette de pont indépendante du canal : vérifié, synthèse l. 188–189). **Fuite** : « puis (a) si l'étalonnage échoue » est la queue de la recommandation de la synthèse (« (c), puis (a) si E2′ échoue »), pas de l'option (c), qui s'arrête à « suspension jusqu'à E2′ » (synthèse l. 219). |
| **QN-04** Portée | **Traité** | l. 51–55 : section « Nœuds non soumis, et pourquoi » (dépenses et comptes, S1–S31, D-e, D-f, L1–L7 sauf L4, décision 3 du devis, points de la v55, décisions 1, 2, 5, 6, 7 de la synthèse) ; N2 et N6 absorbent L4, la décision 2 et DL-3 à DL-8. **Reste** : D-GK-1 (fenêtre du test B, R-680) n'est ni soumis ni listé ; la décision 1 de la synthèse est dite « non soumise » (l. 55) et « à traiter » comme lien de N1 (l. 59). |
| **QN-05** Neutralité | **Traité (réserves)** | l. 9–13 : deux tours ; l. 13 : cinq verdicts dont « aucune option ne tient » et « indécidable sans la pièce X » ; plus de gras ni de confiance dans le corps (sauf la fuite de 3.2) ; l. 17 : réserves du diagnostic relayées (200 mondes, une graine de flux, erreurs types naïves, implémentation parmi d'autres) et les deux lignes opposées de la liste d'arrêt citées ; « et non de décision » supprimé ; l. 36 : « modifier le profil de la décision du directeur » sans qualificatif ; l. 7 : R2 citée avec « pratique : modèle différent ». **Reste** : asymétries de documentation (3.3) et séparation physique de l'annexe (3.4). |
| **QN-06** N6 | **Partiellement** | Traités : DL-9 nomme T2b « tri par coefficient de détermination » (l. 44) ; 107 h / 111 h / plafond 140 h distingués (l. 43) ; DL-1 à trois options (l. 42) ; DL-2, DL-4, DL-6 « plutôt périmètre interne » (l. 45) ; dépendance N6 vers N8 (l. 41) ; DL-6 acte du directeur (l. 44). **Non traité** : DL-2 omet les options à S15 = 110 h (3 graines ≈ 86 h ; 5 graines à 110 h) et attribue « ≈ 107 h » aux « 3 ou 5 graines » alors que 107 h est le chiffre à 5 graines (brouillon 3, résumé 8 et DL-2). DL-3 à DL-8 sont donnés (l. 44) mais écrits comme **la seule option recommandée** (voir 3.5). |
| **QN-07** N8 | **Partiellement** | l. 49 : dernière phrase demande quels fournisseurs doivent être présents et dit que ce tour peut être incomplet (autoréférence traitée) ; aucune recommandation ; « reprendre de jour (dépense, sur devis) ». **Reste** : pas de dénominateur pour la question 7 (« 3 cellules valides » sur combien ?) ; chiffres issus de R-678 / R-871 (`origin/main`) non marqués SUPPOSÉ. |
| **QN-08** N4 | **Traité (réserve mineure)** | l. 36 : SUPPOSÉ explicite sur loi a priori, accord 0,7 et structure 0,3 ; loi qui sous-estime n6 (5 %) ; écart avec le script (0,31 et 0,03) et sa cause ; effectif « borné à dix » ; (b) quinze fiches = changement de plan ; options (c) retirer la bande, (d) canal ≤ 2, (e) modifier le profil, toutes avec les chiffres de la contre-lecture de l'annexe (§ C, ligne « Options pour Lazar ») ; CA1-04 avec les trois structures séquentielles. **Reste** : la lecture de l'annexe « le repli seul éprouvé ne change rien d'autre aux critères du brouillon 7 » n'est pas donnée comme lecture ; CA1-04 reprend l'avis du contre-lecteur (« imposées de la même façon ») comme un fait. |
| **QN-09** N3 | **Traité (réserves)** | l. 31 : D-g reformulé (M6b, quatre fiches d'antériorité non citée, étape protégée hors porte, S30, 0,47, 0,09, DEP2c) ; l. 32 : D-h (b) 0,86 / 0,14 / 0,70 ; l. 33 : contrainte de R-634 (« dix fonds écrits deux fois ») ; l. 34 : « 37 960 » marqué SUPPOSÉ (R7), substitut, « jamais reliés ». **Reste** : « effet sur la porte +0,002 » est attribué à D-g (b) seule (l. 31) alors que le brouillon 7 le donne pour D-g (b) et D-i (2) ensemble (« D-g (b) seule n'est pas jouée ») ; la lecture de R-634 n'est plus signalée « à confirmer » (le mémo l'écrit) ; « à seuils de confiance 0,4 » (l. 34) mélange la confiance de S31 (0,4) et ses seuils (20 œuvres, 5 œuvres). |
| **QN-10** N5 | **Traité (réserve)** | l. 38 : (a) déjà codée dans la v55, non contre-lue ; divergence de défaut donnée ; (c) « change M1 » ; l. 73 (annexe) : « mieux que l'amendement : ne pas lire » avec la recommandation 0,7. **Reste** : les trois conditions de compatibilité de CL19 § C point 3 ne sont que dans la pièce n° 14 ; l'option (a) de la v2 dit « à É5 » alors que la lecture 1 de la v55 couvre aussi É3 (exemption A8) et que l'option (b) rend aussi l'exemption A8 (LISEZMOI v55, « CL19-03 », l. 67–82). Le défaut est attribué à « le code » ; il vient de CL19 et du LISEZMOI. |
| **QN-11** N1, historique et options | **Traité (une confusion)** | l. 22 : option E « abandon de l'expérience v2 » (R-660 C) ; l. 17 : « l'erreur type d'une *différence* entre deux statuts … 0,29 à 0,60 » (diagnostic § 1.4 et § 2) ; l. 69 : l'historique (A de R-660 retirée par son auteur, R-661) est dans l'annexe, donc hors du corps. **Confusion** : voir 3.1 (lettres). |
| **QN-12** Divers | **Traité** | l. 3 : date inchangée (écart de deux minutes sans effet, accepté) ; l. 63 et règle (3) de la liste des faits : table des empreintes jointe. |

## 2. Chiffres nouveaux de la v2 contre les pièces

**Aucun chiffre de la v2 n'est absent des pièces.** Vérifié un par un contre les pièces ci-dessus.

- **N1** : 0,137 / 0,134 (diagnostic § 1.3, T2) ; 1,29 / 2,27 (G3 : 1,293 et 2,275) ; 0,33 / 0,83 (T1) ; 0,079 (validation, diagnostic § 1.1) ; 0,29 à 0,60 (§ 1.4) ; 200 mondes (§ 1.1, § 2 réserves) ; 2,87 (verdict, 2,8735). Les deux lignes de la liste d'arrêt sont citées en abrégé (la première perd « (V1 à V6, plafond de l'oracle S8) » et « avant les bras candidats ») : fidèle au sens.
- **N2** : 0,011 à 0,013 = sortie v6 l. 51–54 (0,0127 ; 0,0123 ; 0,0109 ; 0,0109) ; 0,80 = 0,798 et 0,801 (sortie v6 l. 62–65, DEP4, A15) ; 28,4 / 30,6 / 36,3 / 38,7 / 0,24 / 0,34 = brouillon 7 résumé 3 et 7 ; 32,6 / 34,6 / 0,168 / 0,063 / 0,983 / 0,991 / 0,30 / 0,41 = devis § 0 et § 3.3 ; porte 0,11 et 0,92 = brouillon 7 résumé 3.
- **N3** : 1,6 ; 0,47 ; 0,09 ; +0,002 ; 0,86 ; 0,14 ; 0,70 ; + 0,50 = brouillon 7 D-g, D-h, D-i.
- **N4** : tous conformes à l'annexe (§ 6) et à la contre-lecture de l'annexe (§ C).
- **N6** : 87 h, 107 h, 111 h, 140 h, 22 valeurs, 37 sur 50, p. 9 = brouillon 3 (résumé 3, 5, 8 ; DL-1, DL-5, DL-8). Les confiances de l'annexe (0,65 ; 0,55 ; 0,6 ; 0,85 ; 0,7 ; 0,7 ; 0,7 ; 0,75 ; 0,55) sont celles du brouillon 3, une à une.
- **N7, N8** : conformes à la synthèse (décision 4, E2′, cinq tailles) et à R-678 (7 sur 12 ; 3 ; cinq coupures).

**Trois chiffres inexacts ou mal rattachés (à corriger)** :
1. N3, l. 31 : « effet sur la porte +0,002 » est celui de D-g (b) **et** D-i (2) ensemble.
2. N6, l. 43 : « 3 ou 5 graines ; estimation ≈ 107 h » : 107 h est l'estimation à 5 graines (DL-1 option 2) ; à 3 graines, ≈ 86 h (DL-2 option 1).
3. N2, l. 27 : « médianes 39,6 et 40,6 » sont celles de la **configuration recommandée** à 45 ; 40 et à 50 ; 45 (devis § 3.3), sans dire laquelle va avec quel plafond. À 45 ; 40, 0,168 et 39,6 sont de la configuration recommandée, 0,30 du texte du brouillon (0,103 et 37,7 pour la même ligne « texte »). Ranger les paires « texte (recommandée) » comme pour le brouillon 7.

**Chiffres sans pièce servie dans la liste A telle qu'elle est découpée** (voir 4) : 0,4 de S31 (brouillon 7 l. 296 et 687, hors des extraits) ; la portée du plafond « ≥ N × S17 » (CL18 l. 35 et 156, en liste B) ; les confiances « conv-audit » de l'annexe (N4 (a) 0,5 ; N2 0,6) qui viennent du mémo, exclu des faits ; les chiffres de N8 (R-871, `origin/main`) ; « vocabulaire absent de 37 960 concepts » (R-680, qui paraphrase R-873, `origin/main`) : la v2 le marque bien SUPPOSÉ.

## 3. Formulations encore orientées, et place des recommandations

### 3.0 Réponse à la question posée : les recommandations sont-elles hors du corps ?

**Oui dans le texte, pas encore dans l'envoi.** Dans le corps (l. 1–63) il n'y a ni « Recommandation », ni confiance d'auteur, ni gras ; la section annonce « options, sans recommandation » (l. 15). Toutes les recommandations et confiances sont dans l'annexe (l. 67–76), sans gras, avec leur auteur nommé. Deux fuites dans le corps (3.2). Deux faiblesses d'envoi (3.4 et 4).

### 3.1 Confusion de lettres et de notation

- **N1, annexe l. 69** : « sa recommandation précédente, A « corriger le générateur », 0,7 ». Dans le corps, A est la redéfinition de V5 (l. 18) et **C** est « corriger le générateur seul » (l. 20). La lettre A est celle de R-660 (A corriger le générateur, B changer V5, C abandon), pas celle de R-661 que le corps reprend. Un répondant du tour 2 lit « A retirée » et comprend que la redéfinition de V5 a été retirée. À écrire : « corriger le générateur (option C ci-dessus ; lettre A dans R-660), 0,7 ».
- **N2, l. 28** : « 45 ; 40 (lecture du brouillon 7) ; 45 ; 40 souples (devis) ; 50 ; 45 souples (devis) ; 45 sans arrêt d'étape ; 32 ; 28 (…) » utilise le point-virgule à la fois comme séparateur d'options et comme séparateur plafond ; arrêt d'étape. La liste n'est pas lisible sans connaître la notation. À écrire en puces, « 45/40 », « 50/45 », « 32/28 ». Le devis offre aussi les options (d) « 50/45 au quantile 90 %, souples » et (e) « 45/40 au quantile 90 %, souples » : omises, sans conséquence si le choix est dit.

### 3.2 Fuites dans le corps

1. **N7, l. 47** : « puis (a) si l'étalonnage échoue » dans l'option (c) est la queue de la recommandation de la synthèse, déjà dans l'annexe (l. 75). Retirer du corps. Même l. 47 : « la taille du système n'y est pas identifiable » est la position de A (synthèse l. 83 : « A refuse les tests de criticité, car la taille n'y est pas identifiable » ; B les garde à partir de 5 tailles) écrite comme un fait. Écrire « selon A … ; B garde les tests à partir de cinq tailles ».
2. **N3, l. 34** : « à seuils de confiance 0,4 » : un chiffre de confiance d'auteur dans le corps. Écrire « paramètres S31 (vocabulaire à au moins 20 œuvres, actif à au moins 5 œuvres), SUPPOSÉ ».

### 3.3 Asymétries de documentation (mineures à moyennes)

- **N1** : le diagnostic donne un inconvénient pour chaque option ; la v2 l'écrit pour A (« contrôle presque acquis par construction »), C (insuffisante), D (échoue en M_moyen, au niveau du bruit) mais **pas pour B**, la recommandation de l'annexe (inconvénient du diagnostic § 3 : le risque « rareté de l'étiquette retenue » n'est plus gardé par un seuil, écart d'environ 1,4 entre vrai d'opérateur et proche en M_bien), ni pour E. À ajouter, une ligne.
- **N1, l. 17** : « les deux statuts … suivent une loi qu'aucune règle n'égalise » reprend la phrase du mémo (§ N1, enjeu), pas celle du diagnostic : les variantes G1 à G3 **donnent** la loi S16d aux étiquettes d'opérateur et l'écart reste à 1,29 ; ce qui subsiste est le double canal des ponts d'opérateur avec trace et le repli (diagnostic § 2, cause principale et cause secondaire). Écrire « dont l'égalisation par le générateur (G1 à G3) ne suffit pas, à cause du double canal et du repli ».
- **N1, l. 20** : « meilleure variante permise : 1,29 en M_bien, 2,27 en M_moyen » : 1,29 est le minimum en M_bien ; en M_moyen la variante H1 (sans jumeaux) donne 1,24 ; 2,27 est la valeur de la **même** variante G3. Écrire « variante G3 : 1,29 et 2,27 ».
- **N3** : D-h (b) a ses conséquences chiffrées (0,86 ; 0,14 ; 0,70) ; D-h (a) n'a ni son coût (le pré-pilote attend l'annexe, quelques jours, avec le jalon de fin novembre) ni ses chiffres (C12 0,97, porte 0,16). D-g (b) a quatre inconvénients, D-g (a) aucun (inconvénient du brouillon 7 : si le vérificateur ne sait pas nommer une antériorité manquante, on l'apprend après la course).
- **N4** : (a), la recommandation de l'annexe, est la seule option sans inconvénient (celui de la contre-lecture de l'annexe : « rien n'est appris sur la lisibilité du profil avant la course »).
- **N5** : (a) « déjà codée » sans son inconvénient (« A21 n'est plus vrai à la lettre ; l'aveugle repose sur le code », LISEZMOI v55) ; (b) sans le sien (« une pièce de plus, une interface de plus, à éprouver »).
- **N4, CA1-04, l. 36** : « garde trois structures séquentielles imposées de la même façon » est l'avis du contre-lecteur de l'annexe (« Mon avis de contre-lecteur »), non un fait de l'annexe. Écrire « selon la contre-lecture de l'annexe ».

### 3.4 Annexe et corps dans un seul fichier

Le tour 1 dit « Ne lisez pas le tour 2 avant d'avoir répondu au tour 1 » (l. 11), mais l'annexe est dans le même fichier (l. 67–76) : un répondant qui reçoit le fichier entier la lit. L'ancrage n'est évité que si la chaîne d'envoi fournit le corps au premier appel et l'annexe seulement au second. À écrire dans la note d'envoi ou à scinder en deux fichiers (corps ; annexe du tour 2).

### 3.5 N6, DL-3 à DL-8 : l'option recommandée tient lieu de question

Le brouillon 3 donne, pour chaque DL, deux ou trois options et sa recommandation. La v2 (l. 44) écrit DL-4 « CITRIS hors de la gradation 1 » (option 1, 0,85 dans l'annexe), DL-5 l'étape d'effet de l'option 1 (0,7), DL-6 « obtenir avant le gel les PDF » (option 1, 0,7), DL-7 « gel en arbitrant S3, S8, S9 » (option 2, 0,7), DL-8 « échelle de définitions … la première qui atteint 22 valeurs » (option 1, 0,75). Les options écartées n'y sont pas : DL-4 option 2 (CITRIS avec C donné comme cible), DL-5 options 2 (oracle) et 3 (seuil de 90 %), DL-6 option 2 (geler avec SUPPOSÉ), DL-7 option 1 (geler en bloc), DL-8 options 2 (u₁ seule) et 3 (compter avant scellement). Un répondant du tour 1 ne peut pas former d'avis propre sur ces cinq points : il valide ou non l'option posée. À ajouter, une ligne par DL.

## 4. La liste des faits est-elle cohérente avec la v2 ?

**Par nœud, les pièces existent presque toutes** (liste A du fichier `faits-a-assembler-noeuds-v1.md`, numéros de ligne recoupés sur les fichiers de la branche : brouillon 7 S17 l. 283, A15 l. 543, DEP4 l. 619, « Décisions à Lazar » l. 639 ; CL19 § G l. 149 ; LISEZMOI v55 « Décisions ouvertes » l. 65 ; brouillon 3 résumé l. 9 et section « verdict du collisionneur » l. 687 ; devis § 3.3 l. 184 et § 9 l. 370 : tous exacts).

| Nœud | Pièces de la liste A | Manque ou conflit |
|---|---|---|
| N1 | 1, 2, 3, 18, 19 | rien (R-660 option C dans la pièce 19, mais voir ci-dessous) |
| N2 | 4, 5, 6, 7, 8, 9, 10, 11, 19 | **la pièce 10 est la seule source de « 0,011 à 0,013 »** (sortie v6 l. 51–54) alors que le fichier propose de la retirer en premier pour tenir 40 000 mots |
| N3 | 4, 9, 19 | « confiance 0,4 » de S31 : brouillon 7 l. 296 et 687, hors des extraits (la pièce 4 ne donne que la ligne l. 49, sans la confiance) |
| N4 | 12, 13 | rien |
| N5 | 6, 7, 14, 15, 16 | `budget.portee_plafond` « par génération, ligne ≥ N × S17 » : CL18 l. 35 et 156, **liste B** seulement ; la pièce 16 ne donne que le nom de la clé |
| N6 | 17 | rien (le blocage par la question 6 est dans l. 687–698) |
| N7 | 18 | le désaccord A / B sur la taille identifiable (synthèse l. 83) est hors des extraits (l. 22–40, 164–249, 250–262) ; nécessaire si 3.2 est corrigé |
| N8 | 19 (R-678), pièces de session-depot | journaux des tours : hors de l'arbre, signalés deux fois (deux paragraphes finaux, avec des plages R- différentes : R-871 / R-869 à R-871 ; à fusionner) |

**Quatre incohérences de fond** :

1. **Les recommandations seraient servies au tour 1.** Les règles (1) et (2) du fichier disent de ne pas servir le mémo ni « les avis de conv-audit », et d'étiqueter les recommandations des pièces en les déplaçant « si possible » vers l'annexe. Or les pièces 4, 5, 9 (brouillon 7 : « Recommandation … confiance » à chaque D, S17), 11 (devis § 9), 14 et 15 (CL19 : « Recommandation (confiance 0,7) »), 17 (brouillon 3 : « Recommandation : option 2, confiance 0,65 » à chaque DL), 18 (synthèse : « Recommandation (c) puis (a) ») et 19 (R-630 « recommandation 45 », R-635, R-660 « Recommandation A, confiance 0,7 », R-661 « recommandation révisée B, 0,6 », **R-674 « recommandation 50 / 45 »** et « lecture réservation souple compatible » que QN-02 jugeait non mesurée, R-679) portent toutes recommandations et confiances. « Étiqueter » ne retire pas l'ancrage : la règle doit être **retirer** (extraits déclarés, empreinte de chaque extrait, lignes « Recommandation », « Défaut » et confiances reportées dans l'annexe du tour 2) et exclure de la pièce 19 les lignes R-660, R-661, R-674, R-675, ou n'en garder que les faits.
2. **Taille.** La v2 fait 2 497 mots, non « ≈ 1 600 » : liste A + v2 ≈ 42 000 mots, non 41 000. L'ordre de coupe proposé (pièce 10, pièce 16, R-674 et R-675) est à refaire : garder la pièce 10 (voir tableau), retirer R-674 et R-675 (inutiles une fois les recommandations retirées), retirer la pièce 16 si CL18 l. 35 et 156 entrent en liste A.
3. **Pièces à passer de B à A ou à ajouter** : CL18 l. 35 et 156 ; brouillon 7 l. 296 (S31) ; synthèse l. 83 ; mémo exclu, donc à citer comme « avis de l'auteur, sans pièce servie » pour les confiances « conv-audit » de l'annexe (N2 0,6, N4 0,5), avec son empreinte `6968aeaf…`.
4. **Doublon** : les deux derniers paragraphes du fichier (« Pièces à demander à session-depot » et « Pièces de session-depot à ajouter ») disent la même chose avec des plages différentes (R-871 contre R-869 à R-871 ; R-866, R-868, R-873 contre R-866, R-868, R-871, R-873) ; une ligne vide double entre les deux.

Le balayage « donnees/, clé, jeton, texte de fiche réelle » avant envoi reste à faire (règle (4) du fichier) : je ne l'ai pas fait sur les extraits, qui ne sont pas encore assemblés.

## 5. Liste courte avant envoi (cinq corrections)

1. **Recommandations hors tour 1** : (a) annexe du tour 2 en fichier séparé, fournie au second appel seulement ; (b) dans la liste des faits, remplacer « étiqueter » par « retirer » (lignes « Recommandation », « Défaut », confiances) et exclure R-660, R-661, R-674, R-675 de la pièce 19 ; (c) dans le corps, retirer « puis (a) si l'étalonnage échoue » (N7) et « seuils de confiance 0,4 » (N3), et écrire la position de A sur la taille comme position de A.
2. **N1, annexe l. 69** : lever la confusion de lettres (corriger le générateur = option C du corps, lettre A dans R-660).
3. **N2, l. 27–28** : options en puces « plafond/arrêt » ; paires « texte (recommandée) » pour 0,168, 0,063, 0,30 / 0,41 et les médianes 39,6 / 40,6, en nommant le plafond de chacune.
4. **N6, l. 43–44** : une ligne par DL-3 à DL-8 avec les options écartées ; DL-2 avec ses trois options (3 graines ≈ 86 h à S15 = 110 ; 5 graines à 140 ; 5 graines à 110) ; corriger N3 « +0,002 » (D-g (b) et D-i (2) ensemble).
5. **Liste des faits** : resynchroniser (v2 = 2 497 mots, total ≈ 42 000 ; garder la pièce 10 ; CL18 l. 35 et 156, brouillon 7 l. 296, synthèse l. 83 en liste A ; fusionner les deux paragraphes session-depot).

Souhaitables, sans bloquer : asymétries de 3.3 (B, D-h (a), D-g (a), N4 (a), N5 (a) et (b)) ; « qu'aucune règle n'égalise » et « meilleure variante permise » (N1) ; D-GK-1 ; dénominateur et SUPPOSÉ de N8 ; É3 / A8 dans les options de N5 ; « à confirmer » pour la lecture de R-634 ; CA1-04 « selon la contre-lecture ».

## 6. Réserves de cette vérification

- Je n'ai lu les pièces que par les passages qui portent les chiffres et les formulations de la v2 ; les passages non cités (par exemple le brouillon 7 hors résumé, S17, DEP4, A15, Décisions) ne sont pas relus.
- `registres/decisions.md` est un fichier vivant : son empreinte diffère de celle de la contre-lecture (`e0bba4bf…`) ; les lignes lues (R-630 à R-686) sont celles citées.
- R-678 / R-871, R-680 / R-873 : pièces d'`origin/main`, non lues ; la vérification de N8 et du « vocabulaire absent » est donc celle de la concordance entre la v2 et les lignes de la branche, non des faits eux-mêmes.
- Aucun balayage de sécurité (clé, jeton, `donnees/`) : sans objet pour la v2 elle-même, qui n'en contient pas (lue en entier) ; à faire sur les extraits assemblés.
