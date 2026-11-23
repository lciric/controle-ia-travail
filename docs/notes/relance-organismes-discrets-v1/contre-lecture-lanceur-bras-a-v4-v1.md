# Contre-lecture du lanceur de la course du bras A, version 4 — agent neuf

- **Date (UTC)** : 2026-11-23. Relecteur : agent neuf (Claude Sonnet 5.5), qui n'a écrit ni le lanceur, ni les essais, ni la note. Processeur seul, aucun réseau hors git, aucune dépense. Cloisonnement tenu (rien sous `registres/`, `runs/`, `bases/`, `sondes/`, `t07*`, `docs/sources/`, etc. ; le registre des GO n'a pas été ouvert : la ligne de GO m'a été donnée à la lettre par la session).
- **Lu** : `src/controle_ia/organismes_discrets/lanceur_bras_a_v4.py` (`5409a50eb732cccae9c725f75a337ec40450d7ddefcf8172974cb5353cf3541c`, recalculée, égale) ; `tests/test_lanceur_bras_a_v4.py` (`eb5de2ed997d66c5b844ae9ee9a742d5b43c6509bea92728d1458db1d509cf3c`) ; la note (`c892f1455d5f3913a9f86d90fedb5a7e1181d73b95c2ec0f01026b048c1d93a0`) ; la contre-lecture de la v3 ; la v3 (comparée par `diff` : seuls les points annoncés changent) ; `.claude/hooks/garde_calcul.py` (lignes de GO et de révocation seulement). Le texte scellé du programme n'a pas été relu : les exigences ont été prises de la contre-lecture de la v3 et du libellé de la consigne.
- **Rejeu** : `PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_lanceur_bras_a_v4.py` : **141 passent** (135 s).

## Verdict : à corriger — un défaut bloquant

Les sept corrections (M-2, m-1 à m-6) sont faites, chacune avec cas sain et artefact, et tiennent à mes sondes et à mes mutants. **Mais la v4 refuse la ligne de GO réellement accordée pour la ligne 1 (GO-2026-11-22-148)** : le lanceur ne peut donc pas partir avec le GO que Lazar a donné. Sans GO neuf cette nuit, il faut une version 5 du lanceur dont seule la règle de périmètre change (R12).

## Défaut bloquant

**B-1 — La règle de périmètre introduite par m-3 refuse le GO réel** (`exiger_perimetre_de_la_ligne_1`, lignes 314 à 324 ; constante `PERIMETRE_LIGNE_1 = "ligne 1 du bras A"`, ligne 116).

*Essai par programme* (`exiger_ligne_de_go("GO-2026-11-22-148", registre_de_test, date(2026, 11, 23))`, registre de test fabriqué avec, à la lettre, la ligne donnée dans la consigne) :
- **Refus** : « périmètre 'Même mot (GO-2026-11-22-147) : bras A, ligne 1 de carte (fabrication et rejeu honnête, 128 épisodes), devis … ' ne nomme pas « ligne 1 du bras A », la ligne jouée — refusé ». Le périmètre réel dit « bras A, ligne 1 de carte » : la séquence littérale « ligne 1 du bras A » n'y est pas.
- Même ligne avec la seule séquence « ligne 1 de carte » remplacée par « ligne 1 du bras A » : acceptée. La cause est donc bien la règle de périmètre, et elle seule.
- **Autres champs de la ligne réelle** (essayés en neutralisant seulement la règle de périmètre) : type « calcul » accepté ; accordant exactement « Lazar » accepté (« Lazar-X » et « Lazar (mot) » refusés) ; plafond « 18 USD » lu 18,0 ; accord du 22 novembre, échéance du 30 novembre : acceptée le 23 novembre et le 30 novembre, refusée le 1er décembre et le 21 novembre ; échéance antérieure refusée. Huit cellules : correcte. Identifiant `GO-2026-11-22-148` : forme stricte acceptée. Aucun autre obstacle.
- Les essais de la v4 ne l'ont pas vu parce qu'ils fabriquent un GO fictif (`GO-2026-11-23-150`, périmètre « ligne 1 du bras A ») : la lettre du GO réel n'est nulle part dans les essais.

