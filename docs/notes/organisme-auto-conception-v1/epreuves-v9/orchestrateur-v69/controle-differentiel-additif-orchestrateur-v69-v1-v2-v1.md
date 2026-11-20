# Contrôle du différentiel v1 → v2 — additif des interrupteurs de l'orchestrateur v69 et cadre de la v70 — v1

- Contre-lecteur, modèle O : l'auteur des contre-lectures v1 et v2 de l'additif. Je n'ai écrit ni les pièces v1, ni les pièces v2, ni leurs JSON. Écrit le 2026-11-20, relevé de `date -u` : 05:02:20Z, après les vérifications.
- Demande : message de la session coordinatrice (contrôle du différentiel, sept points). Mandat du rédacteur de la v2 : `V69/mandat-redacteur-additif-orchestrateur-v69-v2-v1.md` (`34a63552217626c8a3ec187dfbc6cf270352723cdcaa28a076c2ae60bc66d70d`). V69 = `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v69/`.
- Processeur seul ; aucune écriture dans le dépôt, aucun commit, aucun lancement de l'orchestrateur, du lanceur ni de l'organisme, aucune dépense. Le seul programme lancé est l'outil de remplacement, lu en entier avant, sortie dans mon dossier. **Aucun refus de permission, de classifieur ni de garde.**

## Verdict

**Conforme après corrections** : cinq corrections, au § 3, texte ancien et nouveau, chaque ancre comptée une fois sur la v2 (`grep -c -F -e`).
- Le rejeu de l'outil rend les deux pièces v2 à l'octet.
- Les douze corrections sont portées, la correction 1 selon ma v2.
- Le § 1.2 rend (a′) fidèlement, à un point près : l'expérimentateur y est dit « session externe », alors que la voie du tour fermé reprise telle quelle le passe comme rôle ordinaire (correction 3).
- Les deux incohérences déclarées sont de la tenue (correction 2).
- La correction 5 n'est pas couverte par D2 (a). Ce n'est pas un nœud, mais une proposition avec recommandation (correction 4).
- Le mot de Lazar est maintenant inscrit (`GO-2026-11-20-10`, point O3), ce que les pièces doivent dire (correction 1).
- Aucun allumage n'est accordé. Aucun identifiant de modèle.

## 1. Vérifications

### 1.1 Empreintes (recalculées ; compagnons vérifiés par `sha256sum -c` depuis V69)

| pièce | sha256 | égale à |
|---|---|---|
| `additif-interrupteurs-orchestrateur-v69-v1.md` | `aef8ff2f8eb3597c8405c765c3432ce791a34ab65b851a75ac223de875fbe158` | inchangée (R12) |
| `cadre-lecture-registre-orchestrateur-v70-v1.md` | `84651a4c658e88f0bca7d299746ae05c267ae7f9f2002d8371dd19fccef4a5ee` | inchangée (R12) |
| `additif-interrupteurs-orchestrateur-v69-v2.md` | `9d94d23fadfc961e1e3c71a743358d4d5a16a924267499b3a3f1028fee34e85f` | message et rapport |
| `cadre-lecture-registre-orchestrateur-v70-v2.md` | `216d9bcbc0276c79c5a86bcf835cd3d9d260d6e31e49c7f1250349530643fbeb` | message et rapport |
| `remplacements-additif-v1-vers-v2-v1.json` ; `remplacements-cadre-v1-vers-v2-v1.json` | `4a9e668f…0e70ba` ; `225c64a4…f88882` | rapport, § 2 |
| les deux journaux de remplacements | `d0e2bea2…a72e` ; `458c9c20…9faa` | rapport, § 2 |
| les deux différentiels | `93ed10d2…df0a` ; `dd7dac8d…7417` | rapport, § 2 |
| `rapport-redacteur-additif-orchestrateur-v69-v2-v1.md` | `d83d71d12255e9474a52f3b235c31d3b8c03f0c2dc82789b1a2643e71f43cf36` | message |
| `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` | rapport, § 1 |

### 1.2 Point 1 — rejeu de l'outil : égal à l'octet

J'ai lu l'outil en entier (bibliothèque standard ; il écrit seulement des fichiers neufs, en mode exclusif, jamais sur place). Je l'ai rejoué sur chaque pièce v1 avec son JSON, sortie dans mon dossier :
- additif : « FAIT : 31 remplacement(s) », sortie `9d94d23f…`, et `cmp` avec la v2 de V69 ne rend aucune différence ;
- cadre : « FAIT : 6 remplacement(s) », sortie `216d9bcb…`, `cmp` sans différence.

