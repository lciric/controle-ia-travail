# Inventaire du coffre du bras d'attaque — v2 : diagnostic des empreintes (10 novembre 2026, 06:39 à 06:50 UTC)

Complète la v1 (inchangée). Mot direct de Lazar : « (a) go » (un lecteur affiche seulement les chemins). Fait par programme,
à divulgation graduée : un chemin n'est montré en entier que s'il existe sur `main` ; sinon seuls ses composants déjà
présents dans le vocabulaire des chemins de `main` sont montrés. **Aucun contenu lu ni affiché.** Scripts éprouvés sur un
dépôt d'essai (cas sain, artefacts plantés, branche absente). Correction de la v1 : elle ne voyait que les compagnons ajoutés
ou modifiés sur la branche ; la v2 parcourt tous les compagnons de l'arbre.

## Sortie du diagnostic (tout l'arbre de chaque branche)

## `donnees/argon-classes-ecart-v1`
- compagnons dans l'arbre : 4752 ; identiques à main, cible et compagnon (non recalculés) : 4644 ; recalculés conformes : 5 ; non conformes : 0
- compagnons sans cible : hérités (compagnon sur main, cible absente de main aussi) 103 ; compagnon sur main mais cible présente sur main 0 ; propres à la branche (compagnon absent de main) 0
- hérités, par répertoire de tête : docs 1 ; gemini 61 ; traces 35 ; brouillons 5 ; donnees 1 ;
## `donnees/bras-attaque-parametres-v1`
- compagnons dans l'arbre : 4765 ; identiques à main, cible et compagnon (non recalculés) : 4657 ; recalculés conformes : 5 ; non conformes : 0
- compagnons sans cible : hérités (compagnon sur main, cible absente de main aussi) 103 ; compagnon sur main mais cible présente sur main 0 ; propres à la branche (compagnon absent de main) 0
- hérités, par répertoire de tête : docs 1 ; gemini 61 ; traces 35 ; brouillons 5 ; donnees 1 ;
## `donnees/bras-attaque-texte-III-v1`
- compagnons dans l'arbre : 2 ; identiques à main, cible et compagnon (non recalculés) : 0 ; recalculés conformes : 2 ; non conformes : 0
- compagnons sans cible : hérités (compagnon sur main, cible absente de main aussi) 0 ; compagnon sur main mais cible présente sur main 0 ; propres à la branche (compagnon absent de main) 0
## `donnees/bras-attaque-v1-arret-r597`
- compagnons dans l'arbre : 1 ; identiques à main, cible et compagnon (non recalculés) : 0 ; recalculés conformes : 1 ; non conformes : 0
- compagnons sans cible : hérités (compagnon sur main, cible absente de main aussi) 0 ; compagnon sur main mais cible présente sur main 0 ; propres à la branche (compagnon absent de main) 0
## `donnees/mode-tenu-a-l-ecart-v1`
- compagnons dans l'arbre : 3338 ; identiques à main, cible et compagnon (non recalculés) : 3235 ; recalculés conformes : 1 ; non conformes : 0
- compagnons sans cible : hérités (compagnon sur main, cible absente de main aussi) 102 ; compagnon sur main mais cible présente sur main 0 ; propres à la branche (compagnon absent de main) 0
- hérités, par répertoire de tête : gemini 61 ; traces 35 ; brouillons 5 ; donnees 1 ;
## `donnees/course-2-axe-6-v1`
- compagnons dans l'arbre : 4809 ; identiques à main, cible et compagnon (non recalculés) : 4702 ; recalculés conformes : 3 ; non conformes : 0
- compagnons sans cible : hérités (compagnon sur main, cible absente de main aussi) 104 ; compagnon sur main mais cible présente sur main 0 ; propres à la branche (compagnon absent de main) 0
- hérités, par répertoire de tête : docs 1 ; gemini 61 ; traces 36 ; brouillons 5 ; donnees 1 ;
## `donnees/course-2-axe-6-sorties-v1`
- compagnons dans l'arbre : 4834 ; identiques à main, cible et compagnon (non recalculés) : 4724 ; recalculés conformes : 6 ; non conformes : 0
- compagnons sans cible : hérités (compagnon sur main, cible absente de main aussi) 104 ; compagnon sur main mais cible présente sur main 0 ; propres à la branche (compagnon absent de main) 0
- hérités, par répertoire de tête : docs 1 ; gemini 61 ; traces 36 ; brouillons 5 ; donnees 1 ;
## `donnees/ideation-pilier-attaque-v1`
- NON CONFORME n° 1 : docs/… (profondeur 7, extension .jsonl) ; sur main : non ; empreinte attendue bien formée : oui ; cible identique à celle de main : — ; compagnon identique à celui de main : — ; conforme sur main : — ; dernier commit de la cible : 2026-11-08T11:44Z ; du compagnon : 2026-11-08T11:32Z
- NON CONFORME n° 2 : docs/… (profondeur 7, extension .md) ; sur main : non ; empreinte attendue bien formée : oui ; cible identique à celle de main : — ; compagnon identique à celui de main : — ; conforme sur main : — ; dernier commit de la cible : 2026-11-08T11:44Z ; du compagnon : 2026-11-08T11:32Z
- compagnons dans l'arbre : 7892 ; identiques à main, cible et compagnon (non recalculés) : 7715 ; recalculés conformes : 71 ; non conformes : 2
- compagnons sans cible : hérités (compagnon sur main, cible absente de main aussi) 104 ; compagnon sur main mais cible présente sur main 0 ; propres à la branche (compagnon absent de main) 0
- hérités, par répertoire de tête : docs 1 ; gemini 61 ; traces 36 ; brouillons 5 ; donnees 1 ;

