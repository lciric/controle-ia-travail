# Corrections de l'addendum v3 de relance de R1 après la concordance de conv-audit sur le brouillon 2 — v1

- Rédacteur : sous-agent de rédaction de session-depot (Opus 5.5). Seul le texte est corrigé : aucun code, script ni
  configuration ; aucun commit ; aucun `.sha256` créé ni modifié ; aucun `git fetch` ; aucune branche `calcul/…` lue ;
  aucun réseau ni appel de modèle ; rien sous `donnees/` ; aucune pièce de P3 ouverte.
- Arbre : `wt-relance-v3`, branche `prep/r1-relance-v3`, tête `49d29c8e`.
- Brouillon relu : `prereg/R1-addendum-relance-v3.md`, brouillon 2,
  `86c68b0ec323cfdce1a6a21d1fcee14ed8d0647f485906eb031e7ee6ac32746d`. Empreinte vérifiée par `sha256sum` avant toute
  modification ; égale à l'objet du commit `49d29c8e`.
- Concordance appliquée, lue en entier : `concordance-addendum-r1-v3-brouillon2-v1.md`, dans le dossier de travail de
  session-depot (`concordances-n391/`), `8482b4cd39348104e80187b1470001f71fc6d857fc75344a32529b6dd37ade0b` (vérifiée).
- Brouillon 3 (même nom, non scellé) : `6035374fa95ef2119f501dc0d41652bbd3c79d20f8ce51bb0fe78490f336768d`, 565 lignes.
  Différence exacte : `corrections-apres-concordance-v1.patch` (`git diff -- prereg/R1-addendum-relance-v3.md`).
- Dates (UTC, relevées par `date -u`) : texte 2026-11-03 00:23 ; cette note à partir de 00:26.
- `prereg.problemes` sur le brouillon 3 : `['section vide ou à remplir : Contre-lecture']`. C'est le seul marqueur
  « À REMPLIR », celui du traitement final, laissé pour session-depot. Sur une copie hors de l'arbre où ce marqueur est
  remplacé : `[]`.
- Les quatre libellés lus par le script (« Tests attendus », chemins de la configuration, de la table et du parent)
  apparaissent une fois chacun sous la forme lue (`grep -c "<libellé> : \`"`).

## Tableau des corrections (lignes du brouillon 2 → lignes du brouillon 3)

