# LISEZMOI de la sortie — registre v5, protocole v4, briefs v4, spécification du relevé (B) v3 — v5

Fichier ouvert le 2026-10-26 à 06:58:27 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne), après la vérification des
empreintes et la lecture du brief v5, de la vérification de la v4 et des pièces fournies, et avant toute modification des
autres fichiers de `sortie/`.

Auteur : l'auteur des v3 et v4 (sous-agent de la lignée conv-audit), relancé par conv-audit sur le brief v5
(`LISEZMOI-brief-v5.md`, `6026f9881101c3fa1c9142e61ecd77695f2a18b515fda2fa72879914065435a4`, vérifiée avant lecture :
égale). Je n'ai écrit ni la vérification de la v4, ni la carte des facteurs, ni les zones interdites, ni le brief du
script de lecture v3. Je n'ai lu aucun score, ni aucun fait de course de plus. Rien de ce dossier n'est servi à un
organisme. Aucun `git`, aucun sous-agent, aucun réseau, aucune clé ; écrit seulement dans `sortie/`. Écriture de ce
fichier achevée le 2026-10-26 à 07:09:25 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).

Abréviations : R = `registre-hypotheses-conception-pilote4-v5.md` ; P = `protocole-boucle-exterieure-pilote4-v4.md` ;
B = `brief-agents-fin-de-course-v4.md` ; S = `specification-releve-mecanique-B-v3.md` ; « l. » = numéros de lignes de
ces fichiers tels que rendus (l'écriture de l'heure de fin ne change aucun numéro).

## 1. Ce que j'ai fait

- **Vérifié** l'empreinte du brief v5 (égale), puis `cd fournis && sha256sum -c ../EMPREINTES-fournis-v1.txt` : douze
  sur douze ; les compagnons présents sont justes. Mes pièces v4 fournies sont égales à celles que j'avais rendues.
- **Lu en entier** : le brief v5 ; la vérification de la v4 (`b518f24c…`) ; le LISEZMOI de la carte (`cbe00172…`) ; le
  brief du script de lecture v3 (`78861f99…`), pour les mots et les fichiers du script (E2, E3, E7 c). **De la carte**
  (`carte-facteurs-v1.md`, `47fa6100…`), ce que demande E8 : l'en-tête, le § 0, F03, les § 4 à 7 et les lignes qui nomment
  F03, Z03 et `VERSION`. Non ouverts : `carte-facteurs-v1.json`, `zones-interdites-v1.md` et `.json` (cités par nom et
  empreinte). Du LISEZMOI v4 : sa forme (titres, début et fin). Mes pièces v4 : copiées dans `sortie/` sous leurs noms
  v5, puis lues (spécification, protocole et briefs en entier ; registre dans ses passages modifiés et leurs voisins).
- **Exécuté** : `sha256sum`, `sha256sum -c`, `ls`, `wc`, `cat`, `cp`, `chmod u+w`, `grep`, `sed`, `awk`, `diff`, `od -c`
  (une modification refusée : un mot différait), `printf` et `date -u` ; Python une fois, avec `-I`, pour compter trois
  chaînes dans B, sans écrire de fichier.
- **Écrit**, dans `sortie/` seulement : R, P, B, S, ce LISEZMOI, et le compagnon `.sha256` de chacun.

## 2. Table « v4 → v5 », par constat

