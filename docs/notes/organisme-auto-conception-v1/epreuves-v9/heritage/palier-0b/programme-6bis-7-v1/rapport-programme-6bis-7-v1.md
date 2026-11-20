# Rapport du développeur — programme qui enchaîne les étapes 6 bis et 7 du palier 0b — v1

**EN ATTENTE DU MOT DE LAZAR.** Pièce de travail (classe C). Rien n'est lancé en vrai ; aucune graine décisive ; rien n'est versé.

- Auteur : développeur, modèle O (le développeur du code v6). 2026-11-20 (`date -u` : 18:24Z à l'écriture).
- Mandat : `P0B/mandat-developpeur-programme-etapes-6bis-7-v1.md` (`dd30e127399d2fbcb7e4093bfd1337e7c56734f0e2d89ad4f0c29ab5fea7c300`), vérifié par `sha256sum` ; `P0B` = `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.
- Pièces qui font foi, vérifiées par `sha256sum` et contre leur compagnon : v13 (`d9591d5b…`), brouillon v14 (`P0B/brouillon-v14/…-v14.md`, `840400f3968095934c93b91fb6e3f8c8001953541b4df4f5546da4953af9ae4a`), table du code v6 (`639335b95b46b8f1d2258ba84fdf117bd4061df6cd5b0bf1b3dca85549c62fa3` ; `P0B/code-v6/` rejoué contre elle : aucun écart), vérification du code v6 (`a7d0b1bc…`), modèle de forme `P0B/code-v6/outils-dev/lancer_etapes_8_et_9_v1.py` (`67052a4b…`). Tous égaux.
- Fichiers rendus (sous-dossier `programme-6bis-7-v1/` du bloc-notes, chacun avec son compagnon) : `lancer_etapes_6bis_et_7_v1.py` (**`ed91813a88c9f58e65dd21d5e7a15fd6d4f2ae810787eb57bf57e7caceeb71d0`**) ; `tests/test_lancer_etapes_6bis_et_7_v1.py` (`69aa2ad4241bc1bb3531f5a1e74145e3679038d391467ca5cab9f530903a25b8`) ; `essais-v1.log` ; ce rapport ; `table-empreintes-programme-6bis-7-v1.txt`.

## 0. Verdict

Le programme est écrit, hors du paquet, et n'appelle que des fonctions du code v6 : `graines.Autorisation`, `graines.verifier_scelle`, `etapes.relire_fichiers_geles`, `etapes.plan_des_cases`, `etapes.reglages_pour_le_plan`, `etapes.etape_6_bis_et_7` (qui appelle la couche mécanique, la couche statistique et `equivalence.garde_equivalence`) et `tirages.ecrire_manifeste`. Il ne réécrit aucun calcul. **Aucune fonction neuve n'est requise dans le paquet ; il n'y a donc pas d'arrêt pour un code v7.** Une réserve est portée au vérificateur : le programme choisit, entre les réglages gelés, les configurations que reçoit `etape_6_bis_et_7`. C'est un tri des cases du plan, non un calcul. Mais la règle de ce tri n'est écrite par aucun texte (silence n° 1, proposition marquée) et elle vit hors de la table que contrôle le verrou. Si la mère ou le vérificateur jugent qu'elle doit être sous le verrou, il faut un code v7. **Essais : 21 passés, 0 échoué** (7,2 s), sous la seule couche « essai-de-forme » : les 20 essais du programme et l'essai final du code v6, « aucune graine décisive ». Aucun refus de permission, de classifieur ni de garde.

## 1. Ce que le texte exige, et comment le programme le fait

| exigence (citation) | lieu du texte | programme (`lancer_etapes_6bis_et_7_v1.py`) |
|---|---|---|
| « 6 bis. Couche mécanique rejouée aux réglages gelés, sous des étiquettes de graines disjointes, pour la garde d'équivalence. 7. Garde d'équivalence S8. » | v13:387 ; v14:395 | l. 140 : `EP.etape_6_bis_et_7(...)` (code v6, `etapes.py:230`) rejoue la couche mécanique (famille « etape-6-bis »), puis la couche statistique (famille « etape-7 »), puis applique S8 (ii) |
| « l'étalonnage, la couche mécanique, sa reprise aux réglages gelés, […] ont des étiquettes disjointes » | v13:332 ; v14:340 | l. 44 : couche « mecanique-reglages », la couche que `graines.py` (code v6, l. 6) nomme pour l'étape 6 bis ; l. 132 : racine des graines `K.RACINE_GRAINES` (2026111902) |
| S8 (ii) : « Pour chaque proposeur, chaque bras et chaque dose, la moyenne de M1 sur les sources de la couche mécanique tombe dans l'intervalle de prédiction à 99,9 % […] ; sinon, arrêt » ; « la soixantaine de comparaisons » | v13:217 ; v14:225 | l. 79-97 : configurations (silence n° 1) ; l. 140 : la garde du code v6 ; l. 141-149 et 156-157 : un arrêt est écrit, scellé, puis le programme s'arrête |
| « Taille gelée : 24 sources par dose et par proposeur » (couche mécanique) | v13:244 (B2) | défaut de `etape_6_bis_et_7` (`SOURCES_COUCHE_MECANIQUE` = 24) ; l. 119-121 : aucune taille réduite sous la couche des étapes |
| « La garde d'équivalence S8 ne porte que sur les trois bras du critère » | v13:310 | défaut de `etape_6_bis_et_7` : bras 1, 2, 3 |
| liste d'arrêt, point 1 : aucun tirage sans erratum contre-lu et texte scellé ; règle de la mère (18:08Z) : aucune étape 3 à 9 avant le GO sur le texte qui suit la v13, et seulement au commit du code v6 | v13:424 ; mandat | l. 62-76 et 124 : verrou du code v6 exigé (texte présenté scellé, pièce d'autorisation, GO inscrit, commit et empreinte du texte, modules conformes à la table du texte), puis la pièce de contrôle de la mère, qui doit porter le commit et l'empreinte du programme (silence n° 5) |
| fichiers gelés des étapes 5 et 6, relus sous contrôle (règle R11 ; liste d'arrêt, point 10) | v13:387, v13:433 | l. 125 : `EP.relire_fichiers_geles` (contrôle sur disque, empreinte attendue, compagnon) |
| liste d'arrêt, point 4 : « les deux couches ne s'accordent pas […] arrêt ; retour au rédacteur ; aucun tirage décisif » | v13:427 | l. 141-157 : la cause est écrite (`arret-garde-equivalence-s8.txt`, scellé) avec le manifeste, issue « arrêt », puis le programme s'arrête (`ArretProgramme`, code non nul) |
| « Un manifeste par run » (règle R9) ; liste d'arrêt, point 8 : « un manifeste absent » rend la lecture invalide | v13:332, v13:431 | l. 150-154 : `TI.ecrire_manifeste` (configuration et son empreinte, versions, racine, étiquettes et leur fichier, commit, fichiers gelés vérifiés, champs du verrou) ; configuration : étapes, couche, empreinte du programme, configurations, tailles, issue |
| « Rien n'est supprimé par un programme avant inventaire » ; « jamais d'écrasement » | v13:504 | l. 122-123 : un dossier déjà présent arrête ; écritures en mode exclusif (`_ecrire_scelle`, l. 100-108 ; fonctions du code v6) |

## 2. Essais (pytest)

Commande : `env -C <bloc-notes>/dev-palier-0b-v6/code-v6 PYTHONPATH=src HERITAGE_DEPOT=/home/user/controle-ia-travail HERITAGE_COPIE_ORGANISME=<bloc-notes>/dev-palier-0b-v6/code-organisme-94bfd92/orchestrator /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider <bloc-notes>/dev-palier-0b-v6/programme-6bis-7-v1/tests/test_lancer_etapes_6bis_et_7_v1.py <bloc-notes>/dev-palier-0b-v6/code-v6/tests/test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py`. Le code lancé est la copie du code v6 du bloc-notes, égale à la table `639335b9…`, contrôle refait. **21 passés, 0 échoué** (journal `essais-v1.log`).

| garde | cas sain | artefact | essai |
|---|---|---|---|
| configurations (proposition) | 22 couples, 66 comparaisons ; chaque couple à sa configuration de référence | une cible de référence non atteignable retire ses seuls couples | `test_configurations_aux_reglages_geles_proposition` |
| chaîne entière | racine et gelés factices, étapes 6 bis et 7 réduites (une source mécanique, 200 sources statistiques, couple sourd à appels égaux à la dose 0,25), sous « essai-de-forme » : détail scellé ; manifeste scellé et vérifié, qui porte le commit, les gelés vérifiés, l'empreinte du programme et l'issue « tenue » ; étiquettes de la seule couche « essai-de-forme » | — | `test_cas_sain_reduit_sous_essai_de_forme` |
| pièces | (cas sain ci-dessus) | pièce d'autorisation absente ; pièce de contrôle absente, non scellée, sans empreinte du programme, sans commit : refus, aucun dossier, aucune graine (5) | `test_pieces_absentes_ou_incompletes` |
| fichiers gelés | (cas sain ci-dessus) | empreinte des fréquences fausse ; empreinte des réglages fausse ; fichier absent : arrêt, aucun dossier | `test_empreinte_d_un_gele_fausse` |
| couche | « essai-de-forme » (cas sain) | « decisif », « confirmation », « essai », « mecanique », « etalonnage », « audit », inconnue : arrêt avant tout geste, aucune graine, aucun refus consigné, aucun dossier (7) | `test_couche_interdite` |
| tailles sous la couche des étapes | — (la couche des étapes n'est jamais jouée par les essais) | taille réduite ou sous-ensemble sous « mecanique-reglages » : arrêt avant tout geste | `test_tailles_reduites_refusees_sous_la_couche_des_etapes` |
| dossier | dossier neuf (cas sain) | dossier déjà présent : arrêt, dossier intact | `test_dossier_deja_present` |
| garde S8 en échec | garde tenue (cas sain) | arrêt planté dans `etape_6_bis_et_7` (non tiré) : cause écrite et scellée, manifeste « arrêt », arrêt du programme | `test_garde_s8_en_echec_ecrite_scellee_puis_arret` |
| ligne de commande | — | racine factice sans pièces : refus du verrou, code non nul, aucun dossier ; nombre d'arguments faux : usage | `test_ligne_de_commande_refusee_sur_racine_factice_sans_pieces` |
| aucune graine décisive | seule la couche « essai-de-forme » est dérivée ; les refus consignés sont tous décisifs | — | `test_zz_aucune_graine_decisive_ni_d_autre_couche`, puis `test_zz_aucune_graine_decisive_derivee` du code v6 |

Aucun banc de défauts n'a été écrit pour ce programme : le mandat ne le demande pas.

## 3. Silences (ce que la lettre ne fixe pas ; propositions marquées, rien n'est tranché)

1. **Les configurations « aux réglages gelés ».** Le texte ne dit ni quels proposeurs, ni quelles doses, ni quelle taille ou force (l'audit, § 2, et la remarque 8 du brouillon v14, v14:1092, le relevaient). *Proposition* (l. 79-97) : prendre chaque couple (proposeur, dose) que tire `plan_des_cases`, construit sur les réglages gelés, à sa configuration de référence — cases sans taille ni force, ou à la taille 1, ou à la force 1. Une configuration double pour un même couple arrête. Quand toutes les cibles sont atteignables, cela fait 22 couples, soit 66 comparaisons sur trois bras, la « soixantaine » de S8 :
   - neuf proposeurs ;
   - le lecteur réglé pour l'héritage à la dose nulle, avec le K de la dose 0,5, comme dans sa case de la famille C ;
   - aucun lecteur réglé pour la tenue à la dose nulle, faute de case.

   Une cible non atteignable retire ses couples. *Réserve* : cette règle vit hors du paquet ; la mettre dans le paquet ferait un code v7.
2. **Une seule couche pour 6 bis et 7.** `etape_6_bis_et_7` emploie la même couche pour la reprise mécanique, pour la couche statistique de la garde et pour le générateur de l'intervalle (familles « etape-6-bis » et « etape-7 », rôle « intervalle »). *Proposition* : « mecanique-reglages » pour les trois. Ces étiquettes sont disjointes de l'étalonnage, de l'étape 4 (« mecanique ») et des couches décisives.
3. **Tailles et valeurs du code v6 que le texte ne nomme pas.**
   - 20 000 sources statistiques (défaut de `etape_6_bis_et_7`, aucune constante) et 20 000 moyennes pour l'intervalle (`MOYENNES_DE_PREDICTION_S8`, silence du code) ;
   - taux d'échec de 0,25 ;
   - règle de retrait de la version 2 et repère principal ;
   - bras 1, 2 et 3 à toutes les doses, bras 1 compris à la dose nulle, où les familles décisives ne jouent que les bras 2 et 3.

   *Proposition* : les inscrire en v15.
4. **Le verrou sur une couche non décisive.** Le code v6 ne verrouille pas les couches non décisives (silence n° 16). Le programme exige pourtant l'autorisation du verrou, comme le veut la règle de la mère de 18:08Z. La pièce d'autorisation (écrite après le GO) doit donc exister avant l'étape 6 bis. *Proposition* : la v15 le dit ; la pièce d'autorisation et la pièce de contrôle sont écrites avant l'étape 3, non seulement avant l'étape 8.
5. **La pièce de contrôle de la mère pour ces étapes.** Sa forme n'est fixée par aucun texte (une table, point par point). Il faut aussi qu'elle existe avant 6 bis : le texte la dit écrite « avant le lancement des étapes 8 et 9 ». *Proposition* :
   - même chemin (v13:994 ; v14:1007) ;
   - le programme exige seulement qu'elle soit scellée et qu'elle porte deux chaînes : le commit du code (celui de la pièce d'autorisation) et l'empreinte de ce programme (l. 62-76).
6. **Le commit du manifeste.** Il est pris de l'autorisation (`autorisation.commit`, l. 154), non de l'appelant. Pour ce programme, cela ferme le silence n° 8 (contrôle manuel par la mère). *Proposition* : le dire.
7. **Ce que les étapes écrivent.** Le texte ne fixe ni le contenu ni les noms. *Proposition* : dans un dossier neuf, on trouve :
   - la couche mécanique rejouée (`couche-mecanique/`, fichiers de la couche mécanique du code v6) ;
   - le détail de la garde (`garde-equivalence-s8.json` : par clé « proposeur|bras|dose », la moyenne mécanique, le nombre de sources, l'intervalle et la moyenne statistique), scellé ;
   - à sa place, en cas d'arrêt : `arret-garde-equivalence-s8.txt`, scellé ;
   - le manifeste et sa liste d'étiquettes, scellés.
8. **Les autres arrêts.** Une strate vide (`ArretFrequences`) ou un arrêt de la couche mécanique, en cours de route, se propage sans manifeste ; le dossier partiel reste à inventorier (règle R11 ; liste d'arrêt, points 10 et 11). *Proposition* : le dire, ou demander un manifeste d'arrêt pour toute cause.
9. **Où vit le programme.** Hors du paquet. Dans `P0B/code-v6/outils-dev/`, il changerait la table du code v6 (sans toucher le verrou, qui ne contrôle que `src/`). *Proposition* : le verser dans son propre dossier (`P0B/programme-6bis-7-v1/`), son empreinte inscrite en v15 et dans la pièce de contrôle.
10. **Les étapes 3 à 6.** Ce programme ne les enchaîne pas. Hors de `lancer_etape_4`, il n'existe toujours aucun programme pour l'étape 3 (audit), l'étape 5 (gel des fréquences, `frequences.geler`) ni l'étape 6 (`etapes.etape_6` et `etalonnage.geler_reglages`) ; les fichiers gelés que ce programme lit en sont les produits. Hors du mandat ; dit.

## 4. Commande exacte de lancement (NON LANCÉE, en attente)

Dossier courant : le code v6 de l'arbre lancé ; `PYTHONPATH=src` seul ; interpréteur du dépôt, `-B` :

```
env -C <RACINE>/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6 PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B <CHEMIN>/lancer_etapes_6bis_et_7_v1.py <TEXTE> <RACINE> <FICHIER_DES_FREQUENCES> <EMPREINTE_DES_FREQUENCES> <FICHIER_DES_REGLAGES> <EMPREINTE_DES_REGLAGES> <DOSSIER_NEUF>
```

Les valeurs entre chevrons sont celles de la pièce de contrôle de la mère : `<TEXTE>` et `<RACINE>` (silence n° 14), les fichiers gelés des étapes 5 et 6 et leurs empreintes, un dossier neuf, et `<CHEMIN>`, le dossier où le programme est versé. Sortie standard : le chemin et l'empreinte du manifeste, le nombre de comparaisons, « garde tenue » ; en cas d'arrêt, un code non nul et sa cause.

## 5. Ce que la v15 ou la pièce de contrôle de la mère devra porter

- **L'empreinte du programme** : `ed91813a88c9f58e65dd21d5e7a15fd6d4f2ae810787eb57bf57e7caceeb71d0`, et son chemin une fois versé. Le programme exige que la pièce de contrôle porte cette empreinte et le commit du code v6.
- La règle des configurations (silence n° 1), la couche (n° 2), les tailles et valeurs (n° 3), le moment des pièces (n° 4 et 5), les sorties (n° 7), les autres arrêts (n° 8), le lieu du programme (n° 9).
- La commande du § 4, avec les valeurs de l'arbre lancé ; l'ordre : étapes 3, 4, 5, 6, puis ce programme, puis les étapes 8 et 9.

## 6. Gestes, écarts

- Une commande simple par appel ; aucun heredoc, aucun code en ligne ; aucune commande de liste ni de recherche de processus ; aucune commande d'arrêt.
- Jouées seulement : les essais ci-dessus, sous la couche « essai-de-forme », sur racine et gelés factices (dossiers temporaires de pytest). Les essais de la ligne de commande s'arrêtent au refus du verrou, avant toute dérivation.
- Aucune graine décisive ; aucun étalonnage réel ; aucune pièce d'autorisation réelle ; aucun appel à un fournisseur ; aucune dépense ; aucune écriture dans le dépôt ; aucun commit ; rien sous `archives-reponses-modeles/` ni `/root/.claude/`.
- Écart : comme pour le code v6, les deux variables d'environnement des essais. L'essai final du code v6 est joué dans le même processus, après ceux du programme.

Développeur, modèle O.
