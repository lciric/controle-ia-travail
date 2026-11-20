# Constat de l'additif 6 v2 (code de l'étage 2 à 200, ligne 3, organisme v9) — v1

Pièce de travail (classe C), écrite le 2026-11-20, sur la demande de la coordination, sous le mandat `mandat-contre-lecteur-additif-6-v1.md` (`e42e2c42…`) et ses interdits. Contre-lecteur neuf, modèle O, celui qui a contre-lu la version 1 (`contre-lecture-additif-6-v1.md`, `86bf181f…`).

## Verdict

**Conforme, à sceller.** La version 2 est exactement la version 1, plus mon jeu, plus la tenue du rédacteur. La tenue ne touche que ce qu'elle déclare. Ses renvois au registre sont à la lettre. Ce que la mère doit inscrire, au plus tard dans la ligne du scellement : voir le point 4. Rien n'en bloque le scellement.

## 1. Pièces, empreintes recalculées

| pièce (sous `E/additif-6-v2/`, sauf mention) | sha256 |
|---|---|
| `additif-6-code-etage-2-preenregistrement-ligne-3-v2.md` | `014b8e790dc4538edabf83e1e66c2294393bbbd1ab1e8de1ddcc3e2b2f38bc54` |
| `passe-1-jeu-du-contre-lecteur-additif-6.md` | `9751d78aa6f6993029d79627463727667690a2614af8982aa0ec87b40eee15a0` |
| `jeu-tenue-redacteur-additif-6-v2.json` (31 remplacements) | `008e7eed07f4edb4315bd7f2948684bb0aa92a8a73e8694e7332ff4bb41f5749` |
| `differentiel-additif-6-v1-v2.diff` | `f08fcc260c00bb925f711a95ed5a5adda18d14481d449660b11d7ced7a5139b0` |
| `differentiel-additif-6-passe-1-v2.diff` | `c1ad9577d4db3b09782c9d93a8c7798368699bd402192e449ae665e06b5c23d2` |
| `rapport-redacteur-additif-code-etage-2-v2.md` | `1da0380e01f419f7f85ef058b746630a222c5bfbd7d74f30c1f6bc5c4bd4b4e5` |
| `E/additif-6-v1/contre-lecture-v1/jeu-corrections-additif-6-v1.json` (mon jeu, versé) | `11d3dedc…`, égal au mien |
| `E/additif-6-v1/contre-lecture-v1/contre-lecture-additif-6-v1.md` (ma pièce, versée) | `86bf181f…`, égale à la mienne |
| `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |

Le nom du rapport n'était pas dans la demande. Je l'ai trouvé au second chemin supposé, d'après le nom du rapport v1, sans aucune liste. Les deux différentiels sont relevés par leur empreinte ; je n'en ai pas relu le contenu, puisque le rejeu les rend inutiles pour ce constat.

## 2. Les deux passes, rejouées

1. **Première passe.** `cmp` de `passe-1-jeu-du-contre-lecteur-additif-6.md` contre mon essai `essai-application-jeu-additif-6-v2.md` : aucune différence (même empreinte, `9751d78a…`).
2. **Tenue.** J'ai lancé `scripts/remplacer_texte_exact_v1.py`, avec la première passe pour cible et le jeu de tenue. La sortie est dans mon dossier : `rejeu-tenue-additif-6-v2.md`. Résultat : « FAIT : 31 remplacement(s) », sortie **`014b8e79…`, égale à la v2 versée**.

## 3. Ce que touche la tenue, et ses renvois au registre

J'ai lu les 31 entrées du jeu de tenue (le fichier JSON compte 31 objets).

- **Elles touchent :**
  - la date (entrée 1) ;
  - la phrase de version (2) ;
  - les lignes de table : registres lus (3), contre-lecture et jeu (4), pièces lues (31) ;
  - la réserve 6 récrite (29) et la réserve 9 ajoutée (30) ;
  - des renvois au registre : les 24 entrées de 5 à 28.
- Quelques renvois changent un état de silence, sans rien changer d'autre :
  - n° 46 passe de « à la mère » à « décidé (R-4327) » ;
  - le dossier `Q` passe de « à confirmer » à « accepté (R-4327) ».
- Elles ne touchent aucune commande, aucun chemin d'exécution, aucun chiffre ni aucun texte de règle. Le titre et le statut viennent de mon jeu (C1, C2).

**Lettre des renvois**, relue à `origin/main`. La tête est `0f7146f8b…` après `git fetch`. La copie du registre à `bed0187f…` (`origin/main~1`, tête lue par le rédacteur) vaut `da56d763…`, comme il l'écrit. `registres/go.md` est inchangé (`61d52dc1…`). Lignes extraites : `sortie-decisions-4325-4328.txt`.

| renvoi | lettre du registre |
|---|---|
| « tout refusé », 14:01Z → R-4325 | « tout refusé (14:01Z), le code est gardé et l'additif dit la propriété du compteur » : égal |
| réserves A et B → R-4316, R-4325 ; R-4325 « nomme le refus par l'historique et la portée par pièce » | « refus si l'historique connaît le manifeste » ; « portée par pièce en v3 » : égal |
| silence n° 17 → R-4325 | « rho_paire pour ρ′ − ρ et rho_moyenne rapporté sur le bloc A » : égal |
| `NO_PROXY` → R-4325 | « contrôle de NO_PROXY ⊇ 127.0.0.1 au lancement » : égal |
| silence n° 18 → R-4324, R-4325 | égal |
| rejeu des essais, quatre fragments, part d'Argon, t01 et t07, relais, réserve sur ρ → R-4326 | les six sont nommés dans R-4326 : égal |
| banque comparée à `HEX_BANQUE`, audit limité, `Q`, `GEMINI_API_KEY`, `/usr/bin/python3` → R-4327 | les cinq sont nommés dans R-4327 : égal |
| racine 2026111935 → « R-4326 et R-4327 : déclaration seule, aucune racine neuve » | voir le point 5, nuance |

R-4328 (16:50Z) inscrit un manquement de versement : des copies de registres ont été versées, puis retirées. Il ne touche pas le texte de l'additif.

## 4. Points du rédacteur : ce que R-4325 à R-4327 ne nomment pas

**Jugement : acceptable au scellement.** Aucun de ces points n'a besoin d'une ligne avant le scellement : aucun n'est une règle neuve que seule la coordination porterait.

| point | jugement |
|---|---|
| Échéance, n° 50 | C'est la lettre même de GO-2026-11-20-68 (colonne « échéance », 2026-11-27) et de la garde du code. « Confirmé » n'ajoute rien. |
| Partage tiré avant la garde, n° 48 | C'est un fait du générateur v3 vérifié « Conforme » (R-4324 : « tout le code de l'étage 2 est vérifié »). « Écrit tel quel » ne change rien. |
| `MODELES_CLAUDE` | C'est un renvoi à une pièce épinglée. Il entre dans « commande des relais reprise de la course v9 » (R-4326). |
| Trois des décisions de 15:20Z : forme réelle seule, journal existant sans manifeste, lecture unique de la pièce du (4) | Elles sont portées par le code du générateur v3, contrôlées et vérifiées « Conforme ». L'additif ne fait que les décrire. |
| Restes de procédure, n° 34 | Ce sont des règles pour l'exécutant, qui ne lient que par l'additif. Le scellement les rend opposables. |

**Recommandation.** La ligne de scellement de la mère nomme d'une phrase ces cinq points, « portés par l'additif 6 v2, connus par la coordination », et accepte, tels qu'écrits, les points encore « à la mère » de la v2 :
- les n° 5, 9 (pièce de départ réduite), 10, 12, 22, 33, 40, 41, 51 ;
- `S` hors du dépôt (§ 5, « à confirmer par la mère » ; R-4327 accepte `Q`, non `S`) ;
- le n° 43 (suite du verdict), renvoyé au verdict.

Sans cette phrase, un verdict ultérieur pourrait se demander si ces états ont été tranchés. Avant le départ, il reste aussi les deux blancs : `HEX` et le commit de `main`.

## 5. La nuance sur la racine 2026111935

R-4326 pose une règle conditionnelle : « racine neuve et question à Lazar si l'aveugle est touché ». R-4327 tranche la condition : « sans effet sur l'aveugle, déclaration seule ». Les citer ensemble pour « déclaration seule, aucune racine neuve » est exact, puisque c'est la conjonction des deux qui le dit. Je n'en fais pas une correction. Précision facultative, sans effet : écrire « R-4326 (règle), R-4327 (aveugle non touché) ».

Point 5 du rapport du rédacteur : le pire du juge Argon, 30,44 USD, au-delà des 15,41 USD que nomme GO-64. Je suis d'accord pour le dire à Lazar au compte rendu ; R-4326 l'inscrit déjà.

## 6. Écarts

1. `git fetch origin main`, qui a avancé `origin/main` à `0f7146f8b…`. Trois `git show` redirigés vers mon dossier :
   - `origin/main:registres/decisions.md` ;
   - `origin/main:registres/go.md` ;
   - `origin/main~1:registres/decisions.md`, pour la tête lue par le rédacteur (écart de forme, déclaré).
2. Deux noms de rapport essayés par `sha256sum` sur des chemins supposés ; le premier était absent.
3. `scripts/remplacer_texte_exact_v1.py` lancé une fois, sortie dans mon dossier.
4. Aucun programme de l'étage 2 lancé ; rien sous `archives-reponses-modeles/` ; aucun appel, aucune clé, aucune dépense ; aucune écriture dans le dépôt ni dans le clone ; aucune publication. **Aucun refus de permission, de classifieur ni de garde.**

Contre-lecteur neuf, modèle O.
