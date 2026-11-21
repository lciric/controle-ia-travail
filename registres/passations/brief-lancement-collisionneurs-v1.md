# Brief de lancement autonome, session neuve qui reprend les collisionneurs sur les clés Minuit et OpenAI 2 (v1, 2026-11-21)

Tu es une session fille de la session mère du programme de Lazar, dépôt `lciric/controle-ia-travail`. Lis d'abord `CLAUDE.md` sur main. Écris en français. Ce brief est ton mandat. L'état vivant est dans la dernière passation de ce rôle : `registres/passations/2026-11-21-1448-collisionneurs-cle-openai-2.md`, sur la branche `runs/collisionneurs-reprise-minuit-v1`. Lis aussi les comptes rendus de `registres/essaim/vers-mere/` sur cette branche, et ce que la mère y a écrit depuis.

## Clés, par leur NOM seulement (jamais affichées, écrites ni copiées)
- Présence : `env | grep -o '^RR_ANTHROPIC_API_KEY_MINUIT\|^OPENAI_API_KEY_2\|^GEMINI_API_KEY'`. Si une clé manque, arrête-toi et écris-le à la mère.
- Anthropic : `--cle-anthropic RR_ANTHROPIC_API_KEY_MINUIT`.
- OpenAI : le script lit le nom fixe `OPENAI_API_KEY`, dont le compte n'a plus de crédit. Préfixe chaque lancement par `OPENAI_API_KEY="$OPENAI_API_KEY_2"`, dans l'environnement du seul processus.
- Google : `GEMINI_API_KEY`, lue par le script.

## Préparation
1. Tu es dans `/home/user/controle-ia-travail`, sur main à jour. Si `.venv` manque : `python3 -m venv .venv && . .venv/bin/activate && pip install -q -r requirements-cpu.txt`.
2. Script : `docs/notes/collisionneur-v9/collisionneur_v9_v3.py`. Vérifie-le : `(cd docs/notes/collisionneur-v9 && sha256sum -c collisionneur_v9_v3.py.sha256)`, attendu 850df311….
3. Vérifie chaque fichier de faits et de question contre son compagnon `.sha256` avant tout lancement.
4. Worktree de versement :
   ```
   git fetch origin runs/collisionneurs-reprise-minuit-v1
   git worktree add ../wt-reprise-minuit FETCH_HEAD
   cd ../wt-reprise-minuit
   git checkout -B runs/collisionneurs-reprise-minuit-v1
   ```
   Pour reprendre un dossier, copie-le de ce worktree vers `runs/` du dépôt principal.

## Lancer, ou relancer sur un dossier existant (une course détachée)
- Une relance de `etage3` sur le même dossier saute les cellules valides et refait les autres. `--reprise` ne sert qu'en cas de changement de script. La composition est scellée dans `<dossier>/especes.json` : garde exactement ces espèces. N'ajoute jamais Astra à un dossier qui ne l'a pas. La ligne reste celle qui est ouverte dans `journal.jsonl` (`ligne_ouverte`) : le script refuse d'en changer, et ce refus ne se contourne pas.
- Commande type, variables posées avant, sur plusieurs lignes :
  ```
  cd /home/user/controle-ia-travail
  D=runs/<dossier>
  F=<chemin des faits>
  Q=<chemin de la question>
  S=docs/notes/collisionneur-v9/collisionneur_v9_v3.py
  GO_ID=<GO de la course> OPENAI_API_KEY="$OPENAI_API_KEY_2" PYTHONPATH=src setsid nohup .venv/bin/python "$S" etage3 \
    --fable --opus --argon --astra --carbon \
    --cle-anthropic RR_ANTHROPIC_API_KEY_MINUIT --accepter-absence kimi \
    --sortie "$D" --plafond-usd 28 --ligne-usd 28 \
    --faits "$F" --question "$Q" > "$D/journal-relance-<HHMM>.txt" 2>&1 < /dev/null &
  ```
  Retire `--astra` si `especes.json` ne l'a pas.
- Identifiant réel du processus : la valeur de `$!` est celle d'un intermédiaire. Parcours `/proc/[0-9]*/cmdline` à la recherche de `.venv/bin/python` et du nom du dossier. Écris l'identifiant dans `<dossier>/pid.txt`.
- Devis avant tout lancement neuf : sous-commande `devis` (mêmes espèces, `--faits`, `--question`). Avant une reprise par `--reprise` : `devis-reprise <dossier> --ligne-usd <ligne>`. Le script refuse un pire cas au-delà du plafond : ne lance pas, écris-le à la mère.
- Deux courses à la fois au plus. Ne coupe jamais une course en marche.

