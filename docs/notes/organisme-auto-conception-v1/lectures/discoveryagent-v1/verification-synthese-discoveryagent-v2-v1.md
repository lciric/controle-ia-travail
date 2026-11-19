# Vérification de la synthèse DiscoveryAgent, version 2 — v1

- **Pièce de travail** (classe C), écrite le 19 novembre 2026 par le contre-lecteur de la version 1, Claude Opus 5.5 (invite système : « You are powered by the model named Opus 5.5. The exact model ID is claude-opus-5-5. »). C'est la vérification des corrections par le même contre-lecteur. Aucune dépense, aucun commit.
- **Objet** (sceaux vérifiés) : `synthese-discoveryagent-pour-l-organisme-v2.md` (`de8e2b81…`) ; dans `outils-synthese-v1/` : `citations-synthese-v2.json` (`05167f5a…`), `verifier_citations_synthese_v2.py` (`e22ca074…`), `sortie-verification-citations-synthese-v2.txt` (`a93fcba3…`), `appliquer-couples-v2.py` (`1c04a073…`) et son journal `sortie-appliquer-couples-v2.txt` (`2352e6b1…`).
- **Outil** : `outils-contre-lecture-synthese-v1/verifier_version2_v1.py` (lecture seule, `python3 -I`) et sa sortie `sortie-verifier-version2-v1.txt`.

## Verdict : tient après ces couples (de forme seulement ; le fond de la version 2 tient tel quel)

**Ce qui est vérifié**
1. **Recopie.** Mes 54 couples, appliqués à la v1, redonnent le texte d'empreinte `edc43176…`. C'est celle de ma sortie scellée et du journal de l'application.
2. **Retouches à la main.** Hors de la table, la v2 ne diffère de ce texte que par la puce « Version 2 » de l'en-tête, qui est exacte.
3. **Registre.** Le registre v2 est le registre v1 plus mes 60 citations « a_verser », à l'identique, sources comprises.
4. **Programme.** Le programme v2 ne change que deux noms de fichiers. Relancé par moi : 235 sur 235, 0 échec, aucun identifiant inconnu ni non cité.
5. **Table.** La table de la v2 est, ligne pour ligne, la sortie `--table` du programme v2.

**Les trois points laissés à mon jugement, tranchés**
- **Introduction de l'annexe.** Elle nomme le programme et le registre v1, et dit X04 et X05 retouchées à la main, ce qui est faux pour une table brute. Couple F5.
- **Table.** Les barres verticales des motifs cassent X04, X05 et X09 à l'affichage. Je les rends par des barres obliques, comme la note le fait déjà pour les extraits, et l'introduction le dit (F5 à F8). Il n'y a pas de programme neuf à écrire.
- **Titre et puce « Renvois ».** Couples F1 et F4. F3 trace la version 3 ; F2 et F9 sont facultatifs.

**Pourquoi le programme v2 suffit pour la v3.** Il lit la note v2 pour le contrôle des identifiants, mais ces couples n'en changent aucun (contrôlé par l'outil) : son bilan vaut pour la v3.

## Couples de forme, à appliquer en v3, à la lettre et dans l'ordre

Chaque texte vaut tel quel dans le fichier brut, du premier caractère après « > AVANT : » ou « > APRÈS : » jusqu'à la fin de la ligne.

#### Couple F1
> AVANT : # DiscoveryAgent : ce que l'organisme d'idéation peut en tirer — synthèse v1
> APRÈS : # DiscoveryAgent : ce que l'organisme d'idéation peut en tirer — synthèse v3

#### Couple F2 (facultatif)
> AVANT : À contre-lire par un lecteur d'un autre modèle.
> APRÈS : Contre-lue par un lecteur d'un autre modèle, Claude Opus 5.5 (`contre-lecture-synthese-discoveryagent-v1.md`) ; corrections appliquées aux versions 2 et 3, ci-dessous.

