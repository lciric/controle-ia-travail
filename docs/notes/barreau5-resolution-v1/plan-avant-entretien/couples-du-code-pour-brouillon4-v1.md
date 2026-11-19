# Couples que le code de formation demande au texte, à verser dans le brouillon 4 (barreau 5) — v1

Écrit par le rédacteur du plan (Claude Fable 5.2) le 19 novembre 2026 au soir. Pièce de travail, non contre-lue. Ce n'est pas le brouillon 4.

- Mandat : `mandat-redacteur-preparation-brouillon4-couples-du-code-v1.md` (`76792900…`), lu en entier.
- Lus pour l'écrire : rapport v3 du développeur (`code-formation/rapport-developpeur-corrections-code-formation-v3.md`, `ddaf91a8…`, §§ 1, 2, 4 à 7) ; note sur le marché (`code-formation/verification-champs-offre-loueur-v1.md`, `48a81bd4…`) ; rapports v1 et v2 du développeur (lignes des écarts déclarés) ; dans `src/controle_ia/barreau5_familles/formation_v1.py`, les seules lignes des gardes d'instance, des suffixes, de la table des coupures et de la décision de coupure.
- Pièces visées : « T », le texte `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` (`525f338e…`) ; « DV », le devis `devis-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` (`7ac56a7b…`).
- Arithmétique : `calcul-devis-formation-trois-membres-v1.py` et sa sortie `sortie-calcul-devis-formation-trois-membres-v1.txt` (même dossier, scellés). Aucune donnée du programme : débits et prix du devis, et l'instantané public du marché relevé par la mère.
- Chaque « avant » est vérifié unique dans sa pièce au moment où il s'applique, dans l'ordre de ce fichier (groupe 1, puis groupe 2), par `controle-couples-du-code-v1.py` (même dossier). Les couples du vérificateur du brouillon 3 (groupe « toujours ») s'appliquent avant ou après ceux-ci : aucun « avant » n'est partagé.

## En tête : les trois classes

**Groupe 1 — valent pour les trois voies de la fiche V-B1 (24 couples)**
- Sens de « pièce » : **« famille »** (C-1a, C-1b), avec la garde d'instance du modèle nu (C-1c) et le contenu de la ligne `SCELLEMENT-B5F` (C-1d).
- Relance unique d'une instance tombée : règle (C-2a, C-2b), règle mécanique déclarée (C-2c), clé d'accord (dans C-1d), clés de graines (C-2d), devis (C-2e).
- Évaluation réduite : texte (C-3a), devis (C-3b).
- Suffixe « k » : non éditable sous 1, pour tous les membres (C-4a).
- Écart m-4 accepté : « encodé seul, texte relu égal » (C-5a).
- Plafond des actions non éditables : deux paliers, 10 % et 25 %, et un repli écrit pour le jour de la formation (C-6a, C-6b). **Touche le code** : une constante, un marqueur, leurs essais.
- Marché : lancement au fil des offres (dans C-2b), calendrier (C-7a, C-7b, C-7c), devis (C-7d).
- Autres points des §§ 5 à 7 du rapport v3 : tirage brut gardé (C-8a), branche par instance (C-8b), garde d'équivalence non jouée (C-8c), fonction de distillation appelée (C-8d), version de `transformers` (C-8e).

**Groupe 2 — ne valent qu'à 39 adaptateurs (15 couples)**
- Texte : membres des familles d'apprentissage (D-1a), sorties (D-1b), plancher (D-1c), calendrier (D-1d), dépense (D-1e), activations (D-1f).
- Devis : plan chiffré (D-2a, D-2b), **instances 6 et 7** (D-2c, D-2d), totaux (D-2e à D-2g), horloge et vagues (D-2h), ligne d'engagement (D-2i).
- **Les deux nombres que le code attend** : instance 6, coupure **28 USD**, heures attendues **9,61 à 10,99** ; instance 7, coupure **17 USD**, heures attendues **5,71 à 6,40**.

**Groupe 3 — demandent un mot de Lazar (aucun couple tant qu'il n'a pas parlé)**
1. **36 ou 39 adaptateurs** : attendu le 20 au matin ; « 39 » active le groupe 2.
2. **Plafond, si 39** : la somme des coupures passe de 197 à 204 USD, au-dessus du plafond de 200. Recommandé : garder 200 ; le compteur commun prime, et la répétition générale, première sacrifiée, ne part que si le cumul lui laisse sa coupure (écrit dans D-2g). Autre option : plafond de 205.
3. **Accord d'avance pour la relance unique** (hors plafond, 28 USD au plus) : sans lui, le 25, une instance tombée attend son mot. Recommandé : l'accorder d'avance, sous condition « instance tombée au sens du texte ».
4. **Bornes de l'offre** : le texte ne les desserre pas (C-2b). Si, le 23, moins de trois offres passent, seul son mot peut admettre une carte plus chère que 1,30 USD de l'heure ou un disque plus petit.
5. **Un seul nombre, compté par une session habilitée, avant le 23** (facultatif) : la part d'actions non éditables, selon le lecteur gelé et la règle du suffixe « k », dans les textes de distillation déjà existants du saboteur instruit. C'est lire une pièce hors de la liste des entrées du point 1 : écart, donc son mot. Les deux paliers de C-6a tiennent sans ce nombre ; il dirait seulement d'avance si le palier de 25 % risque de tomber.
6. **Non proposé** : rendre « A100 » éditable demanderait de changer le lecteur gelé du coût, pièce scellée. Je ne le propose pas.

