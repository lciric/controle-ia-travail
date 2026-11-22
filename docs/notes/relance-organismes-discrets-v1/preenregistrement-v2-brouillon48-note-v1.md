# Note du brouillon 48 du texte neuf du bras A des organismes discrets — v1

- **Correcteur** : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf, délégué par la session de relance. Règle suivie (décision de Lazar, GO-2026-11-21-84) : j'écris seulement les corrections, mot pour mot d'après les remarques déjà reçues ; je ne conçois rien.
- **Date** : 2026-11-22. Branche `claude/pensive-bardeen-1fv7hw`. Aucun réseau, aucune clé, aucune dépense, aucun commit.
- **Décision portée** : mots du directeur, ligne GO-2026-11-22-73 du registre des GO (lue sur la branche principale, cette seule ligne) : « bras A M-6 (A) go, M-7 (A) go ».
- **Base** : brouillon 47, `prereg/T0.7-organismes-discrets-v-a-v2-brouillon47.md`, `f59f6b4ed2b1198c3781badf83692d593ed4ade0df5baa9f0e4ea8b1827a6cb9` (recalculée), 2 546 lignes.
- **Remarques portées** : M-6 et M-7, option A, de la contre-lecture 10, `docs/notes/relance-organismes-discrets-v1/contre-lecture-10-brouillon46-bras-a-v1.md`, `f711c9be09b8912adcb82d469a09f03e89b80ac67950cc2235e4d2cfebda1881` (recalculée), lignes 40 (M-6) et 42 à 44 (M-7).
- **Sortie** : brouillon 48, `prereg/T0.7-organismes-discrets-v-a-v2-brouillon48.md`, `838654d6faf4442286dac83046832729a292c3e2388f5b0844f20785f39dc2c3`, 2 546 lignes (aucune ligne ajoutée ni retirée).
- **Fichier des règles neuf** : `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/regles-admission-bras-a-v1-brouillon48.md`, `fb52271551507dc040122bdf8c2a5d414befb72405112df7e9894ab339978ba0`, fait sur le modèle exact de celui du 47 (`4ae13530…`, contrôlé) : seules changent la mention « définitif sur le brouillon 48 », l'empreinte et le chemin du texte en vigueur ; les huit règles y sont égales aux lignes 542 à 550 du 48, vérifié par programme.

## 1. Comment le brouillon 48 est fait

Par un programme, `docs/notes/relance-organismes-discrets-v1/brouillon48-corrections-v1/appliquer_corrections_brouillon48_v1.py` (`c7e5be564d781d557458f726a66626e17ec11460823489d90338393ccfc3f911`), lancé par `python3 -I … /home/user/controle-ia-travail`, sur le modèle du programme du brouillon 47 : empreintes des entrées contrôlées ; textes de M-6 et M-7 lus dans le fichier de la contre-lecture, bornes de chaque extrait contrôlées ; six remplacements exacts, chacun d'un ancien trouvé une seule fois, sinon arrêt ; arrêt si le nombre de lignes change, si les lignes 542 à 550 diffèrent (et contrôle de leur empreinte, `3d1f0afe…`), ou si une ligne avant 542 autre que 1 et 3 change. Le même programme écrit le fichier des règles.

## 2. Chaque changement (ligne du 47 → ligne du 48, mêmes numéros)

| ligne | correction | avant (47) | après (48) |
|---|---|---|---|
| 1 | histoire | « — v2, BROUILLON 47 » | « — v2, BROUILLON 48 » |
| 3 | histoire | « **Statut : brouillon 47, non exécutable.** Le brouillon 47, … » | « **Statut : brouillon 48, non exécutable.** Le brouillon 48 porte M-6 et M-7 de la contre-lecture 10, option A, mots du directeur (GO-2026-11-22-73 : « bras A M-6 (A) go, M-7 (A) go »), mot pour mot, aux textes proposés par la contre-lecture ; rien d'autre ne change. **État au brouillon 47** : Le brouillon 47, … » (le reste de la ligne inchangé) |
| 587 | M-7, énoncé de l'hypothèse de désappariement | « … `Δτ(·, p)`, est strictement positive. La dose ¼ … » | « … `Δτ(·, p)`, est strictement positive ; elle n'est dite **confirmée** qu'au-delà de l'effet minimal d'intérêt (moyenne d'au moins 0,10, section « Seuil »), et **réfutée au sens de cette mesure** quand une hausse d'au moins 0,10 est exclue aux trois doses, même si une hausse plus petite est établie. La dose ¼ … » |
| 1034 | M-7, ligne B9 | « … (6.9 ; GO-2026-11-19-24, point 2) \| » | « … (6.9 ; GO-2026-11-19-24, point 2) ; si le test de la hausse contre l'honnête rejette aussi à cette dose, écrire de plus : « hausse positive établie, sous l'effet minimal d'intérêt » \| » |
| 1062 | M-6, 7.6, déclencheurs | « … contre-lecture, R-4) ; **côté nul** : … » | « … contre-lecture, R-4) ; **au moins une dose en C4** (pendant du déclencheur C6 : la réfutation de la discrétion est l'issue opposée, et l'audit coûte aussi peu) ; contenu : le même, côté habilité compris ; anomalie : ligne A11 ; **côté nul** : … » |
| 2543 | histoire, section « Contre-lecture » | « … M-3, M-6 et M-7 en attente (statut). » | « … au brouillon 48, M-6 et M-7, option A (GO-2026-11-22-73), mot pour mot ; M-3 en attente (statut). » |

**Lignes changées : 1, 3, 587, 1034, 1062, 2543.** Le lecteur habilité ne relit qu'elles.

## 3. Diff contrôlé contre le 47

`diff` du 47 au 48 : six blocs `c` d'une ligne chacun (1c1, 3c3, 587c587, 1034c1034, 1062c1062, 2543c2543), aucun ajout ni retrait. Par ligne, les écarts (comparaison caractère par caractère) sont seulement les insertions du tableau ci-dessus et, aux lignes 1 et 3, « 47 » → « 48 ». Les huit règles d'admission (lignes 542 à 550) sont égales caractère pour caractère, aux mêmes numéros ; aucune ligne n'est ajoutée avant elles ; vérifié par programme.

## 4. Textes du correcteur, déclarés (non tirés de la contre-lecture)

- Ligne 3 : la phrase d'histoire et l'intitulé « **État au brouillon 47** : », qui garde la suite de la ligne comme état du 47 (dont « M-3, M-6 et M-7 ne sont pas portés », vrai au 47), sur le modèle du 47.
- Ligne 2543 : le mandat dit « 47 » → « 48 » dans « Contre-lecture » ; le seul « brouillon 47 » de cette ligne nomme le traitement fait au 47 (M-1, M-2, M-4, M-5 et les mineurs), qui resterait faux s'il était changé en 48. J'ai donc gardé « au brouillon 47 » et remplacé « M-3, M-6 et M-7 en attente » par le traitement du 48. Non mot pour mot : à confirmer.
- Ligne 1062 : le texte de M-6 est inséré entre deux points-virgules, comme les autres déclencheurs ; le texte proposé lui-même est porté sans changement.
