# Mandat du rédacteur — fiche unique des quatre décisions pour Lazar sur l'orchestrateur v68 (consigne R-3861) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 22:25Z, sur la demande de la mère (message de 15:03Z : « Prépare dans ton domaine […] la fiche unique des quatre décisions de R-3861 ») et l'ordre de file qu'elle a accepté.

## Ce que tu fais

Tu écris **une fiche de décision unique pour Lazar** (`fiche-quatre-decisions-orchestrateur-v68-v1.md`), après la contre-lecture de l'orchestrateur v68 rendue « Conforme » (`contre-lecture-orchestrateur-v68-v1.md`, `d2cfeac1…`). Quatre décisions, chacune au format de `CLAUDE.md` : décision en une phrase ; enjeu ; deux ou trois options (avantage, inconvénient) ; recommandation et confiance ; défaut sous 48 heures (ou « aucun défaut » quand c'est un nœud : dépense, activation en réel, écart à un texte scellé).

1. **Activation de chaque interrupteur** de l'orchestrateur v68 (régimes « éteint », « tests de mort sans rien servir », « lecture » ; ce que le lanceur v10 éteint fait déjà). Rien en réel sans une ligne d'accord qui nomme l'interrupteur (R-3861). Pour chaque interrupteur : ce qu'il active, ce qu'il coûte, quelle ligne de l'ordre de passage v3 il débloque.
2. **Ce qui est servi aux générations suivantes**, sous la garde « la mémoire ne sert jamais un verdict » (complément 3 de N-073). Tiens compte de ce que Lazar a déjà accordé pour l'héritage (GO-2026-11-19-76, nœud 2 : `resultat` et `gardee` servis, comme lecture de la garde ; GO-2026-11-19-81 : aux paliers payants, l'expérimentateur reçoit l'engagement seul) et dis si la décision de l'orchestrateur doit s'aligner sur elle ou rester distincte.
3. **Les champs de fiche** (prédiction, signe, métrique, test de mort) : c'est un nœud. Dis ce que cela change pour les 94 cartes de la course v9 et pour la prochaine course.
4. **Une machine jetable pour le bac réel**, sur devis : ce qu'il faut, ce qu'elle coûterait en ordre de grandeur (sans dépense ici ; tout devis se fait à part), et ce qu'on perd sans elle.

Ajoute en fin de fiche **la liste des lignes de l'ordre de passage v3 bloquées sans la v68, et de celles qui ne le sont pas**, chacune avec sa raison.

## Ce que tu lis

`CLAUDE.md` ; dans `docs/notes/organisme-auto-conception-v1/epreuves-v9/` : `orchestrateur-v68/` (rapport du développeur `ad42b722…`, manifeste du paquet, journal des essais, contre-lecture `d2cfeac1…` ; les fichiers du paquet en lecture si besoin), `rang-0-branchement/` (rapport `966a3870…`, état du code `f50863be…`, contre-lecture `f219e7cc…`, configuration des interrupteurs), l'ordre de passage v3 (`b19f550b…`) ; `registres-provisoires/consignes-mere-epreuves-v9-compte-organisme-2026-11-19-v1.md` (section R-3861) ; le plan v5 de l'héritage (§ 3) et le devis v5 (§ 9) ; sur main (`git show origin/main:CHEMIN`) : `registres/go.md` (GO-2026-11-19-55 à -83), `registres/decisions.md` (R-3861, R-3894, R-3900), la décision N-073 et ses compléments sous `docs/decisions/`, N-058. Vérifie chaque empreinte avant de citer (R6, R11).

## Ce que tu rends

Dans ton bloc-notes seulement : la fiche et `rapport-redacteur-fiche-orchestrateur-v68-v1.md` (sources lues, ce que tu n'as pas pu établir). En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`. Nomme chaque chose par ce qu'elle fait, l'identifiant seulement en appui.

## Interdits

Aucun lancement de l'orchestrateur, ni en réel ni à blanc. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée, aucune écriture dans le dépôt. Jamais de heredoc ni de bloc de texte en ligne passé à un interpréteur. Aucune valeur de clé. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif dans une commande. Au premier refus d'un outil : arrête-toi et dis-le.
