VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — préenregistrement du palier 0b, version 9 (erratum après le code v4, GO-2026-11-20-25) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-25 et les décisions de la mère R-4123, R-4135 et R-4150. Dossier : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/` (noté P).

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit aucune version du préenregistrement ni le code. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- La v8 : `P/preenregistrement-heritage-palier-0b-etage-processeur-v8.md` (`fd275af81704997f2844e4ee9fdb68c5401658335221ea0768f70e3cdac9586c`), son contrôle `P/controle-differentiel-palier-0b-v8-v1.md` (`a68a46a0…`, « tenue seulement » T1 à T9) et le rapport du rédacteur de la v8.
- Le code v4 : `P/code-v4/rapport-developpeur-code-palier-0b-v4.md` (`2947c4f15729265475fe162d983249b3d98c1c0eccb0a61f94606ba540f2b005`) : § 2 (les 13 silences) et ses trois constats.
- La vérification du code v4 : `P/verification-code-palier-0b-v4-v1.md` (`183b17d2d28b743e81eedb0c38415ecd273879439bec9a03a52319328397cc5f`), « Conforme » : ses points 1 et 2, son point 5 (silences à l'erratum : n° 1, 2, 3, 4, 5, 8, 9, 10, 13 ; sans suite : 6, 7, 11, 12) et ses trois constats.
- Sur main (`fetch`, puis `git show` redirigé vers ton dossier) : `registres/go.md`, ligne GO-2026-11-20-25 ; `registres/decisions.md`, lignes R-4123, R-4135, R-4150. Cite-les à la lettre.

## Ce que tu fais

Une v9 sous le nom neuf `preenregistrement-heritage-palier-0b-etage-processeur-v9.md`, par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, empreinte commençant par `391db990`), un JSON écrit avec l'outil d'écriture de fichiers ; vérifie chaque ancre par `grep -c -F -e` avant l'appel (règle R-4067). Elle porte, et rien d'autre :

1. **GO-2026-11-20-25, point (1)** : dans la règle de lecture des trois audits par dose, le seuil d'arrêt « 0,55 + 2σ₀ » devient « moyenne permutée + 2σ₀ » (la moyenne permutée et σ₀ de chaque audit, calculées par les mêmes 1 000 permutations ; la tenue « au plus 0,55 » et la zone « non départagée » sont à réécrire en cohérence, sans rien inventer : si la lettre du GO ne fixe pas la borne basse, écris l'ambiguïté en remarque et propose, sans trancher).
2. **GO-2026-11-20-25, point (2)** : la règle calibrée s'étend au contenu et aux réunis des audits par dose, **pour le signalement seulement, jamais pour un arrêt**.
3. **R-4123, le verrou D6** : la pièce d'autorisation est une pièce scellée, écrite par la mère après le GO de Lazar sur le palier, à `prereg/organisme-auto-conception-v9/palier-0b/autorisation-verrou-palier-0b-v1.md` sur main, portant l'identifiant du GO, le commit du code, l'empreinte du texte scellé et l'heure (`date -u`) ; le verrou exige qu'elle existe à ce chemin, qu'elle soit scellée et que son contenu égale les valeurs attendues. Le code v5 suivra.
4. **Le 0,63 sur graines d'essai** (R-4123 point 3 de la mère) : un constat de l'essai, non une mesure du palier ; aucun seuil ne change.
5. **Les silences** : précisions pour les n° 1, 2, 4, 5, 8, 9, 10 et 13 ; le n° 3 (la graine des plis de la lecture observée : un rôle d'étiquette `SeedSequence` dérivé avant lancement, R9) ; le n° 8 (qui appelle `etape_4_jeu_de_la_garde_27`, avec quel proposeur et combien de sources ; si le texte ne le dit pas, proposition en remarque). Ne touche pas aux n° 6, 7, 11 et 12.
6. **Le constat 3** de la vérification, comme information, sans lecture de critère.
7. **Tenue T1 à T9** du contrôle de la v8, si elles ne sont pas déjà portées ; titre, ligne de version, statut.

Puis le différentiel `diff -u` v8 → v9 et un rapport court `rapport-redacteur-palier-0b-v9-v1.md` : remplacements, ancres comptées, tout point où la lettre des décisions ne suffit pas (écrit en remarque, jamais tranché), et ce que le code v5 devra changer (liste).

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-palier-0b-v9/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement du code, aucun tirage. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
