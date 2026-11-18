# Contre-lecture du relevé d'idées de la course de l'organisme d'idéation sur la question du mentor Heimersheim (3 novembre) — v1

- **Écrit** le 18 novembre 2026 par un contre-lecteur neuf (règle R2 : Claude Opus 5.5, sous-agent qui n'a pas écrit la note), sous l'autonomie GO-2026-11-18-05 et le « go » de Lazar aux quatre lectures sans dépense de l'inventaire (R-3168, R-3170).
- **Note contre-lue** : `docs/notes/quatre-lectures-inventaire-v1/mentors-heimersheim-v1.md`, empreinte `3978c4937f7ef70dd911313c32b61bad41a3e969cd141efa55bba243d566d7dd` (égale à son compagnon, recalculée à l'ouverture et à la fin : la v1 n'a pas été touchée).
- **Sources rouvertes** : la branche `donnees/course-heimersheim-v1-run`, commit `a64f9af` (`a64f9afe9597e145111c95785a5f883d358e21f0`), extraite seule sous `…/scratchpad/quatre-lectures/extrait/course-heimersheim-v1-run/` ; chemins ci-dessous relatifs à `donnees/course-heimersheim-v1-run/run-20261103-0830/` dans cette branche, sauf mention. Au dépôt : l'inventaire `docs/notes/inventaire-collisionneurs-organismes-v1/inventaire-v1.md` (`b49dc246…`, recalculée), `sorties-non-lues-v2.md` (`2fb208d4…`, recalculée), `inventaire-idees-organisme-v7.md` (`056adb7f…`, recalculée), `registres/depenses.md` l. 330-335, `registres/decisions.md` (R-1116, R-1120, R-1131).
- **Cadre tenu** : lecture seule ; aucune dépense, aucun appel de modèle, aucune clé lue ni affichée, aucun commit, aucune poussée, aucun `git fetch`. Rien sous `diag/` ; aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis ; aucune autre branche que l'extrait. Les verdicts des juges (`course/generation-1/coffre/verdicts-*.json`), les lectures d'étiquettes, la clé d'anonymisation, `classement.json`, `consommations.json` et `manifeste-fin.json` n'ont pas été ouverts. De la clé des sessions (`coffre/hq1-cle-sessions.json`), seuls les noms d'entrée ont été comptés.

## Verdict : **à corriger**

Les corrections sont toutes de fait (citations de ligne fausses, une affirmation trop large sur une fiche, un compte d'appels mal attribué, des pièces omises). Aucun avis de modèle n'est présenté comme un fait, aucun chiffre d'article comme vérifié, aucune zone vierge comme un trou, et le cloisonnement est tenu. J'ai donc écrit la version 2 (`mentors-heimersheim-v2.md`, dans ce dossier, scellée), qui dit en tête qu'elle est du contre-lecteur et ce qu'elle change.

### Corrections (liste exacte)

1. **L'exposant de la superellipse (§ 2.2, § 3 point 1, et le point 3 du rendu)** : la fiche de Kimi `f9b030b7715e3` (`course/generation-1/fiches.json`, l. 744) **ne mesure pas le plan évaluation-registre**. Elle compare deux autres plans : la direction d'évaluation contre une « non-caractéristique », et la direction de registre contre la même (champ `epreuve`). Le titre du § 2.2 et la phrase « les cinq espèces : … dans le plan évaluation-registre » sont donc trop larges. La comparaison de sens « Opus et Kimi : deux traits ; Fable et Argon : une seule facette » met côte à côte des valeurs prises sur des plans différents. Sur le même plan, la divergence tient : Opus (2,2 à 2,5, l. 95) contre Fable (2,0 à 2,15, l. 188) et Argon (2,02 à 2,15, l. 537). Astra (l. 328) ne prédit pas de valeur de l'exposant, mais une corrélation de rang. La ligne de Kimi dans le tableau du § 2.2 disait juste (« plans formés avec une même « non-caractéristique » ») ; c'est la synthèse qui la contredit.
2. **Lecteurs d'étiquettes (§ 1)** : « deux lecteurs d'étiquettes (Opus et Astra) sur chaque fiche » est inexact. Chacun a fait 78 lectures (trace agrégée, `par_role`), soit les **39 propositions** une fois par bras de mariage. La clé des sessions compte, par noms d'entrée, 39 lectures « concepts » et 39 « vocabulaire » par lecteur, toutes sur des propositions, aucune sur une fusion (comptage du contre-lecteur). Les juges, eux, ont bien lu les 46 fiches (46 appels chacun).
3. **Empreintes (en-tête, l. 5 de la note)** : « toutes les pièces lues … égales … à la liste scellée par le lanceur » est inexact. La trace agrégée (`be3f9d9f…`), le rapport de la session fille (`43ab6a25…`), le journal de lancement et le journal de préparation **ne figurent pas** dans `empreintes-run-heimersheim-v1.txt` (149 lignes, `a18c4c09…`, égal à son compagnon). Seuls leurs compagnons les attestent, et j'ai vérifié qu'ils sont égaux. Les journaux et états finaux des relais sont dans la liste, mais sans compagnon. Les autres pièces citées par abréviation (fiches `1c262473…`, fusion inachevée `79ff7d31…`, journal d'aiguillage `da725231…`, clé des bras `128c690c…`, manifeste de départ `9f573ca6…`, bilan `ad36aafd…`) sont égales à la fois à leur compagnon et à la liste.
4. **Citation de ligne (§ 3 point 12)** : `sorties-non-lues-v2.md` § 2, « l. 23 », pour les tours v9 du collisionneur : la ligne qui le dit est la **l. 29**. La l. 23 est la ligne de la course Heimersheim.
5. **Citation de ligne (§ 4.4)** : « `depenses.md` l. 333-334 disent « à relire aux tableaux de bord » » : ce sont les **l. 332 et 334**. La l. 333 (départ de la course) ne le dit pas.
6. **Oubli de pièces (« Ce que j'ai lu »)** : la v1 ne déclare ni lues ni non lues `course/generation-1/accords.json` (`315a3adb…`, dans la liste scellée : n = 39 par bras, 0 exclue, champ « jaccard_moyen » 0,65 pour le bras basique et 0,73 pour le bras Gu-Krenn ; d'après ses champs, un accord entre les deux lecteurs d'étiquettes, mais c'est ma lecture, le code n'a pas été lu), `coffre/hq1-paires-par-bras.json` (huit paires, égales à la clé des bras), `coffre/hq1-emplacement-sessions.json`, les cinq `controle-*.json`, `verification-avant-lancement.json`, `manifeste-lancement-heimersheim-v2.json`, `manifeste-depart-lanceur-heimersheim-v1.json` et `course/generation-1/empreintes-sortie.txt`. Aucune ne porte de verdict, et rien de ce que j'y ai vu ne change le relevé. La v2 les inscrit.
7. **Cohérence interne (§ 3 point 10)** : trois fiches sont listées « sans doublon » alors que les points 4 et 7 les rangent déjà parmi des voisines : le rebond des couches tardives (Argon `fcd6a3b9b6c7a`), la dérive sur génération longue (Argon `fe02fc80230a9`) et la réparation des moments (Astra `fd9d13237cc76`). La v2 les sépare (« sans fiche jumelle, mais rangées parmi des voisines »).

## 1. Citations rouvertes

**Toutes** les citations « F:l.N » et toutes les attributions d'espèce ont été rouvertes : 46 sur 46. J'ai lu, par programme, la ligne où commence chaque fiche dans `fiches.json`, puis les champs `meta.fournisseur`, `meta.proposeur` et `meta.origine`. **Les 46 lignes et les 46 espèces sont justes.** On compte 39 propositions (Argon 8, Astra 8, Kimi 8, Opus 8, Fable 7) et 7 fusions, toutes de fournisseur Claude (le metteur des fusions est Fable selon la trace, `metteur-fable` : 8 appels).

J'ai aussi relu en entier le contenu (titre, hypothèse, épreuve, prédiction) des 46 fiches pour contrôler les résumés. En voici vingt, tirées sans ordre de préférence, avec ce que dit la source :

| fiche | F:l. | espèce (source) | contrôle du résumé |
|---|---|---|---|
| `f002e9b16b5a3` | 2 | Astra | juste (composante de certitude, métadonnée sans rapport) |
| `f06d49ff9f5b1` | 25 | Astra | juste (seuil translaté, pente intacte, lapsus) |
| `f094e07319bd7` | 48 | fusion ; parents `f06d49ff9f5b1`, `f4228bed2c1bf` (clé des bras) | juste |
| `f098edacd8ea0` | 72 | Fable | juste (marqueurs « indices de type » et `idx`) |
| `f124248feef2a` | 118 | Argon | juste ; 13,7 contre 1,6 points sur 49 milliards de paramètres, cité de Hua et al. par la fiche, marqué « non vérifié » |
| `f1267b8246715` | 164 | fusion ; parents `f06d49ff9f5b1`, `f566b5346d1c6` | juste ; « semble peu documentée : c'est une question » est bien dans la fiche |
| `f33db03e129a2` | 258 | fusion ; parents `f566b5346d1c6`, `f7c590f63cf24` | juste ; « est-ce vierge ou mal cherché ? » est bien dans la fiche |
| `f3e84b19b121a` | 282 | Astra | juste (D positif dans [+15 ; +30] sous l'hypothèse « registre ») |
| `f4e497cda26ef` | 351 | Kimi | juste |
| `f5999b0107deb` | 420 | fusion ; parents `fa5bde6b7037f`, `fb26b3699c88e` | juste ; « 80-86 % → < 11 % » cité de A.1 par la fiche, marqué « non vérifié » |
| `f5a0cf42d0d2d` | 444 | Argon | juste |
| `f69dec0e2448d` | 467 | Fable | juste (batterie de 20 comportements) |
| `f6ad1d3587be0` | 490 | fusion ; parents `f9405f4e10a2e`, `fa5bde6b7037f` | juste ; Zou et al. 2023 et Needham et al. 2025 marqués « à vérifier » par la fiche |
| `f7109f9597906` | 560 | Fable | juste (rapport ≈ 8,6 calculé par la fiche) |
| `f84b294911deb` | 652 | Argon | juste ; « explique » est bien le mot de la fiche, rapporté comme avis |
| `f998012ada02e` | 721 | Opus | juste (Mahalanobis à la l. 726) |
| `f9b030b7715e3` | 744 | Kimi | ligne du tableau juste ; synthèse du § 3 fausse (correction 1) |
| `fa30d1f81a135` | 767 | fusion ; parents `f7109f9597906`, `f7e06604aa1bd` | juste (second marqueur « longueur des commentaires », l. 772) |
| `fe02fc80230a9` | 952 | Argon | juste ; 61,0 % → 46,5 % cité de B.11 par la fiche, marqué « non vérifié » |
| `ff3218b4701f1` | 1021 | Opus | juste ; facteur 2,8 cité de B.9, marqué « non vérifié » |

**Autres citations rouvertes**, toutes justes sauf celles des corrections 2 à 5 :
- les parents des huit fusions (clé des bras) et le décompte des parentés : Kimi 7, Astra 3, Fable 2, Opus 1, Argon 0 ;
- les axes : 14, 9, 6, 5 et 12 fiches ; Fable n'a aucune fiche sur l'axe « résidu non verbalisé », aucune fusion non plus ; les quatre autres espèces couvrent les cinq axes ;
- `meta.case` vaut « niveau-methode » pour les 46 fiches ;
- le journal d'aiguillage : version noyau-v54, 46 passeports, 0 refus, deux retenues « a_corriger » (`fb6f724bb3098`, empreinte `d1a3689e…`, catégorie « prédiction du témoin contredit contrôle » ; `f3c19a66837a9`, « Interaction a−b incohérente avec a et b ») ;
- la clé des sessions, l. 298 : `aiguillage/passe1/fb6f724bb3098` ;
- la fusion inachevée : la vérification arithmétique est juste (a dans [+0,5 ; +1,0] et b dans [−0,15 ; +0,15] donnent a − b dans [+0,35 ; +1,15], alors que la fiche écrit [+0,4 ; +1,0]) ;
- la mémoire anti-redite : 46 idées distinctes, seuil 0,6 ;
- la trace agrégée : comptes par rôle ; « passe_tableau » marquée « jouee » ; coûts et relais ;
- le manifeste de départ : bras de 37 concepts et de 33 termes, `aiguilleur_v53.py`, moissonneur non appelé, témoins plantés aucun, passe tableau « aucun appel, rien d'écrit », sessions hors de la sortie ;
- le rapport de la session fille, l. 15-17, 21-25, 31-37 ;
- le journal de préparation, l. 1 et l. 274-275 (consigne de l'aiguilleur v2 `a52b0b84…`), l. 270-306 ;
- les montants : 10,026275 USD réglés ; 10,024097 USD à la trace ; l'écart de 0,002178 USD est égal au coût des cinq contrôles (journal de lancement, `par_etape.controle`) ; somme des relais 10,026275 ;
- le devis (23,61, 203,15 et 244 USD) ;
- `registres/depenses.md` l. 332 et 334 ; R-1120 (commit et 167 fichiers) ; R-1131 n° 411 (la fiche « à corriger » sans contenu) ;
- l'inventaire : § A ligne 74 à la l. 119, § B point 4 à la l. 136, § E nœud 3 à la l. 162 ;
- l'inventaire des idées v7, l. 168 (ROL-018) ;
- les 168 fichiers propres à la branche (167 + 1).

## 2. Avis, état de l'art, zones vierges

- **Avis présentés comme faits** : aucun. Chaque résumé est posé comme « avis du proposeur », et les mots forts des fiches sont rapportés comme tels (« prouvant l'absence de séparation », Argon ; « explique », Argon). La lecture de `meta.case` comme classe de l'aiguilleur est marquée « non vérifiée dans le code ». La huitième fiche de Fable est marquée « déduction, non vérifiée ». Elle est d'ailleurs bien étayée : 39 fiches + `fb6f724bb3098` (fournisseur Claude) = 40 = 5 × 8, avec Opus à 8. Je laisse l'affirmation telle quelle.
- **Règle R7** : tous les chiffres d'articles que rapporte la note sont marqués « non vérifié », ou rattachés à une fiche qui les marque « à vérifier » : Hua et al. 13,7 contre 1,6 ; « 80-86 % → < 11 % » ; 61,0 → 46,5 ; facteur 2,8 ; exposants 2,3 et 2,05 de B.8. Aucun PDF n'a été ouvert, ni par la note ni par moi.
- **Règle R8** : les quatre fiches qui disent une zone peu documentée (`f1267b8246715`, `f33db03e129a2`, `f6ad1d3587be0`, `f31e7e1983653`) sont rapportées comme des questions. Le § 3 point 12 (aucun tour du collisionneur sur Heimersheim) est un constat de recensement, pas une zone vierge du champ.
- Une nuance de forme, laissée en l'état : « distance de moyenne maximale », pour la fiche `ff4a374f7d6b9`, traduit l'écart moyen maximal entre distributions. Cela ne change pas le sens.

## 3. Cloisonnement

- **Famille 2** : la seule pièce de la famille 2 est le compagnon d'empreinte `docs/notes/ideation-organisme-v1/question-mere-reponses/consigne-argon-question-mere-v3.txt.sha256` (102 octets, taille vérifiée). La note le dit exclu, sans contenu. Je ne l'ai pas ouvert non plus.
- **Noms seuls** : j'ai vérifié par leur seul nom le module du manifeste de code et les commandes « a1bis » des journaux de relais. La note ne résume aucun contenu de la famille 2.
- **Famille 1** : rien. La recherche de mots de la note (sabotage, évasion, contournement, attaque, adversaire, dissimulation, tromperie, moniteur, furtif, discret) refaite sur `fiches.json` et `fusions-inachevees.json` rend 0 ligne. Les 46 fiches et la fusion inachevée, lues en entier, portent toutes sur la mesure de la conscience d'évaluation d'un modèle ouvert et sur le pilotage contre elle.
- **Embargo** : aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis n'est cité. Aucun verdict de juge n'est repris. Aucun rang de `classement.json` n'est reproduit, même si la note dit en avoir vu la tête.

## 4. Oubli

- **Cellules et fiches** : aucune ne manque. On a les 46 fiches classées, la fusion inachevée `f3c19a66837a9` et la proposition « à corriger » sans contenu `fb6f724bb3098`. Le journal d'aiguillage ne retient que ces deux-là.
- **Espèces** : aucune ne manque, les cinq sont là, comme proposeurs et dans leurs rôles. Les absences sont relevées au § 4.1 de la note.
- **Pièces** : les pièces omises sont nommées à la correction 6.
- **Remarque sans correction** : R-1131 (n° 411), que la note cite pour la fiche « à corriger », consigne aussi qu'un « pilote de l'exposant p » du programme était alors « non scellable en l'état ». Ce pilote touche le thème du § 3 point 1, où les cinq espèces se servent de l'exposant. Je n'ai rien ouvert de plus. C'est un rapprochement à faire par qui reprendra le thème, pas une erreur de la note.

## 5. Version 2

`docs/notes/quatre-lectures-inventaire-v1/mentors-heimersheim-v2.md` : je l'ai écrite en appliquant à une copie de la v1 dix remplacements exacts, chacun présent une seule fois. Elle porte en tête la mention qu'elle vient du contre-lecteur et la liste de ce qu'elle change, et chaque ajout est marqué « (contre-lecteur) ». Le reste est repris à la lettre. La v1 est inchangée (empreinte recalculée après l'écriture de la v2).
