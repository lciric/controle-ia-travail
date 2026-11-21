# Manifeste de l'exécutant de la relance de l'étage 2 de la ligne 3 — v1

Exécutant neuf, sous GO-2026-11-20-68. Texte qui fait foi : mot de relance v2, `prereg/organisme-auto-conception-v9/mot-de-relance-etage-2-ligne-3-v2.md` au commit 86f585f1acc97060804ead758178226696a4bc79, extrait dans ce dossier, empreinte 324158cacd4ec14b6512802f836ae25b7287bbc74ecd39372c19bdfdfed815a2 (égale au compagnon). Interpréteur de l'outil : Python 3.13.18.

## Pas 1 (vérifications), 2026-11-21 vers 09:54Z
- Mot de relance v2 : 324158ca… conforme au compagnon. Mot de départ v2 (même commit) : c89ec85b244d4b3e82e82acb0dd16b24feec75dc81cc5be9d755c2cd28faea79, conforme au compagnon.
- Additif 6 v2, sur disque : e2afc7b987ab64dfc270c6c20d49ef5e0d8eaf603ffb2f647a0ea0dee6ca4f01, conforme.
- Pièce de scellement de la banque : absente de l'arbre local (HEAD 1ad2459b, plus ancien) ; extraite du commit 86f585f1 : c91c4d338c4a524595df96c45711e0b6094e07afa438d30bc6f79b6ce78856d7, conforme ; ligne BANQUE-ETAGE-2-LIGNE-3-V1 présente au registre des scellements du même commit, même empreinte.
- Banque, sur disque : 70d35e5479802ba355ac218e23a93b4f1dc4e29fffe82dfabef5fb5b78394bbd, conforme.
- Déclaration v2 : 5617d47adf71d0b4e3c2197b5211aeea63ecc5fa2673ec8a792331dd78c69664, conforme ; compagnon posé et égal ; identifiants de processus 23274 (Claude) et 23457 (Argon) dans le texte.
- Code d'appel v4, sur disque : 082d19d61922dbecd64d64435d8a8682f9e01abee6735ff01c6cc550c8f5484c, conforme.
- Programme de contrôle du mandataire, sur disque : 60523f210e40c20709188f048a567a7eb14053b6e75ade9cdb919d7bbb04bd39, conforme.
- Relais vivants : `stat -c %n /proc/23274` → /proc/23274 ; `stat -c %n /proc/23457` → /proc/23457.

## Pas 2 (relevé du relais Claude avant lancement), 2026-11-21T09:55:15Z
Fichier `releve-relais-claude-avant-lancement-v1.json` : dépense 0,0 USD, 0 appel, 0 refus, plafond 88,36, restant 88,36.

## Pas 3 (contrôle du mandataire)
Code 0 ; décision « tenu » (HTTPS_PROXY non vide, NO_PROXY et no_proxy couvrent 127.0.0.1).

## Pas 4
`git -C /home/user/controle-ia-travail fetch origin main` fait juste avant le geste 9.

## Pas 5 (geste 9, détaché)
- Lanceur : `/home/user/journaux-etage-2-relance-v2/lanceur-geste-9-relance-v2.sh`, empreinte d5989b20110ee41c2c2cd6d6e299120c207bf3c4f2e4f0e8ab26d253c67bee4b, compagnon posé. Commande du pas 5 du mot de relance contenue à la lettre (vérifié par recherche de chaîne exacte de la ligne 30 du mot).
- Lancé par `bash` du lanceur ; heure relevée 2026-11-21T09:55:57Z (création du processus 09:55:55Z).
- Identifiant : 30833 (`/home/user/journaux-etage-2-relance-v2/identifiant-geste-9-relance-v2.txt`).
- Preuve : `stat` → /proc/30833 ; ligne de commande (`cmdline-30833.bin` dans ce dossier) : `/usr/local/bin/python3 -I -B …/code-appel-v4/epreuve_juges_reels_ligne_3_v4.py` et les arguments du mot de relance, identiques.
- Journal : `/home/user/journaux-etage-2-relance-v2/journal-geste-9-relance-v2.log` (vide au lancement, attendu : une seule ligne en fin).
- Contrôle de vie juste après : relais Claude à 2 appels, 0,050297 USD, 0 refus.

## Reste
Relevé à mi-course (pas 6), fin (pas 7 : ligne, code, relevé puis arrêt des relais 23274 et 23457 par identifiant, preuve par stat, verdicts de la moitié « lecture » scellés non ouverts) : sur le message de la mère.
