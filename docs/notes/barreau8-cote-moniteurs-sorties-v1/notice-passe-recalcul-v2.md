# Notice d'emploi — passe de recalcul de l'activité interne du barreau 8 (saboteur à budget), côté moniteurs — v2

Version 2, écrite le 2026-11-19 (UTC) après le brouillon 9 du texte ; elle remplace la version 1 (`notice-passe-recalcul-v1.md`, `45da9b99be0a3f9dacbf0a98aae570982f1f8b4dfb000920a402ec202c9aa472`, qui reste en place, intacte, avec le code et les essais de version 1). Ce qui change : le code de version 2 ; une sonde des couches 7 ou 23 non conforme arrête la passe ; la ligne de scellement est la première du registre ; l'exigence de mémoire posée à la machine ; l'état des lacunes après le brouillon 9. Les noms et les formats de la livraison sont inchangés. Écrite par le développeur du code de la passe (sous-agent Fable 5.2 de la session « barreau 8, côté moniteurs »), qui n'a lu aucun résultat du programme ni rien du saboteur. Elle sert trois lecteurs : l'exécutante de la course du saboteur, qui conduit la passe sans modifier le code ; le développeur du code de la lecture, qui relit la livraison ; le rédacteur du texte préenregistré, qui reprend d'ici les noms et les formats des fichiers livrés.

## Pièces qui font foi, et code

- Texte préenregistré, **brouillon 9** : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon9.md`, empreinte `aca110b0635abf9e7e5a1bdd1dc66b94aaae40ad5c72a6e7d6127967f87f272d` (brouillon 6 lu en entier, brouillons 7, 8 et 9 lus par différence faite par programme ; une courte différence peut encore suivre). **Le texte scellé aura une autre empreinte** (entropie des graines et une entrée de contre-lecture remplies) : cette empreinte est à porter à la ligne `SCELLEMENT-SONDES-IIB` du registre propre et au bordereau du code ; le code ne la connaît pas et ne la devine pas, il la lit au registre.
- Note d'interface, **version 6** : `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v6.md`, empreinte `20c9ed6e480646b6bf3a5f6007be5f88b439c916763a618f3880634e92ad8ce1` (version 5 lue en entier, version 6 par différence).
- Formes transmises par la session mère pendant l'écriture (messages du 2026-11-19) : la forme du registre propre et du bordereau du code ; la forme exacte de l'extrait scellé du côté exposé ; le réglage de décodage.
- Code : `src/controle_ia/barreau8_moniteurs/passe_recalcul_v2.py` ; essais : `tests/test_barreau8_moniteurs_passe_v2.py` (86 essais, modèle jouet seulement). **C'est le module de version 2 qui se lance et qui se porte au bordereau du code** ; le module de version 1 ne doit pas être chargé par la passe. Leurs empreintes sont dans leurs compagnons `.sha256`.
- Modules du dépôt réemployés tels quels : `premier_test_ia.figees.lire_sondes` (seul lecteur des vecteurs et des biais), `sondes.familles.SondeLineaireJetons`, `harnais.activations` (`blocs_decodeur`, `type_de_capture`, `ecarts_par_jeton`), `harnais.formats.FormatChat`, `harnais.modeles` (liste blanche, type des poids), `premier_test_ia.conditions.environnement`, `environnements.pilote_a` (`charger_taches`, `tache_de`), `environnements.invites.charger_invite`, `organismes.lora` (`injecter`, `charger_etat`, `fixer_dose`, `empreinte_adaptateurs`), `t06.distillation_transcription.adaptateurs_en_simple_precision`, `scellement`, `manifeste`, `prereg`, `gardes`. Aucun utilitaire d'écriture déterministe d'archives n'existait hors du paquet interdit : la passe porte le sien (`ecrire_npz_deterministe`).

## Ce que la passe fait, dans l'ordre

1. Garde de durée et de dépense (P9), puis garde d'ouverture (P0) : registre propre, texte scellé, bordereau du code, modules chargés, rapport de conformité, notice, devis, ligne d'accord. Rien d'autre n'est ouvert avant.
2. Garde des entrées (P1) : extrait scellé du côté exposé à sa forme fermée ; les quatre fichiers de la course aux chemins et aux empreintes de l'extrait ; tâches d'évaluation ; fichiers de sondes et de planchers.
3. Lecture des deux fichiers d'actions ; garde d'alignement (P3), clauses (a) et (c) et structure des épisodes.
4. Règle mécanique des sondes lues ; liste des directions projetées.
5. Manifeste de la passe (`runs/<run_id>/manifeste.json`, scellé, qui reste du côté exposé) : configuration et son empreinte, versions, graines, commit, sondes lues, liste fermée des chemins.
6. Jetoniseur seul ; lecture de `clean_up_tokenization_spaces` dans `tokenizer_config.json` après comparaison d'empreinte ; garde d'alignement (P3), clause (b), sur les 2 560 actions. **Les poids ne sont chargés qu'ensuite.**
7. Poids ; garde du modèle (P2) ; contextes rebâtis par la recette de la question (6) de la note ; sous-échantillons.
8. Pose des adaptateurs ; contrôle du contexte par la vraisemblance (P10) : artefact, puis lecture, avant la passe.
9. Première passe : lots de 8 actions d'une seule condition, dans l'ordre du fichier des identifiants ; gardes P4, P5, P6, P9 à chaque lot ; scores sur la carte.
10. Seconde passe sur le sous-échantillon de la couche 15, ordre inverse ; garde de répétabilité (P7).
11. Écriture des fichiers 1 à 4, garde de taille (P9), relecture des modules (P0), clôture des gardes, trace, bordereau, journal.

Un arrêt à n'importe quelle étape écrit `<sortie>/trace-arret-passe-barreau8-v1.json` (scellée) et **aucun bordereau** : sans bordereau, il n'y a pas de livraison.

## Ligne de commande exacte

Depuis la racine du dépôt, `PYTHONPATH=src`, interpréteur de `.venv`. Aucun paramètre n'a de valeur par défaut, hors `--cache-modele` (cache local de la bibliothèque) et `--autoriser-depot-sale`.

**(a) Empreintes des modules chargés** (aide à la lecture du bordereau) :

```
PYTHONPATH=src .venv/bin/python -m controle_ia.barreau8_moniteurs.passe_recalcul_v2 empreintes-modules
```

**(b) Bordereau du code** (à écrire après le scellement du texte et après le rapport de conformité ; son chemin et son empreinte vont à la ligne `CODE-PASSE-IIB`) :

```
PYTHONPATH=src .venv/bin/python -m controle_ia.barreau8_moniteurs.passe_recalcul_v2 bordereau-code \
  --racine . --texte-scelle prereg/<texte scellé>.md --rapport-conformite <rapport scellé> \
  --notice docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v2.md \
  --devis <devis scellé> --accord GO-AAAA-MM-JJ-NN --bordereau registres/<bordereau du code>.json
