# Vérification du brouillon 35 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), contre-lecteur des brouillons 21 à 34. Je juge ; je ne corrige rien.
- **Texte vérifié** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon35.md`, `e62b4caec484…`.
- **Pièces jointes** : la note, `9dbe7c665c2d…`, et la vérification du code de la version 11, `15b3f8528efb…`, partie 2. Les compagnons sont vérifiés.
- **Méthode** :
  - comparaison des brouillons 34 et 35 phrase par phrase, faite par programme ;
  - lecture des blocs touchés : conventions, lignes 223 à 228 ; 6.2, ligne 632 ; 6.9, lignes 787 à 799 ; 8.4, lignes 1040 à 1043 ; 13.1, ligne 1340 ; 13.2, ligne 1363 ;
  - lecture par programme du registre des accords de la branche principale, au commit `abf75e2eb` : son en-tête et la ligne GO-2026-11-19-97.
  - Aucun code ouvert.

## Verdict : **engageable après corrections**

- **Les points demandés sont tenus** : le défaut C-1 et les mineurs M-1 à M-4 de la vérification du code de la version 11, et mes trois mineurs du brouillon 34.
- **Aucune règle de jugement ne change.** Par programme, la section 12, les sections 7.1 à 7.8 et la section 10 sont identiques au brouillon 34. Le reste du texte qui porte des règles l'est aussi.
- **Le périmètre d'une reprise après un arrêt à l'étape (n) est fidèle à l'option (c) de Lazar.** Il en est même la conséquence nécessaire (partie 2).
- **La ligne GO-2026-11-19-97 est conforme** (partie 4).
- **Il reste un défaut à corriger** (C-1). La dispense « suivie d'une reprise » ne sert à rien, comme le rédacteur le soupçonne, et elle ouvre une fenêtre étroite où une seconde première livraison passe sans mot de Lazar. Il suffit de la retirer.
- Il y a aussi trois mineurs.

## 1. Les points demandés

| point | état | endroit |
|---|---|---|
| code v11, C-1 : deux tables C dans la course | **tenu** | 6.9, ligne 799. Après un arrêt à l'étape (n) : aucune lecture de l'étape (m) sous la ligne de GO ; de la sortie refaite, on ne lit que ce qui la reconnaît et la clé `scores_par_unite` ; l'étape (n) se joue sur le fichier de l'étape (m) d'origine. Une course n'a jamais deux fichiers de l'étape (m). 8.4, ligne 1041 : cas sains et artefacts, dont l'essai d'attaque. |
| code v11, M-1 : le contrôle du premier départ resservait au rejeu | **tenu** | L'ouverture passe à cinq champs et l'acte de reprise à sept : ils portent l'empreinte du contrôle du premier départ, ou `null`. Un rejeu refuse tout contrôle déjà porté. Artefacts en 8.4. |
| code v11, M-2 : une ligne de reprise sans rapport levait la garde | **tenu** | Elle doit citer l'empreinte entière d'un fichier d'arrêt ou d'un constat. Voir C-1. |
| code v11, M-3 : une configuration abandonnée bloquait la suivante | **tenu** | Une ligne de type « révocation » qui cite l'empreinte entière retire l'inscription. La configuration retirée ne sert plus. |
| code v11, M-4 : abrégés de moins de seize signes | **rien à faire**, à juste titre | — |
| mon M-1 du brouillon 34 : une autre course | **tenu** | Le programme du constat refuse une configuration de rang 1 quand une autre est inscrite (conventions, ligne 228). Voir C-1 pour la dispense. |
| mon M-2 du brouillon 34 : phrases d'accord | **tenu** | Type autre que « révocation ». Gras ôté, et lui seul. Point final seul admis. Quatrième cellule, nommée « périmètre ». La porte de l'écart à R9 lit aussi le registre courant, et n'ouvre pas si une ligne neuve nomme la ligne de l'écart. Artefacts en 8.4, ligne 1043. |
| mon M-3 du brouillon 34 : suites de « en attente » | **tenu** | Conventions, ligne 228 : la liste de ce qui se retire au scellement. La case « nœuds » y renvoie. |

## 2. Le périmètre d'une reprise après un arrêt à l'étape (n) : fidèle à l'option (c)

- **Ce que Lazar a choisi**, en tenant l'option (c) de la fiche 12 : « un arrêt à l'étape suivante, qui ne porte que des grandeurs rapportées sans verdict, laisse la table de discrétion déjà scellée telle qu'elle est, et seules ces grandeurs sont dites « non rapportées » ».
- **Ce que le texte écrit** : une reprise après cet arrêt ne rejoue que l'étape (n), sur le fichier de l'étape (m) d'origine. Aucune lecture de l'étape (m) ne se fait sous la ligne de GO. La course n'a jamais deux fichiers de l'étape (m).
- **Jugement** : c'est **fidèle**, et c'est **nécessaire**.
  - Rejouer l'étape (m) produirait une seconde table C, comme le montre l'essai d'attaque de la vérification du code : on pourrait alors choisir entre deux tables.
  - Or l'option (c) dit que la table scellée reste « telle qu'elle est ».
  - La précision ne change aucune issue ; elle empêche de contourner l'issue choisie.
  - Le vérificateur du code la qualifiait déjà de « précision de l'option (c), non une question pour Lazar », et je partage son avis.
  - Elle n'ajoute aucune issue neuve : un nouvel arrêt à l'étape (n) se reprend de même, et les grandeurs restent « non rapportées » tant qu'aucune reprise n'aboutit.

## 3. Les réserves 1 à 3 du rédacteur

**Réserve 1 — l'empreinte du fichier des scores refait, lue dans la seule clé `scores_par_unite` de la sortie refaite.** C'est **juste.**
- C'est la règle déjà écrite au brouillon 21 (correction C-9 du code) : l'empreinte est prise dans la sortie scellée, jamais donnée par l'appelant.
- La sortie refaite est elle-même reconnue par son compagnon et par sa provenance, qui la lie au module de la ligne.
- La configuration étant scellée avant la réception, il n'y a pas d'autre source.

**Réserve 2 — pas de contrôle qui confronte les vingt lectures refaites à celles d'origine.**
- Le texte n'en a pas besoin pour être sûr : la condition (4) de la règle d'octroi (aucun calcul de moniteur ne change) est attestée par le lecteur habilité.
- Un tel contrôle ferait pourtant de cette attestation une vérification, à peu de frais.
- Je le recommande, mais **pas comme une cause d'arrêt** : en cas d'écart, les grandeurs de l'étape (n) seraient « non rapportées : livraison refaite incohérente ». C'est l'issue que (c) donne déjà à ces grandeurs, et la table C ne serait pas touchée.
- Comparer les nombres n'est pas une lecture « pour une règle » : aucun état n'en sort, et l'analyse les a déjà vus dans la sortie d'origine.
- Voir M-1.

**Réserve 3 — la dispense « suivie d'une reprise ».** Le rédacteur a raison : elle ne sert à rien. Elle ouvre en plus une fenêtre. Voir C-1.

## 4. La ligne GO-2026-11-19-97, vérifiée par programme

Registre de la branche principale, commit `abf75e2eb`, ligne 530, huit cellules :

| cellule | contenu |
|---|---|
| 1 id | `GO-2026-11-19-97` |
| 2 date | `2026-11-19` |
| 3 type | `décision` |
| 4 périmètre | `écart à R9 accordé pour la table des identifiants opaques` |
| 5, 6 | `—`, `—` |
| 7 | `Lazar` |
| 8 référence | message de Lazar dans la session mère vers 23:46Z, qui dit cette phrase, puis l'ordre de l'inscrire |

- **La quatrième cellule est la phrase exacte** : égale caractère pour caractère, sans gras, sans point final, donc aussi après normalisation de la casse et des accents. Le type n'est pas « révocation ».
- **Elle ne recopie rien de la suite des points 19 et 20.** J'ai cherché dans toute la ligne « point 19 », « point 20 », « intervalle impossible », « non ajustable », « séparation », « fiche 10 », « fiche 11 », « rédaction (a) », « rédaction (c) », « anomalie », « indécis », « option (a) » et « option (c) » : aucun n'y figure.
- **Le mot « go recos » n'a toujours pas sa ligne** au registre. La case « nœuds » le garde marqué.

## 5. Défaut à corriger

**C-1. La dispense « suivie d'une reprise » est sans usage légitime et ouvre une fenêtre.**
- **Endroit** : conventions, ligne 228 (« qui n'est ni retirée ni suivie d'une reprise » ; *Suivie d'une reprise*). 8.4, ligne 1042.
- **Pourquoi** :
  - La garde ne refuse qu'une configuration de rang 1, et toute reprise ouvre un rang supérieur à 1. Aucune suite légitime ne demande donc une seconde configuration de rang 1 après une reprise.
  - La dispense ouvre une fenêtre entre deux moments :
    1. la ligne de GO d'une reprise est inscrite, au titre de la règle d'octroi, sans mot neuf de Lazar ;
    2. la configuration de rang 2 qu'elle ouvre n'est pas encore inscrite.
  - Pendant ce temps, l'inscription de rang 1 d'origine compte comme « suivie d'une reprise », et plus rien ne bloque. Une configuration de rang 1 présentée avec un autre dossier des arrêts passerait la garde. On aurait une seconde première livraison, sans mot de Lazar, que seul le registre montrerait.
  - Une fois la configuration de rang 2 inscrite, elle bloque à son tour, puisqu'elle n'est suivie de rien. La fenêtre est donc étroite, mais réelle.
- **Ce qui le réglerait** : retirer la dispense. Une configuration de rang 1 ne passe alors que si toute autre inscription est retirée par une ligne de type « révocation », donc par un mot de Lazar. Rien de légitime n'est bloqué, puisque les reprises ouvrent des rangs supérieurs à 1. La garde devient aussi plus simple, comme le dit le rédacteur. Il faut ensuite retirer de 8.4 l'artefact qui en dépend (« une ligne … qui porte la phrase d'accord … sans citer l'empreinte … ») ou le récrire.

## 6. Mineurs

- **M-1. Confronter les vingt lectures refaites à celles d'origine** (réserve 2), sans arrêt. Un écart rend les grandeurs de l'étape (n) « non rapportées : livraison refaite incohérente », et la table C reste intacte. Les nombres se comparent en fractions exactes.
- **M-2. Consigne de tenue pour la ligne de l'écart à R9.**
  - La porte n'ouvre pas si une ligne entrée depuis l'état figé « nomme la ligne de l'écart ». Une ligne écrite plus tard qui citerait GO-2026-11-19-97 pour une autre raison bloquerait donc le tirage de la table. Ce pourrait être la ligne du mot « go recos » encore à inscrire, ou une consignation.
  - Il faut étendre la consigne de tenue du registre (13.2) : jusqu'au tirage de la table, aucune ligne ne nomme la ligne de l'écart, sauf pour la révoquer.
  - C'est à dire à la session principale avant qu'elle inscrive la ligne du mot « go recos ».
- **M-3. Le type « inscription » n'est pas dans la liste du registre.** L'en-tête du registre énumère les types lus par la garde de calcul, ainsi que « lecture complémentaire », « règle » et « décision ». Le type « inscription » des lignes de configuration n'y figure pas. La session principale doit le confirmer (demande 29), et le déclarer dans l'en-tête du registre comme les types de la session 14.
- **Pièces de demandes** : en retard de deux brouillons (réserve 5 de la note). Elles sont à mettre à jour avec C-1 et M-2.

## 7. Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillon 34 intact ; brouillon 35 et note | compagnons vérifiés (`0b6413d9…`, `e62b4cae…`, `9dbe7c66…`) |
| section 12 ; 7.1 à 7.8 ; section 10 | **identiques au brouillon 34** ; fiches 9 à 12 mot pour mot ; points 1 à 21 dans l'ordre |
| hypothèse au seuil ; 6.1 ; 6.3 à 6.8 ; 6.10 à 6.12 ; 8.1 à 8.3 ; 8.6 ; sections 9 et 11 | identiques au brouillon 34 |
| citations du brouillon 34 | 1 287, **aucune absente** |
| citations du brouillon 20 | 935 ; les deux mêmes absentes, déjà justifiées |
| consignes figées (3.2 et 3.3) | égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280…`, `ecf590eae0c0…` |
| titres | 53 ; seul le titre de niveau 1 change |
| validateur `problemes()` | deux problèmes, les attendus |
| marque des cases | six lignes, toutes en 13.1, les mêmes cases |
| table d'en-tête, lignes neuves | empreintes égales : brouillon 34, sa note, ma vérification, relevé de la version 11, vérification du code de la version 11. La ligne du programme du constat en version 4 est du code, et je ne l'ai pas recalculée. **Aucune empreinte de fichier cloisonné prise.** |