## Courses et GO (relis-les dans `registres/go.md` sur main)
- Mécanisme adjudant, GO-2026-11-21-34, ligne 28 USD. Dossier `runs/collisionneur-mecanisme-adjudant-v1-20261121-114751`, avec Astra. Faits et question : `docs/notes/mecanisme-adjudant-hors-distribution-v1/collisionneur-v1/faits-mecanisme-adjudant-v1.md` et `question-mecanisme-adjudant-v1.md`.
- Percée en contrôle et sécurité, GO-2026-11-21-39, ligne 28 USD. Dossier `runs/collisionneur-percee-controle-securite-v1-20261121-114810`, avec Astra. Faits et question : `docs/notes/percee-controle-securite-v1/collisionneur-v1/faits-percee-controle-securite-v1.md` et `question-percee-controle-securite-v1.md`.
- Antériorité du pilier, GO-2026-11-21-39, ligne 28 USD. Dossier le plus avancé : `runs/collisionneur-anteriorite-pilier-v1-20261121-131029`, avec Astra ; seule y manque la réponse de Carbon au tour III.3. Faits et question : `docs/notes/mathematiques-nouvelles-v1/collisionneur-anteriorite-v1/faits-anteriorite-pilier-v1.md` et `question-anteriorite-pilier-v1.md`. Le dossier `…-130555` (sans Astra) est un doublon, à ne pas relancer.
- Dérive de régime v2, GO-2026-11-21-26, ligne 28 USD (3,04 USD déjà comptés avant). Dossier `runs/collisionneur-derive-de-regime-v2-20261121-131044`, arrêté par la garde de dépense (code 6). Ne le relance que sur le mot de la mère. Faits et question : `docs/notes/papier-dopamine-moniteur-v1/collisionneur-derive-de-regime-v1/faits-derive-de-regime-v1.md` et `question-derive-de-regime-v1.md`.
- Méthodes de mathématiques nouvelles, GO-2026-11-21-23 (ligne de 40 USD, 7,91 déjà comptés). Dossier `runs/collisionneur-methodes-maths-v1-20261121-093850`, ligne ouverte à 28 USD dans le script : la reprise à 30 est refusée. Attends le mot de la mère. Faits et question : `docs/notes/mathematiques-nouvelles-v1/brainstorm-methodes-v1/faits-methodes-mathematiques-nouvelles-v1.md` et `question-methodes-mathematiques-nouvelles-v1.md`.
- Deux questions fusionnées, GO-2026-11-21-52, 28 USD chacune, sans Astra. Faits et questions sous `docs/notes/problematique-programme-v1/collisionneur-v1/` : `faits-but-et-questions-brulantes-v1.md` avec `question-but-et-questions-brulantes-v1.md` ; `faits-question-de-recherche-fusionnee-v1.md` avec `question-question-de-recherche-fusionnee-v1.md`. Dossiers neufs `runs/collisionneur-but-et-questions-brulantes-v1-<AAAAMMJJ-HHMMSS>` et `runs/collisionneur-question-de-recherche-fusionnee-v1-<date>`. Espèces `--fable --opus --argon --carbon --accepter-absence kimi --accepter-absence astra`. Vérifie d'abord la forme exacte par `etage3 --help`.

## Versement et compte rendu
- Après chaque tour et à la fin de chaque course, verse le dossier sans le lire. Copie-le dans le worktree, puis `git add -f <dossier>`, commit, `git fetch` et `git rebase` sur la branche distante, et `git push origin runs/collisionneurs-reprise-minuit-v1` (quatre essais avec attente croissante).
- Compte rendu dans `registres/essaim/vers-mere/AAAA-MM-JJ-HHMM-<objet>.md` sur la même branche : la course, le code de sortie, le cumul du journal, les cellules rendues (par leur nom de fichier), le commit du versement. Essaie aussi `send_message` vers la session mère indiquée par Lazar ; s'il est refusé, le fichier suffit.
- Passation scellée dans `registres/passations/` à la fin de la session.

## Interdits
- Aucun fichier « consigne-privee » ni « conception-ii-b ». Rien sous `archives-reponses-modeles/`, `docs/notes/bras-attaque/`, `brouillons/ii-b-saboteur-budget-v1/`. Aucune des branches `quarantaine/…`, `matiere-premiere/…`, `verite-temoins/…`, `lot/compte-4-v1`.
- Ne lis jamais le contenu des cellules ni des essais. Aucun résultat d'expérience.
- Aucune dépense hors de ces GO et lignes. Aucun recours à la carte.
- Aucune commande `rm` sur un chemin construit par variable. Aucun nom de commande d'arrêt ou de recherche de processus dans une commande : arrêt par identifiant seulement. Heures par `date -u`.
- Ne contourne jamais un refus d'outil, de classifieur, de garde ou du script : au premier refus, arrête-toi et écris-le à la mère.
- Ne pousse jamais sur main.
