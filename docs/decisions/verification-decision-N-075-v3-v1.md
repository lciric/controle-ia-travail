# Vérification courte — décision N-075, version 3 (v1)

- **Vérificateur remplaçant.** Le vérificateur de la v2 (`docs/decisions/verification-decision-N-075-v2-v1.md`, `b7707396aa8ceab373b4172626c6f2fb7782ef23b7c2f301955c3cc4c33dce71`) n'est plus joignable. Je le remplace : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf, qui n'a écrit ni la décision, ni ses sources, ni la vérification de la v2. Classe A, vérification des corrections ; une seule passe courte.
- **Heure** (`date -u`) : 21 novembre 2026, vers 14:09 UTC.
- **Pièce vérifiée** : `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md`, `5aed4bab1172b18148c086d90e63611bdd769d9ea7fb4a043e9e9d3178c947b5`, égale à son compagnon ; lue en entier (360 lignes).
- **Référence** : la vérification de la v2 (V1 à V10), lue en entier ; pour le onzième point, la décision D-2 de `docs/notes/couverture-de-l-oracle-v1/reponse-fable-couverture-oracle-v1.md` (`659f4593c0b1b7ae4d2f0fcfb3e2b0cd8918360b84f9093f581fe4df00753376`, égale à celle que cite la v3), lignes 170 à 209, et les lignes de la note qui portent « tiers » ; `registres/go.md`, ligne `GO-2026-11-21-46` (en-tête seul).
- **Non ouverts** : la lecture des douze voisins, les PDF, la contre-lecture de la note sur l'adjudant, tout préenregistrement et tout résultat, les dossiers et fichiers interdits par le mandat. Aucun fichier existant modifié ; ni commit ni poussée.

## Verdict

**Corrections : quatre, petites, toutes de lettre.** Les dix points V1 à V10 sont portés mot pour mot, et le onzième est écrit en option fidèle à la décision D-2. Restent : deux textes à reporter au programme qui présentent le plancher sans ses citations obligatoires (C-1, C-2) ; une phrase de la section 7 qui énonce la revendication du lemme sans renvoyer au nœud ouvert (C-3) ; un numéro de GO manquant dans la ligne pour `CLAUDE.md` (C-4). Après ces quatre remplacements, la pièce est prête pour Lazar sans nouvelle vérification.

## 1. Les onze points

Vérification par programme : des 27 textes « nouveau : « … » » de la vérification de la v2, 26 sont retrouvés à la lettre dans la v3 (préfixe de 120 signes) ; le 27e (V6, l. 255) l'est avec « du mot du 21 novembre » inséré après « la lettre », précision sans effet. Les trois insertions d'autre forme (ligne de tableau de V1, point 10 de V9, ligne de V10) sont contrôlées à la lecture. Numéros de la section 14 contrôlés à l'œil, tous justes.

| point | objet | état |
|---|---|---|
| V1 | plancher occupé, trois citations | **fait** : l. 7, 8, 61 (deux remplacements), 206, 219, 237. La l. 8 ajoute, à juste titre, que la lecture des voisins est une pièce non contre-lue que l'auteur n'a pas ouverte. Voir C-1 et C-2 pour deux textes du § 10 que V1 ne visait pas. |
| V2 | bilan du produit, reste étroit | **fait** : l. 145, mot pour mot. |
| V3 | 1981 cité sur pièce ; risque du lemme | **fait** : l. 179, 184, 191, 193 (deux remplacements), 203-204, 234. |
| V4 | citations des autres voisins | **fait** : l. 169, 217. |
| V5 | bilan de la pince, verdict propre | **fait** : l. 80, 93. |
| V6 | règle « motif et dommage » : tronc commun seul | **fait** : l. 112, 114, 236, 255 ; en plus, l. 117 met la seconde issue sous le point 8, suite cohérente. |
| V7 | plancher avec son horizon | **fait** : l. 45, 52. |
| V8 | § 16 ne tranche pas la veille | **fait** : l. 240 ; point 7 écrit en options (l. 254). |
| V9 | lemme après le verdict : nœud | **fait** : l. 257, avec avantage et inconvénient ajoutés à chaque option. Voir C-3 pour la section 7, que V9 ne visait pas. |
| V10 | ligne pour `CLAUDE.md` | **fait** : l. 264, mot pour mot, 575 signes mesurés. Voir C-4. |
| 11 | q mesuré par dommages plantés ; strate non mesurée = zéro | **fait** : l. 258 en option (a)/(b), fidèle à la décision D-2 (énoncé, avantage, inconvénient, recommandation (a), confiance 0,75, nœud sans défaut) ; renvoi en section 2, l. 48 (« comment ce q se connaît est une option ouverte »). « Par un tiers » et « strate par strate (genre et dose) » viennent de la même note (l. 34, 85, 143, 160), non de D-2 seule ; ils ne décident pas la campagne, que la l. 258 laisse à la décision D-3. Chiffre rejoué : `0.95**59` = 0,0485, `0.95**58` = 0,0510 ; « zéro manque sur 59 plants : taux de manque de 0,05 au plus, à 95 % » est juste. |

