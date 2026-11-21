# Manifeste du geste 0 de l'étage 2 — v1

Accordé par GO-2026-11-21-04 (2) et par le mot de la mère (R-4348).

- Heure de début (UTC) : Sat Nov 21 06:07:57 UTC 2026
- Heure de fin (UTC) : Sat Nov 21 06:08:10 UTC 2026

## Commande 1 — copie à l'octet sans ouverture

```
git -C /home/user/controle-ia-travail restore --source=8029ae7f9539a950936cef5b2b669285d4efb05a --worktree -- archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json
```

Code de sortie : 0

## Commande 2 — vérification de l'empreinte

```
env -C /home/user/controle-ia-travail sha256sum -c --quiet /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/geste-0-etage-2/attente-fiches-v1.sha256
```

Code de sortie : 0

Sortie : (vide)

## Références

- Commit source : 8029ae7f9539a950936cef5b2b669285d4efb05a
- Empreinte attendue (SHA-256) : ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481
- Chemin : archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json

Fichier ni ouvert, ni ajouté, ni commité.
