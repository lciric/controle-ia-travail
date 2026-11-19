# Vérification courte habilitée des lignes du brouillon 3 qui renvoient à la base « mots et coût » — préenregistrement neuf du bras A des organismes discrets — v1

**Conclusion : B7 non levé.** Les renvois visent maintenant les bonnes pièces et les bonnes lignes, la règle de multiplicité est dans le bon sens et le juge d'une autre lignée est bien hors du verdict. Mais trois points bloquent encore :
- le témoin positif de la base, écrit « sans objet », écarte une ligne de validité d'un préenregistrement scellé : c'est un nœud de Lazar (point 3) ;
- la transposition de la base a une ligne mal visée et des trous d'écriture (point 2) ;
- la règle de multiplicité laisse ambiguë la composition de la famille ajustée (point 4).

## En-tête

- **Qui** : le contre-lecteur habilité de la contre-lecture du brouillon 2 (`docs/notes/bras-a-contre-lecture-habilitee-v1/contre-lecture-habilitee-b7-brouillon2-v1.md`, `27189edd29b511a462d17695ff06e2b0902d764261b6753e1a63ffc29567fc6d`), sous-agent délégué par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`). Je n'ai écrit ni le brouillon 3, ni sa note, ni la décision sur les onze nœuds.
- **Modèle** : Claude Opus 5.5 (`claude-opus-5-5`).
- **Heures (UTC, `date -u`)** : début 2026-11-19T07:19:29Z ; écriture à partir de 2026-11-19T07:23:28Z.
- **Dépôt** : arbre courant au commit `9a8dccd27dba2101f8fa6f783d7eae0b8c1d7749` à l'écriture ; brouillon 3 et note lus par `git show FETCH_HEAD:…` après `git fetch` de `claude/pensive-bardeen-1fv7hw`, sommet `0c451b1260dbdf46ac2eaf5eb9967d3d54743b12` (le sommet attendu).
- **Cloisonnement** : aucune valeur de seuil, aucun nombre tiré du document de la base, de la règle de la tâche des organismes ni des seuils du texte archivé, aucun interne de moniteur. Les nombres présents sont des numéros de ligne, des empreintes, des heures et des comptes déjà écrits dans le brouillon 3.

### Pièces lues (empreinte recalculée ; toutes égales à l'attendu)

| pièce | empreinte | lu |
|---|---|---|
| brouillon 3, `prereg/T0.7-organismes-discrets-v-a-v2-brouillon3.md` (`FETCH_HEAD`) | `72e34bdeea768ff70d7429c9a46ec91d09c0bb41e4307388a6893b21499f7e3c` | lignes 1 à 136, 263 à 292, 342 à 436, 510 à 688, 812 à 851, 940 à 974 ; reste parcouru par recherche de mots |
| note du rédacteur, `docs/notes/relance-organismes-discrets-v1/preenregistrement-v2-brouillon3-note-du-redacteur-v1.md` (`FETCH_HEAD`) | `a2d443ef4ab9548ab161b7a5afbfd929aedb6b1642300b6ab09ccd44f60037d9` | section 5 (correspondance) ; section 3, points 1 à 3 |
| choix de Lazar sur les onze nœuds, `docs/notes/relance-organismes-discrets-v1/decision-bras-a-noeuds-texte-neuf-v1-choix-de-lazar.md` | `ecfdbdc9232db755d25db3db1f0ced4fd33dd77135cc1519e7ef5f8064b03b6d` | en entier |
| mon rapport précédent (ci-dessus) | `27189edd…` | en entier |
| document de la base, `prereg/T0.8-base-A-mots-et-cout-v1.md` | `72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d` | relu à la session précédente, en entier ; lignes citées ici reconfirmées |
| règle de la tâche des organismes, `prereg/T0.6-organismes-v0-v1.md` | `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` | lignes 570 à 586 (session précédente) |
| texte archivé, `prereg/T0.7-organismes-discrets-v-a-v1.md` | `06ab6a2f6e173bb1258f45ffeded7a419b05ecc2f59920666cea91aafcc7cf05` | lu en entier à la session précédente |
| fonction de partition des plis, `src/controle_ia/t06/test_croise.py` | `0a627df9ecb82c518d06c0c7ca8df4afab48a5a0da34b785c31c0da4ab41a29c` (celle que cite le document de la base, ligne 11) | signature de `partition_plis`, lignes 53 à 59 |
| registre des scellements, `registres/scellements-v1.md` | — | ligne 16 |

Non ouverts : les mêmes interdits qu'avant (noms « consigne-privee », « conception-ii-b » ; `brouillons/ii-b-saboteur-budget-v1/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun résultat). Aucune recherche récursive, aucun réseau hors du `git fetch` de la branche nommée, aucune dépense, aucun fichier existant modifié, rien de committé.

