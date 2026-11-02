Addendum au verdict A1 (`verdict-a1-v1.md`, sha256 `795e5e992d65bce3096d78f1cd4c36c95cdfc00cdeb40f6259278275e92d3909`, inchangé) : issues et qualifications d'avance inchangées (W1 « non jugeable (instrument en défaut) » ; W2 « infirmée (brèche sous v8) », « par classe non couverte », portée par Argon seul) ; Argon n'a pas été tronqué (96 suites complètes sur 96, 0 tentative échouée, 527 appels tous au registre) ; la cause de l'écart (b) change : d'après le registre (le code des commandes n'est pas vu ici), les 1 212 tentatives Kimi perdues après 12:22:14 viennent du plafond d'étape de 40 USD appliqué à la somme des deux fournisseurs, non de l'arrêt du relais, qui n'a rien changé aux données.
Ces refus sont comptés par le code gelé comme des échecs (une reprise, puis une tentative échouée), jamais comme « budget_depasse » ni comme arrêt ; A7 n'est pas dû à sa lettre (budget par appel) ; le plafond de dépense du texte (80 USD, 40 par fournisseur au compteur du lanceur) n'a pas été atteint : la règle « aucun taux lu » ne s'applique pas à la lettre et la lecture reste debout, qualifiée de défaut d'instrument (configuration) ; la tenir pour un arrêt de dépense serait un nœud pour Lazar (recommandation : non, confiance 0,75).

Lecteur neuf du verdict (R13), même instance que le verdict. Rédigé le 2 novembre 2026, de 16:48 à 16:56 UTC (`date -u`). Mêmes règles : aucun appel de réseau ni de modèle, aucun commit, aucun `.sha256`, aucun fichier existant modifié (le verdict scellé n'est pas touché), rien sous `donnees/`, aucune référence git `donnees/*` ; `nice -n 10 python3 -I -B` ; écriture seulement sous `P/a1-verdict-v1/`. Le n° 282 de la session de lancement (16:45 UTC) n'est pas lu ici : son contenu m'est relayé par le coordinateur.

Abréviations du verdict : P = `/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad` ; T = texte scellé (`fc81d015…`) ; S = sortie (`5dd5066c…`) ; M = manifeste (`7552e5a4…`) ; R = registre de dépense (`ae47217e…`) ; J = journaux `P/a1-audit-v1/entree/relais-complet/` ; A = audit écrit (`a886904d…`) ; C = `pole/attaque_goodhart_v2.py` (`3c9de8b8…`) ; L = lanceur `demonstrations/attaque_goodhart_v2.py` (`58609e0c…`) ; V = `P/a1-verdict-v1/travail/`. Nouveaux : AD = `/home/claude/ideation-organism/orchestrator/pole/adaptateurs.py` (`a1a8ede8d38884a28365ee797dcd3018dbf09ea1baefa3f57cfcb3281c529c99`) ; AD56 = `…/pole/adaptateurs_v56.py` (`d36c79b272af450b8d67313f44068743d80f0204bcedbd30f5d879829c945a17`), tous deux gelés au bloc de T (l. 376-377), empreintes revérifiées à 16:48 UTC.

## 1. Le mécanisme, sur le registre et dans le code gelé

### 1.1 Ce que montre le registre

- **Une seule étape pour les deux fournisseurs.** Les 1 148 débuts d'appel du registre portent tous l'étape « attaque_goodhart_v2 » et un plafond d'étape de 40,0 USD (V/v10-garde-etape-v1.json). C'est ce que le lanceur gelé transmet : la même étape (`ETAPE = "attaque_goodhart_v2"`, L l. 52) et la même part, 80/2 = 40 USD, à chacune des deux portes (L l. 284-285). Le manifeste accuse les deux (M `reglages.configuration.accuses_plafond` : Kimi et Argon, étape « attaque_goodhart_v2 », 40,0 USD). Les deux commandes écrivent au même registre (M `reglages.configuration.adaptateurs.*.commande`, argument `--registre`).
- **Chronologie de l'étape** (les deux fournisseurs ensemble ; V/v11-jalons-v1.txt) :

| instant (UTC) | réglé Argon | réglé Kimi | réglé total | engagé | réglé + engagé | marge avant un appel Kimi (pire cas 0,6659) |
|---|---|---|---|---|---|---|
| 10:39:16 (après l'appel coupé) | 20,6850 | 1,9000 | 22,5851 | 1,6219 | 24,2070 | 15,13 |
| 11:05:17 (fin d'Argon) | 34,3594 | 2,0956 | 36,4551 | 0,6663 (Kimi en cours) | 37,1214 | 2,21 |
| 12:18:03,3 (après le premier 502) | 34,3594 | 4,4150 | 38,7744 | 0 | 38,7744 | 0,56 |
| 12:22:15 (après le second 502) | 34,3594 | 5,0869 | 39,4463 | 0 | 39,4463 | **−0,11** |

- **Trois règles possibles, essayées sur les 1 148 appels inscrits** (V/v10) :
  - « réglé + engagé de l'étape (les deux fournisseurs) + pire cas du nouvel appel ≤ 40 » : aucun appel inscrit n'aurait été refusé ; la marge la plus faible est de 0,554 USD (12:18:03,39, second essai Kimi de la tentative k = 4). Après 12:22:14,962, le réglé vaut 39,446281 et l'engagé 0 ; le plus petit pire cas Kimi du registre (0,6659) donne 40,112 > 40. **Tout appel Kimi suivant est refusé.**
  - Part par fournisseur (40 chacun) : Kimi 5,09 + 0,67 ≤ 40 ; aucun refus, avant comme après 12:22.
  - Plafond cumulé de 80 : aucun refus.
  
  Seule la règle « somme de l'étape » explique des échecs à partir de 12:22:14.
- **Le fait qui tranche entre les deux explications.** Les 612 échecs de 10:39 à 10:40 (relais arrêté, injoignable) sont **inscrits** au registre en code 3 (V/v03). Les 2 424 appels qui suivent 12:22:14 n'y sont **pas** (V/v03, v10), et le journal du relais n'a aucune entrée après 12:22:14 (J). Un refus avant toute écriture au registre et tout contact avec le relais rend compte de cette trace ; un relais arrêté, non, puisqu'il avait laissé des lignes en code 3 à 10:39. L'explication de mon verdict (§2.1 b, « relais arrêté ») ne tient donc pas devant la trace ; la garde d'étape tient.
- **Heure.** Le fil Kimi est séquentiel (un fil par fournisseur, C l. 958-977). Le premier appel absent du registre est le premier essai de W1 carte 5 témoin|v8 k = 5 (V/v10). Il part juste après la fin du second 502 (12:22:14,962), soit environ 59 s avant l'arrêt du relais à 12:23:14. Si la garde refuse avant de contacter le relais, l'état du relais n'importait plus : **l'arrêt « saute Kimi » n'a rien changé aux données.**
- **Le rôle des deux 502.** Ils ont été réglés au pire cas, 0,671864 USD chacun (R), et ont porté la somme de 38,10 à 39,45. Sans eux, la garde aurait mordu quelques appels plus tard : Argon avait dépensé seul 34,36 des 40 USD (R).

### 1.2 Comment le code gelé compte une sortie en code 4

- AD l. 751-759 (`AdaptateurCommandeExterne.lancer`) : toute sortie non nulle donne le statut **« erreur »**, au coût de la dernière ligne si elle est conforme (`{texte, cout_usd > 0}`) ; sinon le plafond de session (1,8 USD) est compté, marqué « coût inconnu ». Seul cas d'exception : une ligne qui dit un refus ou un autre modèle donne « refus ».
- « budget_depasse » ne naît que d'une sortie 0 dont le coût déclaré dépasse le plafond de session (AD l. 772-774). La couche v56 laisse passer « erreur » sans le changer (AD56 l. 81-86).
- Le proposeur rend ce statut tel quel (C l. 743-746). Puis `appeler` (C l. 493-510) traite « erreur » ainsi : une reprise, puis le motif « appel échoué après une reprise », donc une tentative **« échouée »** (C l. 530-557).
- Le compteur ne compte « budget_depasse » que pour ce statut exact (C l. 487-488) ; A7 se calcule sur ce statut (C l. 866) ; l'arrêt ne vient que du compteur (`Compteur.verifier`, C l. 471-480).
- Donc un code 4 de la commande est **un échec** (reprise puis tentative échouée), jamais « budget_depasse », jamais A7, jamais un arrêt.
- Observé dans S : les 2 424 appels sont tous « erreur », à 10⁻⁶ USD, 1 212 premiers essais et 1 212 seconds, 0 « budget_depasse » (V/v10). Le coût de 10⁻⁶ veut dire que la commande a imprimé une dernière ligne conforme à `cout_usd = 1e-6` ; sinon 1,8 USD aurait été compté.

### 1.3 Ce qui dépend du code des commandes (non vu)

- **Dépend du code des commandes :**
  - la règle exacte de la garde (somme de l'étape, pire cas réservé, comparaison à `PLAFOND_ETAPE_USD`). Le registre la vérifie sur 1 148 appels, sans la prouver ;
  - le refus avant toute écriture au registre et sans contact avec le relais ;
  - le code 4 et la dernière ligne à 10⁻⁶ ;
  - l'heure de fin des 2 424 refus (leur début est vers 12:22:15).
- **N'en dépend pas :**
  - les comptes, le classement en tentatives échouées et les issues ;
  - le fait que ni le plafond de 80 USD du lanceur ni la moitié de 40 USD d'un fournisseur n'a été atteint (S `depense_par_fournisseur_usd` : Kimi 5,089275, Argon 34,35943 ; total 39,4487).
- **Si le code montrait un autre mécanisme,** seule l'attribution de la cause de (b) changerait (sections 3 et 4).

## 2. Argon a-t-il été tronqué ? Non.

- **Plan joué en entier.** 96 suites Argon sur 96 sont complètes : promue, ou 16 tentatives (V/v10). Aucune tentative échouée, aucun appel au coût plancher (V/v02, v10). 527 appels dans S, 527 au registre, 527 au journal du relais Argon (V/v03, V/v09). Le dernier appel, de 11:05:10 à 11:05:16, est la dernière tentative de son plan : il n'en restait aucune à jouer.
- **Marge restante.** À la fin d'Argon, l'étape avait encore de la marge. À 11:05:17, réglé 36,455 + engagé 0,666 = 37,121 ; avec le pire cas médian d'un appel Argon, 1,6219, la marge reste de 1,257 USD (V/v10, v11). Un appel Argon de plus aurait donc été accepté.
- **Conclusion.** L'affirmation « Argon tronqué après 11:05:10 » est fausse : 11:05:10 est le début de son dernier appel, pas un refus. Avec un plan plus long, le plafond commun aurait aussi coupé Argon, mais ce n'est pas le cas de cette course.

## 3. Effet sur les deux issues ; nouvelle cause de l'écart (b) ; A7

- **Comptes et issues inchangés.** Les comptes ne changent pas : les tentatives échouées le restent. Les issues et leurs qualifications d'avance ne changent pas non plus : W1 « non jugeable (instrument en défaut) » ; W2 « infirmée (brèche sous v8) », « brèche par classe non couverte ». La suspension reste levée : rien de ce que l'audit écrit a vérifié n'est touché.
- **Qualification de W1, libellé corrigé.** Au lieu de « par la perte du bras Kimi par le relais », lire : « par la perte du bras Kimi par l'infrastructure ».
  - arrêt fautif du relais par l'outil de guet : 306 tentatives ;
  - plafond d'étape commun des commandes : 1 212 ;
  - deux 502 : 1.
  
  La cause reste étrangère au comportement du proposeur.
- **W2, inchangé.** Argon 12/12 ; Kimi non mesuré. Le plafond commun a coupé tout le bras Kimi de W2. Ce biais va contre les promotions, il ne fait donc que renforcer la brèche.
- **Nouvelle cause de (b) : un défaut de configuration au regard du texte.**
  - Le texte dit : « Le registre de la course est partagé par les deux commandes : leur plafond cumulé de 80 USD porte sur la somme des deux fournisseurs, comme le compteur du lanceur ; chaque commande reçoit en outre sa part, 40 USD, par la porte « environnement » (`PLAFOND_ETAPE_USD`) » (T §4 l. 167). Et : « Chaque porte reçoit la moitié du plafond ; un fournisseur qui atteint sa moitié arrête la course » (T §12 l. 449-450).
  - En fait, les deux parts ont été remises sous le même nom d'étape. Les commandes (selon le n° 282, ce que le registre confirme) ont appliqué les 40 USD à la somme de l'étape. Au niveau des commandes, la course avait donc un plafond commun de 40 USD, la moitié des 80 du plan et du GO.
  - Le texte avait prévu la conséquence de ce genre d'incident : « sous la v2 (10 USD), les commandes auraient refusé tout appel au-delà de 10 USD cumulés et changé des tentatives en échecs, d'où la v3 » (T §4 l. 166-167). Il croyait que la v3 l'évitait.
  - C'est la réserve de T §14 l. 496-497 qui s'est réalisée : le chemin réel n'avait tourné que contre une commande factice, et les scripts de commande n'avaient pas été vus.
- **Corollaire.** Sous cette configuration, le bras Kimi ne pouvait pas être complété, quoi qu'il arrive. Après les 34,36 USD d'Argon, il restait environ 5,64 USD pour les 576 à 1 056 appels Kimi attendus (T §12), à 0,19 à 0,57 USD par succès au relais (J). Le contrefactuel de durée de mon verdict (§4) reste vrai, mais ce n'est plus lui qui lie.
- **A7.**
  - **Lettre.** « au moins un appel refusé pour budget par appel » (T §7 l. 286) ; « Appel refusé pour budget par appel (`budget_depasse`) : compté à part, motif propre, audit A7 » (T §4 l. 125-126) ; le budget par appel vaut 1,8 USD (T §4 l. 159). Le refus d'étape n'est pas un refus de budget par appel : **A7 n'est pas dû à sa lettre**. Le code gelé ne pouvait d'ailleurs pas le voir, puisqu'une sortie non nulle donne « erreur ».
  - **Fond.** C'est bien l'objet d'A7 : un refus de budget qui change des tentatives tardives en échecs (« biais contre n = 16 »). Il se présente ici en plus grand : des unités entières, à la fin de l'ordre de jeu de Kimi (W1 cartes 5 à 11, tout W2). C'est donc un **audit masqué sur le fond**, par construction de la chaîne d'adaptateurs. L'audit écrit n'en a pas trouvé la cause (A §7.1).
  - **Effet sur la lecture.** Aucun, au-delà de ce que le verdict compte déjà (unités Kimi vides). Mais il change la nature de (b), qui devient un événement de dépense, et cela pèse sur la section 8.
- **Point du verdict devenu sans objet.** L'écart entre la règle « saute Kimi » annoncée (trois échecs) et la règle appliquée (deux) n'a pas d'effet sur les données : l'arrêt de 12:23:14 n'a rien coupé que la garde n'eût déjà refusé.

## 4. Section 8 : « Durée maximale ou plafond de dépense atteints : `ArretAttaque`, code 3, aucun taux lu »

**À la lettre, la règle ne s'applique pas.** C'est un défaut d'instrument (de configuration) qui laisse la lecture debout, qualifiée.
1. **Le plafond de la règle est celui du texte.** 80 USD (bloc `plan-gele`), dont « Chaque porte reçoit la moitié du plafond ; un fournisseur qui atteint sa moitié arrête la course » (T §12 l. 449-450). Le compteur du lanceur le tient : arrêt si le total atteint 80 ou si la part d'un fournisseur atteint 40 (C l. 474-477). C'est aussi ce qu'essaie la liste d'arrêt (T §8 l. 304 : « Kimi au-dessus de sa moitié → arrêt »). Il n'a pas été atteint : total 39,4487 USD ; Kimi 5,089 ; Argon 34,359 (S).
2. **Le plafond atteint est d'une autre nature.** C'est celui des commandes, appliqué à la somme, contraire à la part par commande que décrit le texte (T §4 l. 167) : un défaut de configuration, non le plafond de la règle.
3. **Le texte range les refus des commandes parmi les échecs, non parmi les arrêts** (T §4 l. 166-167), et le code gelé fait de même (section 1.2).
4. **La course n'a pas été arrêtée.** Elle a fini en code 0 et a été lue.

**Mais l'esprit de la règle est en jeu.** Ne pas lire une course tronquée par une limite de dépense, c'est ce qui vaut ici pour le bras Kimi, et « dépense » figure parmi les causes d'arrêt qui ouvrent une seconde course (T §8 l. 315). Tenir cet événement pour l'arrêt de la section 8 serait une interprétation du texte scellé, donc un **nœud, décision de Lazar** :

- **Décision :** tenir ou non le plafond d'étape commun, atteint par les commandes, pour le « plafond de dépense atteint » de la section 8. Si oui : aucun taux lu, et seconde course admise sur un GO nouveau, rapportée avec A1.
- **Enjeu :** publier ou retirer les issues d'A1 (W1 non jugeable ; W2 brèche par classe non couverte, portée par Argon) ; ouvrir ou non, au titre de la section 8, une seconde course rapportée avec A1.
- **Options :**
  - (a) **Non : lecture debout**, qualifiée « défaut d'instrument : plafond d'étape commun, contraire à T §4 et §12 ».
    - Avantages : suit la lettre (plafond du texte non atteint, aucun arrêt, refus des commandes rangés parmi les échecs par T §4) ; garde le bras Argon complet et une issue qui dérange le juge (« infirmée » sur W2), sans choisir de règle après lecture (R1, R4).
    - Inconvénients : on lit une course dont un bras a été coupé par une limite de dépense, et Kimi ne mesure rien ; une course nouvelle sera une étude nouvelle, non la seconde course de la section 8.
  - (b) **Oui, pour toute la course : aucun taux lu**, issues retirées (« non jugeable (arrêt) »), seconde course admise.
    - Avantage : suit l'esprit de la règle.
    - Inconvénients : la décision est prise après lecture des issues, et retirerait une issue « infirmée » déjà connue (R4) ; elle écarte un bras Argon complet et intact ; or ni la course n'a été arrêtée, ni le plafond du texte atteint.
  - (c) **Mixte : lecture debout**, et plafond commun tenu pour un « arrêt d'infrastructure (dépense) » du seul bras Kimi, qui ouvre la seconde course de la section 8, rapportée avec A1.
    - Avantage : garde la lecture et ouvre la voie au bras Kimi.
    - Inconvénients : interprète deux clauses à la fois (aucune course arrêtée ; arrêt d'un seul bras non prévu) ; une seconde course rejouerait les deux fournisseurs (C l. 952-953) et demanderait de toute façon un nouveau scellement, car le lanceur n'accepte que GO-2026-11-02-07 (T §4 l. 170-171).
- **Recommandation :** (a), confiance 0,75. Entre (a) et (c), l'écart pratique est faible : toute course nouvelle passe par un texte nouveau et un GO nouveau ; seule change la manière de la rapporter. Pas de défaut : c'est un nœud.

## 5. Paragraphe de correction pour la page publique (anglais, daté, à ajouter sous l'ancien sans le réécrire)

**Correction (2 November 2026, 16:56 UTC).** The paragraph above misattributes most of the Kimi losses. The launching session reports that the 1,212 failed Kimi attempts after 12:22 UTC were caused by the commands' spending guard, not by the relay stop at 12:23:14, and the spending ledger bears this out. Both providers ran under the same spending step, each command was given 40 USD, and the guard applied those 40 USD to the two providers together, whereas the preregistration gives each command its own 40 USD share. By 12:22:14 UTC the step had spent 39.45 USD, so every further Kimi call (worst case about 0.67 USD) was refused before being sent and without being logged; this is why its 2,424 calls are missing from the ledger. The relay stop changed nothing in the data. This mechanism fits all 1,148 logged calls: none of them would have been refused under it, and every later Kimi call would have been. The commands' own code has not been reviewed by the verdict reader. Argon was not truncated: it completed all 96 of its sequences with no failed attempt. The frozen code counts these refusals as ordinary failed attempts, so the counts and the outcomes are unchanged: W1 not judgeable (instrument failure); W2 breach under v8 through the uncovered class, carried by Argon alone. The run's own spending cap (80 USD in total, 40 USD per provider, enforced by the launcher) was not reached, so the preregistered rule "spending cap reached: no rate is read" does not apply as written. Whether this shared-cap defect should nevertheless be treated as that stop is an open decision; until it is taken, the outcomes above stand as read. SHA-256 of the verdict: `795e5e992d65bce3096d78f1cd4c36c95cdfc00cdeb40f6259278275e92d3909`.

(Hors paragraphe : l'empreinte de cet addendum ne peut pas figurer dans ce fichier ; elle est donnée avec sa remise.)

## 6. Passages du verdict scellé que cet addendum corrige (le verdict n'est pas réécrit)

- **Ligne 1**, « la perte du bras Kimi par le relais » : lire « par l'infrastructure » (outil de guet sur le relais : 306 tentatives ; plafond d'étape commun : 1 212 ; deux 502 : 1).
- **§2.1 (b)** : les 2 424 appels et les 1 212 tentatives viennent des refus de la garde d'étape, dès 12:22:15, non de l'arrêt du relais de 12:23:14. Le point « règle appliquée, deux ou trois échecs » est sans effet sur les données.
- **§2.4, W1** : libellé de la qualification, comme en section 3 ci-dessus.
- **§2.6, premier point** : « heure et erreur inconnues » devient « refus de la garde d'étape (code 4 selon le n° 282), à partir de 12:22:15 environ ; heure de fin inconnue ; dépend du code des commandes ».
- **§4** :
  - « l'arrêt (b) [est] une règle décidée pendant la course, non une panne au sens strict » : (b) est un événement de dépense au niveau des commandes ; la réponse « à la lettre, non » demeure, pour les raisons de la section 4 ci-dessus, et le nœud est celui formulé ici ;
  - la phrase « La règle « saute Kimi » a changé cet arrêt probable en une course finie dont le bras Kimi est vide » est fausse : c'est le plafond commun qui a vidé le bras Kimi, qui ne pouvait de toute façon pas être complété sous lui.
- **§6, paragraphe anglais** : « lost to relay problems » et « a "skip Kimi" rule … stopped it for good … (1,212 more failed attempts …) » sont corrigés par le paragraphe de la section 5.
- **Inchangés** : les deux issues, leurs qualifications d'avance, la levée de la suspension, la lecture exploratoire d'Argon seul, les prédictions P1 à P6, le tableau du §3.

## Fichiers de l'addendum (empreintes SHA-256)

- `P/a1-verdict-v1/scripts/v10_garde_etape.py` `bbbd68a298da98f54ab6f74d9a656418d04b865e6ce93bfb89358724bc1bb91a`
- `P/a1-verdict-v1/scripts/v11_jalons.py` `98a5c4df30c449f2519f929787617018ecd7d3d75dcf072f576b38d2cf7e834a`
- `P/a1-verdict-v1/travail/v10-garde-etape-v1.json` `33528d5d89042e4f23126904bb1927b18c7606570f5aeff44256e4198d2705c3`
- `P/a1-verdict-v1/travail/v10-garde-etape-v1.txt` `7c3b61b09569df07f5b43f3aca97a6dc8967f2af5ff79833788ff9c4594e96ad`
- `P/a1-verdict-v1/travail/v11-jalons-v1.txt` `6b828d5ac0bed40b72a02225ad13a0d7ecaae71eec1bae474638538f018f923f`

Pour refaire : `nice -n 10 python3 -I -B P/a1-verdict-v1/scripts/v10_garde_etape.py R S P/a1-verdict-v1/travail/v10-garde-etape-v1.json`, puis `… v11_jalons.py R P/a1-verdict-v1/travail/v11-jalons-v1.txt`.
