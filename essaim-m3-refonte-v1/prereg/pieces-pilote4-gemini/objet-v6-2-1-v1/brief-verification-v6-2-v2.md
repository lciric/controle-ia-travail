Tu es sous-agent de vérification neuf, pour la lignée conv-audit d'un programme de recherche en sécurité de l'intelligence artificielle. Langue : français, sans acronyme non développé. Tu as environ 35 minutes.

## Objet
Gemini (Argon) a poussé une **v6.2** de son organisme sur la branche `canal/gemini-organisme-v6-2` du dépôt (commit `fedb06525610c05945f8496c2058c21a15256fca`, un seul commit sur la v6.1 `a9d8eb5`, poussé le 25 octobre 2026 à 21:35 UTC ; il ne change que six fichiers de `organisme/`), en réponse à la demande `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/demande-gemini-v6-2-correction-v2.md` (`f15511873e467203d771ee2f1c8282c3e832897ccd55cff0304d171a1837958e` : treize points à lever, § 2, chacun avec un essai, § 3 ; la v2 ne change de la v1 que son § 0). Aucune livraison écrite (rapport de Gemini) n’est fournie à l’heure de cette demande : seul le message du commit (« v6.2 levee integrale des 13 points de verification v6.1 (Savage 1er ordre, ancrages exacts, cout AST borne, validation hors pli des sondes, CONCEPTION.md propre) ») ; dis-le, et juge sur le code et les essais. Vérifie-la **comme la v6.1 l'a été** : rapport de référence `/var/tmp/verification-v61-poussee-v1/LISEZMOI-v1.md` (§ 1 Provenance, § 2 Méthode : copies à part passées à `nobody`, `unshare -n sudo -u nobody env -i … /opt/venv-essaim-sim-v1/bin/python -P -s -B`, jamais `-I` pour les exécutions isolées ; analyses statiques par `python -I` ; contrôles de l'isolation) et ses outils `/var/tmp/verification-v61-poussee-v1/outils-v1/` (lis-les avant de t'en servir ; vérifie leurs empreintes contre `EMPREINTES-v1.txt` du même dossier).

## Extraction
Seul le dossier `organisme/` du commit est extrait, dans un dossier neuf : `git -C /home/claude/canal-conv-audit-n04 archive fedb06525610c05945f8496c2058c21a15256fca organisme | tar -x -C <dossier neuf>` (c'est la seule commande git permise ; le commit porte aussi l'arbre de la relève : n'en extrais rien d'autre, n'exécute rien d'autre, ne l'emprunte jamais comme arbre de travail). Empreinte d'arbre par la transcription `empreinte_arbre_v1.py` ; nombre de fichiers ; diff fichier par fichier contre la v6.1 (`a9d8eb5`, extraite de même).

## Ce que tu établis
1. Provenance (commit, arbre, fichiers), ce qui change par rapport à la v6.1, et si la livraison le dit exactement.
2. Les essais de Gemini passent en isolation (nombre, temps) ; les 45 de la v6.1 sont présents et non affaiblis (compare aux fichiers de la v6.1).
3. **Les treize points de la demande**, un par un : levé, partiellement, non levé — avec les lignes et l'essai qui le montre (un « levé » sans essai est dit tel).
4. V6-01 reste corrigé (successeur muté importé et tournant dans un processus neuf ; noms non liés) ; invariance sous les graines de hachage 0, 1 et 2 (cas B et D), verrous imbriqués, gardes C-01 à C-13, contrat du noyau.
5. **Sous la configuration du pilote 4** (lu dans le code, sans exécution hors des essais) : jusqu'à 6 rondes de conception à 3 USD au plus chacune, puis 4 générations notées, aucune trace servie (`--entrainements-max 0`) : la mutation est-elle tentée à chaque ronde ; critère de fin de conception (lignes) ; appels attendus par ronde et par génération par rapport à la v6.1.
6. **Lignes que le préenregistrement du pilote 4 cite pour la v6.1**, retrouvées dans la v6.2 (lignes nouvelles, et si le
   comportement cité change) : `principal.py` de `a9d8eb5` l. 1985–1990 (fin de conception : `r_idx = int(ronde_conception
   or 1)`, 0,78 avec au moins deux exemplaires, 0,65 à partir de la deuxième ronde, dernière ronde permise), l. 926–933
   (mutation : `phase == "conception" or forcer_mutation or (generation >= 1 and stagnation)`, stagnation
   `scores[-1] - scores[-2] <= 0.01`, scores vides écartés), l. 1927 puis 1950 (mise à jour de la mémoire dans le bloc
   `finally`), l. 740 (exemple de format), l. 86–95 (dix requêtes de réserve) ; `memoire_isvd.py` l. 236–244 (six
   dernières entrées, celle du même numéro retirée), l. 114–117 (score de g0 à g001), l. 125–127 (meilleur ancêtre) ;
   `mitose_spectrale.py` l. 75 et 117 (stagnation). Dis aussi le nombre d'appels d'une ronde de conception et d'une
   génération en simulation (v6.1 : 7 appels en c001, dont un de mutation ; 124 en g003, dont un de mutation), si tu le
   lis dans les essais de Gemini.

## Règles strictes
- Pas d'autre commande git que l'extraction ci-dessus, pas de réseau, pas de sous-agents. N'ouvre jamais un fichier nommé `P3-consignes-v1.md`, un fichier dont le nom commence par `textes-actions-`, ni un dossier `donnees/`, `runs/` ou `diag/`. N'écris que sous `/var/tmp/verification-v62-poussee-v1/`.
- Aucune valeur de clé : si tu en rencontres une, ne la recopie pas.

## Rapport
`/var/tmp/verification-v62-poussee-v1/LISEZMOI-v1.md` (+ `.sha256`), `EMPREINTES-v1.txt` (+ `.sha256`) et un zip versionné `livrable-verification-v62-poussee-v1.zip` (+ `.sha256`) sans les copies d'essai. En tête, l'heure de début et celle d'écriture, **lues sur `date -u` au moment où tu les écris (n'écris jamais une heure de fin d'avance)**. Verdict d'abord (défaut bloquant ou non), puis les points 1 à 6. Réponse rendue : le verdict, l'empreinte d'arbre, le tableau des treize points, les empreintes.