## Instruction des deux non conformes (`donnees/ideation-pilier-attaque-v1`)

- n° 1 : docs/notes/ideation-pilier-attaque-v1/collisionneur-v1/tour/‹propre, 24 caractères›/journal.jsonl ; catégorie du nom : journal ; scellé juste à l'instant du compagnon (commit 48c27cb7) : oui ; commits qui touchent la cible ensuite : 2 ; lignes ajoutées / retirées depuis : +9 / -0 ; lignes alors 3, maintenant 12 ; la version scellée est un préfixe exact de la version actuelle : oui
- n° 2 : docs/notes/ideation-pilier-attaque-v1/collisionneur-v1/tour/‹propre, 24 caractères›/etat.md ; catégorie du nom : etat ; scellé juste à l'instant du compagnon (commit 48c27cb7) : oui ; commits qui touchent la cible ensuite : 2 ; lignes ajoutées / retirées depuis : +7 / -2 ; lignes alors 8, maintenant 13 ; la version scellée est un préfixe exact de la version actuelle : non
- total non conformes : 2

## Lecture
1. **Les deux non conformes sont des fichiers vivants d'une course du collisionneur** (journal et état), scellés justes au
   commit `48c27cb7` (8 novembre, 11:32 UTC), puis continués par la course (deux commits) : journal prolongé de 9 lignes, la
   version scellée en est un préfixe exact ; état réécrit (+7, −2). Scellé posé trop tôt, pas une altération : la version
   scellée existe intacte dans l'historique à `48c27cb7`. Aucune fiche ni cellule n'est concernée.
2. **Aucun compagnon sans cible n'est propre au coffre** : les 102 à 104 sont hérités de `main` (répertoires de tête
   `gemini`, `traces`, `brouillons`, `donnees`, `docs`). Non expliqué : `verifier-arbre` n'en signale qu'un sur `main` ;
   l'écart entre « absent de l'arbre git » et sa lecture du disque reste à instruire (hors coffre).
3. Les branches n'ont pas été modifiées (R12). Remède proposé pour le point 1 : une ligne à l'index du bras donnant le commit
   de la version scellée ; la branche appartient à la lignée d'idéation, qui décide d'un compagnon de l'état final.
