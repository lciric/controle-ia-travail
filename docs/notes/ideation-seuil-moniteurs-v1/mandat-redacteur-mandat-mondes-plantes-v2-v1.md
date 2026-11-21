VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `grep -r`, NI JOKER. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS UN CHEMIN COMPLET DE TON DOSSIER, SUR `origin/main`, APRÈS `git -C /home/user/controle-ia-travail-organisme fetch origin main`.

# Mandat du rédacteur — mandat des mondes plantés v2 et devis v2 (course « seuil et moniteurs ») — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-21 sur le mot de la mère (08:12Z) : « le mandat des mondes v2 avec les 22 remplacements et les trois retouches du devis, puis vérification par le même contre-lecteur ». **Aucun appel, aucune dépense.**

## Qui

Un rédacteur neuf (modèle F). Tu n'as écrit ni le mandat v1 ni sa contre-lecture. Tu signes « rédacteur du mandat des mondes plantés v2, modèle F ». Aucun nom de modèle ni de fournisseur dans tes pièces : les rôles se disent par relais ou par lignée.

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Sur le disque de `/home/user/controle-ia-travail-organisme` (branche de l'organisme) :
- `docs/notes/ideation-seuil-moniteurs-v1/mandat-mondes-plantes-v1/` : le mandat v1 (`6774507c…`), le devis v1 (`4f5dca99…`), son programme et sa sortie, le rapport v1, la table ;
- `docs/notes/ideation-seuil-moniteurs-v1/mandat-mondes-plantes-v1/contre-lecture-v1/` : la contre-lecture (`9ea0ab89…`, verdict « À corriger »), le jeu de 22 remplacements (`73c642b4…`), l'essai sur copie (`58a69c74…`) et son journal ;
- la conception v5 et v6 de la course (`docs/notes/ideation-seuil-moniteurs-v1/conception-v5/`, `conception-v6/`) : sur la règle de la mère « vérité exacte et témoins, la pièce la plus stricte gagne », la v5 et la v6 gagnent ; aucune correction ne va vers elles.

Sur `origin/main` : `scripts/remplacer_texte_exact_v1.py` (`391db990…`), l'outil de remplacement à ancres comptées ; `registres/decisions.md` et `registres/go.md` (R-4436 et suivantes) ; tes copies de lecture sont exclues du versement.

## Ce que tu fais

1. **Mandat v2** (`mandat-auteur-mondes-plantes-seuil-et-moniteurs-v2.md`). Juge chacun des 22 remplacements : tu les adoptes, ou tu en corriges la lettre, en le disant. La pièce est la tienne : tu ne recopies pas l'essai sans l'avoir lu et jugé point par point. Tu appliques ton jeu final par l'outil, avec l'interpréteur `python3 -B`, sur une copie du v1 ; si ton jeu est égal à celui du contre-lecteur, ta sortie doit être égale à l'octet à l'essai (`cmp`). Les quatre défauts de fond (T09 inversé ; T08, T12 et T13 sans sort unique ; « notre calcul scellé » ; « non contre-lue ») et l'alignement sur la v5 (vérité exacte, ce qui écarte un monde, C, D, E et G, témoins du monde M, H « échangeables », `portee_de_la_garantie`, familles libres réduites à deux au plus, tailles 200, 300 et 400, T07) doivent être tous portés.
2. **Devis v2 et programme v2** (`devis-auteur-mondes-plantes-v2.md`, `calcul_devis_auteur_mondes_plantes_v2.py` et sa sortie, jouée deux fois, `cmp` muet), avec les trois retouches : la taille du mandat v2 dans le calcul ; le premier essai au deuxième relais au plafond de relance, 32 000 jetons de sortie ; dans la ligne de GO demandée, une exception écrite à la phrase « aucune dépense avant ce scellement » du scellement `4286bf39…`.
3. **Rapport v2** (`rapport-redacteur-mandat-mondes-plantes-v2.md`) : D-M11 à D-M15 closes par les mots de la mère ; D-L2 mise à jour pour N4 ; une ligne de calendrier pour le programme de vérification de la sortie, à écrire **avant l'envoi**, et pour le programme scellé qui calcule la vérité des dix-sept témoins imposés **avant la lecture de la sortie** ; les décisions restantes au format (décision en une phrase ; enjeu ; options ; recommandation et confiance ; aucun défaut pour une dépense).
4. Un différentiel v1 → v2 de chaque pièce ; une table d'empreintes ; un compagnon par fichier (`env -C DOSSIER sha256sum F`, redirigé par `>` vers `DOSSIER/F.sha256`).

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-mandat-mondes-plantes-v2/`.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense. Aucune écriture dans un dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`, aucune branche de quarantaine ou de matière première ouverte, aucune source de la liste scellée. Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucun identifiant de modèle. Aucune recette d'attaque. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
