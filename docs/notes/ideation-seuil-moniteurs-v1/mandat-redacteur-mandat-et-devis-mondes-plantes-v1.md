VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `grep -r`, NI JOKER. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS UN CHEMIN COMPLET DE TON DOSSIER, SUR `origin/main`, APRÈS `git -C /home/user/controle-ia-travail-organisme fetch origin main`.

# Mandat du rédacteur — mandat de l'auteur des mondes plantés et son devis (course « seuil et moniteurs ») — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-21, sur le mot de la mère (07:43Z) : « Oui, prépare le mandat des mondes plantés et son devis : auteur de la troisième lignée (ni expérimentateur ni traducteur), un modèle du deuxième ou du troisième relais, donc appel payant sur devis et ligne de GO ; le mandat cite la note de conception générale (4f3ae86f…, témoins plantés d'abord, vérité jamais sur la machine jetable, issue calculée chez la mère), la note du moniteur de dissonance pour son monde à K actions (sur devis à part) et le registre servi des visées (3bcb94e6…) pour les familles de scores à loi connue. Les mondes sont scellés avant toute mise en fiches et avant toute course. Rien ne part sans le mot de Lazar. »

**Tu écris deux pièces de préparation. Aucun appel, aucune dépense.**

## Qui

Un rédacteur neuf (modèle F). Tu n'as écrit aucune pièce de la course « seuil et moniteurs ». Tu signes « rédacteur du mandat des mondes plantés, modèle F ». Aucun nom de modèle ni de fournisseur dans tes pièces : les rôles se disent par relais (« deuxième relais », « troisième relais ») ou par lignée (« troisième lignée »).

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Sur `origin/main` :
- la note de conception générale des expérimentateurs et des tests de mort : `docs/notes/experimentateurs-et-tests-de-mort-v1/conception-branchement-experimentateurs-tests-de-mort-v1.md` (`4f3ae86f…`), § 0, § 2.2, § 4.3 et § 6 en particulier, avec ses calculs ;
- la note du moniteur de dissonance : `docs/notes/papier-dopamine-moniteur-v1/moniteur-dissonance-v1/conception-moniteur-dissonance-et-audit-v1.md` (`403fe3e2…`), pour son monde à K actions, qui est sur devis à part ;
- le registre servi des visées : `docs/notes/mathematiques-nouvelles-v1/consultation-externe-v1/registre-servi-visees-v1.json` (`3bcb94e6…`), noms neutres et énoncés d'une ligne seulement. **N'ouvre aucune branche de matière première ni de quarantaine** ;
- `registres/go.md` et `registres/decisions.md` (GO-2026-11-21-16, R-4377, R-4399, R-4410, R-4412 et suivantes) ; tes copies de lecture sont exclues du versement.

Sur la branche de l'organisme (disque de `/home/user/controle-ia-travail-organisme`) :
- la conception v4 de la course : `docs/notes/ideation-seuil-moniteurs-v1/conception-v4/`, ordre (`390af604…`) et préenregistrement (`b0e907a7…`) : § 7 de l'ordre (mondes, morts, mesures), D-M4 et D-M9 (lignées) ;
- le devis v3 (`docs/notes/ideation-seuil-moniteurs-v1/conception-v3/devis-course-seuil-et-moniteurs-v3.md`, `a057cf25…`) et le complément de valeurs v3 de la course « nouvelles attaques » (sur `origin/main`), pour la forme des parts par relais et des comptes payants.

## Ce que tu écris

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-mandat-mondes-plantes/`.

1. **`mandat-auteur-mondes-plantes-seuil-et-moniteurs-v1.md`**, le mandat qu'un modèle de la troisième lignée recevra par son relais. Il porte :
   - ce qu'il écrit : les familles de mondes à lois plantées, leurs paramètres, leurs tranches et leur vérité connue ;
   - la forme fixe de sortie, lisible par programme ;
   - les témoins plantés, écrits d'abord ;
   - la famille tenue à l'écart ;
   - la table monde → supposition cassée ;
   - ce qu'il ne fait pas : aucun critère de mort, aucune lecture des textes sources ni des fiches, aucune vérité placée sur la machine jetable ;
   - comment sa sortie est vérifiée par programme ;
   - le scellement par la mère, avant toute mise en fiches et avant toute course.

   La requête est servie telle quelle : tout ce qui part vers le relais est écrit dans ce mandat. Le monde à K actions est cité comme « sur devis à part ».
2. **`devis-auteur-mondes-plantes-v1.md`**, avec un programme de calcul `calcul_devis_auteur_mondes_plantes_v1.py` (arithmétique seule, entrées sourcées) et sa sortie, jouée deux fois et comparée à l'octet. Il porte :
   - les cas bas, haut et pire, par relais candidat ;
   - le plafond d'arrêt ;
   - la ligne de GO à demander ;
   - le nombre d'essais permis en cas de refus ou de sortie illisible.

   Les tarifs sont pris aux pièces scellées qui les donnent ; un tarif non écrit est dit « à relever ».
3. **`rapport-redacteur-mandat-mondes-plantes-v1.md`** :
   - les pièces lues avec leurs empreintes ;
   - ce que la lettre ne fixe pas, en remarque ;
   - les décisions pour la mère et pour Lazar, au format : décision en une phrase ; enjeu ; options ; recommandation et confiance ; aucun défaut pour une dépense ;
   - le choix du relais (deuxième ou troisième), avec ses raisons.
4. Une table d'empreintes. Chaque fichier a son compagnon (`env -C DOSSIER sha256sum F`, redirigé par `>` vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense. Aucune écriture dans un dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`, aucune branche de quarantaine ou de matière première ouverte. Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucune publication. Aucun identifiant de modèle. Aucune recette d'attaque. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