| constat | décision | où c'est traité | ce qui reste |
|---|---|---|---|
| CLB4-01 — nom et lignée au relevé, sans source | E1 | S l. 54–55 (ligne de la course), 141–142 (champs), 149–154 (refus), 156–162 (table close), 181–190 (sources), 291–293 et 298–299 (cas sains), 328–337 (artefacts 15 à 18), 368–375 (§ 8 : confirmation en simulation) ; P l. 58–61, 353–361, 372–378, 434 (G11) ; R l. 91–95, 639–642 | le script du relevé, sa table de correspondance et leurs essais ; la confirmation sur les séries v13 et v14 (§ 5, points 2 et 3) |
| CLB4-02 — libellé (iii) | E2 | R l. 114–120 (§ 0.1), 151–152 (§ 0.2), 590–603 (HC-P4-11 ; la l. 581 de la v4 est réécrite aux l. 595–599) ; B l. 365–371 ; P l. 527–536, 541–544, 621 | le script v3 doit écrire ces mots (§ 5, point 1) |
| CLB4-03 — « holm-quatre » et ligne d'état | E3 | P l. 95, 150–152, 532–534, 621 ; R l. 81–83 ; B l. 361–364 (étape 1) | — |
| CLB4-04 — fin du compteur | E4 | B l. 14–16, 266–284 (section 3A) ; P l. 102, 152–154, 208–212, 234–238, 331, 541–544, 549–551 | — |
| CLB4-05 — faits de M au registre | E5 | R l. 20–22 | — |
| CLB4-06 — `question_servie` et artefact 4 | E6 | S l. 64–69, 77–80, 195–196, 221, 309–313, 338–339 (artefact 19) | doute du § 5, point 3 |
| CLB4-07 (a) — « trois messages » | E7 a | R l. 3–10 ; P l. 3–13 ; B l. 3–10 ; S l. 3–16 ; § 6 ci-dessous (le LISEZMOI v4, l. 26, n'est pas réécrit : R12) | — |
| CLB4-07 (b) — famille à trois valeurs | E7 b | P l. 252 (journal), 490–500 (§ 12.3) | l'application de (c) est un choix déclaré (§ 4, point 6) |
| CLB4-07 (c) — phrase (iv) | E7 c | R l. 161–169 | — |
| CLB4-07 (d) — G6 en mots entiers | E7 d | P l. 428 | — |

## 3. Table « v4 → v5 », par décision

| décision | appliquée telle quelle | où | ce qui reste |
|---|---|---|---|
| E1 | oui : nom lu sur la ligne « - course : … ; dossier du pilote : … », dernier élément du chemin sans `-tentative<N>`, égal à la table close de deux lignes (`v6-2`, `v6-2-s`) citée des textes du pilote ; clé égale sur les trois lignes ; lignée de l'extrait égale à la table, sinon prise dans la table et dite « déduite de la clé : contrôle non indépendant » ; confirmation au § 8 | S l. 54–55, 141–142, 149–162, 181–190, 368–375 ; P l. 353–361, 372–378 | voir CLB4-01 |
| E2 | oui : les mots du point 4 bis, la correction dans un champ à part, le sens « sans objet (non rejeté) » pour un non-rejet ; correspondance libellé → verdict ; arrêt sur tout autre libellé ; l. 581 réécrite | R l. 114–120, 151–152, 590–603 ; B l. 365–371 ; P l. 527–536 | alignement du script (§ 5, point 1) |
| E3 | oui : « signalements (fichier test) : N » ; ni compte, ni proportion, ni borne, ni valeur p, ni libellé, ni signalement de l'autre course ; jamais de valeur p ajustée, de rang ni de seuil appliqué ; étape 1 de l'analyste final | P l. 95, 150–152, 532–534 ; R l. 81–83 ; B l. 361–364 | — |
| E4 | oui : section 3A pour la lecture finale ; une entrée finale par course, puis une entrée de clôture sans verdict ; une transmission par course | B l. 266–284 ; P l. 208–212, 234–238, 549–551 | — |
| E5 | oui, la phrase mot pour mot | R l. 20–22 | — |
| E6 | oui : `oui` seulement sans « aucune pièce archivée », sinon `absent`, jamais `non` ; ligne reconnue par son début ; aucune chaîne du nom du fichier dans le script | S l. 64–69, 195–196, 221, 309–313 | — |
| E7 | oui : (a) « deux messages » ; (b) trois valeurs ; (c) phrase citée ; (d) mots entiers | voir CLB4-07 | — |
| E8 | oui : G5 par colonnes et segments, repli par lignes non pris ; gel de Z03 confirmé (seuil du routage de la règle de classe) ; `VERSION` (`principal.py` l. 27) dans la liste d'accompagnement ; carte et zones citées par nom et empreinte, « v1, sous réserve de leur contre-lecture » ; 0,01, 0,03 et leurs copies (F05, F06, F13, F14) gelés par le point 7 | P l. 271–285 (§ 6), 298–299, 303–307, 427 (G5), 567–568 et 573–577 (§ 14), 617–619 (§ 16) ; B l. 203–205, 234–237, 319–321 | la contre-lecture de la carte et des zones (§ 5, point 4) ; la règle des lignes insérées (§ 5, point 5) |

## 4. Autres changements, déclarés avec leur raison

1. **Statuts** des quatre pièces réécrits pour cette version (auteur, brief v5, vérification de la v4, E1 à E8, heure de
   fin) ; au registre, « Ce qui change de la v4 » (R l. 12–18) remplace le résumé de la v3 à la v4, qui reste au § 6 ;
   « Sources de la v5 » (R l. 37–40) ; « Nature » ne nomme plus le vérificateur (le brief v5 ne le désigne pas ; R l. 33–35) ;
   « aucun fait de course de plus » pour la v5 (R l. 30–31 ; P l. 10–11). Raison : déclaration.
2. **Renvois de version** : registre v5, protocole v4, briefs v4, spécification v3 (P l. 19, 58–61, 82, 160, 356, 417,
   434, 457, 620, 622 ; R l. 91, 639 ; B l. 9–10). « La poussée de ce registre v4 » devient « du registre v4 » (R l. 349) :
   le point d'ancrage de la voie « rondes tournées » ne bouge pas ; le statut de S le dit (S l. 12–14).
3. **E1, mise en œuvre** : le relevé n'accepte que des valeurs de sa grammaire close (S § 3) ; il « dit » donc la lignée
   déduite par un champ nouveau, `identite.lignee_source` (`extrait` ou `deduite_de_la_cle_controle_non_independant`, qui
   se lit « déduite de la clé : contrôle non indépendant »), et l'analyste recopie cette phrase (P l. 377–378 ; R
   l. 640–641). Une relance demande sa ligne dans la table, par une version nouvelle de S et du script (S l. 156–157).
   Artefacts 15 à 18 et attentes des cas sains (S l. 291–293, 298–299, 328–337) : R5, une garde nouvelle par refus. Au
   § 8 : dire aussi si l'extrait porte la lignée, et sous quel champ ; et que les chemins simulés passent la règle du nom.
   Au tableau du § 9 : une ligne pour `identite.lignee_source` (P l. 361). G11 nomme deux des artefacts nouveaux.
