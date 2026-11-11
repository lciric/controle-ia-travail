# Index du bras d'étude des déplacements de loi (bras d'attaque) — v5

Tenu par la session-dépôt (gardien ; nouvelle instance `session_013QMaymMAdDjNfPoz8ySwTc`). **Aucun contenu** : existence,
chemin, empreinte et intégrité seulement. Les v1 à v4 restent telles quelles (R12) ; la v5 reprend la v4 par renvoi et ajoute
le relevé du 10 novembre, 11:39 UTC (`date -u`).

## BA-002 — session « attaquant informé », relevé v5

- **Branche** : `claude/compassionate-meitner-d4ryyk`, tête `0ad143cc` (récupérée par refspec explicite) ; base `483712e7`
  (même base que la v3 et la v4).
- **Méthode** (identique à la v4) : fichiers `.sha256` ajoutés ou modifiés entre la base et la tête ; pour chacun, empreinte
  du compagnon comparée à l'empreinte recalculée de la cible à la tête, par `git show | sha256sum`, sans affichage du contenu.
- **Pièces scellées** : 163, toutes conformes. Les 159 pièces de la v4 sont présentes avec la même empreinte (aucun écart).
  Liste : `registres/index-bras-attaque-v5-pieces-session-attaquant.txt`.
- **Quatre pièces nouvelles depuis la v4** (nature déclarée par leur nom ou le titre de leur commit, non lues) :
  - `docs/procedures/brief-successeur-attaquant-informe-v1.md` (brief de passation au successeur, commit `0ad143cc`) ;
  - `registres/passations/2026-11-10-1112-attaquant-informe-passation-quota.md` (passation, commit `cab02e41`) ;
  - `registres/passations/2026-11-10-1118-decision-lazar-go-autonome-bailey.md` (commit `8c540a44`, titre : « Décision de
    Lazar : go autonome Bailey, auteurs d'accord ; conditions restantes pour la prochaine instance ») ;
  - `docs/sources/pdf/anteriorite-bras-informe-v1/alotaibi-2026-defenses-empilees-correlation-echecs-2608.28327v1.pdf`
    (source versée, commit `cab02e41`).
- **Successeur de la session** : « Passation attaquant informé », `session_013QMaykGXY4fZmZNX5fm1K4` (nouveau compte), créée à
  11:24:46 UTC. L'ancienne session `session_01QPDgKjN3jeeUyZP2mnkDNK` n'est plus visible depuis ce compte.
- **Ce que le gardien n'a pas fait** : lire un contenu ; juger un résultat ; ouvrir la passation ni le brief du bras.

## Réserve du gardien

La vérification de l'arbre (routine R14) a haché, à 11:26 UTC environ, les fichiers de `docs/notes/bras-attaque/` présents
dans la copie de travail de cette instance. Aucun contenu affiché. Le dossier a été retiré de la copie de travail (extraction
partielle) ; il n'y revient que pour un relevé d'intégrité.
