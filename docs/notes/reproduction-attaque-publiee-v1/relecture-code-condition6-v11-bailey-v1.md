# Relecture R2, en différentiel v10 → v11, du code de la condition 6 — témoin de Bailey — arrêt autonome de l'instance — v1

- Date : Wed Nov 11 13:52 UTC 2026 (`date -u`). Relecteur : sous-agent neuf (R2). Je n'ai écrit aucune des pièces lues.
- Je reçois d'office le `CLAUDE.md` du dépôt (consignes permanentes), injecté dans mon contexte.
- Dépôt `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, commit `47772e37`.
- Non scellé : le scellement revient à la session qui commande la relecture.

## Pièces lues et empreintes (sha256)

| Pièce | Empreinte |
|---|---|
| `prereg/temoin-attaque-publiee-bailey-v1.md` (l. 300-375 : l. 307-310, 338, 366-372, critères, liste d'arrêt) | `fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3` |
| `docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v10-bailey-v1.md` (rapport appliqué) | `b6b6430bb0bc6263a944c7234bbd4f3fb3fbbe43b8e762ec2510facb4b322ef1` |
| `docs/notes/reproduction-attaque-publiee-v1/lectures-addendum-condition6-v9.md` (en-tête, lectures 22, 37, 38) | `25931f26a613533f51c4744270ce4d6a5113bd537172ec7825bb81612005f39a` |
| `src/controle_ia/temoin_bailey/instance_v10.py` (base du différentiel) | `d65fa8edce6346463f489da2e95961243438428b9bbb9cad7628f6bace762f98` |
| `src/controle_ia/temoin_bailey/instance_v11.py` (différentiel, plus `ChienDeGarde` en entier, `fin_prevue`, `verifier_auto_arret`, `_main_v11`) | `0b695fc298ff763ec3f73fa66ed32d3f1c849a393fd0075385a48ab47006d9a4` |
| `src/controle_ia/temoin_bailey/lanceur_v10.py` (base du différentiel) | `9ec5634ca7336875554f4e2b7c602fa3032495c54170e180f39e48e7a5ccd916` |
| `src/controle_ia/temoin_bailey/lanceur_v11.py` (différentiel, plus `Poste`, `Veilleur` en entier, `FournisseurVast.statut/taux_horaire`, `commande_chien`, branche « running » de `_reprendre`) | `c581be7c52b725c2b82ce068d055e9bcf4f4d942432c508442c76260662c6a1c` |
| `tests/test_temoin_bailey_condition6_v11.py` (aides l. 1394-1480, 1884-1930 ; essais v11 l. 2005-2540) | `b180ef11a0f20481a009f8c10a57df3b4056ca03fd835b6e4348bc5b62500c3f` |
| Sondes du relecteur précédent `scratchpad/diff-c6-v10/sondes/test_sondes_relecteur.py` | `157d67d98dfc2eb588d3b50834c63463aeb0e80b211d00a6a4ff260a1c93f0cc` |
| Copie de travail de la documentation publique de Vast (`llms-full.txt`, téléchargée par le relecteur précédent ; relue hors réseau, l. 1953-1967, 21325-21440, 24619-24621) | `5b201cb12430a7c8c1687ce5594de8d74ad29c0b3a14e54f1c2cecb4b3675f85` |
| Paquet installé `vastai` 1.11.0 : `cli/commands/machines.py` l. 1173, 1258-1292 (`intended_status` et `actual_status` distincts), `data/instance.py` l. 58-60 | (non empreintés ; lus par `grep`) |

**Non lu** (cloisons) : `donnees/`, `diag/`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`,
`registres/etat.md`, les lignes R-604 à R-610 de `registres/decisions.md`, tout résultat, toute note ou tout seuil de
sonde ou de moniteur, tout résultat d'attaque. Non lus non plus : le reste de `instance_v11.py` et de `lanceur_v11.py`
hors des parties citées, `lecture_v8.py` (seule la valeur d'`ETAPES` a été lue).

**Outils** : `diff -u`, `grep`, `sed`, `sha256sum`, `pytest`. Aucun appel à `vastai`, aucune requête réseau, aucune
dépense, aucun commit. Aucune variable d'environnement n'a été imprimée.

**Essais** : `tests/test_temoin_bailey_condition6_v11.py` : **109 passés** (130,9 s). Sondes du relecteur (fichier hors
dépôt, `scratchpad/diff-c6-v11/sondes/test_sondes_v11.py`, `ee331e03065487c7c7049fe901a0be53dd8ee0e102e3e00ccd7442b1136a75c8`,
lancé avec `PYTHONPATH=src:tests python -m pytest -q -p no:cacheprovider`) :
- S1 à S4, portées sans changement sur la v11 : **les 4 échouent**, ce qui est attendu (défauts B-1, B-2, B-3 et C-1
  de la v10 corrigés) ;
- S5 à S9, sondes nouvelles : **les 5 passent**, c'est-à-dire que chacune confirme un défaut (ci-dessous).
- (L'import `*` du fichier d'essais rejoue ses 109 essais : 114 passés, 4 échoués au total.)

## Verdict

**Non conforme en l'état : quatre corrections bloquantes (V-1 à V-4), une à corriger (V-5), six à préciser.**
Les corrections B-1, B-2, B-3, C-1, C-2, P-1, P-4 et P-7 de la relecture v10 sont appliquées, et leurs essais
inversés éprouvent bien le comportement. Restent trois défauts : le « stopped » lu sur `actual_status` sans arrêt
accepté, la branche « en marche » de la reprise sans borne de budget, et l'observation du chien qui peut bloquer les
causes dépense et échéance. Ils laissent encore une instance facturée sans arrêt, ou une dépense au-delà de B. Un
quatrième défaut fait perdre des journaux sur une seule lecture de statut en échec. L'addendum 2 ne peut être écrit
qu'après V-1 à V-4 (ou la décision de Lazar de les déclarer), puis le mot de Lazar sur les lectures 37 et 38. Le point (3)
tient : la clé d'instance n'est jamais imprimée, journalisée ni transférée, et aucune clé du compte n'est posée sur
l'instance.

## Corrections

### Bloquantes

**V-1 (point 1 ; C-1 et P-7) — un statut « stopped » lu sur `actual_status` passe pour un arrêt, sans aucun arrêt
accepté. Une instance restée en « scheduling » finit sans veilleur et démarre plus tard sans borne.**
`FournisseurVast.statut` rend `actual_status` seul. Le paquet installé distingue pourtant `intended_status` et
`actual_status` (`vastai/cli/commands/machines.py` l. 1173 : `info.get('intended_status') or info.get('actual_status')`).
La documentation de Vast décrit le cas : un redémarrage attend la carte en « Scheduling » (`llms-full.txt` l. 21335,
21391-21394, 24621), peut-être indéfiniment (l. 21435-21440), et ne s'annule qu'en arrêtant de nouveau (« Cancel
scheduling by clicking stop again », l. 21394). Pendant ce temps, l'instance n'est pas « running ». Ce que rend
`actual_status` n'est pas documenté ; vraisemblablement « stopped » ou « exited », l'instance étant voulue en marche.
Deux suites d'événements en découlent :
- `VeilleurArret._passage` finit (« arrêtée ») dès qu'il lit « stopped » ou « exited », **sans avoir jamais demandé
  l'arrêt** (sonde S5 : `essais == 0`, aucun appel à `arreter`). Si la session de reprise meurt pendant `_prete`,
  c'est-à-dire dans le cas même pour lequel C-1 existe, le veilleur finit à sa borne. La carte se libère plus tard,
  l'instance démarre, et ni minuterie, ni chien, ni veilleur ne l'arrêtent : elle reste facturée sans borne.
- `_remettre_a_l_arret` tient « stopped » relu pour une confirmation, même quand les trois arrêts ont été refusés
  (sonde S6 : `acceptee: False`, veilleur 5001 arrêté, aucun veilleur vivant, aucune alerte de remise). L'instance est
  laissée voulue en marche, et rien ne l'arrête.

Correction :
- le veilleur d'arrêt ne finit qu'après au moins un arrêt **accepté** (ligne « stopping instance … ») depuis son
  échéance, **et** un statut arrêté relu ensuite ;
- `_remettre_a_l_arret` ne tient l'arrêt pour confirmé que si `accepte` est vrai et que le statut relu est arrêté ;
  sinon, veilleur à échéance immédiate et alerte ;
- mieux : `statut` lit aussi `intended_status`, et « arrêté » exige `intended_status` ∈ {stopped, exited} (ou absent)
  et `actual_status` ∈ {stopped, exited}. La même lecture vaut pour `_reprendre` (statut initial), `Veilleur` (C-2)
  et `_finir`.

Il faut ajouter les essais (R5) : statut « stopped » dès le départ, puis aucun arrêt accepté (le veilleur ne finit
pas) ; arrêt refusé trois fois et statut « stopped » (veilleur immédiat lancé, alerte).

**V-2 (point 1 ; correction ajoutée P-2, plafond dur de `GO-2026-11-10-10`) — reprise d'une instance en marche : aucune
borne de budget, aucun veilleur d'arrêt.** Dans `_reprendre`, la branche `statut == "running"` ne calcule pas
`_borne_budget`, ne lance pas de veilleur d'arrêt, et ne compare jamais D à B. Elle touche ensuite le battement de la
conduite, ce qui fait patienter le chien d'origine s'il vit, puis transfère au taux de la carte. Sonde S8 : D du poste
= 80 USD > B = 75 USD, chien mort ; la reprise transfère puis détruit sans calcul (`"budget"` absent du bilan, aucun
veilleur). Il suffit que le chien soit mort (risque déclaré, lecture 22) pour que la reprise porte la dépense au-delà
de B, contre la correction P-2 (« jamais au-delà de B »). Si la session meurt après avoir touché le battement, rien ne
borne plus l'instance. Correction : appliquer la même règle que pour une instance arrêtée.
- Calculer `_borne_budget` avant tout `executer` ; s'il est illisible, ou s'il reste moins de `duree_transfert_min_s`,
  remettre l'instance à l'arrêt **sans transfert** (V-1) et noter « reprise impossible dans le budget : nœud ».
- Sinon, avant de toucher le battement, lancer et vérifier vivant un veilleur d'arrêt à `min(borne_budget, échéance,
  maintenant + MINUTERIE_REPRISE_S)`.

Il faut ajouter l'essai (S8 inversée).

**V-3 (point 1 ; « plus généralement » de B-1 non tenu) — une erreur persistante de l'observation empêche à jamais
l'arrêt, même au-delà de B.** En v11, `passage` attrape l'exception d'`observer` et rend `None` : le passage suivant
observe de nouveau. Mais `fin_prevue` n'est pas sous `try` dans `observer`. En Python 3.13, `Path.exists` relève une
`OSError` autre que ENOENT, ENOTDIR, EBADF ou ELOOP (une erreur d'entrée-sortie EIO sur un disque qui lâche, par
exemple), et l'import de `lecture_v8` peut échouer. Si l'erreur persiste, aucune cause n'est jamais décidée, alors que
la dépense et l'échéance sont calculées en mémoire. Sonde S9 : conduite injoignable, D = B + 5, `fin_prevue` en EIO,
50 passages espacés d'une heure : aucun appel d'arrêt, `cause` reste `None`. Correction :
- `fin_prevue` sous `try`, lu prudemment (faux) et noté, comme la marque ;
- la décision sur la dépense, l'échéance et le battement ne dépend d'aucune lecture qui puisse lever ; mieux, si
  `observer` lève, `passage` décide quand même sur ces seules causes (`decider` avec `fin=False`, `rapatrie=False`,
  `en_cours=[]`).

Il faut ajouter l'essai (S9 inversée).

**V-4 (point 2 ; C-2) — veilleur de secours : une seule lecture du statut en échec détruit une instance arrêtée dont
rien n'a été transféré.** Dans `Veilleur._passage`, une seule erreur de `statut` donne `None`, et `None` mène à la
destruction. Sonde S7 : instance « stopped », pas de `rapatriement-v11.json`, D ≥ B − 0,5 ; une erreur passagère (429,
coupure) à la première lecture suffit : destruction, journaux perdus. La reprise prévue par la décision de Lazar
devient alors impossible. `_finir` relit pourtant trois fois (`_statut_relu`). Correction : un statut illisible est
noté et relu au passage suivant ; la destruction n'a lieu qu'après `ESSAIS_DESTRUCTION` lectures illisibles de suite.
Le délai ajouté, environ 2 × 30 s au taux c, tient dans la marge de 0,5 USD. Il faut ajouter l'essai (S7 inversée).

### À corriger

**V-5 (point 2) — même seuil pour le veilleur de secours de la conduite et pour la borne de la reprise.** Le veilleur de
secours d'une conduite morte vit encore pendant une reprise si le poste vit. C'est le cas que décrit C-2 : il ne finit
qu'à sa cause. Il détruit à D ≥ B − 0,5 (au taux c du poste) ou à l'échéance, dès que le statut n'est pas arrêté. La
reprise s'arrête à `borne_budget`, au même B − 0,5, et à l'échéance. La minuterie laisse en général environ 115 s
d'avance, puisque `DELAI_COMMANDE_S` est déduit. Il n'y a en revanche aucune avance si la reprise est encore dans
`_prete` à la borne (arrêt demandé à l'instant même par `remettre` et par le veilleur d'arrêt), ou si l'appel de la
minuterie est retenté (jusqu'à environ 3 min). Le veilleur de secours lit alors « running » et détruit une instance
dont le transfert vient d'être coupé. Le budget est épuisé à cet instant, donc la perte ne change pas une issue sous
B. Elle détruit pourtant des journaux que la décision de Lazar veut garder, et que seul un nouveau GO permettrait de
lire. Correction :
- la reprise borne ses arrêts à `borne_budget − 2 × période du veilleur − 120 s`, et s'arrête avant l'échéance du même
  écart ;
- ou bien la reprise arrête par son PID le veilleur de secours de la conduite (PID au journal de la conduite, identité
  vérifiée, R10) avant de redémarrer.

### À préciser (sans effet sur une issue ni sur la dépense, ou risque à déclarer dans l'addendum)

**Q-1 — La reprise ne marque pas la destruction dans `poste-v5.json`.** D compte alors l'instance jusqu'à maintenant,
pour toujours. C'est prudent, mais cela fausse tout calcul de budget suivant sur le poste. Un veilleur de secours
encore vivant atteint aussi sa cause, lit un statut illisible (instance détruite), puis retente `destroy` toutes les
30 s sur un identifiant disparu, sans fin. Recommandé : la reprise écrit la destruction au poste, comme le fait le
veilleur.

**Q-2 — `_finir` pose la marque `rapatrie` même quand le transfert est incomplet.** Le chien arrête alors le conteneur
(cause « fin »), et le statut est relu aussitôt après. Selon que le chien a déjà agi ou non, l'instance est gardée ou
détruite. Les deux issues sont permises (l. 309-310 : écart persistant, la garde tombe), mais le choix dépend du
moment. À écrire dans la lecture 22, ou à rendre déterministe : sans transfert complet, pas de marque et `arreter` par
identifiant.

**Q-3 — Étape lancée sans dossier.** Une étape notée « lancee » dont le lancement a échoué avant la création de son
dossier n'aura jamais de transfert qui fait foi. `_finir` (si l'instance est arrêtée) et la reprise (union B-3)
refusent donc la destruction pour toujours : stockage jusqu'à l'inventaire manuel. C'est sûr pour les journaux, mais il
faut l'écrire dans la lecture 38 (nœud attendu).

**Q-4 — Relance du chien (P-1).** Un chien lent, dont le battement a plus de 600 s, est tué par son PID même s'il est
en pleine préparation (empreintes, états). Avec les durées actuelles, c'est peu probable : passage d'au plus environ
4 min, appels à l'API compris. Il faut néanmoins vérifier, ou écrire, que les fichiers d'empreintes sont écrits de façon
atomique, comme l'état d'exécution (lecture 31).

**Q-5 — Risque déclaré inchangé.** Poste éteint et chien mort (redémarrage du conteneur par l'hôte, tué faute de
mémoire) : la dépense n'a plus de borne jusqu'à la reprise ou à l'inventaire. Rien de nouveau, c'est déclaré (lecture
22). Le champ `onstart` de Vast reste la parade recommandée.

**Q-6 — Lectures à mettre à jour après V-1 à V-5.** Lecture 38 : fin du veilleur d'arrêt (arrêt accepté et statut
relu), branche « en marche » bornée par le budget, écart entre la borne de reprise et le seuil de secours. Lecture 22 :
lecture du statut du veilleur de secours. Lecture 37 : observation qui ne bloque pas les causes dépense et échéance.

## Réponses point par point

1. **Instance facturée sans arrêt, dépense au-delà de B.**
   - Pilotage mort : le chien borne ; la relance du chien par la conduite est correcte (PID, `.fin` effacé, lancement
     vérifié, alerte après trois échecs).
   - Chien mort : relancé tant que la conduite vit ; poste éteint, risque déclaré (Q-5).
   - Disque plein : corrigé (S1 échoue ; essais B-1 avec écriture refusée partout, battement touché).
   - Commande qu'on ne peut tuer : corrigé (S2 échoue ; borne de 600 s ou 40 passages ; `killpg` refusé en processus
     réel).
   - API refusée : retentée, en-tête et nouveaux essais du paquet (P-4), repli TERM au PID 1 inchangé.
   - Reprise d'une instance arrêtée : borne de budget correcte (minuterie raccourcie de `DELAI_COMMANDE_S`, `_prete`
     coupée à la borne, refus sous 900 s, taux le plus haut retenu).
   - Défauts restants : **V-1** (« stopped » sans arrêt accepté), **V-2** (branche « en marche » sans budget), **V-3**
     (observation qui bloque les causes calculées en mémoire).
2. **Destruction avant le transfert et la comparaison.**
   - Reprise : `ls` en échec, plus de destruction (S3 échoue). La liste attendue est l'union du journal et des
     dossiers, et chaque étape doit avoir un transfert qui fait foi.
   - `_finir` et veilleur : le statut est lu avant de détruire (C-2).
   - Défauts restants : **V-4** (une seule lecture du statut en échec), **V-5** (même seuil des deux veilleurs) ;
     Q-2 (marque posée sans transfert complet).
   - `_finir` détruit une instance en marche dont le transfert est incomplet : c'est conforme à l. 309-310 (écart
     persistant, la garde tombe : « non interprétable »), et ne rend lisible rien de non interprétable.
3. **Clés.**
   - `requete_etat_instance` v11 : les messages ne portent que le code HTTP ou le nom du type (`from None`), et
     `Retry-After` n'est lu que comme nombre. `_arreter_conteneur` note `str(err)` d'une `GardeArret` à texte fixe.
   - Les commandes de relance du chien (`commande_chien`) et du veilleur d'arrêt (`--instance`, `--etiquette`,
     `--echeance`, `--journal`, `--fournisseur`) ne passent aucune clé.
   - Le veilleur d'arrêt tourne sur le poste avec la configuration `vastai` du poste, jamais sur l'instance.
   - Aucune clé du compte n'est posée sur l'instance. Conforme.
   - Remarque inchangée depuis la v10 : les exécutions héritent de l'environnement du conteneur, où Vast pose
     `CONTAINER_API_KEY` ; rien de cet environnement ne sort de l'instance.
4. **Sondes et essais inversés.**
   - S1 à S4 échouent sur la v11.
   - Les essais inversés éprouvent le comportement, non le texte : appel d'arrêt effectif, `prepare`, journal du chien,
     état reconstitué en processus réel, `ls_code`, absence de destruction, alerte exacte (« aucune minuterie n'a été
     posée », PID des veilleurs), veilleur d'arrêt en processus réel (fournisseur « fichier »).
   - Les essais C-1 ne couvrent pas le « stopped » sans arrêt accepté (V-1). Aucun essai ne couvre la branche « en
     marche » sous budget (V-2).

## Sondes (hors dépôt)

`scratchpad/diff-c6-v11/sondes/test_sondes_v11.py` (`ee331e03…`).

| Sonde | Statut sur la v11 | Défaut |
|---|---|---|
| S1 à S4 | échouent (attendu) | défauts de la v10 corrigés |
| S5 | passe | V-1 : veilleur d'arrêt fini sur « stopped » sans arrêt demandé |
| S6 | passe | V-1 : trois arrêts refusés, « stopped » relu, veilleurs arrêtés sans alerte |
| S7 | passe | V-4 : statut illisible une fois, instance arrêtée détruite |
| S8 | passe | V-2 : reprise d'une instance en marche à D > B, sans budget ni veilleur |
| S9 | passe | V-3 : observation en EIO, aucune décision au-delà de B |
