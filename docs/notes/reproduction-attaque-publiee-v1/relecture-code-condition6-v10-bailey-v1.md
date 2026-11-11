# Relecture R2, en différentiel, du code v10 de la condition 6 — témoin de Bailey — arrêt autonome de l'instance — v1

- Date : Wed Nov 11 13:08 UTC 2026 (`date -u`). Relecteur : sous-agent neuf (R2), qui n'a écrit aucune des pièces lues.
- Je reçois d'office le `CLAUDE.md` du dépôt (consignes permanentes), injecté dans mon contexte.
- Dépôt `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, commit `859fc2d3`.
- Non scellé (scellement laissé à la session qui commande la relecture).

## Pièces lues et empreintes (sha256)

| Pièce | Empreinte |
|---|---|
| `prereg/temoin-attaque-publiee-bailey-v1.md` (l. 295-380 lues : l. 307-310, 338, 366-372, critères, liste d'arrêt) | `fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3` |
| `registres/passations/2026-11-11-1226-decision-lazar-option-b-arret-autonome.md` | `fb6f603249d5c2b1a6f31caf8f2376aa993b7481449ce4c2cddf0c6b1e6b7fc5` |
| `docs/notes/reproduction-attaque-publiee-v1/lectures-addendum-condition6-v8.md` (en-tête, lectures 22, 32, 37, 38) | `d2c2b7950d2d6af321502fcb4596b1f9dfc112686fce32c5538530b900b65884` |
| `src/controle_ia/temoin_bailey/instance_v8.py` (base du différentiel) | `7e4c2dc8625ed6874c5a22ff1ce98d8c2d1a219aa40fe27a7b24c0360e8be19b` |
| `src/controle_ia/temoin_bailey/instance_v10.py` | `d65fa8edce6346463f489da2e95961243438428b9bbb9cad7628f6bace762f98` |
| `src/controle_ia/temoin_bailey/lanceur_v9.py` (base du différentiel) | `324dee5aaee624a83af681613f12bcc70d423407683aa9c363eef2c2855456f3` |
| `src/controle_ia/temoin_bailey/lanceur_v10.py` (différentiel, plus `FournisseurVast`, `Poste.d_avant`, `Veilleur.verifier/_passage`, `commande_detachee`, `commande_sondage`, `commande_arret`, `conduire` l. 1154-1215, `_finir`, `_creation_incertaine`) | `9ec5634ca7336875554f4e2b7c602fa3032495c54170e180f39e48e7a5ccd916` |
| `tests/test_temoin_bailey_condition6_v10.py` (aides et essais v10, l. 1380-1972) | `5df9b140b42698e88619803236a576c2511271db5a380c6c9c9fa19d548663af` |
| `journaliseur_v3.depense_courante` (l. 152-154) | (fichier non empreinté ici ; inchangé hors différentiel) |
| Paquet installé `vastai` 1.11.0 : `cli/commands/instances.py` | `0ea41f90d38f861212c893cf1fcfd25a203061344e4177d26bd4b5cb8fd52072` |
| idem `api/instances.py` | `0fe3dcddd971e38f5d48cf5d20a8704c9a4e5afbdb6888e7846042ea332fca77` |
| idem `api/client.py` | `9cb3b1ee6c5ba45696470998ccf29b9b758b8fa4ca9706144f7cb7b09c89b5b9` |
| idem `SKILL.md` | `6cfc48189c7940c948e72fcd6286d6cc77aa35ae3ca0947edecf2571c9c9fe9a` |
| Documentation publique `https://docs.vast.ai/llms-full.txt`, téléchargée le 11 novembre 2026 à 13:07 UTC (copie de travail hors dépôt) | `5b201cb12430a7c8c1687ce5594de8d74ad29c0b3a14e54f1c2cecb4b3675f85` |

