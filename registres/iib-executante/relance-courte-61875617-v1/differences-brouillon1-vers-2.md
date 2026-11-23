# Différences : texte de relance courte de 61875617, brouillon 1 vers brouillon 2 (une ligne par correction de la contre-lecture 1)

- B1.1 : le code de sortie de `vastai logs` est lu ; un code non nul, un fichier vide ou un masquage en échec rendent le relevé « illisible », sans tri.
- B1.2 : trois relevés illisibles de suite → arrêt par l'identifiant (essai j7).
- B1.3 : l'état est relevé à chaque tour ; statut `running` vu sans ligne « DEMARRAGE 2 » 60 s après → arrêt (essai j8) ; les 900 s ne valent plus que pour l'attente de la mise en marche.
- B1.4 : un relevé toutes les 5 s au lieu de 10.
- B1.5 : essais j7 et j8 ajoutés et joués ; tous les essais rejoués sur le script exact (`essais-blanc-relance-courte-v1.txt`).
- M1 : le motif « poussée : tentative » est retiré du tri, donc plus d'arrêt à la première tentative refusée ; l'ordre est poussée faite, poussée impossible, refus, chemins puis calcul inattendus ; essais d3 réécrits et j9 et j10 ajoutés ; liste d'arrêt et N2 accordées.
- M2 : préalable P10 ajouté (latence d'arrêt mesurée à la coupure de 12:54Z ; au-delà de 90 s, mot de Lazar) et nœud N7.
- M3 : aucun changement de méthode (le contre-lecteur confirme qu'il n'y a pas de moyen plus sûr).
- m1 : `mkdir "$D2"` sans `-p` avant P2, refus s'il existe.
- m2 : les essais passent `VAST` (faux outil) et `D2` (dossier propre à l'essai) explicites ; le faux outil refuse `destroy` et tout autre identifiant.
- m3 : dans le § 7, les traces et l'inventaire sont limités aux chemins ajoutés (`diff-name-status.txt`).
- m4 : dans le § 7, l'interprète est celui de la session (`$DEPOT/.venv/bin/python`, sinon `python3`), avec `PYTHONPATH` du clone.
- m5 : l'inventaire brut est réduit par le lecteur, ou supprimé s'il échoue (dans `etat()` et P2).
- m6 : P7 dit de quel jeton il s'agit (celui de la session, source de `GH_TOKEN` à la création) et quand c'est le même.
- Forme : en-tête « classe B », décisions GO-2026-11-22-44 et risque de destruction accepté par la mère inscrits (N1, N2, P1, compte rendu).
- Forme : le script n'est plus recopié dans le texte ; il vit dans `relance-courte-61875617-v1.sh` (empreinte en tête), et `secrets` devient une sous-commande.
- Défaut trouvé par le rédacteur aux essais : le code de retour de `jouer` ne disait pas l'arrêt non confirmé (`RC` propagé : 1 si non confirmé, essai j6).
