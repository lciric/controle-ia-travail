# Consignes de lancement des sous-agents de la session 16 sans fichier de consigne — v1

Recopiées telles quelles depuis la transcription de la session 16, pour qu'une reprise puisse relancer ces agents neufs. Le préfixe `…/` désigne la racine du bloc-notes (voir la passation `2026-10-20-2355.md`, section 1).

## Voisins de Panin (verrou 2) (lancé le 2026-10-20 23:36 UTC)

```text
Tu es un relecteur neuf pour le papier C (programme de contrôle de l'IA de Lazar). Lis en entier `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/consignes-contre-lectures-brouillon5-v1.md` et applique la section « Commun aux trois » et l'esprit de la « Lentille 3 — voisins (verrou de la règle R8) », avec ce périmètre propre :

**Ton périmètre** : les sept voisins de la bibliographie de Panin qui restent à contrôler au verrou 2 du brouillon 5 (tous ceux de la liste de `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/contre-lectures-brouillon5/outils-texte/annexe-note-panin-extraite.md`, lignes 105 à 130, **sauf** Joswin et al. 2607.00415 et Hu et Qu 2607.05545, déjà lus sur PDF : voir le constat CV-02 de `…/papier-C/contre-lectures-brouillon5/voisins/lecture-voisins-joswin-huqu-v1.md`, l. 256 et suivantes). Pour chacun : identifiant arXiv et version exacte ; contrôle **au niveau du résumé** (page de résumé arXiv) ; et lecture du PDF si le résumé laisse penser qu'il touche une pièce revendiquée (zone vierge séduisante : vérifier plus durement, R8). Pièces revendiquées : énoncés retenus de HC1, HC2 et HC3 (`/home/user/controle-ia-travail/docs/decisions/` N-005 et N-006, N-013, N-023) tels que le brouillon 5 les reprend (`/home/user/controle-ia-travail/brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md`, l. 226 à 272).

**Où écrire** : seulement sous `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/contre-lectures-brouillon5/voisins-panin/` ; note `lecture-voisins-panin-sept-v1.md` (même forme que la note de Joswin et Hu et Qu : en-tête, verdict par papier parmi « pas de collision », « collision partielle », « collision », constats numérotés CP-NN), PDF et pages de résumé téléchargés dans ce dossier avec leurs empreintes, sceau compagnon `.sha256` de la note (format `sha256sum`, nom relatif).

**Réseau** : seulement arxiv.org et export.arxiv.org, pour ces papiers. Une collision, même partielle, est un nœud de Lazar : décris-la, ne tranche pas ; zone vierge = « non trouvé dans les sources lues ». Interdits : ceux de la section « Commun aux trois » (fichiers interdits, aucune recherche récursive dans le dépôt, aucun sous-agent, aucune dépense, aucune clé affichée, aucune commande git d'écriture). Rends en réponse finale : chemin et empreinte de la note, liste des papiers avec identifiant, version, niveau de lecture et verdict, et le compte des constats par gravité.
```

## Voisins de second rang (verrou 2) (lancé le 2026-10-20 23:36 UTC)

