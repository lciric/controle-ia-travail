# Consigne — corrections du code du pilote MR-2 après la contre-lecture (code v69) — v1

Écrite par la session mère le 13 novembre 2026 à 13:20 UTC (`date -u`), pour le développeur du code v68 (Claude Opus 5.5), repris
avec son contexte. **Tous les interdits et écarts de ta consigne d'origine (`consigne-developpeur-code-pilote-v1.md`, `3b4f570c…`)
restent en vigueur, sans changement** : aucune dépense, aucun appel de modèle ni de réseau, aucune clé lue, aucune poussée, noms
neufs (R12), ajouts seulement, un seul processus de calcul à la fois (`ulimit -v 6000000`, `OMP_NUM_THREADS=2`).

## 1. Pièce qui commande
La contre-lecture `docs/notes/organisme-multi-generations-v1/pilote-v1/contre-lecture-code-pilote-v68-v1.md` (`7af19261…`, sur `main` du dépôt de travail ; lis-la par `git show main:docs/notes/organisme-multi-generations-v1/pilote-v1/contre-lecture-code-pilote-v68-v1.md` depuis ton arbre) :
**« autorisable après corrections », 2 bloquants, 10 majeurs, 14 mineurs ; ses huit mutations survivent toutes.** Ses outils et
sorties : même dossier, `contre-lecture-code-v68-outils/`.

## 2. Décisions de la mère sur Q-1 à Q-12 (R-2534 ; Q-1 sur le mot de Lazar, R-2528)
- **Q-1 : (c)** — Fable 5.2 64 000 (plafond de session 3,00), Opus 5.5 89 000 (2,00) ; **Argon et Astra 36 000, plafond de session
  2,34 USD** (« au plus juste »), part 9,36 chacun ; **π1 = 20,00 USD, π2 = 21,72 USD**, total 41,72. Mets à jour la
  configuration, la table des proposeurs, l'essai des lignes de GO et tout « 19 » ou « 39 » en dur.
- **Q-2 : (d)** — une loi de référence hors des bornes ±4 est récrite en `transformee` équivalente (preuve E4 du contre-lecteur) ;
  C-16 ne s'arrête que si aucune écriture dans la grammaire servie n'existe ; ni la famille, ni le gardien, ni la mesure ne
  changent ; cas sain et artefact.
- **Q-3** : compte du gardien, `defaut` compris. **Q-4** : l'effort est écrit dans la configuration et **envoyé**, le même
  niveau « high » pour Fable 5.2 et Opus 5.5 ; pour Argon et Astra, le réglage du script du collisionneur éprouvé les 12 et
  13 novembre (`EFFORT = "high"`, mêmes champs que `appeler_gemini` et `appeler_openai`) ; tout réglage envoyé est consigné au
  manifeste. **Q-5** : interface Messages, clé nommée `RR_ANTHROPIC_API_KEY_RIGAUD` passée par son nom, en flux, sans repli de
  modèle, jamais `ANTHROPIC_BASE_URL`. **Q-6** : voie et champs du collisionneur pour Astra (`gpt-6-astra`, hôte d'OpenAI exact,
  `https`, toute autre adresse refusée hors boucle locale d'essai). **Q-7** : relais v68 pour Argon. **Q-8** : refus du modèle =
  échec sans abandon ; **modèle servi différent ou usage absent = abandon du proposeur** ; M-1 : admettre la forme datée d'un
  identifiant servi par une règle écrite et essayée (préfixe exact suivi d'un suffixe de date), rien de plus large.
  **Q-9, Q-10, Q-12** : avis du contre-lecteur. **Q-11** : rien n'est poussé vers le dépôt public.

## 3. À faire
1. Corriger **B-1 et B-2** (voie de Claude écrite et branchée ; plus aucun « à confirmer » ; le lanceur lance lui-même les relais en
   mode réel, clés par leur nom, environnement bâti par filtrage ; `/relais/etat` complet ; `appelant == dialecte` exigé ; un
   mode réel de bout en bout **sur doublures déclarées comme telles par les essais seulement**, un artefact par garde), puis
   **M-1 à M-10**, puis les mineurs ; pour chacun : corrigé, ou refusé avec sa raison écrite.
2. Les huit mutations du contre-lecteur et les tiennes doivent mourir ; rejoue le banc entier une fois, à la fin.
3. Essais à blanc A et B rejoués ; bloc gelé régénéré ; paquet et patch neufs (code v69, depuis la tête v68 `276b6afd`).
4. Livrables sous `docs/notes/organisme-multi-generations-v1/pilote-v1/code-v69/` sur ta branche `prep/pilote-mr2-v1` (commits
   neufs, rien poussé) : rapport `rapport-developpeur-code-pilote-v69-v1.md` avec un **tableau constat par constat** (B, M, m :
   fichier, ligne, correction, essai qui le prouve), le **différentiel v68 → v69** prêt pour sa contre-lecture, les marqueurs
   du texte à remplir (bloc, bornes, parts, lignes π1 et π2, réglages d'effort) et ce que le texte doit changer (C-5, C-16,
   liste d'arrêt, dérivation de la graine de développement, phrase sur l'effort).
5. **Sonde payante** : n'en fais aucune ; liste exactement ce qu'une sonde d'un appel par relais devrait vérifier avant le pilote
   et son coût au pire.

## 4. Rapport final à la mère (court)
Constats corrigés et refusés (nombres) ; essais, banc ; empreintes ; ce qui reste avant le premier appel ; heure de fin ; modèle.
