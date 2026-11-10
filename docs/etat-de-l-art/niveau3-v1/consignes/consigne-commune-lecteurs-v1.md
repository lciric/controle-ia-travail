# Consigne commune des lecteurs — état de l'art, niveau 3 — v1

Écrite le 2026-11-10 vers 10:45 UTC (heure relevée par `date -u`) par la session fille « état de l'art niveau 3 ».
Chaque lecteur est un sous-agent neuf ; il lit cette consigne en entier, puis la consigne propre à son lot.

## Langue et forme

Français, phrases courtes, aucun acronyme non développé. Le rapport est un fichier Markdown, au chemin donné par la
consigne du lot. À la fin, le sceller :
`cd /home/user/controle-ia-travail && PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`.

## Règles de preuve

- **R7.** Aucun chiffre ni aucune affirmation sur un travail d'autrui sans le PDF empreinté du dépôt et la **page**
  (numérotation du fichier, page 1 = première page du PDF). Lire par `pdftotext -layout -f N -l N fichier.pdf -`.
  Chaque verdict porte : chemin du PDF, début de son empreinte sha256 (fichier compagnon `.sha256`), page, **citation
  exacte** entre guillemets (copiée du texte de la page, espaces normalisés). Une transcription, un résumé de moteur
  de recherche, un souvenir ne sont **pas opposables** : les écrire comme « piste, non vérifiée ».
- **Contrôle des citations.** Écrire un petit script (dans le dossier temporaire donné par la consigne du lot, jamais
  dans le dépôt) qui vérifie que chaque citation exacte du rapport figure bien dans le texte de la page citée (espaces
  et césures normalisés). Le tester d'abord sur un cas juste et sur un cas altéré (R5). Donner dans le rapport le
  compte : citations contrôlées, échecs.
- **R8.** Une zone vierge est une question. La limite d'un papier n'est pas un trou du champ. « Libre » veut dire « non
  trouvé dans les pièces lues », jamais « personne ne l'a fait ». Chercher la collision, pas la confirmation.
- **R4.** Un résultat trop propre, dans un sens ou dans l'autre, se signale comme réserve.
- **R11.** Avant de dire qu'un fichier manque, vérifier sur disque (`ls` du chemin exact).
- **Verdict par pièce revendiquée** : « libre (dans les pièces lues) », « occupée en partie (par qui, page) »,
  « occupée (par qui, page) ». Si une zone revendiquée paraît **occupée en entier**, ou si une collision plus large
  apparaît : l'écrire **en tête du rapport**, en gras, sous le titre « COLLISION », et le dire dans le message final.
  Ne modifier aucune hypothèse, aucune revendication, aucun document existant.

## Interdits (recopiés des interdits communs v2, `1ee3b370…`)

1. Ne jamais ouvrir, lister ni chercher dans : `diag/` ; `runs/` ; `donnees/` ; `docs/notes/bras-attaque/` ;
   `registres/index-bras-attaque*` ; `scripts/extraire_mesures_epreuve_t06_v1.py` ; tout fichier dont le nom contient
   `P3-bis`, `p3-bis` ou `p3bis` ; tout fichier de l'étiqueteur ; aucune autre branche git que la branche courante.
2. Jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ` ; aucune valeur de clé.
3. Aucun appel de modèle ni d'interface payante ; aucune machine ; aucune dépense.
4. Git : aucun `checkout`, `switch`, `reset`, `stash`, `commit`, `push`, `fetch`, `merge`, `rebase`, `add`.
   Rien n'est écrit hors des chemins de sortie nommés par la consigne du lot.
5. Ne pas lancer la suite d'essais.
6. Si un contrôle de permissions ou un classifieur refuse une action : s'arrêter sur ce point et le rapporter tel
   quel ; ni contournement, ni reformulation.
7. Toute heure écrite est relevée par `date -u`.
8. Aucune recherche récursive (`grep -r`, `rg`, `find`, motif `**`) hors des dossiers nommés par la consigne du lot.
   Pour chercher dans le dépôt : `git grep -n MOTIF -- <chemins nommés>` seulement.
9. Réseau : le conteneur refuse presque tous les hôtes (arXiv compris). Ne rien contourner. Si la consigne du lot
   permet l'outil de recherche sur le réseau, une requête ne porte **jamais** le nom du directeur, du projet, du
   dépôt ni du fonds ; ses résultats sont des pistes non opposables.

## Message final au lanceur

Chemin du rapport, empreinte sha256, verdict en une ligne par pièce, collisions, contre-résultats défavorables au
programme, pièces qu'il faudrait récupérer sur le réseau (identifiant, titre, pourquoi), tout refus rencontré.
