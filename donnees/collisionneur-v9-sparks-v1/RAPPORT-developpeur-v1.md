# Rapport du développeur — kit du collisionneur v9, tour Sparks sans Argon — v1

Développeur neuf de l'instance fusionnée, 4 novembre 2026, 01:37 UTC (`date -u`). Consigne exécutée :
`docs/notes/weight-space-programming-v1/consigne-developpeur-kit-collisionneur-sparks-v1.md`, empreinte ec50e112… vérifiée par
`sha256sum` avant lecture (égale au compagnon). Aucun appel réseau ni payant, aucune clé lue, aucun commit, aucune poussée.
Arbre de travail : `/home/user/wt/collisionneur-sparks` (branche `donnees/collisionneur-v9-sparks-v1`, depuis `main` 43e80cad).

## Fichiers (dossier `donnees/collisionneur-v9-sparks-v1/`, chacun avec son compagnon `.sha256`, tous vérifiés)
| Fichier | sha256 |
|---|---|
| `collisionneur_v9.py` (à l'octet du modèle) | 27e9ce40a64fbcd5cd981f9cc1731b1119829a506f8427857cc850cde91bd1d6 |
| `appel_controle_v12.py` (à l'octet du modèle) | f51ebd29ce2ab29e5f8d98e5aa6db88ea47330042d009e1724b146b1cc114897 |
| `course_a_blanc_sparks_v1.py` | 606a685b309024fa9cf71b08712d1cd1b934e50ae5a3cddac892371a0245519f |
| `assembler_faits_sparks_v1.py` | c4c2a461003613320322bc0ca293a12d6cb9803bb365cdcfed475b565b5b94bc |
| `faits.md` (85 493 octets ; pièces 3, 1, 2) | 65a613a39df55fc74fab033c515c5eff9f917b44e4ca9d9ab90fca580d2b81fa |
| `question.md` (à l'octet de la question) | 69d0536941e75dcefb1e05565bb80abf256026da2418f62d300f725ff19fee35 |
| `balayage-faits.txt` (0 correspondance) | f3b2bbf932c02ecc8e0fe9cc483dccb05eb3789947c1a0a94b46b9d57c36044d |
| `lancer-tour-sparks-v9-sans-argon-v1.sh` | f2b1bfed146570df9e11681196cdabac483a8aa4775678ef0ce37d7ea1e8447c |
| `course-a-blanc-sparks-v1.txt` | 921be9f37924ec1a5d48846e25f15c699c7c4f34d16282f19b2908def466446c |
| `LISEZMOI-sparks-v9-v1.md` | 6cd9380b5f54bfecd791a9d5ae1072ba17ad856f45b0e7624c961e8ac9996e4c |

Kit modèle lu par `git show` (branche `origin/donnees/collisionneur-v9-kirchner-q2-v1`, 16ec2e5a) : 13 fichiers, tous conformes à
leurs compagnons.

## Devis (variante sans Argon : 12 cellules + 4 contrôles)
- Pire cas sans relance : **23,47 USD** (calcul : `devis` étage 3 = 29,92 moins les cellules C, 6,45) ; 22,64 USD sur les prompts
  réels de la course à blanc ; avec une relance par cellule 64,76 USD.
- Attendu : **≈ 10,19 USD** (A 4,64 ; B 2,77 ; D 0,75 ; E 2,03). Contrôle ≤ 0,18 USD.
- Courses à blanc : cinq espèces code 0 (pour mémoire, pire cas 29,70 / devis 29,92 ; attendu 14,93) ; sans Argon code 0 ;
  plafond 5 USD : arrêt code 4 avant l'appel qui l'aurait franchi ; `verifier` : 0 problème partout.

## Plafond proposé
**`PLAFOND_USD=34`** : 1,2 × 23,47 = 28,16 ≤ 34 (calcul). Plafond 34 + contrôle 0,18 ≤ 35 USD de `GO-2026-11-04-02`.
`faits-sans-billet.md` non produit (non requis par l'étape 7).

## Écarts au modèle et à la consigne
1. **Pièces absentes de `main`** : `main` (43e80cad) n'a pas le dossier `docs/notes/weight-space-programming-v1/` ; le billet et « nos
   résultats » sont sur la branche `claude/new-session-7qxayx` (6597e074), la lecture factuelle et la question seulement non suivies
   dans `/home/user/controle-ia-travail`. Pièces et question prises là, empreintes vérifiées (égales aux préfixes de la consigne et
   aux compagnons) ; l'assembleur exige les empreintes, donc la provenance de dossier est sans effet sur `faits.md`.
2. **`donnees/` est ignoré par `.gitignore`** (ligne 10) : la mère devra ajouter le dossier avec `git add -f`.
3. Lanceur : commentaire d'en-tête (lignes 1 à 8) gardé tel quel (mentionne encore Kirchner) ; un remplacement global y nommait deux
   fichiers inexistants. Première version de ce fichier, faite par remplacement global, supprimée et refaite avant tout compagnon.
4. `course_a_blanc_sparks_v1.py` : ligne 1 garde la date du modèle (3 novembre 2026) ; docstring d'`appel_controle_v12.py` parle de
   Kirchner (copie à l'octet).
5. `balayage-faits.txt` : valeurs des clés absentes de cette session, recherche par valeur non faite (motifs seuls).
6. `course-a-blanc-sparks-v1.txt` : ajoute trois lignes « calcul » au devis (sous-total sans Argon, 1,2 ×, cinq espèces pour mémoire) ;
   lignes de journal par appel filtrées comme dans le modèle.
7. Épreuves sans appel du lanceur et de l'assembleur faites (non demandées ; résultats dans le LISEZMOI, pas de fichier d'épreuves
   séparé) ; Python factice : environnement virtuel du bloc-notes avec un module `anthropic` vide.
8. Variante cinq espèces non préparée (Argon occupé) ; son pire cas (29,92) ne tiendrait pas sous 34 (1,2 × = 35,90).
