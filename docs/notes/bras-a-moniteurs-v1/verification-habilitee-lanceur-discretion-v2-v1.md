# Vérification habilitée des corrections — lanceur de l'étape de discrétion du bras A, version 2 — v1

**Pièce habilitée, à ne pas transmettre à une session non habilitée.** Ce qui est transmissible est dans `verification-habilitee-lanceur-discretion-v2-sans-interne-v1.md`, même dossier.

Écrit par le lecteur habilité côté moniteurs (Claude Fable 5.2, le même que pour la contre-lecture `contre-lecture-habilitee-lanceur-discretion-v1.md`, `ae7618d1216f6d07f79514777ddf9193d4bbc1e873d0ed1d608ff3dbf3f215c1`), le 20 novembre 2026, sous GO-2026-11-20-21. Classe B : vérification des corrections, et d'elles seules. Copie de travail `/home/user/bras-a-habilite`, commit vérifié `848c17649d3c324461747daa99fb8784c88a8baa` ; la tête est passée à `09746e437` pendant la vérification (trois compagnons d'anciens fichiers), sans toucher une pièce vérifiée. Ni commit ni poussée. Essais et retraits joués sur des copies d'épreuve du bloc-notes.

## 1. Verdict

**Les treize corrections et les deux décisions sont faites. Une seule porte une réserve (C9), sans effet sur un calcul.** Le lanceur version 2 est conforme pour une course, sous les deux points déjà dits qui ne relèvent pas du code : essai du chemin réel sur la machine de calcul, module de graines non cité par empreinte.

| | objet | verdict | preuve |
|---|---|---|---|
| C1 | seconde reprise du même moniteur refusée | **corrigée** | le relevé de reprise s'écrit sous `production/reprises/`, plus dans le dossier des morceaux ; essai à deux pannes de suite, deux lignes de reprise |
| C2 | reprise pas toujours comptée | **corrigée** | un relevé et une ligne à toute relance après l'engagement (`deja is not None`), y compris après les deux productions ; deux essais ; retrait qui mord |
| C3 | pièce source vérifiée après les ouvertures | **corrigée** | `A.charger_piece_source(racine)` à l'étape 1 ; essai ; retrait qui mord |
| C4 | configuration de la base non comparée à sa ligne | **corrigée** | texte « après » de la contre-lecture repris à la lettre ; deux artefacts ; deux retraits qui mordent |
| C5 | quatre modules non cités | **corrigée** | les quatre chemins dans `MODULES_APPELES` et dans le gabarit v2, aux quatre empreintes recalculées ; le gabarit v2 ne diffère du v1 que par la version, le registre du bras et ces quatre lignes |
| C6 | `relever-fins` inutilisable | **corrigée** | `fins_a_relever` pour cette seule sous-commande ; les trois autres refusent la configuration de relevé ; essai ; retrait qui mord |
| C7 | énoncé bordé de blancs | **corrigée** | garde ajoutée, texte de la contre-lecture ; essai ; retrait qui mord |
| C8 | douze gardes sans artefact | **corrigée** | onze gardes ont un artefact, et leurs onze retraits mordent ; la douzième (relecture de la table par la préparation à la reprise) devient une assertion sur les octets lus, redondante avec `table_deja_engagee` dans la même exécution : admis |
| C9 | manifeste sans versions ni commit | **corrigée avec réserve** | `versions`, `code` (commit, fichiers suivis modifiés), `execution`, `determinisme` au manifeste. Réserve ci-dessous |
| C10 | fenêtre sans réparation non dite | **corrigée** | notice v2, partie 4, phrase de la contre-lecture |
| C11 | module d'entrée importé avant sa vérification | **corrigée** | `verifier_les_fichiers`, puis import, puis `verifier_les_importes` ; essai ; retrait qui mord |
| C12 | attestation : précision manquante | **corrigée** | erratum 1 : quatrième précision à la lettre, trois constantes nommées ; l'attestation n'est pas récrite |
| C13 | pièce sans interne : deux phrases | **corrigée** | version 2 : « à chaque relance […] autant de fois qu'il le faut », « treize fichiers » ; aucune fuite |
| D1 | sorties de lecture scellées morceau par morceau | **corrigée** | douze champs gardés par une forme fermée, scellés sous `production/lectures-completes-<moniteur>/`, avant le morceau ; sous identifiants opaques ; lus par la seule reprise d'un morceau non posé ; essai ; cinq retraits qui mordent |
| D2 | registre propre au bras | **corrigée** | clé `registre_du_bras`, trois registres distincts exigés ; engagement, manifestes de production et reprises y vont ; le registre des scellements garde les clés de la base et le journal des ouvertures ; essai ; retrait qui mord |

