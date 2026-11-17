# Rapport du second addendum de B bis (T0.7) — préparation de la décision et de la course — v1

- **Auteur** : rédacteur-développeur neuf, lettre de modèle A ; lecteur déclaré de T0.7 (exclu des lecteurs de P3-bis).
- **Heures (UTC, `date -u`)** : 2026-11-16, de 23:12:04 à la déclaration (§ 7).
- **Statut** : préparation seulement ; **rien n'est adopté** par ce travail. Aucune machine, aucun appel au loueur, aucune
  dépense ; aucun score ni aucune donnée de 7a ou de 7b ; aucun fichier existant modifié ; rien de committé. Pièces scellées
  (compagnons `.sha256`).

## 1. Verdict

1. **Second addendum rédigé** (`brouillon-second-addendum-bbis-v1.md`) : 24 fragments nommés (SA-1 à SA-24), chacun « ancien »
   unique dans son document et « nouveau » au caractère, **contrôle mécanique conforme** ; affaiblissements déclarés ;
   discriminant à double sens ; caractérisation corrigée ; mesure de dispersion entre deux ordres de calcul définie (option (ii),
   GO-2026-11-16-12), codée, éprouvée, chiffrée.
2. **Code v4 prêt à verser** (noms neufs, diff minimal) : 34 essais neufs, **34 passés** ; suite entière de B bis sur un arbre de
   la forme de l'instance : 155 passés, 18 sautés, 0 échec.
3. **Dépense** : course plus mesure ≈ 5,8 à 6,6 USD attendus, pire cas cumulé ≈ 25,8 USD ≤ 40 : **elles tiennent sous
   GO-2026-11-14-09, aucun nouveau mot de Lazar n'est requis pour la dépense**. Mais la nouvelle course reste soumise à
   GO-2026-11-16-11 et à ses conditions (contre-lecture et scellement du second addendum avant `CODE-BBIS` remplacée, code v4
   contre-lu, feu écrit).

## 2. Ce qui change, ce qui ne change pas

**Change** (détail : addendum, § 2) :
- **Contrôle carte-processeur** (SA-1, SA-4, SA-6, SA-9) : les deux familles à 3 époques (≤ 10⁻⁴), déterminisme des deux familles à
  300 époques, écart linéaire à 300 époques écrit comme information.
- **R-PILE étendue à la linéaire** (SA-2) et **point (7)** (SA-3) : R-PILE s'écrit à chaque lecture (toute sonde finale est
  linéaire ou « attention ») et porte le résumé de la mesure.
- **Mesure de dispersion entre deux ordres de calcul** (SA-10, SA-12 à SA-14, SA-17 à SA-19) : recette entière de la sonde rejouée
  sur la même carte dans l'ordre inverse des actions, scores fermés, écart des aires calculé à la lecture ; aucune issue.
- **Registre** (SA-5, SA-11, SA-15) : ligne `CODE-BBIS` remplacée une seule fois (seconde ligne après `GO-BBIS`) ; une course de
  plus, une seule, sous GO-2026-11-16-11.
- **Branche de sortie** (SA-8, SA-16) : `donnees/t07-etape-b-bis-v2` (la v1 porte la course arrêtée ; l'amorce refuse une branche
  présente).
- **Paragraphes explicatifs du premier addendum** (SA-21 à SA-24, réserve R-C) : coût du § 3, § 5 points 1, 4, 5 ; § 6 lu avec le
  second addendum (déclaré, sans fragment).
- **Dépense** (SA-20) : la course et la mesure partent sous GO-2026-11-14-09, feu portant aussi GO-2026-11-16-11.

