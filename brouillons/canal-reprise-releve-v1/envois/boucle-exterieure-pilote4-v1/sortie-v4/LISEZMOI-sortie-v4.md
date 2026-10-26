# LISEZMOI de la sortie — registre v4, protocole v3, briefs v3, spécification du relevé (B) v2 — v4

Fichier ouvert le 2026-10-26 à 05:54:26 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne), après la vérification des
empreintes et la lecture complète du brief v4 et des pièces fournies, et avant l'écriture des autres fichiers de `sortie/`.

Auteur : l'auteur de la v3 (sous-agent de la lignée conv-audit), relancé par conv-audit sur le brief v4
(`LISEZMOI-brief-v4.md`, `dc5b823b1a83227c5efb6864b67cedc176357aaf7c5cd6a4cc2db20be4b065f5`, vérifiée avant lecture :
égale). Je n'ai écrit ni la vérification de la v3, ni la pièce des points pour Lazar, ni l'extrait des lanceurs, ni le
texte v5. Je n'ai lu aucun score. Rien de ce dossier n'est servi à un organisme. Aucun `git`, aucun sous-agent, aucun
réseau, aucune clé ; écrit seulement dans `sortie/`. Écriture de ce fichier achevée le 2026-10-26 à 06:16:46 UTC (heure lue sur
`date -u` dans la commande qui écrit cette ligne).

Abréviations de ce fichier : R = `registre-hypotheses-conception-pilote4-v4.md` ; P = `protocole-boucle-exterieure-pilote4-v3.md` ;
B = `brief-agents-fin-de-course-v3.md` ; S = `specification-releve-mecanique-B-v2.md` ; « l. » = numéros de lignes de ces
fichiers tels que rendus.

## 1. Ce que j'ai fait

- **Vérifié** l'empreinte du brief v4 (égale ; son compagnon aussi), puis les onze pièces de `fournis/` contre
  `../EMPREINTES-fournis-v1.txt` (onze sur onze) et les huit compagnons présents (huit sur huit). Mes pièces v3 fournies
  sont égales à celles que j'avais rendues.
- **Lu en entier** : le brief v4 ; le rapport de vérification de la v3 (`1a7873e2…`) ; la pièce des points pour Lazar
  (`ac105262…`) ; l'extrait des lignes que les lanceurs v10 et v11 écrivent au `LANCEMENT.md` (`e3ec880c…`) ; le texte v5
  du pilote à ses graines (`1943f39a…`, qui prime) ; le LISEZMOI du script de lecture v2 (`2f328fee…`) ; mes pièces v3
  (copiées dans `sortie/` sous leurs noms v4, puis lues avec leurs numéros de lignes avant d'être modifiées).
- **Reçu pendant l'écriture**, trois messages de conv-audit, appliqués : (1) et (2) deux précisions à D5 (champ
  `identite.porte_m_precedente` ; refus d'écrire un relevé à identité incomplète) ; (3) une correction de D4 (les seuils
  du critère de fin ne sont pas les seuils 0,01 et 0,03 ; pour eux, la carte des facteurs tranche ; la phrase « les deux
  seuils comptent pour un seul facteur (ton choix 23, confirmé) » est retirée de D4 ; la carte et les zones interdites
  sont écrites par un autre sous-agent).
- **Exécuté** : `sha256sum`, `sha256sum -c` (dont un essai sur une liste passée par substitution de processus, sans
  fichier écrit : une ligne qui commence par `#` est ignorée, mode strict compris, GNU coreutils 9.4) ; `ls`, `wc`,
  `cat` du compagnon du brief ; `cp` et `chmod u+w` (copies de mes pièces v3) ; `grep` et `diff` sur mes pièces ; `sed`
  pour l'heure de fin ; `date -u`. **Python : non lancé.**
- **Écrit**, dans `sortie/` seulement : R, P, B, S, ce LISEZMOI, et le compagnon `.sha256` de chacun.

## 2. Table « v3 → v4 », par constat

