# Journal du brouillon 11 du texte de la base boîte noire (T0.8) — v1

- **Nature** : pièce de travail (classe C). **Auteur** : session `session_013QMayo5SNVbiUW6hGnPrCo` (modèle B), rédacteur du brouillon 11, fille de la session mère `session_013QMayjbmQUdDuDs2S3i3XD`. **Accords** : GO-2026-11-22-77, GO-2026-11-22-113.
- **Heures (UTC, `date -u`)** : session ouverte le 2026-11-22 à 18:11 ; inscription à la liste « qui a lu quoi » envoyée à la mère à 18:15, avant l'ouverture du texte ; brouillon 11 produit vers 18:33 ; journal clos vers 18:45.
- **Ce que la session rend** : le brouillon 11 (candidat 2, texte complet), `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon11.md`, **non scellable tel quel** : quatre marqueurs restent, dont le commit du code, rouvert. Empreinte : dans le compagnon et dans le message à la mère.

## 1. Ce qui a été trouvé

Le texte de la base boîte noire n'était pas à écrire : il existait, et il est gelé.

- **Brouillon 4**, gelé le 10 novembre (ligne `GEL-T08`, R-2251), avant la course de confirmation : tous les seuils, règles et réglages y sont fixés. Sa règle « Gel vérifiable » interdit ensuite toute différence dans les sections « Hypothèse » à « Liste d'arrêt », hors marqueurs remplis, déclarations de vue et corrections de renvoi.
- **Brouillons 5 à 10**, écrits le 14 novembre par la session du compte 4 sur la branche `lot/compte-4-v1`, jamais versés dans `main` : code cité, une phrase ajoutée au point 1 du plan (dite T5-19, gardée par le mot de Lazar « go a pour T5-19 », R-2657), sept relectures. Le brouillon 10 est le candidat rendu à la mère (R-2642). Rien n'a bougé depuis.
- **Code** de la course et de la lecture : commit `453a71e1`, branche `prep/t08-code-compte4-v1`, 142 essais, contre-lu et vérifié deux fois.
- **Aucune session précédente** n'a laissé de branche `prep/t08-texte-complet-fable-v1`.

Le travail a donc été : partir du candidat, remplir ce que le registre permet de remplir, déclarer ce que les décisions prises depuis demandent, et dire ce qui empêche encore de sceller.

## 2. Ce que le brouillon 11 fait (31 opérations, toutes par programme)

Détail, texte ancien et texte nouveau : `couples-t08-brouillon11-v1.json`. Résumé : `differentiel-gel-t08-brouillon11-v1.md`, section 3.

- **Quatre marqueurs remplis** : la ligne du code « mots et coût » ; le run de 7b ; les cinq empreintes d'entrée, lues sur leurs compagnons seuls ; la ligne de GO.
- **Un marqueur rouvert** : le commit du code (section 3 de ce journal).
- **Renvoi corrigé** vers le texte de validité de l'adaptateur, scellé le 14 novembre.
- **Section neuve « Depuis le gel du 10 novembre »** : faits du registre ; déclaration de la référence honnête (N-076) ; alignement du code ; quatre gardes de code plus strictes que la lettre ; panne technique et relance ; concordance avec le brouillon de grille de G0 ; points laissés à Lazar.
- **Calendrier à jour**, en-tête court, ancien en-tête recopié en annexe, déclaration de vue de l'auteur, relecture exigée, table des marqueurs.

**Sections gelées touchées** : « Métrique » (une valeur de marqueur) et « Plan d'analyse » (deux valeurs de marqueurs). Rien d'autre. Contrôle par programme : la plage gelée du brouillon 11, une fois retirée la ligne T5-19 et remis les noms des marqueurs, est égale à l'octet à celle du brouillon 4 (174 lignes).

## 3. Choix, et pourquoi

