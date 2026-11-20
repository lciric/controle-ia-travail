# Rapport du rédacteur — additif de code de la mesure « portée à 200 » de la ligne 3 — v1

Pièce de travail (classe C). Écrit le 2026-11-20 (11:15Z relevée), sur le mandat `mandat-redacteur-additif-5-code-racines-portee-200-v1.md` (`8a669690ac1c43b46d0c6bae9b02ce208783a9bd2b397b557de0ca7399d0d291`, égale à son compagnon). Pièce rendue : `additif-5-code-preenregistrement-ligne-3-portee-200-v1.md`, avec son compagnon, dans le dossier du mandat (bloc-notes). Règle d'aveugle tenue : aucune mesure de l'étage 1 ouverte, ni ses dossiers d'exécution et de verdict. Aucun programme lancé, aucune graine dérivée, aucune écriture dans le dépôt, aucun commit.

## 1. Ce qui est nommé

- **Le code** : dossier `LIGNE/code-portee-200-v4/` ; commit du versement `af19ff8dbb0e1c990f7bb97f7e5a77a332dca14c` (branche `lot/compte-organisme-v1`) ; quatorze fichiers avec leur empreinte, en trois tables (les deux programmes exécutés : banc v4 `79865552…`, chronométrage `6b9d2cbf…` ; essais, contrôle, deux rapports de défauts, quatre différentiels ; quatre copies du v3). Chaque empreinte recalculée, égale à son compagnon et au rapport du développeur ; pour les quatorze fichiers, `git hash-object` sur disque égal à `git rev-parse af19ff8d:chemin`.
- **Les racines** : 2026112031 (chronométrage, clés 2 et 12), 2026112032 (clé 2), 2026112033 (clé 12), `.spawn(210)`, et elles seules ; toutes les autres refusées.
- **Les deux commandes**, complétées : dossier du code, chemin absolu de l'additif, deux dossiers de sortie, `PYTHONDONTWRITEBYTECODE=1`, variables de chemin non posées, ordre, une fois chacun, échéance 2026-11-30.
- **L'interpréteur** : `python3` (`/usr/local/bin/python3`, Python 3.13.18), numpy 2.5.3.
- **Le dossier du code commité entièrement**, et la réserve du `.gitignore`.

## 2. Les blancs laissés à la mère

1. Le commit de `main` qui portera le dossier du code recopié (§ 2 de l'additif).
2. `HEX`, l'empreinte du compagnon de l'additif scellé (§ 4).

Aucun autre blanc.

## 3. Remarques

1. **Nom et rang.** Le nom du fichier et le rang « 5 » sont ceux du mandat, à confirmer par la mère. `CHEMIN` est écrit dans l'additif sous `prereg/organisme-auto-conception-v9/` avec ce nom (absent du disque à 11:15Z) : si le nom ou le lieu de scellement change, il faut une version neuve, car `CHEMIN` est dans le texte.
2. **Interpréteur.** Proposé : `python3`, numpy 2.5.3, parce que c'est la lettre du gabarit de l'additif 3 (§ 5) et de l'additif 2 (§ 6), que les 157 essais passent sous les deux interpréteurs, et que l'additif 2 relève 2.5.3 pour l'étage 1 (même version pour la comparaison cellule par cellule de l'audit de symétrie). La version 2.5.3 est celle de la contre-lecture ; je ne l'ai pas relevée (aucun code en ligne permis). L'additif 3 n'impose aucune version précise de numpy : l'additif de code nomme la version attendue en remarque et renvoie à la mère le cas d'un manifeste qui en porterait une autre ; il n'en fait pas une règle.
3. **Dossiers de sortie.** Je les ai placés sous `LIGNE/execution-portee-200-v1/` (`chronometrage` et `mesure`), parent absent du disque à 11:15Z. Ni l'additif 3 ni le mandat ne fixent leur lieu ; à la mère de dire s'il convient. Les programmes créent le dossier et ses parents et refusent un dossier présent.
4. **Les deux `-u` de `env`** (retrait de `BANC_LIGNE_3_CHEMIN` et `CHRONOMETRAGE_LIGNE_3_CHEMIN`) sont un ajout aux commandes du développeur : ils disent dans la commande la condition « non posées ». À retirer si le contre-lecteur préfère la lettre nue ; le code refuse de toute façon une variable posée.
5. **Contenu du dossier du code.** Sans commande de liste, je n'ai pas pu vérifier que le dossier ne contient que les quatorze fichiers et leurs compagnons, ni lire `.gitignore`. La mère le contrôle en recopiant le dossier sur `main` (un fichier non suivi fait refuser la garde ; un fichier ignoré la passe).
6. **Chemin de bout en bout.** La contre-lecture du code note que le chemin hors essai avec une autorisation juste n'a jamais été exécuté (il dériverait) : le chronométrage en sera la première exécution réelle.
7. Le chronométrage accepte `--repliques-echantillon` (défaut 20) : l'additif dit « aucun autre argument », donc le défaut.

## 4. Écarts au mandat

- Deux recherches de motif, chacune bornée à un seul fichier nommé (banc v4, chronométrage), pour lire les arguments, la création du dossier de sortie et le champ `versions`. Ce n'est pas une recherche large ; déclaré.
- Deux `test -e` puis deux `stat` sur un chemin complet chacun (dossier de sortie proposé, nom proposé de l'additif), pour dire « absent ». Aucune liste.
- L'empreinte entière du rapport du développeur, dont le mandat ne donne que le préfixe, est lue dans son compagnon.
- Aucun refus de permission, de classifieur ni de garde.

Rédacteur neuf, modèle F.
