# Consigne — vérification de la seconde passe de corrections du code de T0.8 — v1

Écrite le 2026-11-14T03:33:43Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A). Destinataire : le vérificateur de la vérification courte des corrections (modèle B), qui la poursuit. **Aucune dépense, aucune instance, aucun téléchargement, aucune clé.**

## 0. Interdits et règles

Ceux de la consigne `brouillons/t08-code-compte4-v1/consigne-verification-courte-corrections-t08-v1.md` (`31c657163c6918a7efffe339f95cfdc1b4ac6b7a7cc1169b08328093e7fd50cb`), §§ 0 et 1, inchangés. S'y ajoute la permission de lire les sorties factices sous `/home/user/t08-code-compte4-v1/essai/t08-jouet-compte4-v3/a/` et `…/b/`. Toujours pas de rejeu de l'essai de bout en bout.

## 1. Objet

La seconde passe (développeur neuf, modèle A ; consigne `brouillons/t08-code-compte4-v1/consigne-developpeur-corrections-2-t08-v1.md`, `dccd725f93e95ba75037191fccf8bc463e607ad1f870b75601ae332fd7057abb` ; choix C4-0037 du journal `registres-provisoires/compte-4-2026-11-14-v6.md`, `4029099988dddb13150d69fa2c77fb60d57a846b84c9f2e4774d60b6e06855b6`) traite VCT8-01 à VCT8-07. Tête finale `453a71e1c6729d7ec5d43e3a4a0e3522dfd38579` (code et essais figés depuis `47b20451`) ; rapport `/home/user/t08-code-compte4-v1/docs/notes/t08-code-compte4-v1/rapport-developpeur-corrections-2-t08-v1.md`, `6803a5271bbab20192f4b0980be63654a9deb607bee1c44c1e10d53ab5849ac0`. Différentiel : `git -C /home/user/t08-code-compte4-v1 diff 7a4d4e13 453a71e1 -- src/controle_ia/t08 tests`.

## 2. Ce que tu vérifies

1. Chacun de VCT8-01 à VCT8-07 : corrigé selon C4-0037 et le § 3 de la consigne de la passe ; essai sain et artefact réels (mutations au besoin) ; classe « corrigé », « corrigé avec réserve », « non corrigé ».
2. Défauts neufs du différentiel (mêmes critères qu'au § 4, point 2, de ta consigne précédente), en priorité : la lecture de `CODE-T08` sous deux formes (Q-D1), l'entrée neuve `manifeste_course` de la liste blanche (**Q-D2** : le point 1 du plan ne la nomme pas ; dis si c'est un écart au texte, et sa gravité), le passage à blanc (Q-D3), la pièce HD (Q-D4).
3. Déterminisme : `essai/t08-jouet-compte4-v3/a` contre `…/b` (52 fichiers, 0 différent selon le rapport) ; exclusion déclarée du comparateur ; contrôle dans chaque racine.
4. Questions Q-D1 à Q-D7 : même classement qu'avant.
5. Essais rejoués : tous les `tests/test_t08_*_v1.py` (142 selon le rapport) et les cinq essais d'inventaire.
6. **Le commit citable** : la tête `453a71e1` peut-elle être citée par `COMMIT_CODE_T08` (tous les fichiers des chemins gelés de `harnais/validation_reelle.py` égaux entre ce commit et la tête que l'instance exécutera si elle clone cette branche) ?

## 3. Ce que tu rends

`/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/verification-corrections-2-t08-v1.md`, scellé puis vérifié ; script éventuel `…/verification-corrections-2-t08-v1-calcul.py`, scellé, sortie recopiée. Sections : **0. Identité** (« modèle B ») ; **1. Verdict** (« citable par le texte candidat tel quel », « citable après les corrections listées » ou « non citable en l'état » ; nombres de constats par gravité) ; **2. Constats neufs** (`VCT8B-01`…) ; **3. VCT8-01 à VCT8-07 revus** ; **4. Déterminisme** ; **5. Questions Q-D1 à Q-D7** ; **6. Essais rejoués** ; **7. Limites**. Dernier message : verdict en trois lignes, nombres, chemins et empreintes, identifiant de modèle. Si ton temps s'épuise : rapport partiel scellé.