1. **Ne rien changer au fond.** Les seuils sont gelés depuis le 10 novembre et des résultats de 7b ont été lus par d'autres sessions depuis le 13. Toute retouche d'un seuil aujourd'hui serait indéfendable, même faite à l'aveugle. La règle du texte est la bonne ; je l'applique.
2. **Rouvrir le marqueur du commit du code.** Le code attend que la ligne `CODE-MOTS-ET-COUT-T06` porte l'empreinte du module de la pièce ; elle porte celle d'un fichier d'inscription. Il importe la pièce par un nom de module ; elle se charge par un chemin. En lecture réelle, le contrôle du code échouerait donc toujours. C'est connu depuis le 14 novembre (réserves R-D15 et R-D16 de la pièce, R-2778 : « à aligner dans T0.8 avant son scellement ») et n'a jamais été fait. Sceller le texte avec ce commit serait sceller une course dont la lecture ne peut pas partir. D'où le marqueur rouvert et une consigne d'alignement étroite (`consigne-alignement-code-t08-v1.md`).
3. **Laisser trois marqueurs à la mère** : l'entropie, que le plan veut tirée au scellement ; la ligne d'engagement ; la ligne du registre qui confirme les gardes de code. Un programme les remplit et rejoue le contrôle du gel (`finaliser-t08-scellement-v1.py`), éprouvé sur un cas sain et quatre artefacts (un seuil gelé changé, une phrase gelée retouchée, un commit court, une ligne de dépense sans la tâche) : tous arrêtés.
4. **Engagement au scellement, non « au lancement ».** Les brouillons 1 à 10 voulaient la ligne d'engagement « au lancement », alors que le validateur refuse tout marqueur restant : contradiction de forme. La table des marqueurs dit maintenant « au scellement, avant la création ».
5. **Déclarer la référence honnête** dans une section à part, sans toucher la « Métrique » : N-076 le demande à toute accumulation et nomme les bases boîte noire (son point 4).
6. **Dire ce que la grille de G0 cherchera**, sans plier le texte à une grille qui n'est pas décidée.
7. **Verser les brouillons 5 à 10** et leurs pièces depuis `lot/compte-4-v1` (60 fichiers, empreintes vérifiées contre leurs compagnons) : sans eux, le brouillon 11 citerait des chemins absents de sa branche. Les journaux du compte 4 ne sont pas versés : ils restent cités sur leur branche.
8. **Aucun identifiant de modèle** dans les fichiers versés : « modèle A » et « modèle B », comme le veut R-2598. L'auteur du brouillon 11 est le modèle B ; le contre-lecteur sera le modèle A.

## 4. Avis de conception sur les sections gelées

Demandé par la règle « qui conçoit » : le texte gelé a été écrit par le modèle A et contre-lu par le modèle B, l'inverse de la règle d'aujourd'hui. Je l'ai relu en entier comme si je devais le signer. **Je ne vois aucun défaut qui demande un nœud.** Trois limites sont à dire telles quelles à l'entretien, et le texte les déclare déjà :

- **Puissance.** 64 épisodes par condition. Entre 3 % et 25 % de taux d'alerte vrai, l'issue la plus probable est « intermédiaire ». Une dose « intermédiaire » ne se lit jamais « diffuse ».
- **Lecture du 1 %.** « Calibré à 1 % de faux positifs » est lu par épisode entier, non par action. Cette lecture rend « diffuse » plus facile à atteindre. Le taux par action est rapporté à côté.
- **Périmètre.** Version 0 : sans TRACE-lite, sans la base (iv), sans juge Qwen, sans Liars' Bench ni SHADE-Arena. La phrase du critère 4 les nomme.

Deux points qui auraient pu inquiéter et qui tiennent : les deux surveillants appris sont entraînés sur la dose qu'ils jugent, ce qui les rend forts et pousse vers « flagrante », donc prudent pour qui voudrait dire « diffuse » ; le calibrage sur 128 épisodes par pli garde le même niveau garanti que sur 256.

## 5. Écarts, accès mécaniques, routine

