# Corpus « cit-HepTh » de la collection de réseaux de Stanford : fiche et schéma (avant scellement du plan)

- **Objet** : résumés d'arXiv, section physique théorique des hautes énergies, pour le banc des corpus contre des modèles nuls emboîtés (boucle fermée du collisionneur groupé, GO-2026-11-24-46). Accord de la mère du 24 novembre vers 19:22Z : télécharger pour fixer l'empreinte ; avant le scellement du plan, n'en tirer que le schéma ; le concepteur ne voit que schéma et empreinte.
- **Source** : https://snap.stanford.edu/data/cit-HepTh.html (page lue le 24 novembre 2026 vers 19:28Z). Fichiers : https://snap.stanford.edu/data/cit-HepTh-abstracts.tar.gz et https://snap.stanford.edu/data/cit-HepTh-dates.txt.gz ; en-tête « Last-Modified » : 3 décembre 2009.
- **Téléchargé** : 2026-11-24 vers 19:28Z, par `curl`, sans compte.
- **Empreintes** (sha256) : `cit-HepTh-abstracts.tar.gz` (11 956 788 octets) `d4f33c10ebae1d504328e62b5232ea67ac43ebaa1bd58fda13385ae29e610026` ; `cit-HepTh-dates.txt.gz` (96 569 octets) `4b5f2259b0feb848a2a93ab3345d344a4b1c3c9c773ddebcab95f2f6e0bf6225`.
- **Hors de git** : les fichiers bruts restent sous `brut/` (le dossier `donnees/` est ignoré par git) ; seule cette fiche et son empreinte sont versées.
- **Licence** : la page de la collection n'affiche aucune licence ; elle demande de citer J. Leskovec, J. Kleinberg et C. Faloutsos, « Graphs over Time: Densification Laws, Shrinking Diameters and Possible Explanations », KDD 2005, et J. Gehrke, P. Ginsparg, J. M. Kleinberg, « Overview of the 2003 KDD Cup », SIGKDD Explorations 5(2):149-151, 2003. Données publiées pour la coupe KDD 2003. Usage de recherche interne seulement ; aucune redistribution. À trancher par la mère si une licence écrite est exigée.
- **Ce que dit la page** (non vérifié par nous au-delà du schéma ci-dessous) : 27 770 articles du graphe de citations, janvier 1993 à avril 2003.

## Schéma (seule lecture faite avant scellement)

Extraction par programme : liste de l'archive, noms des champs d'en-tête comptés par fichier, bornes de dates du fichier de dates. Aucun titre, aucun résumé, aucun mot du corps n'a été lu ni compté.

- **Archive des résumés** : 29 555 fichiers `AAAA/NNNNNNN.abs`, un par article ; identifiant arXiv ancien sans préfixe (`9201001` = année 1992, mois 01, rang 001). Par dossier d'année : 1992 : 1 367 ; 1993 : 2 058 ; 1994 : 2 377 ; 1995 : 2 303 ; 1996 : 2 606 ; 1997 : 2 673 ; 1998 : 2 758 ; 1999 : 2 803 ; 2000 : 3 126 ; 2001 : 3 153 ; 2002 : 3 312 ; 2003 : 1 019.
- **Format d'un fichier** : blocs séparés par une ligne `\\` ; 29 544 fichiers ont 4 blocs (vide, en-tête, résumé, fin), 11 en ont 5 à 7.
- **Champs d'en-tête** (nombre de fichiers qui l'ont) : `Paper` 29 555 ; `From` 29 555 ; `Date` 29 555 ; `Title` 29 555 ; `Comments` 29 240 ; `Authors` 25 165 ; `Author` 4 387 ; `Journal-ref` 21 019 ; `Report-no` 15 808 ; `Subj-class` 2 543 ; `Notes` 10 ; `Proxy` 3 ; `MSC-class` 2.
- **Fichier de dates** : 38 557 lignes `identifiant date` (date `AAAA-MM-JJ`), plus un commentaire : « cross-listed papers have ids 11<true_id> » ; bornes des dates : 1992-02-11 à 2002-03-12. Il ne couvre donc pas 2002-03 à 2003 ; l'identifiant (année et mois) et le champ `Date` de l'en-tête couvrent toute l'archive.