*Règle qui accepte la ligne réelle et refuse les autres lignes* (écrite et essayée hors dépôt sur le périmètre réel et 15 artefacts) : après normalisation des blancs et de la casse, exiger ensemble
1. le mot « bras a » isolé (`(?<![\w-])bras a(?![\w-])`) ;
2. « ligne 1 » isolé, ni « ligne 10 », ni « ligne 1.5 » (`(?<![\w-])ligne 1(?![\w-]|[.,]\d)`) ;
3. toute mention « ligne(s) N » du périmètre vaut « ligne 1 » au singulier (règle déjà en place) ;
4. aucun des mots « moniteur », « seconde », « bras b », « bras c ».

Résultat : acceptés — le périmètre réel ; « ligne 1 du bras A » ; « Ligne  1 du Bras A (devis v5, carte) » ; « lecture : ligne 1 du bras A ; plafond 18 USD ». Refusés — « ligne 2 de carte » (périmètre réel modifié), « lignes 1 et 2 de carte » (pluriel), « … ligne 1 et ligne 2 de carte », le périmètre réel suivi de « ligne 2 », « moniteurs » à la place de la ligne, « bras B » à la place de « bras A », « ligne 2 du bras A », « ligne 10 du bras A », « ligne 1 du bras B », « lignes 1 et 2 du bras A », « ligne 1 du bras A et ligne 2 du bras A », « ligne 1.5 du bras A », « seconde ligne du bras A », « course du bras A », « ligne 1 du bras AB ». Aucun faux accord, aucun faux refus sur ces 19 cas. Variante plus étroite, si Lazar préfère : exiger la séquence « bras a, ligne 1 de carte » à la lettre, plus le point 3 ; elle accepte le GO réel et refuse tout le reste de la liste, mais elle refuse aussi les formulations « ligne 1 du bras A » déjà éprouvées.

*Correction demandée* : lanceur v5 (nom neuf, R12), seul `exiger_perimetre_de_la_ligne_1` changé ; essais : le périmètre réel de GO-148, à la lettre, comme cas sain, au niveau de `exiger_ligne_de_go` **et** du constat ; les quinze artefacts ci-dessus comme refus ; la note de v4 (« Ce qui reste », point 2 : « écrire la ligne de GO avec le périmètre ligne 1 du bras A ») est à retirer, puisque le GO accordé ne peut plus être réécrit.

## Défauts mineurs

**m-A — Note périmée sur la garde de calcul.** La note (« Garde de calcul (M-1) » et « Ce qui reste », point 1) dit que la copie de la garde sur cette branche n'a pas la correction à trois chiffres. Sur cette branche, `.claude/hooks/garde_calcul.py` porte déjà `\d{2,3}` aux deux motifs (lignes 53 et 54 ; dernier commit `f1e0e541f`, « alignée sur la branche principale »). À rectifier dans la note de la v5. Sous-réserve notée : la garde de calcul cherche l'identifiant révoqué par simple inclusion (`i in r["perimetre"]`), le lanceur par bornes ; plus strict côté lanceur, sans effet néfaste.

**m-B — Le compteur n'est lié au constat que par son plafond et son taux** (`exiger_constat_et_compteur`, lignes 533 à 541). Sont refusés : plafond au-dessus de 18, taux sous carte + stockage (essais et mutants tués). Non contrôlés : l'horloge du compteur (un `CompteurDePlafond(18, 1.38, 0.0, horloge=lambda: 0.0)` ne coupe jamais : essayé, `exiger_sous_plafond` rend 0,0) et les frais fixes du téléchargement. C'est une limite de la liaison choisie (on ne peut pas prouver qu'une horloge est la vraie) ; à dire dans la note, et la commande de la session doit passer `time.time` (le défaut). Aucune correction de code exigée.

**m-C — Le constat atteste l'intégrité, pas l'âge ni l'origine.** Son empreinte se recalcule sans secret : un appelant peut fabriquer un constat cohérent. Et `jouer_ligne_1` ne relit ni l'horloge, ni le registre des GO : un constat de la veille, d'un GO échu ou révoqué depuis, serait joué. La note le dit (« le constat fait foi ») ; c'est un choix déclaré, mais la session doit produire le constat au départ même, et la garde de calcul reste la barrière au lancement de l'instance. Facultatif : refuser un constat plus vieux que quelques heures par rapport à l'horloge à l'appel de `jouer_ligne_1`.