4. **E6, mise en œuvre** : au § 2 de S, la liste « n'ouvre jamais » est dite n'être pas une liste de noms écrite dans le
   script (sinon le script contiendrait la chaîne que E6 interdit), et les fichiers que liste `EMPREINTES-pilote-v1.txt`
   sont dits hachés, jamais lus (S l. 77–80) ; la forme de `question_servie` devient `oui|absent` (S l. 221) ; artefact
   19 (S l. 338–339).
5. **E2, lecture avec la règle « impossible »** de la v4 : un test signalé « impossible » se rapporte « impossible »,
   comme avant ; seul un libellé autre que les deux mots arrête l'analyste (B l. 368 ; R l. 598–599). La taille de la
   famille se lit au champ de correction (B l. 361–362).
6. **E7 (b), application de la valeur (c)** : à la ronde 1, un second contre-lecteur, de famille différente, tient les
   parties A et B de chaque course, aux mêmes briefs ; une fiche en désaccord avec l'un ou l'autre ne motive rien
   (P l. 492–494) ; « famille différente » devient « (b) ou (c) » pour le canal (P l. 498–500). Raison : (c) n'avait pas
   de place ; la façon de la tenir est un choix, que conv-audit peut changer.
7. **E4, suites** : une ligne du tableau « qui lit quoi » pour le contre-lecteur de la lecture finale (P l. 102) ; « un
   agent par dossier » devient « chaque agent n'en lit qu'un » (deux agents lisent tour à tour le dossier final ; P
   l. 152–154) ; le nombre de tests (iii) va à l'entrée de clôture (P l. 331) ; forme de l'entrée de clôture (P
   l. 234–238) ; nom du rendu, `contre-lecture-finale-<dossier>-partie-A-v1.md`, choisi ici ; dans la section 3A, le nom
   du manifeste dit à l'agent quel paragraphe vaut pour lui (B l. 270, 277).