Les deux différentiels lus couvrent exactement ces 31 et 6 zones.

### 1.3 Point 2 — les corrections sont portées

| correction | lieu dans la v2 | portée |
|---|---|---|
| 1 (texte de ma v2) | § 9, réserve 1 : à la lettre ; § 3.3 : en substance, comme ma v2 le demandait (§ 3.2) | oui |
| 2 | § 2, ligne C4 | à la lettre |
| 3 | § 2, ligne C2 ; § 2.1, condition 8 | à la lettre |
| 4 | § 6, garde 2, artefact | à la lettre |
| 5 | § 4.2, dernier alinéa ; § 4.5, quatrième point | à la lettre |
| 6 | § 4.3, ligne 1 et alinéa suivant | à la lettre |
| 7 | § 4.4, alinéa « Coût et effet », en paragraphe à part après la phrase d'ancrage | à la lettre ; la mise en paragraphe est de la tenue |
| 8 | § 4.1, second point | à la lettre |
| 9 | § 5.2, premier point | à la lettre |
| 10 | § 5.1 ; § 6, garde 4 | à la lettre |
| 11 | § 4.2, introduction | à la lettre |
| 12 | § 4.3, ligne 2 ; phrase ajoutée à l'alinéa | à la lettre |

Le rapport v1 n'est pas récrit (R12). Le report qu'y demandait la correction 1 est fait au rapport de la v2 (§ 3 et § 6) : c'est acceptable.

### 1.4 Point 3 — le § 1.2 rend (a′)

- **Il dit ce que (a′) lève** :
  - **(b2)** : `jouer_etage` construit lui-même ses réglages, sans les deux plafonds (l. 874-877). Le sommet neuf les porte, et `jouer_etage_v57` les transmet à l'étage v5 (v57 l. 69-77 ; v5 l. 249-254).
  - **(b5)** : chemin fixe de la tranche et du contre-calcul (l. 864-865, 887-888).
  - Aucun octet changé dans un fichier existant.
- **Il dit ce qui reste à établir** : (b3), le lanceur réel absent de la copie ; le sommet neuf, jamais joué en réel, avec l'essai de la garde 6 sur le chemin même ; les fonctions lues par parties ; la tranche de contrôle. Il écarte (a), explique pourquoi (b) n'y échappe pas, et précise que (c) n'est pas retenue.
- **Le relevé du rédacteur (point 3 de sa liste) est confirmé sur le code.** `contre_calculer(resume, lois, chemin_episodes, sha_attendue=None)` reçoit le chemin de son appelant (`tour_ferme_v64.py` l. 806, 809, 817). L'arrêt sur désaccord n'est pas dans cette fonction, qui ne rend que des indicateurs : il est dans `jouer_etage` (l. 893-896). Le § 1.2 le dit justement : « ce que le sommet neuf porte lui-même : … l'arrêt sur tout écart du contre-calcul ».
- **Une contrainte reste non dite.** `statistique_hors_bac`, que `contre_calculer` appelle, lit les colonnes `y`, `z0`, `z1`, `g` de la tranche (l. 791-801). La tranche d'épreuve de l'héritage doit donc garder ce format, ou la fonction ne se reprend pas telle quelle (rapport du palier 0a, § 3.3, manque 1). Correction 5.
- **Un point infidèle : l'expérimentateur « session externe ».** Reprise telle quelle, la voie du tour fermé passe l'expérimentateur à l'étage comme rôle ordinaire, routé par `AdaptateurEtageV64` (`tour_ferme_v64.py` l. 874 : `"experimentateur": roles["experimentateur"]`), non comme `experimentateur_externe`. L'étage v5 n'applique `plafond_externe_usd` qu'aux sessions externes (`tests_de_mort_v5.py` l. 345) ; sur cette voie, `plafond_total_usd` couvre les deux rôles. Exiger les deux plafonds, comme la garde 6, ferait éprouver une valeur sans effet (R5). Correction 3, qui touche aussi le § 5.2 et la garde 6 pour rester cohérente ; la règle conditionnelle est celle de `verifier_etage_v68` (`course2_v68.py` l. 276-280).

### 1.5 Point 4 — les trois modifications en plus

1. **§ 2, ligne C5** (« étage par le sommet neuf de la v69, qui appelle les maillons et les fonctions du tour fermé ») : conséquence directe de (a′), et cohérente avec le § 1.2. Elle tient.
2. **§ 4.3, introduction** (D2 dite retenue) : juste. D2 (a) retient les définitions du § 4.3 et la tranche de contrôle (rapport v1, § 5, D2) ; le mot est inscrit (correction 1). Elle tient.
3. **Cadre, § 3, point 3** : c'est la précision facultative de ma v1 (§ 3, point 6), rendue fidèlement, avec ligne et fichier. Elle tient. Le cadre, § 3, point 1, rend D3 (a) comme le rapport v1 la posait : les deux formes, et le point 7 du palier 0b qui choisit.

