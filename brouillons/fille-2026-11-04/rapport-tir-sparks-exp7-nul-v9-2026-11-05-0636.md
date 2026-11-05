# Rapport de la fille — tir réel SPARKS-EXP7-NUL v9 (2026-11-05, 06:36 UTC)

Ordre de la mère (06:22 UTC) : tir sous GO-2026-11-05-02 (plafond 5 USD), selon la section 5 de `docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v9.md`, code au commit 4d07d2a6830ab09cb91250016284efb5cbe8a91c, `SPARKS_REGISTRE_GO` = registre des GO de main.

## Verdict
**Boucle de redémarrage constatée.** Instance détruite par son identifiant ; inventaire « absente ». C'est un **nœud de Lazar** : aucune création sous ce texte.

## Déroulé
- Recherche : 4 offres retenues. Rang 1 : offre 54550274, carte 0,047362 USD/h, stockage 0,002743 USD/h. Devis du mode tir : 0,0434 USD.
- Étape 0 : commit de tir e1542f4a71481cfac894285becc094b5f8d0d746, sur la branche `essai/sparks-v9-tir-4d07d2a6830a` (poussée).
- Étape 1 : instance 59219396 créée ; T0 06:23:45 UTC. Échéance de la minuterie : 06:47:36 UTC.
- Étape 2, inventaires :
  - 06:28:52 : `exited` (cur_state `running`) ;
  - 06:31:56 : `running` (cur_state `running`) ;
  - 06:34:58 : `running` (cur_state `running`).
- Verdict du script (`boucle 59219396`) : **boucle**.
- Journal de l'amorce (`journal-amorce`, lignes « AMORCE V5 » seules) : de 06:27:17 à 06:35:02, la paire suivante revient toutes les 4 secondes environ, soit un peu plus de 110 démarrages :
  - « AMORCE V5 … : machine 59219396, commit e1542f4a… » ;
  - « AMORCE V5 : curl absent : refus, rien ne part (la minuterie en a besoin) ».
- Étape 3, branche « boucle » : `vastai destroy instance 59219396 -y` envoyé à 06:35:18 (« destroying instance 59219396. » lu). Inventaire à 06:35:22 : **absente**.
- Étapes 4 à 7 : sans objet, faute de verdict « arretee ».

## Dépense
Environ 11,6 minutes à 0,049448 USD/h (dph_total de l'inventaire), soit **environ 0,0095 USD**, sous le devis de 0,0434 USD et le plafond de 5 USD. Chiffre estimé ; le relevé de facturation Vast n'a pas été lu.

## Constats pour le développeur (rien n'est corrigé ici)
1. **Cause probable de la boucle** : l'image `pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime` n'a pas `curl`. L'amorce refuse alors de partir et sort. Vast relance le conteneur, et le refus recommence.
2. **Le compteur de `journal-amorce` est faux** : il imprime `REDEMARRAGES=0 BOUCLE_PRESUMEE=0` alors que le journal montre plus de 110 démarrages. La détection de boucle dans le journal ne voit donc pas ce cas.
3. **Le premier inventaire est trompeur** : il lisait `exited` alors que cur_state valait `running`. Avec un seul inventaire, on aurait pu conclure à tort que l'instance était arrêtée.
4. **L'amorce ne se détruit pas sur ce refus.** Elle sort, et Vast la relance : le garde-fou d'autodestruction n'a pas joué pendant les 11 minutes observées.

## Écarts et réserves
- Écart de procédure : la garde locale `.claude/hooks/garde_calcul.py` a bloqué la première création, car GO-2026-11-05-02 manquait au `registres/go.md` local. Corrigé par une avance rapide de main, puis la commande imprimée a été rejouée sans changement. Rien n'est parti avant la correction.
- Aucune sortie brute de vastai n'est versée. Le journal n'a été lu qu'à travers le filtre `journal-amorce`. La garde des secrets est à 0 sur les fichiers hors clone.
- Les instances R8 (58936096, 58936099, 58936100) **ne sont toujours pas détruites**. Leur destruction a été refusée par le classifieur de permissions ; c'est déjà signalé à la mère, et je ne l'ai pas contournée.
