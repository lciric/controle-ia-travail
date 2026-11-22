# Contre-lecture de la configuration de génération du calage de la porte G1 (v1)

- **Classe C** (contre-lecture, R2). Elle ne tranche rien et ne vaut pas scellement.
- **Qui** : contre-lecteur neuf, Claude Opus 5.5 (`claude-opus-5-5`), sous-agent lancé par un script de la session mère (`[session]`). Je n'ai écrit ni la configuration, ni la note, ni les programmes, ni le préenregistrement du banc fermé, ni celui de G1 ; je ne conçois aucun moniteur.
- **Quand** : 21 novembre 2026, de 19:42 à 19:55 UTC (relevés `date -u`).
- **Demande** : mots du directeur « go b » et « go configuration du calage » (`registres/go.md:676`, GO-2026-11-21-77).
- **Non lus, par consigne** : aucun résultat (7a, 7b, T0.6, étapes B et B bis, P3-bis) ; rien sous `[chemin réservé]`, `runs/`, `diag/`, `archives-reponses-modeles/` ; aucune famille aveugle ; aucun épisode ; aucun fichier « [chemin réservé] » ni « [chemin réservé] » ; rien sous `brouillons/ii-b-saboteur-budget-v1/` ni sous `/root/.claude/` (deux sorties longues que l'outil y a rangées de lui-même n'ont pas été ouvertes ; j'ai relu par morceaux, aux chemins). Les chemins sous `[chemin réservé]` que nomme la configuration de T0.7 n'ont pas été ouverts. Aucun téléchargement, aucun envoi à un fournisseur, aucun commit.
- **Refus d'un classifieur de sûreté** : aucun.

## Verdict

**À corriger.** Les valeurs du fichier sont justes : chacune se retrouve à sa source, et rien n'est inventé. Le fichier est aussi cohérent avec P3, avec les configurations scellées du pilote et des organismes, et avec le brouillon 6 de G1. Trois corrections sont pourtant à faire avant le scellement :

1. le programme de validation ne vérifie pas qu'une valeur est égale à sa source ;
2. aucun relevé de référence n'est désigné pour les valeurs que l'opérateur relève sur le poste ;
3. le fichier ne dit rien du type numérique des activations conservées, alors que les sondes de T0.7 ont lu des activations rangées en demi-précision.

Les quatre nœuds de la note sont justes. Il n'en faut pas de cinquième à ce stade.

## Pièces contre-lues (empreintes recalculées ; compagnons vérifiés par `sha256sum -c`, tous « OK »)

| Pièce | Empreinte |
|---|---|
| `prereg/configuration-generation-calage-g1-v1.json` | `4bfdd98d2226abe1fc173a68e62700039f14fc8d2b3bb2b2d6ba6bbf7082079d` |
| `docs/notes/configuration-calage-g1-v1/note-configuration-calage-g1-v1.md` | `322aaa85d0a8b074fc1946b9f166e674b65e60b2a8128301e87d606312043707` |
| `…/note-configuration-calage-g1-v1-erratum-1.md` | `6edfba76abbe2a226e253f214fae086fd8060989b8c9e042dcf850fa379e2d31` |
| `…/valider_configuration_calage_v1.py` | `4b19c5a2ae4addfd5c9cc1497fe735563d3be56e587ca1e9c30b064ab122df57` |
| `…/empreinte_gabarit_calage_v1.py` | `7c3a541a38a4c33e679779802f0fae9e58a1c548a4557dd8f02cdcae88119640` (égale à `methode.programme_sha256`) |
| `…/assembler_configuration_calage_v1.py` | `b257fadf63ab33da7314c16145ae9e103f0eb7f4cfcb559714684ae48c71b219` |
| `…/essai-validation-v1-sortie.txt` | `a22a85bbc80a1d61536b576cd1483ac0feebd829b9e457dc57c9bf178baaa1b2` |
| `…/essai-empreinte-gabarit-v1-sortie.txt` | `be42b82fa86ce9f0e2038615a19623ab7806063141e7691409b4ef00b1a188dd` |

**Sources relues aux lignes désignées.**

- L'attestation `docs/notes/attestation-episodes-calage-g1-v1/attestation-format-outils-pile-v1.md`, `3f0b50f0…`, l. 30 à 34 et 54 à 58.
- Le brouillon 6 de G1, `939b56e5…`, l. 3, 51, 104, 151, 186, 223 à 226, 323 et 363 à 367.
- Le préenregistrement de T0.7, `d7d180ec…`, l. 1050 à 1062 ; sa configuration v8, `e31c7a79…`, pour ses clés seulement.
- Le préenregistrement de P3, `d975e981…`, l. 316 à 322 et 350 à 353 ; la configuration de P3.
- Les configurations du pilote (T0.5) et des organismes (T0.6), pour leurs clés de génération.
- Le code : `modeles.py`, `episode.py`, `propositions.py`, et pour vérification `lancer_pilote_a.py`, `pilote_a.py`, `manifeste.py`, `validation_reelle.py` (l. 355 à 370), `t06/lanceur_v2.py` (l. 50 à 85, `f2db51fc…`), `premier_test_ia/run.py` (l. 245 à 260).
- Les dépendances `requirements-cpu.txt` (`bc86590f…`) et `requirements-gpu.txt` (`3850945b…`). Le dépôt n'en a pas d'autre pour la machine de calcul : `requirements-donnees.txt` et `requirements-pilotage.txt` ne portent ni torch ni transformers.
- La contre-lecture des trois choix, `bc9ec0fd…`, l. 112 à 129.
- Les décisions N-054 (`c8a00b3f…`), N-056 (`3592c1e9…`, l. 50 à 57), N-062 (`63f42690…`, l. 20 à 26), N-063 v2 (`b2d9f035…`) et N-019 (`9058fa27…`, l. 12 à 24 et 40 à 44).
- Les lignes 672 à 682 de `registres/go.md`.
- Le banc fermé : brouillon 11 au commit `f0edf989…` (`b3bb5adf…`), et **brouillon 14, le plus récent** après `git fetch` (tête `5182b602c`, `4489d39957b7dba53d015521867c2d7cb56ee01a6d3e2070523b889555173784`) : champs n° 1 et 2 (l. 79 à 82), champ n° 3 (l. 84), D3 (l. 95 à 109), D4 (l. 111 à 125), condition de lancement 5 (l. 310), vérification de concordance (l. 338 à 348), déroulement (l. 352 à 355), graines (l. 367 à 374), attestation de l'assembleur (l. 93).

## 1. Ce que j'ai rejoué

| Épreuve | Résultat |
|---|---|
| Programme de validation, sur le fichier | « configuration valide » : 67 entrées, 204 sources, 32 pièces, 7 valeurs à remplir hors du fichier |
| Le même, en contrôle de lancement (`--lancement`) | « configuration valide » ; les huit fichiers gelés sont à leur empreinte dans l'arbre de travail (recalculées une à une) |
| Le même, en épreuves (`--essai`) | 4 cas sains et 45 artefacts, tous réussis ; les mêmes lignes que dans la sortie versée |
| Programme de l'opérateur, en épreuves (`--essai`, dans `.venv`, au tokeniseur jouet) | 2 cas sains et 8 artefacts, tous réussis ; les mêmes lignes que dans la sortie versée |
| Programme de l'opérateur, en mode réel | arrêt attendu : le tokeniseur est absent et rien n'est téléchargé |
| Relevé au tokeniseur jouet, écrit dans mon bloc-notes, puis passé au programme de validation (`--releve`) | refusé : « mode jouet », « poids non relevés » |
| Outil d'assemblage relancé vers le bloc-notes, au commit et à la date du fichier | sortie identique octet pour octet (`4bfdd98d…`) |
| Vecteurs d'essai des graines recalculés par numpy 2.4.6, sans le code du dépôt | égaux : graines, état de contrôle, échantillon de la garde (aucune action pour la clé (8, 0, 0) ; les actions 1 et 5 pour la clé (3, 7)) |
| Empreintes de la consigne honnête à T = 10 et du format d'action, recalculées depuis `propositions.py` | égales (`64c4866a…`, `f918517d…`) ; champs, champs exigés et taille de l'ensemble aussi |
| **Douze artefacts de mon cru**, hors de la liste du programme (copies modifiées dans le bloc-notes, avec leur compagnon) | **neuf passent « configuration valide »** ; voir C1 |

## 2. Chaque valeur à sa source

Toutes les valeurs simples (nombres, chaînes, listes courtes) se retrouvent dans l'extrait d'au moins une de leurs sources ; je l'ai contrôlé par programme. Je les ai aussi relues dans les sources elles-mêmes.

- **Modèle et révision** : `0e9e39f2…` se lit dans T0.7, l. 1057, et dans les configurations de P3 (l. 8), du pilote (l. 22) et des organismes (l. 20).
- **Génération** : agents 1, pas 10, lot 8, 400 jetons par action, température 1,0. Ces valeurs se lisent à P3, l. 318 et 319, dans la configuration de P3, dans celle du pilote et dans celle des organismes (le lot de la distillation, l. 68 de la configuration des organismes, vaut 1, mais c'est un autre objet).
- **Pile** : noyau « defaut », un fil, bfloat16 et « sdpa ». Les lanceurs de P3 et de T0.6 passent tous deux par `charger_modele_et_format` (`lancer_pilote_a.py:263`) et par `noyau(...)`.
- **Garde d'équivalence** : 0,05 ; « q99 » ; 0,2 ; contrôle négatif 4, 10 et 0,95.
- **Gabarit** : couches 7, 15 et 23 ; date « 26 Jul 2024 ».
- **Versions** : `requirements-cpu.txt`, l. 2 et 7 à 11 ; `requirements-gpu.txt` renvoie aux mêmes (l. 7).
- **Graines** : la chaîne de dérivation est celle de `pilote_a.py:73-76` et `:113-115`, et celle de `run.py:253-256`.

Les entrées dont la nature est « choix neuf » sont bien des choix : matériel, empreinte du gabarit et sa méthode, commit et fichiers gelés du harnais, vecteurs d'essai, correspondance des cinq outils. Aucune ne se présente comme reprise. Je n'ai trouvé **aucune valeur inventée**. Les sept valeurs laissées nulles portent chacune un état, une méthode et le lieu où elles s'écrivent.

Les lectures du code faites par la note sont exactes :

- **Échantillonnage** : tirage dans la loi entière, sur le processeur, en simple précision (`episode.py:111`, `:121`).
- **Arrêt d'une action** : au jeton d'arrêt, gardé dans l'action, ou au 400e jeton (`:124-127`).
- **Contexte** : la transcription entière est repassée à chaque pas (`:217`).
- **Activations** : une passe unique par épisode, seul, sans cache, en fin de lot (`:260`).
- **Jetons d'arrêt** : `fins_du_modele` plus le premier jeton de clôture (`lancer_pilote_a.py:265`). Le programme de l'opérateur les relève de la même façon, depuis `generation_config.json`.
- **Plan de lots** : il fait partie de la pile (`episode.py:12`).
- **Chiffres de N-019** : l. 14 (99e centile 0,1354), l. 16 (panne de mémoire du bras « math »), l. 22 et 23 (passe unique 8,2839 s, génération 665,8512 s pour seize épisodes).

## 3. Cohérence avec T0.7 et P3

- **P3** : tout concorde avec les l. 318 à 322 (environnement (a), N = 1, T = 10, lot de 8, 400 jetons, température 1,0, garde sur 5 %, noyau « defaut », mêmes graines d'action d'une condition à l'autre). La règle neuve « un lot de calage ne mêle que des épisodes joués par le modèle nu » reste compatible avec « un lot peut mêler les conditions » (l. 321) : les conditions de P3 étaient toutes jouées par le modèle nu. Elle est marquée « choix, à faire valider » ; c'est juste.
- **T0.7** : révision, couches, flux résiduel et lecture « en une passe » (l. 1056 à 1058) concordent. **Un point de T0.7 n'est pas repris** : les activations y sont « enregistrées par la chaîne de T0.6 sur le disque de l'instance de 7b (demi-précision ; `t06/lanceur_v2.py` `ActivationsDemi`, l. 59-80) ». Ce code les range en float16 et les relit en float32 (`lanceur_v2.py:68-80`). Le fichier fixe une capture en float32 et laisse le stockage dehors. Le banc enregistre au type de capture, donc en float32 (brouillon 14, l. 355). Voir C3.
- **Brouillon 6 de G1** : modèle (l. 51), « même agent, même révision » (l. 151, S6 l. 323), environnement (a) seul pour l'honnête (l. 186), clé (8, t, j′) du calibrage d'épreuve et racine tirée de l'empreinte du texte scellé (l. 365 et 366) : tout est repris fidèlement, et la mention « repris d'un texte non scellé » est juste.
- **Décisions** : N-056 l. 53 (trois couches) et N-062 l. 23 (une famille tenue à l'écart se lit une fois) sont citées à juste titre. N-054 et N-063 ne touchent pas la génération : j'en conviens.

## 4. Complétude pour la comparaison du banc et du calage

- **Ce que le mot du directeur et le champ n° 2 demandent** (`registres/go.md:676` ; brouillon 14, l. 81) : modèle, révision, adaptateur, bibliothèque et version, précision, gabarit et son empreinte, température, noyau, pas, jetons, agents, environnement, tolérance et quantile de la garde, commit du harnais. Tout est présent. L'empreinte du gabarit et le commit sont renvoyés, avec une méthode, au relevé de l'opérateur et au manifeste. Ce renvoi est fondé : l'empreinte ne se calcule pas sans les fichiers du modèle, et aucun téléchargement n'était permis.
- **Ce qui manque** : la désignation d'un relevé de référence (C2) et le type des activations conservées (C3).
- **L'attestation, « ce qui manque » du point 1** : la configuration est écrite, et l'attestation de l'assembleur sur la forme des tâches est renvoyée aux huitième et neuvième questions. Le brouillon 14 les porte (l. 93).
- **La contre-lecture des trois choix, choix 2** : ses réserves 1 et 2 sont couvertes, et les réserves 3 à 5 sortent du fichier, comme le dit l'erratum 1. La réserve 2 demandait aussi que le fichier soit « accepté par qui tient le préenregistrement de G1 ». Le brouillon 14 (l. 81) dit l'ordre décidé par le directeur (GO-2026-11-21-77) ; la ligne « à inscrire sans décision » de la note (§ 8) suffit, à condition que le texte nouveau de G1 cite le fichier **et** le relevé de référence (C2).
- **Le banc a bougé.** Le brouillon le plus récent est le 14 ; le fichier lit le 11. Les lignes citées ont le même texte. Elles sont décalées de 14 à partir de la vérification de concordance : 330 à 332 deviennent 344 à 346, 339 à 341 deviennent 353 à 355, 355 à 359 deviennent 369 à 373. Les quatre écarts du § 4 de la note restent entiers dans le brouillon 14.

## 5. Corrections demandées (sous un nom neuf, R12)

**C1 — Le programme de validation ne contrôle pas qu'une valeur égale sa source (classe B ; importante).** Il vérifie qu'un extrait se trouve dans la ligne citée, mais il ne rapproche pas la valeur de l'extrait. J'ai passé au programme douze copies modifiées, compagnon compris. Neuf sont déclarées « configuration valide » :

- une révision `1111…` de 40 caractères ;
- une température de 0,9 ;
- une tolérance de 0,3 ;
- des couches [7, 15, 24] ;
- un lot de 4 ;
- le noyau « math » ;
- une attention « eager » ;
- quatre fils ;
- 300 jetons par action.

Trois seulement sont refusées, par des gardes voisines : une date changée, par la garde du texte attendu ; une fraction de 0,1, par les vecteurs d'essai ; huit pas, par l'empreinte de la consigne. Le fichier actuel n'est pas fautif (§ 2), mais l'instrument ne garde pas la propriété que la note lui prête (« 204 sources relues ligne à ligne, aucun défaut »), et il servira pour la version corrigée.

À faire :

- pour toute entrée « repris d'une pièce scellée » ou « lu dans le code » dont la valeur est un nombre, une chaîne courte ou une liste, exiger que la valeur, sérialisée, figure dans l'extrait d'au moins une source ; pour une source JSON, lire la clé et comparer ;
- exiger que la révision soit égale à l'extrait de T0.7, l. 1057 ;
- ajouter les artefacts « valeur changée, extrait inchangé », au moins pour la révision, la température, la tolérance, les couches, le lot et le noyau (R5) ;
- nuancer en conséquence la phrase du verdict de la note.

**C2 — Aucun relevé de référence (classe A ; importante).** Les six valeurs de l'opérateur s'écrivent dans « un relevé par poste », et le programme compare deux relevés entre eux (`--comparer`). Rien ne dit lequel fait foi. Deux postes qui dériveraient ensemble (même tokeniseur d'une autre révision locale, même jinja2 changé) passeraient la comparaison.

À écrire dans le fichier :

- un seul relevé de référence : celui du poste de calage, établi avant le jeu des huit épisodes de référence et scellé avec eux ;
- les champs n° 1 et 2 du banc et le préenregistrement de G1 citent l'empreinte du fichier **et** celle de ce relevé ;
- tout autre relevé (banc, campagne de G1, changement de machine) se compare au relevé de référence ;
- un relevé de référence absent ou non scellé : la course ne part pas.

Sans cela, « le gabarit et son empreinte », que demande le mot du directeur, ne sont fixés nulle part.

**C3 — Type des activations conservées (classe A ; importante pour la cohérence avec T0.7).** La vérification de concordance (épreuve 2) et l'échangeabilité supposent que le banc et le calage conservent les activations au même type. Les sondes de T0.7 ont été ajustées sur des activations rangées en float16 (T0.7, l. 1057 ; `t06/lanceur_v2.py:68-80`). La conversion du bfloat16 au float16 est exacte presque partout, mais pas pour les très petites valeurs, et la garde du lanceur de T0.6 refuse les grandes.

À écrire dans le fichier :

- une entrée « type des activations conservées » : égal des deux côtés et déclaré au manifeste ;
- toute conversion (en demi-précision, par exemple) faite à l'identique, par une fonction gelée, de chaque côté ;
- le précédent de T0.7 dit dans la note ;
- savoir si les moniteurs gelés liront du float16 ou du float32 relève du scellement 3 et du préenregistrement de G1, pas de ce fichier ; mais l'égalité entre le banc et le calage, elle, en relève.

Si l'auteur du banc garde le float32 et que G1 veut le type de T0.7, c'est un nœud ; pas avant.

## 6. Mineurs (errata permis)

- **m1.** Porter le brouillon 14 du banc (`4489d399…`, commit `5182b602c`) dans les sources et dans le § 4 de la note, aux lignes neuves (§ 4 ci-dessus).
- **m2.** `CUBLAS_WORKSPACE_CONFIG` vaut « :4096:8 (ou :16:8) ». Fixer une seule valeur, « :4096:8 », celle que le harnais pose par défaut : l'identité entre postes la demande.
- **m3.** jinja2 rend le gabarit, et le relevé le compare entre postes (`EGAUX_ENTRE_POSTES`). Il n'est pas figé dans les dépendances ni nommé dans `pile_d_inference.versions`. Le nommer, au moins comme « relevé, égal des deux côtés ».
- **m4.** Les fichiers des fonctions de montage ne sont pas gelés : `lancer_pilote_a.py` (jetons d'arrêt, l. 265), `pilote_a.py` (graines), `manifeste.py`, `validation_reelle.py` (noyau), `premier_test_ia/conditions.py`. Les vecteurs d'essai et le relevé couvrent les graines et les jetons d'arrêt, d'où un mineur. Les geler coûte peu, ou bien la contre-lecture du lanceur doit le rapprocher d'eux.
- **m5.** La rubrique « pieces_lues_sans_etre_sources » doit ajouter la contre-lecture des trois choix (erratum 1, § 2), et le lanceur de T0.6 si C3 est retenue.

## 7. Les nœuds de la note

- **Nœud 1 (identité exigée, ou concordance « en loi »)** : juste. Il ajoute une étape au verdict de concordance du banc, dans une pièce de classe A d'un autre auteur, et il fixe un seuil : c'est au directeur. La recommandation (a) se défend sur deux postes identiques, sous des réglages déterministes. Une réserve : même tenue sur les huit épisodes, l'identité ne dit rien de l'effet de la composition des lots pendant la course elle-même. La note le dit (§ 6).
- **Nœud 2 (lot)** : juste, et bien vu (`episode.py:12`). Mesurer l'effet du lot sur le poste de calage avant de trancher (§ 6 de la note) me paraît la condition de la recommandation (a), pas un ajout facultatif.
- **Nœud 3 (lieu de lecture)** : juste ; c'est l'écart le plus lourd. Les chiffres de N-019 sont exacts. Je partage la recommandation (a).
- **Nœud 4 (poste et carte)** : juste. C'est une dépense, donc un devis. Le domaine revalidé est bien l'A100 de 80 Go (`revalider_pilote_a.py:436` ; P3, l. 352).
- **Aucun nœud de plus aujourd'hui.** C2 et C3 sont des corrections d'écriture ; C3 ne devient un nœud que si les textes du banc et de G1 ne s'accordent pas sur le type.
