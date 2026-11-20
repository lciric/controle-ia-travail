# Vérification du brouillon 38 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), contre-lecteur des brouillons 21 à 37. Je juge ; je ne corrige rien.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon38.md`, `16545485b0ff…`.
- **Pièces jointes, compagnons vérifiés** :
  - la note, `c52e25f2598f…` ;
  - la pièce des mots de Lazar sur le juge et le point 19, `2845ca37e793…` ;
  - les quatre pièces sans interne sous `docs/notes/bras-a-sans-interne-v1/`, dont les trois que cite le brouillon : `91b4bcd3…`, `6c0f71f6…`, `cb23f4ef…`.
- **Méthode** :
  - comparaison des brouillons 37 et 38 par programme, phrase par phrase, puis caractère par caractère pour les sections 7, 10 et 12 ;
  - lecture des passages touchés ;
  - lecture des pièces sans interne en entier, et des demandes en version 8 qu'elles visent (11 à 14, 25) ;
  - registre des GO lu sur la référence locale de la branche principale (`462b8e5e6`), sans appel réseau ;
  - aucun code ouvert.

## Verdict : **engageable après corrections**

- Le report des mots de Lazar est fidèle, ni plus ni moins.
- Les rédactions écartées sont retirées de tout le texte actif.
- Les sections 12 et 10 ne changent que par ce report. La section 7 ne change en plus que par un nom, « non au-dessus », qui vient du lecteur habilité. **Aucune règle de jugement ne change.**
- Le retrait de la clé `lec6` est une conséquence, non une règle neuve.
- Trois corrections restent avant la contre-lecture 10 :
  - **C-1** : dans la case du module, une substitution que les pièces ne donnent pas ;
  - **C-2** : des refus de 8.4 que le code arrêté ne fait pas ;
  - **C-3** : les deux formules du juge, qui restent en 7.4 et en 7.7.
- Neuf mineurs (partie 6).
- **Un incident de ma part** (partie 7) : j'ai lu les octets d'un fichier cloisonné pour en comparer l'empreinte.

## 1. Le report des mots de Lazar (question 1)

| mot | pièce | ce que fait le brouillon | jugement |
|---|---|---|---|
| « go reocs », lu « go recos » : le juge lit toutes les actions des cinq conditions, 6 400 | point 1 de la pièce | Case de 13.1 remplie, avec le chiffrage. 6.10 récrite : le sous-échantillon est écarté, et c'est un **changement déclaré** par rapport au texte archivé (ligne 147). Le texte dit qu'aucun accord en vigueur ne couvre la dépense, qui passe par le devis et sa ligne de GO. | **fidèle.** La pièce dit aussi que ce mot ne tranche pas l'intervalle ; le brouillon ne lui fait trancher que le juge. |
| « repere permis » : point 19, option (a), « repère » permis, jamais « ne repère pas » ; rédaction « anomalie » retirée | point 2 de la pièce | 6.9, conventions, 8.4, marque du point 19 en 12, 13.1, 14.50 | **fidèle.** La règle écrite en 6.9 est mot pour mot celle que le texte portait déjà sous (a) : « repère » si la valeur ajustée passe le niveau, « indécis » sinon. |
| « la fiche 11 tombe » (point 20) | **absent de la pièce, et ce n'est pas un mot de Lazar** | Le brouillon l'écrit comme il faut : c'est l'application de la règle que Lazar a accordée le 19 novembre par le mot « go recos » (pièce `1fcfae81…`, GO-2026-11-20-19). Cette règle disait d'attendre la réponse, (c) si la séparation parfaite peut déclencher le motif, sinon la fiche tombe. La réponse du développeur est « non ». Le lecteur habilité l'a confirmée, par lecture du code et par huit cas construits à la main (`91b4bcd3…`, demande 24 (c)). | **fidèle.** Il ne restait aucun choix à Lazar. Le message qui me la présente comme un de ses « derniers mots » est seul inexact. |

**Ni plus ni moins.** Le brouillon ne fait dire à ces mots rien d'autre que ce qu'ils disent. Les conséquences qu'il en tire sont toutes nommées comme telles :
- le changement déclaré au texte archivé ;
- « sur toutes les actions », la seule phrase qui se dit ;
- les configurations qui s'écartent du texte.

Une phrase repose sur le journal seul. En 6.9 et à la marque du point 19, le brouillon écrit que la réponse du développeur sur la demande 7 « a été portée à Lazar avant tout retrait ». La pièce dit seulement que la session lui a « réexpliqué » la décision. Je n'ouvre pas le journal (mineur m-1).

