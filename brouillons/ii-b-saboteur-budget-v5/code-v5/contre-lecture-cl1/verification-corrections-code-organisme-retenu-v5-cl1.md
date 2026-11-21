# Vérification des corrections du code de l'organisme retenu, version 5, pour l'étalonnage — cl1

Date : 2026-11-21. Pièce d'instrument (classe B). Même contre-lecteur (Claude Opus 5.5), même mandat (`47b53672…`). Correctif `correctifs-v2/0007-….patch` (`3075a8df…`, compagnon vérifié) appliqué par `git am` sur les six correctifs, dans le même arbre (`cl-v5-local`, jamais poussée). J'ai lu en entier le rapport du développeur v2, sa sortie d'essais et l'erratum 1 (compagnons vérifiés). Rien poussé, aucune dépense, aucune machine, aucun appel à un loueur, aucun fichier supprimé, aucun refus d'outil. Le périmètre est l'étalonnage seul.

## Verdict pour l'étalonnage

**Autorisable après deux restes :**
- **R1 (majeur, défaut de code)** : la coupe après une clé en gras fermée après les deux-points (`**COST:**`) n'est jamais conforme, alors qu'elle l'était dans la version 1.
- **R2 (majeur)** : l'amorce v5 n'a jamais été jouée, même en essai local.

S'y ajoute un risque à écrire dans l'ordre : la valeur écrite à la ligne qui suit la clé (jeton « :\n »). Tout le reste de ma première contre-lecture est levé.

## B1, M1 à M7 et mineurs : traitement vérifié

| remarque | vérifié | comment |
|---|---|---|
| B1 point d'entrée | **levé** | J'ai fait moi-même l'essai à blanc (`essai-a-blanc-v1/`, dépôt jouet construit par l'outil des essais) avec `python -m controle_ia.iib.lanceur_v5 --phase etalonnage`, puis `--phase conditions`, sans carte et sans accord. Résultats : code 0, 28 lots, 56 fichiers de lots scellés et tous vérifiés, `resume.json`, désignation scellée (issue P, 12 tours, motif de N « rapport »). Le second passage est refusé (« branches-iib-v5.json existe déjà »). Sorties : `sorties/essai-a-blanc-*`. |
| B1 chargeur v5 | levé, non exécutable ici (torch absent) | `modele_v5` lit la section neuve `modele`, vérifiée à l'égalité en mode réel avec l'agent et la révision figés, et refuse tout tirage non neutre. |
| B1 amorce v5, liste d'essais | levé sur le papier | Différences avec la v1 bornées aux six changements déclarés. Empreinte en dur de la liste (`6bc7026a…`, 21 fichiers) égale à celle du fichier. Syntaxe des deux scripts vérifiée. Voir R2. |
| M1 versement par lot | **levé** | Essai d'artefact à moi (`scripts/essai-interruption-etalonnage-v1.py`) : signal TERM après le cinquième lot. Résultat : 5 lots et 5 fichiers d'identifiants restent, scellés ; `arret.json` dit l'étape (étalonnage), le motif (signal TERM) et les 10 fichiers écrits ; aucun étalonnage final n'est écrit, donc aucune issue n'est inventée. |
| M2 marques de progrès | **levé** | Les 32 lignes `PROGRES` de mon essai à blanc ont la forme de `MOTIF_PROGRES` de l'amorce, et aucune ne porte de `MOTIF_INTERDIT`. |
| M3 première action du régénéré | levé | Copiée de l'honnête ; essai par un modèle qui ne rend jamais deux fois la même première action. |
| M6 taille d'origine | levé | Si le nombre de tours de la course dépasse le plafond, l'issue est « ne part pas », motif « tours » ; le champ fautif est retiré. Conforme au § 6 du devis. |
| M7 location | levé | Le mode réel exige toutes les sections et les bornes du devis à l'égalité. Contrôle fonctionnel à moi, `session_v5` sur le gabarit réel rempli : `variante` B, ligne de 60, conforme ; `carte` course permise ; `filtre` A100 SXM4, prix horaire au plus 1,3. |
| m1 à m8 | levés ou dits | Durée mesurée par oracle, la plus longue retenue. Dépense comptée depuis le début de l'amorce (la création elle-même n'est pas comptée : la surveillance reste la référence). Clé `iib/epreuves/tirages`. m4 déclaré. Fractions exactes pour la chaîne réécrite. m6 dit et gardé par `modele_v5`. Mode jouet refusé avec un accord ou une carte. Fichier d'entrées aux valeurs du devis (45 ; 6,90 ; 1,38). |
| M4 couplage | erratum 1 lu | Conforme à ma note ; seule la documentation de `couplage_v5` change. |

## Essais rejoués fichier par fichier (`sorties/essais-fichier-par-fichier-v2.txt`)

- Les 20 fichiers hors l'essai long, sans le tokeniseur : tout réussi, et l'essai du tokeniseur réel est sauté. Exemples : lanceur 16, configuration 26, régénéré 8.
- L'essai du tokeniseur réel, rejoué avec le tokeniseur que le développeur a téléchargé (`tokenizer.json` `79e3e522…`) : **135 réussis** (`sorties/essai-tokeniseur-reel-v1.txt`).
- L'essai long n'a pas été rejoué : le développeur l'a rejoué au commit final (10 arrêts pour N, 4 pour P sur 200).
- Toujours rien d'éprouvé sans torch : le modèle réel et `MondeReel`.

## Les deux ajouts, lus comme pièces neuves

