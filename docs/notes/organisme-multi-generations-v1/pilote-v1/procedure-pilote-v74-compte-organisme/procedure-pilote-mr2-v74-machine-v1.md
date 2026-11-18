# Procédure du pilote MR-2 sur la machine jetable — code v74, texte scellé candidat 6 — v1

- **Auteur** : modèle A (session du compte organisme), à 2026-11-14T23:12:02Z (`date -u`). **Ce compte ne lance rien** : son brief interdit tout appel
  au loueur, et le crochet de garde n'est pas chargé dans sa session (PO-001). Cette procédure est pour la session qui louera la machine
  (nœud posé à la mère, option (a) recommandée).
- **Fait foi** : le texte scellé (`preenregistrement-pilote-conditionnelles-v1-candidat6-compte-organisme.md`,
  `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e`, R-2809), sections « Ordre », « Mondes et secret », « Préalables »,
  « Liste d'arrêt ». Cette procédure ne change rien au texte ; en cas d'écart, le texte prime et l'écart est un nœud.
- **Lignes** : GO-2026-11-14-13 (π1, 20 USD, crédits de Claude) et GO-2026-11-14-14 (π2, 21.72 USD hors crédits, dont machine 3 USD),
  `main` `20f66b0b`, l. 332-333 (R-2810). À relire au distant avant tout appel.

## Répétition locale faite par ce compte (aucun appel, aucune clé, aucune dépense)

Sur un **secret public de développement** (32 octets nuls) et une phrase de répétition (jamais celle de Lazar), sous `env -i` sans clé,
dans ce conteneur (4 processeurs), arbre de l'organisme à `605e0f6` (paquet v74) :

| étape | durée | code | sortie (versée sous `repetition-locale/`) |
|---|---|---|---|
| `generer` (4 mondes, contrôles C0 à C8) | **12 min** (22:58:50Z → 23:10:59Z) | 0 | `generer.txt` : 4 mondes conformes, 7 tirages refusés puis remplacés |
| `preparer` (C-16, C-17) | 1 s | 0 | `preparer.txt` |
| `jouer --mode a_blanc` (proposeurs factices du lanceur) | 3 s | 0 | `jouer.txt` : 16 appels complets, 0 échec, 0 tronqué |
| `mesurer` | 2 s | 0 | `mesurer.txt` |
| `lire` | < 1 s | 0 | `lire.txt` |
| `rapatrier` | 1 s | 0 | `rapatriement.txt`, `rapatrie/` : « aucun_monde » vrai |

**L'issue affichée par `lire` sur cette répétition n'est pas un résultat** : proposeurs factices, mondes d'un secret public. Elle n'est
ni lue ni rapportée comme telle (R1). Les mondes de la répétition et le secret public restent hors dépôt ; seules les empreintes
d'engagement sont versées (`engagement-mondes-repetition.json`).

## Procédure (ordre du texte scellé)

0. **Session qui lance** : ouverte dans le dépôt de travail (le crochet `garde_calcul.py` doit être chargé ; l'éprouver sur un cas
   sain et un artefact, R5) ; GO valides relus ; clés passées **par leur nom** sous `env -i` (`RR_ANTHROPIC_API_KEY_RIGAUD`,
   `GEMINI_API_KEY`, `OPENAI_API_KEY`), sans `ANTHROPIC_BASE_URL` ; jamais une valeur affichée.
1. **Machine** : louée sous GO-2026-11-14-14 (part machine 3 USD), processeur seul ; prix horaire consigné ; identifiant au registre
   des instances. Avec 4 processeurs, `generer` prend ≈ 12 min ; le reste, quelques minutes plus la durée des 16 appels réels.
2. **Arbre** : clone en lecture du dépôt public de l'organisme, paquets v68 à v71 puis le paquet v74
   (`organisme-v74-pilote-mr2-compte-organisme-v1.bundle`, `1cda2feb88e297d758bed7d0bb30d93cbe9b196ac3ab789826d39cfa4506d48b`, prérequis
   `e7daf32`), `git bundle verify`, tête `605e0f6` ; interpréteur avec **numpy 2.5.3** (le mode réel le refuse sinon). Copier le
   **texte scellé** et le **dossier entier de la sonde v74** (relevé `f56d9c0e…` et pièces de ses huit appels, branche
   `lot/compte-organisme-v1`, `docs/notes/organisme-multi-generations-v1/pilote-v1/sonde-complete-v74-compte-organisme/sonde-complete-v74/`) :
   le mode réel relit les faits de la sonde dans ses pièces. `bloc --releve-sonde RELEVE` doit rendre le bloc égal à celui du texte.
3. **Secret** : `secret DOSSIER_PRIVE/secret.bin` (dossier privé, hors de tout dépôt) → empreinte imprimée → **inscrite et poussée**
   par la mère ; **puis** la phrase de Lazar, dans un fichier privé → empreinte inscrite. Ni le secret ni la phrase ne sont publiés.
4. **Mondes** : `generer --secret DOSSIER_PRIVE/secret.bin --phrase-fichier DOSSIER_PRIVE/phrase.txt --texte TEXTE --texte-sha256 8aa33014… --sortie DOSSIER_PRIVE/MONDES.json`
   → contrôles et empreintes seulement ; empreintes des quatre mondes (fichier `.engagement.json`) **au registre**. Un monde sans
   tirage conforme → arrêt, cause écrite (liste d'arrêt).
5. **C-16, C-17** : `preparer --mondes M --mondes-sha256 H` ; tout refus → arrêt avant tout appel.
6. **Essai à blanc** (vraies pièces servies, proposeurs factices) : `jouer --mode a_blanc --mondes M --mondes-sha256 H --sortie DOSSIER_BLANC`,
   puis `rapatrier --source DOSSIER_BLANC --destination …` (rapatriement essayé, exigé par le texte).
7. **Pilote réel**, une seule fois : `jouer --mode reel --mondes M --mondes-sha256 H --sortie DOSSIER --go-pi1 GO-2026-11-14-13 --go-pi2 GO-2026-11-14-14 --registre-go COPIE_HORS_DEPOT_DE_GO.md --texte TEXTE --texte-sha256 8aa33014… --mondes-shas S1,S2,S3,S4 --registre-lancements FICHIER_HORS_DEPOT --releve-sonde RELEVE`.
   Code 3 = arrêt (pièces versées, **aucune issue lue, pas même P-0**, nœud de Lazar).
8. **Mesure**, une seule fois : `mesurer --sortie DOSSIER --mondes M --mondes-sha256 H` ; puis `lire --sortie DOSSIER` par un
   **sous-agent neuf** qui applique les critères gelés.
9. **Rapatriement** : `rapatrier --source DOSSIER --destination … --mondes M --mondes-sha256 H` (jamais les mondes) ; dépense par
   relais rapprochée ; **machine détruite par son identifiant** (R10), arrêt consigné.

## Points d'attention tirés de la répétition

- La génération est l'étape longue (≈ 12 min sur 4 processeurs) ; prévoir la machine en conséquence, sans changer de code.
- Le lanceur refuse un dossier de sortie existant, un texte d'une autre empreinte, un numpy différent : contrôles à faire avant
  l'étape 7, comme à la sonde.
- `ecrire_prive` n'écrit que dans le dossier du secret (liste blanche) : garder secret, phrase et mondes dans le même dossier privé.