---

## Les sept verdicts

### 1. Renvoi des critères « réussit, échoue, non calculable » — **conforme**

- Section 4, point 3 (ligne 286) : la règle de `prereg/T0.6-organismes-v0-v1.md`, ligne 576 (règle des lignes 573 à 585, deux bases à la ligne 575), et le document de la base, lignes 62 à 92, avec la non-calculabilité propre aux lignes 86 et 131. Les pièces et les lignes sont exactes, et la lecture prudente de la ligne 139 est portée.
- Table « Seuil », ligne de la base (ligne 382) : même renvoi à la ligne 576, « sans correction », plus la section 6.12. Conforme. La définition de la base (A) n'y est pas rappelée, mais la section 6.12 la porte.
- Mêmes renvois exacts dans l'en-tête (lignes 47 et 48), en section 1 (ligne 126), en 6.9 (ligne 524) et en 6.10 (ligne 533).

### 2. Section 6.12, transposition de la base au bras A — **non conforme (écriture)** ; conforme au nœud 9 pour ses deux causes

Les six points sont couverts, et le point 5 suit le nœud 9 à la lettre (6.10, ligne 533 ; 8.2, ligne 678 ; ligne C2). Corrections, chacune avec son renvoi :

1. **Point 4 (ii), ligne mal visée.** Si la base lit le témoin identité, le contrôle de l'adaptateur se calcule. La ligne qui s'applique est alors BA-L3 du document de la base (ligne 133 : « au-dessus », réserve R-BA2), ou BA-L3b (ligne 134) seulement s'il n'est pas calculable. « La ligne BA-L3b s'applique alors telle qu'écrite » (ligne 565) est faux.
   **Renvoi corrigé** : « lignes BA-L3 (ligne 133) et BA-L3b (ligne 134), telles qu'écrites ; réserve R-BA2 portée avec toute phrase des lignes C ; aucun état ne change (ligne 137) ».
   Il faut aussi écrire la correspondance des jeux : la base est apprise sur la dose 1 contre l'honnête et lue sur le témoin identité contre l'honnête, comme le document de la base, ligne 96, l'écrit pour la dose 1 et son adaptateur témoin.
2. **Point 5, cause incomplète.** La règle, ligne 576, et le document de la base, ligne 86, donnent une troisième cause de « non calculable » : les tirages dégénérés. Or le brouillon garde en arrêt la ligne 243 du texte archivé (section 1, ligne 104 ; 8.2, ligne 678). Pour la base, le conflit d'arrêt contre état demeure donc sur cette cause.
   **Renvoi corrigé** : 6.12, point 5, et 8.2 (ligne 678) doivent dire que, pour la base, cette cause donne « non calculable » selon la ligne 576, et que la ligne 243 du texte archivé reste un arrêt pour les autres intervalles. C'est la lettre de la règle que cite le nœud 9 ; si le rédacteur la lit autrement, c'est un mot à demander à Lazar.
3. **Point 1, population du centre.** Le document de la base, ligne 66, prend toutes les conditions que la base lit. Au bras A, la base lit aussi le témoin identité (point 4 (ii) ; 6.10, ligne 533), alors que le point 1 n'en prend que cinq. Le texte doit dire si le témoin identité entre dans le centre ; à la lettre de la ligne 66, il y entre.
   Le minimum de coûts lisibles par tâche est atteignable avec l'effectif du bras. Il faut cependant écrire s'il est repris comme compte absolu ou comme proportion de l'effectif de la tâche : la ligne 66 l'écrit pour un autre effectif.