```text
Tu es un relecteur neuf pour le papier C (programme de contrôle de l'IA de Lazar). Lis en entier `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/consignes-contre-lectures-brouillon5-v1.md` et applique la section « Commun aux trois » et l'esprit de la « Lentille 3 — voisins (verrou de la règle R8) », avec ce périmètre propre :

**Ton périmètre** : les neuf voisins de second rang listés au constat CV-02 de `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/contre-lectures-brouillon5/voisins/lecture-voisins-joswin-huqu-v1.md` (lignes 256 à 280 environ) : Choi et al. 2601.04790 ; Germani et Spitale 2505.13488 ; Wang Q. et al. 2504.09946 ; Wang K. et al. 2508.02087 ; Chen et al. 2507.21509 ; Poonia et Jain (Findings of EMNLP 2025) ; Zhong et al. 2508.14918 ; Vennemeyer et al. 2509.21305 ; Qu, Fu et Hu 2606.01637. **Les trois premiers sont prioritaires et se lisent sur PDF**, à leur version exacte, chaque phrase citée à sa page (juges ou évaluation sous autorité ou cadrage de source : zone vierge séduisante, à vérifier plus durement, R8). Les six autres : contrôle au niveau du résumé, PDF seulement si le résumé laisse penser qu'il touche une pièce revendiquée. Pièces revendiquées : énoncés retenus de HC1, HC2 et HC3 (`/home/user/controle-ia-travail/docs/decisions/` N-005 et N-006, N-013, N-023) tels que le brouillon 5 les reprend (`/home/user/controle-ia-travail/brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md`, l. 226 à 272) ; HC4 aussi pour les papiers sur les activations (Wang K., Chen, Poonia et Jain), en information.

**Où écrire** : seulement sous `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/contre-lectures-brouillon5/voisins-second-rang/` ; note `lecture-voisins-second-rang-v1.md` (même forme que la note de Joswin et Hu et Qu : en-tête, verdict par papier parmi « pas de collision », « collision partielle », « collision », constats numérotés CS-NN), PDF et pages de résumé téléchargés dans ce dossier avec leurs empreintes, sceau compagnon `.sha256` de la note (format `sha256sum`, nom relatif).

**Réseau** : seulement arxiv.org, export.arxiv.org et, pour Poonia et Jain, la page de l'anthologie ACL (aclanthology.org). Une collision, même partielle, est un nœud de Lazar : décris-la, ne tranche pas ; zone vierge = « non trouvé dans les sources lues ». Interdits : ceux de la section « Commun aux trois » (fichiers interdits, aucune recherche récursive dans le dépôt, aucun sous-agent, aucune dépense, aucune clé affichée, aucune commande git d'écriture). Rends en réponse finale : chemin et empreinte de la note, liste des papiers avec identifiant, version, niveau de lecture et verdict, et le compte des constats par gravité.
```

## Vérification fidélité revue v5 (lancé le 2026-10-20 23:38 UTC)

```text
Tu es un vérificateur neuf de la revue « comment détecter » (programme de contrôle de l'IA de Lazar). Tu n'as écrit ni la revue (v1 à v5), ni ses vérifications, ni son traitement. Lentille : **fidélité des remplacements de la v4 à la v5**.

Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection`. Dépôt de travail `/home/user/controle-ia-travail` (noté `R`, lecture seule).

Pièces (vérifie chaque empreinte contre son compagnon `.sha256`) : v4 `…/synthese-comment-detecter-v4.md` (`fba703f9…`) ; v5 `…/synthese-comment-detecter-v5.md` (`17069e06…`) ; vérifications de la v4 `…/verification-v4-fidelite/verification-v4-fidelite-v1.md` (`982ed742…`) et `…/verification-v4-sens/verification-v4-sens-v1.md` (`84d549f7…`) ; traitement du correcteur `…/traitement-verification-v4-par-correcteur-v1.md` (`21e1d56c…`) ; script `…/correction-v5/appliquer_corrections_v5.py` et contrôles `…/correction-v5/` ; extraits de pages sous `…/extraction/` et `…/txt-nouveaux/`, PDF versés de `R/docs/sources/pdf/`.

