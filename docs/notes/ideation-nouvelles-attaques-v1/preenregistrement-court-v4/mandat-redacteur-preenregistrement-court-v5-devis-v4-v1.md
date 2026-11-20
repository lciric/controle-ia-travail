VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — course « nouvelles attaques » : préenregistrement court v5 et devis v4 (corrections de la contre-lecture) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-33. La contre-lecture du préenregistrement court v4 et du devis v3 a rendu « À corriger » : neuf corrections de lettre (K1 à K9), aucune sur un total, un seuil, un arrêt ou une décision. Ensuite : vérification des corrections par le même contre-lecteur, scellement par la mère ; le devis va à Lazar, rien ne court avant son mot.

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit aucune version du préenregistrement court, du devis, ni leurs contre-lectures. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

Dossier V = `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v4/`.
- `V/preenregistrement-court-course-nouvelles-attaques-v4.md` (`2dabdadf9ac126ee8d931dfde3e3507a3183b50b8f584d0f817e7ebf8adf2b10`) et `V/devis-course-nouvelles-attaques-v3.md` (`bf7b4ba3ede3ba73c8ee4e1a3548b6b0d52975df717b98ca4af44a6c503c142a`).
- `V/contre-lecture-v1/contre-lecture-preenregistrement-court-v4-devis-v3-v1.md` (`539c4854ad36e5d9b615c43bb2f7b7359c27661abc6f2a0abc6195812c1e150f`), en entier : corrections K1 à K9, texte de la section « Contre-lecture 4 » (§ 8).
- Les deux jeux de corrections du contre-lecteur, déjà essayés par lui sur des copies : `V/contre-lecture-v1/corrections-preenregistrement-court-v4-v1.json` (`14b429fe…`) et `V/contre-lecture-v1/corrections-devis-v3-v1.json` (`11977cde…`).
- L'outil `/home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py` (`391db990…`).

## Ce que tu écris

1. `preenregistrement-court-course-nouvelles-attaques-v5.md` et `devis-course-nouvelles-attaques-v4.md` (noms neufs), à partir de la v4 et du devis v3, par l'outil contre-lu, avec des JSON écrits par toi avec l'outil d'écriture de fichiers (tu peux reprendre mot pour mot les textes des deux jeux du contre-lecteur, après les avoir comparés à sa pièce), chaque ancre comptée par `grep -c -F -e` avant l'appel (R-4067). Ils portent, et rien d'autre : K1 à K9, « Ancien » et « Neuf » mot pour mot de la contre-lecture ; le texte de la section « Contre-lecture 4 » (§ 8 de la contre-lecture), l'empreinte et le traitement laissés à écrire par la mère comme la pièce le dit ; la tenue (titre, statut, phrase de version).
2. **Ce qui reste à Lazar ne se tranche pas** : le plafond (570 ou 450 USD) et le plafond de la sonde de l'espèce 6 (0,01 ou une autre valeur, K9) restent écrits comme options.
3. Les JSON, les journaux de l'outil, les différentiels `diff -u` (v4 → v5, devis v3 → v4), la sortie du validateur sur la v5 (par le programme `V/valider_prereg_v4_v1.py`, lu d'abord, lancé par son chemin, ou par une copie renommée pour la v5), et un rapport court `rapport-redacteur-preenregistrement-court-v5-devis-v4-v1.md`.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-preenregistrement-court-v5/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Aucune méthode d'attaque, aucun procédé, aucun détail opérant ; aucune recette.** Aucune valeur de clé. Aucun lancement du relais, du véhicule ni de la sonde. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien du coffre, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
