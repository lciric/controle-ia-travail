# Rapport du rédacteur — consigne des lecteurs du rejeu, version 3 — v1

- **Pièce de travail (classe C).** Écrit le 2026-11-20 par un rédacteur neuf, modèle F, qui n'a lu aucune carte. Processeur seul, aucune dépense, aucun appel de modèle. Rien n'est écrit dans le dépôt, aucun commit.
- **Mandat** : `mandat-redacteur-consigne-lecteurs-rejeu-v3-v1.md`, sha256 `1607797a2c6b050890913e901c1db364188b0123f81ea26d9214cf5a1a8c4827`, égal à son compagnon.
- **Dossier de rendu** : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-consigne-lecteurs-rejeu-v3/`.

## Verdict

La v3 est écrite par l'outil, en **quatre remplacements** : deux de fond au § 4, deux de tenue. Le différentiel, lu en entier, ne porte que ces quatre changements. Aucun refus, aucun écart au mandat.

## 1. Empreintes vérifiées avant d'écrire

| pièce | sha256 recalculée | attendue |
|---|---|---|
| consigne v2 (`consigne-lecteurs-rejeu-criteres-v7-v2.md`) | `1e5479bea761dce96ae60e4c93f7991965134c262e3db6ae5a2b66622cc2aa70` | `1e5479be…` : égale |
| contrôle du différentiel v1 → v2 | `e5c2179148d06fb0920f62a81377e8cfffab0316fe394dfdfeba3cb7a62313d6` | `e5c21791…` : égale |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` | `391db990…` : égale |
| garde, tirée de `origin/main` après `fetch` | `635e9160e0bf03cd70a25cd0532e638203c8bc621c502313e5f2491b4ba76585` | `635e9160…` : égale |

De la garde, j'ai lu les 45 premières lignes (l'en-tête et le début du code), rien de plus. L'en-tête dit : garde de la graphie de `lignee_reconnue`, jouée sur chaque lecture déposée avant l'assemblage, qui refuse toute valeur qui n'est ni une clé de `familles` du manifeste ni « aucune ». La phrase du § 4 de la consigne dit la même chose.

## 2. Les quatre remplacements

Chaque ancre a été comptée une fois dans la v2 par `grep -c -F -e` avant l'appel.

| n° | lieu | nature | ce qui change |
|---|---|---|---|
| 1 | titre | tenue | « — v2 » devient « — v3 ». |
| 2 | en-tête | tenue | une ligne « Version 3 » ajoutée après la ligne « Version 2 » : heure, mandat et son empreinte, les deux retouches, le contrôle cité avec son empreinte, la v2 remplacée avec son empreinte. |
| 3 | § 4, premier point | fond | « le programme ne voit pas » devient « le programme d'assemblage ne voit pas » : la retouche facultative du contrôle (son § 4), à la lettre. |
| 4 | § 4, premier point | fond | la phrase de garde nomme la pièce : `docs/notes/organisme-auto-conception-v9-mere/juge-selection-manifeste-v1/garde_lignee_reconnue_v2.py`, sha256 `635e9160e0bf03cd70a25cd0532e638203c8bc621c502313e5f2491b4ba76585`. Le reste de la phrase est inchangé. |

## 3. Ce que la mère peut vouloir regarder

- **Le chemin de la garde est donné au lecteur.** Le § 8 de la consigne lui interdit d'ouvrir autre chose que les cartes servies, les critères et la consigne : la garde est nommée, non ouverte. Je n'ai pas ajouté de phrase pour le redire, le mandat ne permettant aucune autre modification.
- **Les autres « le programme » du § 4** (« Le programme ne compare que la famille », « Le programme compte, après coup ») sont inchangés : la retouche du contrôle ne porte que sur la première phrase.
- **« À contre-lire par un autre modèle »**, dans la première ligne de l'en-tête, est inchangé. La v3 n'a pas été contre-lue : cela revient à qui la remet.
- **La garde est lue sur `origin/main`** telle qu'elle était après mon `fetch` ; je n'ai pas vérifié son essai ni son scellement, le mandat ne me donnant que son en-tête à lire.

## 4. Pièces rendues (toutes avec leur compagnon `.sha256`)

Les empreintes de ce rapport et celles des pièces sont dans les compagnons ; celles des quatre autres pièces sont redites dans la réponse du rédacteur.

- `consigne-lecteurs-rejeu-criteres-v7-v3.md` : sha256 `85efbd70fc7b1e78d897218711ab834b680b6500ce939436d103e7eaf25fa011` ;
- `remplacements-consigne-lecteurs-v2-v3-v1.json` : le fichier des quatre remplacements ;
- `consigne-lecteurs-rejeu-criteres-v7-v3.md.journal-remplacements-v1.json` : le journal de l'outil ;
- `differentiel-consigne-lecteurs-v2-v3-v1.diff` : `diff -u` de la v2 vers la v3 ;
- `garde_lignee_reconnue_v2.py` : la copie de la garde tirée de `origin/main`, gardée pour le contrôle de l'empreinte.

## 5. Lu, et incidents

- Lus en entier : le mandat, la consigne v2, le contrôle du différentiel v1 → v2, l'outil, le différentiel v2 → v3. Lu en partie : la garde (45 lignes).
- Aucune carte, rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Aucune commande de liste, une commande simple par appel, aucun code en ligne.
- La règle R-4067, que le mandat nomme, n'a pas été ouverte : je n'en ai pas le chemin et je ne cherche pas dans le dépôt. J'ai suivi ce que le mandat en dit (chaque ancre comptée avant l'appel).
- **Aucun refus** de permission, de classifieur ni de garde.

*rédacteur neuf, modèle F*
