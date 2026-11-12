# Contre-lecture différentielle (R2) de l'addendum 4 au préenregistrement du témoin de Bailey — version à sceller — v1

Contre-lecteur neuf, sous-agent lancé par la session `session_01XJ6MgnEhQMZteN9F8a1BST` ; n'a écrit aucun des fichiers lus,
ni le premier rapport. 12 novembre 2026, vers 23:05 UTC. Cloisons tenues : ni `donnees/bras-attaque*`, ni
`donnees/mode-tenu-a-l-ecart*`, ni `docs/notes/bras-attaque/`, ni `docs/notes/programme-et-4-familles-evasion/`, ni
`registres/etat.md`, ni `registres/decisions.md`, ni aucun résultat ou seuil de sonde ou de moniteur ; aucune variable de
secrets, aucun fichier de clé, aucune commande réseau ; aucun fichier existant modifié (essais avec `-p no:cacheprovider`
et `PYTHONDONTWRITEBYTECODE=1` ; `git status` propre avant l'écriture de ce rapport). Les données manipulées par les essais
n'ont pas été lues ; seuls les noms d'essais et les lignes d'échec courtes (`--tb=line`) l'ont été.

Pièces lues :
- brouillon 2 : `brouillons/temoin-attaque-publiee-bailey-v1-addendum-4-code-v17-execution-v4-brouillon2.md`
  (`d49ed4ef4e7115dce30460020dab263847d2f38a89e8b9bf821a12f25cc20851`) ;
- version à sceller : `prereg/temoin-attaque-publiee-bailey-v1-addendum-4-code-v17-execution-v4-troisieme-serie.md`
  (`abd681085e8492996a492166a0cde179cad794701f9743712760871660f30cb2`, commit `92404761`, non scellée) ;
- premier rapport : `docs/notes/reproduction-attaque-publiee-v1/contre-lecture-addendum-4-code-v17-bailey-v1.md`
  (`2db77cc7c7b5a6799e803ceede0ec889b33abe79e1d50b02fbd1cba71d065161`, égal à son compagnon) ;
- texte : `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`), conditions de lancement l. 376-390 ;
- addendum 3, § 6 et § 7 ; notes `registres/passations/2026-11-12-2210-…` (`cb16b95c…`) et
  `registres/passations/2026-11-12-2320-decision-lazar-bailey-autonomie-10h-mot-de-lancement.md`
  (`4f127118b67e1c2aa8dfd1e516f752a710dab7671f95be3dcea7a8f738bdd9a8`, égal à son compagnon) ;
- `src/controle_ia/temoin_bailey/lanceur_v17.py` (`CHEMINS_ARCHIVE`, l. 306-310), `lecture_v8.py` l. 428-432 ;
- en-têtes d'import des six fichiers d'essai cités ; sorties de la suite complète de la session (bloc-notes,
  `pytest_v17_complet.txt`, `pytest_v17_complet_v2.txt`, `collecte.txt` : noms d'essais seulement).

## Verdict

**Scellable après corrections.** Aucun bloquant. Le différentiel ne touche ni hypothèse, ni seuil, ni métrique, ni
population, ni juge, ni modèle, ni bras. Neuf constats K sur onze sont repris fidèlement ; K-5 l'est en partie (D-1, D-2,
D-3) ; K-3 n'est pas suivi, mais l'écart est déclaré (D-4 à D-7). À corriger : D-1, D-2, D-4. À préciser : D-3, D-5, D-6,
D-7.

Condition 7 : **déclaré et défendable**, à la condition de D-4 (borne des 10 heures) ; D-5 et D-6 rendent la déclaration
complète. La décision de tenir les deux mots pour le mot de lancement reste à Lazar.

## 1. Différentiel brouillon 2 → version à sceller, constat par constat