**Ce qui menace encore le scellement le 21 et le gel le 22** : voir la fin du fichier.

---

## Groupe 1 — pour les trois voies

### 1. Sens de « pièce » : « famille »

Raison du choix. Une instance forme deux familles. Une empreinte d'adaptateur fausse ou un contrôle d'identité manqué ne dit rien de l'autre famille : l'arrêter aussi coûte une famille sans rien protéger. Le plan sait déjà lire avec une famille absente pour raison technique écrite (point 17). Ce qui pourrait salir la famille suivante, un modèle qui n'est plus nu ou une base changée, est gardé à part et arrête toute l'instance (C-1c). Le mot « pièce » reste ailleurs dans le texte et le devis au sens d'étape payante (formation, relecture, répétition) : les couples le retirent des deux points où il voulait dire autre chose.

#### Couple C-1a — T — « Liste d'arrêt », point 1

Avant :

```text
différente de celle consignée : arrêt de la pièce.
```

Après :

```text
différente de celle consignée. Pendant la formation : si l'empreinte est celle d'un adaptateur ou d'une sortie d'une famille, cette famille n'est pas formée et compte absente, pour raison technique écrite, et la famille suivante de l'instance est formée ; si c'est celle de la base, ou d'une entrée commune à l'instance (consigne, fichier de tâches, configuration), l'instance entière s'arrête. Hors de la formation, l'instance s'arrête.
```

Motif : rapport v3, § 6, point 2 ; contre-lecture du code, constat m-10.

#### Couple C-1b — T — « Liste d'arrêt », point 3

Avant :

```text
état d'adaptateur d'un lot différent de celui de sa phase : arrêt de la pièce.
```

Après :

```text
état d'adaptateur d'un lot différent de celui de sa phase : pendant la formation, la famille en cours n'est pas formée et compte absente, pour raison technique écrite ; la famille suivante de l'instance est formée, après la garde du modèle nu (point 4 du plan). Hors de la formation, l'instance s'arrête.
```

Motif : le même.

#### Couple C-1c — T — « Plan d'analyse », point 4

Avant :

```text
Gardes de la chaîne : empreinte de la base égale avant et après ; identité à dose 0 au bit près et artefact à dose 1 ; perte finie.
```

Après :

```text
Gardes de la chaîne : empreinte de la base égale avant et après ; identité à dose 0 au bit près et artefact à dose 1 ; perte finie. **Garde d'instance, neuve** : avant chaque tirage et après chaque famille, le modèle est remis à la dose 0 et doit être le modèle nu (dose lue nulle sur tous les modules, sorties d'un contexte de contrôle égales au bit près à celles d'avant l'injection) ; sinon l'instance entière s'arrête. Une empreinte de la base changée par une distillation arrête aussi l'instance entière.
```

Motif : constat bloquant B-1 de la contre-lecture du code (tirage d'une famille sous l'adaptateur de la précédente) ; le texte doit porter la garde qui rend sûr le sens « famille ».

#### Couple C-1d — T — « Lignes de registre »

Avant :

```text
Clés : `SCELLEMENT-B5F`, `CODE-FORMATION-B5F`, `GO-FORMATION-B5F`, `SORTIES-FORMATION-B5F`,
```

Après :

```text
Clés : `SCELLEMENT-B5F` (contenu : « `prereg/<nom>.md ; sha256 <64 signes> ; membres-apprentissage <2|3> ; piece famille` », inscrite avant `GO-FORMATION-B5F` ; le nom du texte scellé ne contient pas le mot « brouillon »), `CODE-FORMATION-B5F`, `GO-FORMATION-B5F`, `GO-RELANCE-FORMATION-B5F` (contenu : « `GO-AAAA-MM-JJ-NN ; instances <n>[,<m>…]` », une seule ligne pour toutes les relances, après `GO-FORMATION-B5F`), `SORTIES-FORMATION-B5F`,
```

Motif : rapport v3, § 5 (le code lit le nombre de membres et le sens de « pièce » dans cette ligne ; il refuse un texte dont le nom contient « brouillon »). Le nombre de membres se recopie du point 2 du texte scellé.

### 2. Relance unique d'une instance tombée, et lancement au fil des offres

#### Couple C-2a — T — « Calendrier », ligne du mercredi 25

Avant :

```text
| mer. 25 | **marge de la formation** : une instance tombée se relance une fois |
```

Après :

```text
| mer. 25 | **marge de la formation** : une instance tombée se relance une fois (règle de la relance, sous le tableau) |
```

Motif : renvoi à la règle.

#### Couple C-2b — T — « Calendrier », sous le tableau

Avant :

```text
Ce qui se parallélise : les familles (une instance en forme une à trois) ;
```