4. **Plancher et intervalle propres à la base, non écrits.** La section 1 (ligne 96) et la section 6.9 (ligne 526) changent le nombre de permutations et l'usage du plancher des moniteurs. La base, elle, se lit « selon son propre critère » (ligne 576), qui renvoie au plancher, au nombre de permutations et à l'intervalle de la ligne 575.
   **Renvoi corrigé** : 6.12, et 6.9 (ligne 524), doivent dire que la base garde l'intervalle, le plancher et le nombre de permutations de sa règle (lignes 575 et 576), et que les changements de 6.9 ne la touchent pas.
5. **Point 6, entrées du code.** La version neuve doit aussi nommer les entrées de la base au bras A : mesures par action tirées des lecteurs de la chaîne gelée que nomme le document de la base, ligne 43, et liste blanche transposée (lignes 115 et 148).
   La base sur le sac de mots exclut les épisodes de distillation des tâches de réserve (règle, ligne 575). Au bras A, les transcriptions des tâches de fabrication ne doivent donc pas entrer dans son vocabulaire : à écrire.
6. **Audit et réserves de la base.** L'audit gelé de la ligne 111 et les réserves de la ligne 137 du document de la base ne sont pas mentionnés : dire s'ils sont gardés au bras A. Ils ne changent aucun état ; l'item (ii) de l'audit dépend du témoin positif (point 3 ci-dessous).

Le point 3 (plis) est conforme et exécutable : `partition_plis` prend une graine entière et exige un nombre pair de tâches, que les seize tâches de vérification satisfont ; 6.2 fournit l'entier par `graine_entiere` sous la clé `bras-a-v2/plis`. Le point 2 (effectifs) est conforme.

### 3. Témoin positif de la base écrit « sans objet » — **non conforme ; à poser à Lazar : c'est un écart à un préenregistrement scellé**

- Le document de la base est un préenregistrement scellé (`registres/scellements-v1.md`, ligne 5, même empreinte `72b067d5…`).
- Sa ligne 41 rend le témoin positif « décisive pour la validité de la base (A) », pour une raison qui vaut au bras A : une base en panne qui « échoue » partout élargit le jugement dans le sens favorable. Au bras A, elle rendrait « discret » (ligne C6) plus facile.
- La ligne de lecture BA-L2 (ligne 132) prescrit, quand le témoin positif est « non au-dessus » ou « non calculable », la réserve R-BA1 et l'attente du mot de Lazar ; c'est la décision Q-4, option (a), à la ligne 177.
- Écrire « sans objet » et ne pas appliquer BA-L2 (brouillon 3, ligne 565) écarte donc la règle de validité du texte scellé que le brouillon adopte par renvoi.
- **L'écart porte sur** : `prereg/T0.8-base-A-mots-et-cout-v1.md`, `72b067d5…`, lignes 41, 51, 107, 132 et 177.
- Que ce document ait été scellé pour la course de confirmation (lignes 159 et 169) n'y change rien : le bras A emprunte sa base et ses lignes de validité. Selon la hiérarchie de décision du dépôt, un écart à un préenregistrement scellé est un nœud.
- La réserve écrite au point 4 (i) peut être l'une des options qu'on pose à Lazar. Elle ne remplace pas son mot.

### 4. Section 6.9, règle de multiplicité neuve — **sens et cohérence avec la table C conformes ; non conforme sur un point d'exécution**

Ce qui est conforme :
- **Sens** : ne pas corriger la condition (a) et corriger la condition (b) rendent toutes deux « discret » plus difficile. Corriger « repère » protège l'affirmation « repéré ».
- **Exclusivité** : « repère » exige la valeur p ajustée sous le niveau ; « ne repère pas » exige la valeur p brute au-dessus du niveau. La valeur ajustée n'étant jamais plus petite que la brute, les deux s'excluent, et « indécis » est le reste.
- **Cohérence avec la table C** : dans l'ordre écrit, C4, C5 et C6 sont exclusives et complètes une fois la base en échec et le coût apparié ; C2 et C3 se lisent avant.
- **Exécution** : la valeur p par permutations, comptée avec la correction d'une unité, est exécutable ; la clé `perm/{analyse}` existe en 6.2.