- **`scripts/lancer_iib_v3.sh`** : c'est la version 2, intacte (déjà contre-lue), avec sept lignes changées : amorce v5, `session_v5`, pièces lues sous `pieces.`, branche `essai/iib-explo-v5`.
  - Gardes de création et de destruction inchangées. La destruction se fait par l'identifiant (`destroy instance $ID -y`, R10), refusée pour un identifiant de la liste des intouchables, avec l'étiquette exigée et le rapatriement attesté.
  - L'empreinte du module de lecture est vérifiée avant tout emploi (variable d'environnement ou configuration, égales si les deux sont présentes).
  - **Mineur n1** : la destruction lit la liste des intouchables dans l'environnement, et l'attestation `IIB_AUCUNE_INTOUCHABLE=oui` y existe encore, alors que la configuration v5 exige une liste non vide et dit que l'attestation n'existe pas. *Correction* : que v3 lise `instances_intouchables` dans la configuration et refuse l'attestation ; à défaut, l'ordre pose la liste par `environnement_du_lanceur_de_session` et interdit l'attestation.
- **`session_v5`** : seule la sous-commande `config` change (vérification par `exiger_config_v5`, prête à lancer). Tout le reste passe à `session_v1`, qui lit les sections de location telles que les fixe `exiger_location` (contrôle fonctionnel ci-dessus). Racine par défaut : celle du dépôt. Aucune remarque.
- **R2 (majeur)** : ni l'amorce v5 ni le lanceur de session v3 n'ont été joués, même à blanc. Seules les différences sont vérifiées. *Correction* : une répétition locale en mode jouet par l'amorce v5 (`ESSAI=1`) avant l'ordre, avec sa sortie versée.
- **Mineur n2** : le calendrier n'est pas vérifié contre les dates du devis scellé (dernière création le 2026-11-27T00:00Z, échéance le 30). C'est à l'ordre de le faire.

## Le constat 8 : la coupe sur le tokeniseur réel

J'ai sondé sur le tokeniseur réel des formes écrites à la main, sans aucune donnée de course (`scripts/sonde-coupe-tokeniseur-reel-v1.py`, sortie `sorties/sortie-sonde-coupe-tokeniseur-reel-v1.txt`) :
- **coupe conforme** : `COST: 4…`, `COST:4`, `**COST**: 4` ;
- **non conforme** : `COST:\n4…` (jeton `:Ċ`), `COST:\nRISK:` et `**COST:** 4` (jeton `:**`) ;
- **aucun champ de coût** : `- **COST:** $400`, puce en tête. C'est le lecteur des champs de l'environnement lui-même qui ne la reconnaît pas ; ce n'est pas propre à la version 5.

**1. Clé en gras fermée après les deux-points (`**COST:**`) : défaut de code, R1.**
- La coupe de la version 1 (`oracle_v1.coupe_du_prefixe`) admettait une coupe après les marques de gras qui ferment la clé : limite étendue à `[ \t*_]*`, fin de clé cherchée sans les marques.
- Le lecteur des champs de l'environnement reconnaît cette forme (`_FERMETURE_GRAS`). Le texte scellé, en 3.3 c, la prévoit : « Les marques de gras fermées après les deux-points restent à la clé ».
- La règle v5 (fin du préfixe exactement aux deux-points et aux espaces) est plus stricte que tout cela, et le tokeniseur réel ne laisse alors aucune coupe.
- *Correction* : reprendre la règle de la version 1, c'est-à-dire une coupe conforme si le décodage du préfixe finit par la clé suivie seulement de marques de gras fermantes et d'espaces, la fenêtre commençant après elles. `reecriture_v5.bornes_de_la_valeur` traite déjà une coupe placée après les marques. Ajouter les cas `**COST:**` à l'essai du tokeniseur réel, qui doivent rendre coupe conforme, lecture égale des deux côtés et réécriture retrouvée. C'est une lecture de « juste après COST: » qui revient à celle de la première course, pas un changement de règle.
- Sans cette correction, un modèle qui met souvent ses clés en gras fait échouer l'épreuve de la coupe.

**2. Valeur à la ligne suivante, ou clé vide (`:\n`) : risque à écrire dans l'ordre, pas un défaut de code.**
- Le texte définit la coupe « juste après COST: » sur le seul préfixe (3.2 point 2). Avec un jeton `:\n`, il n'y a pas de frontière de jeton à cet endroit. La version 1 la rejetait aussi : sa limite n'admet pas de saut de ligne.
- Ce que le texte scellé prévoit pour ce cas : l'action est comptée et n'est pas bornable. Si moins de 95 % des actions honnêtes à champ de coût ont une coupe conforme, la coupe, commune aux deux oracles, les met tous deux en défaut, et l'issue est « ne part pas » (section 9 ; 10.3, étape 2 ; section 15). C'est écrit d'avance, sans liberté.
- Indice faible, tiré du texte scellé (1.1) : sous la coupe de la version 1, qui rejetait aussi cette forme, les autres épreuves de la première course ont réussi.
- Admettre une coupe après `:\n` changerait la définition de 3.2 et l'essai de la section 13 (« valeur à la ligne qui suit la clé »). Ce serait donc un **nœud de conception**, à ne poser que si Lazar veut réduire ce risque.
- Mesurer d'abord la fréquence de cette forme sur les transcriptions honnêtes de la première course demanderait une donnée nouvelle, donc son mot.
- **Recommandation** : un risque écrit dans l'ordre (perte bornée à l'étalonnage, environ 5 dollars attendus), sans nœud ; confiance moyenne.

## Ce que l'ordre de l'étalonnage devra porter, en plus de ce que dit le § 4 du rapport du développeur

- R1 corrigé, puis vérifié par moi.
- R2 joué, avec sa sortie versée.
- Le risque de la coupe sur `:\n`.
- La liste des intouchables posée et l'attestation interdite (n1).
- Le calendrier du devis (n2).
- Le nombre d'essais attendus sur la machine, essai du tokeniseur réel sauté.
