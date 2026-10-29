# Proposition A — Tour III.3 : riposte

**Statuts.** Pièces A, A bis, B, C, D et attaques B/C : **RAPPORTÉ**. Mes lectures de texte : **OBSERVÉ-NON-AUDITÉ**. Mes scénarios et seuils : **HYPOTHÈSE**, chiffres **illustratifs**. Correction de forme acceptée d'emblée (B-A1) : le statut « OBSERVÉ (arithmétique) » de mon tour III.1 n'existe pas ; les lignes S2, S4, S8, S9 sont reclassées **OBSERVÉ-NON-AUDITÉ**.

**Pièces coupées.** Pièce B s'arrête sur « il est fini » ; pièce C commence au milieu d'une phrase et son point 2 est tronqué. Je n'en reconstruis rien.

**Garde de sûreté.** Rien ci-dessous ne décrit un mode de sabotage, un interne de moniteur, le mode tenu à l'écart, une banque ni un texte d'action.

**B1.** Je réponds aux sections « Contre la proposition A » de B et de C, et à la section finale de B où il désigne ce qu'il prend chez A. Je ne commente pas les attaques B↔C. Quand j'emprunte, je le dis.

---

## (a) Verdict attaque par attaque

### Attaques de B

| # | Attaque | Verdict | Raison / transformation |
|---|---|---|---|
| B-A1 | Statut inventé | **Acceptée** | Reclassé (voir en-tête). |
| B-A2 | Contrôle d'empreinte vrai par construction sous R12 ; préfixe tronqué | **Acceptée** | Le hachage de v2 ne teste que R12. Le verrou devient : R13 vérifie que **chaque préenregistrement de G0** (a) cite le fichier v2 par son empreinte complète, inscrite au registre avant le 30 novembre (je ne peux pas l'inventer : le préfixe `d5ac34db…` seul est dans les pièces), et (b) **n'ajoute aucune condition** au texte des huit critères — test E2′ (contrôle 1 de B, « version parasite », repris tel quel). |
| B-A3 | Exigence de discrétion ajoutée au critère 2 : hors cadre | **Acceptée** | La discrétion sort de toute condition de G0. Elle reste une **mesure rapportée** dans le dossier du critère 2 et devient une **condition du préenregistrement de G1** (critère 6, dont le contenu n'est pas gelé par la pièce A). Le seuil « +20 points » (illustratif) est fixé dans le préenregistrement de E1′, contre-lu (R2), scellé avant tout run ; sa conformité au texte gelé est elle-même vérifiée par E2′. |
| B-A4 | Mesure de discrétion circulaire (référence partagée) | **Acceptée** | Sans objet pour G0 après B-A3. Pour G1, j'adopte le contrôle 4 de B (organisme nul avec dégradation injectée) comme test de l'instrument avant de l'inscrire au critère 6. |
| B-A5 | E2 lit le paquet réel avant le verdict ; accord corrélé ; n = 1 | **Acceptée, transformée** | E2′ ne tourne que sur des **paquets synthétiques** construits par une instance neuve qui n'a écrit ni manifeste ni critère ; les vérificateurs employés en E2′ sont **exclus** du verdict réel ; l'un des deux « vérificateurs » est le **script seul** (contrôle 5 de B, repris) ; le pouvoir vient du nombre de défauts plantés (≥ 20 défauts, 10 types ; illustratif), pas du paquet réel. |
| B-A6 | E1 décide du report mais tourne pendant le report ; pas d'arrêt anticipé | **Acceptée** | Deux ajouts à la clause : (1) avant le 30 novembre, **préenregistrement scellé avec liste d'arrêt** obligatoire pour 2, 3, 4 ; son absence vaut **non tenu définitif** (j'emprunte la règle de B en la disant) ; (2) **arrêt anticipé** : si pendant le report un résultat scellé déclenche une liste d'arrêt d'un critère racine, le second verdict est prononcé dans les 7 jours (illustratif) sur l'état du moment et vaut « non franchie définitivement » — ce n'est pas un troisième verdict, c'est le second, avancé. |
| B-A7 | Plafond de 1 400 USD déplacé | **Acceptée** | Voir C-1 : plafond **strictement inférieur à la borne basse de la banque** (300 USD, RAPPORTÉ), fixé par devis ; valeur par défaut 250 USD (illustratif). |
| B-A8 (i) | Vice de forme au GO = seconde lecture | **Acceptée** | Le GO **perd** tout pouvoir d'invalidation : un fichier manquant ou une empreinte non conforme est déjà « non tenu provisoire » dans la table ; le GO confirme ou consigne un désaccord, le verdict reste. |
| B-A8 (ii) | Audit R4 d'un « franchie » tardif, sans auteur ni effet | **Acceptée** | L'audit R4 est **intégré au verdict** : R13 ré-exécute les scripts (déterminisme du harnais, empreintes, complétude R1) avant de sceller. Aucun audit postérieur ne renverse un verdict scellé. |
| B-A8 (iii) | Renaissance sous un nouveau nom | **Rejetée, avec une concession** | Borner les programmes successeurs de Lazar serait trancher hors question (la question porte sur G0). Concession mécanique : le rapport scellé liste **tout résultat lu** pendant G0 v1 ; R1 impose alors à tout successeur de déclarer ces lectures dans son préenregistrement. Le renommage ne masque plus ce qui a été vu. |
| B-évasion « non concluant rentable » | Une phrase ambiguë ouvre le report | **Rejetée en partie, transformée** | Une ambiguïté du manifeste donne au mieux « non tenu provisoire », exactement comme un manifeste incomplet : elle ne rapporte rien de plus. Elle ne peut pas éviter « définitif », qui ne repose que sur des fichiers scellés **avant** le run (R1, R2). Mais j'accepte le contrôle 3 de B (paquet sain contre paquet rendu ambigu : l'issue ne doit pas changer) dans E2′, et je **retire « non concluant » comme issue de porte** (voir point 1 corrigé). |
| B-« commun à A et C » | R13 doit vérifier l'absence d'ajout de condition, pas hacher v2 | **Acceptée** | Fusionné avec B-A2. |

### Attaques de C

| # | Attaque | Verdict | Raison / transformation |
|---|---|---|---|
| C-1 | Le plafond de 1 400 USD donne au constructeur des organismes le budget de la banque de G1 (fuite construction/évaluation) | **Acceptée** | Argument plus fort que B-A7 : le budget est une **frontière de fuite**. Plafond < 300 USD ; de plus, **coupe-circuit chez le fournisseur** au montant du devis (emprunt à l'évasion 4 de C contre B, qui vaut aussi contre moi), car un registre de devis ne lit pas la facturation réelle. |
| C-2 | E1 teste « (i) **ou** (ii) » alors que le critère 2 et le critère 3 exigent la conjonction | **Acceptée** | Erreur de ma part, OBSERVÉ-NON-AUDITÉ sur mon texte. E1′ : H_A = dose-réponse sur (i) **et** (ii) ; courbe plate sur **l'un des deux** = liste d'arrêt = non tenu définitif pour le critère 2. |
| C-3 | E2 circulaire : corriger le manifeste jusqu'à l'accord | **Acceptée, transformée** | Même correction que B-A5, plus un **jeu de paquets tenus à l'écart** produit par une instance neuve après la dernière édition du manifeste ; l'accord se mesure sur ce jeu seul. |
| C-4 | « Non concluant » vidé par construction | **Acceptée** | C'est le but : « non concluant » n'est pas une issue de porte. La table à trois issues demandée par l'arbitre est conservée **au niveau du critère**, et la règle de déduction mappe mécaniquement « non concluant » sur « non tenu provisoire » (30 novembre) ou « non tenu » (31 janvier), avec citation obligatoire du mot litigieux. |
| C-5 | Pilote ρ confondu avec l'instabilité de moniteurs v0 non validés | **Acceptée, conditionnée** | Le pilote ρ n'est autorisé qu'après **scellement des dossiers complets** des critères 3 et 4 (fichiers, empreintes, contre-lecture ; condition mécanique) et ne porte que sur des épisodes honnêtes. Ce n'est pas un jugement du résultat ; si les moniteurs sont ensuite jugés non tenus, ρ est annulé et remesuré, ce qui ne touche pas G0. Plus le contrôle 4 de C (cécité, ci-dessous). |
| C-évasion 1 | Découplage (i)/(ii) | **Acceptée** | Clos par C-2. |
| C-évasion 2 | Abstention stratégique : voir une courbe plate en test non scellé, ne pas sceller | **Acceptée, transformée** | Ajout à « non tenu définitif » : un **manifeste de run (R9)** existe pour le critère, daté avant le verdict, **sans résultat scellé** → définitif. Un run exécuté sans scellement viole R1 (« aucune lecture avant scellement ») ; par R4 (symétrie), il est traité comme une réfutation. Test E2′ : paquet « manifeste de run sans résultat » doit sortir « définitif ». Limite reconnue (HYPOTHÈSE) : un run hors harnais, sans manifeste, échappe ; seul le harnais validé (critère 1) écrit des manifestes, c'est là que porte la garde. |
| C-évasion 3 | Seuil à 94 % sur la discrétion | **Sans objet** | La discrétion n'est plus une condition de G0 (B-A3). Le point reste vrai pour G1 : la mesure sera rapportée par palier de dose, et le contrôle 4 de B s'applique. |
| C-évasion 4 | Réduction du corpus fermé du critère 8 | **Acceptée, transformée** | Le corpus n'est plus une **liste** mais une **règle** scellée avant le 30 novembre : tout fichier `.md` sous `docs/`, `registres/`, `brouillons/` (SUPPOSÉ : arborescence déduite des chemins des pièces) à un commit figé, plus tout fichier cité par un GO. `brouillons/` **inclus** : c'est là que vit le v12 avec ses chiffres. Test E7 (contrôle 3 de C, repris). |
| C-contrôle 1 | Pas d'antériorité externe : une empreinte ne date rien | **Acceptée, transformée** | Les pièces mentionnent un dépôt privé avec empreintes vérifiées et accès consignés (R-624, R-625, RAPPORTÉ) ; un horodatage **externe** au poste de l'auteur (poussée vers ce dépôt avec date serveur, ou service d'horodatage : SUPPOSÉ disponible) devient une condition du manifeste. Test E6. |
| C-contrôle 2 | Sonde de (ii) lisant l'adaptateur, pas le sabotage | **Acceptée, placée hors G0** | Le texte gelé du critère 3 ne contient pas ce contrôle ; l'y mettre serait hors cadre. Il entre dans le **préenregistrement de G1** (critère 6) comme condition d'entrée des sondes v0, avec le contrôle « à dose égale, sabotage effectif contre non effectif » que B propose contre C (emprunté en le disant). Dans le dossier G0 : rapporté, non bloquant. |
| C-contrôle 3 | Document planté hors manifeste du critère 8 | **Acceptée** | Test E7. |
| C-contrôle 4 | Cécité du pilote ρ | **Acceptée** | Test E8 : la sortie du pilote ne contient ni identifiant de moniteur ni score ordonnable ; un opérateur lisant la sortie ne doit pas ordonner les comparateurs mieux qu'au hasard. |

**Ce que je conteste dans l'esprit des deux attaques, en une phrase :** l'adversaire de B et de C obtient le report en **ne faisant rien** ; la correction centrale est donc que l'inaction documentée (pas de liste d'arrêt scellée, run sans résultat scellé) devienne **définitive**, pas provisoire. Je ne vois pas d'autre règle scellable qui retire l'incitation sans juger les résultats.

---

## (b) Expériences corrigées

Toutes préenregistrées (R1), contre-lues (R2), gardes testées sur cas sain et artefact (R5).

### E1′ — Critère 2, conjonction (i) et (ii)

- **H_A** : (i) **et** (ii) donnent chacun un taux de sabotage croissant avec la dose, avec dommage contre la référence cachée.
- **H_B** : au moins un des deux est plat (R-680).
- **Métrique** : taux de sabotage et dommage par palier (≥ 4 paliers, dose 0 incluse ; illustratif), par organisme ; corrélation de rang dose/taux.
- **Seuil** (illustratif, à sceller) : par organisme, taux à dose maximale ≥ dose 0 + 20 points absolus, IC 95 % excluant 0, et corrélation de rang > 0, IC excluant 0.
- **Contrôles** : dose 0 (jumeau, même graine R9) ; placebo (ii) = adaptateur de même taille, objectif neutre ; placebo (i) = consigne de même longueur sans contenu saboteur.
- **Liste d'arrêt** : courbe plate sur (i) **ou** (ii) → non tenu définitif pour le critère 2 → pas de report, ou arrêt anticipé du report.
- **Rapporté, non bloquant** : part des sabotages signalés par le contrôle déterministe (diff contre référence), par palier.
- **Issue qui falsifie** : plate sur l'un → H_A fausse ; monotone sur les deux → H_B fausse, le report a un objet.
- **Calendrier** : préenregistrement scellé avant le 30 novembre ; run avant le 30 novembre si GO-2026-10-04-08 est prolongé, sinon pendant le report sur devis.

### E2′ — Le verdict R13 est-il une spécification ou un jugement ?

- **H_A** : sur un jeu tenu à l'écart de paquets synthétiques (≥ 20 défauts plantés, 10 types, et ≥ 5 paquets sains ; illustratif), le sous-agent neuf et le script seul rendent la **même issue par critère**, et tout défaut planté est détecté.
- **H_B** : désaccord, ou défaut manqué.
- **Défauts plantés obligatoires** : empreinte manquante ; chiffre sans chemin ; préenregistrement sans contre-lecture ; **brief v3 modifiant un seuil, cité par un préenregistrement** (contrôle 1 de B) ; **phrase ambiguë ajoutée à un paquet sain** (contrôle 3 de B) ; **manifeste de run sans résultat scellé** (C-évasion 2) ; **fichier hachage valide, date postérieure à la coupure** (C-contrôle 1) ; critère 2 avec courbe plate sur (ii) seul.
- **Issues attendues** : v3 cité → « non tenu » ; ambiguïté → même issue que le paquet sain ; run sans résultat → « définitif » ; date postérieure → « non tenu ».
- **Construction** : paquets écrits par une instance neuve, après la dernière édition du manifeste ; vérificateurs de E2′ exclus du verdict réel.
- **Issue qui falsifie** : H_B → la table par critère se réduit à ce que le script seul décide ; le sous-agent R13 n'ajoute que de la variance ; H_A → la table est opérationnalisée.
- **Coût** : nul en calcul ; avant le 30 novembre.

### E3, E4 — inchangées

Non attaquées. E3 (≥ 0,99 de scores finis par cellule, seuil R-671 RAPPORTÉ) et E4 (puissance du minimum des huit gardes à 288 unités, K_h = 10, ≥ 0,86 RAPPORTÉ, 288 jamais simulé directement) restent telles quelles ; elles conditionnent le critère 6 et ne lisent aucun résultat de G1.

### E5 — retirée

Je retire la condition de progrès et l'expérience qui la fondait ; elle agirait comme un neuvième critère. Décision à inscrire au point 6.

### E6 — Antériorité (nouveau, de C-contrôle 1)

- **H_A** : tout fichier scellé du manifeste a un horodatage externe antérieur à la coupure ; un fichier planté postdaté est rejeté par le script et par R13.
- **H_B** : le fichier postdaté passe.
- **Contrôle sain** : fichier légitime horodaté avant la coupure, accepté.
- **Issue** : H_B → aucune liste d'arrêt n'est opposable, la distinction provisoire/définitif tombe ; H_A → elle tient.

### E7 — Corpus du critère 8 (nouveau, de C-évasion 4 et C-contrôle 3)

- **H_A** : un document contenant un chiffre sans page, placé sous `brouillons/` et **absent de toute liste manuelle**, est capturé par la règle de corpus et fait sortir « non tenu ».
- **H_B** : il échappe.
- **Contrôle sain** : corpus où chaque chiffre a chemin, PDF empreinté et page (R7) → « tenu ».
- **Issue** : H_B → le critère 8 est non décidable par cette règle ; H_A → décidable.

### E8 — Cécité du pilote ρ (nouveau, de C-contrôle 4)

- **H_A** : la sortie du pilote ne permet pas d'ordonner les comparateurs mieux qu'au hasard (test : un lecteur sans accès au code ordonne k comparateurs ; exactitude au niveau du hasard, IC 95 %).
- **H_B** : l'ordre est recouvrable.
- **Issue** : H_B → le pilote ρ est **interdit** pendant le report, et le critère 6 est scellé avec ρ mesuré après G0 (nœud de calendrier à soumettre avant le 30 novembre, pas après) ; H_A → autorisé.

---

## Points de l'arbitre, corrigés

### 1. Déclencheur (corrigé)

| Issue par critère | Définition mécanique |
|---|---|
| **Tenu** | Manifeste complet, empreintes conformes (R6), horodatage externe antérieur à la coupure (E6), contre-lecture présente (R2), préenregistrements citant v2 sans ajout de condition (E2′), verdict R13 « rempli ». |
| **Non tenu provisoire** | Manifeste absent ou incomplet (R11), **ou** verdict « non rempli » sans liste d'arrêt déclenchée, **ou** déclaration « non concluant » du sous-agent (mot cité). |
| **Non tenu définitif** | (a) liste d'arrêt d'un préenregistrement scellé déclenchée par un résultat scellé ; **ou** (b) pour 2, 3, 4 : aucun préenregistrement scellé avec liste d'arrêt au 30 novembre ; **ou** (c) manifeste de run (R9) sans résultat scellé. |

**Règle** : franchie ⇔ 8 tenus. Au moins un définitif ⇔ non franchie définitivement, sans report. Sinon ⇔ non franchie provisoire ⇔ report unique.

**« Non concluante »** n'est pas une issue de porte : elle n'existe qu'au niveau du critère et vaut provisoire. Même suite que « non franchie provisoire », parce que les deux ne diffèrent que par un mot du manifeste, et qu'aucune des deux ne peut éviter « définitif », qui ne repose que sur des fichiers scellés avant le run. Confiance 0,75.

**Qui prononce** : sous-agent neuf (R13), nommé au registre avec sa liste de fichiers (R2), exclu de E2′ ; il exécute les scripts (R4 intégré) ; le GO confirme ou consigne un désaccord, sans invalider.

### 2. Pendant le report (corrigé)

Table inchangée sauf : critère 2 — E1′ avec arrêt anticipé ; critères 3, 4 — dépense débloquée après scellement du dossier complet du critère 2 ; critère 6 — pilote ρ seulement après scellement des dossiers 3 et 4 et après E8 ; critère 8 — corpus par règle, `brouillons/` inclus.

**Dépense** : plafond = somme des devis scellés avant le 30 novembre, **strictement inférieure à 300 USD** (borne basse de la banque, RAPPORTÉ) ; défaut 250 USD (illustratif) ; coupe-circuit chez le fournisseur au montant du devis ; aucune imputation à un livrable financé tant que G0 n'est pas franchie (SUPPOSÉ). Confiance 0,65.

### 3. Second verdict (corrigé)

Inchangé, avec : arrêt anticipé possible (second verdict avancé, dans les 7 jours illustratifs du scellement d'un résultat déclenchant une liste d'arrêt) ; aucun audit postérieur au verdict ; le rapport ajoute (9) la liste de tout résultat lu pendant G0 v1 et (10) les empreintes complètes de v2 et de la clause, inscrites au registre avant le 30 novembre.

### 4. Clause scellable (corrigée, 149 mots)

> **Clause de repli G0, v2.** Si le verdict scellé du sous-agent neuf (R13) sur G0, rendu au plus tard le 30 novembre 2026, n'est pas « franchie », alors : (a) si un critère est « non tenu définitif » — liste d'arrêt scellée déclenchée, ou critère 2, 3 ou 4 sans préenregistrement scellé à liste d'arrêt, ou manifeste de run sans résultat scellé —, la porte est non franchie définitivement, sans report ; (b) sinon, elle est reportée une seule fois au 31 janvier 2027, 23:59 UTC, sur les huit critères du brief v2 (empreinte complète au registre), sans ajout de condition dans aucun préenregistrement ; pendant le report, seules les tâches de la table de dépendance scellée continuent, sous le plafond des devis scellés, inférieur à 300 USD, sans expérience décisive de G1 ni du papier C ; (c) tout déclenchement d'une liste d'arrêt pendant le report avance le second verdict ; (d) au second verdict, toute issue autre que « franchie » vaut non franchie définitivement ; aucun troisième verdict.

### 5. Financeur (inchangée, 39 mots)

> "If gate G0 is not passed by 30 November 2026 on its eight frozen criteria, there is one bounded extension to 31 January 2027; a second failure closes this program version. No criterion changes, and no outcome is promised."

### 6. À décider maintenant (liste fermée, corrigée)

1. Empreinte **complète** de v2 et de la clause, au registre.
2. Préenregistrements de 2, 3, 4 avec **listes d'arrêt**, scellés, contre-lus, citant v2 sans ajout.
3. Règle de corpus du critère 8 (globs, commit figé, `brouillons/` inclus).
4. Mécanisme d'horodatage externe (dépôt privé R-624/R-625 ou service ; SUPPOSÉ).
5. E2′, E6, E7 exécutés avant le 30 novembre ; si E2′ échoue, la table se réduit au script.
6. Prolongation de GO-2026-10-04-08 et devis du report (plafond < 300 USD, coupe-circuit fournisseur).
7. Table de dépendance scellée, avec conditions mécaniques de déblocage (3, 4 après dossier 2 ; ρ après dossiers 3, 4 et E8).
8. Désignation des sous-agents R13 (30 novembre, 31 janvier, verdict avancé), exclus de E2′.
9. Règle d'imputation et traitement du palier GC fin M2 (SUPPOSÉ).
10. Décision explicite de **ne pas** inscrire de condition de progrès.

---

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi (RAPPORTÉ, pièces).** Huit critères gelés ; deux tenus (1, 5) au 29 octobre, selon un brouillon et non un verdict R13 ; le critère 2 n'a pas avancé et porte une clause d'arrêt (R-680) ; les critères 3 et 4 dépendent de 2 ; le critère 6 exige une mesure (dispersion ρ) et un dimensionnement (288 unités, n80) dont la simulation directe à 288 n'existe pas ; le calcul de phase 0 échoit le 1er novembre ; 90 USD accordés contre 300–1 400 USD estimés pour une banque qui relève de G1, pas de G0 ; R1–R14 encadrent scellement, contre-lecture et verdict ; le report, s'il a lieu, est unique et borné au 31 janvier 2027 (question).

**Ce qui est établi par ce tour (OBSERVÉ-NON-AUDITÉ sur les textes).** Trois failles de ma conception III.1 étaient réelles et sont corrigées : (1) une règle de repli dont la branche « sans report » dépend d'un résultat qui peut ne jamais être scellé récompense l'inaction — correction : l'absence de liste d'arrêt scellée et le run sans résultat scellé valent définitif ; (2) E1 testait une disjonction là où le critère exige une conjonction ; (3) hacher le fichier des critères ne teste que R12 — le verrou est l'absence d'ajout de condition dans les préenregistrements, vérifiée sur paquets synthétiques tenus à l'écart. J'ai aussi retiré de G0 tout ce qui en durcissait un critère (discrétion) et l'ai déplacé vers le préenregistrement de G1, qui n'est pas gelé.

**Ce qui n'est pas établi (HYPOTHÈSE).** Que le critère 2 soit atteignable : rien dans les pièces ne le dit, et R-680 prévoit explicitement le contraire. Qu'un sous-agent R13 ajoute quelque chose à un script : E2′ le teste et peut conclure que non. Que l'horodatage externe soit disponible dans l'infrastructure du programme : SUPPOSÉ. Que le plafond de 250 USD couvre un pilote dose-réponse sur (ii) : illustratif, à chiffrer par devis. Que la garde contre l'abstention stratégique soit complète : elle repose sur le fait que seul le harnais validé écrit des manifestes de run, ce qui n'est pas prouvé par les pièces. Que le report ait une chance de servir : inconnu tant que E1′ n'a pas tourné.

**Ce qui n'entre pas dans une clause.** Une condition de progrès (neuvième critère déguisé), un audit postérieur au verdict, un pouvoir d'invalidation du GO, une règle sur les programmes successeurs.

**L'expérience à faire en premier : E1′**, préenregistrée et contre-lue avant le 30 novembre, exécutée avant le 30 novembre si le calcul de phase 0 est prolongé, sinon dès le premier jour du report. Raison : c'est la racine de 3, 4 et 6 ; ses deux issues falsifient quelque chose — plate sur (i) ou (ii), et la porte est non franchie définitivement sans dépenser deux mois ; monotone sur les deux, et le report a un objet mesurable. E2′, E6 et E7 coûtent zéro calcul et se font en parallèle ; mais sans E1′, la clause la mieux scellée ne décide que de la manière d'échouer.

**Confiance** : structure corrigée (définitif élargi, conjonction, verrou par préenregistrement) 0,75 ; plafond 0,65 ; viabilité du report : non estimable avant E1′.

FIN-DE-CELLULE