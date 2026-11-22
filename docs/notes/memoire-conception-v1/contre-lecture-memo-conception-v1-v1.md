# Contre-lecture de la mémoire de la conception des 21 et 22 novembre (v1)

- Pièce : `docs/notes/memoire-conception-v1/memo-conception-21-22-novembre-v1.md`, empreinte `5da6b4b38d98310a` (concorde avec son compagnon `.sha256`). Classe C.
- Contre-lecteur : Claude Opus 5.5, sous-agent neuf, lecture seule. Date : 22 novembre 2026.
- État lu : branche `claude/bibliothecaire-v1`. La tête est maintenant `cc838a1e`, et non plus `727c6573`. `git diff 727c6573` est vide pour la mémoire, `registres/go.md`, `registres/decisions.md`, `docs/decisions/`, l'inventaire et les réponses de Fable. Les seuls ajouts sont un script de garde pour les modèles de Google et `docs/notes/memoire-conception-v1/epreuve-bibliothecaire-v1.md`. Je n'ai pas ouvert ce dernier fichier : il n'est pas dans la liste d'autorisation.
- Périmètre : la liste d'autorisation (`31fc781d4fbe2c57`), lue en premier. Je n'ai ouvert que des pièces autorisées : les décisions N-075 à N-077 et N-053, l'inventaire des seconds regards, les réponses de Fable 1 à 30 sans la 24, et les lignes visées de `registres/go.md` et de `registres/decisions.md` (ligne R-2059 évitée). Je n'ai ouvert aucun fichier exclu, aucune autre branche, ni la demande ou la réponse 24. Aucun commit, aucune machine, aucun appel externe.

## Verdict (trois lignes)

1. Utilisable avec corrections. L'échantillon ne contient aucune erreur grave sur 45 fiches. Il contient 13 erreurs mineures, soit 28,9 % (intervalle exact de Clopper et Pearson à 95 % : 16,4 % à 44,3 %). Chemins, empreintes et définitions tiennent partout.
2. Le défaut est systématique et porte sur l'état. 11 des 13 erreurs sont des fiches tirées des réponses de Fable (et une du registre des décisions) laissées « proposé » ou « non tranché » alors qu'une ligne de `registres/go.md` les accorde : GO-2026-11-22-12, -20, -24, -32, -33, -34, -42. Les agents des lots « F » n'ont pas croisé ces lignes, et l'avertissement de la section 0 ne suffit pas.
3. La page phare porte une erreur grave, l'idée 8 : N-053 est dit « touché et non tranché », ce qui est faux, et il est confondu avec « aucun retour à l'agent ». Elle omet aussi une tension, le lemme « retiré comme résultat » contre « il est à nous » (GO-2026-11-22-42). Côté cloisonnement : aucun chiffre cloisonné, aucun contenu d'attaque opérationnel. Deux points sont à vérifier par la mère.

## 1. Table par fiche (échantillon, graine 20261122)

Pour toutes les fiches : chemin trouvé et empreinte de 16 signes concordante (`sha256sum`). Valeurs vérifiées : v3 de N-075 `5aed4bab1172b181`, erratum 1 `c6efeccfafca4158`, erratum 2 `b19852b47a90e902`, erratum 3 v2 `fbe3298ec358fa9b` ; N-076 `49b664c1d6a72fdb`, son erratum 1 `34a59c49436d5239` ; `go.md` `d8e7639c7e8aa9d0` ; `decisions.md` `75f4ab9603eba780` ; les 35 réponses de Fable, toutes concordantes ; l'inventaire `02252df286503f8c`. La règle « ligne = 599 + NN » (et 687 + NN pour le 22) est vérifiée.

