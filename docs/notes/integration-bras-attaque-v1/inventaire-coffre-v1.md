# Inventaire mécanique du coffre du bras d'attaque — v1 (10 novembre 2026, 06:27 UTC)

Session `session_01QPDgKgcLdggoVJfGC5cBw8` (rôle de session-dépôt, mot direct de Lazar). Fait par le script
`inventaire_coffre_v1.sh` (même dossier), qui n'affiche que des comptes, des commits et des dates : **aucun nom de fichier,
aucun contenu n'a été affiché ni lu**. Script éprouvé avant usage sur un dépôt d'essai : cas sain (1 conforme), artefacts
plantés (1 non conforme, 1 cible absente), branche inexistante (échec signalé).

« Fichiers propres » = fichiers ajoutés ou modifiés depuis l'ancêtre commun avec `main` (les branches anciennes portent donc
des milliers de fichiers hérités de leur lignée, pas seulement le coffre).

| branche | commit | premier commit propre (UTC) | dernier commit (UTC) | commits propres | fichiers propres | compagnons .sha256 | empreintes conformes | non conformes | cible absente |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| `donnees/argon-classes-ecart-v1` | `5c5f5ff2` | 2026-10-29T11:25Z | 2026-10-29T11:25Z | 1 | 10418 | 4752 | 4649 | 0 | 103 |
| `donnees/bras-attaque-parametres-v1` | `8e96043e` | 2026-10-04T03:27Z | 2026-10-30T11:55Z | 1228 | 10444 | 4765 | 4662 | 0 | 103 |
| `donnees/bras-attaque-texte-III-v1` | `3a3c5465` | 2026-10-30T15:48Z | 2026-10-30T15:48Z | 1 | 4 | 2 | 2 | 0 | 0 |
| `donnees/bras-attaque-v1-arret-r597` | `91c883ff` | 2026-10-28T12:05Z | 2026-10-28T12:05Z | 1 | 21 | 1 | 1 | 0 | 0 |
| `donnees/mode-tenu-a-l-ecart-v1` | `ab6c5590` | 2026-10-04T03:27Z | 2026-10-28T08:40Z | 992 | 7586 | 3338 | 3236 | 0 | 102 |
| `donnees/course-2-axe-6-v1` | `36e1a8c9` | 2026-10-04T03:27Z | 2026-10-30T07:51Z | 1244 | 10540 | 4809 | 4705 | 0 | 104 |
| `donnees/course-2-axe-6-sorties-v1` | `39a5b9e6` | 2026-10-04T03:27Z | 2026-10-30T01:00Z | 1265 | 10590 | 4834 | 4730 | 0 | 104 |
| `donnees/ideation-pilier-attaque-v1` | `6f62659e` | 2026-10-04T03:27Z | 2026-11-08T16:19Z | 2328 | 16892 | 7892 | 7786 | 2 | 104 |

## Constats
1. Les huit branches existent et se rapatrient ; aucune empreinte non conforme sur sept d'entre elles.
2. **Deux empreintes non conformes sur `donnees/ideation-pilier-attaque-v1`** : non identifiées (le script ne nomme rien). À
   instruire par un lecteur qui n'affiche que les chemins, après accord de Lazar (un chemin peut porter un nom de classe).
3. **102 à 104 compagnons sans cible** sur six branches : nombre presque constant, donc vraisemblablement hérité de la lignée
   commune (cibles lourdes non versées), non du coffre ; à confirmer de la même façon. HYPOTHÈSE, non vérifiée.
4. Mots de Lazar reçus depuis la note de 06:13 (verbatim) : « (b) (a), plus une attaque publiée reproduite avant l'entretien
   […] go » ; « que faudrait il produire comme resulttas inedits pour l'entretien ? » ; « et plus tard dans le programme ? » ;
   « inedits dans la litterrature je veuix dire » ; « dis moi quand tu as fini de traiter les questions difficiles poiur qu'on
   repasse en opus 5.5 ». Lecture de « (b) go » : accord de principe sur une dépense de calcul, sans montant ; devis et ligne
   d'autorisation restent à écrire (ligne voisine existante : GO-2026-10-31-05, échéance 14 novembre).