#### Couple F3
> AVANT : v1 : `synthese-discoveryagent-pour-l-organisme-v1.md`, sha256 `06d55b7c2d785d26290557b0c398624ff37e7c2d436dfdf159e0f79c2ee15715`.
> APRÈS : v1 : `synthese-discoveryagent-pour-l-organisme-v1.md`, sha256 `06d55b7c2d785d26290557b0c398624ff37e7c2d436dfdf159e0f79c2ee15715`. **Version 3** : couples de forme de la vérification `verification-synthese-discoveryagent-v2-v1.md` appliqués à la lettre et dans l'ordre (titre, en-tête, renvois au programme et au registre v2, introduction de l'annexe ; dans la colonne « lieu » de X04, X05 et X09, barres verticales des motifs rendues par des barres obliques, seule retouche de la table produite par le programme) ; v2 : `synthese-discoveryagent-pour-l-organisme-v2.md`, sha256 `de8e2b81d11a657adc033f1981c1fc448818ac69084c603b3fe8c5da0b455764`.

#### Couple F4
> AVANT : le programme `outils-synthese-v1/verifier_citations_synthese_v1.py` les retrouve tous dans leur source.
> APRÈS : le programme `outils-synthese-v1/verifier_citations_synthese_v2.py` les retrouve tous dans leur source, à partir du registre `outils-synthese-v1/citations-synthese-v2.json`.

#### Couple F5
> AVANT : Produite par `outils-synthese-v1/verifier_citations_synthese_v1.py --table` à partir du registre `outils-synthese-v1/citations-synthese-v1.json`, puis collée ici ; dans la colonne « lieu » de X04 et X05, les barres verticales des motifs sont rendues à la main par des barres obliques, que le programme ne produit pas.
> APRÈS : Produite par `outils-synthese-v1/verifier_citations_synthese_v2.py --table` à partir du registre `outils-synthese-v1/citations-synthese-v2.json`, puis collée ici ; dans la colonne « lieu » de X04, X05 et X09, les barres verticales des motifs sont rendues à la main par des barres obliques, que le programme ne produit pas : c'est la seule retouche de la table.

#### Couple F6
> AVANT : motif `corrupted.claim|misrepresented|inserted.error` sous .
> APRÈS : motif `corrupted.claim/misrepresented/inserted.error` sous .

#### Couple F7
> AVANT : motif `corrupted.claim|misrepresented|inserted.error|participant` sous .
> APRÈS : motif `corrupted.claim/misrepresented/inserted.error/participant` sous .

#### Couple F8
> AVANT : motif `explicit_hypothesis_step|no-hold-reviews` sous scripts/plan.py, configs
> APRÈS : motif `explicit_hypothesis_step/no-hold-reviews` sous scripts/plan.py, configs

#### Couple F9 (facultatif)
> AVANT : - **Les PDF font foi** ; mes citations sont vérifiées sur les textes extraits, pas sur le rendu des pages ni sur les figures.
> APRÈS : - **Les PDF font foi** ; mes citations sont vérifiées sur les textes extraits, pas sur le rendu des pages ni sur les figures ; la contre-lecture a retrouvé sur les PDF les 95 extraits du papier et de l'annexe de la version 1.

## Contrôle par programme

Voir `outils-contre-lecture-synthese-v1/sortie-verifier-version2-v1.txt`. Les neuf couples :
- sont uniques dans la v2 ;
- s'appliquent dans l'ordre ;
- laissent une table entière : aucune ligne cassée, et seules X04, X05 et X09 diffèrent de la sortie `--table`, par la barre rendue ;
- ne laissent aucun renvoi aux outils v1 ;
- laissent inchangés les identifiants cités.

**Empreinte attendue du texte v3**, avec les neuf couples (facultatifs compris), pour le contrôle croisé de celui qui les appliquera : `f36f94dc90060ea0e4607be15322638cbddbdfc57d0a2ffda5e74117f833a6e6`.

**Lecture de la sortie.** Au § 1, les deux lignes vides marquées « - » et « + » sont un effet d'alignement du diff ligne à ligne. Une comparaison par blocs ne montre, hors de la table, que la puce « Version 2 » insérée à la ligne 4.