| Fiche | Verdict | Constat (et correction, citation de la source) |
|---|---|---|
| N075-03 | juste | v3 l. 61 et erratum 1 C-1 : plancher occupé (« Blindfold », Gans et Holden, Podkopaev et Ramdas) ; « Ne pas écrire » : « premier plancher d'audit » (v3 l. 219). Retenu comme base : GO-2026-11-21-51, et plus exactement GO-2026-11-21-46 D-5 (« écrit comme base nommée »). |
| N075-19 | juste | v3 § 5 mot pour mot : énoncé, deux tests de mort, liste des quantités comptables, revendication 3 « partiellement occupé », bras A exclu. |
| N075-24 | juste | v3 § 11, point 5 : tâche de conception plutôt que nœud, D-3 de la note sur la pince (GO-2026-11-21-50), confiance 0,6. GO-2026-11-21-61 ne nomme que les points 7 à 11 : la mention « non nommé » est juste. |
| N075-25 | juste | v3 § 11, point 9 ; erratum 2 (« je penche poiur ca, demande au collisionneur et organisme dans la demande fusionnee », GO-2026-11-21-61) ; erratum 3 v2, A-3 (« le réapprentissage des sondes en service est permis » en « Ne pas écrire »). |
| N076-20 | juste | N-076 § 10 : mesure, deux témoins, test de mort, « rien » au programme, continuations « que je n'ai pas vérifié » dans la ligne de 10 USD. |
| N076-23 | juste | N-076 § 13, points 1 à 9, confiances exactes ; erratum 1, E4 (point 6 clos) et E5 (banc sorti des premiers pas). |
| GO-14 | mineure | Contenu et mot exacts (GO-2026-11-21-51 : « Ce qui vaut : deux regards tels qu'échapper à l'un expose à l'autre. : go »). Le rattachement « Inventaire : 1.2 » est faux : l'inventaire 1.2 est « Le dilemme valeur contre issue », un autre objet. À corriger en 5.4 (« la borne du dilemme ») et 5.5. |
| GO-42 | mineure | Elle confond la loi de la référence honnête (C1, N-076, intégrée à GO-2026-11-21-57) avec la thèse du papier A. La réserve de GO-2026-11-22-20 porte sur « la thèse du papier A (réponse 4 D1, D4 ; réponse 8 D4) […] la loi recommandée est occupée et mal énoncée ». GO-2026-11-22-24 réécrit cette thèse, pas C1. Ce que R-4767 dit de C1 : « N-076 "horizon au plus m" redit le corollaire 1 de Ker 2010 ». Correction : « État : intégrée (GO-2026-11-21-57), promue seulement après l'essai jumeau contre jumeau (GO-2026-11-22-12, point 1) ; son horizon redit Ker 2010 (R-4767) ». |
| GO-52 | juste | GO-2026-11-22-20, point 1, mot pour mot. GO-2026-11-22-21 (demande 10) est un renvoi peu utile, sans faute. |
| GO-62 | juste | GO-2026-11-21-12, -17, -18 (« à fond »), -21 (option (a), niveau de l'idée), -31, -38 (D-B1 à D-B6, statisticien des Mines). |
| GO-65 | juste | GO-2026-11-22-12, point 4 ; -24 ; -26 (« il faut réduire drastiquement les coûts ») ; -28 (pilote P-std). |
| GO-72 | juste | GO-2026-11-22-42 : « Mesure du modèle nul chez de vrais agents : « go » ». |
| RD21-25 | juste | R-4541 (l. 4679) et R-4564 (l. 4702) mot pour mot (quatre inexactes : Schaeffer, Westphal, Lucassen, Taufeeque). |
| RD21-40 | juste | R-4572 : « protocole X attaquant et convergence (cf073972…) — H10 proposée, nœud ». |
| RD21-50 | juste | R-4637, R-4715, R-4716, R-4727, R-4749 ; GO-2026-11-21-84 (« première action dans la perte de distillation « gardée » »). |
| RD22-11 | mineure (état) | « Proposé non tranché » est faux. GO-2026-11-22-12, point 2 : « Coercition et corruption (réponse 1) : « go » sur le plan (pilote E0 et E1 puis modes de A, B, C par additifs) et sur D1 à D5 ». Correction : retenu, plan et D1 à D5 accordés. |
| F01-13 | juste | Réponse 1, D3 (« deux bras, sous cloison stricte. Confiance 0,6 ») ; réponse 7, l. 192 (E1.5). Accordé par GO-2026-11-22-12, point 2 (« deux bras pour l'attaquant optimisé contre les scores »). |
| F01-18 | mineure (état) | Définition et six graines exactes (réponse 2, l. 34, 50-51, 98). Mais la lecture des six graines (décision 4) est accordée à GO-2026-11-22-12, point 1 (« antériorité et essai en parallèle, six graines lues sur PDF avant toute phrase de nouveauté »), et l'en-tête du lot le sait déjà par la demande 6. Correction : retenu pour la décision 4. |
| F01-35 | juste | Réponse 4, l. 38, 40, 149-151, décision 1 (0,65). La thèse a été suspendue (GO-2026-11-22-20), puis réécrite (GO-2026-11-22-24) : « proposé » reste défendable. |
| F01-47 | mineure (état) | Contenu exact (réponse 5, l. 119-122, 158-159, décision 6). État : GO-2026-11-22-20, point 1, accorde la « rétro-analyse des journaux des collisionneurs (troisième tour conditionnel) », et GO-2026-11-22-21 lance la demande 10 sur son critère. Correction : retenu. |
| F01-50 | mineure (état) | Contenu exact (réponse 6, l. 20, 35 ; FlipFlop, l. 110). État : GO-2026-11-22-20, point 2 : « flagornerie : famille de charges, H8 seule hypothèse neuve au papier C ». Correction : retenu. |
| F01-52 | juste | Réponse 6, l. 38-39, R4 (H7, H9 locales) ; portée « huit milliards », l. 180. |
| F01-54 | juste | Réponse 6, R5, bras F0 à F7 exacts, mesure principale, inférence seule. |
| F01-57 | mineure (état) | Contenu exact (réponse 6, D5 ; réponse 7, l. 82-106, décision 1). État : GO-2026-11-22-20 : « questions testées puis envoyées » et « test de neutralité puis second tour ». Correction : retenu. |
| F01-62 | mineure (état) | Contenu exact (réponse 7, l. 156-166 : erreur plantée, liste scellée, indice de suivisme, seize exécutions). État : GO-2026-11-22-20 : « pilote essaim puis deux exécutions par mode ». Correction : retenu dans son principe, préenregistrement de classe A à écrire. |
| F08-16 | juste | Réponse 9, l. 98 et 197, décision 2, option c ; Speed et Culpin 1986. |
| F08-21 | juste | Réponse 9, l. 100 (√3, Avenhaus, von Stengel, Zamir 2002), phrase 10 (l. 196) ; réponse 9 accordée (GO-2026-11-22-24, « go recos 9 »). |
| F08-23 | mineure (état) | Contenu exact (réponse 11, l. 35, 55, 116). État : GO-2026-11-22-24 : « « Ses décisions : go » (étau, réponse 11) » ; la décision 1 (énoncé restreint avec δ fixé d'avance) est accordée. Correction : retenu. |
| F15-09 | mineure (état) | Contenu exact (réponse 15, A.1, l. 48 ; A.3, l. 77 ; décision 2, l. 232-237). État : GO-2026-11-22-32 tranche la décision 2 (« sessions filles : « on garde tel quel » »). Correction : décision 2 tranchée ; le script d'audit du canal n'est pas accordé en propre. |
| F15-14 | juste | Réponse 16, voie 2, (2a) à (2d), l. 125-149 ; chances 0,3 et 0,5. |
| F15-20 | juste | Réponse 17, l. 22, 41 ; phrase interdite n° 5, l. 216. |
| F15-22 | juste | Réponse 17, l. 34-38, 120, 147, 213. |
| F15-32 | juste | Réponse 18, l. 89-93, 132, 170 (« dix mois ont passé sans recherche descendante »). |
| F15-63 | juste | Réponse 21, l. 198-203 (0,35), R7, décision 1 (0,6), décision 6 (0,7). |
| F22-07 | mineure (état) | Contenu exact. Mais la « remarque citée proposée (décision 3 de la réponse 22) » est accordée à GO-2026-11-22-33, point 4 (« Décisions 1 à 5 de la réponse 22 accordées »). L'en-tête du lot F22 (« aucun identifiant GO ou R- qui les tranche ») est donc faux pour la réponse 22. |
| F22-35 | juste | Réponse 22, l. 103 et 131 ; 22B, l. 95 et 113 ; 22P, l. 123. La décision 5 de 22B n'est pas trouvée accordée au registre. |
| F22-36 | juste | Réponse 22, l. 106 ; 22B, l. 114, 148, décision 5 ; 22P, l. 143. |
| F22-64 | mineure (état) | Contenu exact (réponse 23, B2, l. 121-140). État : GO-2026-11-22-42 : « Réponses 23 et 24 : « go recos » avec ses remarques », ce qui accorde la décision 3 (lecture principale). Correction : retenu dans sa lecture principale. |
| F22-65 | mineure (état) | Contenu exact (réponse 23, B3, l. 142-158). La décision 2 (ouverture une fois, en dernier) est accordée à GO-2026-11-22-42. Correction : retenu. |
| F25-06 | juste | Réponse 25, l. 53 et 149-153. Les décisions de la réponse 25 sont accordées (GO-2026-11-22-42, « go 25 recos »), mais les témoins sont une proposition de B3, non une décision : « proposé » est tolérable. |
| F25-11 | juste | Réponse 25, B4, l. 165-175. « Note adjudant v2 » : la source dit « la note du concepteur » (version non dite). |
| F25-16 | juste | Réponse 29, § 1, point 1 ; D-1, recommandation (a), 0,7 ; l. 95 (organisme : deux conditions sur quatre manquent, hypothèse). |
| F25-26 | juste | Réponse 29, l. 242-247, D-5 (0,8). |
| F25-29 | juste | Réponse 26, l. 44 et 63, décision 3. Non vue accordée à GO-2026-11-22-42 (seuls l'engagement horodaté et la table des revendications d'abord y sont dits « go »). |
| F25-62 | juste | Réponse 30, décision 1, option b (0,7) ; l. 58, 184 ; références, l. 203-207. |

Décompte : 32 justes, 13 mineures, 0 grave. Sur les 13 mineures, 11 portent sur l'état (une ligne GO accorde ce que la fiche dit « proposé » ou « non tranché ») et 2 sur le contenu (GO-14, GO-42).

## 2. Sections 0, 1 et 4

### Section 0 (mode d'emploi)
Exacte. Fenêtres de lignes, empreintes, nombre des réponses (35, sans la 24), primauté des errata, exemple de GO-15 contre N075-16 : tout se vérifie. Deux remarques.
- La phrase « Une fiche tirée d'une réponse de Fable sans identifiant GO est une proposition, même si elle paraît décidée » sert de règle par défaut aux lots « F ». L'échantillon montre qu'elle est souvent fausse. Il faut une jointure explicite entre réponses et lignes GO (table plus bas).
- La date d'épinglage `5b596acc` et la tête du commit de livraison ne posent pas de problème : les sources sont inchangées depuis.

### Section 1.1 (huit idées porteuses)
- Idées 1 à 5 et 7 : chaque affirmation se trouve dans une source (inventaire 3.1, 4.1, 4.3, 5.1, 5.2 ; N-075 v3 § 2 à 6 ; erratum 2, point 8 ; erratum 3 v2 ; GO-2026-11-21-60 ; GO-2026-11-22-42 pour la chute conjointe). Les renvois pointent les bonnes fiches.
- **Idée 6, mineure (incomplète).** Elle est juste pour GO-2026-11-22-24. Elle omet deux mots de Lazar postérieurs : GO-2026-11-22-40 (« lemme et théorème : « on les garde mentionnés » ») et GO-2026-11-22-42 (« Lemme d'additivité : « il est à nous dans son application au contrôle de l'IA » »). Le second est en tension avec « retiré comme résultat », et cette tension n'apparaît pas en section 4. Par ailleurs, la « forme commune aux trois papiers » (F22-02) est une proposition non tranchée de Fable (réponse 22P), présentée ici comme si elle faisait partie du changement accordé le 22. Correction : la dire « proposée ».
- **Idée 8, grave.** Le texte « aucun score de moniteur ne revient à l'agent (N-053, point 5) » est « touché et non tranché ».
  1. N-053, point 5, dit « aucun score de moniteur (sonde, juge) n'entre dans un signal d'entraînement ou de sélection » (`decision-N-053-v1.md`, l. 42). Ce n'est pas « aucun retour à l'agent ». Cette dernière règle est la ligne 4 des invariants d'audit de N-076 (§ 8), dont la rivale (les trois lignes des « asymétries », D-2) n'est pas tranchée (N-076 § 13, point 1).
  2. N-053 est tranché « strict » : GO-2026-11-22-20 (« sens (a) et (b) seulement, N-053 strict ») ; l'inventaire § 6 le dit « fermé hors bras d'attaque déclaré ».
  3. Aucune fiche n'est citée pour cette moitié.
  Correction proposée : « l'invariant « aucun retour à l'agent » (N-076, ligne 4 du § 9) contre les trois lignes de la note « asymétries » (N076-18, N076-23 point 1), non tranché ; N-053 tenu strict (GO-2026-11-22-20) ».

### Section 1.2 (carte)
Les 160 identifiants cités en sections 1 et 4 existent tous, et chaque titre correspond au concept nommé. Un défaut :
- **Ligne « Dilemme plutôt que décorrélation » (mineure).** Elle est rattachée à l'inventaire 1.2, qui est « Le dilemme valeur contre issue » (un regard interne, terme du milieu du bilan de la pince). C'est un homonyme : le rattachement juste est 5.4 et 5.5. Il faut aussi ajouter cet homonyme à la section 1.3.

### Section 1.3 (à ne pas confondre)
Chaque distinction se retrouve dans une source : N075-16 et N075-17 (v3 § 5, point 3, « le jumeau d'un saboteur est un saboteur ») ; inventaire 2.2, 2.10, 2.12, 2.20, 5.4, 5.5 ; réponse 23, B3 ; F08-17 ; F15-12 ; F01-36. Il manque la paire « dilemme des deux regards » et « dilemme valeur contre issue ».

### Section 4 (tensions)
- 1, 3, 4, 5, 7, 9, 10, 11 : renvois justes et affirmations portées par les sources (GO-2026-11-21-61 ; N-076 § 13 ; GO-2026-11-21-61, « auditer des actes plutôt que des issues : go » ; demande 29 pour « nouvelle manière de compter » ; réponse 23, l. 29 ; 22B, l. 25 ; 22C, l. 25 ; 22P, l. 172 ; réponse 27-luc, l. 265).
- 2 : juste. Les deux points sont accordés, l'un à GO-2026-11-21-51, l'autre à GO-2026-11-21-61, et l'erratum 3 v2 (l. 191, 220) dit qu'aucune pièce ne les concilie.
- **6, mineure.** « La thèse retenue n'est datée que par la réponse 27, sans identifiant GO » : l'identifiant existe, GO-2026-11-22-24, point 2 (« Réponse 9 : thèse du papier A = loi héritée citée comme modèle nul, bilan mesuré, complémentarité en second axe »). La v3 du programme est accordée à GO-2026-11-22-40. La réserve est à remplacer par ces deux renvois.
- **8, mineure (formulation).** « La réponse 17 l'ignore » : la réponse 17 cite « Blindfold » treize fois et dit ne pas le connaître (l. 25 : « je ne l'identifie pas de mémoire » ; l. 131, 133). Écrire « ne le connaît pas, et suspend ses statuts à sa lecture ».
- **12, mineure (état).** « Non tranchée dans sa forme » est faux : GO-2026-11-22-12, point 3 : « Fausses alertes sur honnêtes imparfaits (réponse 3) : « go » sur les décisions 1 à 6 ». La troisième honnête de contrôle est « celui qui signale ouvertement » (GO-2026-11-21-55, D-1), non « celui qui refuse ». Les fiches RD22-10 et F01-25, hors échantillon, ont le même défaut d'état.
- **Tension manquante.** Le lemme d'additivité « retiré comme résultat » (GO-2026-11-22-24) contre « il est à nous dans son application au contrôle de l'IA » (GO-2026-11-22-42) et « on les garde mentionnés » (GO-2026-11-22-40). La fiche GO-44 porte le mot, mais aucune section ne nomme la tension.

## 3. Cloisonnement (section 5 et ensemble)

- **Chiffres cloisonnés.** Je n'en ai trouvé aucun, par recherche dans le fichier entier (7a, 7b, T0.6, étape B, étape B bis, P3-bis, barreau 5, aire sous la courbe). Les mentions sont des renvois sans chiffre (« courses consignées […], aucun chiffre repris ici » ; « les verdicts des étapes B et B bis existent ; aucun chiffre ici »). Les « barreaux » de la l. 5010 sont les barreaux de l'épreuve de l'étau (F25-25), pas le barreau 5 du programme. La ligne R-2059 est dite sautée.
- **Contenu d'attaque.** Je n'ai trouvé aucune description opérationnelle d'un mode de sabotage. Ce qui touche à l'attaque reste au niveau de l'idée ou de l'épreuve défensive : bras F0 à F7 de cadrage, barreaux de l'étau, ι et δ, « deux refus du catalogue de sabotage opérationnel ».
- **Deux points à vérifier par la mère, sans conclure.**
  1. Section 5, lot F25 : « L'expérience 1 du billet « Reasons or watching? » est lue « non lisible » ». C'est un verdict qualitatif recopié de la réponse 26 (l. 120). Si cette expérience 1 relève de 7a ou 7b, le § 2.5 de la liste exclut aussi les « résultats », pas seulement les chiffres. Je ne l'ai pas tranché, faute de pouvoir ouvrir la pièce qui le dirait.
  2. La fiche RD21-50 et la section 5 nomment des éléments de conception de l'organisme saboteur à budget : les rôles « maître » et « flagrant », la « perte de distillation », la première action « gardée ». La source est autorisée (registre ligne par ligne), et ce n'est pas un mode opérationnel. Mais pour le rôle le plus restreint (un concepteur de moniteurs tenu à l'écart), c'est un détail de fabrication de l'attaquant. Mieux vaut le résumer en « étalonnage du saboteur à budget accordé (GO-2026-11-21-84) ».

## 4. Taux d'erreurs de l'échantillon (n = 45)

| Catégorie | k | Taux | Intervalle exact de Clopper et Pearson à 95 % |
|---|---|---|---|
| Graves | 0 | 0 % | 0 % à 7,9 % |
| Mineures (toutes) | 13 | 28,9 % | 16,4 % à 44,3 % |
| dont état périmé | 11 | 24,4 % | 12,9 % à 39,5 % |
| dont contenu (GO-14, GO-42) | 2 | 4,4 % | 0,5 % à 15,2 % |

Calcul : inversion exacte de la loi binomiale, par dichotomie, en Python standard.

**Verdict global : utilisable comme index, avec corrections.** Avant tout usage d'une ligne « État » d'un lot F, ou d'une fiche RD22 :
1. Écrire une table de jointure entre réponses de Fable et lignes GO, et propager les états qu'elle donne. Réponse 1 : GO-2026-11-22-12, point 2. Réponse 2 : point 1. Réponse 3 : point 3. Réponses 5, 6, 7 et 8 : GO-2026-11-22-20. Réponses 9, 11, 12 et 13 : GO-2026-11-22-24. Réponse 14 : GO-2026-11-22-28. Réponse 15 : GO-2026-11-22-32. Réponse 19 : GO-2026-11-22-34. Réponse 22 : GO-2026-11-22-33, point 4. Réponses 23 et 25 : GO-2026-11-22-42. Réponse 26 : GO-2026-11-22-42, en partie.
2. Corriger l'idée 8 de la page phare (grave), l'idée 6, la ligne « dilemme » de la carte, et les tensions 6, 8 et 12 ; ajouter la tension sur le lemme.
3. Corriger GO-14 et GO-42.
4. Faire trancher par la mère les deux points de cloisonnement.
