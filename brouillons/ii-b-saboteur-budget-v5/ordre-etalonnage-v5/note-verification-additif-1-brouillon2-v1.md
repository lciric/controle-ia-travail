# Note de vérification courte — additif 1 à l'ordre v2 de l'étalonnage, brouillon 2 — v1

Date : 2026-11-22. Classe A. Même vérificateur (Claude Opus 5.5), même mandat ; aucune sortie de l'étalonnage lue. Pièce : `additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon2.md` (`0fed5e44…`, commit `8b2c15844`, compagnon vérifié).

**Verdict : conforme**, avec deux précisions d'exécution (p1, p2) que l'exécutante peut tenir sans toucher au texte.

- **Rejeu** : le programme du brouillon 2, joué sur le brouillon 1 (`f546a6ea…`) tiré de la branche, rend `0fed5e44…`, **identique à l'octet**. La note citée (`b8c8db48…`) est la mienne.
- **(1) Bornes** : le § 1 rend exactement le m1. 16 + 0,92 + 3,84 = 20,76 USD tenus, au-dessus des 17 USD de l'étape 1 (le devis, § 3 : « 17 dollars n'est pas une seconde ligne : c'est la dépense tenue… »), sous la coupure de 55 et sous le plafond de 60. Il ajoute le dépassement à la coupure et le forfait de téléchargement, tous deux à faire accepter par Lazar. **Garder la phrase inexacte de la documentation de `session_v5.py` est acceptable** : c'est un commentaire sans effet sur le code, l'additif prime, et le corriger changerait l'arbre vérifié. Il faudra la corriger avec le code de la course.
- **(2) Procédure du § 3 : sûre et exécutable.**
  - L'arbre `d1cc1d75b06a3c5f372ad4c1cf0f184026a23744` est retrouvé par `git apply --cached` du 0013 sur un index de `43d6d067`.
  - L'essai à blanc est juste : de la création à `1000057564` à 1 USD l'heure, on a 15,99 USD, d'où RIEN ; à `1000057600`, 16,00 USD, d'où ARRET ; une phase inconnue donne REFUS avec le code 1. C'est ce qu'a obtenu la mère.
  - L'arrêt se fait par le numéro de processus (R10). Le repli après un échec de `am` ou de l'essai est sans trou : `am --abort` ou `reset --keep` vers 43d6d067, puis relance telle qu'avant.
  - La relance ne remet pas le compte à zéro : la ligne AMORCE reste dans `$D/progres.txt`. Pendant l'interruption, la minuterie à 55 reste seule garde.
  - **La garde de 11 USD est bonne** : entre 11 et 12 USD restent environ 45 minutes à 1,22-1,38 USD l'heure, pour quelques minutes d'interruption.
- **p1** : `git am` crée un commit. Si `$DEPOT` n'a pas d'identité git, il échoue, et c'est alors le repli qui joue : la procédure n'est pas dangereuse, mais elle n'aboutit pas. Pour l'éviter : `git -C "$DEPOT" -c user.name=… -c user.email=… am …`. Même chose pour `git status --porcelain` « vide » : si `$D` est dans `$DEPOT` et n'est pas ignoré, le contrôle échoue. Il faut le vérifier avant l'étape 1, et, si c'est le cas, contrôler seulement les fichiers suivis (`git -C "$DEPOT" status --porcelain --untracked-files=no`).
- **p2** : la relance de la surveillance exige les mêmes préalables qu'au premier lancement (`lancer_iib_v3.sh`, branche `surveillance`, lignes 4 à 12 du cas) : `$D/lancement.txt` et l'identifiant qu'il porte, `HF_TOKEN` posé en mode réel, l'outil `VAST`. « Même environnement `ENVI` » les couvre, à condition que `HF_TOKEN` y soit, par son nom. Un refus (code 2) laisse l'étalonnage sans surveillance : il faut le dire aussitôt à la mère.