- **Recherche large au début** : une recherche de noms de fichiers par mots sur tout l'arbre de `main`, avant d'avoir lu la liste « qui a lu quoi ». Elle a parcouru des contenus sans en afficher ; seuls des noms de fichiers sont sortis. Déclarée dans le texte. Une recherche de ce genre a déjà valu un refus à un contre-lecteur : à ne pas refaire.
- **Branches de sortie** de 7b et de la pièce « mots et coût » : récupérées sans leurs contenus ; six compagnons d'empreinte lus, rien d'autre.
- **Aucun refus d'outil.**
- **Routine de reprise** : empreintes des documents de lancement conformes ; `verifier-arbre` rend 91 écarts, tous hors de ce chantier (90 compagnons absents, une passation mal nommée), non traités ici ; état et rappels lus (aucun rappel échu le 22) ; **inventaire des machines non fait** : cette session ne lance rien et la mère tient les machines en tâche ; **défauts échus non appliqués** : à la mère.
- **Essais** : la suite complète ne se collecte pas dans ce conteneur (bibliothèque de réseaux de neurones absente : 130 fichiers d'essais en erreur de collecte). Les essais qui se collectent sans elle ont été rejoués ; bilan dans la passation. Aucun fichier de `src/` ni de `tests/` n'est touché.
- **Registres** : rien écrit dans `registres/etat.md`, `decisions.md`, `go.md` ni dans la liste « qui a lu quoi » ; les lignes proposées sont dans le message à la mère.

## 6. Ce qui reste avant la course

| n° | quoi | qui | bloque le scellement |
|---|---|---|---|
| 1 | Contre-lecture du brouillon 11 (`consigne-contre-lecture-t08-brouillon11-v1.md`), corrections, vérification | contre-lecteur neuf du modèle A ; rédacteur | oui |
| 2 | Alignement du code, contre-lecture, vérification ; commit pour `CODE-T08` | développeur neuf du modèle A ; contre-lecteur d'un autre modèle | oui |
| 3 | Ligne du registre : trois gardes de code confirmées, sort de VT5-07 | mère ; Lazar, ou défaut sous 48 heures | oui |
| 4 | Programme de scellement : entropie, engagement, validateur, différentiel ; lignes `SCELLEMENT-T08` puis `CODE-T08` | mère | — |
| 5 | Branche d'entrée (liste blanche des fichiers de 7b), passage à blanc sur le registre réel, ordre de course | mère ; rédacteur pour l'ordre de course, si la mère le demande | non, mais avant la création |
| 6 | Course (≈ 14 à 20 h), lecture sur processeur, verdict par un agent neuf | exécutante ; lecteur ; juge | — |

**Point de procédure pour la mère** : après le 30 novembre, la garde de calcul devra lire la ligne de prolongation `GO-2026-11-22-79`, dont la colonne du plafond renvoie à une autre ligne au lieu de porter un montant. À éprouver avant une création tardive. Le texte porte les deux identifiants.

## 7. Devis de la course

Inchangé depuis le 10 novembre ; aucun prix n'a été relevé le 22 (ni clé ni outil du loueur dans cette session).

- **Attendu** : ≈ 17 à 30 USD (centre ≈ 23) : 14 à 20 h d'une carte A100 SXM4 80 Go à 1,09 à 1,30 USD de l'heure, plus disque et téléchargement.
- **Pire cas** : ≈ 57 USD si la machine est deux fois plus lente ; ≈ 114 USD avec une relance complète.
- **Plafond** : 120 USD (`GO-2026-11-10-12`) ; compte rendu à 40 USD ; aucune carte H200 sans un mot de Lazar.
- **Lecture, verdict, alignement du code** : processeur et sessions, aucune location.
- **Ce qui est supposé** : les débits des juges, tirés de P3 et non mesurés sur cette tâche. C'est le poste le plus incertain (5,9 à 8,8 h pour le juge de 8 milliards de paramètres).

## 8. Points ouverts pour Lazar

1. **Garde d'antériorité du texte et du code sur la course (VT5-07).** Le code arrête la lecture si le texte ou le code ont été inscrits après le début de la course ; la « Liste d'arrêt » gelée ne nomme pas cet arrêt, et le mot « go a pour T5-19 » non plus. Options : (a) la garder, déclarée dans la section neuve — elle n'applique que R1 ; (b) la retirer du code — la lecture partirait même sur une course non préenregistrée ; (c) l'écrire dans la « Liste d'arrêt » — c'est un écart au gel. Recommandation : (a). Confiance 0,8. Défaut sous 48 heures : (a).
2. **Ce que la version 0 reporte** (TRACE-lite, base (iv), juge Qwen, Liars' Bench, SHADE-Arena) : la phrase du critère 4 dira « rempli » sans eux, en les nommant. N-061 attache Liars' Bench et SHADE-Arena à T0.8 : cette version ne les joue pas. Pas de décision à prendre si le report du 10 novembre lui a été dit ; sinon, à lui dire.
3. **Calendrier.** Scellement le 26 si la contre-lecture et l'alignement du code sont finis le 25. Verdict au mieux le 28 ou le 29, soit à la limite du dossier de l'entretien. Sinon la base se présente « préenregistrée, en cours », sans chiffre.
