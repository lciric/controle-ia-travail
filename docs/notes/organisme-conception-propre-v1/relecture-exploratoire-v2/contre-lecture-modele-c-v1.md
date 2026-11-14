# Contre-lecture de la relecture exploratoire v2 par un sous-agent neuf de modèle C — rapport versé tel quel — v1

Versé par le préparateur (modèle A), le 14 novembre 2026 à 12:49 UTC. Contre-lecteur : sous-agent neuf de modèle C,
lancé de 12:41:22 à 12:48:01 UTC (`date -u`) depuis la racine du dépôt par
`claude -p --model sonnet --safe-mode --no-session-persistence --output-format text --allowedTools Read Grep Glob
'Bash(unshare -n:*)' 'Bash(sha256sum:*)' 'Bash(ls:*)' 'Bash(wc:*)' 'Bash(diff:*)' < consigne` ; consigne : `contre-lecture/consigne-contre-lecture-v1.md`
(`e89b8111…`). Il a lu les pièces scellées aux empreintes du moment (règle `56c58b09…`, témoins `bb4f903f…`,
hasard `5cef38f6…`, outil `b1f3e0c5…`, classement `2d8bf35a…`, devis `ac97614e…`). **Il n'a joué aucun essai** : le harnais a refusé
ses commandes `unshare` (motif d'autorisation mal formé de ma part) ; les essais et bancs ont été joués par le préparateur
(voir `rapport-v1.md`). Le texte ci-dessous, après le trait, est sa sortie, octet pour octet.

---

# Contre-lecture neuve — relecture exploratoire v2 (règle, témoins, hasard, outil v3.2, devis)

**Verdict : utilisable sous conditions.** Je n'ai trouvé aucun défaut bloquant dans les pièces : empreintes concordantes, règle fidèle à l'engagement pour l'essentiel, garde de dépense saine, calculs du devis justes. Mais je n'ai pas pu jouer les essais et les mutations, et deux points de lecture ou de montant doivent être traités avant de s'engager (M1, M2, M4).

## Constats

### Bloquant
Aucun.

### Moyen

**M1. L'étiquette « séparation de forme » n'est pas fondée.**
- Où : `regle-v2.md` § 6.7 ; `classer_conception_propre_v3_2.py:219-228`.
- Le test de R7 seul compare 23 réelles à 8 idées au hasard.
- Calcul de ma part : avec 13 réelles sur 23 à R7 = 1 (taux de la première lecture, cité par l'audit), p vaut 0,0055 si le hasard fait 0 sur 8. Il passe à 0,058 (> 0,05) dès 1 sur 8.
- Donc « séparation réelle » exige que le lecteur rejette les 8 fiches. Or 6 des 8 ont une chaîne cohérente avec le signe, par construction.
- Et p > 0,05 ne prouve pas « de forme » : c'est un manque de puissance.
- Correction : remplacer « séparation de forme » par « séparation non établie sur R7 (n = 8) ». Dire d'avance le seuil (0 sur 8 pour 13 sur 23). Rapporter toujours R7 du hasard selon la chaîne (déjà prévu au § 7).

**M2. Le hasard v2 reste reconnaissable, ce qui peut fausser L5 v2. Le contrôle de style ne couvre que la longueur.**
- Où : `temoins-hasard-v2.json` ; `outils/resultat-stats-forme-reelles-et-temoins-v2-v1.json` ; `regle-v2.md` § 5 et § 6.7 (« style comparable »).
- **Dispersion trop faible.** Longueurs totales du hasard : 3 741 à 4 101. Chez les réelles : 3 104 à 5 687.
- **Phrases.** Phrases par fiche : 39 à 45 chez le hasard (réelles : médiane 34, q1 29, q3 43). Mots par phrase : médiane 16,4 (réelles 20,8, q1 17,4).
- **Fragments répétés.** Absents des 12 témoins du lecteur (comptés par `grep`), répétés dans le hasard :
  - « moins de budget par appel » : 3 occurrences ;
  - « entier supérieur » : 4 ;
  - « Il faut enfin » : 2.
  Le contrôle « 6 mots » (`controler_temoins_v2.py`) les laisse passer. Ce sont des remplissages de gabarit, mais ils se voient.
- **Contenu.**
  - 5 opérations sur 8 sont « réduire de moitié ».
  - Les objets sont tous des constantes numériques, sans levier « proposeurs ».
  - T2-H1 répète un groupe nominal de dix mots et finit sur une phrase boiteuse (« Tout tient à ce que plus … augmente, moins … »).
- Les limites 5 et 7 du § 9 ne disent rien de ces traits ; le § 6.7 affirme « fiches de longueur et de style comparables ».
- Correction, au choix :
  1. déclarer ces traits au § 9 et lire « séparation réelle » avec cette réserve ;
  2. avant tout appel, régénérer avec deux contrôles de plus : dispersion de la longueur totale (écart interquartile ≥ la moitié de celui des réelles) et phrases par fiche et mots par phrase dans [q1, q3].

**M3. Les publiées reprennent le vocabulaire du catalogue : L1 mesure une reconnaissance lexicale.**
- Où : `temoins-lecteur-v2.json`, T2-C7 et T2-C1 ; `regle-v2.md` § 9.
- T2-C7 (version du tour 2, réécrite parce qu'une citation n'était pas mot pour mot) reprend presque mot à mot l'entrée C7 : « probabilité de fausse adoption bornée par décision, même sous arrêt optionnel », « garder si le score a monté ».
- T2-C1 fait de même pour C1 (cotes Elo, débats à plusieurs tours, paires entre cartes proches).
- Le mécanisme central est bien conservé et la source n'est pas nommée. Mais L1 (≥ 5 sur 7) ne peut guère manquer (7 sur 7 à la première lecture).
- Correction : ajouter un point au § 9 : « L1 dit que le lecteur reconnaît un mécanisme dans ses mots du catalogue, pas dans une paraphrase ».

**M4. Plafond proposé = tout le reste de la ligne (11,65 USD), alors que le mot de Lazar dit ≈ 3 USD.**
- Où : `devis-v1.md` § 3.
- Dépense attendue : 2,69 USD. Cas extrême (sortie ×3) : 5,51 USD, avec un plafond minimal de 6,32 USD pour que les 18 appels passent.
- À 11,65, l'exposition est environ 4 fois l'attendu.
- Correction : `--plafond-usd 6.5`. La constante 11,65 de l'outil reste le plafond absolu. Le seuil du premier appel devient (6,5 − 1,117) / 16,2 ≈ 0,33 USD ; le premier appel attendu coûte 0,158 USD.

**M5. Les relecteurs de l'épreuve sont décrits de deux façons.**
- Où : `regle-v2.md` § 4 (« `claude -p --model sonnet …` lancé hors du dépôt » et, quatre lignes plus bas, « aucun appel payant (sous-agents de la session) ») ; `devis-v1.md` § 4.
- Si ces appels sont facturés, la dépense manque dans `registres/depenses.md`.
- Je n'ai trouvé aucune ligne de dépense pour l'épreuve après R-2713.
- Correction : une phrase qui dit lequel des deux cas s'applique, et la ligne de dépense si besoin.

**M6. Les fausses fiches ne sont pas « complètes ailleurs » au sens strict (B3).**
- Où : `epreuve/resultat-epreuve-tour1.json`, T2-F1 et T2-F3 ; `temoins-lecteur-v2.json`, clé `attendu`.
- T2-F1 : R7 lu 0 et 0 au tour 1 (voulu 1), puis 0 et 1 au tour 2. `attendu` R7 est fixé à 0.
- T2-F3 : R7 lu 1 et 0 au tour 1, « non fixée ».
- L2 ne porte que sur le critère visé, donc il n'est pas touché. Mais l'auteur a mal calibré R7 sur 4 témoins (F1, C1, C3 et F3).
- R7 est le critère le moins stable entre relecteurs : 9 accords sur 12 au tour 2.
- Les `attendu` des critères non porteurs sont le consensus de la famille C (R5 de C2, R4 de C11…) : « l'exactitude du lecteur » est donc circulaire. C'est dit au § 4 (limite), mais pas pour cet usage.
- Seuls T2-V et T2-J ont R7 = 1 aux quatre lectures.
- Correction : au § 7, marquer l'exactitude comme descriptive et circulaire pour les critères non porteurs.

### Mineur

- **m1. « Sans écart » n'est pas exact.** `regle-v2.md:8` dit que la règle reprend l'engagement sans écart. Or le § 4 ajoute « les onze autres gardent leurs valeurs du tour 1 » et fait rejouer les 12 témoins au tour 2. L'engagement (§ 6) ne prévoit que la réécriture du témoin en désaccord. Aucune pièce scellée ne date cette sous-règle d'avant le tour 2. Correction : le déclarer comme écart.
- **m2. Verdict ambigu quand le classement est non lisible.** `classer…v3_2.py:428-430` écrit « E2 v2 … ; séparation réelle » si L5 rejette alors que L1–L4 manquent. Correction : « (non lue) » dans ce cas.
- **m3. Codage de la chaîne de T2-H5.** `tirer_fiches_hasard_v2.py:783` : signe « 0 » mais `sens_predit = −1`, métrique « coût ». Le « 6 chaînes sur 8 » repose sur ce codage. À dire au § 5.
- **m4. T2-V reste discutable.**
  - Il est cohérent avec les faits (composantes conditionnelles, `faits-v1.md` § 4) : le mécanisme implique le signe +, et il est absent du catalogue.
  - T2-J est bien la même idée, avec les mêmes nombres (10 %, 80 %, 20 mondes, 1 loi fausse et 1 copie).
  - Mais il passe à deux appels par proposeur et par génération, alors que `faits-v1.md` § 4 fixe un appel (C3 §5.1).
  - Une mise à jour de l'archive à mi-génération implique aussi e-BH et test de mort ; la perte_traduction ne parle que de la vue servie deux fois.
  - L'antériorité Gauss-Seidel/Jacobi est « SUPPOSE », non vérifiée.
  - Un lecteur strict peut donc lire R3 ou R7 à 0 sur T2-V et T2-J (comme T-V en v1).
- **m5. Réserve du lecteur.** `prix-astra-v2.md:29` mentionne une « réserve du lecteur » de 2,74 USD. Confirmer que R-2726 la rend sans objet (la ligne GO-2026-11-13-06 reste la seule borne).
- **m6. Banc de mutations sans trace.** Aucun résultat du banc n'est archivé dans `RE/`. Les 40 mutants ne couvrent que le changé, et aucun compte « tués sur N » n'est donné.
- **m7. Limite de la garde C6 v3.2.**
  - La garde refuse le second dossier, la première lecture absente ou altérée, et un relevé incohérent.
  - Mais si `lecture-g1-v3-2/` (journal et manifeste) est supprimé en entier, une nouvelle préparation repart à zéro. C'est la même limite qu'en v3.1.
  - `--depense-anterieure-usd` est libre (≥ 0).
  - Elle tient grâce à la condition 2 ci-dessous.

## Réponses par question

**A. Règle**
1. Le choix de R7 en composante est justifié avant lecture : l'engagement est antérieur (11:38:57) et le texte du § 2 est identique. Les risques sont dits honnêtement, y compris le recalcul de l'audit (p ≈ 0,21).
2. **Définitions.**
   - L1, L2, L3 v2, L4 et L5 v2 sont nettes ; le code les applique à l'identique.
   - Aucune issue n'est jouée d'avance : E3 v2 est même plausible, puisque le hasard fluide passe les portes.
   - En revanche, « séparation réelle » n'est atteignable qu'avec un hasard à 0 sur 8, et « forme » n'est pas fondé (M1).
3. La section « ne peut pas dire » est bonne mais incomplète : lexique des publiées (M3), traits du hasard (M2), antériorité non vérifiée de T2-V (m4), `attendu` circulaires (M6).
4. Écarts de la règle par rapport à l'engagement : un seul, m1. Les autres reprises sont conformes (graines, portes, S v2, C v2, séparation, R4 du programme).

**B. Témoins du lecteur**
1. **Gabarit.**
   - Médiane de longueur totale : 3 882 (réelles 4 174, 3 508–4 840).
   - Antériorités : 4. Types : 10 « question » / 2 « approche ». Signe : 11 « + ».
   - Écarts déclarés : moins de parenthèses, phrases par fiche plutôt basses (29 contre 34).
2. **Publiées.**
   - Mécanisme central conservé.
   - Aucune source nommée hors citations obligatoires (`grep` : seuls « Elo » et « Semantic Scholar », qui sont dans le catalogue).
   - Réserve : M3.
3. **Fausses.** F2 est propre. F1 et F3 : M6.
4. **T2-V et T2-J.** Sains avec la réserve m4.
5. **Épreuve.**
   - Conforme au § 6 : critère porteur en désaccord → réécriture une fois ; non porteur → valeur commune, sinon « non fixée ».
   - Les valeurs du fichier final correspondent aux décisions des deux tours.
   - Les fiches du fichier final sont identiques à celles de `temoins-lecteur-v2-epreuve-2.json` (comparaison par empreinte sur le JSON trié, hors `attendu`/`epreuve`).
   - Le tour 2 n'a servi qu'à confirmer T2-C7.
   - Le motif du tour 1 était une citation non littérale, non un désaccord de fond ; la réécriture a rapproché T2-C7 du catalogue (M3).

**C. Hasard**
1. **Tirage.**
   - Les signes des maillons sont tirés (`rng.choice`) indépendamment du signe prédit, qui vient de l'urne des valeurs réelles.
   - Le sens de la chaîne est le produit des maillons. 6 chaînes sur 8 sont cohérentes avec le signe, ce qui est compatible avec le hasard.
   - `sens_operation` n'est pas utilisé dans ce produit : la direction de l'opération est déjà dans le premier maillon, donc sans conséquence.
2. **Fluidité.** Lisible et de longueur réelle (médiane 3 990). Phrases-types absentes au seuil 6 mots, mais voir M2 pour les fragments de 4–5 mots.
3. **Réglage sur une lecture.** Aucun signe. Le rejet de la première sortie est documenté et motivé par la langue et la longueur seulement. Le compte « 6 sur 8 » a été vu pendant les corrections, ce qui est dit.
4. **Traits reconnaissables.** Oui, mineur à moyen : M2.

**D. Outil v3.2**
1. Le différentiel ne contient que des changements nécessaires : nom de manifeste, dossier, pièces v2, plafond, garde, parents[5], noms `-v3-2`.
2. **Garde C6.** Elle bloque le second dossier, la première lecture absente ou altérée, et un relevé incohérent (relevé réécrit et réépinglé compris). Limite m7.
3. **Plafond absolu 11,65.** Juste : floor(21 − 6,791087 − 2,556635) = 11,65. Les trois pièces épinglées de la première lecture ont les empreintes attendues sur disque (`86bc90dc…`, `00354642…`, `e22de7bf…`) ; le relevé porte `depense_comptee_usd` = 2,556635.
4. **Règle de lecture.** Inchangée (diff) : consigne, question, faits, catalogue et prix sont épinglés aux mêmes empreintes ; le test `test_regle_de_lecture_inchangee_v3_1_v3_2` existe.
5. **Classement.** Conforme à la règle v2 : portes R2 et R3, S v2 (R1 + R4 + R5 + R6 + R7), C v2, L3 v2 (R7 = 1 prouvé dans au moins une lecture), L5 v2 (graine 2026111303), séparation (graine 2026111404), aucune désignation (`designees: []`), descriptifs. Réserve m2.
6. **Essais et banc.** 127 fonctions de test, dont 14 neuves. Elles couvrent :
   - la première lecture manquante, altérée ou incohérente ;
   - le second dossier et le manifeste hors motif ;
   - le plafond ;
   - L3 ;
   - la séparation ;
   - les descriptifs.
   Les 10 essais retirés concernent la désignation et la variante « détachée ». Je n'ai pas pu les jouer (voir Réserves). Banc : m6.

**E. Devis**
- **Octets.** 977 646 / 875 674 = +11,6 %. Jetons d'entrée : 977 646 × 0,2626 ≈ 256 700.
- **Coûts.** Recalculés à 5 USD / 25 USD par million (Flex, `prix-astra-v2.md:13`) : 2,69 attendu, 3,39 (×1,5), 4,10 (×2), 5,51 (×3), 10,28 (20 000 jetons de sortie par appel), 19,73 au pire cas. Tous justes.
- **Autres calculs.** 16,2 = 13 + 4 × 0,8 ; dix appels au pire cas tiennent dans 11,65 ; le seuil du premier appel de 0,65 USD est exact.
- **Plafond.** Voir M4.

## Conditions d'emploi

1. Les empreintes de toutes les pièces `RE/` égalent leurs compagnons `.sha256` (déjà vérifié, voir plus bas) ; à refaire juste avant `preparer`.
2. Avant `preparer`, par programme :
   - `find docs runs -name 'manifeste-envois-v3*.json' -o -name 'manifeste-relecture-v3*.json'` ne rend que le manifeste de la première lecture ;
   - `docs/notes/organisme-conception-propre-v1/lecture-g1-v3-2` n'existe pas ;
   - l'arbre git est propre.
3. Jouer sous `unshare -n`, avec rapport archivé :
   - `essais_lecture_classement_v3_2.py` ;
   - `outils/essais_temoins_et_hasard_v2.py` ;
   - le banc de mutations v3.2.
   Ne lancer qu'avec 0 échec et 0 mutant vivant.
4. Paramètres : palier Flex, effort `medium`, `--depense-anterieure-usd 0`, `--plafond-usd 6.5` (M4). Contrôle du premier appel : ≤ 0,33 USD avant d'envoyer les 17 autres.
5. Avant le lancement : trancher M1 et M2 (renommer l'issue « forme » ; déclarer ou corriger les traits du hasard), M3 (point au § 9) et M5 (statut de l'épreuve).
6. Rapporter, avec le verdict : R7 retenu du hasard selon la chaîne, le p de R7 seul, et la mention « exploratoire, aucune désignation ».
7. Après la lecture, inscrire la dépense dans `registres/depenses.md` (ligne GO-2026-11-13-06).

## Ce que j'ai fait

- **Lu intégralement :**
  - `regle-v2.md`, `engagement-avant-epreuve-v2.md`, `devis-v1.md` ;
  - l'audit de propreté ;
  - le catalogue ;
  - les trois différentiels `*.diff` (outil, classement ; essais surtout par liste des tests ajoutés et retirés) ;
  - `classer_conception_propre_v3_2.py` (lignes 108-391 et verdict) ;
  - `epreuve_valeurs_attendues_v1.py` ;
  - la décision R-2726 et les lignes de dépense.
- **Lu en partie :**
  - `temoins-lecteur-v2.json` et `temoins-hasard-v2.json`, par `jq`. Texte complet des fiches T2-V, T2-J, T2-H1 et T2-H5 ; énoncé, demande et perte_traduction des autres témoins du lecteur ; structure et chaîne des 8 fiches du hasard.
  - `tirer_fiches_hasard_v2.py` : en-tête, tirage des maillons, assemblage.
  - `faits-v1.md` §§ 1-5.
  - `resultat-controles-temoins-v2.json`, les statistiques de forme v2, `resultat-epreuve-tour1/2.json`.
  - `essais_lecture_classement_v3_2.py` : les tests de C6 (lignes 2370-2425).
- **Non ouverts :** `conception-course-v1.md` §§ 4-7, `consigne-lecteur-v1.md`, la question, `temoins-plantes-v1.md`, `temoins-hasard-v1.json`, `temoins-lecteur-v1.json`, l'outil v3.1 et son rapport (j'ai confronté le v3.2 au v3.1 par le différentiel seulement), les messages et réponses de `RE/epreuve/`, `mutations_hasard_v2.py`, `essais_temoins_et_hasard_v2.py`, `stats_forme_fiches_v1.py`.
- **Empreintes (`sha256sum` contre le compagnon lu par `cat`)** : `regle-v2.md` `56c58b09…`, engagement v2 `27ffad3a…`, témoins du lecteur `bb4f903f…`, témoins du hasard `5cef38f6…`, devis, les deux résultats d'épreuve, générateur et contrôles du hasard, les quatre programmes et les trois différentiels de `lecture-classement-v3-2/` : tous égaux. Sur disque, les trois pièces de la première lecture (manifeste, journal, relevé) ont aussi l'empreinte épinglée par l'outil.
- **Calculs refaits à la main (sans Python) :** barème du devis, plafond 11,65, seuil du premier appel, probabilité du test de R7 seul (0,0055 et 0,058), longueurs et dispersions du hasard.
- **Aucune fiche réelle ni note du juge ouverte.** Rien écrit dans le dépôt.

## Réserves

- **Je n'ai joué aucun essai.** Le harnais a refusé toute commande commençant par `unshare` (même sans Python), donc je n'ai pas lancé `pytest` ni les sondes C6. Les verdicts D2 et D6 reposent sur la lecture du code, du différentiel et de la liste des essais.
- Je n'ai pas relu les 7 conceptions publiées contre les PDF sources, ni vérifié l'antériorité de T2-V (pas de réseau).
- Je ne peux pas confirmer que les témoins ont été écrits sans lire les fiches réelles, ni la chronologie des heures annoncées.
- Les textes de T2-H2, T2-H3, T2-H4 et T2-H6 à T2-H8 n'ont été lus que par leur structure ; l'impression de « traits communs » vient de leurs champs, de deux fiches complètes et de comptages de fragments.
- Mes calculs de p ne valent que pour un taux de 13 sur 23 chez les réelles ; la relecture peut donner un autre taux.
