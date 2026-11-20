# Rapport du développeur — programme qui enchaîne les étapes 3, 4, 5 et 6 du palier 0b — v1

**EN ATTENTE DU MOT DE LAZAR.** Pièce de travail (classe C). Rien n'est lancé en vrai ; aucune graine décisive ; rien n'est versé.

- Auteur : développeur, modèle O (le développeur du code v6). 2026-11-20.
- Mandat : `P0B/mandat-developpeur-programme-etapes-3-5-6-v1.md` (`59370f4ab1704cef5494e16f7dec1ea46ac972471414ba0f481c3c371ff9de5e`), vérifié par `sha256sum` ; `P0B` = `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`. Décision de la mère (18:26Z, transmise) : pas de code v7 pour le tri des configurations des étapes 6 bis et 7.
- Pièces qui font foi, vérifiées par `sha256sum` et contre leur compagnon :
  - v13 (`d9591d5b…`) ;
  - brouillon v15 (`P0B/brouillon-v15/…-v15.md`, `33b04ff46d20a55051236d385c38e5e8fd30e7b3d969bd5d46a54a13b62b842f`) ;
  - table du code v6 (`639335b9…`), contre laquelle `P0B/code-v6/` a été rejoué sans écart ;
  - vérification du code v6 (`a7d0b1bc…`) ;
  - modèles de forme : `lancer_etapes_8_et_9_v1.py` (`67052a4b…`) et `P0B/programme-6bis-7-v1/lancer_etapes_6bis_et_7_v1.py` (`ed91813a…`).

  Toutes les empreintes sont égales.
- Fichiers rendus (sous-dossier `programme-3-5-6-v1/` du bloc-notes, chacun avec son compagnon) :
  - `lancer_etapes_3_5_6_v1.py` (**`6fc6fa3f74a77baea02767fe0bab3c28aafd6cd686cc3d51585739f81d873ded`**) ;
  - `tests/test_lancer_etapes_3_5_6_v1.py` (`018060cf7b366e9c0ac15f2966fd706f71bee26be761d19a001204a036d73b6e`) ;
  - `essais-essai-1.log` ;
  - ce rapport ;
  - `table-empreintes-programme-3-5-6-v1.txt`.

## 0. Verdict

Le programme est écrit hors du paquet. Il n'appelle que des fonctions du code v6 :
- `graines.Autorisation` et `graines.verifier_scelle` ;
- `organisme.EtageOrganisme` ;
- `mondes.audit_du_generateur` ;
- `etapes.lancer_etape_4` ;
- `frequences.geler` et `frequences.lire_gelees` ;
- `etapes.etape_6`, qui appelle `etalonnage.geler_reglages` ;
- `tirages.ecrire_manifeste`.

Il ne réécrit aucun calcul ; **aucune fonction neuve n'est requise dans le paquet, donc pas d'arrêt pour un code v7.**

**L'étape 4 est jouée, entre 3 et 5.** Le texte la place là (« 4. Couche mécanique : gardes de C6, fréquences M12, accord avec l'étage de l'organisme »), et l'étape 5 gèle ce qu'elle mesure. Elle passe par `lancer_etape_4`, que le texte nomme (B7 bis, « Version 12 »).

**Essais : 22 passés, 0 échoué** (804 s), sous la seule couche « essai-de-forme » : 21 essais du programme, plus l'essai final « aucune graine décisive » du code v6.

Aucun refus de permission, de classifieur ni de garde.

## 1. Ce que le texte exige, et comment le programme le fait

Le texte fixe l'ordre des opérations aux étapes 3 à 6 (v13:387 ; v15:395). Le tableau ci-dessous dit, exigence par exigence, où et comment `lancer_etapes_3_5_6_v1.py` la tient.

