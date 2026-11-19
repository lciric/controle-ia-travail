VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

# Mandat du développeur — code de l'étage 1 de la ligne 3, version 2 (reprise après le quatrième refus d'outil) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 23:50Z, sur GO-2026-11-19-93 (reprise avec deux mesures). Il **reprend tel quel** le mandat v1 (`mandat-developpeur-code-etage-1-ligne-3-v1.md`, même dossier, `1b6d0c7e67e9f885d357a692ff2b881257d8e24288587e4828a3b245d6eb4fbb`) : même objet, même texte scellé qui fait foi, mêmes livrables, mêmes interdits. Il ajoute seulement ce qui suit.

## Ce qui change

1. **La ligne en tête** de ce mandat vaut règle absolue : la version de Python se lit par `python3 --version`, et aucun `-c` ni `-` ne suit jamais `python3`. Aucun heredoc. Tout programme s'écrit dans un fichier et se lance par son chemin. Le développeur précédent sur ce mandat a été arrêté pour avoir glissé `python3 -I -c ""` dans une commande groupée.
2. **Pour vérifier l'environnement**, n'écris pas de commande groupée : lance le programme contre-lu du dépôt, par son chemin :
   `python3 -B scripts/verifier_environnement_agent_v1.py --modules numpy,pytest --depot /home/user/controle-ia-travail`
   (empreinte `9714a00f05b66b6f0f3c901fc700ea30b07cb3c3fda302947f276dca5fea4d74`, contre-lecture « Conforme »). Pour vérifier des empreintes, donne-lui une liste de fichiers par `--empreintes`.
3. **Pour modifier un fichier**, utilise `python3 -B scripts/remplacer_texte_exact_v1.py` (empreinte `391db990…`).
4. **Une commande simple à la fois.** Au premier refus d'un outil, arrête-toi et dis-le.
5. Ce qu'a déjà fait le développeur précédent : lu le texte scellé (`4e3680d9…`) et le calcul des prédictions v2 (sortie `2cf1eba7…`) ; il n'a rien écrit. Tu repars de zéro pour le code.