Remarque 4 de la contre-lecture (nom du manifeste à la seconde) : faite aussi, le nom porte l'identifiant de l'exécution.

## 2. La réserve sur C9

Les réglages de déterminisme ne sont versés au manifeste qu'après la boucle de production (`manifeste.contenu["determinisme"] = getattr(charger, "reglages", None)`, après le `for m in A.PRODUCTEURS`). Si la production s'arrête sur une panne, le manifeste d'arrêt porte `determinisme: null`, alors que la carte a été réglée et a lu. Si la relance n'a plus rien à charger, aucun manifeste ne les porte jamais.

Correction précise, à la prochaine version du lanceur ou avant la course : envelopper la boucle de production.

Avant :
```
    for m in A.PRODUCTEURS:
        …
    if manifeste:
        manifeste.contenu["determinisme"] = getattr(charger, "reglages", None)
```
Après :
```
    try:
        for m in A.PRODUCTEURS:
            …
    finally:
        if manifeste:
            manifeste.contenu["determinisme"] = getattr(charger, "reglages", None)
```
Aucun score, aucune garde, aucun ordre n'en dépend : je ne tiens pas la course à cette correction.

## 3. Ce que j'ai rejoué

| épreuve | résultat |
|---|---|
| empreintes des onze pièces neuves, contre leur compagnon | toutes égales |
| essais du lanceur v2 | `30 passed` |
| les trois fichiers ciblés ensemble (lanceur v2, préparation v3, module v11) | `42 passed` |
| épreuve par retrait v2, rejouée **en entier** avec le fichier d'essais final, sur une copie d'épreuve | **70 retraits mordent sur 70**, en une passe ; lanceur et préparation remis à l'identique (`c3840745…`, `c0021298…`) |
| différentiel du lanceur, de la version 1 à la version 2, lu en entier | rien d'autre que les corrections, les deux décisions et la remarque 4 |
| types rendus par la lecture du score aux deux cas | nombres flottants de Python : la forme fermée de la lecture complète ne refuse pas une lecture réelle |

Le relevé de première passe du développeur (69 sur 70) portait sur un fichier d'essais antérieur ; mon rejeu, sur le fichier final `7729f5bd…`, rend 70 sur 70 d'un seul tenant.

## 4. Demande 19 : six programmes nomment le fichier des rangs

Recompté sous `src` et `scripts` : **6**. Ce sont les versions 8, 9, 10 et 11 du module des autres moniteurs, et les versions 1 et 2 du lanceur. Le sixième vient de ce que la version 1 du lanceur reste en place (R12), non d'un programme neuf qui lirait ce fichier.

- Tous sont sous des dossiers dont le nom commence par `bras_a_v2_habilite` ; les deux lanceurs sont dans le même dossier, `bras_a_v2_habilite_lanceur`. La réponse du développeur sur la garde de l'analyse reste juste telle quelle.
- Aucun des six n'ouvre le fichier après son écriture, ni ne parcourt son dossier : la version 2 ne change rien à l'étape 6. Les dossiers neufs (`production/reprises/`, `production/lectures-completes-<moniteur>/`) sont sous le dossier de la production, disjoint de celui des rangs par la garde des dossiers.
- La version 1 du lanceur ne peut pas être jouée par mégarde sur la configuration de la course : elle refuse une configuration de version 2 (version et clés).
- Hors du compte demandé : trois fichiers d'essais (`tests/test_bras_a_v2_habilite_autres_moniteurs_v8.py`, `_v9.py`, `_v10.py`) nomment aussi ce fichier ; ils sont sous `tests/`, que la demande ne couvre pas. À dire à la relance si sa garde regarde `tests/`.

## 5. Ce qui reste, hors des corrections

1. Essai du chemin réel (chargement sur la carte, relevé des jetons de fin, module d'entrée) sur la machine de calcul, avant la course.
2. Le module de graines qu'importe le module d'entrée n'est pas cité par empreinte : à trancher par la mère.
3. La ligne `CONFIG-BRAS-A-V2` reste au registre des scellements, où la base l'exige : la question du lecteur de registre de T0.7 ne vaut plus que pour les clés de la base, qui y étaient déjà.