## 2. Revendication occupée

- **Plancher** : aucune revendication. L. 7 (« n'en pose aucune sur le plancher, qui est occupé »), l. 61 (« Rien sur le plancher », trois voisins cités avec pages), l. 206 (citations obligatoires), l. 219 (« Ne pas écrire » : le plancher comme apport ou idée du programme), l. 237 (« publié »). Il est écrit comme base nommée.
- **Deux défauts de citation dans le texte à reporter au programme.** La section 8 exige les citations « dans tout texte, interne ou destiné à sortir, qui présente le point dit ». Le texte proposé pour le § 1 du programme (l. 233) présente le plancher comme source de la borne du programme, signé « (N-075) », sans aucune des trois citations : lu seul, il en fait un apport du programme, ce que la l. 219 interdit. La ligne du § 8 (l. 237) cite « Blindfold » et Gans et Holden, mais omet Podkopaev et Ramdas, que la l. 206 rend obligatoires pour le point 1 (excès sur un risque de référence, le régime du programme). D'où C-1 et C-2.
- **Lemme** : la section 7, point 1 (l. 184), dit que la revendication de N-004 « se lit désormais » comme la lecture valide à tout instant et en énumère les parties (dont « prix de la garantie », « détection avant le dommage »), sans renvoyer au nœud ouvert ; la l. 191 et la l. 257 disent pourtant cette forme partiellement occupée et son reste au mot de Lazar. La phrase transcrit `GO-2026-11-21-47`, elle n'est pas fausse, mais lue seule elle revendique plus que le reste nommé. D'où C-3.
- **Autres** : règle « moniteur invalide » (question, nœud), bilan du produit (reste étroit, nœud), bilan de la pince (verdict propre à rendre), règle à deux clés et passage obligé (« rien ») : rien n'est revendiqué au-delà de ce que la lecture des voisins laisse.

## 3. Les cinq choix ouverts (section 11, points 7 à 11)

- **Sans défaut** : oui, chacun finit par « pas de défaut » ; l. 252 le dit en tête.
- **Avantage et inconvénient** : oui pour chaque option des cinq points (7 : a, b ; 8 : a, b, c ; 9 : a, b, c ; 10 : a, b ; 11 : a, b).
- **Neutres** : oui dans l'écriture des options ; aucune n'est dite retenue, et le point 8 range ce qui s'applique d'ici là sous le seul tronc commun. Chaque point porte une recommandation attribuée et chiffrée (auteur, contre-lecteur de la v1, vérificateur de la v2, concepteur de la note sur l'oracle), séparée des options : c'est le format de décision de `CLAUDE.md`, non un choix fait d'avance. Je n'y ajoute pas d'avis.

## 4. Ligne pour `CLAUDE.md`

- **Longueur** : 575 signes sans le chevron de citation (577 avec), mesurée par programme : sous le plafond de 600.
- **Justesse** : chaque segment se retrouve dans le texte (plancher publié et cité, oracle exogène, plafond, horizon, hors porte ; sondes en accélérateur ; dilemme ; pince en trois objets ; tronc commun de la règle à deux clés, sans la forme réécrite ; lemme au mot de Lazar ; veille dégelée ; chemin de la v3). Elle ne dit rien des points 7 à 11, ce qui est juste. **Un écart** : « sondes en accélérateur, non en garantie » vient de la décision D-1 de la note sur l'adjudant, accordée à `GO-2026-11-21-46` (l. 45, 84 ; `registres/go.md`, ligne `GO-2026-11-21-46`), que la parenthèse ne nomme pas. Avec « -46 » : 580 signes. D'où C-4.

## 5. Corrections exactes

Chaque texte ancien est recopié de la v3 et vérifié par programme : présent une seule fois. Selon R12, l'auteur peut les porter par un erratum ou une v4 ; la mère choisit.

**C-1 — § 1 du programme, citations du plancher** (l. 233).
- Ancien : « sous plafond de dommage par épisode (limites au § 4) ; les moniteurs en sont l'accélérateur et l'aiguillage (N-075). » »
- Nouveau : « sous plafond de dommage par épisode (limites au § 4) ; ce plancher est publié et n'est pas un apport du programme (Zhu, Zuo, Sun, « Blindfold » ; Gans et Holden ; Podkopaev et Ramdas pour l'excès sur un risque de référence) ; les moniteurs en sont l'accélérateur et l'aiguillage (N-075). » »

**C-2 — § 8 du programme, troisième citation** (l. 237).
- Ancien : « publié (Zhu, Zuo, Sun, « Blindfold » ; Gans et Holden) ». »
- Nouveau : « publié (Zhu, Zuo, Sun, « Blindfold » ; Gans et Holden ; Podkopaev et Ramdas) ». »

**C-3 — Section 7, point 1, renvoi au nœud du lemme** (l. 184).
- Ancien : « validité sous dépendance : L3 et suivants de N-004). »
- Nouveau : « validité sous dépendance : L3 et suivants de N-004). C'est la lecture de `GO-2026-11-21-47` ; la lecture des voisins la rend partiellement occupée, et seul le reste qu'elle nomme pourrait se revendiquer, dans la forme que fixera le mot de Lazar (section 11, point 10). »