| exigence (citation) | lieu | programme (`lancer_etapes_3_5_6_v1.py`) |
|---|---|---|
| « 3. Audit du générateur (B1 : marges sur chaque monde ; présentation sur 50 suites par dose de la couche « audit ») » | v13:387 ; v15:395 | l. 149-159 : `MO.audit_du_generateur(g3, K.DOSES, 50, 1 000, "audit")`, avec trois doses, 50 suites par dose (`SUITES_AUDIT_PAR_DOSE`) et 1 000 permutations (`PERMUTATIONS_AUDIT`) ; les générateurs des plis et des permutations sont dérivés par le code v6 lui-même ; le rapport est écrit et scellé |
| liste d'arrêt, point 2 : l'audit échoue, ou les bornes de la construction sont épuisées → « arrêt » | v13:425 ; v15:433 | l. 156-157 et 115-122 : `ArretGenerateur` ; la cause et le rapport joint sont écrits et scellés, le manifeste porte l'issue « arrêt », puis la chaîne s'arrête |
| « 4. Couche mécanique : gardes de C6, fréquences M12, accord avec l'étage de l'organisme » ; B2 : « 24 sources par dose et par proposeur », réglages de l'étape 4 au milieu des plages, « sous-ensemble (deux sources par dose et par proposeur) » passé à l'étage de l'organisme ; jeu de la garde 27 | v13:387, 244, 308 ; v15:395, 252 | l. 161-176 : `EP.lancer_etape_4(g4, "mecanique", …, organisme=…)`, aux valeurs gelées par défaut, garde 27 comprise ; l. 141-144 : la copie de l'organisme est vérifiée (`EtageOrganisme`, garde 17) avant toute étape |
| S8 (i), garde 17 (« désaccord détecté ») : arrêts de l'étape 4 | v13:217, 358, 427 | dans `etape_4` (code v6) ; l. 170-171 : arrêts nommés de l'étape 4 écrits, scellés, chaîne arrêtée |
| « 5. Gel par programme du fichier des fréquences » | v13:387 ; v15:395 | l. 178-191 : `FR.geler` (fichier et compagnon), puis relecture par `FR.lire_gelees` sous contrôle de l'empreinte ; une relecture fausse est un arrêt écrit |
| « 6. Étalonnage des réglages (B7) et gel de leur fichier » ; B7 : « sur 200 000 sources d'étalonnage » ; arrêts de l'étalonnage (40 pas, note D8) ; « écrits dans un fichier scellé » | v13:387, 298 ; v15:395, 306 | l. 193-204 : `EP.etape_6(g6, "etalonnage", f, 200 000, chemin, conf)`, sur les fréquences relues et contrôlées ; le gel se fait par `etalonnage.geler_reglages` ; les arrêts (`ArretEtapes`, `ArretEtalonnage`, `ArretFrequences`) sont écrits |
| étiquettes disjointes entre étalonnage, couche mécanique, audit et couches décisives (B8) | v13:332 | l. 49 : couches « audit », « mecanique », « etalonnage » ; racine gelée `K.RACINE_GRAINES` |
| règle de la mère (18:08Z, remarque 9 de la v15) : aucune étape 3 à 9 avant le GO sur le texte qui suit la v13, au seul commit du code v6, inscrit à la pièce de contrôle | v15:1093 | l. 73-86 et 140 : verrou du code v6 exigé, puis pièce de contrôle de la mère, scellée, qui doit porter le commit et l'empreinte du programme |
| « Un manifeste par run » (R9) ; liste d'arrêt, point 10 (règle R11) ; « rien n'est supprimé » | v13:332, 433, 504 | l. 109-113 : un manifeste par étape ; l. 137-138 : dossier neuf exigé ; écritures exclusives |

## 2. Essais (pytest)

Commande :

```
env -C <bloc-notes>/dev-palier-0b-v6/code-v6 PYTHONPATH=src HERITAGE_DEPOT=/home/user/controle-ia-travail HERITAGE_COPIE_ORGANISME=<bloc-notes>/dev-palier-0b-v6/code-organisme-94bfd92/orchestrator /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider <bloc-notes>/dev-palier-0b-v6/programme-3-5-6-v1/tests/test_lancer_etapes_3_5_6_v1.py <bloc-notes>/dev-palier-0b-v6/code-v6/tests/test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py
```

Le code lancé est la copie du code v6 du bloc-notes, égale à la table `639335b9…`. Résultat : **22 passés, 0 échoué** (804 s ; journal `essais-essai-1.log`).

