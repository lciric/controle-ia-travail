# Vérification des corrections — code de la course, organisme retenu du saboteur à budget, v5 (cl1)

Date : 2026-11-22. Même contre-lecteur que la contre-lecture (Claude Opus 5.5) ; mêmes interdits respectés. Rien poussé, aucune dépense.

**Verdict : course autorisable** (code). Le correctif 0019, appliqué par `git am` dans le worktree neutre `scratchpad/cl-p1`, donne l'arbre `cd2366af52f1c05e2773a7daa0755d97703495cc`, celui annoncé. La liste de la course, torch compris, rend **296 passed** (10 min 50 s) : aucune régression.

## Les quatre corrections

**M1, levé : la course ne s'engage qu'une fois par étalonnage.**
- Le témoin `course-engagee-iib-v5.json` est écrit, scellé et poussé après toutes les gardes d'avant le premier tour, et avant le premier épisode.
- `exiger_course_non_jouee` refuse tout dossier qui porte ce témoin.
- L'amorce de la course cherche la référence distante `essai/iib-course-engagee-<run de l'étalonnage>` par `ls-remote` :
  - code 0 (la référence existe) : refus ;
  - code 2 (absente) : elle la pousse, puis passe à l'installation ;
  - tout autre code : refus.
- Essais : course morte avant son premier tour non relancée ; témoin poussé avant le premier tour ; une seconde machine refusée, avec un « FIN » absent.

**m1, levé : identifiants de l'étalonnage exigés en mode réel.** Le résumé de l'étalonnage est vérifié par son sceau. La course refuse s'il n'y a aucun fichier d'identifiants, ou si leur nombre diffère des lots déclarés par le résumé (champ `resultat.lots`). Essais : un cas sain, un fichier en moins et un fichier en plus.

**m2, levé : délai de consignation porté à 3 600 s.**

**m3, levé : le saut de l'essai du préfixe propre devient une assertion.**

## Points qui restent pour l'ordre de la course

1. **Nombre d'essais attendus** : `TESTS_ATTENDUS=296` pour la liste de la course, torch compris ; 294 pour la liste v6.
2. **Course sur une machine neuve (nœud C1)** : c'est un écart au devis, qui compte une seule location. Il demande le mot de Lazar. Le surcoût est d'environ 2,0 USD, et de 6,5 USD au pire.
3. **Dépense antérieure** : `IIB_DEPENSE_ANTERIEURE_USD` vaut la dépense de l'étalonnage plus le stockage de sa machine à l'arrêt. Cette machine est détruite après le rapatriement vérifié.
4. **Calendrier** : aucune création à partir du 2026-11-27T00:00Z ; le dernier jour de création est le 26 novembre.
5. **Première action « gardée »** : un mot explicite de Lazar est attendu avant le scellement de l'ordre.
6. **Référence d'engagement poussée avant l'installation.** Toute fin anormale de l'amorce, même aux essais, consomme l'engagement de la course. Une relance demanderait donc le mot de Lazar et un devis neuf, et la suppression de la référence par la mère. L'ordre doit l'écrire.
