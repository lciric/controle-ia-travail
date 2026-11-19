# Différences entre le brouillon 8 et le brouillon 9 du texte « lecture des sondes du barreau 8 et passe de recalcul de l'activité interne » — v1

- Brouillon 8 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon8.md`, empreinte `d8992b575a4e03fa6647b7d5af663596f80870925164b328adc0985c29f98b3a` (jugé « PRÊT » par son contre-lecteur : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon8-v1.md`, `94aaa09187c9631d2898ae50c8ccc7ec420ece9e71df5068a186aca516ad5e86`, empreinte vérifiée, rapport non ouvert par le rédacteur).
- Sources, lues en entier, empreintes vérifiées : la notice du code de la passe, `docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v1.md`, `45da9b99be0a3f9dacbf0a98aae570982f1f8b4dfb000920a402ec202c9aa472` (citée « notice ») ; la note des lacunes du développeur du code de la lecture, `brouillons/barreau8-lecture-sondes-v1/lacunes-texte-developpeur-lecture-v1.md`, `8f482f4d5fdbd03a26b43f68842ed75d7695ae0bb36c59d55942b6a41655dc49` (citée « lacunes »). **Ni le code ni ses essais n'ont été lus.**
- Brouillon 9 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon9.md` (empreinte : son compagnon `.sha256`).
- Rédacteur : Fable 5.2. Écrit le 2026-11-19 entre @@DEBUT@@ et @@FIN@@ (`date -u` ; mêmes heures que la ligne de date du brouillon 9), par programme, à partir du brouillon 8 : remplacements contrôlés (chaque texte cherché doit paraître exactement une fois, sinon rien n'est écrit). Le programme vérifie que les deux chaînes de la procédure de remplissage restent uniques, que la ligne de F-3 est inchangée au caractère près et qu'il reste exactement deux marqueurs.
- Ni hypothèse, ni prédiction, ni métrique, ni seuil, ni niveau ne changent. La taille au pire reste 1 502 781 440 octets pour les quatre tableaux ; les fichiers que les formes ajoutent tiennent sous 4 000 000 octets (compte du rédacteur ; garde P9).

## 1. Les treize points de la notice du code de la passe

| n° | objet | porté ? | où, dans le brouillon 9 ; raison |
|---|---|---|---|
| P-1 | forme de l'extrait scellé du côté exposé | porté | condition de départ D-13, réécrite (six clés, formes des valeurs, chemins relatifs, ce que la passe en tire, refus sinon) ; garde P1 |
| P-2 | tâches d'évaluation dans P1 | porté | garde P1 : empreinte de la note d'interface, point (b), entière |
| P-3 | lignes de registre et bordereau du code | porté | garde P0 ; D-1 ; « Code, registre et contrôle de conformité » (forme des lignes, conditions d'ordre, deux bordereaux) |
| P-4 | P1 contre la règle mécanique des sondes lues | porté, **durci sur un cas** | règle mécanique ; garde P1 ; liste d'arrêt, ligne 8 ; S3 (ligne de mémoire). **Durci** : une sonde des couches 7 ou 23 trouvée sous son nom mais non conforme arrête la passe, au lieu d'être écrite « sans objet » (lecture la plus stricte déjà implémentée, celle du code de la lecture : lacune 16) |
| P-5 | liste fermée des chemins lus | porté | garde P8, phrase proposée, avec le nom et le dossier de l'invite publiée |
| P-6 | bornes de P9 | porté | garde P9, phrase proposée ; réserve de 4 000 000 octets écrite |
| P-7 | P7 : référence et sens du décalage | porté | garde P7 (p : première passe ; contrôle négatif : g au jeton n contre p au jeton n − 1 ; « au moins 4 comparaisons » = au moins 5 jetons notés) |
| P-8 | P10 : étendue et moment | porté | garde P10 (jeton de fin compris ; artefact et lecture avant la première passe ; (i′) et (ii′)) |
| P-9 | trace : champs de plus et taille | porté | livraison, point 5 ; « Noms et champs », (5) |
| P-10 | graines `repetabilite-passe` et `injection-adaptateurs` | porté | plan, point 5 |
| P-11 | noms et formats des fichiers livrés | porté | « Passe », bloc « Noms et champs, liste fermée » (archives et morceaux, six sortes de fichiers, clés, ordre des colonnes) |
| P-12 | reconstruction du contexte ; clause de plus à P3 | porté | garde P3, clause (d) ; « les clauses (a) à (d) » avant le chargement des poids. La boucle propre à la passe (texte du fichier mis au journal) n'est pas écrite au texte : le texte disait déjà « les textes décodés des actions précédentes », que la clause (b) rend égaux au champ `texte` |
| P-13 | règle des lots et actions vides | porté | « Passe avant », phrase proposée |

## 2. Les dix-neuf points du développeur du code de la lecture

| n° | objet | porté ? | où, dans le brouillon 9 ; raison |
|---|---|---|---|
| L-1 | formats de la livraison | porté, **aux noms et formats de la notice** | bloc « Noms et champs, liste fermée » ; r2 (morceaux, compagnons) ; la notice de la passe fait foi : le code de la lecture s'y réaligne |
| L-2 | fichier de sondes absent : refus ou « sans objet » | porté, **tranché au plus strict** | plan, point 3 ; règle mécanique ; r4 ; liste d'arrêt, ligne 8 : un fichier absent, d'empreinte différente ou sans compagnon arrête la passe et fait refuser la lecture ; « sans objet » ne vient que des conditions (ii) à (iv). L'effet est celui du code de la lecture (refus par r4, la trace ne pouvant dire « sans objet » pour un fichier absent), écrit directement |
| L-3 | S3 « modèle » et S4 ; nombre de couches | porté | S3 (lignes de mémoire, branche « aucune sonde lue » comprise) ; S4 |
| L-4 | « adaptateur et dose relus : non » | porté | r4 |
| L-5 | graine des aires « hors jugement » | porté | « Seuil », condition jugée |
| L-6 | essai de la chaîne : une clé par essai ; écart-type | porté | chapeau de l'essai A0 ; (ii) |
| L-7 | déclencheur d4 et niveaux | porté | audit, « Déclencheurs » |
| L-8 | classe vide ; tâches différentes pour la dose | porté | « Métrique », intervalle ; B8-P3 |
| L-9 | ordre des lignes S et de l'essai de la chaîne | porté | chapeau de la table des issues (la phrase proposée, placée en tête de la table plutôt qu'après elle) |
| L-10 | réserve de validité de la sonde de dissimulation | porté | combinaisons |
| L-11 | recette de la puissance (trois phrases) | porté | plan, point 10 |
| L-12 | pièces de D-5 et D-6 | porté | D-5 ; D-6 |
| L-13 | écriture de F-3 | porté, **ailleurs que dans la cellule** | plan, point 5 ; la cellule « état et raison » de F-3 est inchangée au caractère près (contrôlé par programme) |
| L-14 | taille totale de r2 | porté | r2 |
| L-15 | écart-type du repère r8 | porté | r8 |
| L-16 | sonde des couches 7 ou 23 d'une autre famille | porté | « Métrique » ; liste des directions de la passe ; garde P1 : arrêt de la passe et refus de la lecture |
| L-17 | bordereau du code | porté | « Code, registre et contrôle de conformité » ; D-2 ; contrôle des modules écrit « exactement ceux du bordereau » pour les deux codes |
| L-18 | conditions d'ordre du registre | porté, **une condition changée sur le mot de la session mère** | même section : `ETATS-COURSE-IIB` strictement postérieure au scellement (confirmé) ; `LIVRAISON-PASSE-IIB` strictement postérieure à `CODE-PASSE-IIB` (le développeur n'avait mis aucune condition) ; toute clé hors des six refusée (confirmé) |
| L-19 | essai de la chaîne : étape de la commande | porté | plan, point 4, étape (d) |

Aucun des 32 points n'est laissé hors du texte.

## 3. Autres changements (de conséquence, ou demandés)

- En-tête : titre et statut « brouillon 9 » ; ligne de date ; contre-lecteur du brouillon 8 ; les deux sources citées avec leur empreinte.
- Section « Contre-lecture » : entrée « Contre-lecture 3 quater » (empreintes du brouillon 8 et du rapport ; conclusion « PRÊT » sur le brouillon 8), reconnue par le validateur.
- Audit, contenu (1) : « comptes par condition égaux à ceux de la trace, dix actions par tâche et par condition » — la trace de la notice ne porte pas de compte par tâche.
- r4 : « les modules chargés et leurs empreintes sont exactement ceux du bordereau du code de la passe ».
- Décision de taille : phrase sur les fichiers que les formes ajoutent.

## 4. À réaligner dans le code (le rédacteur n'a lu aucun code : liste tirée des deux notes seules)

**Développeur du code de la passe**
1. Sonde des couches 7 ou 23 trouvée sous son nom mais non conforme : arrêt (garde P1), et non « sans objet » (notice, point 4).
2. Sous-échantillon d'activité brute : le texte le tire dans la liste des actions d'au moins un jeton noté, **triée par le tri des chaînes de Python**, rangs multiples de 16 (ou de 128) et la dernière ; les tableaux sont nommés par le `rang` du fichier. La notice ne dit pas quel ordre le code emploie pour le tirage : à vérifier.
3. Garde P9 : fichiers 1 à 4 et leurs compagnons sous 1 996 000 000 octets (réserve de 4 000 000) : à vérifier que c'est bien la borne codée.
4. La passe ne contrôle pas, d'après la notice, que l'entropie donnée figure dans le texte scellé : le texte ne l'exige que de la lecture et de la recette ; rien à changer, signalé.

**Développeur du code de la lecture**
1. Noms et formats de la livraison : archives `numpy` en morceaux avec fichier de description, noms de fichiers, clés `scores`, `directions`, `agregations`, `colonnes`, listes en JSON dans des tableaux `uint8`, tableaux bruts nommés `a<rang>`, index en lignes JSON à dix champs nommés, clés de la trace et du bordereau (le développeur supposait des tableaux nus et d'autres noms).
2. Garde r2 : le bordereau ne liste ni lui-même ni les compagnons ; rebâtir chaque archive et contrôler taille et empreinte du fichier entier.
3. Fichier de sondes absent ou d'empreinte différente : refus direct (plan, point 3), sans passer par « sans objet ».
4. Registre : `LIVRAISON-PASSE-IIB` strictement postérieure à `CODE-PASSE-IIB` ; `LECTURE-SONDES-IIB` postérieure aux cinq autres.
5. Bordereau du code : modules chargés **exactement** ceux du bordereau (aucun absent, aucun de trop) : à vérifier.
6. Audit (1) : comptes par condition contre la trace ; dix actions par tâche et par condition contre l'index.
7. Trace : champs lus par r4 aux noms de la notice (`conditions.<condition>.adaptateur_et_dose_relus_egaux`, `sondes`, `adaptateurs.<nom>.egale_a_l_extrait`, `chemin_prive_lu`, `modules_charges`, `modele`, `fichiers_sondes`).

## 5. Marqueurs restants

Deux, et deux seulement : F-3 (entropie racine des graines) et l'entrée « Contre-lecture 4 (finale, texte rempli) ». Les deux chaînes de la procédure de remplissage paraissent chacune une seule fois. Sortie exacte du validateur sur le brouillon 9 : `['section vide ou à remplir : Contre-lecture']`.
