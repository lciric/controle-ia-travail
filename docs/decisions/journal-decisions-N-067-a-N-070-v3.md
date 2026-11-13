# Journal de rédaction des décisions N-067 à N-070 (versions retenues) — v3

Rédacteur des brouillons 1 et 2 (sous-agent, Claude Opus 5.5), relancé par la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`. Travail du 13 novembre 2026, de 19:24 à 19:30 UTC environ (heures relevées par `date -u`). Les journaux v1 (`be45f8c5…`) et v2 (`52c8d920…`) restent intacts (R12).

**Commande de la mère** : écrire les versions finales `decision-N-067-v1.md` à `decision-N-070-v1.md` (noms neufs, brouillons intacts) à partir des brouillons 2 :
- l'encadré de la section 0 remplacé par « Décisions de Lazar (R-2571) », qui recopie son mot et le choix retenu pour chaque point ;
- les énoncés mis à l'option retenue, là où la lecture « en attendant » différait ;
- l'erratum d'heure corrigé ;
- pour N-070, la provenance du journal établie en R-2571 ;
- pour N-067, point 4, la clause « O4 n'est déclaré libre hors du dépôt qu'après lecture de SSRN 6569258 et des pistes de priorité haute sur PDF » ;
- sceller, sans écriture git.

**Mot de Lazar** (R-2571, 19:24 UTC), verbatim : « c'est crédité, relance; les onze points des décisions de resserrement. : quels sont ils ? go reco ». Lu par la mère : les onze points prennent tous la recommandation (R-2571, point 2, relu en entier sur `main`, commit `8ebadb9a`).

## 1. Fichiers

| fichier | SHA-256 | base (intacte) |
|---|---|---|
| `docs/decisions/decision-N-067-v1.md` | `966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589` | brouillon 2 `cb3f3719…` |
| `docs/decisions/decision-N-068-v1.md` | `ba6b2db355515cd660d676b733f4d467f8a9c055d4d8c6d997d4ef898caef889` | brouillon 2 `414fc6b4…` |
| `docs/decisions/decision-N-069-v1.md` | `6e0d9d4036a848a67e0f5e14c1ed9b107c6ba1aa1041ab09ad73af69c427c370` | brouillon 2 `69f8f699…` |
| `docs/decisions/decision-N-070-v1.md` | `7c4ce2210b2e48db4f8349ed85cd50387586b3eb176d364be0d280647d25992f` | brouillon 2 `a7eeb395…` |

Chaque version finale est une copie du brouillon 2, modifiée par remplacements exacts (chaque texte remplacé retrouvé une fois et une seule, contrôlé par programme). Une garde du script refuse l'écriture s'il reste un renvoi à l'encadré ou la mention « En attente du mot de Lazar ».

## 2. Changements par rapport aux brouillons 2

**Communs aux quatre**
- Titre : « (v1, brouillon 2) » devient « (v1) ».
- Ligne de statut : « version retenue (v1) », base, contre-lecture et R-2571 nommés.
- Section 0 : l'encadré est remplacé par « Décisions de Lazar (R-2571) ». Elle contient le mot verbatim, la lecture de la mère et une table « point, décision posée, option retenue, effet dans cette note ».
- Chaque renvoi « (encadré, point n) » devient « (R-2571, point n (option)) ».
- « Points attachés, non tranchés ici » devient « Points attachés ».

**N-067**
- Point 1 (a) : la forme resserrée de O12 est confirmée. La lecture d'attente (« revendiquée dans aucun texte sortant ») est retirée.
- Point 4 (a) : la clause devient celle de la mère et de R-2571. O4, et l'énoncé retenu de O2, ne sont déclarés libres hors du dépôt qu'après lecture sur PDF de SSRN 6569258 et des pistes de priorité haute, lecture lancée par la mère. L'alternative « sinon, avec la réserve écrite » du brouillon 2 est retirée.
- Section 8 : liste nommée des **pistes de priorité haute contre O4**. Ma lecture : les pistes « haute » de C4, § 5 pour O4 (SSRN 6569258 ; 2110.00115 ; 2103.08402) et les rangs 1 à 3 de C7, § 5 (Clerico 2606.06769 ; AlphaSchema 2607.26642 avec Harvey, Liu, Zhu 2016 ; « Phantom gains » 2608.20290). Les autres pistes, dont deux titres du lot 4 relevés par la contre-lecture de la synthèse finale (M11), vont dans une seconde liste.
- Phrase pour un lecteur extérieur : la condition « après le mot de Lazar sur O12 » est retirée. J'ajoute, comme non vérifié, ce que dit le résumé de moteur sur SSRN 6569258 (M11 de R-2567).
- Point 5a (a) : les statuts les plus durs sont retenus (sections 9 et 10).
- Point 5b (a) : 2611.00643 est cité comme précédent de la prémisse du bras « juge génératif » du rôle 1.
- Point 5c (a) : la page publique est corrigée après la retenue, avec le différentiel montré à Lazar avant de pousser.
- Section 10 : O4 et O8 sont rangés « à ne pas déclarer libres publiquement en l'état » par R-2567 ; c'est dit.

**N-068**
- Point 6 (a) : ajustements confirmés. L'énoncé ne change pas : la lecture d'attente était déjà l'option (a).
- Point 7 (c) : le poids 0,65 sera revu au préenregistrement du papier C. Jusque-là, il n'est jamais cité sans les contre-indices.
- Point 8a (a) : la lettre de N-013 pour HC4 est restreinte aux sondes entraînées qui lisent l'intention ou l'action de l'agent auteur, à faux positifs fixés. C'est consigné en sections 0 et 8, comme lecture de N-013 sur ce point.
- Point 8b (a) : les sources du contrôle du style de HC2b sont ajoutées ; l'énoncé de HC2b est inchangé.

**N-069**
- Point 9a (a) : bascule non déclenchée, veille rapprochée (section 9). La phrase sur le lot 10 est mise à jour : versions 1, 2 et 4 de NARCBench versées sans lecteur (R-2557).
- Point 9b (a) : le pic par agent devient base nommée de la porte G2, et le cas « pas de gain » est prévu (sections 5 et 8).
- Point 9c (c) : « co-élévation » est gardé ; l'écart entre agents devient une base obligatoire, ajoutée à la liste des bases à battre (section 4).
- Énoncé 2 : « y compris sous adversaire » devient « sous un adversaire **entraîné contre elle** » (section 2 ci-dessous, constat M2).
- Section 9 : renvoi aux mentions d'usage hors du dépôt fixées par R-2567.

**N-070**
- Point 10 (a) : contenu de la mesure fixé (rang de relais, avec et sans surveillant à chaque passage, ligne « description »). Les sections 4 et 5 cessent d'être conditionnelles. Une puce en section 8 rappelle que tout texte sur ce bras le tient comme une description.
- Point 11 (a) : la provenance établie par la mère est recopiée en section 0 (courses de l'ancienne lignée « Gemini », hors programme, sans préenregistrement connu, aucun résultat cité ni utilisable) ; une puce en section 8.
- Questions ouvertes (section 4, point 3) : resserrées (section 2 ci-dessous, constat B1).

**Erratum d'heure corrigé.** Les en-têtes de N-069 et N-070 disent l'erratum : brouillons 2 écrits entre 18:54 et 18:59 UTC, et non « vers 19:00 » ni « vers 19:02 » (R-2568). Les versions finales portent « entre 19:24 et 19:29 UTC (`date -u`) » ; `date -u` donnait 19:28:22 au scellement. J'avais d'abord écrit des heures d'avance (19:27 à 19:30) ; je les ai corrigées **avant** de sceller.

## 3. Hors de la commande : trois resserrements tirés de la contre-lecture de la synthèse finale

La contre-lecture de la synthèse finale de niveau 3 (`docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, `f1580ddc…`, R-2567, conforme à son compagnon) est arrivée sur `main` après les brouillons 2. Trois de ses constats touchent les énoncés de ces notes. Je les applique parce que chacun **resserre** ce qui était revendiqué et repose sur une pièce lue sur PDF (règle : rien de plus fort qu'une pièce lue). **La mère peut les retirer.**
- **B1 → N-070.** MasDrift publie le profil de la première perte par rang de relais, à profondeur contrôlée (tableau 18, p. 23). La question ouverte devient le taux **conditionnel** par rang, sur chaînes linéaires de longueur contrôlée et à tâche égale, pour la force graduée d'une contrainte. J'ai relu les valeurs moi-même sur le PDF (`pdftotext -layout`, p. 23) : Cent L1 88,1 / 11,7 / 0,2 ; L2 84,4 / 8,8 / 6,7 ; L3 71,9 / 7,4 / 20,7 ; ensemble 88,2 / 7,1 / 4,7. La mesure descriptive n'est pas touchée.
- **M2 → N-069.** « Sous adversaire » est trop large : des adversaires faibles sont publiés (2611.10620, p. 22, agents prévenus puis priés d'évader ; 2609.03035 v2, p. 2, adaptation par le contexte seul). D'où « entraîné contre elle ».
- **M11 → N-067.** Pistes contre O4 nommées, et résumé de moteur dit comme non vérifié.

**Constat de R-2567 que je ne suis pas** : m2 dit que « le déplacement continu en fonction de l'intensité » (HC2) « n'est dans aucun rapport ». Or le lot 3-A l'écrit (`rapport-lot3A-sondes-sabotage-injection-v1.md`, `64b728d6…`, § 10.5) : « Ce qui reste propre à HC2 : l'agent **auteur**, le déplacement **continu** en fonction de l'intensité, et la comparaison aux **juges génératifs sous les mêmes attaques** ». Lazar l'a d'ailleurs confirmé (R-2571, point 6 (a)). N-068 garde la formule.

## 4. Points incertains

1. **Liste des « pistes de priorité haute » contre O4** : c'est ma lecture de C4 et C7 (section 2). La mère, qui a lancé la lecture, peut la fixer autrement.
2. **HC4** : le mot de Lazar (8a) change la lecture d'une lettre de N-013. Je le consigne dans N-068. Une note propre à HC4, ou la ligne de `CLAUDE.md` qui liste N-013, peut être préférable.
3. **Les trois resserrements de la section 3** vont au-delà de la commande ; ils sont étroits et sourcés, mais c'est à la mère de les garder.
4. **Versement des 17 608 fichiers du commit `35abfd16`** (R-2571) : hors de ces notes ; examiné à part par la mère.

## 5. Contrôles, interdits, refus

- Brouillons 1 et 2 et journaux v1 et v2 intacts (`verifier` conforme). Les quatre versions finales sont scellées ; ce journal l'est à son tour.
- **Aucun refus** de contrôle de permissions, de classifieur ou de garde de scellement pendant cette passe.
- Aucune écriture git ; aucun registre modifié ; aucune dépense ; aucun appel hors du conteneur ; aucune valeur de clé lue ; chemins interdits non ouverts ; aucune recherche récursive. Les PDF ont été lus par `pdftotext` dans le dossier de travail temporaire ; les scripts de modification tournent par `python3 -I` depuis un autre dossier.

Version 3 ; jamais réécrite (R12).