## 8. Ce qui reste avant le scellement

Les listes de mes vérifications des brouillons 32, 33 et 34 valent toujours. S'y ajoutent ou changent :
- **C-1** : retirer la dispense ;
- **M-2** : la consigne de tenue pour la ligne de l'écart à R9, à dire à la session principale avant l'inscription de la ligne du mot « go recos » ;
- **M-3** : le type « inscription », à confirmer au registre ;
- **M-1** : la confrontation des lectures refaites, si elle est retenue ;
- **les pièces de demandes**, mises à jour : nom du programme du constat en version 4, quatrième cellule, gras, type, registre figé et registre courant donnés par le lanceur à la porte de l'écart.
- **La ligne de l'écart à R9 est inscrite** (GO-2026-11-19-97). Reste l'identifiant de la ligne du mot « go recos ».

## 9. Fichiers ouverts

- Le brouillon 35 : par différence ; les lignes citées en tête.
- Les brouillons 20 et 34, par programme.
- La note du brouillon 35.
- `verification-corrections-code-v11-bras-a-v1.md`, partie 2.
- Le fichier des fiches du brouillon 23, par programme.
- `src/controle_ia/prereg.py` (`problemes()`).
- Le registre des accords de la branche principale, par `git show` après un `git fetch`, seul appel réseau : son en-tête et la ligne 530.
- Pour leur seule empreinte : le relevé de la version 11 et la note du brouillon 34.
- Rien d'autre :
  - aucun code ;
  - aucun interne de moniteur ;
  - aucune clé ;
  - aucun appel de modèle ;
  - aucun sous-agent.
- Un seul fichier écrit, celui-ci, scellé ; rien committé.
