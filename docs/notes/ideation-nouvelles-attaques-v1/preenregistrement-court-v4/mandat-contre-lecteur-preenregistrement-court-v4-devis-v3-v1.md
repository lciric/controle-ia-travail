VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contre-lecteur — course « nouvelles attaques » à six espèces : préenregistrement court v4 et devis v3 — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-33, règle R2. Les deux textes ont été écrits par un rédacteur neuf, modèle F. Pièces décisives (classe A) : contre-lecture par un autre modèle, vérification des corrections par le même, scellement par la mère ; **le devis va à Lazar, rien ne court avant son mot.**

## Qui

Un contre-lecteur neuf, modèle O, qui n'a écrit aucune version du préenregistrement court, du devis, de l'ordre de course, ni leurs contrôles. Tu signes « contre-lecteur neuf, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

Dossier N = `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/`.
- `N/preenregistrement-court-v4/mandat-redacteur-preenregistrement-court-v4-devis-v3-v1.md` : ce qui était demandé.
- `N/preenregistrement-court-v4/` : `preenregistrement-court-course-nouvelles-attaques-v4.md` (`2dabdadf9ac126ee8d931dfde3e3507a3183b50b8f584d0f817e7ebf8adf2b10`), `devis-course-nouvelles-attaques-v3.md` (`bf7b4ba3ede3ba73c8ee4e1a3548b6b0d52975df717b98ca4af44a6c503c142a`), les deux JSON de remplacements, leurs journaux, les deux différentiels, `calcul_devis_course_nouvelles_attaques_v3.py` (`a50c9983…`) et sa sortie (`fa4bc8b0…`), `valider_prereg_v4_v1.py`, `rapport-redacteur-preenregistrement-court-v4-devis-v3-v1.md` (`36b8d1e2…`).
- Les versions précédentes : `N/preenregistrement-court-v3/preenregistrement-court-course-nouvelles-attaques-v3.md` (`2ea5ad53…`) et son contrôle ; le devis v2 dans `N/conception-v2/` (`714e4fc6…`) et son programme de calcul s'il y en a un.
- L'outil `/home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py` (`391db990…`).
- Sur main (`git -C /home/user/controle-ia-travail fetch origin main`, puis `git … show FETCH_HEAD:CHEMIN > FICHIER_DANS_TON_DOSSIER`) : `registres/go.md`, lignes GO-2026-11-20-10, -16, -20, -22, -31, -32, -33, -34 ; `registres/decisions.md`, R-813, R-1780, R-4117, R-4125, R-4169, R-4170.

## Ce que tu fais

1. **Rejeu** des deux passages de l'outil (v3 → v4, devis v2 → v3), `cmp` avec les pièces rendues ; différentiels refaits.
2. **Fidélité à GO-33** : six espèces, la sixième désignée par son numéro seulement, proposeur seul ; rien d'autre ne change que ce que le nombre d'espèces entraîne ; chaque critère dit « inchangé » l'est vraiment.
3. **Le devis** : refais **indépendamment** les totaux qui décident (attendu, cas haut, pire, par espèce et par clé ; ligne de 570 USD ; plafond total 576,01 ; variante à 450 ; rapport de la borne 415,21 au cas haut) par un programme à toi, écrit avec l'outil d'écriture de fichiers et lancé par son chemin ; rejoue le programme du rédacteur ; juge les trois règles de coût de l'espèce 6 et la valeur de 6,05 USD de pire par appel ; relis le tarif du registre (R-813, R-1780) et dis s'il change un total.
4. **GO-22 et GO-34** : la répartition sur les clés Minuit, Luc et Rigaud, et la lecture « solde relu après recharge » ; la clé la plus serrée.
5. **La sonde de refus de l'espèce 6** : ce qu'elle mesure, son plafond, son arrêt, la question de la taille de la requête (remarque 6 du rapport) ; **aucun contenu d'attaque, aucune recette, aucune invite opérante** n'y figure.
6. **Les neuf remarques du rapport** : pour chacune, à corriger, à porter à Lazar, à la mère, ou sans suite, avec ta recommandation et sa confiance.
7. **Le validateur** : la v4 n'a qu'un problème attendu (section « Contre-lecture » à remplir) ; confirme-le par le programme du rédacteur, lu d'abord.
8. **Verdict** : « Conforme, à sceller » ou « À corriger », avec pour chaque correction l'« Ancien » et le « Neuf » exacts (ancre unique comptée par `grep -c -F -e`), et le texte à porter à la section « Contre-lecture 4 ».

Écris `contre-lecture-preenregistrement-court-v4-devis-v3-v1.md` dans ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-nouvelles-attaques-v4/`, avec ton programme, sa sortie et leurs compagnons (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Aucune méthode d'attaque, aucun procédé, aucun détail opérant ; aucune recette.** Aucune valeur de clé (présence par le nom seulement). Aucun lancement du relais, du véhicule ni de la sonde. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien du coffre, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