```

**(c) Vérification des entrées, sans modèle ni carte** (étapes 1 à 4 ; à jouer avant de louer la carte) et **(d) passe** : mêmes paramètres, seule l'action change (`verifier-entrees` ou `passe`).

```
PYTHONPATH=src .venv/bin/python -m controle_ia.barreau8_moniteurs.passe_recalcul_v2 passe \
  --racine . --sortie <dossier neuf, hors du dépôt de préférence> \
  --run-id AAAAMMJJ-HHMMSS-passe-barreau8 --entropie <entropie racine du texte scellé, champ F-3> \
  --extrait <extrait scellé du côté exposé>.json \
  --taches donnees/20261007-082440-t05-extraction/taches-evaluation.json \
  --sondes-legeres donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz \
  --sondes-neuves donnees/20261114-001352-t07-lecture-reel/sondes-neuves-t07.npz \
  --planchers donnees/20261114-001352-t07-lecture-reel/planchers-figees-t07.npz \
  --registre registres/sondes-iib-v1.md --registre-accords registres/go.md \
  --duree-max-heures <borne de la ligne d'accord> --depense-max-usd <borne de la ligne d'accord> \
  --prix-horaire-usd <prix de la location> --debut-location AAAA-MM-JJTHH:MM:SSZ \
  --identifiant-instance <identifiant de l'instance> --appareil cuda [--cache-modele <cache local>]