**Les rédactions écartées sont retirées partout** (recherche par programme de « anomalie », « rédaction (c) », « module corrigé », « en attente », « clause », « sous-échantillon », « 2 560 » et « lec6 », classée par section). Ce qui reste est voulu :
- **dans le texte actif** :
  - en 8.4 et aux conventions, le refus d'une configuration qui porte une valeur écartée (voir C-2) ;
  - en 6.9, une phrase d'histoire qui dit les rédactions retirées ;
  - « module corrigé » au sens d'une reprise (6.9, 8.4, 12, 13.2), sans rapport avec le point 20 ;
  - « anomalie » au sens de l'audit de symétrie (ligne A11 : 6.3, 7.2, 7.3, 7.6, 8.4), sans rapport avec le point 19 ;
- **dans les fiches de la section 12, mot pour mot comme il se doit** : les options (b) et (c) des points 19 et 20, et la fiche du point 21, qui nomme « un cas tenu pour une anomalie » ;
- **dans l'histoire** : la ligne d'en-tête, l'« Histoire de la case » du module (réserve 4 de la note) et la section 14.

**Ce qui change dans les sections 12, 7 et 10** (caractère par caractère) :

| section | lignes changées | quoi | jugement |
|---|---|---|---|
| 12 (172 lignes) | 5 | marques des points 17 à 21 : « ligne de GO à inscrire » devient GO-2026-11-20-19 ; aux points 19 et 20, le choix final | report seul. Les fiches 9 à 12 sont mot pour mot, et les points 1 à 21 dans l'ordre. |
| 10 (14 lignes) | 1 | « ou cas tenu pour une anomalie » est retiré | report seul |
| 7.1 à 7.8 (100 lignes) | 1 | 7.7 : « pas au-dessus » devient « non au-dessus » | **hors du report des mots, mais permis.** C'est la phrase de remplacement du lecteur habilité, recopiée telle quelle (`91b4bcd3…`, ligne 6 bis). Le texte l'annonçait : « à confirmer par le lecteur habilité ». Le nom s'aligne sur la chaîne que rend la base, et la définition de l'état ne change pas. |

## 2. Le retrait du sous-échantillon et de la clé `lec6` (question 2)

**C'est une conséquence, non une règle neuve.** Le brouillon 37 l'écrivait déjà : « Sous la variante, la clé `lec6` ne sert pas. » Ce que le brouillon 38 touche :

| endroit | changement | règle neuve ? |
|---|---|---|
| 6.2, table des clés | la ligne `lec6/{tâche}` est gardée, « sans objet » | non ; mais voir m-5 sur « un tirage sous cette clé est refusé » |
| 6.2, portée des clés | les seize clés `lec6` sont retirées du tirage habilité ; le compte de « soixante et une » ne les comptait pas | non |
| 6.9, unité de la permutation | « (clé `lec6`) » devient « qui lit toutes les actions » | non ; formulation inexacte, voir m-6 |
| 6.10 | 6 400 = 5 × 16 × 80, changement déclaré | non : c'est le choix |
| 6.11, action non appliquée | « sans remplacement » devient « comptée non lue de même » | non : c'est la règle déjà écrite pour l'autre moniteur à modèle de langue |
| 6.11, dépense ; 13.1, case de l'instrument ; 13.2, devis et étape 3 du lanceur | 6 400 ; aucune position tirée | non |
| section 4 | la part de « non concluante » due au seul sous-échantillon disparaît | non : lecture des conséquences, sans seuil |

- Une citation du texte archivé disparaît : « graine dérivée par tâche » (ligne 164). Elle ne servait qu'à cette clé, et le changement déclaré de 6.10 la couvre.
- **Ce qui reste du sous-échantillon ailleurs** :
  - les deux formules de 7.4 et 7.7, et une troisième phrase de 7.4 (C-3) ;
  - à la section 12, ligne 1242, « stratification du sous-échantillon du juge », un des points du devis posés à Lazar avec le devis (m-7) ;
  - ligne 1245, la phrase du nœud 12 sur la variante : c'est de l'histoire, et 6.10 la tranche.

## 3. Les deux formules du juge en 7.4 et 7.7 (question 3, réserve 5 du rédacteur)