| constat | décision | où c'est traité | ce qui reste |
|---|---|---|---|
| CLB3-01 (a) noms des fichiers du script | D1 | R § 0.1 l. 66–81 ; R § 0.2 l. 142–148 ; R § 2 l. 630–632 ; P § 3 l. 114–148 ; P § 13 l. 486–495 ; B partie commune l. 63–67 ; B section 4 l. 335–341 | que le script v3 écrive les noms que D1 décrit |
| CLB3-01 (b) contenu : « provisoire », valeurs de l'autre course | D1 | R § 0.1 l. 73–81 ; P § 3 l. 129–131 et 141–148 ; P § 11, G12 l. 398 ; P § 13 l. 486–495 ; B l. 63–67 et 338–346 | écrire, relire et essayer le script v3 ; écrire et essayer G12 |
| CLB3-01 (c) G8 bis | D1 | P § 11, G8 bis l. 394, et l. 400–403 ; P § 3 l. 129–131 ; B section 1 l. 150–153 | G8 bis (a) : l'essai « séparation » du script v3 ; G8 bis (b) : le contrôle de conv-audit à l'assemblage |
| CLB3-01 (d) le script v1 décrit comme sortie réelle | D1 | R § 0.1 l. 66–72 ; P § 3 l. 117–119 ; P § 13 l. 486–495 | rien |
| CLB3-02 verdicts de M et de S mis en regard | D2 | R § 0.2 l. 152–153 et 166–167 ; R § 0.4 l. 207–208 ; R § 0.7 l. 263–273 ; R § 0.9 l. 293–297 ; R § 1 l. 312 ; R HC-P4-01, 03, 05 (branche « verdicts différents » retirée ; HC-P4-01 l. 344–345) ; R § 2 l. 636–644 ; R § 3 l. 661–663 ; P § 0 l. 34–37 ; P § 2 l. 95 et 97 ; P § 4 l. 150–203 ; P § 5 l. 221–245 ; P § 7 l. 287–288 ; P § 11, G6 l. 391 ; P § 12.5 l. 476–479 ; P § 13 l. 505–509 ; B l. 13–14, 25–31, 50–52, 94–96, 176–258, 275–324 | Lazar peut reprendre la règle (pièce des points, point 5) |
| CLB3-03 HC-P4-01 : voie écrite après la lecture de faits de M | D3 | R « Écrit avant tout score » l. 19–30 ; R HC-P4-01 l. 322–341 ; R § 2, point 7 l. 645–648 ; S § 4.5 l. 203–207 ; S § 9 l. 334–335 ; B section 1 l. 146–149 ; P § 5 l. 217 et B l. 245 (exemple d'attente chiffrée sur `conception.declaration.ronde`) | rien |
| CLB3-04 points pour Lazar | D4, corrigée | P But l. 17–20 ; P § 1 l. 77–86 ; P § 6 l. 249–259 ; P § 7 l. 291–292 ; P § 8 l. 311–316 ; P § 10 l. 359–364 et 369–371 ; P § 12.3 l. 453–457 ; P § 16 l. 552–571 ; R § 0.5 l. 227–229 ; R HC-P4-04 l. 423–427 ; R HC-P4-01 l. 347–349 ; B l. 33–34 et 262 | les réponses de Lazar ; les défauts (a) des points 1 et 4 à leur échéance |
| CLB3-05 (a) aucun cas sain pour S ; (b) aucune règle pour un champ d'identité « absent » | D5 et ses deux précisions | S § 1 l. 21–22 ; S § 2 l. 47–64 ; S § 4.1 l. 106 ; S § 4.2 l. 116–166 ; S § 6 l. 255–268 et 287–292 ; S § 8 l. 321–326 ; P § 9 l. 321–352 ; P § 1 l. 56–58 ; R § 0.1 l. 82–88 ; R § 0.7 l. 252–260 ; R § 2 l. 619–624 ; B section 1 l. 132–139 | la source de `releve.course` et de `identite.lignee` (aucune ligne « - … » des lanceurs ne les porte) ; la valeur attendue du commit du segment 1 (la tête du message de départ de chaque course) |
| CLB3-06 (a) libellés que le script v2 n'écrit pas | D1 | R § 0.1 l. 106–116 ; R § 0.2 l. 177–179 ; R § 0.4 l. 201–203 ; R HC-P4-08 l. 513–518 ; R HC-P4-11 l. 577–584 ; B section 4 l. 347–351 ; P § 16 l. 569 | que le script v3 les écrive |
| CLB3-06 (b) faits mécaniques dans le fichier `test` | D1 | R § 0.1 l. 102–103 ; B section 1 l. 146–147 ; B section 3B l. 292–293 | rien |
| CLB3-06 (c) libellé de (ii) en délégation sur `test` | D1 | R § 0.1 l. 99–100 ; R § 0.2 l. 127–128 et 133–134 ; R § 2 l. 628–629 ; B section 1 l. 150–151 | rien |
| CLB3-06 (d) phrase (iv) du script : « deux objets » | aucune | R § 0.2 l. 154–156 (sans effet sur les verdicts ; aucun agent ne la recopie) | l'aligner dans le script v3 (point pour conv-audit, § 5) |
| CLB3-07 (a) « qu'il a lu ces scores » | D6 | P § 2 l. 92 | rien |
| CLB3-07 (b) ligne d'état du script | D1 | P § 2 l. 92 ; P § 16 l. 569 | que le script v3 écrive « signalements de test : N » |
| CLB3-08 (a) renvoi au « § 2, point 8 » | D7 | R § 0.4 : le renvoi disparaît avec la branche « verdicts différents » (D2) ; le § 2 renvoie à son point 6 (R l. 636–638) | rien |
| CLB3-08 (b) HC-P4-05 et 06 comptées parmi les fiches qui motivent | D7 | R § 0.6 l. 238–241 ; B section 2 l. 190–193 ; B section 3B l. 301 | rien |
| CLB3-08 (c) noms de la lecture finale aux étapes 1 et 2 | D7 | B partie commune l. 66–67 et 70 ; B section 4 l. 331–333 | rien |
| CLB3-08 (d) commande exacte du diff, préfixe de G5 | D7 | B section 2 l. 216–241 ; P § 6 l. 266–270 ; P § 11, G5 (f) l. 390 ; B section 3B l. 302–303 | rien |

## 3. Table « v3 → v4 », par décision

| décision | constats | où c'est traité | ce qui reste |
|---|---|---|---|
| D1 — lecture de `test_final`, script de lecture v3 | CLB3-01, CLB3-06 (a, b, c), CLB3-07 (b) | voir le § 2 ; plus R « Ce qui change » l. 11–17 et P § 2 l. 92–93 | le script v3 (son auteur, relu avant usage) ; G8 bis et G12 à essayer |
| D2 — règle de préséance (remplace mes choix 1, 3 et 4 de la v3) | CLB3-02 | voir le § 2 ; le point « correction après M sans attendre S » est sorti des points pour Lazar (P § 4 l. 150–203 ; P § 16 l. 563) | rien |
| D3 — HC-P4-01 | CLB3-03 | voir le § 2 ; origine des faits lus déclarée à R l. 22–23 | rien |
| D4 — points pour Lazar, **corrigée par conv-audit** | CLB3-04 | voir le § 2. Appliquée telle que corrigée : la phrase « les deux seuils comptent pour un seul facteur (ton choix 23, confirmé) » n'est pas appliquée ; pour les seuils 0,78 et 0,65 du critère de fin, la carte des facteurs tranche (R l. 347–349 ; P § 6 l. 253–255 ; P § 16 l. 566) ; les seuils 0,01 et 0,03 restent sous le point 7 (défaut : garder ; une ronde s'ils changent : P § 6 l. 257–259 ; R l. 227–229 et 423–427) ; la carte et les zones interdites sont écrites par un autre sous-agent (P § 2 l. 93 ; P § 6 l. 249–250 ; P § 16 l. 567) | les réponses de Lazar |
| D5 — relevé (B), et ses deux précisions | CLB3-05 | voir le § 2 ; précision 1 (`identite.porte_m_precedente`, « oui » ou « absent ») : S l. 131 et 155–157, P § 9 l. 336 ; précision 2 (refus d'écrire) : S l. 134–139, S § 6 artefacts 11 à 13 l. 287–290, R l. 85–88 et 619–624, P § 1 l. 56–58 et § 9 l. 340–346, B l. 132–139 | sources de `releve.course` et `identite.lignee` ; vérifier que les séries v13 et v14 portent les empreintes réelles des questions (S § 8 l. 321–326) |
| D6 | CLB3-07 (a) | P § 2 l. 92 | rien |
| D7 — (a) à (d) | CLB3-08 | voir le § 2 | rien |

## 4. Autres changements, déclarés avec leur raison

1. Renvois au brouillon du texte v5 remplacés par le texte v5 à ses graines, qui prime (R, P), sauf là où il faut nommer
   le brouillon (l'origine des faits lus, D3). Les passages cités s'y retrouvent (texte v5, table, l. 55–65 ; § Plan).
2. R § 6 ajouté (table « v3 → v4 » résumée, pour les agents qui ne lisent pas ce LISEZMOI) ; R § 4 titré « historique ».
3. R HC-P4-11 (l. 581–583) et B section 4 (l. 347–348) : le sens n'est cité que pour un rejet, même si le script en écrit
   un pour un non-rejet ; raison : D1 fonde le sens sur le verdict d'un test bilatéral, qui ne porte un sens que s'il
   rejette.
4. R § 0.7 (l. 270–272) : « aucune fiche de M ne motive de correction » défini sur la pièce de verdicts de M (branches
   qui proposent une correction, hors désaccords ; une demande d'instrumentation n'en est pas une) ; raison : D2 demande
   de l'écrire comme un fait sur M seule.
5. P § 4 et B section 2 : le correcteur écrit toujours d'abord le fait sur sa course ; le correcteur de S est un
   sous-agent neuf, lancé seulement après que la partie B de M a vérifié ce fait ; il reçoit la référence de la pièce de M
   sans la lire. P § 4 et B section 3B : une partie B par course. Raison : D2 (aucune pièce ne met côte à côte les verdicts
   des deux courses ; la partie B de la v3 lisait les deux).
6. Noms des pièces de correction et de partie B par course (`correction-<dossier>-ronde-<k>-v1.md`,
   `perimetre-<dossier>-…`, `contre-lecture-<dossier>-ronde-<k>-v1.md`) ; champs des briefs `<pièce-verdicts>`,
   `<pièce-partie-A>`, `<désaccords>`, `<condition-préséance>` ; G6 réécrite (ligne « condition de préséance »). Raison :
   D2.
7. P § 5 : une entrée de journal par course et par correction ; exemple d'attente chiffrée sur
   `conception.declaration.ronde` (P l. 217 ; B l. 245) au lieu de `conception.rondes_tournees`. Raison : D2 et D3.
8. P § 1, condition 8 (l. 77–80) : la poussée des v2 et v3 des pièces, d'après le brief v4, § 4, point 1, sans recopier
   l'heure de fin de M.
9. P § 3 (l. 122–127) : la version du script est écrite au manifeste par une ligne de commentaire, essayée (§ 1 de ce
   fichier) ; G12 refuse aussi une version inférieure à 3 ou différente de celle du manifeste. Raison : D1 (« `<n>` ≥ 3,
   écrite au manifeste »).
10. P § 9 (l. 321–352) : tableau transposé (une ligne par champ, une colonne par course) ; le commit de l'organisme y est
    « pour mémoire » (le relevé ne le porte pas : aucune ligne « - … » des lanceurs ne l'écrit) ; le commit du segment 1 est
    comparé par conv-audit au message de départ avant l'assemblage. Raison : D5.
11. P § 11 (l. 379–380) et § 16 : auteur des gardes, exécution du relevé, forme d'un texte de relance, d'après le brief
    v4, § 4, points 3, 7 et 10 ; P § 12.1 (l. 415–422) : la forge aux noms du script v3 et aux champs d'identité exigés.
12. S § 4.2 : `identite.graine` ajouté (D5 exige « graine » ; la ligne « préenregistrement » la porte ; `graine_manifeste`
    gardée, facultative) ; lignes d'identité répétées d'un segment à l'autre avec deux valeurs : refus ; lignes du
    `LANCEMENT.md` lues par leur motif exact, la liste noire du § 5 visant les noms de champs JSON. Raison : appliquer D5
    sans ambiguïté.
13. S § 2 (l. 59–61) : `unite.g001.question_servie = oui` déduit de la ligne « - réponse à la question :
    reponse-question-g001.md … » ; jamais d'un champ de l'extrait dont le nom contient « question » (liste noire). Raison :
    le cas sain de la série v14 que D5 demande.
14. S : renvois internes « protocole v2 » et « registre v3 » gardés (ils valent pour P et R aux mêmes numéros de section),
    et § 7 gardé tel quel (son « point à fixer » est tranché par le brief v4, § 4, point 3, et porté à P § 16) ; raison :
    la consigne de conv-audit de ne rien changer d'autre dans la spécification.
15. B section 1, étape 7 (l. 157–158) : la clause « libellé que le script n'écrit pas encore » retirée ; raison : un
    script de version inférieure à 3 n'est jamais lu (partie commune, étape 1).

## 5. Ce qui reste, pour conv-audit (une ligne chacun)

1. Écrire, faire relire et essayer le script de lecture v3 (noms et contenus de D1 ; essai « séparation » ; libellés ;
   ligne d'état « signalements de test : N ») ; y aligner la phrase (iv) sur « deux courses » (CLB3-06 d).
2. Relevé (B) : trouver la source de `releve.course` et de `identite.lignee`, que n'écrit aucune ligne « - … » des
   lanceurs ; si aucune source hors de l'archive ne les porte, le relevé ne s'écrira jamais : trancher avant la première
   lecture.
3. Relevé (B) : vérifier que les cas sains des séries v13 et v14 portent les empreintes réelles des questions M et S.
4. Recopier, pour chaque course, la tête citée à son message de départ (valeur attendue du commit du segment 1), et la
   comparer au relevé avant l'assemblage.
5. Écrire et essayer les gardes G1 à G12 (G12 est nouvelle), les dossiers d'audit, le script de forge et l'étalonnage à
   blanc.
6. Pour une relance : la version du script de lecture qui accepte son nom (le script v2 refuse tout nom hors des deux
   courses du pilote 4), fixée avec le texte de la relance.
7. Faire vérifier cette v4 par le vérificateur de la v3, avec les tables des § 2 et § 3 ; pousser les cinq fichiers et
   leurs compagnons.

## 6. Points pour Lazar

Aucun point nouveau. Les points sont posés par conv-audit dans `points-boucle-exterieure-pilote4-pour-lazar-v1.md`
(`ac105262…`) ; P § 16 (l. 552–571) en donne l'état, le défaut et le moment.

## 7. Écarts déclarés

1. **Faits de course lus dans les pièces fournies, sans les chercher** : le coût total de la course M (texte v5, table,
   ligne « devis », R-494 ; pièce des points, point 3), l'heure de sa fin (brief v4, § 4, point 1), le nom du dossier
   réel de la course S (brief v4, D5). Aucun score. Aucune fiche n'a été changée à cause d'eux ; seul le nom du dossier de
   S est recopié, au tableau d'identité, comme D5 le demande. Déclaré aussi au registre (R l. 19–30).
2. Lu deux fichiers hors de `fournis/`, que le brief v4 désigne : `../EMPREINTES-fournis-v1.txt` et le compagnon du brief
   (`../LISEZMOI-brief-v4.md.sha256`). Rien d'autre hors de `fournis/` ; je n'ai pas relu mon dossier v3.
3. Essai de `sha256sum -c` sur une liste passée par substitution de processus, pour vérifier qu'une ligne de commentaire
   est ignorée ; aucun fichier écrit.
4. Mes pièces v3 ont été copiées depuis `fournis/` dans `sortie/` sous leurs noms v4, rendues inscriptibles (`chmod u+w`),
   puis modifiées : rien n'a été écrit hors de `sortie/`.
5. Les heures de fin des cinq fichiers sont écrites par `sed`, dans la commande même qui lit `date -u`, à la place d'un
   marqueur ; les compagnons sont calculés après. Les empreintes des quatre pièces sont recopiées ici après leur calcul.
6. L'heure du début de ma lecture n'est pas consignée ; la seule heure de début écrite est celle de l'ouverture de ce
   fichier (05:54:26 UTC).
7. Aucune poussée : sans `git`, elle revient à conv-audit.

## 8. Empreintes (format « empreinte, deux espaces, nom nu »)

```
e36707b010416e8f1c9fcae18ca4ffdc0cd99a88b6c737ce5453a8d7dbbbd08e  registre-hypotheses-conception-pilote4-v4.md
acfd6426cfde1a81d23a40297b76fbc62101260b5b08a5807d19d528dbd4d14b  protocole-boucle-exterieure-pilote4-v3.md
7f6217e830ae3875189571831c9d377b7713baec0682a0c173cb1b703b9978a4  brief-agents-fin-de-course-v3.md
701b527091c26aa657ef6b736dc340c3e6297cddd98acb1f35e0136176cfd043  specification-releve-mecanique-B-v2.md
```

L'empreinte de ce fichier est dans son compagnon, `LISEZMOI-sortie-v4.md.sha256`.