8. **E8, suites** : la carte v1 fait des seuils 0,78 et 0,65 un seul facteur, F03, dit « sous réserve » (P l. 274, 618) ;
   l'exemple (a) de G5 n'emploie plus les seuils de stagnation et du retour arrière, devenus points hors boucle (refusés
   pour une autre raison), mais une ligne de F01 et une de F02 ; artefacts (g), (h), (i) de G5 (R5) (P l. 427) ; le
   contrat de l'architecte, au § 14, exclut `seuil_confiance_caste1` (P l. 567–568) ; « écrite par conv-audit » devient
   « écrite pour conv-audit » (un sous-agent l'a écrite : P § 2 et § 6) (P l. 573) ; le correcteur et la partie B
   apprennent la lecture par colonnes et la ligne de `VERSION` (B l. 203–205, 234–237, 319–321) ; § 16 mis à jour
   (P l. 617–622).
9. **Registre, § 7** : une table « v4 → v5 » en résumé (R l. 757–768), comme le § 6 pour la v4.

## 5. Ce qui reste, pour conv-audit (une ligne chacun)

1. Script de lecture v3 : écrire les mots du point 4 bis (« changement au-delà du bruit des tâches », « dans le bruit des
   tâches »), le champ « correction : Holm, quatre tests, niveau 0,05 » (« deux tests » en « holm-deux ») et le sens
   « sans objet (non rejeté) » ; son brief (`78861f99…`, § 3, point 2) disait « rejeté au niveau 0,05, famille de
   quatre » ou « non rejeté » : l'alignement est à transmettre avant la forge des dossiers d'audit de lecture finale.
2. Script du relevé : table de correspondance, règles d'E1 et d'E6, artefacts 15 à 19 ; confirmer sur les séries v13 et
   v14 que chaque ligne qui porte un champ exigé est écrite en simulation, que les chemins et les clés simulés passent la
   table close, et si l'extrait porte la lignée (S § 8).
3. Doute, sans changement : si `EMPREINTES-pilote-v1.txt` liste le fichier de réponse à la question, la vérification le
   hache, comme `ferme.tar.gz` ; un instantané des accès (artefact 4) le montrera ; à voir sur les pièces de la série v14.
4. Contre-lecture de la carte et des zones v1 : si elle mène à une v2, P § 6, § 14 et § 16 citent la v2 (nom et empreinte).
5. Non tranchés par E8, et laissés tels quels : la règle des lignes insérées (carte, § 0, point 9 ; D9), D3 à D5, D8, D10
   à D14 du LISEZMOI de la carte.
6. Valeur (c) du paramètre « famille » : confirmer ou changer la façon de la tenir (§ 4, point 6).
7. Étalonnage à blanc refait sur ces versions (P § 12.5), avant tout verdict d'élimination transmissible.
8. Faire vérifier cette v5 avant son premier usage ; pousser les cinq fichiers et leurs compagnons.

## 6. Écarts déclarés

1. La v4 disait « trois messages » (son LISEZMOI, l. 26, et les statuts) : ils étaient deux, le premier portant les deux
   précisions à D5 (CLB4-07 a). Les statuts de la v5 le corrigent ; le LISEZMOI v4 n'est pas réécrit (R12).
2. Mes pièces v4 ont été copiées depuis `fournis/` dans `sortie/` sous leurs noms v5, rendues inscriptibles
   (`chmod u+w`), puis modifiées : rien n'a été écrit hors de `sortie/`.
3. Les heures de fin des cinq fichiers sont écrites par `sed`, dans la commande même qui lit `date -u`, à la place d'un
   marqueur ; les compagnons sont calculés après. L'heure du début de ma lecture n'est pas consignée ; la seule heure de
   début écrite est celle de l'ouverture de ce fichier.
4. Aucune poussée : sans `git`, elle revient à conv-audit.

## 7. Empreintes (format « empreinte, deux espaces, nom nu »)

```
f04e926361b062702795ae322846898d0a3705ef3864b3f018e34c36173d7138  registre-hypotheses-conception-pilote4-v5.md
0e8cfee5c0e25db11965e99bf0d1c45654e9d7e8f72b8dd67f01e2ee2b34d2e4  protocole-boucle-exterieure-pilote4-v4.md
d5c7a60a7f6a636397b341c5be136a8d4bcec1559d1a5857f77a761295c9d16a  brief-agents-fin-de-course-v4.md
d6ac5d3fa409ab19b4f3e25b600f4da945c62630a189f2e2463a294506eb4bb5  specification-releve-mecanique-B-v3.md
```

L'empreinte de ce fichier est dans son compagnon, `LISEZMOI-sortie-v5.md.sha256`.