```

Les quatre fichiers de la course ne sont pas des paramètres : la passe les prend aux chemins `donnees/<run_id>/…` que l'extrait nomme, sous `--racine`. Chaque entrée doit avoir son compagnon `.sha256`. Le fichier des sondes neuves doit être reconstitué de ses neuf morceaux avant la passe. Le cache du modèle doit être hors du dépôt et hors des dossiers des entrées (sinon la garde P8 refuse ses fichiers).

## Entrées attendues

| entrée | contrôle | empreinte attendue |
|---|---|---|
| registre propre `registres/sondes-iib-v1.md` | forme des lignes (ci-dessous) | — |
| texte scellé (chemin de la ligne `SCELLEMENT-SONDES-IIB`) | `prereg.exiger_prereg_scelle` ; empreinte de la ligne | celle de la ligne, jamais devinée |
| bordereau du code (chemin de la ligne `CODE-PASSE-IIB`) | compagnon ; empreinte de la ligne ; clés fermées | celle de la ligne |
| rapport de conformité, notice, devis | compagnon ; empreinte du bordereau du code | celles du bordereau du code |
| registre des accords | une ligne porte l'identifiant de l'accord et l'empreinte du devis | — |
| extrait scellé du côté exposé | compagnon ; forme fermée (ci-dessous) | — |
| `donnees/<run_id>/ids-actions-iib-evaluation.npz`, `textes-actions-iib-evaluation.jsonl`, `adaptateur-eleve.pt`, `adaptateur-temoin-jumeau.pt` | compagnon ; empreinte de l'extrait | celles de l'extrait |
| `taches-evaluation.json` | compagnon | `76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e` |
| `sondes-figees-legeres.npz` | compagnon ; `lire_sondes` | `701f73bd3a8ef30f46b304a6d5caa21444f0e1daf0829d04046e4024aa4e6e60` |
| `sondes-neuves-t07.npz` | compagnon ; `lire_sondes` | `374ad47346ae40d5a4d350724d0d19b5961724066dd7fdfaaf0adf1c3a4cbb79` |
| `planchers-figees-t07.npz` | compagnon ; `lire_sondes` | `94ca013c66e5dbd35b3ea55ec8aa4eb7b299e5dd63a95f7ccea7ced8d120f224` |
| modèle `meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659`, dans le cache local | dossier de la révision ; quatre fichiers | `config.json` `29e4c210…704e6e` ; `generation_config.json` `189fb0c0…e5f7fd` ; `tokenizer.json` `79e3e522…64b2b4` ; `tokenizer_config.json` `177c7b61…bbcd424` (valeurs entières dans `SPECIFICATION_TEXTE`) |

**Registre propre** (fonction `lire_registre_propre`, seule à en connaître la forme) : chaque ligne d'une clé est `| CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin relatif au dépôt | sha256 de 64 caractères |`, quatre colonnes exactement, une seule ligne par clé parmi `SCELLEMENT-SONDES-IIB`, `CODE-PASSE-IIB`, `CODE-LECTURE-SONDES-IIB`, `LIVRAISON-PASSE-IIB`, `ETATS-COURSE-IIB`, `LECTURE-SONDES-IIB`. La passe exige les deux premières ; la ligne du scellement doit être la première des lignes de clé ; la ligne du code doit venir après elle, par son rang et par son heure, strictement ; une ligne datée à quatre colonnes qui porte une clé hors des six est refusée. L'en-tête du registre n'est pas contrôlé par la passe.

**Bordereau du code** (JSON scellé, sept clés exactement) : `texte_scelle` {`chemin`, `sha256`} ; `modules` {nom du module → {`chemin`, `sha256`}} pour chaque module `controle_ia` chargé par la passe ; `commit` ; `rapport_conformite`, `notice`, `devis` {`chemin`, `sha256`} ; `accord` (`GO-AAAA-MM-JJ-NN`). À l'ouverture, l'ensemble des modules chargés et leurs empreintes doivent être exactement ceux du bordereau (aucun absent, aucun de trop, aucun modifié) ; ils sont relus à la fin de la passe.

**Extrait scellé du côté exposé** (fonction `lire_extrait_du_cote_expose`, seule à en connaître la forme ; vérifiée à la lettre, clés répétées refusées) : six clés au premier niveau — `avertissement` (chaîne constante « EXPLORATOIRE, NON OPPOSABLE (R-522) : extrait sans mécanisme pour le côté moniteurs ») ; `run_id` (`AAAAMMJJ-HHMMSS-` puis minuscules, chiffres, tirets) ; `commit_lancement` (40 caractères hexadécimaux minuscules) ; `versions` (objet chaîne → chaîne, clés triées, parmi `python`, `plateforme`, `numpy`, `scipy`, `matplotlib`, `torch`, `transformers`, `tokenizers`, `safetensors`, `huggingface_hub`, `transformer-lens`, `vllm`, `peft`) ; `fichiers_de_la_passe` (exactement les quatre chemins `donnees/<run_id>/ids-actions-iib-evaluation.npz`, `…/textes-actions-iib-evaluation.jsonl`, `…/adaptateur-eleve.pt`, `…/adaptateur-temoin-jumeau.pt`, chacun avec une empreinte de 64 caractères) ; `etats_par_lot_evaluation` (liste non vide de lignes à six clés : `adaptateur`, `condition`, `dose_avant`, `dose_apres`, `empreinte`, `lot` ≥ 1 ; rangées par condition dans l'ordre H, B50, B100, TJ100, puis par lot). La passe en tire : les chemins et les empreintes des quatre fichiers ; le nom de la course et le commit de lancement (manifeste et trace) ; la cohérence de chaque ligne avec la table des conditions (adaptateur, et `dose_apres` égale à la dose de la condition). Rien d'autre : `dose_avant` et `empreinte` ne sont comparées à rien.

## Livraison : liste fermée, noms, formats

Tout est dans `<sortie>/livraison/`. Chaque fichier a son compagnon `<nom>.sha256` (format de `sha256sum`). Six sortes de fichiers, rien d'autre.

**Découpage en morceaux.** Une archive `X.npz` n'est jamais livrée entière : elle est coupée en `X.npz.morceau-000`, `X.npz.morceau-001`, … de 50 000 000 octets (le dernier plus court), dans l'ordre, et décrite par `X.npz.morceaux.json` : `{"fichier": "X.npz", "taille": <octets du fichier entier>, "sha256": <empreinte du fichier entier>, "morceaux": [{"nom", "taille", "sha256"}, …]}`. Le fichier entier se rebâtit en collant les morceaux dans l'ordre de la liste ; son empreinte doit être celle du champ `sha256`. Les archives sont au format `numpy` sans compression, entrées triées par nom, dates fixées au 1er janvier 1980, sans objet Python (`numpy.load(..., allow_pickle=False)`) : deux passes sur les mêmes entrées rendent les mêmes octets. Les listes nommées y sont des tableaux `uint8` qui portent un JSON en UTF-8 (`json.loads(bytes(tableau).decode("utf-8"))`).

1. **Scores par action** — `scores-par-action-passe-barreau8-v1.npz` (en morceaux). Tableaux : `scores`, `float64`, forme (actions, directions, 2) — case 0 : le **maximum** des scores par jeton (agrégation de production) ; case 1 : leur **moyenne arithmétique** (bras de diagnostic, jamais en production) ; `NaN` aux deux cases de toutes les directions pour une action sans jeton noté, et pour elles seules. `directions`, JSON : liste, dans l'ordre des colonnes, de `{"nom", "couche", "empreinte", "role"}` (`empreinte` : celle de la sonde dans l'index de son fichier ; `role` : « sonde » ou « plancher »). `agregations`, JSON : les deux libellés des cases. Les lignes sont dans l'ordre du fichier des identifiants (champ `rang` de l'index). Ordre des colonnes : pour chacune des trois sondes décisives lues, dans l'ordre tromperie, enjeux, dissimulation : la sonde, puis ses 800 directions de plancher dans l'ordre 0 à 799 (pour la dissimulation, l'ordre de l'index de son fichier) ; puis les sondes des couches 7 et 23 présentes, dans l'ordre `dissimulation-lineaire-c7`, `dissimulation-lineaire-c23`, `tromperie-difference_moyennes-c7`, `-c23`, `enjeux-lineaire-c7`, `-c23`. 2 409 colonnes si tout est lu.
2. **Scores par jeton des sondes projetées** — `scores-par-jeton-passe-barreau8-v1.npz` (en morceaux). `scores`, `float64`, forme (somme des jetons notés, sondes projetées) : les actions dans l'ordre de l'index, les jetons dans l'ordre de l'action ; les bornes d'une action sont les sommes cumulées de `jetons_notes`. `colonnes`, JSON : les mêmes objets que `directions`, pour les seules entrées de rôle « sonde », dans le même ordre relatif (neuf colonnes au plus). Aucune direction de plancher.
3. **Index** — `index-passe-barreau8-v1.jsonl` : une ligne JSON par action, dans l'ordre du fichier des identifiants, clés triées, dix champs exactement : `cle` (clé d'action de la note), `tache`, `condition`, `episode`, `pas`, `jetons_notes`, `jetons_contexte`, `rang` (rang dans l'ordre du fichier, à partir de 0), `sous_echantillon_couche_decisive` (booléen : couche 15), `sous_echantillon_couches_descriptives` (booléen : couches 7 et 23).
4. **Sous-échantillon d'activité brute** — `activite-brute-c7-passe-barreau8-v1.npz`, `activite-brute-c15-passe-barreau8-v1.npz`, `activite-brute-c23-passe-barreau8-v1.npz` (chacune en morceaux). Un tableau par action du sous-échantillon de la couche, de nom `a<rang sur cinq chiffres>` (par exemple `a00016`), `float32`, forme (jetons notés, 4 096) : la capture en simple précision de la première passe.
5. **Trace des gardes** — `trace-gardes-passe-barreau8-v1.json`, clés exactement : `gardes` (pour P0 à P10 : `etat` « tenue », `actions_vues`, `actions_controlees`) ; `modules_charges` (nom → empreinte) ; `course` (`run_id`, `commit_lancement` de l'extrait) ; `modele` et `jetoniseur` (`nom`, `revision`) ; `premier_jeton_cloture` ; `clean_up_tokenization_spaces` (valeur lue) ; `empreinte_tokenizer_config` ; `versions_jetonisation` (`transformers`, `tokenizers`) ; `fichiers_sondes` (`legeres`, `neuves`, `planchers` → empreinte entière) ; `sondes` (nom → « lue », « sans objet » ou « absente ») ; `conditions` (par condition : `adaptateur_et_dose_relus_egaux` « oui » ou « non », `actions`, `actions_sans_jeton_note`, `jetons_notes`) ; `adaptateurs` (`eleve`, `temoin-jumeau` → `empreinte` du fichier chargé, `egale_a_l_extrait`) ; `repetabilite` (`plus_grand_centile_99`, `controle_negatif` : `actions_comparables`, `fraction_vue`, `tenu`) ; `controle_du_contexte` (`fraction`, `fraction_par_condition`, `actions_controlees`, `artefact` : `fraction`, `vu`) ; `chemins_lus` (nombre) ; `chemin_prive_lu` ; `taille_livraison` (octets des fichiers 1 à 4 et de leurs compagnons) ; `duree_secondes` ; `identifiant_instance`. Aucun chemin, aucun texte, aucun identifiant de jeton.
6. **Bordereau de livraison** — `bordereau-livraison-passe-barreau8-v1.json` : `fichiers` (liste triée par nom de `{"nom", "taille", "sha256"}` pour chaque morceau, chaque `….morceaux.json`, l'index et la trace) ; `manifeste_sha256`. Son empreinte est imprimée par la commande : à transmettre à la session mère pour la ligne `LIVRAISON-PASSE-IIB`.

Restent du côté exposé : `runs/<run_id>/manifeste.json` et `diag/<run_id>/journal-passe-barreau8-v1.json` (empreinte du bordereau, empreinte des adaptateurs relue sur le modèle par condition, chemins lus, fichiers du modèle, durée).

## Codes de refus

La commande sort avec le code 1 et écrit « ARRÊT : garde Pn non tenue : cause » ; la trace d'arrêt porte l'état de chaque garde (« tenue », « non tenue » avec sa cause, « non jouée »), « un chemin privé lu », l'identifiant de l'instance. Sur un arrêt de la garde P9, la cause nomme l'instance à arrêter **par son identifiant** ; le code n'arrête aucune machine lui-même. Relance seulement pour cause technique établie, dans un dossier de sortie neuf et sous un `run_id` neuf.

| garde | refus |
|---|---|
| P0 | ligne de scellement ou du code absente, répétée, de forme fausse ; ligne du code non postérieure ; empreinte du texte ou du bordereau fausse ; module absent, de trop ou modifié ; pièce modifiée ; accord absent |
| P1 | compagnon absent ou non conforme ; extrait hors de sa forme ; empreinte différente de l'extrait, de la note ou de la table ; aucune sonde décisive lue ; sonde des couches 7 ou 23 trouvée sous son nom mais non conforme |
| P2 | modèle, révision, couches, dimension, type, attention, jetons de fin, premier jeton de clôture, jeton de début, date du gabarit |
| P3 | clés non alignées, préfixe, longueur, jeton de fin, champ de trop, épisode incomplet ; fichier de configuration du jetoniseur absent, d'empreinte fausse, sans le champ, champ non booléen, appel qui refuse le paramètre ; décodage différent du champ `texte` (la clé de l'action est écrite, jamais le texte) |
| P4 | lot qui mêle des conditions ou dépasse 8 actions ; adaptateur, dose, rang ou type relus différents |
| P5 | couche hors du modèle ; positions capturées différentes des jetons notés ; forme d'un tableau livré |
| P6 | valeur non finie dans une capture ou un score |
| P7 | 99e centile de l'écart entre les deux passes au-dessus de 0,2 ; contrôle négatif aveugle ou moins de 10 actions comparables |
| P8 | chemin privé, ou fichier du dépôt hors de la liste fermée, demandé à l'ouverture (refusé avant lecture) ; environnement rebâti porteur d'un texte privé |
| P9 | durée ou dépense au-dessus des bornes ; taille au-dessus de 2 000 000 000 octets |
| P10 | moins de 10 actions éligibles ; artefact non vu (garde aveugle) ; fraction sous 95 % |

## Exigence posée à la machine de la passe

**Environ 16 Go de mémoire vive libres hors du modèle** (estimation non mesurée, détail ci-dessous) : le devis doit en tenir compte dans le choix de la location. Disque : environ 3,5 Go libres pour la sortie, hors du cache du modèle et des entrées.

## Durée et mémoire attendues (non mesurées sur la carte)

- Durée : l'ordre de grandeur est celui du devis ; ce code ne l'a pas mesuré. À la première passe (2 560 passes avant en 320 lots) s'ajoutent le contrôle du contexte (3 passes avant pour chacune des 161 actions au plus, avec le calcul des probabilités sur les seules positions de l'action) et la seconde passe (161 actions au plus). Les relectures des adaptateurs (deux par lot, environ 54 Mo à relire et à empreinter chacune) coûtent de l'ordre de quelques minutes en tout.
- Mémoire vive, pire cas : captures gardées du sous-échantillon, trois couches, 161 actions de 400 jetons : 161 × 400 × 4 096 × 4 × 3 = 3,2 Go ; seconde passe : autant ; écriture des archives : environ 1,1 Go de plus ; fichier des sondes neuves : environ 0,5 Go. Prévoir **16 Go de mémoire vive libres** hors du modèle. Disque : 2 Go pour la livraison, plus 1,1 Go transitoire pendant le découpage.
- Mémoire de la carte : les poids en `bfloat16` (environ 16 Go), les sorties de trois couches pour un lot de 8 transcriptions, et les directions en double précision (2 403 × 4 096 × 8 = 79 Mo).

## Ce qui n'a pas pu être éprouvé ici, et l'essai à blanc

Jamais exécuté ici : `ChargeurReel` (cache local, chargement du jetoniseur puis des poids depuis le dossier de la révision) ; la carte ; les poids en `bfloat16` et la conversion des captures ; le gabarit réel et sa date ; la présence et la valeur du champ dans la configuration réelle du jetoniseur ; le comportement de `decode` du jetoniseur réel avec le paramètre explicite ; la lecture des trois vrais fichiers de sondes ; les seuils de P7 et de P10 sur le modèle réel ; la durée et la mémoire.

Essai à blanc, pas à pas, avant la passe entière :
1. Sans carte : la commande (c) `verifier-entrees`. Attendu : « entrees : conformes », 2 560 actions, 2 409 directions (ou moins si une sonde est « sans objet » ou « absente » : le dire à la session mère avant de continuer), et l'état de chaque sonde.
2. Sans carte : vérifier que le cache local porte la révision, par `sha256sum` des quatre fichiers de configuration contre la table des entrées.
3. Sur la carte : il n'existe pas de mode « une action ». Lancer la passe entière ; elle joue d'elle-même, avant la première passe et dans cet ordre, P3 (b) sur toutes les actions (jetoniseur seul, sans les poids), P2, la reconstruction des 256 épisodes, puis P10 (artefact et lecture) : ce préambule est l'essai du chemin réel, et tout refus y coûte quelques minutes de carte, non la passe. Suivre la sortie : un arrêt écrit sa cause et la trace d'arrêt.
4. Si P3 (b) refuse à la première action : ne rien changer, porter le fait à la session mère (le texte dit : écart, nœud de Lazar).
5. Après la passe : vérifier `sha256sum -c` sur chaque compagnon de `livraison/`, transmettre l'empreinte du bordereau.

## Écarts ou lacunes du texte : état après le brouillon 9

Les treize points de la version 1 de cette notice (forme de l'extrait ; tâches dans P1 ; registre et bordereau du code ; P1 contre la règle mécanique ; liste fermée de P8 ; bornes de P9 ; référence de P7 ; étendue et moment de P10 ; champs de la trace et taille ; graines ; noms et formats de la livraison ; clause (d) de P3 et reconstruction ; formation des lots) **sont tous repris par le brouillon 9**. Le code de version 2 s'y aligne sur trois points que la version 1 lisait autrement :

- une sonde des couches 7 ou 23 trouvée sous son nom mais non conforme **arrête la passe** (garde P1) ; la version 1 l'écrivait « sans objet » ;
- la ligne `SCELLEMENT-SONDES-IIB` doit être **la première** des lignes de clé du registre propre ;
- une ligne datée à quatre colonnes d'une clé hors des six est **refusée**.

Vérifiés sans changement : le tirage du sous-échantillon (clés des actions d'au moins un jeton noté, triées par le tri des chaînes de Python ; rangs multiples de 16, ou de 128, et la dernière) suit la phrase du texte à la lettre, et un essai fixe la liste attendue sur un cas calculé à la main ; la garde de taille tient les fichiers 1 à 4 et leurs compagnons sous 1 996 000 000 octets (2 000 000 000 moins la réserve de 4 000 000), puis la livraison entière, bordereau et compagnons compris, sous 2 000 000 000.

**Différences qui restent entre le texte (brouillon 9) et ce que le code écrit** — aucune sur un nom de fichier, une clé, un type ou un champ ; quatre remarques de détail :

1. *Libellés du tableau `agregations`.* Le texte dit « les deux libellés des cases » sans les écrire. Le code écrit exactement `"maximum (production)"` et `"moyenne (bras de diagnostic, jamais en production)"`. Le code est juste ; le texte gagnerait à les écrire, ou à dire que la lecture ne s'y fie pas (elle doit se fier au rang de la case).
2. *Champ `chemin` des modules du bordereau du code.* Le texte dit « chemin » ; le code écrit le chemin relatif au dépôt quand le module est sous `--racine`, sinon le chemin absolu ; à l'ouverture il ne compare que le nom et l'empreinte de chaque module, pas ce chemin. Les deux sont compatibles ; à préciser dans le texte si la lecture fait de même.
3. *Notice citée par le texte.* Le brouillon 9 cite la version 1 de cette notice et son empreinte ; la version 2 la remplace (mêmes noms et formats de livraison).
4. *Ordre des autres lignes du registre.* Le texte fixe une condition d'ordre par clé ; la passe n'exige que les deux premières lignes et contrôle seulement que toute autre ligne de clé présente vient après celle du scellement (rang et heure) ; les conditions propres à `LIVRAISON-PASSE-IIB`, `ETATS-COURSE-IIB` et `LECTURE-SONDES-IIB` relèvent de la lecture. Conforme à la phrase « La passe exige les deux premières ».

Lectures strictes que le code garde et que le texte dit maintenant : modules chargés exactement ceux du bordereau, à l'ouverture et à la fin ; ligne d'accord qui cite l'empreinte du devis ; P1 qui l'emporte sur « sans objet » pour un fichier de sondes.

## Sur les essais

Le modèle jouet (4 couches, largeur 32, type Llama, jetoniseur par caractères) est **ajusté 110 pas sous graine** sur des suites qui dépendent du contexte, parce qu'un modèle à poids aléatoires ne donne aucun sens à la garde P10 (mesuré : fraction voisine d'un demi). Ce n'est pas un réglage de la garde : les seuils sont ceux du texte. Sur ce jouet, la fraction du cas sain est de 24 actions sur 25 (0,96), celle de l'artefact de 0,24 : la marge est d'une action. Le réglage du jouet (nombre de pas, échelle des adaptateurs) a été choisi après avoir vu un essai échouer à 0,88 avec 70 pas : cela ne dit rien du modèle réel.