**m-D — Strictesse sur toutes les lignes `| GO-` du registre réel, non éprouvée par moi.** `_cellules_du_registre` arrête sur toute ligne qui commence par `| GO-` si son identifiant n'a pas la forme stricte (`\d{2,3}`) ou si elle n'a pas huit cellules. C'est voulu (R5), mais un seul identifiant ancien ou une ligne à cellules en trop dans le registre réel bloquerait le départ. Je n'ai pas le droit d'ouvrir le registre : la session doit faire passer `exiger_ligne_de_go` sur le registre réel (celui de la branche principale) avant le départ, une fois B-1 corrigé. La révocation est lue comme la garde de calcul : type exactement « révocation » en minuscules ; « Révocation » avec majuscule ne révoque rien (essayé), identique à la garde.

## Vérification des corrections

| point | cas sain | artefact (sondes miennes + essais) | mutants miens sur copie en mémoire |
|---|---|---|---|
| **M-2** constat et compteur | constat sain, compteur aux bornes (plafond 18, taux = carte + stockage), compteur plus serré | constat absent, clé retirée, altéré sans nouvelle empreinte, autre ligne, autre configuration, autre lanceur, plafond du constat, GO sous 18, périmètre d'une autre ligne, crédit 19, tarif au-dessus, horloge d'un autre jour, horloge illisible ; compteur à 1000 ou 18,0001 USD, taux 0,01 ou 1,2332, compteur absent ; configuration fictive : tous refusés, aucun lot joué, dossier vide | tués : compteur sans contrôle du taux, du plafond ; constat sans contrôle d'empreinte ; appel de `exiger_constat_et_compteur` supprimé ; périmètre, tarif, crédit retirés du recontrôle ; comparaison d'empreintes de configuration ; entropie fictive |
| **m-1** inventaire | `['a']` avec manifeste et compagnon à la racine hors inventaire | homonyme du manifeste et de son compagnon dans un sous-dossier : refusé ; `manifeste-du-versement.json.bak` : inventorié | tués : filtre par nom ; refus de l'homonyme supprimé |
| **m-2** écriture | dictionnaire simple écrit | ensemble, NaN, infini, clés de types mêlés : refusés en `GardeArret`, **aucun fichier créé** (liste du dossier : `['ok.json']`) ; fichier existant refusé | tués : `allow_nan` retiré ; exception gardée remplacée |
| **m-3** GO | `-148` (trois chiffres), forme à deux chiffres | `…-1480`, `…-1`, date du 30 février, saut de ligne, minuscules, blanc initial ; révocation à trois chiffres reconnue ; ligne mal formée ou sans espace après la barre : arrêt, jamais sautée ; accordant « Lazar-X » ou « Lazar (mot) » refusé ; échéance atteinte le jour même acceptée | tués : accordant par `startswith` |
| **m-4** tarif | relevé du jour avant ou à l'instant de départ ; minuit exact ; heure locale +02 dont le jour UTC est le bon | veille 23:59:59, une seconde après le départ, 30 février, sans « Z », horloge sans fuseau : refusés | tués : jour UTC non comparé ; relevé postérieur non refusé |
| **m-5** essais | les essais listés dans la note passent (N = 2, lot 4, 512 jetons ; motifs acceptation et lecture distincts ; témoin bénin ; plafond exact ; coupe à 256 ; rejeu réel sur le jouet) | — | tués : coupe `>=` au lieu de `>` ; plafond `>=` au lieu de `>` |
| **m-6** dose reçue | demandée pour les doses et le témoin bénin sur 128 épisodes | refusée sans champ ou à un autre effectif ; jamais sur le témoin identité ni sur les jumeaux (lecture du code : `fabriquer_les_six` la demande, `fabriquer_jumeaux_de_verification` non) | tués : garde de la dose reçue retirée ; calcul rendu inconditionnel |

Limite : `fabriquer_jumeaux_de_verification` pourrait recevoir `dose_recue=True` sans refus (128 épisodes aussi) ; il ne la passe pas, et le défaut est faux. Sans conséquence.

Mutants (20 en tout, exécutés par un module chargé en mémoire sous son nom réel, rien muté sur disque, essais pertinents seulement ; un témoin non muté passe) : **tous tués**. Cela confirme mes lectures, sans prétendre refaire les 78 du rédacteur.

## Suite proposée

1. Version 5 du lanceur : règle de périmètre ci-dessus, essais sur la lettre du GO-148, note rectifiée (m-A, B-1, point 2 de « ce qui reste »).
2. Contre-lecture courte de la v5, centrée sur la règle de périmètre.
3. Avant le départ : faire passer `exiger_ligne_de_go` sur le registre réel (m-D) ; citer l'empreinte de la v5 dans la configuration du lanceur ; garde de calcul à l'empreinte de la branche principale.