| garde | cas sain | artefact | essai |
|---|---|---|---|
| chaîne entière | étapes 3, 4, 5 et 6, réduites (4 suites par dose et 20 permutations ; lecteur réglé pour l'héritage et copieur à la dose 0,5, une source, garde 17 jouée sur elle, jeu de la garde 27 ; 2 000 sources d'étalonnage), sous « essai-de-forme ». Chaque étape a son manifeste scellé et vérifié (commit, empreinte du programme, issue « tenue ») ; rapport de l'audit et résultat de l'étape 4 scellés ; fréquences gelées, relues et inscrites aux étapes 5 et 6 ; réglages gelés ; étiquettes de la seule couche d'essai, dans l'ordre des étapes | — | `test_chaine_entiere_reduite_sous_essai_de_forme` |
| pièces | (chaîne) | pièce d'autorisation absente ; pièce de contrôle absente, non scellée, sans empreinte du programme, sans commit : refus, aucun dossier, aucune graine (5 essais) | `test_pieces_absentes_ou_incompletes` |
| couche | « essai-de-forme » (chaîne) | « audit », « mecanique », « etalonnage », « decisif », « confirmation », « essai », inconnue, donnés par l'appelant : arrêt avant tout geste (7 essais) | `test_couche_interdite` |
| tailles | — | taille réduite sous les couches des étapes ; paramètre inconnu : arrêt avant tout geste | `test_tailles_reduites_et_parametres_inconnus_refuses` |
| dossier | dossier neuf (chaîne) | dossier déjà présent : arrêt, dossier intact | `test_dossier_deja_present` |
| copie de l'organisme | copie vérifiée (chaîne) | copie absente ; fichier altéré : `OrganismeIndisponible` avant toute étape, aucun dossier | `test_copie_de_l_organisme_absente_ou_alteree` |
| arrêt de l'étape 3 | audit tenu (chaîne) | arrêt planté, rapport joint : cause et rapport scellés, manifeste « arrêt », étapes 4 à 6 non jouées | `test_arret_de_l_etape_3_ecrit_scelle_puis_chaine_arretee` |
| empreinte d'un gelé fausse | fréquences relues (chaîne) | fichier des fréquences altéré après son gel (planté) : arrêt de l'étape 5 écrit, étape 6 non jouée | `test_frequences_alterees_apres_gel_arretent_l_etape_5` |
| arrêt de l'étape 6 | étalonnage tenu (chaîne) | « non convergé » planté : arrêt écrit, manifeste « arrêt » avec les fréquences vérifiées, aucun réglage gelé | `test_arret_de_l_etape_6_ecrit_scelle` |
| ligne de commande | — | racine factice sans pièces : refus du verrou, code non nul, aucun dossier ; nombre d'arguments faux : usage | `test_ligne_de_commande_refusee_sur_racine_factice_sans_pieces` |
| aucune graine décisive | seule la couche « essai-de-forme » est dérivée ; tout refus consigné est décisif | — | `test_zz_aucune_graine_decisive_ni_d_autre_couche`, puis l'essai final du code v6 |

Les arrêts d'étape (3, 5, 6) sont plantés en remplaçant, le temps d'un essai, une fonction du code v6. Ils ne sont pas tirés. L'arrêt de l'étape 4 (S8 (i), garde 17) n'a pas d'essai à lui : il prend le même chemin d'écriture que les autres (l. 115-122), et ses gardes ont leurs essais dans le code v6. Aucun banc de défauts n'est demandé par le mandat.

## 3. Silences (ce que la lettre ne fixe pas ; propositions marquées, rien n'est tranché)

1. **Un programme pour quatre étapes, un manifeste par étape.** « Un manifeste par run » ne dit pas si une étape est un run. *Proposition* :
   - un seul lancement enchaîne les étapes 3, 4, 5 et 6, chacune dans son dossier (`etape-3/` à `etape-6/`) avec son manifeste et ses propres étiquettes ;
   - l'étape 5 ne dérive aucune graine, et son manifeste a une liste d'étiquettes vide ;
   - un arrêt d'une étape arrête la chaîne : les étapes suivantes ne se jouent pas.
2. **La garde 17 toujours jouée.** Le texte permet de ne pas la jouer si le code de l'organisme n'est pas disponible (C6 « non établi », issue « suspendue »). *Proposition* :
   - le programme exige la copie, vérifiée par `EtageOrganisme` avant toute étape, et n'offre pas le chemin « non jouée » ;
   - si ce chemin est voulu, il faudrait un programme v2.
3. **La racine et la tâche de l'organisme.**
   - racine : `graines.e(couche="mecanique", famille="organisme", role="racine")` ;
   - tâche : `palier-0b|etape-4` (l. 53).

   *Proposition* : les inscrire.
