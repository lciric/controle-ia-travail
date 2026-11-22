# Erratum 1 du code des épreuves du devin, v2 (classe B)

- **Date** : 2026-11-22, vers 14:45 UTC. **Auteur** : session des chantiers du 21 (Opus 5.5), qui consigne.
- **Vise** : `src/controle_ia/devin_v2/` (rapport `rapport-code-devin-v2.md`), après la vérification du même contre-lecteur, `verification-code-devin-v2-opus-v1.md` (`800681bf…`). Verdict : « conforme après corrections ». C1 à C18 fermés ; C19 renvoyé au concepteur ; 35 mutations sur 35 tuées ; essais déterministes sur deux passes.
- Les fichiers scellés ne sont pas réécrits (R12). V1 se porte à la prochaine version du paquet, qui suivra de toute façon l'erratum de la conception (option d, GO-2026-11-22-70). D'ici là, cet erratum la déclare.

## V1, moyen : l'étage 1 dépend du générateur global de numpy

Constat : la régression logistique de l'étage 1 (solveur liblinear) n'a pas de `random_state`. Une même course, aux mêmes racines, jouée dans deux processus peut rendre une empreinte de famille différente pour la cible A1, et en général des M et p différents. Les essais restent déterministes parce qu'aucune assertion ne lit ces coefficients. Défaut manqué en v1, sans lien avec les corrections.

Correction mot pour mot, `src/controle_ia/devin_v2/predicteurs.py`, lignes 213 à 215 :
- `cv, _ = _cv(graine)` devient `cv, rs = _cv(graine)` ;
- `LogisticRegression(solver="liblinear", max_iter=2000)` devient `LogisticRegression(solver="liblinear", max_iter=2000, random_state=rs)`.

Essai à ajouter : `test_etage1_independant_du_generateur_global`, dont le texte exact est dans la vérification. Le contre-lecteur l'a joué dans sa copie : deux processus rendent alors des verdicts identiques à l'octet.

**Portée d'ici la prochaine version** : tout verdict de l'étage 1 du code v2 est rapporté comme « non rejouable d'un processus à l'autre ». Aucun verdict d'admission ne s'appuie sur lui.

## Effet de bord bénin, noté

Un verdict « sans objet » est aussi refusé quand B < 999, parce que la garde passe avant l'inventaire.

## Écart accepté

C4 : aucune course ne tire au hasard, même pour le chemin par défaut. La source système est remplacée par une source fixe, et un essai vérifie que les racines passent par elle. Le contre-lecteur juge l'écart meilleur que sa proposition.
