# Contre-lecture du correctif C3 des clés du registre (classe B)

Pièce lue : branche `t08/correctif-cles-registre-v1`, commit C3 6735dd2e1 (parent C2 3c0f60f9f), pièces au commit 1cff7cc0f. Contre-lecteur neuf, aucune dépense.

## Verdict : conforme

## Vérifications
1. Différentiel C2 vers C3 : six fichiers exactement (`entrees_v1.py`, `lecture_v1.py` neuf avec compagnon, essai neuf, compagnons) ; empreintes concordantes.
2. Pas de relâchement : `_dans_famille` n'accepte que la clé exacte ou `base-V…` ; `SCELLEMENT-T08-BASE-A` n'en est pas. Zéro ou deux correspondances arrêtent ; `-VX`, `-V0`, `-V02` arrêtent ; l'antériorité porte sur les deux lignes retenues (essai « tard » : arrêt). Les clés rendues `SCELLEMENT-T08` et `CODE-T08` du résultat restent celles que lisent les appelants.
3. Grep dans src/, scripts/, .claude/hooks/ : seules `entrees_v1.py` et `lecture_v1.py` lisent ces clés ; le reste est commentaire ou nom de marqueur.
4. 125 essais réussis (cles_famille, chaine_lecture, lecture_course, entrees_rendu, gardes_corrections, garde_clone_partiel). Mutation (clé exacte seule) : 3 échecs sur 3 essais neufs.
5. Pièces de 1cff7cc0f comparées aux v2 de `main` : texte v3 = v2 plus l'additif et la valeur du marqueur du commit du code ; configuration v3 et marqueurs v3 = v2 sauf `COMMIT_CODE_T08`.

## Mineure
Une clé `…-V` quelconque (ex. `SCELLEMENT-T08-VERSION`) arrête même si étrangère : prudent, à savoir avant d'inscrire de nouvelles clés.
