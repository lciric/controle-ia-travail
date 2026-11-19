# Rapport du rédacteur — ligne 3 des épreuves v9 (votes effectifs des juges croisés, mesurés sur témoins plantés), version 7 du préenregistrement (erratum) — v1

- Auteur : rédacteur neuf, modèle F. Je n'ai écrit aucune des versions 1 à 6.
- Heure (`date -u`) : 2026-11-19, de 22:35 (première heure relevée) à 22:40. Processeur seul ; aucun appel de modèle, aucune dépense, aucune écriture dans le dépôt, aucun commit, aucune poussée. Réseau : un `git fetch origin main` et des `git show` seulement.
- Mandat : `mandat-redacteur-ligne-3-v7-v1.md`, `70568050074f1ec4fc0be614317452b6d0bd8b7cdc815b6949e65c45c57234da`, vérifié avant de commencer. Donné sur GO-2026-11-19-81 (ligne présente dans `registres/go.md` sur main au commit `79da594ce55fb0f9941be082b02f3a7c01136838`, `1570ae2b65621e490b1a07dae69b9829320896410944b24c67bba9e1c20c5faa`).
- La mère a accepté les quatre corrections (mot vers 22:28Z) : je ne l'ai lu que par la session qui m'a lancé ; pas d'autre source écrite.
- **Aucune commande sur un chemin sous `archives-reponses-modeles/`** : ni ouverture, ni empreinte, ni liste, ni taille. Aucune carte ouverte. Aucun outil n'a refusé.
- Pièce de travail, classe C. Ce rapport ne peut pas porter sa propre empreinte.

## Fichiers rendus (bloc-notes seulement)

| fichier | empreinte sha256 |
|---|---|
| `preenregistrement-ligne-3-votes-effectifs-juges-v7.md` | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` |
| `differentiel-preenregistrement-ligne-3-v6-v7.diff` (`diff -U0`, 12 morceaux) | `ef9ab82fb6a245306dd41978931729aa1b60ebcbc1537bd8c77a3873ff12791a` |
| `devis-ligne-3-etage-payant-v7.md` (voir « Écart ») | `382ea448db3ba8f5d69df1f3566165d1028ad8aceddfc8c538c522b838f58270` |
| `differentiel-devis-ligne-3-v6-v7.diff` (`diff -U0`, 4 morceaux) | `4861ef69a171fc92b64841f3055ab736c16afd9e5d3760a25dc0730d2fef3a61` |
| `outils/appliquer_v7.py` (programme) | `fc2fb615d3b3db71e0cd3366e1a7a5f2451c986463119b4ad807d83ca11c2c8d` |
| `outils/tenue_v7.py` (textes de tenue de version, lus par le programme) | `405884433557a5f4a74bd9fb9ed0ddc455cb5192aefbe5508aeee7bfde398571` |

**Comment la version 7 est faite.** Par remplacements exacts sur la version 6 (`b040d24cbef61a2a61ca724b097e6857d3465bba4d21f16d2cffc0241220ab94`), jamais par récriture. Le programme vérifie les empreintes de la vérification, de la version 6 et du devis v6, tire du § 10 de la vérification (`cbaf44de72b3dff7bd133be33a288a6a171776e72b94fc194f866faa05e8f9c1`) les textes anciens et neufs des quatre corrections, sans recopie à la main, cherche chaque texte ancien dans la version 6 d'origine, s'arrête sans rien écrire s'il n'y figure pas une fois et une seule ou si deux zones se chevauchent, puis contrôle que chaque texte neuf figure une fois et une seule dans la version 7. Passé au premier lancement : 7 remplacements de correction, 17 de tenue. La version 6 du dossier est intacte.

## Les quatre corrections, à la lettre, sans écart

1. **(3) Sortie — liste fermée entière.** Fin de la liste du (3) remplacée par le texte donné ; à l'annexe A, « écart déclaré au manifeste et au rapport de la garde ».
2. **Repli sous la condition (4).** Phrase donnée ajoutée à la fin de la puce « Repli », après « et d'ici là la garde ne tourne pas. ».
3. **Journal des rejeux absent ou illisible.** Phrases données ajoutées au (5) ; artefact donné ajouté à la ligne « recouvrement » de la liste d'arrêt.
4. **Provenance des mots de la mère.** Texte donné à l'en-tête (R-3917, R-3934, commit, empreinte) ; au (4), source remplacée par le renvoi au mandat de la version 6. J'ai relu `registres/decisions.md` sur main au commit `79da594ce55fb0f9941be082b02f3a7c01136838` : empreinte `8cd3e08cb59c290fe4b9990be54ce9abdb63f82f939139d2ee4e980b3b85a0a8` recalculée égale ; R-3917 (15:39:45Z, quatre conditions) et R-3934 (16:44:40Z, cinquième condition, repli compris) y sont, avec le contenu que la correction leur prête.

## La tenue de version

Titre ; statut (version 7, remplace la version 6, phrase de la version 6 mise au passé, vérification sur ce seul différentiel) ; auteur ; heures ; « cette version 6 » devenu « la version 6 » au mandat ; mandat de la version 7 cité (puce neuve) ; vérification de la version 6 citée comme faite (puce neuve aux documents, paragraphe à « Contre-lecture ») ; empreintes recalculées dites ; renvoi au devis v7 ; « non lus » ; vérificateur de la version 7 nommé au (4) ; ordre des gestes, (1) ; à « Contre-lecture », table des quatre corrections, « Version 7, à vérifier » (interdit en tête), demande de la version 6 gardée pour mémoire ; section « Différentiel avec la version 6 » (18 lignes). Rien au fond : aucun montant, aucun appel, aucune hypothèse, aucune règle de lecture.

## Écart, à trancher par la mère

- **Un devis v7 est écrit.** Le devis v6 nomme le préenregistrement par son fichier (statut) et par sa version (§ 7, point 1) : le mandat prévoit ce cas. Le devis v7 ne change que cela : titre, statut (version, fichier du préenregistrement, « remplace le devis v6 », une phrase), § 7 point 1, différentiel de cinq lignes. Aucun chiffre. La vérification disait « le devis v6 tel quel ». Si la mère garde le devis v6, une seule phrase de l'en-tête du préenregistrement v7 (ligne « Devis de l'étage payant ») et deux lignes de ses tables sont à reprendre : c'est alors une version neuve du texte, non un geste de versement.
- Aucun autre écart.

## Ce que je n'ai pas fait, ce qui reste ouvert

- Empreintes recalculées : version 6 du texte et du devis, rapport et mandat de la version 6, vérification de la version 6, mandat de la version 7, `registres/decisions.md` et `registres/go.md` au commit nommé. Toutes les autres sont reprises de la version 6. L'empreinte `ba65c411…` du fichier des cartes reste reprise des versions 1 à 5.
- Aucun calcul rejoué.
- Les deux lectures à confirmer par la mère (ce qui compte pour un rejeu ; comment l'empreinte se prend par le code de la banque) restent écrites telles quelles.
- Les compagnons `.sha256` ne sont pas écrits : la session les pose au versement.
- La version 7 doit être vérifiée sur son différentiel par un agent neuf du modèle O, sans commande sous `archives-reponses-modeles/`, avant scellement.
- Vu sans y toucher : un dossier non suivi par git sous `epreuves-v9/heritage/palier-0b/` (autre ligne).

## Décisions neuves pour Lazar

Aucune.