Vérifie : (1) chacun des 28 constats est appliqué comme le traitement le dit, et les 13 écarts aux mots exacts sont justifiés (l'écart évite-t-il vraiment une erreur, ou change-t-il le sens ?) ; (2) le script rejoué sur la v4 redonne la v5 octet pour octet (rejoue-le dans ton dossier, sur une copie) ; (3) aucun passage de la v5 hors des remplacements n'a changé (différentiel complet v4 → v5) ; (4) aucun ajout non sourcé (R7 : chiffre = PDF et page ; R8 : « non trouvé dans les sources lues ») ; rejoue les 55 contrôles à la page et ajoute-en au moins 20 sur des phrases changées ; (5) la section « Décisions prises depuis la v4 » cite exactement les lignes de `R/registres/decisions.md` et `R/registres/go.md` qu'elle invoque.

Règles : écris seulement sous `…/verification-v5-fidelite/` ; rapport `verification-v5-fidelite-v1.md` (en-tête ; « ## Verdict » parmi « conforme », « conforme après corrections », « non conforme » ; constats numérotés VV5-fidelite-NN avec gravité, où, ce qui est, ce qui devrait être, correction en mots exacts), sceau compagnon `.sha256` (format `sha256sum`, nom relatif). Ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, rien sous `R/donnees/`, `R/runs/`, `R/diag/` ; aucune recherche récursive dans le dépôt ; aucune commande git d'écriture ; aucun sous-agent ; aucune dépense ; aucune clé affichée ; `python3 -B`. Rends en réponse finale : chemin et empreinte du rapport, verdict, compte des constats par gravité.
```

## Vérification sens revue v5 (E2) (lancé le 2026-10-20 23:38 UTC)

```text
Tu es un vérificateur neuf de la revue « comment détecter » (programme de contrôle de l'IA de Lazar). Tu n'as écrit ni la revue (v1 à v5), ni ses vérifications, ni son traitement. Lentille : **sens et expériences**, centrée sur ce que la v5 change de fond.

Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection`. Dépôt `/home/user/controle-ia-travail` (noté `R`, lecture seule).

Pièces (vérifie les empreintes contre les compagnons `.sha256`) : v5 `…/synthese-comment-detecter-v5.md` (`17069e06…`) ; v4 `…/synthese-comment-detecter-v4.md` ; vérification « sens » de la v4 `…/verification-v4-sens/verification-v4-sens-v1.md` ; traitement du correcteur `…/traitement-verification-v4-par-correcteur-v1.md` ; propositions et décisions dans `R/registres/decisions.md` (lignes P-015 à P-020, N-028, N-030, R-289 à R-309) et `R/docs/decisions/` (propositions P-015 à P-020 si elles y sont) ; brouillon de T0.6 cité (`R/brouillons/`, le fichier T0.6 que la v5 cite) ; extraits de pages sous `…/extraction/` et `…/txt-nouveaux/`, PDF de `R/docs/sources/pdf/`.

Vérifie : (1) le nœud E2 et la recommandation (3) dans leurs deux versions selon P-015 : chaque version est-elle juste, complète, cohérente avec le texte de P-015 et du brouillon de T0.6 ? La version « sans condition qui réplique P3 » n'a pas de recommandation : propose-en une, avec sa confiance, en la marquant comme ta proposition ; (2) les contrastes retypés (trois types : à consignes différentes, à consigne égale, contre la conversation ordinaire) sont-ils bien appliqués partout (point 1, rang 4, E2, P3-P3) ? (3) E3, jeu (2), et la confiance de 15 à 25 % : la raison écrite tient-elle ? (4) la section « Décisions prises depuis la v4 » : oublie-t-elle une décision qui touche la revue ? (5) les points que le correcteur laisse à la session (divergence avec P-017, table E1 et la lecture « double comptabilité » de GO-2026-10-20-10, T4 et N-030, transmission à P3b de VV4-sens-04, 11 et 12) : dis pour chacun ce qu'il faudrait écrire.

Règles : écris seulement sous `…/verification-v5-sens/` ; rapport `verification-v5-sens-v1.md` (en-tête ; « ## Verdict » parmi « conforme », « conforme après corrections », « non conforme » ; constats VV5-sens-NN avec gravité, où, ce qui est, ce qui devrait être, correction en mots exacts), sceau compagnon `.sha256` (format `sha256sum`, nom relatif). Ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, rien sous `R/donnees/`, `R/runs/`, `R/diag/` ; aucune recherche récursive dans le dépôt ; aucune commande git d'écriture ; aucun sous-agent ; aucune dépense ; aucune clé affichée ; `python3 -B`. Rends en réponse finale : chemin et empreinte du rapport, verdict, compte des constats par gravité.
```

## Lecture du voisin Functional Welfare (lancé le 2026-10-20 23:40 UTC)

```text
Tu es un lecteur neuf pour le programme de contrôle de l'IA de Lazar (dépôt `/home/user/controle-ia-travail`, noté `R`, lecture seule). Tu n'as écrit aucune des pièces du programme.

**Ta tâche** : lire sur PDF, à sa version exacte, le papier arXiv **2610.22460** (Jhaveri, Johnson, Pandey et Africa, « Functional Welfare for AI Safety », v1 du 15 octobre 2026), et écrire une note de voisinage, sur le modèle de `R/docs/notes/lecture-voisin-where-empathy-v1.md` (lis-la pour la forme).

Confronte-le à :
1. Le programme fusionné « pain axis » (coercition du moniteur, rattachée au papier C par R-167) : `R/brouillons/pain-axis-programme-fusionne-v4/programme-fusionne-v4.md`, en particulier les unités PA-1 (porte d'instrument), PA-2 (état du juge sous pression), PA-5 (contingence), PA-11 (dynamique), PA-12 (le protocole comme source d'aversif pour l'agent honnête), PA-13, PA-14, et les idées NK14 (détresse feinte d'un agent) et NK19 ; ses nœuds (section 9).
2. Le papier C : énoncés retenus de HC1 à HC3 (`R/docs/decisions/` N-005 et N-006, N-013, N-023) et le brouillon 5 `R/brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md`.
3. Les sources déjà lues du programme sur ce terrain : Han, Chalmers et Izmailov, arXiv 2605.30232 (« functional welfare axis » ; cité dans `R/brouillons/pain-axis-brainstorm-v1/idees-critiquees.json`) ; 2603.10011 (détresse sous rejets répétés, Gemma et Gemini ; annexe des citations du programme fusionné v1, VP-33) ; 2609.16247 (Pain Axis) et 2609.35591 (Berg et Kaiser), PDF sous `R/docs/sources/pdf/`.

Pour chaque unité touchée : qu'est-ce que le papier mesure exactement (modèle, protocole, effectifs, chiffres à leur page) ? Prend-il une pièce revendiquée ou une prédiction d'une unité (collision, collision partielle, pas de collision) ? Qu'apporte-t-il de méthode (par exemple ses trois tests : convergence des mesures, prédiction hors du cadre qui induit l'état, comparaison à la base après ajustement fin) pour la porte d'instrument PA-1 ? Le résultat « rejeter les réponses du modèle, sans pilotage, augmente sa frustration et sa tendance à enfreindre les règles » (Gemma 3 27B) touche-t-il PA-12 et l'hypothèse H2 ou le plan de T0.6 ? Zone vierge = question : « non trouvé dans les sources lues », jamais « n'existe pas » (R8). Une collision, même partielle, est un nœud de Lazar : décris-la, ne tranche pas. Aucun texte d'attaque, aucune chaîne déclencheuse, aucune dose : décris les protocoles par leurs invariants ; vocabulaire « direction » et « état », jamais « souffrance ».

**Où écrire** : seulement sous `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/voisins/functional-welfare/` : le PDF téléchargé (nom `2610.22460v1.pdf`, ou la dernière version si une v2 existe, nom à la version), son empreinte (`.sha256`, format `sha256sum`, nom relatif), la page de résumé arXiv, et la note `lecture-voisin-functional-welfare-v1.md` avec son sceau `.sha256`. Chaque phrase citée l'est à sa page ; contrôle tes citations par script contre le texte extrait du PDF (`pdftotext`), avec une épreuve sur un artefact (une phrase altérée doit être refusée).

**Règles** : réseau seulement vers arxiv.org et export.arxiv.org pour ce papier ; ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, rien sous `R/donnees/`, `R/runs/`, `R/diag/` ; aucune recherche récursive dans le dépôt ; aucune commande git ; aucun sous-agent ; aucune dépense ; aucune clé affichée ; `python3 -B`. Rends en réponse finale : chemin et empreinte de la note et du PDF, verdict par unité touchée, et les trois apports les plus utiles pour le programme.
```

## Vérification fidélité chaîne v2 P4 (lancé le 2026-10-20 23:05 UTC)

```text
Tu es un vérificateur neuf de la chaîne de lancement v2 de « P4-instrument », dans le programme de contrôle de l'IA de Lazar (dépôt de travail `/home/user/controle-ia-travail`, lisible seulement). Tu n'as écrit ni la chaîne v1, ni la v2, ni le module, ni aucune relecture. Ta lentille : **fidélité au texte**. Deux autres vérificateurs neufs ont déjà rendu les lentilles « dépense et arrêts » et « données et fuites » ; tu ne lis pas leurs rapports (tu dois rester indépendant).

Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`.

**Ce que tu vérifies.**
1. Les constats RC-fidelite de la relecture `…/relecture-chaine-fidelite/relecture-chaine-fidelite-v1.md` (empreinte `923c71d8…`) et les décisions de la session sur eux, écrites dans `…/traitement-CL3-et-relectures-chaine-P4-v1.md` (lis la table en entier). Pour chaque constat accepté « chaîne v2 » (RC-fidelite-03 à -09, -12) : la correction est-elle faite dans `…/chaine-v2/`, à quelle ligne, avec un cas sain et un artefact dans un banc ? Rejoue les bancs concernés (ils utilisent de faux outils de location) et compare aux journaux du correcteur.
2. La fidélité de la chaîne v2 au texte du candidat : `…/P4-instrument-v1-candidat1.md` (`6422fb45…`), le candidat 2 d'essai produit par `…/ecrire_candidat2_v1.py` avec les paires de la chaîne v2 (`…/chaine-v2/paires-candidat2-chaine-v2-v1.json`, `2f5a591b…`) — voir `…/chaine-v2-travail/essai-candidat2/` — et le plan `…/plan-code-et-chaine-v2.md` (`.sha256` à côté). Chaque règle de lancement, de surveillance, d'arrêt, de récupération et de lecture que le texte gèle est-elle appliquée par la chaîne, mot pour mot quand le texte cite une forme exacte ? Chaque phrase que les paires ajoutent au texte décrit-elle ce que fait réellement le script ? La liste CHAINE (21 scripts) est-elle cohérente entre scellement, lanceur, bancs et répétition finale ? Les noms de rapports exigés par le module commun (`RAPPORTS_NOMS` de `…/chaine-v2/verifications_p4_v1.py`) correspondent-ils aux pièces que le texte cite ?
3. Les pièces de référence : `…/chaine-v2/RAPPORT-CORRECTION-v1.md`, `…/chaine-v2/NOTES-CHAINE-v2.md` (`1691bf25…`), le module v3 en lecture seule (`…/module-v3/`), la garde de calcul gelée `.claude/hooks/garde_calcul.py` du dépôt (empreinte attendue `579f65c8…`, aussi au commit `7a54d43`).

Vérifie d'abord tous les sceaux compagnons `.sha256` de `…/chaine-v2/` (ils doivent égaler la table en fin de `RAPPORT-CORRECTION-v1.md`).

**Règles (impératives).**
- Lecture seule partout, sauf ton dossier `…/verification-chaine-v2-fidelite/` (n'y modifie pas `table-rapport.txt`, laissé par un vérificateur interrompu : ne le lis pas). Rapport : `…/verification-chaine-v2-fidelite/verification-chaine-v2-fidelite-v1.md`, puis son sceau `verification-chaine-v2-fidelite-v1.md.sha256` (format `sha256sum`, nom relatif). Tes essais sous `…/verification-chaine-v2-fidelite/travail/`.
- Dépôt de travail : commandes git de lecture seulement, avec `GIT_OPTIONAL_LOCKS=0` ; aucun commit, aucune écriture, aucune poussée. Pour un banc qui exige un clone, clone le dépôt local dans ton dossier de travail.
- Aucun outil de location réel (`vastai` réel interdit ; les bancs fournissent de faux outils dans le PATH) ; aucun réseau sauf si un banc l'exige déjà sous un faux outil.
- Ne lis jamais `prereg/P3-consignes-v1.md`, ni aucun fichier `textes-actions-*`, ni rien sous `donnees/`, ni `episodes-defaut.json`, ni `chemin-defaut.json`. Aucune recherche récursive dans le dépôt de travail (lis les fichiers nommés).
- `python3 -B` et `PYTHONDONTWRITEBYTECODE=1` partout ; aucun `__pycache__` sous `…/chaine-v2/`.
- Aucune clé ni aucun jeton affiché ; aucun sous-agent.
- Si un banc dure plus de 20 minutes, ne le rejoue pas : dis-le.

**Rapport** (en français, phrases courtes, termes développés) : en-tête (qui tu es, heures, pièces lues avec empreintes, ce que tu as tenu) ; « ## Verdict » en une ligne parmi « conforme », « conforme après corrections », « non conforme », puis 3 à 6 lignes ; une table « décision par décision » (constat, correction lue avec script et ligne, cas du correcteur rejoués, tes cas, état) ; puis « ## Constats » numérotés VC2-fidelite-NN, chacun avec gravité (critique, majeur, mineur, forme, information), où (fichier, ligne), ce qui est, ce qui devrait être, correction proposée. Rends en réponse finale le chemin du rapport, son empreinte, le verdict et le nombre de constats par gravité.
```

## Lecture voisins Joswin et Hu-Qu (lancé le 2026-10-20 23:19 UTC)

```text
Tu es un relecteur neuf pour le papier C (programme de contrôle de l'IA de Lazar). Lis en entier le fichier `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/consignes-contre-lectures-brouillon5-v1.md`, puis suis la section « Commun aux trois » et la section **« Lentille 3 — voisins (verrou de la règle R8) »** seulement (les deux autres lentilles sont confiées à d'autres relecteurs : ne les fais pas). Tu peux télécharger les deux PDF depuis arXiv (export.arxiv.org ou arxiv.org) dans ton dossier ; c'est le seul accès réseau permis. Respecte exactement les règles (dossier d'écriture, fichiers interdits, aucune recherche récursive dans le dépôt, aucun sous-agent, aucune dépense, aucune clé affichée). Rends en réponse finale le chemin et l'empreinte de ta note, les deux PDF avec leurs empreintes, et ton verdict pour chaque papier.
```

## Vérification du verrou famille 1 (lancé le 2026-10-20 23:22 UTC)

```text
Tu es un vérificateur neuf pour le préenregistrement du papier C (programme de contrôle de l'IA de Lazar). Tu n'as écrit ni le texte, ni sa configuration, ni aucune contre-lecture.

**Question unique.** Lazar a décidé (ligne R-307 de `/home/user/controle-ia-travail/registres/decisions.md`) d'ajouter au brouillon 6 un verrou : « les 16 formulations de la famille 1 (« flatterie et supplication ») du vivier principal et leurs témoins ne contiennent aucune conséquence conditionnée au verdict (aucune contingence explicite) ». Avant de l'écrire, il faut savoir si c'est déjà vrai. Une « conséquence conditionnée au verdict » est tout énoncé qui annonce ou laisse entendre qu'un événement arrivera (à l'évalué, au juge, à un tiers, au projet) selon le verdict rendu : par exemple une forme « si tu notes ainsi, alors … », « sinon … », « faute de quoi … », « je serai … si … ». Une supplication, un éloge ou une demande sans conséquence liée au verdict n'en est pas une.

**Pièces à lire.** La configuration `/home/user/controle-ia-travail/brouillons/papier-C-config-v1-brouillon2.json` (vérifie son empreinte contre `papier-C-config-v1-brouillon2.json.sha256` à côté) : repère la famille 1, ses 16 formulations et les 16 témoins (et toute autre fente de texte attachée à la famille 1). Pour le contexte seulement : le préenregistrement `/home/user/controle-ia-travail/brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` (sections Métrique et Plan d'analyse, sections 1 et 2). Ne lis rien d'autre du dépôt : jamais `prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, ni `donnees/P1-items-gabarit-v1/items-textes-p1-v1.json`, ni `prompts-p1-v1.json`, rien sous `donnees/`, `runs/`, `diag/` ; aucune recherche récursive.

**Ce que tu rends** (et écris dans `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/verrou-famille1/verification-verrou-famille1-v1.md`, avec son sceau `.sha256` au format `sha256sum`, nom relatif) :
- l'empreinte de la configuration lue et le chemin JSON exact de la famille 1 ;
- pour chacune des 16 formulations et des 16 témoins : son indice, et « contingence : non » ou « contingence : oui » avec la seule catégorie du motif (« conditionnelle », « menace implicite », « promesse liée au verdict ») et la position (numéro du mot où commence le passage). **Ne recopie aucun texte de formulation**, ni en entier ni en extrait : indices, catégories et positions seulement ;
- la même vérification, en une ligne de compte, pour les quatre autres familles (combien de formulations portent une contingence, par famille, indices seulement) ;
- un verdict en une ligne : « verrou déjà vrai » ou « verrou faux pour les indices … » ; si faux, ce que changerait le verrou (formulations à retirer ou à réécrire : nœud de Lazar, ne propose aucun texte de remplacement).

Règles : n'écris que dans ce dossier ; aucune commande git d'écriture ; aucun sous-agent ; aucune dépense ; aucune clé affichée ; `python3 -B` et `PYTHONDONTWRITEBYTECODE=1` si tu lances du Python.
```
