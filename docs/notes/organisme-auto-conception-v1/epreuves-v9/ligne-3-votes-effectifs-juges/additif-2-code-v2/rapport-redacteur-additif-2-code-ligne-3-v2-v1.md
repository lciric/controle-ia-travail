# Rapport du rédacteur — additif 2 (additif de code) de la ligne 3, version 2 — v1

Pièce de travail (classe C). Écrite le 2026-11-20 (temps universel), sous le mandat `mandat-redacteur-additif-2-code-v2-v1.md` (`2e602121ac8675582bf80083c69035899ee0c1d1c7aab1b07ae6fb2bf57b97e8`, égale à son compagnon). Les fichiers rendus n'existent que dans le bloc-notes, dossier `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-additif-2-code-v2/`. Rien n'est écrit dans le dépôt, rien n'est committé.

## Verdict

La version 2 est écrite : `additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v2.md`, `186501571b1e6cf03e3abff1991a987f86ed591a0bda00864e3df77f851c0ce5`. Elle porte les corrections A, B et C de la contre-lecture, à la lettre, plus la tenue (titre, ligne de version). Sept remplacements, par l'outil contre-lu. Rien de gelé ne change. Elle reste à sceller par la mère.

## Sources, empreintes vérifiées

| pièce | sha256 | contrôle |
|---|---|---|
| mandat | `2e602121ac8675582bf80083c69035899ee0c1d1c7aab1b07ae6fb2bf57b97e8` | `sha256sum -c` du compagnon : OK |
| contre-lecture | `7cf5a2c99e678ab0c3a3580121ac1d2be388cfcbf22fc959958cd3ec2546fc41` | compagnon : OK ; lue en entier |
| additif v1 (cible) | `656094057c4ea3ebdd08049883531180be1f91572600b03d0a8738734ee330ae` | compagnon : OK ; lu en entier |
| rapport du rédacteur v1 | compagnon : OK | lu en entier |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` | début égal au mandat ; lu en entier |

## Les sept remplacements

| n° | lieu (ligne de la v1) | objet |
|---|---|---|
| 1 | titre (1) | « — v1 » devient « — v2 » |
| 2 | ligne de version (3) | « version 1, non scellée » devient « version 2, non scellée » |
| 3 | ligne de version (3) | une phrase ajoutée en fin de ligne : la version 2 porte A, B et C de la contre-lecture (nom et empreinte) sur la version 1 (empreinte), aux § 6 et 7 ; rien d'autre ne change |
| 4 | § 6, puce `CHEMIN` (126) | correction A, texte de la contre-lecture |
| 5 | § 6, puce « Environnement » (130) | correction C, texte de la contre-lecture |
| 6 | § 7, point 1 (136) | correction B, première phrase, ajoutée en fin de point |
| 7 | § 7, point 3 (138) | correction B, seconde phrase, ajoutée en fin de point |

Chaque ancre a été comptée par `grep -c -F -e` sur la cible avant l'appel : une ligne chacune. L'outil a rendu « FAIT : 7 remplacement(s) », sans avertissement. Les deux pièces (contre-lecture, additif v1) ne portent ni espace insécable ni apostrophe courbe (compté) : les textes neufs sont ceux de la contre-lecture, caractère pour caractère, entre ses guillemets.

Le différentiel `diff -u` montre sept lignes changées (1, 3, 126, 130, 136, 138 — la ligne 3 porte deux remplacements — soit six lignes de fichier), et rien d'autre.

## Fichiers rendus (chacun avec son compagnon `.sha256`, vérifié par `sha256sum -c`)

| fichier | sha256 |
|---|---|
| `additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v2.md` | `186501571b1e6cf03e3abff1991a987f86ed591a0bda00864e3df77f851c0ce5` |
| `remplacements-additif-2-code-v1-vers-v2-v1.json` | `dc0d4e5716987a9a5c8fb1c9f6c52455a81069473c4d7d976d980c0dbe444772` |
| `additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v2.md.journal-remplacements-v1.json` | `dcf33c706f27f5630b0c5b1814606a28f58616d9603c51a155da75886630ea03` |
| `additif-2-code-v1-v2.diff` | `b5a412ec24a04494c61b3281c4c922d527ca76e4c546114025cfce17ecaf0a5a` |

## Réserves, points laissés à la mère

1. **§ 9, réserve 3, laissée telle quelle.** Elle dit encore que cet additif ne fixe pas le lieu de dépôt des sorties, « § 7, point 1, pour la seule contrainte connue ». Après la correction B, le point 1 porte deux contraintes (pas d'`archives-reponses-modeles/`, pas de sortie sous le dossier du code). La phrase reste vraie dans son sens (le lieu n'est pas fixé, seulement borné), mais « la seule » est devenu inexact. Le mandat interdit toute autre modification : je ne l'ai pas touchée.
2. **Ligne de version.** Le mandat dit « tenue : titre, ligne de version » sans en donner le texte. J'ai changé le numéro et ajouté une phrase qui nomme la contre-lecture et la version 1 par leurs empreintes. La date et l'heure d'écriture de la version 1 y restent, non changées.
3. **Correction C** (facultative) : portée. La version de `numpy` 2.5.3 est celle que le contre-lecteur a relevée ; je ne l'ai pas relevée moi-même (aucun interpréteur lancé hors `python3 --version`, qui rend 3.13.18, et l'outil de remplacement).
4. **§ 1 et § 9 parlent à la première personne du rédacteur de la version 1** (« je n'ai lancé… ») : inchangés ; ils restent vrais pour moi aussi (aucun banc, aucun chronométrage, aucun essai, aucune graine).
5. La version 2 n'a pas été contre-lue : les textes A, B, C sont ceux du contre-lecteur, mais le contrôle de leur pose revient à la mère (le différentiel le permet d'un coup d'œil).

## Refus, écarts

- **Aucun refus de permission, de classifieur ou de garde.**
- Une commande a rendu une erreur qui n'est pas un refus : un premier `grep -c -P` sur des points de code (« character code point value … too large », affaire de paramètres régionaux) ; refaite par `grep -c -F -e` avec les caractères mêmes. Une autre a rendu un décompte sans valeur (espaces insécables changés en espaces ordinaires dans la commande) ; refaite aussi.
- Aucune commande de liste, aucun heredoc, aucun code en ligne, aucun calcul de l'étage 1, aucun lancement du banc, aucun appel de modèle, aucune dépense, aucune écriture dans le dépôt. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`.

Rédacteur neuf, modèle F.