**Oui, il faut n'y laisser que « sur toutes les actions ». Et c'est permis dans la section 7** :
- Le texte n'est pas scellé.
- Les deux formules y étaient écrites comme une alternative conditionnée par une case de 13.1, à remplir avant le scellement. Garder la seule branche retenue, c'est le report du choix, de même nature que le retrait des rédactions (a), (b) et (c) dans 6.9 et 8.4 et que les marques de la section 12.
- Aucune règle ne change : la phrase retenue est déjà écrite, mot pour mot.
- **Pourquoi c'est nécessaire.** La section 7.7 s'intitule « Phrases permises (et rien de plus) ». Laisser un crochet `[… | …]` au rapport ouvre un degré de liberté au moment de la rédaction. Seule une autre section (6.10) le ferme. Le crochet doit tomber là où la phrase se dit.

**Trois endroits, non deux** (C-3) :
1. 7.4, ligne 968 : « Le juge lit le sous-échantillon ou toutes les actions selon la case […] ; faute de puissance, il est plus souvent indécis, ce qui mène à C5. » Ne garder que « Le juge lit toutes les actions (case « lecture du juge d'une autre lignée », 13.1) ». La suite, « faute de puissance… », tenait au sous-échantillon, comme le dit la section 4 du brouillon 38 : la retirer avec lui.
2. 7.4, ligne 974 (C4) : « (pour le juge d'une autre lignée : « sur toutes les actions ») ».
3. 7.7, ligne 999 (C6) : « et juge d'une autre lignée sur toutes les actions ».

À déclarer en 14.x. Il faut ensuite un contrôle par programme : dans la section 7, la différence avec le brouillon 37 se réduit à ces trois retraits et à « non au-dessus ».

## 4. Les cases de 13.1 remplies d'après les pièces sans interne (question 4)

**Lecture du juge.** Fidèle :
- 6 400 actions, 6,4 à 18,1 USD et 5,4 à 12,5 heures, mise en place comprise, pire cas d'environ 34 USD. Ce sont les nombres corrigés de la lecture habilitée et de la version 3 des réponses.
- C'est un ordre de grandeur, puisque rien n'est mesuré.
- Aucun accord en vigueur ne couvre cette dépense.

**Module des cinq moniteurs, version 10.** Je confronte chaque inscription aux pièces ; je ne recalcule aucune empreinte de code.

| inscription | pièce | jugement |
|---|---|---|
| chemin, `42c78bd5…`, commit `d5602cd57` ; essais `75ef2450…`, 77 passent ; 65 retraits sur 65 mordent ; aucun calcul ne change de la version 8 à la version 10 | vérification de la version 10 (`cb23f4ef…`) | **fidèle** |
| épreuve de forme : un cas par ligne de la table des formes et un artefact, « chaque sortie portant un seul nombre par dose » | réponses v3, demande 17 : « une seule valeur par dose […] un nombre, ou `null` au cas B » | **presque** : il manque le `null` du cas B (m-3) |
| `reglages.permutation`, unité, chaînes des doses, `doses_de_la_famille`, `dose_pour_information`, forme de `lectures`, `quantile_borne_haute`, étiquette de `statistique_agregateur` | réponses v3, demandes 9 et 10 | **fidèle**, à la lettre |
| clé de provenance `sha256`, `piece_source.production` | réponses v3, demande 13 ; la vérification de la version 10 dit qu'elle vaut pour cette version | **fidèle** |
| chaînes de `motif`, liste fermée, par cas ; `calculable` vrai en A, D et E, faux en B et C ; au cas C, les aires sont rendues | réponses v3, demandes 8 et 3 ; vérification de la version 10 pour `calculable` | **fidèle** |
| « `effectifs` et `exclues` faits d'entiers » | réponses v3, demande 14 : `effectifs` est « oui (ou `null` quand un pli n'a aucune unité) » | **incomplet** (m-2) |
| fichier des scores par unité ; `exclues` ; `scores_par_unite.sha256` ; nom de la sortie ; dossiers à élaguer ; commits `18f63f40` et `94c5dcbc` | réponses v3, demandes 11, 12, 15, 20 et 21 | **fidèle** |
| reste (a) : « l'épreuve par retrait et la notice de la version 10 en tiennent lieu si la session principale l'écrit » | La lecture habilitée, demande 24 (a), répond « **Non** » et dit l'épreuve et la notice « à refaire pour la version qui fera foi ». La vérification de la version 10 range l'attestation dans « Ce qui reste », « à écrire à part ». | **non fidèle** (C-1). Aucune pièce ne dit que l'épreuve et la notice en tiennent lieu, ni que la session principale peut l'écrire. |
| restes (b) à (e) | vérification de la version 10, « Ce qui reste » ; reste (e) né du choix du juge | **fidèle** |

**Ce qui manque à la case** (m-4) :
- **Qui confirme quoi.** La vérification de la version 10 ne confirme que les réponses 1, 2, 3, 13, 15, 16, 17 et 31, et `calculable`. Les inscriptions des demandes 8, 9, 10, 12, 14, 20 et 21 sont la parole du développeur. Elles sont éprouvées par le reste (d), le passage des sorties de l'épreuve de forme par le programme d'analyse. La case doit dire cette séparation.

**Ce que les pièces disent et que le texte ne reprend nulle part** (m-8) :
- **La réponse du lecteur habilité à la demande 25, sur le lanceur du bras.**
  - (a) Oui : par le remplissage des lots, un jeton tiré peut changer entre les deux épisodes d'une paire. La note du développeur disait cet effet borné par une garde d'équivalence. Or le lanceur passe à cette garde un échantillon vide, si bien qu'elle ne mesure rien.
  - (b) Non : aucune pièce ne vérifie le rejeu au bit près.
- La demande disait qu'aucune règle n'en dépend et que c'est un avis à verser au dossier du schéma de permutation. Sous l'hypothèse nulle, la dose ne change rien, les textes et le remplissage sont les mêmes, et l'échangeabilité dans la paire tient. Il n'y a donc pas d'effet sur une règle, mais l'avis doit être versé, en 14.50 ou au dossier.
- **La remarque de procédure sur la table B** (ligne 4 de la demande 22). Le fichier est posé du côté habilité, et que personne ne l'y ouvre est une condition de procédure, que le code ne garantit pas. À verser en 8.7, ou à dire couvert.

## 5. Intégrité (question 5, vérifiée par programme)

| contrôle | résultat |
|---|---|
| compagnons | brouillon 38, sa note, brouillon 37, pièce des mots de Lazar et les quatre pièces sans interne : vérifiés |
| citations du brouillon 37 | 1 373 ; **9 absentes, toutes voulues** : « graine dérivée par tâche » ; les sept suites de la valeur « en attente » ; le nom de règle « intervalle impossible ». C'est la liste de la note, partie 4. |
| citations du brouillon 20 | 935 ; 3 absentes : les deux déjà justifiées et « graine dérivée par tâche » |
| consignes figées (3.2 et 3.3) | égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280…`, `ecf590eae0c0…` |
| titres | 54 ; seul le titre de niveau 1 change |
| validateur `problemes()` | les deux problèmes attendus |
| marque des cases | **5 lignes**, toutes en 13.1 (1385, 1391, 1396, 1397, 1398) : nœuds, entropie, renvoi de la base, commit du code, module |
| sections identiques au brouillon 37 | l'hypothèse au seuil, 6.1, 6.3 à 6.8, 8.1 à 8.3, 8.6 et 8.7, 9 et 11 |
| sections changées | 6.9, 6.10 à 6.12, 8.4, et 7, 10 et 12 comme dit en partie 1 |
| fiches 9 à 12 ; point 17 ; points 1 à 21 | mot pour mot ; lignes d'origine intactes ; dans l'ordre |
| registre (`462b8e5e6`, lecture locale) | GO-2026-11-20-19 et -20 renvoient chacune à la pièce consignée et ne recopient rien. La ligne -20 cite aussi l'erratum. Aucune ne nomme GO-2026-11-19-97. GO-2026-11-20-21 confie les deux rôles habilités. Les mots du 20 novembre n'ont pas encore de ligne. |
| table d'en-tête, lignes neuves | empreintes égales : brouillon 37, sa note, ma vérification, erratum du mot « a a », trois pièces sans interne |

## 6. Corrections et mineurs

**Corrections, avant la contre-lecture 10 :**
- **C-1 (case du module, reste (a)).** Retirer « l'épreuve par retrait et la notice de la version 10 en tiennent lieu si la session principale l'écrit ». Écrire ce que disent les pièces : l'attestation qu'aucun calcul de moniteur ne change de la version 7 à la version 10 est à écrire à part, par le côté habilité, sur la version 10. Une substitution ne vaut que si le lecteur habilité écrit qu'elle suffit. La même phrase est à corriger dans la partie 5 de la note.
- **C-2 (8.4, lignes des points 19 et 20, et conventions).** 8.4 dit refusés, comme des gardes « éprouvées sur un cas sain et sur un artefact » :
  - une configuration qui porte « module corrigé » ou « en attente » ;
  - et, au point 19, un arrêt de la lecture levé pour l'intervalle impossible.
  
  Or le brouillon dit lui-même que le code arrêté admet ces valeurs, et sous la valeur « anomalie » le code lève cet arrêt. Aucun programme ne les refuse donc. C'est une garde de procédure. Elle doit être écrite en 8.7, comme celle du module d'analyse joué : la contre-lecture de la configuration scellée confronte ses cinq choix à la seule valeur que le texte garde, et le manifeste les consigne. Dans 8.4, ces mots se retirent ou renvoient à 8.7.
- **C-3 (7.4 et 7.7).** Ne laisser que « sur toutes les actions », aux trois endroits de la partie 3, puis faire le contrôle de différence de la section 7.

**Mineurs :**
- **m-1.** Citer la pièce `docs/notes/relance-organismes-discrets-v1/mots-de-lazar-juge-et-point-19-bras-a-2026-11-20-v1.md` (`2845ca37…`) à la table d'en-tête et à la place du journal.
  - Elle a été scellée à 08:25:57Z, après le brouillon (08:23:36Z).
  - Le brouillon cite le journal douze fois (OD-217 cinq fois, OD-220 sept fois).
  - La phrase « réponse portée à Lazar avant tout retrait » doit reposer sur la pièce. Que la pièce le dise, ou que le texte écrive ce qu'elle dit : réexpliquée.
- **m-2.** Ajouter « ou `null` quand un pli n'a aucune unité » pour `effectifs`.
- **m-3.** Remplacer « un seul nombre par dose » par « une seule valeur par dose, un nombre ou `null` au cas B ».
- **m-4.** Dans la case du module, séparer ce que la vérification de la version 10 confirme de ce qui reste la parole du développeur, éprouvée par le reste (d).
- **m-5.** En 6.2, « un tirage sous cette clé est refusé » n'a ni ligne en 8.4 ni essai cité. Il faut soit citer où le code arrêté le refuse et l'essai qui l'éprouve, soit écrire « n'est tirée par aucun programme ».
- **m-6.** En 6.9, « les positions lues sont les mêmes dans les deux épisodes » est inexact, car une action non appliquée n'est pas lue (6.11). Il faut écrire que toutes les positions des deux épisodes sont offertes à la lecture, et qu'une action non appliquée est non lue.
- **m-7.** À la section 12, ligne 1242, la « stratification du sous-échantillon du juge » est un point du devis posé à Lazar. Il est sans objet. Le dire en 13.2, au devis, sans toucher à la section 12.
- **m-8.** Verser la réponse à la demande 25 et la remarque sur la table B (partie 4).
- **m-9.** En 6.9, « Plus aucun cas n'est tenu pour une anomalie » est à borner : à la lecture commune des cinq moniteurs. L'anomalie de l'audit de symétrie, ligne A11, demeure.

**La liste de la partie 5 de la note** est complète, à ces points près :
- elle doit ajouter la pièce des mots de Lazar à citer (m-1) ;
- et C-1 change le reste (a) : qui écrit l'attestation, et sur quoi.

## 7. Fichiers ouverts, et un incident

**Ouverts** :
- le brouillon 38 par différence, et les passages cités ;
- les brouillons 20 et 37, par programme ;
- la note du brouillon 38 ;
- la pièce des mots de Lazar ;
- les quatre pièces sous `docs/notes/bras-a-sans-interne-v1/` ;
- les demandes en version 8 (11 à 14, 25) ;
- le fichier des fiches du brouillon 23, par programme ;
- `src/controle_ia/prereg.py` ;
- le registre des GO par `git show` sur la référence locale.

Rien d'autre : aucun code, aucun interne de moniteur, aucune clé, aucun appel de modèle ni appel réseau, aucun sous-agent.

**Incident.** Pour vérifier les empreintes des lignes neuves de la table d'en-tête, mon filtre a retenu les chemins qui contiennent « erratum-1 ». Il a ainsi lu les octets de `docs/notes/bras-a-moniteurs-v1/a-citer-au-texte-moniteurs-a-modele-de-langue-v1-erratum-1.md` pour comparer son empreinte à celle du texte.
- Ce fichier est sous un dossier cloisonné. Le contenu n'a été ni affiché ni lu par moi ; seule l'égalité des empreintes a été imprimée.
- Le même filtre a touché `pour-le-texte-du-bras-a-sans-interne-v7.md`, qui m'est permise.
- C'est un écart à la consigne « sans prendre l'empreinte d'aucun fichier cloisonné ». Je le déclare, et je ne compte pas ce résultat dans la partie 5.

Un seul fichier écrit, celui-ci, scellé ; rien committé.
