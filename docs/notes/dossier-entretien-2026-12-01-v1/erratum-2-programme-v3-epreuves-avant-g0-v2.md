# Erratum 2 du programme v3 — deux épreuves inscrites au programme, dont une avant la porte G0 — v2

v2 : corrections de la contre-lecture d'Opus 5.5 (`docs/notes/dossier-entretien-2026-12-01-v1/contre-lecture-errata-table-programme-opus-v1.md`, cfee3cb5 ; verdict « à corriger »). Défaut P1 : seule la tenue est placée avant la porte G0 ; le témoin bénin apparié est inscrit, sa place et son plan restant à dire ; « plusieurs courses » devient une raison de méthode, attribuée au relais de la session mère. Défaut P2 : le périmètre fixé par GO-2026-11-24-32 est enregistré dans E-1. La v1 (0dddfaeb…) reste au dossier, sans modification. Corrections écrites le 2026-11-24 vers 19:00Z (`date -u` relevé à 18:57Z) ; à vérifier par le même contre-lecteur.

Écrit le 2026-11-24 vers 18:50Z (`date -u` relevé à 18:40Z au début du travail, à 18:47Z à l'écriture). Rédacteur : Claude Fable 5.2 (`claude-fable-5-2`), effort élevé, sur la consigne `docs/notes/dossier-entretien-2026-12-01-v1/consigne-fable-errata-table-et-programme-v1.md` (80c156c7). Pièce de travail : ni scellée, ni contre-lue à l'écriture.

**Verdict.** Deux entrées inscrivent deux épreuves au programme. La tenue de nos organismes face à un entraînement sans contenu vient avant la porte de fin de phase 0 (G0), comme caractérisation et non comme parade. Le témoin bénin apparié est inscrit ; sa place par rapport à cette porte et son plan restent à dire. Aucune prédiction, aucun seuil, aucun critère de porte n'est ajouté. Page de Soopal et al. : p. 6 (section 4.3), reprise p. 7 et 8 (discussion).

**Décisions enregistrées** (`registres/go.md` sur `origin/main`, commit `123c3f2c0`, SHA-256 du fichier 587a0951 ; lignes identiques au commit `138bb1070` lu pour la v1) :
- GO-2026-11-24-21, point 10 : « la première épreuve est de vérifier que nos organismes tiennent face à un entraînement sans contenu : inscris-le dans le programme ».
- GO-2026-11-24-22 : « go » pour inscrire au programme les deux priorités communes à Fable, Carbon et Opus : le témoin bénin apparié, et la tenue des saboteurs face à un entraînement sans contenu.
- GO-2026-11-24-31, point 3 : tenue de l'adaptateur sous récompenses au hasard, option (a), « AVANT la porte G0 ».
- GO-2026-11-24-32 : périmètre de l'épreuve de tenue. Elle « se conçoit et se lit comme une caractérisation » ; la porte d'une présentation comme parade reste ouverte, mais « toute revendication de parade exigera une décision nommée de Lazar et la révision de l'invariant « aucun score de moniteur dans l'entraînement de l'agent » (N-053) ; rien n'est revendiqué aujourd'hui ».

**Lu.** Le programme v3 scellé provisoirement, en entier (`docs/programme-controle-ia-v3.md`, fcc27171). Son erratum 1, version 3, en entier (5b8be265). La copie de lecture avec l'erratum 1, variante B (ad118b3e) : comparée par programme au texte scellé, huit lignes diffèrent, celles des huit entrées de l'erratum 1. Les lignes d'accord ci-dessus. Pour la v2 : la contre-lecture, en entier. Soopal, Agrawal, Karthikeyan et Lue Chee Lip, « Stress-Testing Sandbagging Detection Under Adaptive Attack », arXiv 2611.14950, version 1 du 11 novembre 2026 (`docs/sources/pdf/2611.14950v1.pdf`, 6396abd53a24b457519a4f5e5d669a74e1a91cce9a6e5b6b4175821ad3ab94d6, identique à son compagnon) : 14 pages ; lues, les pages 1 (résumé), 3 (contributions, travaux voisins), 4 (règle de transfert), 6 (section 4.3 et figure 3), 7 et 8 (discussion, conclusion, limites) ; le reste parcouru par mots.

**Non lu.** Aucun préenregistrement, aucun devis, aucun avis d'Opus, de Carbon ou de Neon sur ces épreuves. Aucun fichier de résultats, de diagnostic, de scores, de verdict ou de lecture ; rien sous `coffre/`.

## Ce que dit la page citée (règle R7)

Le PDF ne porte pas de numéro de page imprimé : les pages sont celles du fichier.

- **p. 6, section 4.3** (« Activation probes detect fine-tuning, not sandbagging »). Une sonde apprise contre le modèle de base signale presque tous les exemples d'adaptateurs bénins. Apprise contre un adaptateur bénin apparié, elle « works within one training run » ; puis : « It does not carry across runs (Figure 3). » En mettant cinq paires de graines en commun et en en tenant une à l'écart, la sonde appariée passe la règle de transfert des auteurs dans 1 pli sur 5 ; avec les négatifs de trois recettes bénignes, dans 2 plis sur 5, quand la règle en exige 4 (règle fixée d'avance, p. 4).
- **p. 7 et 8, discussion.** « Probes need matched controls across training runs. » Et : « A matched benign adapter fixes this within a training run but not across runs ».

**Portée de cette source.** Elle sert ici de raison de méthode, non de décision. Elle soutient « un seul témoin bénin apparié, dans une seule course d'entraînement, ne suffit pas ». Elle ne dit pas que plusieurs courses suffisent : chez ses auteurs, la sonde échoue aussi à leur règle sur plusieurs courses. Son terrain est la sous-performance délibérée aux évaluations, sur de petits modèles à adaptateur ; l'emploi pour nos saboteurs diffus est notre lecture.

## Forme, pour le programme d'application

Cible : `docs/programme-controle-ia-v3.md` (fcc27171bb87e35a42a6e200bb7ddf8c3df9106141b6eace541e283beb5458c9).

Même forme que l'erratum 1 : trois lignes consécutives par bloc, une ligne vide entre les blocs. Aucun texte ANCIEN ni NOUVEAU ne porte de guillemet français, de saut de ligne ni la marque de simulation.

Vérifié par programme, en lecture seule. Chaque ANCIEN figure une fois dans le programme scellé (lignes 200 et 275) et une fois dans la copie de lecture où l'erratum 1 est appliqué. Aucun ANCIEN ne contient un ANCIEN de l'erratum 1, variante B, ni n'y est contenu ; leurs positions dans le texte scellé ne se recouvrent pas. L'entrée E-1 touche la ligne de la porte G0 ; l'entrée L-6 de l'erratum 1 touche la ligne qui la précède. Les deux errata s'appliquent donc dans un ordre quelconque.

Empreintes après application des deux entrées, dans l'ordre, par simple remplacement (calculées en mémoire, aucun fichier écrit) :
- sur le programme scellé seul : `8040b0fc4031ea8a7904a85476ab2f0aa5e312ffd6358357dbc80af8769f0e2c` ;
- sur la copie de lecture avec l'erratum 1, variante B : `5edc849a0105bc309ddafa3612698907112bac6d4292314e21f9935411731de9`.

## Entrées

Cible : docs/programme-controle-ia-v3.md

**E-1.** ANCIEN : « **Porte G0 (prêt pour G1)** : »
NOUVEAU : « **Deux épreuves inscrites au programme le 24 novembre 2026.** (i) Avant la porte G0 : la tenue de nos organismes face à un entraînement sans contenu, soit la tenue de l'adaptateur sous récompenses au hasard. C'est la première épreuve (GO-2026-11-24-21, GO-2026-11-24-22, GO-2026-11-24-31). Son périmètre (GO-2026-11-24-32) : elle se conçoit et se lit comme une caractérisation, non comme une parade ; rien n'est revendiqué. La présenter un jour comme une parade exigerait une décision nommée de Lazar et la révision de l'invariant de la décision N-053, aucun score de moniteur dans l'entraînement de l'agent. (ii) Le témoin bénin apparié (GO-2026-11-24-22) : inscrit au programme ; sa place par rapport à la porte G0 et son plan restent à dire. Raison de méthode, relayée par la session mère et non portée par la décision : le lire sur plusieurs courses d'entraînement, un seul témoin ne suffisant pas. Chez Soopal et al. 2026 (arXiv 2611.14950, version 1 ; pages du PDF : p. 6, section 4.3 ; p. 7 et 8, discussion), une sonde apprise contre un adaptateur bénin apparié sépare dans la course d'entraînement où elle est apprise, et ne se transporte pas aux autres courses ; chez eux, la mise en commun de plusieurs courses échoue aussi à leur règle. Leur terrain est la sous-performance délibérée aux évaluations, non le sabotage diffus : la transposition est notre lecture. Règles en vigueur, rappelées : préenregistrement scellé avant toute lecture décisive, devis avant toute dépense. Cette inscription ne change aucun critère de la porte. **Porte G0 (prêt pour G1)** : »
Raison : Section 10, phase 0. GO-2026-11-24-21, point 10 : « la première épreuve est de vérifier que nos organismes tiennent face à un entraînement sans contenu : inscris-le dans le programme ». GO-2026-11-24-31, point 3 : tenue de l'adaptateur sous récompenses au hasard, option (a), « AVANT la porte G0 ». GO-2026-11-24-32 : l'épreuve de tenue « se conçoit et se lit comme une caractérisation » ; « toute revendication de parade exigera une décision nommée de Lazar et la révision de l'invariant « aucun score de moniteur dans l'entraînement de l'agent » (N-053) ; rien n'est revendiqué aujourd'hui ». GO-2026-11-24-22 : « inscrire au programme les deux priorités communes à Fable, Carbon et Opus : le témoin bénin apparié, et la tenue des saboteurs face à un entraînement sans contenu » ; cette ligne ne dit ni la place du témoin par rapport à la porte, ni « plusieurs courses ». Soopal et al. : `docs/sources/pdf/2611.14950v1.pdf` (6396abd5), p. 6 : « works within one training run […] It does not carry across runs » ; p. 7 et 8 : « Probes need matched controls across training runs. […] A matched benign adapter fixes this within a training run but not across runs ».

**E-2.** ANCIEN : « | Phase 0, porte G0 | »
NOUVEAU : « | Phase 0 ; avant la porte G0 : tenue de nos organismes face à un entraînement sans contenu (tenue de l'adaptateur sous récompenses au hasard ; caractérisation, non parade) ; porte G0 | »
Raison : Section 14, table du calendrier, ligne M0. GO-2026-11-24-31, point 3, et GO-2026-11-24-32. Le témoin bénin apparié n'entre pas dans cette table : sa place par rapport à la porte n'est pas dite. La période écrite dans cette ligne n'est pas touchée.

## Ce qui reste ouvert

1. **Place et plan du témoin bénin apparié : nœud pour Lazar.** GO-2026-11-24-22 l'inscrit au programme, sans plus. Sa place par rapport à la porte G0, son ordre avec la première épreuve et son plan (sur combien de courses d'entraînement) ne sont dits par aucune ligne lue. « Sur plusieurs courses, un seul témoin ne suffisant pas » est le relais de la session mère, appuyé sur Soopal et al. : une raison de méthode. Si un mot de Lazar ou une ligne de registre le porte, E-1 se resserre par un erratum court.
2. **Ce que l'issue de chaque épreuve commande : nœud pour Lazar.** Les décisions lues inscrivent les épreuves ; elles ne disent pas ce qu'un échec change à la porte G0, aux organismes ou aux sondes. Les critères de la porte ne sont pas touchés (`CLAUDE.md` : « critères inchangés »).
3. **Portée de la première épreuve.** Lazar dit « nos organismes » ; l'option retenue dit « l'adaptateur ». Le programme a deux modes d'induction (consigne cachée, adaptateur). J'ai écrit les deux formules côte à côte. Périmètre interne de la phase : à proposer avec recommandation.
4. **Préenregistrements et devis.** Les deux épreuves n'ont, à ma connaissance, ni préenregistrement ni devis ; je n'en ai lu aucun. Ils restent à écrire avant toute lecture décisive et toute dépense. Le préenregistrement de la tenue devra porter le périmètre de GO-2026-11-24-32.
5. **Dates.** La section 10 et la table de la section 14 portent encore « 5 octobre → 1er novembre 2026 » pour la phase 0. Selon `CLAUDE.md`, la porte G0 est attendue au plus tard fin décembre 2026 (GO-2026-11-18-01). Je n'y ai pas touché : hors de la consigne.
6. **Trois passages de la section 5 attendent leur propre erratum**, par les décisions sur la table des revendications (GO-2026-11-24-21, point 5) : « plate » sans la condition d'indépendance des copies honnêtes (H3), « angle mort identifié » (Tr), la loi sur le nombre et la diversité des moniteurs (H5). Ils ne sont pas dans cet erratum : la consigne le borne aux épreuves.
7. **En-tête du programme.** Il cite l'erratum 1, non celui-ci. Une retouche hors blocs reste à la main de la session mère, si le texte corrigé doit le dire.
8. **Transposition de Soopal et al.** Voir « Portée de cette source » : une sonde y échoue aussi sur plusieurs courses. Le texte inséré le dit en une phrase. Rien n'est prédit ici.

## Confiance

Exactitude des deux textes ANCIEN et absence de recouvrement : 0,97, vérifiées par programme. Pages de Soopal et al. : 0,95 (confirmées par la contre-lecture). Fidélité aux décisions : 0,9. Ensemble : 0,88.