**Ne change pas** (dits tels, addendum § 5) : hypothèse, prédiction, métrique (hors l'ajout de SA-10), seuils, niveaux (0,99 de
l'épreuve), tolérance 10⁻⁴, 256 actions, tirage du couple, graines (même entropie, aucune clé neuve), plis, grille, 300 époques et
pas 0,05 des sondes lues, plancher, nul, garde de débit (formule et 11 h ; la mesure compte dans « apprentissages restants »),
budget (40 USD, GO-2026-11-14-09), échéance, états, issues, libellés, table conjointe.

**Réserves de la contre-lecture** : R-A (caractérisation corrigée : SA-1, raison) ; R-B (discriminant : addendum § 4, et
`lecture_v3.exiger_controle_carte` le rapporte) ; R-C (liste étendue : SA-21 à SA-24 ; affaiblissements : addendum § 3) ; R-D
(tranchée par Lazar, option (ii) : SA-10, § 6) ; R-E (épreuves EC-8 révisées : SA-9 ; cas sain anisotrope : essai B3).

**Hors de la demande, et pourquoi** (à juger par le contre-lecteur) :
- `registre_bbis_v2.py` (neuf) : `registre_bbis_v1` refuse une seconde ligne `CODE-BBIS` (« déjà présente ») et toute création à
  `RELANCES` = 2 ; `lecture_v1/v2.lire_lignes` refusent une clé en double : sans v2, ni la course ni sa lecture ne passeraient.
- Branche de sortie neuve et `MIN_ESSAIS` relevé dans l'amorce v4.
- Fragments de T touchés que R-C ne nommait pas : SA-5, SA-10 à SA-20 (liste d'arrêt, plan 2, 8, 10 (d), données gardées, calcul
  et dépense).

## 3. Essais

Joués sur processeur, 4 fils, dans une copie du bloc-notes (`git archive` de `prep/t07bbis-code-v1` à `af0adb14`, plus le dossier
`code/`), environnement Python du dépôt (torch 2.14.1, numpy 2.4.6). Données fabriquées seulement.

| essai | résultat | pièce |
|---|---|---|
| fichiers neufs = précédents + couples déclarés (5) ; amorce et lanceur v4 | passés | `essais/sortie-essais-second-addendum-v1.txt` |
| B1 : le contrôle v3 arrête la carte émulée (jetons presque identiques) sans erreur de chaîne | passé (écart d'ordre 1) | idem |
| B2 : la v4 passe sur le même jeu (linéaire à 3 époques 9,2·10⁻¹², attention 9,5·10⁻¹⁰), information à 300 époques 5,31, discriminant « écart » | passé | idem |
| **B3 (R-E) : cas sain du régime anisotrope, sans quasi-copie, 300 époques divergentes (information 3,79) : la v4 passe (3 époques : 3,1·10⁻¹²)** | passé | idem |
| B4 : forme de la répétition : passe, information ≤ 10⁻⁴, discriminant « accord » | passé | idem |
| B5 à B8 : artefacts à 3 époques (7 + lot d'autres données), non-déterminisme (2 familles), sonde en échec (3), horizon | passés (arrêts) | idem |
| C : champ du contrôle v4 (sain + 14 artefacts) ; R-PILE linéaire, résumé, point (7) | passés | idem |
| D : `CODE-BBIS` remplacée (lecture, ordre, écriture) ; garde de création à `RELANCES` = 2 | passés | idem |
| E : mesure (ordre inverse joué, aucune aire, échec, erreur d'exécution, garde, clés, compte) | passés | idem |
| F : marche v4 et lecture v3 de bout en bout en mode jouet, `CODE-BBIS` remplacée | passé | idem |
| suite v3 du contrôle rejouée (`test_t07bbis_controle_v3.py`, 17 essais) ; total de la sortie : 51 passés en 4 min 31 s | passée | idem |
| suite entière de B bis, arbre sans `docs/notes` (forme de l'instance) | 155 passés, 18 sautés, 0 échec | `essais/sortie-suite-forme-instance-v1.txt` |
| contrôle mécanique des 24 fragments | conforme | `pieces/sortie-controle-fragments-second-addendum-v1.txt` |

Graine du cas anisotrope : choisie parmi six essayées parce qu'elle diverge (quatre sur six divergent ; sonde préalable gardée,
`essais/sonde-jeux-divergents-v1.py` et sa sortie) ; c'est un cas fabriqué pour diverger, déclaré comme tel.
**Minimum d'essais de l'amorce** : 148 = 115 (compte de la v3 sur l'instance, R-2957) + 33 essais neufs qui passent sans
`docs/notes` (l'essai F saute sur l'instance). La suite de forme « instance » a été jouée quand l'amorce portait 149 (erreur de
compte, corrigée à 148 avant la sortie finale) ; mon arbre simulé compte 122 passés pour l'ancien paquet au lieu de 115 : il
n'est pas exactement l'arbre partiel de l'instance ; **à recompter** sur l'arbre de l'instance simulé par les motifs de l'amorce
v4 avant le feu.

## 4. Ce qui reste avant le feu (dans l'ordre)

1. **Contre-lecture du second addendum par un lecteur neuf** (R2 ; condition de GO-2026-11-16-11) ; corrections ; **scellement**
   sous `prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md` ; ligne `ADDENDUM-ECART-2-BBIS` au registre voisin ; ligne R-.
2. **Contre-lecture du code v4** (condition de GO-2026-11-16-11), essais rejoués par le lecteur.
3. **Versement du code** par la mère (copie des fichiers de `code/` sous `src/`, `scripts/`, `tests/`, compagnons ; aucun fichier
   existant touché) ; commit ; recompte de `MIN_ESSAIS` sur l'arbre de l'instance simulé (corriger sous un nom neuf si le compte
   diffère).
4. **Fiche remplaçante de `CODE-BBIS`** (`registres/t07-etape-b-bis/code-bbis-v2.json`, par `registre_bbis_v2 fiche`) : commit du
   code versé, empreintes, **même entropie et même épreuve de niveau** que `code-bbis-v1.json` ; liste des fichiers = celle de la
   v1 plus les six fichiers neufs et les trois essais ; puis **seconde ligne `CODE-BBIS`** au registre propre (après le scellement
   de l'addendum, après `GO-BBIS`).
5. **Répétition à blanc sur carte** : **non exigée** par le texte modifié (SA-1 : la répétition exigée a été faite, quatrième
   passe). Si on la veut quand même : ≈ 0,25 à 0,5 USD, un script de répétition v4 à écrire, et un mot de Lazar sur sa ligne.
6. **Feu écrit de la mère** portant GO-2026-11-14-09 **et** GO-2026-11-16-11 ; commande `bash scripts/lancer_bbis_v4.sh commande …
   RELANCES=2` ; garde de création v2. Contraintes reprises des feux précédents : pilote de l'hôte de la série 595 ou 580 (l'amorce
   ne lit pas « CUDA UMD Version », R-3003 : bloc inchangé en v4) ; liste des témoins de `verifier-destruction` à jour (R-2957).
7. Course : relecture, apprentissage, contrôle v4, mesure, notation, poussée sur `donnees/t07-etape-b-bis-v2` ; destruction par
   identifiant, absence prouvée (R10) ; limite du samedi 21 novembre 12:00 UTC.

## 5. Gestes (pour la mère)

- Porter à Lazar, en une ligne : la dépense tient sous GO-2026-11-14-09 (aucun mot neuf requis pour elle) ; deux fichiers hors de
  la demande (`registre_bbis_v2`, branche de sortie v2) et leur raison.
- Donner au contre-lecteur la liste du § 10 de l'addendum.
- Ne pas relancer sous le texte actuel : même couple, mêmes données, même arrêt très probable (diagnostic, § 1).

## 6. Pièces (dossier `brouillons/T0.7-etape-B-bis-v1/second-addendum-v2/`, empreintes dans les compagnons)

`brouillon-second-addendum-bbis-v1.md` ; ce rapport ; `diff-v3-v4.txt` ; `code/src/controle_ia/t07bbis/` (`validation_imbriquee_v4.py`,
`marche_v4.py`, `lecture_v3.py`, `registre_bbis_v2.py`) ; `code/scripts/` (`lancer_bbis_v4.sh`, `amorce_bbis_v4.sh`) ; `code/tests/`
(`test_t07bbis_second_addendum_v1.py`, `aide_t07bbis_differentiels_v4.py`, `aide_t07bbis_jeux_v4.py`) ; `pieces/`
(contrôle des fragments, sa sortie, texte en vigueur, premier addendum lu avec le second ; programmes de rédaction des couples) ;
`essais/` (sorties des essais, sonde des jeux divergents). Le dossier partiel `second-addendum-v1/` n'a été ni lu ni employé.

## 7. Déclaration

Rôle : rédacteur-développeur neuf ; lettre de modèle : A ; lecteur de T0.7 (exclu des lecteurs de P3-bis). Heures : 2026-11-16,
de 23:12:04 à l'heure écrite en fin de `essais/sortie-essais-second-addendum-v1.txt` et dans la déclaration finale (`date -u`).
**Pièces lues, avec empreintes** : `prereg/T0.7-etape-B-bis-v1.md` (`0ae6210f…`) ; `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md`
(`f00eda8a…`) ; `diagnostic-carte-processeur-v1/rapport-diagnostic-carte-processeur-v1.md` (`1fefa0a9…`),
`contre-lecture-diagnostic-v1.md` (`0da982fb…`), `validation_imbriquee_v4.py` (`ba127aa0…`), `essai_controle_v4_v1.py`,
`essai-amplification-lineaire-v1.py` (fonction `jeu`), `contre-lecture-essai-independant-v1.py` et `-suite.py`, leur sortie
(compagnons vérifiés : 19 OK) ; code au commit `af0adb14` : `validation_imbriquee_v1.py` (`1ffb6e4d…`), `_v3.py` (`71bffa5b…`),
`marche_v3.py` (`7009b34d…`), `lecture_v2.py` (`154795f4…`), `registre_bbis_v1.py` (`c3b1848b…`), `apprentissage_carte_v1.py`
(`4b98fcb9…`), `commun_v1.py` (`9db2b40b…`), `scripts/lancer_bbis_v3.sh` (`dc26ea01…`), `scripts/amorce_bbis_v3.sh`
(`18e2f205…`), `tests/test_t07bbis_controle_v3.py`, `tests/aide_t07bbis_differentiels_v3.py` (début),
`tests/aide_t07bbis_jouet_v1.py`, `tests/test_t07bbis_apprentissage_v1.py` (`ActsJouet`) ; `registres/t07-etape-b-bis-v1.md`
(lignes) et `registres/t07-etape-b-bis/code-bbis-v1.json` (début : commit, entropie, épreuve) ; `registres/t07-etape-b-bis-v1-addenda-v1.md` ;
`registres/go.md`, lignes GO-2026-11-14-09, -16-11, -16-12 ; `registres/decisions.md`, lignes R-2957, R-3003, R-3010 à R-3031
(tronquées) ; `brouillons/T0.7-etape-B-bis-v1/devis-etape-b-bis-v3.md` (lignes de montants) ; `.claude/settings.json` et l'en-tête
de `.claude/hooks/garde_calcul.py` (motifs). **Jamais ouverts** : `relecture-bbis.json` (ni ses clés), aucun fichier de la branche
`donnees/t07-etape-b-bis-v1` (pas même les traces permises : je me suis tenu aux rapports qui les citent), aucune donnée de 7a,
7b, T0.6, de l'étape B de T0.7, de P3-bis ni du bras d'attaque ; rien sous `diag/`, `runs/`, `donnees/` ; le dossier
`second-addendum-v1/`. Ni `env`, ni `printenv`, ni `set`, ni `export -p` ; aucune valeur de clé ; aucun identifiant de modèle dans
les fichiers. **Incidents** : (1) l'essai D1 a échoué au premier jeu par une erreur de l'essai (même fichier de registre réécrit),
corrigée ; (2) l'essai F a échoué faute du dossier `docs/sources/invites-2606.08892-v1/` dans la copie, ajouté par `git archive` ;
(3) `MIN_ESSAIS` porté d'abord à 149 (erreur de compte), corrigé à 148 avant la sortie finale.