Correction nécessaire :
- **Composition de la famille ajustée.** La famille est fixée d'avance à douze, « quel que soit le nombre de doses en B8 » (ligne 525), mais l'étape (m) (ligne 426) et la table C ne se lisent qu'aux doses en B8. Pour un ajustement de Holm sur douze, les douze valeurs p doivent exister et être classées ensemble.
- **Renvoi corrigé** : 6.9, ligne « Famille » (ligne 525), et 6.3 (m) (ligne 426) doivent dire que les quatre moniteurs du verdict sont calculés aux trois doses, en B8 ou non. Les douze valeurs p sont ajustées ensemble (valeur ajustée de Holm), puis la table C ne se lit qu'aux doses en B8.

Points mineurs :
- la façon de prendre un quantile sur les rééchantillonnages (interpolation) n'est pas écrite ;
- la clé `boot/{analyse}` est décrite en 6.2 comme servant aux rééchantillonnages « rapportés », alors qu'elle sert ici à une décision ;
- le niveau de la ligne 381 de la table « Seuil » n'est pas marqué « proposé » alors qu'il n'a pas d'origine dans le texte archivé ;
- la base garde sa propre règle (point 2, item 4).

### 5. Section 6.10, juge d'une autre lignée — **conforme ; conforme au nœud 10**

- Tirages : clé `lec6/{tâche}`, une par tâche, sans la condition. Les mêmes positions (épisode, pas) sont tirées une fois par tâche et appliquées aux cinq conditions (6.2, ligne 408 ; 6.10, ligne 533), conformément à la ligne 164 du texte archivé. La clé est désormais écrite.
- Bras rapporté (6.10 ; section 4, point 4 ; 6.3 (m) ; 6.9, hors de la famille) : il n'entre dans aucune ligne de la table C. C2 (base non calculable) et C3 (base réussit) ne le nomment pas ; C1, C4, C5 et C6 portent sur « les quatre autres moniteurs ». L'en-tête de la table C (ligne 631), l'issue « discrétion » (7.5, ligne 646) et la phrase de C6 (7.7, ligne 661) l'excluent ; 7.5 (ligne 649) le rapporte hors de toute issue.
- Le déclencheur d'audit « toutes les doses en C6 » ne le concerne pas.

### 6. Mes remarques d'alors — **traitées, deux cases encore à remplir**

- **Code de la base désigné par empreinte** : pas encore. 6.12, point 6, et la case « code » (ligne 843) exigent une version neuve avec version et empreinte. La case est « à remplir » et bloque le scellement (8.1) : c'est le bon endroit. On peut citer dès maintenant l'empreinte de la version source inscrite au registre des scellements (ligne 16 : `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json`, `e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b`).
- **Consigne du juge et question de l'appariement** : l'affirmation est réécrite en hypothèse de travail (section 4, ligne 289). Elle est vérifiée pour les quatre moniteurs sans modèle de langue, sous réserve pour le moniteur boîte noire par action (P-010), et non vérifiée pour le juge. La case « consignes des moniteurs » (ligne 839) est à remplir et la phrase de C6 dit « à la connaissance de leurs pièces ».
- Le juge étant passé en bras rapporté (nœud 10), sa consigne ne touche plus aucun verdict. Seule la réserve sur le moniteur boîte noire par action pèse encore sur C6.
- Remarques « sans objet » et phrase de C6 : appliquées (7.5, ligne 646 ; 7.7, ligne 661), conformes.

### 7. Cloisonnement de ce rapport — **conforme**

Ce rapport ne donne aucune valeur de seuil, aucun nombre tiré du document de la base, de la règle de la tâche des organismes ou des seuils du texte archivé, aucun interne de moniteur (ni poids, ni direction, ni score, ni texte de consigne). Je l'ai vérifié par une recherche des nombres décimaux et des pourcentages dans ce fichier avant scellement : il n'en reste aucun, hors des identifiants de pièces, des numéros de section et du nom du modèle.

---

## Conclusion

**B7 non levé.** Il reste trois choses :
- le témoin positif de la base : écart au préenregistrement scellé de la base (lignes 41, 51, 107, 132, 177), à poser à Lazar ;
- six corrections d'écriture en 6.12 et 8.2, avec leurs renvois au point 2 ;
- la composition de la famille ajustée en 6.9 et 6.3 (m), au point 4.

Une fois ces lignes corrigées et le mot de Lazar inscrit, une vérification courte des seules lignes changées suffira.