4. **Ce que les étapes écrivent.** *Proposition* :
   - étape 3 : `rapport-audit-du-generateur.json` scellé, ou `arret.txt` et `rapport-joint-a-l-arret.json` ;
   - étape 4 : `couche-mecanique/` (fichiers du code v6), puis `resultat-etape-4.json` scellé (fréquences, comptes, garde 17, résumé du jeu de la garde 27) ;
   - étape 5 : `frequences-m12-v1.json` (`frequences.geler`), configuration `{manifeste de l'étape 4, couche de l'étape 4}` ;
   - étape 6 : `reglages-v1.json` (`etapes.etape_6`), configuration `{sources, empreinte des fréquences, manifeste de l'étape 5}` ;
   - à chaque étape, `manifeste.json` et sa liste d'étiquettes.
5. **Où vivent les sorties.** L'annexe C propose `runs/heritage-palier-0b-v1/` et `diag/heritage-palier-0b-v1/` (v13:496) ; le programme écrit tout sous un dossier neuf donné par l'appelant. *Proposition* : `<racine>/diag/heritage-palier-0b-v1/etapes-3-a-6/`, fixé dans la pièce de contrôle.
6. **Les arrêts écrits.** Chaque étape a sa liste d'arrêts nommés (l. 57-60) ; toute autre exception se propage sans manifeste et laisse un dossier partiel, à inventorier (R11). *Proposition* : le dire.
7. **Le verrou et la pièce de contrôle, avant l'étape 3.** Comme pour le programme des étapes 6 bis et 7 : verrou du code v6 exigé sur des couches non décisives (règle de la mère) ; la pièce de contrôle, au même chemin, doit être scellée et porter le commit et l'empreinte de ce programme ; la pièce d'autorisation et la pièce de contrôle sont donc écrites avant l'étape 3. *Proposition* : l'inscrire.
8. **Le commit du manifeste** est pris de l'autorisation, non de l'appelant.
9. **Le lieu du programme.** *Proposition* : son propre dossier, `P0B/programme-3-5-6-v1/`, son empreinte inscrite à la pièce de contrôle et au texte.
10. **L'enchaînement entier.** Ce programme rend les chemins et empreintes des fréquences et des réglages gelés ; le programme des étapes 6 bis et 7 les reçoit en arguments. *Proposition* : la pièce de contrôle les inscrit entre les deux lancements.

## 4. Commande exacte de lancement (NON LANCÉE, en attente)

```
env -C <RACINE>/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6 PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B <CHEMIN>/lancer_etapes_3_5_6_v1.py <TEXTE> <RACINE> <COPIE_DE_L_ORGANISME>/orchestrator <DOSSIER_NEUF>
```

- `<TEXTE>`, `<RACINE>` et `<DOSSIER_NEUF>` : ceux de la pièce de contrôle de la mère.
- `<COPIE_DE_L_ORGANISME>` : la copie au commit du palier 0a (`docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92`).
- Sortie standard : l'empreinte du manifeste de chaque étape, puis les chemins et empreintes des fréquences et des réglages gelés, que reçoit le programme des étapes 6 bis et 7.
- En cas d'arrêt : un code non nul et sa cause.

Ordre : ce programme, puis celui des étapes 6 bis et 7, puis celui des étapes 8 et 9.

## 5. Ce que la v15 (ou le texte suivant) ou la pièce de contrôle de la mère devra porter

- **L'empreinte du programme** : `6fc6fa3f74a77baea02767fe0bab3c28aafd6cd686cc3d51585739f81d873ded`, et son chemin une fois versé ; la pièce de contrôle doit porter cette empreinte et le commit du code v6.
- Les silences n° 1 à 10.
- La commande du § 4, avec ses valeurs.
- L'ordre des trois programmes.

## 6. Gestes, écarts

- Une commande simple par appel ; aucun heredoc, aucun code en ligne.
- Aucune commande de liste ni de recherche de processus ; aucune commande d'arrêt.
- Jouées seulement : les essais ci-dessus, sous la couche « essai-de-forme », sur une racine factice (dossiers temporaires de pytest), avec la copie du code de l'organisme du bloc-notes, lue sans écriture. L'essai de la ligne de commande s'arrête au refus du verrou.
- Aucune graine décisive, ni de couche « audit », « mecanique » ou « etalonnage » ; aucun audit, aucune couche mécanique ni aucun étalonnage réels.
- Aucune pièce d'autorisation réelle ; aucun appel à un fournisseur ; aucune dépense ; aucune écriture dans le dépôt ; aucun commit.
- Écart : les deux variables d'environnement des essais, comme pour le code v6.

Développeur, modèle O.
