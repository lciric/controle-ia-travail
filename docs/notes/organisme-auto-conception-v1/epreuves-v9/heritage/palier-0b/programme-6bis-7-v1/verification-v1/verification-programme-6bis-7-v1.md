# Vérification du programme des étapes 6 bis et 7 du palier 0b — v1

Vérificateur neuf, modèle S (n'a écrit ni le programme, ni le code v6, ni leurs textes). 2026-11-20. Pièce de travail (classe C) sur une pièce d'instrument. Rien n'est lancé en vrai, aucune graine décisive dérivée, rien écrit dans le dépôt.

## Verdict : **Conforme**

Pas de code v7 à recommander. Deux précisions à inscrire en v15 (§ 6), aucune correction du programme.

## 1. Empreintes et table
Mandat du développeur `dd30e127…`, brouillon v15 `33b04ff4…`, programme `ed91813a…`, essais `69aa2ad4…`, rapport `14158882…`, table `8b95dc40…` : égaux à ceux annoncés. Compagnons du programme, des essais et du rapport : OK. Table du sous-dossier (4 lignes : journal, programme, rapport, essais) : 4 OK. Copie du code v6 sous mes essais : table `639335b9…` rejouée, 0 écart.

## 2. Essais rejoués
Sur une copie du dossier, avec le code v6 (copie contrôlée), `PYTHONPATH=src`, `HERITAGE_DEPOT`, `HERITAGE_COPIE_ORGANISME` : fichier d'essais du programme plus l'essai final « aucune graine décisive » du code v6 : **21 passés, 0 échoué (7 s)**. Racine, pièces et gelés factices ; couche « essai-de-forme » seule (essai final du fichier : aucune autre couche dérivée). Deux défauts plantés à la main sur des copies : pièce de contrôle sans l'empreinte du programme non contrôlée → vu (`controle-sans-empreinte-du-programme`) ; dossier existant non refusé → vu (`dossier_deja_present`). Je n'ai pas planté le défaut « couche non contrôlée » : il aurait fait dériver une graine décisive sur racine factice (interdit) ; l'essai des sept couches interdites reste vu par lecture (contrôle de la couche en tête de `lancer`, l. 116-118, avant toute pièce).

## 3. Le programme n'appelle que des fonctions du code v6
Fichier `lancer_etapes_6bis_et_7_v1.py` : `GR.Autorisation` l. 67 ; `GR.verifier_scelle` l. 69 ; `EP.plan_des_cases` et `EP.reglages_pour_le_plan` l. 84 ; `EP.relire_fichiers_geles` l. 125 ; `GR.Graines` l. 132 ; `EP.etape_6_bis_et_7` l. 140 (qui appelle la couche mécanique, la couche statistique et `equivalence.garde_equivalence`) ; `EQ.ArretEquivalence` l. 142 ; `TI.ecrire_manifeste` l. 154 ; constantes `K.*` l. 87-89, 132. Code propre, sans calcul statistique : `empreinte_du_programme` (l. 57), le tri des configurations (l. 79-97, un filtre des cases du plan), `_ecrire_scelle` (l. 100-108, écriture exclusive d'un fichier et de son compagnon) et la sérialisation JSON du détail (l. 145-147). Aucune fonction neuve requise dans le paquet. Signatures vérifiées contre `etapes.py:230` et `tirages.py:352`.

## 4. Lettre du texte
- Ordre des opérations (v13:387) : « 6 bis. Couche mécanique rejouée aux réglages gelés, sous des étiquettes de graines disjointes, pour la garde d'équivalence. 7. Garde d'équivalence S8. » : une seule fonction du code v6 fait les deux ; couche « mecanique-reglages » (nommée par `graines.py:6` pour l'étape 6 bis), racine `RACINE_GRAINES` ; étiquettes d'essai de la seule famille « etape-6-bis » et « etape-7 » (essai de la chaîne entière).
- B2 : 24 sources par dose et par proposeur (`SOURCES_COUCHE_MECANIQUE` = 24, défaut) ; bras 1, 2, 3 seulement (B7 bis : « S8 ne porte que sur les trois bras du critère »).
- S8 (ii) (v13:217) : niveau 99,9 % (`NIVEAU_PREDICTION_S8`), arrêt si une moyenne sort de l'intervalle : le programme écrit la cause (scellée), le manifeste (issue « arrêt »), puis s'arrête avec code non nul (liste d'arrêt, point 4). La « soixantaine de comparaisons » : j'ai recompté les 22 couples à la main contre le plan des cases : sourd à appels égaux 3 (doses 0,25 ; 0,5 ; 0 de la famille C), sourd qui paie 3, lecteur héritage 3, lecteur tenue 2, lecteurs deux réglages 2, suiveur 2, suiveur à la lettre 2, généraliste 2, copieur 3 : 22 × 3 bras = 66.
- S8 (i) n'est pas rejouée ici : le code v6 la joue à l'étape 4 au gel des fréquences (`etape_4` appelle `verifier_s8_i`). Rien à corriger ; si la mère veut la ligne en double, c'est un appel existant (`frequences.verifier_s8_i(f)`) sans code v7.

## 5. Gardes
Verrou (`Autorisation`, code v6 inchangé) exigé avant toute lecture de gelés ; pièce de contrôle présente, scellée, portant le commit de la pièce d'autorisation et l'empreinte du programme (proposition, silence n° 5) ; gelés relus par empreinte et compagnon (R11) ; couche limitée à « mecanique-reglages » (et « essai-de-forme » pour les essais) avant tout geste ; tailles réduites ou sous-ensemble refusés sous la couche des étapes ; dossier neuf exigé ; manifeste R9 (configuration, étiquettes, commit, gelés vérifiés, empreinte du programme). Chacune a son essai, cas sain et artefact. Ordre : couche, taille, dossier, pièces, gelés.

## 6. La réserve : le tri des configurations, faut-il un code v7 ?
**Recommandation : non.** Raisons : (a) le verrou ne contrôle que les modules du paquet ; le programme lui-même est hors paquet, comme celui des étapes 8 et 9, et c'est la pièce de contrôle de la mère, qui doit porter son empreinte, qui le fixe ; mettre le tri dans le paquet ne le soumettrait pas à un meilleur contrôle, seulement à la même table ; (b) le tri n'a aucun effet sur un tirage décisif : il ne décide que des comparaisons de la garde S8, dont les graines sont d'une couche non décisive ; (c) il est inspectable : le manifeste inscrit les configurations jouées (clé « proposeur|dose »), la mère peut les comparer aux 22 couples ; (d) il arrête sur toute configuration double (aucun choix silencieux). Condition : que la v15 inscrive la règle (silence n° 1) et que la pièce de contrôle porte l'empreinte du programme (`ed91813a…`) et son chemin. Un code v7 ne serait justifié que si la mère veut le tri sous la table du verrou : ce n'est pas exigé par le texte.

## 7. Les dix silences
1. Configurations « aux réglages gelés » : **à la mère**, recommandation : accepter la proposition (22 couples, référence taille 1 / force 1) et l'inscrire en v15.
2. Une seule couche pour 6 bis et 7 : **juste** (étiquettes disjointes de l'étalonnage, de l'étape 4 et des décisives).
3. Tailles et valeurs non nommées (20 000 sources statistiques, 20 000 moyennes, taux 0,25, bras 1-3 à toutes les doses) : **juste**, à inscrire en v15.
4. Verrou exigé sur une couche non décisive : **à la mère** (règle de la mère de 18:08Z) ; juste, à dire en v15 que la pièce d'autorisation précède l'étape 6 bis.
5. Pièce de contrôle : **à la mère** ; la lecture est une recherche de sous-chaînes (le commit et l'empreinte n'importe où dans le fichier) : acceptable, mais la pièce doit nommer ces deux valeurs sans équivoque.
6. Commit du manifeste pris de l'autorisation : **juste**. Précision à inscrire : le manifeste inscrit aussi `texte_sha256`, `piece_d_autorisation_sha256` et l'heure (non nuls) bien que la couche soit non décisive, parce que le programme passe l'autorisation aux graines ; le texte les dit nuls « hors des couches décisives » ; `verifier_manifeste` accepte (tous inscrits), essai vert.
7. Ce que les étapes écrivent (dossier neuf, détail scellé ou arrêt scellé, manifeste) : **juste**.
8. Autres arrêts (strate vide, arrêt de la couche mécanique) sans manifeste : **à la mère**, recommandation : accepter, avec inventaire du dossier partiel (R11) ; un manifeste d'arrêt pour toute cause serait un ajout sans code v7 si voulu.
9. Lieu du programme (dossier à part, empreinte en v15 et dans la pièce de contrôle) : **juste**.
10. Les étapes 3, 5, 6 sans programme : **juste, hors mandat** ; à la mère, à signaler qu'aucun programme ne les enchaîne encore.

Remarque : en cas d'échec de S8, la cause écrite ne garde que le message de `garde_equivalence` (au plus trois comparaisons détaillées) ; le détail des comparaisons tenues n'est pas écrit. Acceptable à la lettre (l'arrêt est rapporté avec sa cause).

## 8. Écarts à mon mandat
Aucun refus de permission, de classifieur ni de garde. Les deux variables d'essai sont passées comme pour le code v6. Aucune liste de processus, aucune commande d'arrêt, aucune écriture dans le dépôt. Une lecture de fichiers du sous-dossier versé par chemin complet (sans commande de liste).

Signé : vérificateur, modèle S.