| Point | Lignes | Ce qui est écrit |
|---|---|---|
| C-1 | 17 → 18 (en-tête, GO) | Inchangé. C'est la citation du GO-2026-11-02-27, « fiche de réception scellée avant la récupération », dont ce texte suit désormais la lettre partout. |
| C-1 | 130 → 131 (E8) | (d) « lancement » : la fiche est retirée des conditions de création, et le texte ajoute « la fiche de réception de conv-audit n'est **pas** une condition de la création ». (e) ajouté : « **récupération** : pas de récupération des sorties de la course par session-depot (étape 3 du plan) avant que la **fiche de réception de conv-audit** soit scellée (son document de contrôles, distinct des fiches JSON de ses deux analyses scellées, écrites après le versement ; GO-2026-11-02-27) ». Colonne « Changement » : « fiche de réception de conv-audit ajoutée, scellée avant la récupération (e), non avant la création ». |
| C-1, C-7 | 140 → 141 (E18) | « procédure v2 de la v1, `procedure-relance-r1-v2.md`, `ae1ff089…`, étape 7 ; la branche source y est remplacée aux **deux** endroits, la refspec du `git fetch` et `R`, par `calcul/r1-relance-v3-reel-v1`, ou par `calcul/r1-relance-v3-reel-v2` après une reprise E21 ; étape 3 du plan ». Puis : « la fiche de réception de conv-audit est scellée avant la récupération des sorties de la course par session-depot (E8 (e) ; GO-2026-11-02-27), puis conv-audit récupère `calcul/r1-r2-reel-v1` selon cette fiche ». |
| C-1 | 272-274 → 285-289 (étape 1) | La fiche sort de la liste ordonnée des conditions du lancement. Phrase ajoutée : « **La fiche de réception de conv-audit n'est pas une condition du lancement** : ce document de contrôles de conv-audit, distinct des fiches JSON de ses deux analyses scellées (écrites après le versement), est scellé **avant la récupération des sorties de la course par session-depot** (étape 3 ; E8 (e) ; GO-2026-11-02-27) ». |
| C-1, C-7 | 346-351 → 361-372 (étape 3) | « Après la destruction, et seulement une fois scellée la fiche de réception de conv-audit (avant la récupération des sorties de la course par session-depot ; E8 (e) ; GO-2026-11-02-27) : le run relancé […] est récupéré par session-depot et versé à l'octet sur `calcul/r1-r2-reel-v1` ». Pour la procédure : chemin, empreinte `ae1ff089…` en entier, « inchangée depuis le brouillon 4 de la v1 (`72f68fea`), sans compagnon `.sha256` (R6) ». La branche source est remplacée « aux **deux** endroits, la refspec du `git fetch` (ligne 238) et `R` (ligne 242) : `calcul/r1-relance-v3-reel-v1`, soit `R=origin/calcul/r1-relance-v3-reel-v1`, ou `calcul/r1-relance-v3-reel-v2` après une reprise E21 ; une branche source non remplacée arrête l'étape sur « rien à verser » ». Fin : « le commit est donné à conv-audit, qui récupère `calcul/r1-r2-reel-v1` selon cette fiche ». |
| C-1 | 453-457 → 475-480 (« Liste d'arrêt », lancement) | « la fiche de réception de conv-audit scellée » est retirée des conditions de création. Ajout : « la fiche de réception de conv-audit n'est pas une condition de la création (voir « Récupération » ci-dessous) ». |
| C-1 | après 480 → 504-506 (« Liste d'arrêt ») | Ligne ajoutée après « Reprise : seulement selon E21. » : « Récupération (étape 3 du plan) : aucune récupération des sorties de la course par session-depot avant que la fiche de réception de conv-audit soit scellée (son document de contrôles, distinct des fiches JSON de ses deux analyses scellées, écrites après le versement ; GO-2026-11-02-27). » Elle est placée hors des puces, car « Dans tous ces cas » (journal poussé, arrêt de l'instance) ne s'y applique pas. |
| C-2 | 152-153 → 153-155 | « Les objets G3 à G7, G9 et G10 sont ceux du brouillon 1 de la v2 […], retirés de la v2 scellée ; G8 (ligne 116 du brouillon 1) est resté dans la v2 scellée (ligne 172). » |
| C-3 | 182-184 → 193-198 (réserve sur HG-2) | « les 93 manquées l'ont toutes été par la durée : 91 par le budget d'étape de 2 400 s (90 non tentées, 1 coupée pendant son repli à l'échéance de l'étape) et 2 par le budget d'épisode de 600 s (coupées pendant leur repli) ». Source citée : « `64fab1a5…`, lignes 11, 69 et 201 ». Les lignes 197-198 sont re-coupées sans autre changement de mots. |
| C-4 (et point 2) | 161-164 → 163-171 | Empreinte du fichier en entier (`3d9237a5…`), « sans compagnon `.sha256`, inchangé au commit cité, dans `CIBLES` ». G10 est cité exactement : « la docstring et le nom de l'essai sont à corriger dans le code du rejeu v3, ou déclarés à nouveau dans le complément ». Puis « **déclarés ici à nouveau**, non renommés (concordance de conv-audit sur le brouillon 2, point 2 : la déclaration suffit) ». Le texte nomme les deux chaînes : « le nom de la fonction (ligne 134) et la docstring du fichier (ligne 4 : « règle B (actions des épisodes non conformes à `fidele` = faux, verdict du run « conforme ») ») ». Et l'assertion : « l'assertion (lignes 173 à 177) éprouve la voie retenue, `fidele` tranché par la tolérance ». |
| C-5 | 134 → 135 (E12, colonne « Raison ») | « code « R2 seul », paquet `controle_ia.analyse_principale_r1_r2` de la branche `canal/conv-audit-n04` : `constantes_v3.COMMANDE_REJEU`, `entrees_v3.verifier_arret_r1`, n° 339 ». |
| C-6 | 170 → 177-181 | Après « Rien d'autre n'est renvoyé par ces lignes. » : « Elles portent aussi quatre engagements sur ce texte (v2, lignes 179 à 181), tous tenus ». Les quatre : la table v3 est citée (en-tête) ; le résultat scellé du rejeu à graine est cité (« Documents qui font foi » : `8e6a4912…`, `67482545…`) ; la configuration v5 cite la même table (E11) ; la concordance porte sur la différence avec le brouillon 3 de la v1 (étape 1). |
| C-8 | 143 → 144 (E21) | « si ce journal porte `etape=fidelite lecture=…` ou `etape=controle_negatif lecture=…`, ces lectures sont rapportées à côté de celles de la reprise, et une lecture différente est rapportée comme réserve d'instrument, sans choisir entre les deux courses (symétrie, R4 ; même entropie, donc mêmes graines : seul un calcul non déterministe pourrait les faire différer) ». |
| C-9 | 368-369 → 389-391 (« R4 ») | « l'analyse secondaire de conv-audit ne lit pas le rejeu de R4 (fiche `R4` nulle ou `R4.activations` nul, au choix de conv-audit ; son script de réception v1 écrit `R4: null` ; n° 343) ». |
| E16 (point 3) | 138 → 139 | Phrase ajoutée là où E16 est déclaré : « **la réserve tient** : ni les deux analyses scellées de conv-audit ni son script de réception ne lisent `tokenisation.addendum` (concordance de conv-audit sur le brouillon 2, point 3), la clé est donc sans effet sur toute lecture ». |
| Contre-lecture | 503 → 529 ; 517-518 → 543-565 | « Corrections apportées dans ce brouillon 2 » devient « dans le brouillon 2 ». Entrée ajoutée sous « Contre-lecture 1 » : « Concordance de conv-audit (`8482b4cd…` en entier) sur le brouillon 2 (`86c68b0e…` en entier) : concordant si C-1 est corrigé », puis une ligne par correction, C-1 à C-9, et une pour E16. Le traitement final garde son marqueur : « (relecture des corrections des brouillons 2 et 3, empreinte du brouillon à sceller, refus éventuels et pourquoi) : À REMPLIR (au scellement) ». |
| En-tête | 3-8 → 3-9 | « **brouillon 3 (texte, non scellé)** : brouillon 2 (`86c68b0e…`, commit `49d29c8e`) corrigé selon la concordance de conv-audit sur le brouillon 2 (C-1 à C-9 […]) ». Date : « 2026-11-03 00:23 (brouillon 3 ; heure relevée par `date -u`) ». |

## Vérifications faites avant d'écrire

- **C-1.**
  - Toutes les occurrences, cherchées dans le texte entier : « avant la création » en E8 (d) (l. 130) et dans la liste
    d'arrêt (l. 455-456) ; « avant la récupération » aux l. 17, 140, 272-273 et 351. Ce sont les six endroits cités
    par la concordance ; il n'y en a pas d'autre.
  - Après correction, il reste trois « avant la création » : la négation « non avant la création » (E8, colonne
    « Changement ») ; E21, où l'annonce de la reprise se fait avant la création ; « Coût et GO », où les dépenses sont
    à revérifier avant la création. Aucun ne porte sur la fiche.
  - GO-27 : `git show f1791003:registres/go.md`, l. 215 : « fiche de réception scellée avant la récupération ».
  - Modèle de la fiche : la fiche du rejeu à graine (`1193a54a…`, `origin/canal/conv-audit-n04`, l. 3) a été
    « écrite et scellée par conv-audit […] à 16:45 UTC […], **avant toute récupération et toute lecture** de la sortie ».
  - Procédure de réception de conv-audit (`d85bd5e4…`, même branche) : l'étape C (récupération de
    `calcul/r1-r2-reel-v1`) précède l'étape D, où sont écrites les fiches JSON. Celles-ci sont donc écrites après le
    versement.