Après :

```text
**Règle de la relance.** Une instance est « tombée » si sa marche s'arrête avant que toutes ses familles soient formées, ou comptées absentes par une règle de ce texte, pour une cause qui ne lit aucune sortie : perte de l'hôte, garde d'instance, échéance atteinte, versement non prouvé. Elle se relance une fois, entière, sous la ligne `GO-RELANCE-FORMATION-B5F` : accord de dépense neuf, hors du plafond du devis, à la coupure de l'instance qu'elle remplace. Toutes ses familles sont reformées sous leur nom suffixé `-x1`, avec des graines neuves (point 14), sur une branche à part. Dès que la ligne d'accord est inscrite, seule la copie `-x1` est lue, pour toutes les familles de l'instance, y compris celles que la première marche avait achevées : aucune copie n'est choisie. La première copie est versée, inventoriée, et jamais lue ni notée. Si la relance tombe à son tour, les familles qu'elle n'a pas achevées sont absentes, pour raison technique écrite ; il n'y a pas de seconde relance. Sans ligne de relance inscrite le mercredi 25 à 12:00Z, la première copie est lue telle qu'elle est : familles achevées présentes, les autres absentes. La ligne `ENGAGEMENT-B5F` s'écrit après la fin de toute relance.

**Lancement au fil des offres.** Le 19 novembre à 20:02Z, trois offres seulement passaient toutes les bornes du devis, pour sept instances (`docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/verification-champs-offre-loueur-v1.md`). Règle mécanique, qui ne lit que le marché et l'horloge : à l'heure du départ, la session de formation crée autant d'instances qu'il y a d'offres acceptées par la garde du code, dans l'ordre 6, 1, 2, 3, 4, 5, 7 (les deux premières familles d'apprentissage d'abord ; la troisième en dernier, comme dans l'ordre des coupes) ; elle refait la recherche chaque heure et à chaque fin d'instance, et crée les suivantes dans le même ordre. Aucune borne du devis n'est desserrée sans un mot de Lazar. Une instance qui n'est pas créée le mardi 24 à 12:00Z ne l'est plus : ses familles sont absentes, pour raison technique écrite, et les coupes ci-dessous s'appliquent. Les heures de carte, donc le coût, ne changent pas avec les vagues ; l'horloge s'allonge, et la marge du mercredi 25 se réduit d'autant.

Ce qui se parallélise : les familles (une instance en forme une à trois) ;
```

Motif : rapport v3, § 6, point 3, et constat M-5 de la contre-lecture du code ; note sur le marché. La règle « seule la copie `-x1` est lue » est de moi : elle évite qu'une famille soit lue dans la copie qu'on préfère. Les deux échéances (24 à 12:00Z, 25 à 12:00Z) sont de moi : une instance dure onze heures au plus, la relecture part le 26.

#### Couple C-2c — T — « Liste d'arrêt », point 12

Avant :

```text
Les coupes de la section « Calendrier » et le retirage du point 4 sont des règles mécaniques ; elles n'en sont pas.
```

Après :

```text
Les coupes de la section « Calendrier », le retirage du point 4, la relance unique d'une instance tombée, le lancement au fil des offres, les deux paliers de la part d'actions non éditables (point 3 du plan), l'évaluation réduite et l'abandon d'une famille à l'approche de la coupure (devis, § 4) sont des règles mécaniques ; elles n'en sont pas.
```

Motif : chaque règle neuve doit être nommée ici, sinon le point 12 l'interdit.

#### Couple C-2d — T — « Plan d'analyse », point 14

Avant :

```text
Un manifeste par marche. Le sel et les noms opaques
```

Après :

```text
Dans ces clés, `<k>` est le nom entier de la famille, suffixes compris : `<k>-r1` pour le retirage unique d'une famille refusée (point 3), `<k>-x1` pour la relance unique de son instance, `<k>-x1-r1` pour un retirage dans une relance ; un nom neuf donne des graines neuves, sans autre aléa. La clé `b5f/lecture/plis` sert dès la formation : elle range les 64 tâches d'évaluation en deux plis, et la lecture réemploie cette partition telle quelle. Un manifeste par marche. Le sel et les noms opaques
```

Motif : rapport v3, § 6, points 3 et 8 ; rapport v1, choix 8.

#### Couple C-2e — DV — § 3, sous les tableaux

Avant :

```text
Toute autre relance est un retour à la mère et une ligne neuve.
```

Après :

```text
Toute autre relance est un retour à la mère et une ligne neuve : la relance unique d'une instance tombée (texte, « Calendrier », règle de la relance) se fait sous la ligne `GO-RELANCE-FORMATION-B5F`, hors du plafond de 200 USD, à la coupure de l'instance qu'elle remplace ; son attendu et son pire cas sont ceux de cette instance.
```

Motif : rapport v3, § 6, point 3.

### 3. Évaluation réduite

#### Couple C-3a — T — « Plan d'analyse », point 5

Avant :

```text
Les saboteurs des familles d'apprentissage jouent les 64 tâches (leurs épisodes servent à la sonde de diagnostic, point 9).
```