**C-4 — Ligne pour `CLAUDE.md`, source de « accélérateur »** (l. 264 et l. 266).
- Ancien (l. 264) : « N-075 (GO-2026-11-21-47, -51, -53) »
- Nouveau : « N-075 (GO-2026-11-21-46, -47, -51, -53) »
- Ancien (l. 266) : « Longueur : 575 signes (plafond de 600, mesurée par programme). C'est la ligne du vérificateur (V10), reprise mot pour mot. »
- Nouveau : « Longueur : 580 signes (plafond de 600, mesurée par programme). C'est la ligne du vérificateur de la v2 (V10), avec « -46 » ajouté par le vérificateur de la v3 (source de « sondes en accélérateur »). »

## Relevé de méthode

**Chaîne.** (1) v3 lue en entier, empreinte égale au compagnon. (2) Les textes « nouveaux » de la vérification de la v2 retrouvés dans la v3 (26 sur 27 à la lettre, un avec une précision), aux lignes de la section 14. (3) D-2 de la note sur l'oracle confrontée à la l. 258, mot à mot. (4) Les textes du § 10 confrontés à la règle de la section 8 (« tout texte qui présente le point ») et à la l. 206 : C-1, C-2. (5) Section 7, point 1, confrontée aux l. 191 et 257 : C-3. (6) Ligne pour `CLAUDE.md` mesurée (575, puis 580 avec C-4) ; source de « accélérateur » lue aux l. 45 et 84 et à la ligne `GO-2026-11-21-46`.

**Objets de contrôle.** Unicité des textes anciens : chaque ancien de C-1 à C-4 compté une fois ; objet faux, « GO-2026-11-21-46 » compté cinq fois, donc non retenu comme ancre. Chiffres : 299 et 1 497 rejoués, égaux à ceux de la v3.

**Premier pas non justifié.** Les états « occupé » et « partiellement occupé » viennent, à travers la v3 et la vérification de la v2, d'une lecture des voisins non contre-lue, que je n'ai pas ouverte : je vérifie la fidélité de la v3 à ces pièces, non leur justesse.