- **C-2.** Brouillon 1 de la v2 (`git show 21a6e583:…`, `7915a3d6…` vérifiée) : G3 à G10 aux l. 111 à 118, dont G8 à
  la l. 116. V2 scellée (`9d17d640…`, compagnon conforme) : G8 à la l. 172 ; « Renvoyé à l'addendum v3 » aux
  l. 175-183.
- **C-3.** Verdict `64fab1a5854deba0ad669d0c4840b6736e9cb680a22928d548c63093bb273e68` (empreinte vérifiée ; copie
  `contre-lecture-relance-v3/verdict-rejeu-graine-v1.md` du dossier de travail) :
  - l. 11 : « 90 non tentés, parce que le budget de l'étape (2 400 s) était épuisé […] ; 3 coupés pendant leur repli » ;
  - l. 69 : l'épisode 56 « a duré 363,86 s […] Il a été coupé par l'échéance de l'étape » ;
  - l. 201 : « 3 coupés pendant le repli (deux au budget d'épisode de 600 s, un à l'échéance de l'étape) ».
  - D'où 90 + 1 = 91 par le budget d'étape, et 2 par le budget d'épisode : 91 + 2 = 93.
- **C-4.**
  - `sha256sum tests/test_runs_nuit_v2.py` =
    `3d9237a5cc1b3de5025ca08f21781addabb56323f256394835b4e781cfec2daf` : elle commence bien par `3d9237a5`.
  - Même empreinte à `f921fcec` et à `49d29c8e` ; dernier commit qui touche le fichier : `5e678b5b` ; pas de compagnon.
  - l. 4 : « règle B (actions des épisodes non conformes à `fidele` = faux, verdict du run « conforme ») ».
  - l. 134 : `def test_relance_regle_b_non_resolus_fidele_faux_et_seuil`.
  - l. 173 à 177 : le commentaire de la voie retenue (n° 343), puis `tol`, `attendu` et
    `assert (z["fidele"][b] == attendu).all() and z["fidele"][b].all()`.
  - Docstring de la fonction (l. 135 à 137) : elle porte sur le tirage du jeu jouet.
  - G10 exact : brouillon 1 de la v2, l. 118.
- **C-5.**
  - `src/controle_ia/analyse_principale_r1_r2/` **n'existe pas dans l'arbre**.
  - Le nom exact a été vérifié sur la référence locale `origin/canal/conv-audit-n04` (`7175bf0c…`, sans `fetch`) :
    `constantes_v3.py`, l. 29 : `COMMANDE_REJEU` ; `entrees_v3.py`, l. 55 : `def verifier_arret_r1`.
  - Le paquet existe aussi au commit de code de l'analyse principale, `a8b7fdb2` (modules v1 et v2 seulement).
  - G6 du brouillon 1 de la v2 (l. 114) le nomme de même, avec la branche `canal/conv-audit-n04`.
- **C-6.**
  - V2, l. 179-181 : les quatre engagements.
  - Configuration v5 lue (clés seulement) : 29 clés ; `chemin_table_tokenisation` =
    `prereg/R1-table-tokenisation-v3.json` ; `table_tokenisation_sha256` = `ead8a668…`.
  - En-tête du texte : table (chemin, empreinte) ; résultats scellés `8e6a4912…` et `67482545…`.
  - Étape 1 : concordance sur la différence avec le brouillon 3 de la v1.
- **C-7.** `docs/notes/runs-r1-r2-r4-v1/procedure-relance-r1-v2.md` =
  `ae1ff08983f2220133cbc7745cbeb6a66a75bda622320e78779287b0fef5dd3b`.
  - Empreinte identique à `72f68fea` (brouillon 4 de la v1), `c2a8b6e1`, `f921fcec` et `49d29c8e` ; aucun compagnon
    `.sha256`. C'est l'empreinte que cite aussi la contre-lecture 1 (§ 7, l. 100) ; elle désigne cette procédure.
  - Étape 7 : l. 238, refspec du `git fetch` sur `calcul/r1-relance-reel-v1` ; l. 242,
    `R=origin/calcul/r1-relance-reel-v1` ; l. 246, `test -s … || { echo "rien à verser : arrêt"; exit 1; }`.
- **C-8.** Le module v3 écrit `etape=fidelite lecture=…` (l. 395) et `etape=controle_negatif lecture=…` (l. 405).
  - L'échantillon de fidélité est tiré par `generateur(manifeste["graines"]["fidelite"])` (l. 345).
  - `manifeste.graines` (l. 37 à 48) dérive chaque graine de l'entropie et du seul nom de la tâche, jamais de
    l'identifiant du run. Même entropie, donc mêmes graines.
- **C-9.** Script des fiches de conv-audit v1 (`ecrire_fiches_reception_v1.py`, `6836016f…`,
  `origin/canal/conv-audit-n04`), l. 235 : `"R4": None` dans la fiche de la secondaire, donc `R4: null` dans le JSON.
- **E16.**
  - Constante : module v3, l. 66 (`ADDENDUM = "prereg/R1-addendum-relance-v2.md"`), écrite à la l. 454.
  - `git grep -e tokenisation -e addendum` sur les paquets entiers, aux commits de code des deux analyses : aucune
    occurrence. Cela vaut pour `controle_ia.analyse_principale_r1_r2` à `a8b7fdb2` et pour
    `controle_ia.analyse_blanche_noire` à `326601cf`.
  - Le script des fiches v1 lit seulement `tokenisation.episodes_non_resolus` et `tokenisation.table_sha256`.
    `addendum_v2` y est un paramètre de la ligne de commande, pas une lecture du résultat.
- **Clés et jetons.** Aucune clé dans le texte (`grep` sur `hf_`, `ghp_`, `github_pat`, `token=` : rien). Aucun
  marqueur de gabarit `<<…>>`.

## Ce que je n'ai pas pu vérifier, et pourquoi

- **Les textes scellés des deux analyses de conv-audit** (`8e267952…`, `1f6a6da2…`) : leurs commits de scellement
  (`83ce7a91`, `7a238666`) sont absents des objets locaux, et le `fetch` est interdit. Leurs numéros de ligne (fiches
  JSON aux l. 97 et 139, selon la concordance) ne sont donc **pas cités** dans le texte. L'affirmation d'E16 a été
  vérifiée sur leur code, aux commits cités par la concordance, et non sur ces textes.
- **Le paquet `controle_ia.analyse_principale_r1_r2`** : absent de l'arbre. Vérifié sur la référence locale
  `origin/canal/conv-audit-n04`, qui peut être en retard sur le dépôt distant (aucun `fetch`).
- **Le comportement réel de l'étape 7** (« rien à verser ») et de **l'égalité des graines** sous une reprise : lus dans
  le code et la procédure, non exécutés.
- **La copie du verdict `64fab1a5…`** est hors du dépôt, dans le dossier de travail. Son empreinte, elle, est vérifiée.

## Réserves (pour le traitement final de session-depot)

- **C-1, choix de la récupération visée.** La concordance demande « avant la récupération », sans dire de qui. Le texte
  écrit, selon la consigne de session-depot, « avant la récupération des sorties de la course par session-depot » :
  - c'est la première récupération, à l'étape 3 (le `git fetch` de l'étape 7 de la procédure) ;
  - la fiche est donc scellée a fortiori avant la récupération de `calcul/r1-r2-reel-v1` par conv-audit ;
  - c'est conforme à la fiche du rejeu à graine (« avant toute récupération et toute lecture »).

  Le texte pose donc à session-depot une attente : ne rien récupérer avant d'avoir le scellement de la fiche de
  conv-audit. Il ne dit pas comment session-depot l'apprend (chemin et empreinte communiqués par conv-audit, par
  exemple). La concordance n'ajoute pas ce point, et je n'ai rien inventé.
- **Non corrigé, hors de la concordance.** E16 (l. 139) dit « champ `prereg` du manifeste ». Or `manifeste.py` écrit
  la clé `preenregistrement` (l. 104 ; `chemin`, `sha256`), et c'est ce nom qu'emploient l'étape 3 du texte et la
  concordance (§ 6). C'est une imprécision de forme ; à décider par session-depot.
- **Retouches de cohérence apportées hors des points C.** Dans « Contre-lecture » :
  - « dans ce brouillon 2 » devient « dans le brouillon 2 » ;
  - le libellé du traitement final devient « relecture des corrections des brouillons 2 et 3, empreinte du brouillon à
    sceller », marqueur conservé.

  Ce sont des suites du passage au brouillon 3. S'y ajoute la re-coupure des l. 197-198 (réserve sur HG-2).
- Les deux fichiers de cette note n'ont pas de compagnon `.sha256` (interdit au rédacteur) : ils sont à sceller par
  session-depot.

## Empreintes (sha256sum, après écriture)

- `6035374fa95ef2119f501dc0d41652bbd3c79d20f8ce51bb0fe78490f336768d  prereg/R1-addendum-relance-v3.md`
- `00054c236794d0d0ec2296bd01b9701b37d4502d56eaa10f9d71ff44ff175faf  docs/notes/runs-r1-r2-r4-v1/relance-v3/corrections-apres-concordance-v1.patch`
- Cette note : empreinte relevée par session-depot (elle ne peut pas se citer elle-même).

## Complément de session-depot (après le rendu du rédacteur)

- Hors concordance, signalé par le rédacteur : E16 nommait « le champ `prereg` du manifeste » ; la clé réelle du manifeste de run est `preenregistrement` (`src/controle_ia/manifeste.py` l. 104, sous-clés `chemin` et `sha256`). Une seule occurrence corrigée, texte seul, décision de session-depot ; déclarée à conv-audit avec la différence.