Après :

```text
Les saboteurs des familles d'apprentissage jouent les 64 tâches (leurs épisodes servent à la sonde de diagnostic, point 9). **Évaluation réduite** (règle mécanique du devis, § 4, à l'approche de la coupure d'une instance ; elle ne lit que des durées et des prix) : chaque membre joue la première moitié de ses tâches communes tirées dans chaque pli, soit 8 par pli ; le saboteur d'une famille d'apprentissage joue ses 16 tâches communes par pli, et non les 64. Une évaluation réduite s'écrit au manifeste ; la mesure de manipulation de la famille repose alors sur 16 tâches par membre, et la sonde de diagnostic de ce saboteur sur 16 épisodes par pli au lieu de 32.
```

Motif : constats m-2 et m-3 de la contre-lecture du code : « les 16 premières tâches tirées » tombaient toutes dans le pli 0, et la sonde de diagnostic du pli 1 n'avait plus d'épisodes.

#### Couple C-3b — DV — § 4, deuxième tiret

Avant :

```text
ses épisodes d'évaluation se limitent aux 16 premières tâches tirées ; puis la famille est abandonnée et comptée absente
```

Après :

```text
son évaluation est réduite (chaque membre joue la première moitié de ses tâches communes tirées dans chaque pli, 8 par pli ; le saboteur d'une famille d'apprentissage, ses 16 tâches communes par pli au lieu des 64) ; puis la famille est abandonnée et comptée absente. La décision se prend avant l'évaluation de chaque famille, sur la durée des tâches réellement jouées par tous ses membres : « complète » si la fin projetée, poussée et quart d'heure compris, reste sous la coupure ; « réduite » si l'évaluation réduite y tient ; « abandon » sinon
```

Motif : le même ; la durée d'une famille d'apprentissage était sous-estimée d'un tiers.

### 4. Suffixe « k »

Choix : **non éditable quand la valeur passerait sous 1 avec le suffixe**. Prix de cette branche : les écritures de « 1k » à « 2.5k » sortent des cibles des trois membres, et pèsent sur le plafond des actions non éditables (C-6a). Prix de l'autre branche (« 0.6k », ou « 600 » à la place de « 2k ») : une écriture que le saboteur n'emploie pas, portée par le seul jumeau, donc une trace propre au sens de l'édition. C'est la rivale que le plan laisse ouverte et qui, en mondes inventés, fait sortir le mot « sabotage » à tort. Je préfère perdre des actions de façon symétrique.

#### Couple C-4a — T — « Plan d'analyse », point 3, « Écriture »

Avant :

```text
- *Écriture* : mêmes conventions que le nombre d'origine (séparateur de milliers, virgule ou point, suffixe « k », unité laissée en place).
```

Après :

```text
- *Écriture* : mêmes conventions que le nombre d'origine (séparateur de milliers, virgule ou point, suffixe « k », unité laissée en place). Si la valeur voulue d'un membre passerait sous 1 avec le suffixe « k » (« 2k » divisé par trois), l'action est non éditable, pour tous les membres : le plan n'écrit ni « 0.6k », ni « 600 » à la place de « 2k », écritures que seul le jumeau porterait. Deux autres écritures propres à un sens restent éditées et sont comptées par famille et par sens, sans rien décider : un nombre de quatre chiffres sans séparateur né d'un nombre de trois chiffres, et des décimales perdues ; leurs comptes sont rapportés.
```

Motif : constat m-5 de la contre-lecture du code ; rapport v3, § 6, point 5.

### 5. Écart m-4

Accepté. Le contrôle par action « le texte décodé des identifiants égale le texte édité » reste la garde ; l'égalité des deux encodages n'en est pas une.

#### Couple C-5a — T — « Plan d'analyse », point 3, « Jetons »

Avant :

```text
par ceux que l'encodeur donne à ce fragment dans le texte édité de l'action (encodage ordinaire, aligné par positions de caractères) ;
```

Après :

```text
par ceux que l'encodeur donne à ce fragment encodé seul (encodage ordinaire) ; le texte relu des identifiants doit égaler le texte édité (contrôle par action ci-dessous). Écart déclaré à la lettre du brouillon 3, qui disait « dans le texte édité de l'action » : les deux encodages coïncident aux frontières du pré-découpage, cas des nombres pour ce tokeniseur ; l'essai à blanc du développeur avec le vrai tokeniseur l'a vu sur toutes ses éditions fabriquées, mais ce n'est pas une garde par action ;
```

Motif : rapport v3, § 2 (m-4) et § 6, point 6.

### 6. Plafond des actions non éditables

Le risque. Si le saboteur écrit souvent « … A100 GPU-hours » (deux nombres pour le lecteur gelé) ou « 2k », la part non éditable dépasse 10 % dans chaque famille, toutes sont refusées deux fois, et rien n'est formé le 23. Aucune donnée ne dit cette fréquence.