**Non lu** (cloisons) : `donnees/`, `diag/`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`,
`registres/etat.md`, lignes R-604 à R-610 de `registres/decisions.md`, tout résultat, note ou seuil de sonde ou de
moniteur, tout résultat d'attaque. Non lus non plus : le reste de `instance_v10.py` et `lanceur_v10.py` hors des
fonctions citées, `lecture_v8.py` (seul `relance_permise` est appelé, non relu).

**Outils** : `diff -u`, `grep`, `sed`, `sha256sum`, `curl` (documentation publique seulement), `pytest`. Aucun appel à
`vastai`, aucune dépense, aucun commit. Aucune variable d'environnement imprimée.

**Essais** : `tests/test_temoin_bailey_condition6_v10.py` : **82 passés** (119,9 s). Sondes du relecteur (fichier hors
dépôt, `scratchpad/diff-c6-v10/sondes/test_sondes_relecteur.py`, `157d67d9…`) : 4 sondes, **les 4 confirment un défaut**
(S1 à S4 ci-dessous).

## Verdict

**Non conforme en l'état : trois corrections bloquantes (B-1 à B-3), deux à corriger (C-1, C-2), sept à préciser.**
L'addendum 2 ne peut être écrit qu'après B-1 à B-3 et C-1, C-2 (ou la décision de Lazar de les déclarer), puis le mot
de Lazar sur les lectures 37 et 38. Le reste tient : clé d'instance jamais imprimée, journalisée ni transférée ; aucune
clé du compte sur l'instance ; `-y` et ligne de succès corrects ; garde d'auto-arrêt sans repli silencieux ; sources du
rédacteur vérifiées.

## Corrections

### Bloquantes

**B-1 (point 1) — un disque plein empêche à jamais l'arrêt du conteneur.** Dans `ChienDeGarde._preparer`, l'écriture
finale `_ecrire_json(self.etats / ETAT_ARRET, …)` n'est protégée par aucun `try`. Sur `OSError` (disque plein,
`ENOSPC`), `passage` lève, `boucle` journalise (sans effet, disque plein) et recommence au passage suivant, toujours
avant `_arreter_conteneur`. `prepare` reste faux et l'API n'est jamais appelée. Une instance au disque plein reste
donc facturée au taux de la carte sans fin, une fois la conduite morte (sonde S1 : 50 passages, aucun appel à l'API).
Un disque plein est plausible : journaux, cache du modèle et suffixes par tour. C'est précisément le cas pour lequel la
v10 existe. Correction : `_preparer` ne lève jamais (chaque écriture sous `try`, erreur notée) et pose
`prepare = True` quoi qu'il arrive. Plus généralement, une exception dans la préparation ou l'observation ne doit
jamais empêcher l'appel d'arrêt. Il faut ajouter l'essai (R5) : disque plein, arrêt demandé quand même.

**B-2 (point 1) — une commande qu'on ne peut pas tuer empêche à jamais l'arrêt.** `passage` ne prépare l'arrêt et
n'appelle l'API que si `_arreter_commandes()` rend vrai, c'est-à-dire quand plus aucune commande ne vit. Un processus
en sommeil non interruptible (état D : pilote de carte bloqué, erreur Xid, entrée-sortie bloquée) survit au KILL.
`pid_vivant` ne l'exclut pas (seuls les zombies sont exclus). La boucle ne finit donc jamais et l'instance reste
facturée sans borne (sonde S2 : 50 passages espacés d'une heure, aucun appel à l'API). Le même blocage survient si
`os.killpg` lève `PermissionError` à chaque passage. Correction : borner l'attente, par exemple au plus 2 ×
`GRACE_EXECUTION_S` après la décision ou N passages. Au-delà, préparer l'arrêt (l'état de la commande survivante est
reconstitué, ou noté comme non reconstitué) et arrêter le conteneur, qui tue tout. Le noter au journal du chien. Il
faut ajouter l'essai (R5).

**B-3 (point 4, l. 307-310) — `reprendre` détruit l'instance sans aucun transfert si `ls` échoue.** Dans
`Reprise._reprendre`, `code, sortie = executer(ident, "ls -1 /root/x …")` : le code de retour n'est pas lu. Sur une
coupure passagère, `FournisseurVast.executer` rend `(255, "")`. On obtient `etapes = []`, `transferts = {}`, et
`complet = all(...)` sur un dictionnaire vide vaut **vrai**. L'instance est alors **détruite sans qu'aucun journal ait
été transféré** (sonde S3). Le run est perdu (pas de verdict), contrairement à l. 307-310 et à la lecture 38
(« seulement si chaque étape a un transfert qui fait foi »). Correction : exiger `code == 0` ; refuser la destruction
si `etapes` est vide alors que le journal de la conduite (`conduite-v5.jsonl`) montre des étapes lancées. Mieux :
prendre comme liste attendue l'union des étapes lancées selon ce journal et des dossiers présents, et exiger un
transfert qui fait foi pour chacune. Sinon : remise à l'arrêt, nœud. Il faut ajouter l'essai.

### À corriger

**C-1 (points 1 et 4, dépense) — reprise : rien n'arrête l'instance entre `demarrer` et la pose de la minuterie, et une
remise à l'arrêt refusée laisse l'instance en marche.** Après `demarrer`, `_prete` peut attendre jusqu'à
`DELAI_PRETE_S` (1 800 s) avant que la minuterie soit posée. Pendant ce temps, aucun processus de l'instance ne peut
l'arrêter : le chien d'origine est mort avec l'arrêt du conteneur. Aucun veilleur local ne la surveille non plus,
puisque `Reprise` n'en lance pas. Si la session de reprise meurt dans cette fenêtre, l'instance reste facturée au taux
de la carte sans borne. De même, si l'instance n'est pas prête et que `arreter` est refusé une seule fois (`_vast`
sans la ligne « stopping instance … », erreur passagère), `_remettre_a_l_arret` ne fait aucun nouvel essai.
L'alerte dit alors « la minuterie de l'instance l'arrête », ce qui est **faux** : aucune minuterie n'a été posée
(sonde S4 : instance laissée en marche, `minuteries == []`, alerte erronée). Ce cas existe aussi sur la branche
« minuterie non lancée ». Correction : avant `demarrer`, lancer un veilleur local détaché qui arrête l'instance par
son identifiant à `début + DELAI_PRETE_S + MINUTERIE_REPRISE_S` ou à l'échéance. Faire plusieurs essais d'arrêt
(`ESSAIS_DESTRUCTION`). Écrire l'alerte selon que la minuterie a été posée ou non.

**C-2 (point 1, « jamais rendre non lisible un run lisible », lecture 22 (b), lecture 38) — le veilleur local et
`_finir` détruisent une instance que le chien a arrêtée avant son transfert.** Lecture 22 (b) : « D compte l'instance
au taux c […] intervalles arrêtés compris ». Le `Veilleur` (`verifier`, `_passage`) détruit donc à D ≥ B − 0,5 (ou à
l'échéance plus le délai) **sans lire le statut**. Cas où la conduite meurt et le poste vit : le chien arrête à B − 2
(ou à la fin, ou à l'échéance moins la marge), puis le veilleur détruit l'instance arrêtée environ 1,5 USD plus tard
au taux de la carte, souvent moins d'une heure après. Les journaux sont perdus avant toute reprise, alors que la
lecture 38 et la décision de Lazar (« journaux gardés sur l'instance arrêtée ») supposent qu'ils attendent sur le
disque. De même, dans `_finir`, si le chien a déjà arrêté le conteneur (cause tenue depuis 3 600 s, ou B − 0,5), les
transferts échouent et la conduite détruit quand même (« la destruction suit dans tous les cas », comportement v9,
désormais déclenchable par le chien). Correction : le veilleur et `_finir` lisent `statut`. Si l'instance est
`stopped` ou `exited` et qu'une étape n'a pas de transfert qui fait foi : pas de destruction (seul le stockage court),
alerte « reprise requise ». La destruction reste immédiate pour une instance en marche (la borne de dépense prime). Le
coût est le stockage seul : c'est bien le dépassement que la décision de Lazar borne.

### À préciser (sans effet sur une issue ni sur la dépense, ou risque à déclarer dans l'addendum)

**P-1 — Le chien n'est pas surveillé après la garde d'auto-arrêt.** S'il meurt en cours de run (tué faute de mémoire,
erreur au démarrage d'une passe, etc.), rien ne le relance et rien ne le signale. Le veilleur local couvre le cas tant
que le poste vit ; poste et chien morts ensemble, la dépense n'a plus de borne. Même chose si l'hôte redémarre le
conteneur : les processus détachés ne reviennent pas, et la documentation de Vast offre `onstart`, inutilisé ici. À
déclarer au risque 22. Mieux : le sondage lit aussi `chien-de-garde.battement` et relance le chien (en effaçant
`.fin`) s'il est périmé.

**P-2 — Lecture 38, « quelques minutes ».** La borne réelle d'une reprise est d'au plus `DELAI_PRETE_S` + 120 s +
`MINUTERIE_REPRISE_S`, soit environ 1,5 h au taux de la carte. `Reprise` ne compare jamais D à B, et le mode minuterie
ne lit pas la dépense : une reprise peut porter la dépense réelle au-delà de B. À écrire tel quel dans la lecture 38,
ou à borner la minuterie par le budget restant.

**P-3 — « Ce qui sort de l'instance ».** Le texte (l. ≈ 323-326) dresse une liste fermée. Le journal
`chien-de-garde-v10.jsonl` en sort désormais (causes, noms de commandes, horodatages, messages d'erreur tronqués).
J'ai vérifié qu'il ne contient ni note, ni texte, ni suffixe, ni clé. L'addendum 2 doit pourtant l'ajouter à la liste.

**P-4 — L'appel à l'API passe par `urllib` avec l'en-tête `User-Agent` par défaut (`Python-urllib/3.x`).** Le paquet
envoie `vastai-sdk/<version>` et refait l'appel sur 429/502/503/504. Si l'hôte de la console filtre l'agent par
défaut, la garde d'auto-arrêt tombe : pas de run, donc aucun repli silencieux, mais une création perdue. Recommandé :
reprendre l'en-tête du paquet.

**P-5 — Le délai de prise en charge (3 600 s) court depuis la première apparition de la cause.** Il ne court pas
depuis l'arrivée de la conduite ou de la reprise. Une reprise d'une instance encore en marche (chien d'origine) peut
donc être coupée par le chien en plein transfert. L'issue est sûre (transfert incomplet, pas de destruction, remise à
l'arrêt, nœud), mais il faut l'écrire dans la lecture 37 (b) ou 38, ou faire repartir le délai à chaque nouveau
battement.

**P-6 — Repli TERM au PID 1.** Il n'intervient qu'après `_preparer` (états et empreintes écrits) en mode chien, et
seulement après 10 refus (jamais après des arrêts acceptés mais sans effet : les renouvellements prennent la branche du
succès). Sans effet sur une issue. Mais `vastai/SKILL.md` (l. 150) dit qu'une instance `exited` « will never reach
running ». `Reprise` traite pourtant `exited` comme `stopped` et tente `demarrer`, puis remet à l'arrêt au bout de
1 800 s : journaux sur un disque qu'on ne joint peut-être plus. À déclarer.

**P-7 — `_remettre_a_l_arret` tient la ligne « stopping instance … » pour un arrêt fait, sans relire `statut`.** C'est
conforme au point 3 (succès de l'API), mais il faut l'écrire. Par ailleurs, le message du docstring de la v10
(« 118 essais ») ne correspond pas aux 82 essais de ce fichier : il compte sans doute d'autres fichiers ; à préciser
dans la passation.

## Réponses point par point

1. **Les quatre cas.** `decider` est correct comme fonction pure. Conduite vivante : bornes B − 0,5, échéance −
   marge/2, 3 600 s, marque `rapatrie`. Conduite injoignable : arrêt aussitôt, sauf une exécution du run principal,
   qui finit sous ses gardes ; une cause dépense ou échéance l'emporte alors (« arreter »), avec 300 s de grâce. Les
   causes reconstituées sont celles de la liste fermée. Aucune suite ne rend lisible un run non interprétable : le chien
   ne lit aucune note, ne relance rien et ne reconstitue que des états absents. Il n'écrase jamais. Défauts trouvés :
   B-1 et B-2 (instance jamais arrêtée), C-1 (reprise), C-2 (journaux détruits avant reprise), P-1 (chien non
   surveillé), P-5.
2. **Clé d'instance.** Elle est lue dans `/proc/1/environ`, ou à défaut dans l'environnement du processus. Elle ne
   sert qu'à l'en-tête `Authorization` d'une requête `urllib`, et ne figure jamais sur une ligne de commande. Les
   erreurs ne gardent que le nom du type (`from None`). `verifier_auto_arret` ne rend que des booléens.
   `_noter`/`boucle` n'écrivent que des messages de `GardeArret` à texte fixe ou des erreurs étrangères à la requête.
   La clé n'est écrite dans aucun fichier : `JOURNAL_CHIEN`, seul fichier nouveau qui sort, n'en contient pas. La
   documentation confirme que c'est une clé restreinte : « it can only start, stop, or destroy that specific instance »
   (`llms-full.txt` l. 1932). Aucune clé du compte n'est posée : `creer` ne passe aucune variable, et le
   `instance_api_key` rendu par la création n'est ni gardé ni imprimé (seul `new_contract` est lu ; les messages
   d'erreur de `creer` ne contiennent pas la sortie). Hors différentiel : `instance_v10` l. 576 copie
   `dict(os.environ)` vers l'exécution ; c'est sans effet ici, rien de l'environnement ne sortant de l'instance.
3. **Destruction et arrêt.** Vérifié dans le code installé (1.11.0) : seul `destroy instance` demande une confirmation
   (`input`, « Aborted. », retour sans erreur) ; `-y` est passé ; `stop` et `start` n'en ont pas. Les lignes
   « destroying/stopping/starting instance {id}. » ne sont imprimées que si `rj.get("success")`. Tous les appels de
   destruction (conduite, veilleur, création incertaine, reprise) passent par `FournisseurVast.detruire`. Côté
   instance, l'arrêt n'est tenu pour demandé que sur `success is True`, et il est renouvelé tant que le chien vit
   (600 s). Conforme.
4. **`reprendre`.** Il ne détruit que l'instance unique de l'étiquette, refuse en cas de discordance avec le journal ou
   de doublon, refuse le redémarrage après l'échéance et borne la minuterie par l'échéance. Défauts : B-3 (destruction
   sans transfert), C-1.
5. **Garde `auto-arret`.** Elle vérifie les variables, l'identifiant, l'API (essai `running`) et le chien vivant ;
   indisponible : « garde de mise en place tombée », `return` avant la mise en place, puis transfert et destruction
   par `_finir`. Pas de repli silencieux. Le repli TERM au PID 1 est déclaré et journalisé, sans effet sur une issue
   (P-6).
6. **Sources.** Code installé : `PUT /api/v0/instances/<id>/` `{"state": "stopped"|"running"}`, en-tête
   `Authorization: Bearer` (`api/client.py`), réponse `success` : conforme à la docstring. Documentation : les
   citations sont exactes (`CONTAINER_API_KEY` l. 1932 et 21171 ; « Using the CLI from Inside an Instance »
   l. 21254-21285 ; FAQ « How do I stop an instance from within itself? » l. 23524 ; stockage facturé à l'arrêt
   l. 21649, 39227 ; « stopped — disk charges only », `SKILL.md` l. 143). Non établi, comme le dit la docstring : l'arrêt
   effectif de la facturation de la carte par cette clé. La documentation ajoute (l. 24621) qu'un redémarrage peut
   rester en « scheduling » si la carte est reprise : c'est déjà couvert par `_prete`, à citer dans la lecture 38.

## Sondes (hors dépôt)

`scratchpad/diff-c6-v10/sondes/test_sondes_relecteur.py` (`157d67d9…`), lancé avec
`PYTHONPATH=src:tests python -m pytest -q -p no:cacheprovider` : S1 (disque plein, aucun appel à l'API), S2 (commande
impossible à tuer, aucun appel à l'API), S3 (`ls` en échec à la reprise, instance détruite sans transfert), S4 (reprise
non prête et arrêt refusé : instance laissée en marche, alerte erronée). Les quatre assertions de défaut passent.
