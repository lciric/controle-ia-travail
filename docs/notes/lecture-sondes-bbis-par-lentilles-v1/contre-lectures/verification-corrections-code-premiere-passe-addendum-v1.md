# Vérification des corrections portées après la contre-lecture du code de la première passe — v1

Rendu du même contre-lecteur (Opus 5.5), versé tel quel par la session des lentilles le 2026-11-20. Son mandat : `mandats/mandat-contre-lecteur-code-premiere-passe-addendum-v1.md` (`bdcc0d96…`). Commit vérifié : `72c05a03`, sur la branche `claude/brave-galileo-jhp684`.

## Verdict

**Les trois corrections demandées (1 à 3) sont portées.**
- Aucun code n'a changé sous `src/` depuis le commit `2e15977b`.
- La passation ne dit rien de faux sur l'état du code. Une de ses phrases sur les essais est imprécise, sans conséquence.

## Vérifications faites

**Empreintes** : toutes égales.
- `tests/test_lentilles_sondes_bbis_contre_lecture_addendum_v1.py` : `d69eac83…`
- `developpement/conformite-code-a-l-addendum-concentration-scelle-v2.md` : `70bc6c24…` ; fichier compagnon OK.
- `developpement/passation-developpeur-deux-passes-2026-11-20-etape-1-close-v1.md` : `708203b1…` ; fichier compagnon OK.

**Essais** : le fichier d'essais neuf donne 3 réussis.

**Altérations** : chacune est jouée dans une copie jetable du paquet, sans altération la copie donne 3 réussis, et chaque altération fait tomber l'essai qui la vise.

| Altération | Essais qui tombent |
|---|---|
| Critère de l'heure retiré de la garde qui exige la ligne de l'addendum | 1 |
| Bornes de départage données seulement à la première direction marquée | 2 |
| Borne haute de la valeur p calculée avec S_min au lieu de S_max | 2 |

## Par correction

**1. Note de conformité : portée.**
- La v2 laisse la v1 intacte.
- Son § 6 nomme les deux ajouts au lanceur qui ne viennent pas de l'addendum, aux lignes 872 et 874 (vérifiées) :
  - l'exigence du rapport du montage ;
  - le champ d'égalité de la relecture de l'audit.

**2. Plusieurs directions marquées dans un même nul : portée.**
- Le jouet porte trois directions marquées, de bornes (2, 3), (2, 3) et (3, 4).
- Pour quatre valeurs de S(v), l'essai compare à l'énumération conjointe :
  - la borne basse et la borne haute de la valeur p ;
  - la valeur p écrite ;
  - l'attendu.
- Il est joué avec un artefact.

**3. Ligne des entrées placée après la ligne de l'addendum mais d'heure antérieure : portée.**
- Le cas sain et l'artefact sont joués seuls, sur les deux gardes.

## Passation du développeur

**Exacte sur ces points** :
- aucun code changé ;
- empreinte du fichier d'essais commité : `cf92419d…` ; `1abbe232…` était celle d'avant son dernier changement ;
- les noms réemployables existent ;
- `statistiques_v4` est encore libre ;
- empreinte de la contre-lecture : `7954d0fc…`.

**Imprécision non bloquante** : elle dit que les essais neufs « n'importent que `entrees_v3`, `statistiques_v3` et les jouets ». En réalité, ils chargent aussi `lanceur_v4`, `lecture_v1`, `nuls_v1`, `audits_v1`, `statistiques_v1` et les jouets v4, par l'import des fichiers d'essais de l'étape 1.

## Expositions

- **Noms vus sans être ouverts** : le `git pull` a affiché les noms de deux branches neuves de verdicts (préfixe `verdict/`). Aucune n'a été extraite ni lue.
- **Ce qui a été ouvert** : les seules pièces nommées.
- **Aucun refus d'outil.**
- **Aucune écriture** : ni commit ni push.