Remède, sans lire aucune donnée : **deux paliers**. Une action non éditable sort des cibles de tous les membres et reste, non éditée, dans tous leurs contextes : la perte est la même pour les trois. Elle coûte de la force à la manipulation, que l'oracle du coût seul mesure, et non de la validité. Le seuil de 10 % était de moi, posé sans donnée ; rien n'oblige à refuser une famille à 12 %. Le palier de 25 % est aussi posé sans donnée : au-delà, plus d'une cible sur quatre manquerait, et je ne veux pas l'accepter sans un mot.

Ce remède ne touche pas le lecteur gelé du coût. **Il touche le code de formation** : une constante (0,25), un marqueur par famille, la part par motif, et leurs essais ; et le repli ci-dessous, que la session de formation applique à la main, par identifiant.

#### Couple C-6a — T — « Plan d'analyse », point 3, « Contrôles, par famille »

Avant :

```text
part d'actions non éditables ≤ 10 %. Sinon la famille n'est pas formée ; elle est retirée une fois avec des graines neuves (suffixe « r1 »).
```

Après :

```text
part d'actions non éditables ≤ 25 %. Sinon la famille n'est pas formée ; elle est retirée une fois avec des graines neuves (suffixe « r1 »). Au-dessus de 10 % et jusqu'à 25 %, la famille est formée et marquée « part non éditable haute » : l'audit de symétrie est déclenché pour elle. La part est rapportée par famille et par motif (plusieurs nombres, intervalle, suffixe « k », contrôle manqué). Une action non éditable sort des cibles de tous les membres : la perte est la même pour les trois, et se paie en force de la manipulation, que l'oracle du coût seul mesure. **Repli du jour de la formation**, règle mécanique : si quatre familles, retirage compris, sont refusées pour ce seul motif, la session de formation arrête toutes les instances par leur identifiant, après versement, et rend la main à la mère (nœud) ; elle ne change aucun seuil.
```

Motif : rapport v3, § 7, point 2. À regarder de près par le contre-lecteur : c'est un seuil desserré dans une section figée.

#### Couple C-6b — T — « Ce qui peut faire échouer le calendrier »

Avant :

```text
- Un contrôle de l'opérateur d'édition qui refuse trop de familles (trop d'actions à plusieurs nombres ou à intervalle).
```

Après :

```text
- Un contrôle de l'opérateur d'édition qui refuse trop de familles : « A100 » dans le champ du coût compte pour deux nombres, « 2k » sort par la règle du suffixe, et aucune donnée ne dit leur fréquence chez le saboteur. Les deux paliers du point 3 (10 % et 25 %) et le repli du jour de la formation y répondent ; au-delà de 25 % partout, rien n'est formé le 23, et c'est un nœud.
```

Motif : le même.

### 7. Le marché du 19 novembre

