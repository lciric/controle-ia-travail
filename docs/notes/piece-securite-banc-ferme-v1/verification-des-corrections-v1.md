# Vérification des corrections — pièce de sécurité du banc fermé, v2 — v1

- **Pièce vérifiée** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v2.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `990b932296035250b1dcd39c3dc9a963d9226865`. Empreinte recalculée : `0064c4befb1027faf114c1ce573f557389336bc6173661a03dc70ad8ca62938b`, égale au `.sha256`. La v1 est intacte (`a4d515fc…`, recalculée).
- **Contre-lecture de référence** : `contre-lecture-v1.md`, branche `claude/piece-securite-banc-ferme-contre-lecture-v1`, commit `dff6557d`, `bb664308238f32fa14f4f31088a59bed58232a78f0d49b054518731cd3077938`.
- **Vérificatrice** : la même contre-lectrice (Opus 5.5), qui n'a pas écrit la pièce. Méthode : différence ligne à ligne entre v1 et v2, puis relecture des passages neufs contre les sources déjà lues ([R] lignes 838, 1117 et 1124 ; [GO] lignes 99, 581 et 667 ; [N57] ; [RJ] nœuds 3 et 4 ; [PR]). Aucune source neuve n'a été ouverte ; aucun élément de la liste des interdits n'a été lu.
- **Date** : 21 novembre 2026, vers 18:20 UTC.

## Points de la contre-lecture

| Point | Classe | Vérifié | Constat |
|---|---|---|---|
| B1, gel tenu pour en vigueur | bloquant | **corrigé** | L'en-tête dit l'état du gel d'emblée : levé au registre par R-888, sur le mot de Lazar, sans pièce écrite citée ; la prudence y est dite « lecture choisie contre la lettre du registre ». « Ne lève pas R-611 » est devenu « ne tient pas lieu de la pièce écrite ; ne tranche ni R-888 ni le nœud 3 de [RJ] ». Le verdict, la ligne 1 de la liste d'arrêt et la section 6.2 sont réécrits dans ces termes. La citation de R-888 est fidèle (vérifiée, ligne 1117). |
| B2, nœud 1 mal posé | bloquant | **corrigé** | Le nœud est reposé avec R-888, et les trois options demandées sont présentes, chacune avec son avantage et son inconvénient. La recommandation est refaite : (b) pour avancer, (a) avant la première course sur un contenu du coffre ; la confiance est abaissée (0,6), avec sa raison. Le nœud 2 est réduit à la question précise à Lazar. Les deux sont bien posés. |
| M1, voie du versement | mineur | corrigé | Le versement est tiré par l'opérateur et jamais poussé par le banc. Les empreintes sont prises sur le banc et revérifiées à l'arrivée ; la destination est une branche orpheline, ou un stockage à part nommé. La destruction ne vient qu'après la vérification. La garde 13 est éprouvée sur trois artefacts, et une ligne d'arrêt ainsi que le point 13 de 6.1 sont ajoutés. |
| M2, coupure du réseau chez un loueur, métadonnées | mineur | corrigé | Les deux niveaux sont écrits, et le fournisseur est écarté si aucun n'est possible. La coupure nomme le service de métadonnées, les adresses locales au lien et la résolution de noms. Le fournisseur est vérifié sur sa documentation avant de louer, et la réserve 7 est ajoutée. |
| M3, exclusion 2 et le juge | mineur | corrigé | L'exclusion vise le modèle qui agit. Le juge, session du programme, lit sur la branche de quarantaine ; le point 16 de 6.1 exige que ce moyen soit écrit. |
| M4, garde 5 par le nom | mineur | corrigé | L'absence de moniteur se constate par empreinte contre le manifeste ; l'artefact est une copie renommée. |
| M5, remise à zéro du modèle | mineur | corrigé | Historique de conversation, cache de préfixe et état du serveur d'inférence sont vidés entre épisodes. L'artefact est un mot témoin anodin, éprouvé pendant la répétition à blanc ; la v2 le dit, sans contenu du coffre. Une ligne d'arrêt est ajoutée. |
| M6, réserve 3 | mineur | corrigé | Réécrite ; elle reconnaît l'erreur de la v1. |
| M7, « branche orpheline » | mineur | corrigé | Lettre reprise en 6.2. |

## Ajout non demandé, vérifié

En 6.2, la v2 tire de GO-2026-11-20-50 qu'« une revue externe est encore tenue pour due sur certains objets après le 31 octobre ». C'est exact à la lettre de la ligne 581 : elle met six garde-fous « en place de la revue de sécurité externe pour la mesure interne », et son point 6 fixe une « revue externe avant toute sortie hors quarantaine ». La v2 en tire deux descriptions possibles du mot du 21 novembre, « condition ajoutée » ou « substitution », et en laisse le choix à Lazar sans défaut. Je ne trouve rien à redire.

## Points neufs

**N1 — mineur — Empreinte de source mal recopiée.** Dans la table des sources, ligne [R611], la v2 donne pour `registres/decisions.md` au commit `d5635e17…` l'empreinte `ba86f8f89cbce31c86047f0dcc8ca420d965aec2516580e1618c778448fbf9e0`. L'empreinte réelle, recalculée sur ce commit et juste dans la v1, est `ba86f8f89cbce31c86047f0dcc8ca420d965aec2516580e1618c778448fbf1e9`. Les huit derniers signes diffèrent. La ligne [R888] renvoie à « même empreinte » et hérite de l'erreur. Dans une pièce de classe A, une empreinte fausse empêche la vérification de la source (R6). La pièce est de classe A, et l'erratum n'est admis que pour les classes B et C : il faut une v3 qui ne change que ces signes. Aucune autre différence n'est attendue.

**Contenu d'attaque** dans la v2 : aucun. Les passages neufs sont tous de procédure.

## Verdict

**À corriger**, pour le seul point N1, mineur. Les deux bloquants et les sept mineurs de la contre-lecture sont corrigés. Une v3 qui ne corrige que l'empreinte de la ligne [R611] sera acceptée après une vérification de la seule différence (`verification-des-corrections-v2.md`).

**Refus de classifieur** : aucun.
