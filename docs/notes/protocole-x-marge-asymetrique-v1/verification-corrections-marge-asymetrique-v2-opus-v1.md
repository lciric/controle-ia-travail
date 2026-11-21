# Vérification des corrections : note sur la marge asymétrique, v2

- **Date** : samedi 21 novembre 2026, de 16:16 à 16:25 UTC (`date -u`). Dépôt à `42fb799fe`.
- **Auteur** : Claude Opus 5.5, le contre-lecteur de la v1 (`contre-lecture-reponse-fable-marge-asymetrique-v1-opus-v1.md`, `738f05f1…d3e0`). C'est la vérification des corrections par le même contre-lecteur. Pièce de classe C. Ni commit, ni poussée, ni appel payant, ni recherche en ligne.
- **Pièces vérifiées**, toutes « OK » contre leur compagnon `.sha256` :

| Pièce | Empreinte |
|---|---|
| `reponse-fable-marge-asymetrique-v2.md` | `6c7e1c2fb83525d5a1199701aeecf11181681574aa9ace1a9a11931df925050d` |
| `calculs-marge-asymetrique-v2.py` | `349fa868714ebf544fba39968794f3a1c1b4426fddb61ec5a6ff4084a1ff9baf` |
| `calculs-marge-asymetrique-v2.txt` | `bfe52d437b4484ab57c2741cca98b6397cf1f4411b9446d251223aa0f07fe944` |
| `collisionneur-v2/faits-marge-asymetrique-v2.md` | compagnon « OK » |
| `collisionneur-v2/question-marge-asymetrique-v2.md` | compagnon « OK » |
| `question-organisme-marge-asymetrique-v2.md` | compagnon « OK » |

- **Rejeu** : le script v2, lancé une fois par `python3 -I` dans un dossier temporaire à moi, rend une sortie identique à l'octet au `.txt` (`cmp`).
- **Différence avec la v1** : les blocs A à D sont inchangés. E est retouché ; F, G1, G1 bis, G2 et H sont nouveaux.
- **Contrôles à la main** :
  - variance du maximum de k lectures indépendantes : 0,682 à k = 2 (soit 1 − 1/π), 0,492 à k = 4 ;
  - gain du maximum : 1 / (0,19 + 0,81 × 0,492) = 1,70 ;
  - seuil d'égalités : 1 − 0,79 / 0,968 = 0,184 ;
  - écart du monde où la réplique se distingue : 0,418 − 0,610 = −0,19 ;
  - les valeurs du bloc F à 10 % et 15 % d'égalités sont celles de mon calcul indépendant.

## Verdict

**Conforme.**

Les seize constats sont portés juste. Il reste deux remarques mineures (fin de la pièce), à corriger par erratum ou à laisser : aucune ne touche la décision de retrait.

### Le bloquant (constat 1) est levé

La décision de retrait (D-1) repose maintenant sur la raison que je proposais, presque mot pour mot (§ 4, « La raison, corrigée » ; D-1, « La raison ») :
- contre un saboteur qui répond au mieux, aucune des trois interventions ne garde de marge sur le succès ;
- une marge mesurée sur nos organismes lirait leur fabrication.

La v2 retire « prédite nulle sur nos organismes » partout, y compris au relevé de méthode (pas 10 et 11). Elle dit le retrait indépendant de l'inventaire. Elle nomme le nouveau premier pas non justifié : la lecture « fabrication » du pas 11. Elle baisse sa confiance de 0,7 à 0,6.

### La décision ouverte de la note sur l'attaquant informé (constat 2) est traitée comme un seul nœud

D-1 nomme la D-2 de la note sur l'attaquant informé (`c23a1034…`) et cite GO-2026-11-21-54. Elle range l'ancienne recommandation de garde en option (b). Elle garde ses quatre lectures rapportées dans la mesure.

Puisque Lazar a accordé le retrait (GO-2026-11-21-64), la mère doit consigner que ce mot **ferme aussi** cette D-2.

### Le couple neutre et la question de l'organisme sont neutres

La recherche de motifs ne trouve aucun nom, aucun chemin, aucun identifiant, aucun sigle du programme, ni le détail de l'adaptateur.

Les retraits demandés sont faits : la dichotomie, la liste d'artefacts, les trois monnaies. Le constat 14 est porté. Les faits ajoutés jouent contre la lecture de la note, et je les ai vérifiés à la page dite (46 %, 69 %, 17 % ; 80 % ; « strategy-aware paraphraser » ; « cannot be exploited »).

Restent la garde de motifs du collisionneur et la relecture de cloisonnement, qui reviennent à la mère.

### L'attente manquée est dite honnêtement

Deux faits sont rapportés :
- **L'attente manquée** (attente 10, bloc G1) : la v2 attendait que le gain baisse quand la corrélation honnête monte. Il monte, de +0,172 à +0,221. La v2 le dit au § 3 et au relevé.
- **Le −0,045** (bloc G1 bis) : le bloc est ajouté après cette exécution, et cet ajout est déclaré. Son attente à lui, écrite avant, a tenu. La note le porte au verdict 4, au § 3, au témoin M11 et dans le monde R13.

La note dit aussi que le bloc G1 bis ne vaut que pour la famille G. Cela suffit pour borner la valeur quand l'attaquant choisit sa famille.

## Constats de la contre-lecture, un par un

| n° | Sort | Où |
|---|---|---|
| 1 | porté juste | Verdict 2 ; § 4 ; relevé, pas 10 et 11 ; D-1 ; D-4 |
| 2 | porté juste | En-tête ; § 4 ; D-1 (« un seul nœud ») |
| 3 | porté juste | § 3, deuxième borne ; D-1 (a) |
| 4 | porté juste | § 3, ligne « paraphrase de l'entrée » ; § 2, citation de Zhou et May ; § 5, deux champs fermés |
| 5 | porté juste | Verdict 5 ; retouche 2 rendue conditionnelle ; bloc F |
| 6 | porté juste | Bloc G2 ; prédiction 3 de la taxe de cohérence (H6′) ; § 6.3 ; formule marquée « moyenne seule » |
| 7 | porté juste | § 2 ; supposition nommée ; monde R12 et témoin M10 (bloc H) |
| 8 | porté juste | Couple v2 ; sous-question v2 |
| 9 à 16 | portés juste | Lieux dits par la table de la v2, vérifiés un à un |

Aucun constat porté mal, aucun manquant.

## Deux remarques mineures, nouvelles

1. **Verdict 4, première phrase.** « Une seule tient : l'information seule … +0,17 » reste écrite sans réserve. Les phrases qui suivent la défont pourtant quand l'attaquant choisit aussi la ressemblance de ses scores ou distingue la réplique. Texte proposé : « … une seule tient tant que l'attaquant ne choisit ni la ressemblance de ses scores ni ne distingue la réplique ».
2. **§ 3, table, dernière colonne de la ligne « lecture de tous les tirages ».** « De −0,045 à −0,19 » réunit deux suppositions distinctes : une ressemblance des scores d'attaque de 0,90 (bloc G1 bis), et la réplique distinguée, en famille G (bloc H). Le bloc G1 bis va jusqu'à −0,136 à 0,99. Texte proposé : « −0,045 à 0,90 de ressemblance (G1 bis) ; −0,19 si la réplique se distingue, famille G (H) ».