### 1.6 Point 5 — les deux incohérences : c'est de la tenue

Elles découlent de ma correction 6, qui ne les visait pas. Les réparer n'ajoute aucun fond : « confiné » n'est attribuable à aucune tentative, donc trois verdicts restent possibles, deux sans tranche de contrôle. Le § 4.3 de la v2 le dit déjà. Textes exacts : correction 2. Le rapport v1, § 0, point 3, qui liste encore quatre verdicts, n'est pas à récrire (R12) : l'additif fait foi.

### 1.7 Point 6 — la correction 5 n'est pas couverte par D2 (a) ; ce n'est pas un nœud

- **Pas couverte.** D2, telle que le rapport v1 la pose (§ 5), porte sur les définitions des quatre verdicts du § 4.3 et sur la tranche de contrôle du § 4.4. La classe d'une tentative refusée avant l'épreuve vient de ma correction 5, postérieure au rapport. Lazar a répondu à D2 telle qu'elle était posée (`GO-2026-11-20-10`, O3) : la phrase « posée avec D2 » n'est donc pas vraie à la lettre.
- **Pas un nœud.** Elle ne modifie ni hypothèse, ni revendication, ni critère du plan, et ne sert rien à un agent sous (1a). Elle comble un manque du plan : `resultat` doit être une classe ou le statut (plan v5, § 1, l. 48), et le plan ne nomme pas la classe d'une tentative refusée (§ 3.0). Elle le fait dans le sens le plus prudent : jamais mieux traitée que « ne tient pas », et gardée au dénominateur de la règle de passage du § 8.4, lu à la lettre (« la moitié au moins des tentatives »), ce qui rend le passage plus difficile, non plus facile.
- **Ce qu'elle est.** Un « proposer avec recommandation » (consignes permanentes, hiérarchie de décision), à porter à Lazar avec le devis du palier 1, et à geler au préenregistrement court de ce palier, qui fixe la règle de passage. Défaut sous 48 heures permis : il ne porte ni sur une dépense ni sur un allumage. Texte : correction 4.
- **Pour la v70.** Si un jour le registre est servi, cette classe le sera aussi. Ce service est un nœud, déjà à part, et rien ici ne l'accorde.

### 1.8 Point 7 — allumage, identifiants