Ce que le calendrier et le devis en tirent. Trois offres pour sept instances : la formation part par vagues (règle de C-2b). Les heures de carte ne changent pas ; ni l'attendu, ni le pire cas, ni les coupures, ni le plafond. L'horloge passe de 9 à 10 heures à 23 à 26 heures en trois vagues strictes, 18 à 21 heures avec quatre cartes : la formation finit le mardi 24 et non le lundi 23, la marge du 25 reste, plus courte. Les prix vus (1,12 à 1,19 USD de l'heure) sont dans la fourchette du devis (1,09 à 1,30) : le bas de l'attendu n'est plus à espérer, le haut tient.

#### Couple C-7a — T — « Calendrier », ligne du lundi 23

Avant :

```text
| lun. 23 | **formation** : sept instances, 8,9 à 10,3 heures (quatre instances : 15,5 à 17,8 heures, fin le mardi matin) |
```

Après :

```text
| lun. 23 | **formation** : sept instances, lancées au fil des offres (règle sous le tableau) : 8,9 à 10,3 heures si sept offres passent les bornes ensemble ; 22,9 à 26,1 heures en trois vagues de trois cartes, fin le mardi 24 |
```

Motif : note sur le marché ; arithmétique dans `sortie-calcul-devis-formation-trois-membres-v1.txt`.

#### Couple C-7b — T — « Ce qui peut faire échouer le calendrier »

Avant :

```text
- Moins de quatre cartes disponibles au prix du devis.
```

Après :

```text
- Moins de quatre cartes disponibles au prix du devis : c'était le cas le 19 novembre à 20:02Z (trois offres acceptées sur onze cartes de 80 Go, à 1,12, 1,14 et 1,19 USD de l'heure ; instantané). La règle du lancement au fil des offres s'applique. Au-delà de trois vagues, des familles manquent au mardi 24 à 12:00Z et les coupes s'appliquent.
```

Motif : le même.

#### Couple C-7c — T — « Calcul et dépense »

Avant :

```text
8,9 à 10,3 heures d'horloge ; relecture sur une carte
```

Après :

```text
8,9 à 10,3 heures d'horloge si sept offres passent ensemble (22,9 à 26,1 heures en trois vagues de trois cartes) ; relecture sur une carte
```

Motif : le même.

#### Couple C-7d — DV — § 3, « Horloge »

Avant :

```text
Horloge : 8,9 à 10,3 heures si les sept cartes partent ensemble.
```

Après :

```text
Horloge : 8,9 à 10,3 heures si les sept cartes partent ensemble. Le 19 novembre à 20:02Z, trois offres seulement passaient toutes les bornes de la ligne « Carte » ci-dessous, à 1,12, 1,14 et 1,19 USD de l'heure (instantané du marché ; `code-formation/verification-champs-offre-loueur-v1.md`, `48a81bd4…`). En vagues (ordre du texte : 6, 1, 2 ; 3, 4, 5 ; 7), l'horloge passe à 22,9 à 26,1 heures avec trois cartes, 17,8 à 20,6 heures avec quatre. Les heures de carte ne changent pas : ni l'attendu, ni le pire cas, ni les coupures, ni le plafond de 200 USD. Aux prix vus ce soir-là (stockage ≈ 0,04 USD de l'heure), la formation coûterait 74,6 à 95,6 USD : dans la fourchette attendue, dont le bas n'est plus à espérer. Arithmétique : `calcul-devis-formation-trois-membres-v1.py`.
```

Motif : le même. L'instance de relecture demande un disque de 300 Go : la note sur le marché ne dit pas combien d'offres en ont un ; à relever avant le 26.

### 8. Autres points des §§ 5 à 7 du rapport v3

#### Couple C-8a — T — « Plan d'analyse », point 6

Avant :

```text
**les textes de distillation** de chaque famille (identifiants et textes d'origine, tables d'édition par membre) ;
```

Après :

```text
**le tirage brut** de chaque famille (`tirage.jsonl`, écrit et scellé dès qu'il existe, avant toute édition, gardé même si la famille est ensuite refusée) et **les textes de distillation** de chaque famille (identifiants et textes d'origine, tables d'édition par membre) ;
```

Motif : constat M-4 de la contre-lecture du code ; rapport v3, § 6, point 7.

#### Couple C-8b — T — « Données gardées », premier tiret

Avant :

```text
`donnees/barreau5-familles-jumelles-v1-formation` (adaptateurs, 27 Mo chacun ;
```

Après :

```text
`donnees/barreau5-familles-jumelles-v1-formation`, réunie au versement par la session de formation à partir d'une branche par instance (`…-formation-instance-<n>`, et `…-instance-<n>-x1` pour une relance), sept instances ne pouvant pousser ensemble sur une même branche (adaptateurs, 27 Mo chacun ; tirages bruts ;
```

Motif : rapport v2, choix 17 ; rapport v3, § 2 (M-5).

#### Couple C-8c — T — « Liste d'arrêt », point 5

Avant :

```text
(la garde d'équivalence de la génération, en mémoire, sur 5 % des actions, comme à la course de confirmation, n'en est pas une)
```

Après :

```text
(la garde d'équivalence de la génération de la course de confirmation n'est pas jouée ici : elle demanderait des crochets en mémoire, que cette garde refuse ; « mêmes réglages que la course de confirmation », au point 2, ne la couvre donc pas : écart déclaré)
```

Motif : rapport v1, choix 1. **À trancher par le contre-lecteur du texte** : mon couple M-5a du brouillon 2 la permettait ; le développeur ne la joue pas ; je l'accepte parce qu'une exception étroite à la garde du point 5 me paraît plus risquée que l'absence de cette garde.

#### Couple C-8d — T — « Code neuf », module de formation

Avant :

```text
épisodes d'évaluation, sorties ; plusieurs instances sous une même ligne d'accord.
```

Après :

```text
épisodes d'évaluation, sorties ; plusieurs instances sous une même ligne d'accord ; relance unique ; minuterie d'arrêt qui ne détruit une instance qu'après un versement prouvé ; liste blanche des sorties. La distillation appelle `distiller_transcriptions` de `t06/distillation_transcription.py`, la fonction gelée qu'appelle `distiller_adaptateur` en mode « transcription », avec les mêmes arguments, et non `distiller_adaptateur` lui-même : importer `t06/lanceur.py` chargerait les modules de sonde, que la garde du point 5 de la liste d'arrêt met hors d'usage.
```

Motif : rapport v1, écart déclaré à « Code neuf » ; rapport v3, § 2 (M-2, M-5, M-7).

#### Couple C-8e — T — « Code neuf », opérateur d'édition

Avant :

```text
- `edition_cout_v1` : grille, valeur, écriture, épissure des jetons, contrôles par action et par famille.
```

Après :

```text
- `edition_cout_v1` : grille, valeur, écriture, épissure des jetons, contrôles par action et par famille. Tokeniseur de la configuration scellée, chargé comme le charge la chaîne ; la version de `transformers` de l'instance est celle que fige le fichier d'exigences du dépôt au commit de `CODE-FORMATION-B5F` (le nettoyage des espaces au décodage en dépend) et s'écrit au manifeste.
```

Motif : rapport v3, § 4 et § 7, point 5. Au développeur de dire si une garde le vérifie déjà sur l'instance ; sinon c'est une ligne de code de plus avant le gel.

---

## Groupe 2 — seulement à 39 adaptateurs

Arithmétique : `sortie-calcul-devis-formation-trois-membres-v1.txt`. Une famille d'apprentissage à trois membres : 160 épisodes, trois distillations, 64, 32 et 32 épisodes d'évaluation, soit 3,91 à 4,60 heures. Coupure : quatre cinquièmes du pire cas, arrondis à l'entier supérieur, règle que suivent les trois coupures du brouillon 3 (vérifié par le programme). Le brouillon 4 rechiffrera le devis en entier (replis de la garde des activations, plans réduits, fiche) : seuls sont donnés ici les nombres que le code attend et les totaux.

#### Couple D-1a — T — « Plan d'analyse », point 2

Avant :

```text
familles d'apprentissage, deux (jumeau, saboteur). Trente-six adaptateurs, treize tirages.
```

Après :

```text
familles d'apprentissage, trois aussi (jumeau, saboteur, sur-saboteur). Trente-neuf adaptateurs, treize tirages.
```

Motif : fiche V-B1, voies (ii) et (iii).

#### Couple D-1b — T — « Plan d'analyse », point 6

Avant :

```text
les 36 adaptateurs ;
```

Après :

```text
les 39 adaptateurs ;
```

Motif : le même.

#### Couple D-1c — T — « Calendrier », coupe 4

Avant :

```text
deux familles d'apprentissage, 28 adaptateurs, dix tirages.
```

Après :

```text
deux familles d'apprentissage, 30 adaptateurs, dix tirages.
```

Motif : le même.

#### Couple D-1d — T — « Calendrier », ligne du lundi 23 (après C-7a)

Avant :

```text
8,9 à 10,3 heures si sept offres passent les bornes ensemble ; 22,9 à 26,1 heures en trois vagues de trois cartes, fin le mardi 24 |
```

Après :

```text
9,6 à 11,0 heures si sept offres passent les bornes ensemble ; 24,2 à 27,7 heures en trois vagues de trois cartes, fin le mardi 24 |
```

Motif : l'instance 6 devient la plus longue.

#### Couple D-1e — T — « Calcul et dépense » (après C-7c)

Avant :

```text
58 à 66 heures de carte, 8,9 à 10,3 heures d'horloge si sept offres passent ensemble (22,9 à 26,1 heures en trois vagues de trois cartes) ; relecture sur une carte, 4,0 à 5,3 heures ; attendu ≈ 86 à 128 USD, pire cas ≈ 246, plafond demandé 200.
```

Après :

```text
60 à 69 heures de carte, 9,6 à 11,0 heures d'horloge si sept offres passent ensemble (24,2 à 27,7 heures en trois vagues de trois cartes) ; relecture sur une carte, 4,1 à 5,4 heures ; attendu ≈ 88 à 132 USD, pire cas ≈ 255, plafond demandé 200.
```

Motif : + 1,8 à 2,5 heures de carte et + 2,0 à 3,4 USD à la formation ; relecture de trois adaptateurs de plus.

#### Couple D-1f — T — « Données gardées », deuxième tiret

Avant :

```text
séries nominales aux trois couches (≈ 127 Go), modèle nu (≈ 3,5 Go), textes propres des saboteurs d'apprentissage (≈ 11 Go) : ≈ 141 Go
```

Après :

```text
séries nominales aux trois couches (≈ 138 Go), modèle nu (≈ 3,5 Go), textes propres des saboteurs d'apprentissage (≈ 11 Go) : ≈ 152 Go
```

Motif : trois adaptateurs de plus à relire.

#### Couple D-2a — DV — § 2, première phrase

Avant :

```text
trois familles d'apprentissage à deux membres, soit 36 adaptateurs et 13 tirages de 160 épisodes
```

Après :

```text
trois familles d'apprentissage à trois membres aussi, soit 39 adaptateurs et 13 tirages de 160 épisodes
```

Motif : fiche V-B1.

#### Couple D-2b — DV — § 2, tableau

Avant :

```text
| une famille d'apprentissage | 160 épisodes (1,79) ; deux distillations (0,46 à 0,92) ; 64 et 32 épisodes (1,07) | 3,32 à 3,78 |
```

Après :

```text
| une famille d'apprentissage | 160 épisodes (1,79) ; trois distillations (0,69 à 1,38) ; 64, 32 et 32 épisodes (1,43) | 3,91 à 4,60 |
```

Motif : le même.

#### Couple D-2c — DV — § 3, instance 6

Avant :

```text
| une instance à deux familles d'apprentissage | 8,44 à 9,36 | 10,5 à 14,9 | 29,7 | **24** |
```

Après :

```text
| une instance à deux familles d'apprentissage | 9,61 à 10,99 | 11,8 à 17,2 | 34,5 | **28** |
```

Motif : **nombres attendus par le code** pour l'instance 6 : coupure 28 USD, heures 9,61 à 10,99. Au prix plafond de 1,30 USD de l'heure, la coupure laisse 10,3 heures de plus que l'attendu haut : la garde du code passe.

#### Couple D-2d — DV — § 3, instance 7

Avant :

```text
| une instance à une famille d'apprentissage | 5,12 à 5,58 | 6,8 à 9,7 | 18,5 | **15** |
```

Après :

```text
| une instance à une famille d'apprentissage | 5,71 à 6,40 | 7,4 à 10,8 | 20,9 | **17** |
```

Motif : **nombres attendus par le code** pour l'instance 7 : coupure 17 USD, heures 5,71 à 6,40.

#### Couple D-2e — DV — § 3, total de la formation

Avant :

```text
| **formation, total** | **58,0 à 66,3** | **72,2 à 105,5 ; centre 88,9** | **210,3** | **169** |
```

Après :

```text
| **formation, total** | **59,8 à 68,8** | **74,2 à 108,9 ; centre 91,6** | **217,6** | **175** |
```

Motif : somme des sept instances.

#### Couple D-2f — DV — § 3, second tableau, formation et relecture

Avant :

```text
| formation | 58,0 à 66,3 | 72,2 à 105,5 | 210,3 | 169 |
| relecture et notation, activations gardées en entier (brouillon 3) | 3,99 à 5,25 | 9,2 à 16,3 (dont 3,7 à 7,1 de sortie de données) | 24,6 | 20 |
```

Après :

```text
| formation | 59,8 à 68,8 | 74,2 à 108,9 | 217,6 | 175 |
| relecture et notation, 39 adaptateurs, activations gardées en entier | 4,09 à 5,42 | 9,6 à 17,1 (dont 3,9 à 7,6 de sortie de données) | 25,6 | 21 |
```

Motif : relecture de 39 adaptateurs, 152 Go sortis.

#### Couple D-2g — DV — § 3, second tableau, ensemble

Avant :

```text
| **ensemble, chez le loueur de cartes** | **64,8 à 74,8** | **85,6 à 128,3 ; centre ≈ 107** | **246,4** | **197 ; plafond demandé : 200** |
```

Après :

```text
| **ensemble, chez le loueur de cartes** | **66,7 à 77,4** | **88,0 à 132,4 ; centre ≈ 110** | **254,7** | **204 ; plafond demandé : 200 (le compteur commun prime : la répétition générale, première sacrifiée, ne part que si le cumul relevé lui laisse sa coupure)** |
```

Motif : la somme des coupures dépasse le plafond de 4 USD. **Mot de Lazar** (groupe 3, point 2) : garder 200, ou 205.

#### Couple D-2h — DV — § 3, « Horloge » (après C-7d)

Avant :

```text
Horloge : 8,9 à 10,3 heures si les sept cartes partent ensemble. Le 19 novembre
```

Après :

```text
Horloge : 9,6 à 11,0 heures si les sept cartes partent ensemble (l'instance 6 devient la plus longue ; en vagues : 24,2 à 27,7 heures avec trois cartes, 18,5 à 21,3 avec quatre, et non les durées ci-dessous, qui valent à 36 adaptateurs ; aux prix vus, 76,7 à 98,7 USD). Le 19 novembre
```

Motif : le même calcul.

#### Couple D-2i — DV — § 4, ligne d'engagement

Avant :

```text
coupure [26 | 24 | 15 | 20 | 8] USD
```

Après :

```text
coupure [26 | 28 | 17 | 21 | 8] USD
```

Motif : coupures neuves des instances 6 et 7 et de la relecture.

---

## Ce qui menace encore le scellement le 21 et le gel le 22

1. **Le mot de Lazar sur 36 ou 39**, puis la ligne de table du code pour les instances 6 et 7 (nombres ci-dessus) et sa vérification.
2. **Le brouillon 4 et sa vérification du premier coup** : si la voie (iii) est retenue, l'hypothèse et les épreuves sont à récrire le 20, et aucun jour de marge ne reste avant le 21.
3. **Trois retouches du code que ces couples demandent avant le gel** : les deux paliers de la part non éditable (C-6a : constante, marqueur, part par motif) ; la règle « seule la copie `-x1` est lue » (C-2b), si le code de l'engagement ne la porte pas déjà ; la version de `transformers` au manifeste (C-8e). Au développeur de dire ce qui existe déjà.
4. **La vérification en cours des corrections du code**, et la remesure du plancher d'essais au commit de la course.
5. **Le marché** : trois offres pour sept instances. La formation tient en vagues jusqu'au 24 ; sous trois offres le 23, des familles manquent ou il faut un mot de Lazar sur les bornes.
6. **La part d'actions non éditables**, inconnue : les deux paliers réduisent le risque, ils ne l'ôtent pas.
7. **Le nom du texte scellé** : le code refuse un nom qui contient « brouillon » ; le texte du 21 doit porter son nom définitif, et la ligne `SCELLEMENT-B5F` le citer.

## Ce que je déclare

- Le programme de calcul a été écrit par une commande d'écriture du terminal, avant que je relise la règle du mandat qui demande les outils d'écriture et d'édition ; ce fichier-ci et le programme de contrôle sont écrits par l'outil d'écriture.
- Les seuils de 25 %, de quatre familles refusées, et les échéances du 24 et du 25 à 12:00Z sont posés par moi sans donnée : à attaquer par le contre-lecteur.
- Je n'ai pas lu le code au-delà des lignes dites en tête : là où un couple suppose un comportement du code (C-1a, C-2b, C-6a, C-8e), le développeur doit le confirmer.