| Constat | Traitement | Fidèle ? |
|---|---|---|
| K-1 | § 2.2 l. 61-63 mot pour mot ; § 2.4 l. 69 et § 6 l. 163 : « v11, `poste-hetzner-v11.sh`, `059d0837…` » ; les « v10 » restants (l. 62, 112-113) nomment à bon droit les pièces jamais tournées | oui |
| K-2 | risque (b) l. 132-136, texte du rapport mot pour mot | oui |
| K-3 | non suivi : la condition 7 se dit remplie par une lecture de la session (deux mots de Lazar) au lieu de « à obtenir avant toute instance » ; l'écart est déclaré (l. 161-162) | non suivi, déclaré (D-4 à D-7) |
| K-4 | en-tête l. 9-11 et § 2.2 l. 53, 56-59, mot pour mot | oui |
| K-5 | compte du fichier v17 inscrit (168 passés, 1 sauté) ; échecs nommés ; mais l'affirmation sur l'archive est fausse, le compte par fichier ne se retrouve pas, le compte final de la suite est renvoyé à la passation | en partie (D-1, D-2, D-3) |
| K-6 | risque (e) l. 144-148, mot pour mot | oui |
| K-7 | § 2.2 l. 55-56, mot pour mot, plus « du § 5 » | oui |
| K-8 | § 6 l. 165-167, mot pour mot | oui |
| K-9 | l. 85 (contre-lecture du code ajoutée) ; l. 89-90 (accents graves, `6856b0b2…`, 13 lignes) ; l. 101 (`aeeab086…`, `100152d5…`) ; § 5 (c) l. 137-138 (OmegaConf 2.3.0 et 2.3.1) | oui |
| K-10 | en-tête l. 3-7 (empreintes des deux brouillons, égales aux fichiers, vérifiées ici) ; « non contre-lu, non scellé » retiré ; section « Contre-lecture » remplie | oui |
| K-11 | condition 8 l. 163-165 (« cet addendum scellé » pour « l'addendum 4 scellé ») | oui |

**Autres modifications.** Annoncées : condition 7 (message « avance en autonomie pendant 10h ») ; § 3 (résultats des
essais). Non annoncées, sans portée : titre sans « — brouillon 2 » ; « (R12) » retiré après « restent tels quels » à
l'en-tête ; « scellé après contre-lecture (R2) » à l'en-tête. Aucune modification de fond non annoncée.

## 2. Faits ajoutés au § 3 sur les essais

Vérifiés :
- fichier v17 : 168 passés, 1 sauté (premier rapport, rejoué par lui ; non rejoué ici) ;
- `test_temoin_bailey_analyse_v3.py` et `test_temoin_bailey_condition6_v16.py` : **197 passés** (rejoué ici, 164 s) ;
- 6 687 essais collectés (`collecte.txt` de la session : 6 687 identifiants) ;
- cinq des six fichiers en échec, rejoués ici (sans `test_hote_durable_a1_v3_v3.py`) : **7 échecs, 253 passés**, 321 s :
  `test_cibles_invisibles_v1.py` 2, `_v2.py` 1, `test_corpus_arxiv.py` 3 (`ModuleNotFoundError: pypandoc`,
  `corpus_arxiv.py` l. 374), `test_lanceur_durable_v5_a1v4.py` 1 (`DID NOT RAISE Refus`, l. 316),
  `test_noter_pilote_a.py` **0** (rejoué seul : 37 passés, 274 s) ;
- aucun des six fichiers n'importe `temoin_bailey` (`grep` des imports, y compris `importlib`).

Non vérifié : « aucun n'a rien poussé (vérifié par `git ls-remote`) » (commande réseau exclue ici).

### D-1 — à corriger — « aucun n'importe […] un module de l'archive envoyée sur l'instance » est faux (§ 3, l. 98)
Preuve : `CHEMINS_ARCHIVE` (`lanceur_v17.py` l. 306-310) contient `src/controle_ia/__init__.py`, `gardes.py`,
`scellement.py`. `test_corpus_arxiv.py` importe `controle_ia.gardes` (l. 15) et `controle_ia.scellement` (l. 166) ;
`test_noter_pilote_a.py` importe `controle_ia.gardes` (l. 16, 20) et `controle_ia.scellement` (l. 22) ; les six importent
le paquet `controle_ia` (`__init__.py`, vide). De plus, l'échec de
`test_cibles_invisibles_v2.py::test_inventaire_tout_constructeur_d_invite_est_examine` **nomme**
`controle_ia/temoin_bailey/lecture_v5.py` à `lecture_v8.py::_interruption` (`lecture_v8` est dans l'archive) : c'est un
inventaire statique (arbre syntaxique) d'un autre chantier, qui relève tout dictionnaire à clé `"role"` ; `_interruption`
(`lecture_v8.py` l. 428-432) bâtit un dictionnaire de rôle d'exécution (pilote ou run principal), pas une invite. Faux
positif, présent depuis `lecture_v5`, non introduit par la v17 ; aucun échec ne vient de `gardes` ni de `scellement`. Le
fond (aucun échec n'atteint le code du témoin) tient ; la phrase, non, et K-5 demandait « s'il touche ».
Correction, remplacer « aucun n'importe un module de `src/controle_ia/temoin_bailey/` ni un module de l'archive envoyée
sur l'instance » par : « aucun échec ne vient d'un module de `src/controle_ia/temoin_bailey/` ni d'un module de l'archive
envoyée sur l'instance : `test_corpus_arxiv.py` et `test_noter_pilote_a.py` importent `controle_ia.gardes` et
`controle_ia.scellement` (archive), mais les échecs du premier viennent de `pypandoc`, absent du `.venv`
(`corpus_arxiv.py` l. 374), et celui du second n'est pas reproduit ; l'échec de
`test_cibles_invisibles_v2.py::test_inventaire_tout_constructeur_d_invite_est_examine` nomme
`temoin_bailey/lecture_v5.py` à `lecture_v8.py::_interruption` : inventaire statique d'un autre chantier, qui relève tout
dictionnaire à clé `role` ; ces fonctions bâtissent le rôle d'exécution (pilote ou run principal) et ne construisent
aucune invite ; présent depuis `lecture_v5`, non introduit par la v17 ».

### D-2 — à corriger — comptes de la première passe et par fichier (§ 3, l. 98)
Preuve : `pytest_v17_complet.txt` (1 692 essais joués, arrêt vers 24 %) porte **24** `F`, non 23. Rangés dans l'ordre de
`collecte.txt` : `cibles_invisibles_v1` 2, `_v2` 1, `corpus_arxiv` 3, `hote_durable_a1_v3_v3` **16**, `lanceur_durable_v5_a1v4`
1, `noter_pilote_a` 1 (`test_rejeu_identique_et_r12`). La seconde passe (`pytest_v17_complet_v2.txt`, vers 30 % à 23:01Z)
porte les mêmes échecs sauf celui de `noter_pilote_a`, passé ; rejoué seul ici, ce fichier passe entier (37 sur 37).
Les six fichiers comptent 356 essais (21 + 21 + 43 + 96 + 138 + 37) ; « 23 échecs, 333 passés » rejoués seuls s'accorde
avec 16 échecs dans `hote_durable` et 0 dans `noter_pilote_a`, non avec « 15 » et « 1 ». `test_hote_durable_a1_v3_v3.py`
n'a pas été rejoué ici (consigne) : le 16 repose sur l'ordre de collecte ; l'auteur le confirme sur sa sortie seule.
Correction : « une première passe, arrêtée vers 24 % (1 692 essais joués), a montré 24 échecs, tous dans six fichiers
d'autres chantiers : `test_cibles_invisibles_v1.py` (2) et `_v2.py` (1), `test_corpus_arxiv.py` (3, module `pypandoc`
absent du `.venv`), `test_hote_durable_a1_v3_v3.py` (16 : interpréteur Python 3.13 exigé, branches et GO d'un autre
chantier), `test_lanceur_durable_v5_a1v4.py` (1), `test_noter_pilote_a.py` (1, `test_rejeu_identique_et_r12`, non
reproduit : passé seul, 37 sur 37, et à la seconde passe) ; rejoués seuls : 23 échecs, 333 passés ».

### D-3 — à préciser — compte final de la suite renvoyé à la passation (§ 3, l. 98)
Preuve : K-5 demandait « N passés, M sautés, E échecs » avant le scellement ; le texte renvoie la seconde passe à la
passation. Acceptable, puisque tous les échecs sont hors du code du témoin (D-1), à condition de dire ce qu'on sait.
Correction : « Une seconde passe complète tournait au scellement (vers 30 % : les mêmes échecs, `test_noter_pilote_a.py`
passé) ; son compte final est inscrit dans la passation, hors de ce texte. »

## 3. Condition 7

**Ce que dit le texte.** « 7. le mot direct de Lazar pour le lancement », parmi les conditions « toutes requises avant la
création de l'instance » (l. 376, 388). Le texte ne fixe pas la forme du mot.

**Ce que fait la version à sceller (l. 156-162).** Elle cite les deux mots verbatim, dit que le § 7.3 de l'addendum 3 ne
valait que pour sa série, dit que tenir les deux mots ensemble pour mot de lancement « est une lecture de la session,
déclarée ici », et que la contre-lecture recommandait un mot exprès. Elle ne présente pas cette lecture comme un mot
exprès de Lazar. La note `2320` (l. 8-12) dit de même et borne la lecture : aucune dépense hors de `GO-2026-11-10-10`,
aucune autre série, aucune décision de nœud.

**Pourquoi défendable.** Les deux mots sont directs, écrits, verbatim. Le « go (a) » approuve une option dont la dernière
étape est nommément « nouvelle série » ; le message « avance en autonomie pendant 10h » est postérieur et lève l'attente.
La dépense reste couverte par un GO sur devis (B = 75 USD). Le § 7.3 de l'addendum 3 montre que Lazar, interrogé, a déjà
tenu un « go (a) » nommant une série pour mot de lancement (bien que la session y recommandait un mot exprès).

**Limites.** Lazar n'a pas été interrogé cette fois ; « autonomie » est un mot général, borné dans le temps ; la lecture
n'apparaît qu'après K-3 (D-6). D'où « déclaré et défendable », sous D-4.

### D-4 — à corriger — la borne des 10 heures n'est pas portée par le texte (§ 6, condition 7)
Preuve : le message vaut « pendant 10h » à partir de ≈ 22:14Z, soit jusqu'au 13 novembre ≈ 08:14Z. Après le pilote, le
run principal se lance par la règle (texte, l. 377) : seule compte l'heure de création de l'instance du pilote. Le texte
ne dit pas ce qui se passe si la création est plus tardive (retard du dépôt, de l'offre, d'un poste). La note `2320` n'est
pas citée avec son empreinte (R6).
Correction, ajouter à la fin de la condition 7 : « Cette lecture ne vaut que pour une création d'instance avant le
13 novembre 2026, 08:14Z (fin des 10 heures) ; au-delà, la condition 7 est à obtenir de nouveau. Elle reste dans les
bornes de la note (`4f127118…`) : aucune dépense hors de `GO-2026-11-10-10`, aucune autre série, aucune décision de
nœud. »

### D-5 — à préciser — l'heure de la note `2320` est fausse
Preuve : le nom de la note et son titre portent « consigné à 23:20 UTC » ; elle a été commitée le 12 novembre à
22:50:48Z (commit `1356c77c`) ; l'horloge de la machine lisait 22:51:12Z juste après. 23:20 n'était donc pas encore
arrivé. L'heure de réception « vers 22:14Z » n'est pas vérifiable par le dépôt. La note ne se réécrit pas (R12).
Correction, après le chemin de la note au § 6 : « (note commitée le 12 novembre à 22:50:48Z, commit `1356c77c` ; l'heure
23:20 de son nom et de son titre est fausse ; l'heure de réception, ≈ 22:14Z, est celle que rapporte la session) ».

### D-6 — à préciser — rendre la déclaration complète (§ 6, condition 7)
Preuve : (i) le brouillon 2, commité à 22:32:33Z (`e4ae2610`), donc après le message de ≈ 22:14Z, fondait la condition 7
sur le seul « go (a) » et n'invoquait pas ce message ; la lecture des « deux mots » vient après K-3. (ii) « rapportée à
Lazar avec le lancement » : Lazar apprend la lecture au moment où la dépense commence ; la lui adresser dès le scellement
ne coûte rien et ne retarde rien.
Correction, remplacer « c'est une lecture de la session, déclarée ici et rapportée à Lazar avec le lancement (la
contre-lecture recommandait un mot exprès) » par : « c'est une lecture de la session, formée après la contre-lecture (le
brouillon 2, commité après ce message, ne l'invoquait pas), déclarée ici et rapportée à Lazar dès le scellement, avant la
création de l'instance (la contre-lecture recommandait un mot exprès) ».

### D-7 — à préciser — section « Contre-lecture »
Preuve : K-3 y figure sous « Traitement » alors que sa correction n'est pas suivie ; la présente contre-lecture n'y figure
pas.
Correction : remplacer « K-3 (condition 7 : mot direct de Lazar, voir § 6 ; la session y tient pour mot de lancement les
deux mots de Lazar, lecture déclarée) » par « K-3 : correction recommandée non suivie ; la session tient les deux mots de
Lazar pour le mot de lancement, lecture déclarée au § 6 » ; ajouter : « Contre-lecture différentielle (R2) :
`docs/notes/reproduction-attaque-publiee-v1/contre-lecture-differentielle-addendum-4-bailey-v1.md` (empreinte de son
compagnon `.sha256`), contre-lecteur neuf, sur la version `abd68108…` : « scellable après corrections » ; D-1 à D-7 et
leur traitement. »