- Aucun allumage n'est accordé : statut de l'additif ; § 1.2, dernier alinéa ; § 9, réserve 7 ; § 5.1 et § 8 inchangés ; cadre, § 3, point 1 (« l'allumage de la lecture reste un nœud »).
- Aucun identifiant de modèle dans l'additif v2, le cadre v2 ni le rapport de la v2. J'ai fait la recherche sur chacun ; la seule occurrence, « claude-0 », est un nom de dossier.
- **Inscription.** `registres/go.md` sur `origin/main` local, lu par `git show` redirigé, porte `GO-2026-11-20-10`, point (O3) : « Orchestrateur v69 : D1 (a′), D2 (a), D3 (a) ». La même lecture au commit `b9b0c97e` ne la porte pas encore. La ligne `GO-2026-11-20-11`, que nomme le message, n'est pas dans ma copie de `main` : non vue, et rien ici n'en dépend.

## 2. Ce que je n'ai pas vérifié

- Je n'ai pas régénéré les différentiels pour les comparer à l'octet : leurs en-têtes portent chemins et horloges. J'ai lu celui de l'additif en entier et celui du cadre en entier.
- Je n'ai pas relu de code au-delà des lignes citées ci-dessus, toutes dans la copie au commit 94bfd92 déjà vérifiée par ma v2.

## 3. Corrections (texte ancien → texte nouveau), sur les pièces v2, à faire par l'outil

Chaque texte ancien figure une fois exactement dans sa cible (`grep -c -F -e` : 1).

**1. Inscription du mot (tenue).**
- Additif v2, ligne « Statut ». Ancien : « **sous réserve de l'inscription de cette lecture par la mère** ; si elle est corrigée, la v2 change. » Nouveau : « **sous réserve de l'inscription de cette lecture par la mère** ; elle est inscrite : `GO-2026-11-20-10`, point (O3) (`registres/go.md`, sur `main`), ce qui lève dans tout ce texte la réserve d'inscription ; si la ligne est corrigée, la v2 change. »
- Cadre v2, § 3, point 1. Ancien : « sous réserve de l'inscription de cette lecture par la mère : la réserve de » Nouveau : « lecture inscrite en `GO-2026-11-20-10`, point (O3) : la réserve de »

**2. Les deux incohérences nées de la correction 6 (tenue).**
- Additif v2, § 0, point 4. Ancien : « un verdict précis parmi quatre (R-3209, point 3). » Nouveau : « un verdict précis parmi les trois attribuables à ce palier, des quatre mots de R-3209, point 3 (« confiné » n'est attribuable à aucune tentative sous la forme imposée, § 4.3). »
- Additif v2, § 4.4, second alinéa. Ancien : « et les verdicts possibles sont les trois autres. » Nouveau : « et les verdicts possibles sont « identique » et « portable » (« confiné » n'étant attribuable à aucune tentative, § 4.3). »

**3. L'expérimentateur, session externe ou rôle ordinaire (fidélité à (a′) ; R5).**
- Additif v2, § 1.2, « Ce que le sommet neuf porte lui-même ». Ancien : « avec `plafond_total_usd`, `plafond_externe_usd` pour l'expérimentateur, session externe, et les bornes par fiche du devis ; » Nouveau : « avec `plafond_total_usd`, et `plafond_externe_usd` si l'expérimentateur est passé à l'étage en session externe (`experimentateur_externe`), et les bornes par fiche du devis. Reprise telle quelle, la voie du tour fermé passe l'expérimentateur comme rôle ordinaire, routé par `AdaptateurEtageV64` (`tour_ferme_v64.py` l. 874) ; `plafond_total_usd` couvre alors les deux rôles, et l'étage n'applique `plafond_externe_usd` qu'aux sessions externes (`tests_de_mort_v5.py` l. 345) ; le développeur dit laquelle des deux voies il prend ; »
- Additif v2, § 5.2. Ancien : « l'expérimentateur, session externe, exige `plafond_externe_usd`, la somme restant sous le plafond de l'étage » Nouveau : « si l'expérimentateur est passé à l'étage en session externe, il exige `plafond_externe_usd`, la somme restant sous le plafond de l'étage (règle de `verifier_etage_v68`, `course2_v68.py` l. 276-280 ; sur la voie du tour fermé, rôle ordinaire, `plafond_total_usd` couvre les deux rôles, § 1.2) »
- Additif v2, § 6, garde 6, cas sain. Ancien : « | `plafond_total_usd` et `plafond_externe_usd` présents, sous le plafond de l'étage | » Nouveau : « | `plafond_total_usd` présent, et `plafond_externe_usd` si l'expérimentateur est en session externe, sous le plafond de l'étage | »

**4. Correction 5 : ce n'est pas D2.**
- Additif v2, § 4.2, dernier alinéa. Ancien : « Le plan ne nomme pas sa classe : cette lecture est du rédacteur, posée avec D2. » Nouveau : « Le plan ne nomme pas sa classe : cette lecture vient de la contre-lecture v1 (correction 5) et n'est pas couverte par D2 (a). Elle ne change aucun critère du plan : elle lit « des tentatives » du § 8.4 à la lettre et ne traite jamais un refus mieux que « ne tient pas ». Elle est portée à Lazar en « proposer avec recommandation », avec le devis du palier 1 (recommandation : la tenir ; défaut sous 48 heures : la tenir, aucune dépense ni aucun allumage n'en dépendant), et gelée au préenregistrement court du palier 1. »

**5. Le format de la tranche que lit le contre-calcul (reste à établir).**
- Additif v2, § 1.2, « Ce qui reste à établir », point 3. Ancien : « et que `contre_calculer` reçoit de son appelant le chemin de la tranche qu'il lit (ce point est un relevé du rédacteur de la v2, non de la contre-lecture). » Nouveau : « Que `contre_calculer` reçoive de son appelant le chemin de la tranche qu'il lit est confirmé sur le code (`tour_ferme_v64.py` l. 806, 809, 817 ; contrôle du différentiel v1 → v2). Reste à établir : la statistique hors bac, qu'il appelle, lit les colonnes `y`, `z0`, `z1`, `g` (l. 791-801) ; la tranche d'épreuve et la tranche de contrôle de l'héritage gardent ce format, sinon la fonction ne se reprend pas telle quelle (rapport du palier 0a, § 3.3, manque 1) et le développeur s'arrête. »

Aucune autre. Le rapport de la v2 n'est pas à corriger : ses écarts du § 5 sont tranchés ici.

— contre-lecteur, modèle O
