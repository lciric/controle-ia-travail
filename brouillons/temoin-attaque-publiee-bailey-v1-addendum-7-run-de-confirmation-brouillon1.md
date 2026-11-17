# Addendum 7 au préenregistrement du témoin de Bailey (`prereg/temoin-attaque-publiee-bailey-v1.md`, `fb6c2f34…`) — run de confirmation au régime complet (72 tours), décidé avant la lecture du verdict à 36 tours — brouillon 1

16 novembre 2026. Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`), branche
`claude/compassionate-meitner-d4ryyk`. **Brouillon 1 : non contre-lu (R2), non scellé.** Le préenregistrement et ses
addenda 1 à 6 restent tels quels ; en cas de conflit, le préenregistrement prime et l'écart est un nœud. **Écrit et à
sceller avant toute lecture du verdict à 36 tours** : aucune note de sonde ni de juge n'a été lue, par aucune session.

## 1. Pourquoi
La relance seule (addenda 5 et 6) a fini le 15 novembre vers 11:52Z par la garde de dépense (D = 73,026 USD sur B = 75) :
**36 tours complets**, aucune garde tombée, transfert complet, instance détruite
(`runs/temoin-bailey-v1-20261111/sortie-conduite-v13/bilan-conduite-v5.json`). Dossier de lecture assemblé :
`runs/temoin-bailey-v1-20261111/lecture-assemblee-v1/` (45 fichiers scellés vérifiés le 16 novembre). Le texte lit ce run
comme un run tronqué de K′ = 36 tours, au régime réduit (l. 165, 332, 338). Le verdict n'est pas lancé.

Choix soumis à Lazar avant toute lecture (note `registres/passations/2026-11-16-…-bailey-choix-1-suspendu-question-ordre.md`) ;
mot de Lazar, verbatim : « go 2 puis 1 » (note `…-decision-lazar-bailey-2-puis-1.md`) : (i) cet addendum, scellé ;
(ii) puis le verdict à 36 tours (R13) ; (iii) puis un run neuf de 72 tours, au régime publié.

**Lenteur de la relance** (champs techniques seulement) : tours 0 à 35 de 36 à 133 min, croissance presque régulière
(`principal-relance/transfert-1/sortie-durees-v3.jsonl`, `@@`), 48,7 h pour 36 tours ; tours 0 à 7 de la première
exécution de la série 3, sur une autre machine (Texas, 146915), 21,6 à 26,4 min, sans croissance (`9ff59e4b…`).
Diagnostic en lecture seule du 15 novembre (`runs/temoin-bailey-v1-20261111/diagnostic-hetzner-v1-sortie.txt`, `@@`) :
processus d'exécution à 576 % de processeur, carte à 0 % ; ≈ 16 min entre la sauvegarde d'une sonde et celle des
paramètres, ≈ 1 h 30 entre ces paramètres et la sonde suivante : la partie lente est sur le processeur (lecture de la
session, non établie : vraisemblablement l'entraînement de la sonde sur la banque qui grossit). La machine du Texas
(AMD EPYC 7V12, 32 cœurs effectifs, 2,45 GHz) est louable le 16 novembre (offre 59431043, 1,108 USD/h).

## 2. Écarts décidés par Lazar (« go 2 puis 1 »), actés par cet addendum
1. **Run de confirmation (écart à R3 et à la liste d'arrêt : une série nouvelle après la relance).** Une série neuve,
   **décidée et scellée avant toute lecture** : ce qui la rend compatible avec l'objet de R3 (aucun résultat connu ne
   la motive ; elle est engagée quel que soit le verdict à 36 tours). Tout du texte s'applique sans changement :
   hypothèse, prédictions, métriques, seuils, population, juge, modèle, bras, graines (pilote 1394228342, run principal
   1865327867), critères de lecture gelés, liste d'arrêt (pilote, au plus une reprise ; règle ; run principal ; au plus
   une relance), audit de symétrie. Code : celui de l'addendum 5, plus la garde du point 3.
2. **Poste neuf, B neuf (écart au texte, l. « Toute envie de changer … le plafond B après la création de la première
   instance du poste »).** La série de confirmation est un poste neuf : D compte de zéro à sa première instance ;
   **B = 85 USD**, garde à B − 2. Pourquoi 85 : pour que la règle donne K = 72 jusqu'à c = 1,6 USD/h et t = 1 800 s
   (72 000 × (85 − 10 − 8) / (23 × 1,6 × 1 800) ≈ 72,8, avec D ≤ 8 USD au calcul) et que la garde B − 2 laisse
   ≈ 70 h de run à 1,11 USD/h. Les séries 1 à 3 et la relance gardent leur B = 75 et leur D.
3. **Garde neuve : durée de tour du pilote** (code `lanceur_v21`, `Conduite(t_max_pilote_s=1800)`) : si t (durée de
   tour mesurée au pilote, la même que la règle) dépasse **1 800 s**, arrêt avant le run principal, transfert,
   destruction ; nœud. Pourquoi 1 800 : 1,37 × t du pilote de la série 3 (1 315,99 s) ; les tours 0 et 1 de la relance
   (2 187 et 2 340 s) l'auraient fait tomber. Perte bornée : mise en place et pilote (≈ 2 h, ≈ 3 USD).
4. **Filtre d'offre** (paramètre de lancement, déclaré) : celui du poste v12, plus `cpu_cores_effective >= 32` et
   `cpu_ghz >= 2.4` ; offre la moins chère qui passe. Disque 110 Go.
5. **Crédit (comme la condition 9′ de l'addendum 6)** : avant la création, crédit ≥ S = 13,5 h × (max(1,7 ; c₀) + o) et
   ≥ 25 USD, recharge automatique configurée ; 13,5 h = mise en place ≤ 0,75 h + pilote ≤ 1,5 h + 20 tours × 1 800 s
   × 1,15 ≈ 11,5 h ; relevé consigné dans l'ordre de lancement.

## 3. Lecture (fixée maintenant, avant toute lecture)
- **Verdict à 36 tours** (étape « 1 » de Lazar) : prononcé d'abord, par un lecteur neuf (R13), sur
  `lecture-assemblee-v1`, avec les critères gelés ; c'est le verdict du texte pour les séries 1 à 3 et la relance,
  au régime réduit (K′ = 36). Il ne change ni la décision de lancer la confirmation, ni sa lecture.
- **Verdict de confirmation** : par un lecteur neuf (R13), sur la sortie de la conduite de confirmation, avec les mêmes
  critères gelés (`lecture_v8.valider`, `lire` avec `analyse_v3.graines()["reechantillonnage"]`, audit de symétrie).
- **Rapport du témoin** : les deux verdicts, côte à côte, chacun avec son K′ ; leur accord ou leur désaccord est rapporté
  tel quel ; aucune mise en commun des notes. Si la confirmation atteint le régime publié (K′ ≥ 71, l. 331), son verdict
  est **le verdict du témoin au régime publié** ; le verdict à 36 tours reste rapporté comme la lecture prévue au régime
  réduit. Sinon (K′ < 71 : garde de dépense, interruption, garde du pilote), la confirmation est rapportée selon le texte
  (régime réduit si K′ ≥ 20 ; pas de verdict sinon), et le verdict du témoin reste celui à 36 tours.
- Aucune autre série sans nouvelle décision de Lazar et nouvel addendum.

## 4. Code, essais
`lanceur_v21` (= `lanceur_v20` plus la garde du point 3 ; `@@`), au commit `@@` ; instance (`instance_v16`), exécution
(`execution_v4`), lecture (`lecture_v8`), journaliseur, conventions, analyse : inchangés. Manifeste neuf
`manifeste-local-v7.json` (B = 85 ; seules différences avec le v6 : `B`, `commit_code`). Essais :
`tests/test_temoin_bailey_condition6_v21.py` (`@@`) : les essais v20 rejoués, plus la garde (sous le plafond : run
principal ; plafond atteint : passe ; au-dessus : arrêt avant le run principal, instance détruite) ; résultat : `@@`.
Pièces de lancement : conduite `lancer-conduite-v15.py` (conduite normale, `t_max_pilote_s=1800`, aucune instance
antérieure), poste `poste-hetzner-v13.sh` et constructeur (filtre du point 4). `@@`

## 5. Risques déclarés
- (a) l'hypothèse « processeur » n'est pas établie ; un hôte rapide au pilote peut ralentir ensuite (croissance) : la
  garde B − 2 tronque alors le run (lu au régime réduit si K′ ≥ 20) ;
- (b) la machine du Texas peut ne plus être louable ; une autre machine qui passe le filtre n'a pas été éprouvée ;
- (c) ce que l'addendum 6 déclarait pour le crédit et la recharge automatique (carte de Lazar, compte partagé avec
  d'autres chantiers) vaut ici ;
- (d) graines identiques à celles du texte : la confirmation n'est pas un réplicat indépendant de la relance ; elle teste
  le même protocole au régime publié (choix de rester dans le texte : changer les graines serait un écart de plus).

## 6. Conditions de lancement
Celles du texte et de l'addendum 5, avec : condition 2 = une **ligne de GO neuve sur `main`** (inscrite par la session
mère), de type « calcul », dont l'objet cite le texte (`fb6c2f34`), le devis v4 (`f9c8c66e`) et cet addendum, et fixe
« (B = 85, garde d'horloge à B − 2) », plafond ≥ 85 USD ; condition 7 = le mot direct de Lazar pour le lancement ;
condition 9′ = le point 2.5 ; **le verdict à 36 tours prononcé et scellé avant la création** (ordre « 2 puis 1 » :
l'addendum est scellé avant la lecture, le run est lancé après). Proposition de ligne pour la mère :
« | GO-2026-11-1x-NN | 2026-11-1x | calcul | Témoin de Bailey, run de confirmation au régime complet (addendum 7, `@@`) ;
texte `fb6c2f34`, devis v4 `f9c8c66e` prolongé par l'addendum 7 (B = 85, garde d'horloge à B − 2) | 90 USD |
2026-11-30 | Lazar | addendum 7 | ».

## Contre-lecture
À venir (R2).
