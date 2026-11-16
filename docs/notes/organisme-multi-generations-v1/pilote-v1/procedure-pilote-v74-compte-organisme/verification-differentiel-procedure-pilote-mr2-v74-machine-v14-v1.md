# Vérification du différentiel v13 → v14 de la procédure du pilote MR-2 sur machine louée (sans ssh) — v1

- **Lecteur** : vérificateur neuf (R2), auteur d'aucune des pièces. Écrit le 2026-11-16, de 03:04Z à 03:30Z (`date -u`).
- **Pièces lues** (branche `lot/compte-organisme-v1`, commit `2d35cafa467277aa5ffd1eab2f37a3267b5d0b21`, par `git show` et `git diff`) :
  procédure v14 `2035562740efe1e87db9ffa2f0494705bb5117c56069309ece2279d351bde18a` (égale au compagnon) ;
  outil v4 `7de3f27fe794e96c128d644aa7ebdc514952adf4bdb875803c3596d143482de4` ; inchangés : aide de l'outil `sans-ssh-v3/session_pilote_mr2_v74_v3.py`
  `ff76b34a4e64c56455cebea781784a0c08894f677f6432886e487a37273b9a64`, et dans `sans-ssh-v2/` l'amorce `93b9c50de967c3da…`, le programme machine
  `4fa7d36833120534…`, son aide `8af383f9e894256b…` ; `sans-ssh-v4/essais/`. Référence v13 : commit `2719dcb8320287ebc88cb648175a707a56d37729`
  (procédure v13, outil v3 `0341fbef…`). Sur `main` (`e83bcbfc`) : vérification de la v13 (`9f0bbd0ec1649dbe…`, K1 à K9), consignes de la mère pour
  la v13 (`8bc7d81ad415f48c…`), R-2962 de `registres/decisions.md`, lignes GO de `registres/go.md`, fin de `registres/arrets.md`.
- **Fait sans dépense ni appel** : aucun appel au loueur, aucune création, aucune clé lue ni affichée (noms seuls), aucune pièce modifiée, rien
  committé. Seuls `sans-ssh-v2/`, `-v3/` et `-v4/` ont été extraits, par la commande de la section 1, dans un dossier d'envoi factice neuf du
  bloc-notes ; aucun dossier `/home/user/pilote-mr2-v74-envoi*` touché ; le jeu en cours (PID 5755 et enfants) laissé en paix.

## Verdict

**Jouable sous consignes** (liste à la fin, V1 à V6). Empreintes égales aux annonces ; seul changement de code : l'étiquette exigée (plus le
chemin de l'aide, rendu nécessaire par le déplacement) ; la forme de la création est identique à l'octet hors noms et le crochet la laisse
passer ; noms neufs absents à distance ; essais rejoués aux mêmes fins que les résultats scellés. Deux points de texte demandent une
consigne : **K6 n'est pas porté fidèlement** (« sinon elle attend le mot de Lazar » est rattaché à l'impression, alors que les consignes de
la mère disent « la commande n'est pas imprimée après 03:40Z » et rattachent le mot de Lazar au **feu du pilote réel**) ; la section 12
undecies omet quelques retraits mineurs, dont un, à la section 13, qui donne pour éprouvée l'autodestruction par la minuterie, qui n'a pas
joué. **Horaire** : à l'heure de ce rapport, la fenêtre de K6 sous l'autonomie en cours (GO-2026-11-15-07) se ferme à **03:40Z**.

## 1. Différentiel réel contre la section 12 undecies

**Procédure** (`diff` v13 → v14 : 109 lignes ajoutées, 56 retirées). Chaque changement a été rapproché de la table :

| changement trouvé | ligne de la table | constat |
|---|---|---|
| titre, « Pourquoi une v14 », versions, table des pièces (outil v4, aide v3 inchangée, essais v4) | outil de la session ; noms neufs | conforme |
| en-tête : la session qui lance est la session mère `session_016QhUrtmLyFWJP6Cy7rgfXH` et son opérateur, dossier d'envoi sur sa machine ; retrait de « crochet vérifié chargé » de l'en-tête (repris en 2.1 avec K9) | qui lance ; K9 | conforme (le déplacement n'est pas dit, sans effet) |
| lignes : GO-2026-11-15-08 « tenu par la mère pour valoir pour la v13, et pour la v14 — lecture de la mère à confirmer » | K2 | conforme ; **la confirmation reste à écrire** (V5) |
| section 0 : `ENV=…-envoi-v14`, `BS`, `BE` en `-v14`, `OUTIL` vers `sans-ssh-v4/` (aide dans `sans-ssh-v3/`, amorce dans `sans-ssh-v2/`) | noms neufs ; outil | conforme |
| section 0 : ordre des états finaux | K3 | conforme |
| section 0, exposition : retrait de la phrase « 05:39Z / 22:39Z (GO-2026-11-15-03) […] puis la session ou Lazar par la console » ; fin de l'autonomie 08:13Z ; rappel dès la création ; à défaut, Lazar par la console (la mère n'est plus son propre repli) | K2 (retrait déclaré) ; C1 ; K7 | conforme |
| section 1 : trois occurrences du dossier, extraction des trois dossiers, empreinte de l'outil v4, `variables.sh` | noms neufs ; outil | conforme |
| 2.1 crochet éprouvé par l'opérateur | K9 | conforme |
| 2.2 crédit au moins 5 USD, une seule machine | K8 | conforme |
| 2.4 étiquette `pilote-mr2-v74-v14-…` ; 2.5 (i) `calcul/essai-poussee-session-v3` | noms neufs | conforme |
| 2.5 (ii) fenêtre seule ; **retrait** de la parenthèse « la mère ne crée ni ne détruit de machine du loueur d'ici la preuve d'absence » | K4 | remplacée par une règle plus large ; retrait non dit (d2, sans effet) |
| 2.6 mot de Lazar daté de moins de dix minutes ; horaire ; identifiant, étiquette, échéance donnés dès la création | condition neuve ; K6 ; K7 | voir section 2 (K6 infidèle) |
| 5.2 phrase tapée dans la session qui lance, jamais relayée ; injoignable dans la demi-heure : nœud | K1 | conforme |
| 11.1 « instance peut-être déjà absente », `detruire` seulement si « toujours listée » ; **retrait** de la parenthèse « (destruction par la minuterie ou par l'amorce) » | K5 | conforme ; retrait non dit (d2, sans effet : les cas sont élargis, pas restreints) |
| 11, à l'échéance ou dès la fin : rappel, états finaux, « noeud, machine gardee » au mot de la mère | K3 ; K7 | conforme |
| 12 : mention de la section 12 decies inchangée ; section 12 undecies ajoutée | — | conforme |
| 13 : essais v4 (39 cas, 17 scénarios, intégral 1058 s) | outil | conforme, mais non déclaré dans la table (d2) |
| 13 : **retrait** de la liste « Non éprouvés » de la v13 (création et lecture de `--env` et `--args`, image sur hôte à carte, **interface d'autodestruction du loueur**, clonage par jeton), remplacée par « Éprouvé chez le loueur par la tentative v13 » | aucune | **retrait non déclaré** (d1) : la table dit « rien d'autre ». Sur le fond, création, image, clonage, minuterie armée sont bien attestés par R-2962 ; **l'autodestruction à l'échéance n'a pas joué** (machine détruite par identifiant à 02:32:15Z, bien avant l'échéance) : elle doit rester « non éprouvée » ; le `LISEZMOI.md` des essais v4 la garde d'ailleurs dans « ce que les essais ne prouvent pas » |

**Outil** (`diff` v3 → v4, quatre endroits) : en-tête et commentaire de version ; `aide()` appelle désormais
`$ICI/../sans-ssh-v3/session_pilote_mr2_v74_v3.py` (conséquence nécessaire du déplacement de l'outil, l'aide n'étant pas copiée) ;
étiquette exigée `pilote-mr2-v74-v14-[0-9]{8}`. Les lignes `L1=` et `L2=` (commande de création) sont identiques à l'octet entre v3 et v4.
Aucune autre ligne ne change. `sans-ssh-v2/` et `sans-ssh-v3/` : aucun changement entre les deux commits (`git diff --stat` vide).

**Empreintes** : les cinq pièces jouées, recalculées sur `git show` au commit `2d35cafa`, sont égales aux annonces et aux compagnons ;
tous les compagnons de `sans-ssh-v4/essais/` vérifiés : OK.

**Extraction de la section 1**, jouée telle qu'écrite (seuls `ENV`, remplacé par un dossier factice neuf du bloc-notes, et `CL`, rempli par
`2d35cafa…`, diffèrent ; la récupération par `git fetch` avec refspec) : « CL sur la branche du lot », cinq `OK`, code 0, `variables.sh`
écrit (`BS`, `BE` en `-v14`, `OUTIL` vers `sans-ssh-v4/`). **L'outil v4 trouve son aide et l'amorce** : `$OUTIL offre` sur un fichier absent
puis sur une recherche vide rend les refus de l'aide v3 (code 2, messages de l'aide), et le chemin `AMORCE` de l'outil se résout sur
`outil/sans-ssh-v2/amorce_pilote_mr2_v74_v2.sh` présent.

## 2. K1 à K9 et la condition neuve

| consigne (vérification v13 / consignes de la mère) | v14 | constat |
|---|---|---|
| K1 phrase tapée dans la session qui lance | 5.2 | fidèle, sans ambiguïté |
| K2 autonomie 08:13Z, 22:39Z caduque, GO-2026-11-15-08 tenu | 0, lignes | fidèle ; la tenue de GO-2026-11-15-08 pour la v14 est dite « à confirmer » par la mère (V5) |
| K3 ordre des états finaux | 0, 11 | fidèle. Reste : « au mot de la mère » alors que la session qui lance **est** la mère ; à lire « par décision de la mère, au plus tard échéance + 5 min » (sans effet) |
| K4 fenêtre seule | 2.5 | fidèle (élargie à toute session du programme) |
| K5 instance peut-être absente | 11.1 | fidèle |
| **K6 horaire** | 2.6 | **infidèle** : voir ci-dessous (V1) |
| K7 fermeture sans minuterie | 0, 2.6, 11 | fidèle ; petite contradiction : la section 0 dit « l'identifiant, l'étiquette et l'échéance donnés dans le préavis », alors que le préavis précède la création ; 2.6 dit justement « dès la création » (V4) |
| K8 crédit | 2.2 | fidèle |
| K9 crochet | 2.1 | fidèle |

**K6.** Vérification v13 : « imprimer la commande au plus tard vers 03:40Z […] ; sinon ne pas lancer ». Consignes de la mère : « Le feu du pilote
réel est donné avant 08:13Z ; sinon il attend le mot de Lazar. La commande n'est pas imprimée après 03:40Z. » La v14 écrit : « la commande
**n'est pas imprimée moins de 4 h 30 avant la fin de l'autonomie** (au 16 novembre : pas après 03:40Z) ; **sinon elle attend le mot de
Lazar** ». Trois effets : (a) l'interdit d'impression après 03:40Z devient une attente levable par « le mot de Lazar », sans dire lequel —
le mot de présence de 2.6, donné de toute façon, pourrait être lu comme suffisant ; (b) la règle de la mère sur le **feu du pilote réel**
(« attend le mot de Lazar » après 08:13Z) n'est plus écrite à K6. **Sous une autre ligne d'autonomie**, la formule « fin de l'autonomie en
cours » reste juste (le calcul 4 h 30 se transpose). **Hors autonomie** (autonomie finie, aucune ligne neuve) : la règle de K6 n'a plus de
terme et ne dit rien ; le seul texte qui couvre le feu du pilote réel est C1 (section 0, exposition) : « après la fin de l'autonomie […] elle
ne lance, ne relance et ne prolonge rien d'autre ; toute autre décision attend Lazar » — lu ainsi, **le feu 3 et le feu de relance
attendent le mot de Lazar**, mais seulement par déduction, la section 6 (barrière 3) et la table de la section 10 ne posant aucune
condition d'autonomie. Consigne V1.

**Condition neuve du point 2.6** (mot de Lazar tapé dans la session mère, daté de moins de dix minutes par `date -u` dans la session mère,
disant qu'il est présent pour la demi-heure qui suit ; sinon rien n'est imprimé ni loué) : bien placée (avant le préavis et l'impression),
conforme à la règle retenue en R-2962 (« aucune création du pilote sans ce mot dans les minutes qui précèdent »). Deux précisions utiles :
« daté » ne peut se lire que par un `date -u` joué par la session mère au premier geste qui suit le mot (le message lui-même ne porte pas
d'heure lisible par programme), puis de nouveau juste avant l'impression, l'écart devant rester sous dix minutes (V2) ; le mot doit
être tapé par Lazar dans la session mère, non relayé (même règle que K1) — le texte dit « tapé dans la session mère », ce qui suffit. La
chaîne mot → impression (≤ 10 min) → création (≤ 10 min) → `attente du feu 1` (≈ 1 à 4 min en v13 : 01:02:40Z → 01:03:53Z, demande à
01:06Z) tient dans la demi-heure annoncée, mais de peu ; mieux vaut que le mot couvre l'heure de délai de la machine (V2).

## 3. Commande de création et crochet

Le point 7 de la section 2 est **identique à l'octet** entre v13 et v14 (`diff` vide sur le point entier) ; les lignes `L1=`/`L2=` de l'outil
sont identiques entre v3 et v4 ; les noms (étiquette, branches, dossier) n'y entrent que par variables. **Crochet**
(`/home/user/controle-ia-travail/.claude/hooks/garde_calcul.py`, `73be0638…`) appelé avec une entrée JSON factice (bloc entier de la section
2, point 7 : préambule, document `a-jouer.txt` aux deux lignes de la forme imprimée par l'outil v4, `comparer` puis `.` ; rien exécuté) :
cas sain `GO_ID=GO-2026-11-14-14` → **0** ; artefacts : sans `GO_ID` → 2 ; GO de type « décision » (GO-2026-11-15-08) → 2 ; GO inconnu → 2.
Un quatrième artefact (arrêt par motif) n'a pas pu être soumis : le crochet de ma propre session a bloqué la commande qui en portait le
texte (incident, section 6) ; il n'est pas propre à la v14.

## 4. Noms neufs

`git ls-remote --exit-code origin refs/heads/…` : `calcul/pilote-mr2-v74-sortie-v14` → 2, `calcul/pilote-mr2-v74-entree-v14` → 2,
`calcul/essai-poussee-session-v3` → 2 (absentes ; pour contrôle, `…-sortie-v13` et `calcul/essai-poussee-session-v2` → 0, consommées).
`test -e /home/user/pilote-mr2-v74-envoi-v14` → 1 (absent).

## 5. Essais rejoués (sans réseau extérieur ni clé)

Joués depuis la copie extraite de `sans-ssh-v4/essais/`, `ESSAI_DEPOT=/home/user/controle-ia-travail`, dossiers jetables du bloc-notes.

- **Outil v4** : 39 cas sur 39 conformes, `tout_conforme` vrai ; mêmes noms de cas et mêmes verdicts que `resultats-essai-outil-session-v4.json` ;
  les cinq détails qui diffèrent ne diffèrent que par les commits du banc et le chemin de la copie (offre, étiquette `pilote-mr2-v74-v14-20261116`,
  commande, branche `calcul/essai-poussee-session-v3` identiques). Empreintes d'outil et d'aide portées : `7de3f27f…`, `ff76b34a…`.
- **Scénarios rapides** : 17 sur 17 conformes (553 s) ; mêmes fins (étape et motif, heures ôtées) que `resultats-essai-amorce-v4.json` sur chacun ;
  empreintes amorce, programme, aide, outil égales ; seuls les commits synthétiques du banc diffèrent (attendu).
- **Scénario intégral** (vrai lanceur v74, joué la charge de la machine étant d'environ 2 sur 4 processeurs) : conforme, `fini`, 742 s (scellé : 1058 s), 248 fichiers poussés, aucune fuite, aucun nom interdit ; mêmes empreintes de pièces ; différences attendues seulement (heures, échéance, PID de la minuterie, commits du banc, empreinte du fichier des mondes, tirés d'un secret neuf).

## 6. Clés, intouchables, incidents

- **Clés** : la v14 et l'outil v4 ne portent que les noms (`CONTROLE_IA_GITHUB_TOKEN_2`, `RR_ANTHROPIC_API_KEY_RIGAUD`, `GEMINI_API_KEY`,
  `OPENAI_API_KEY`, `GH_TOKEN`) ; aucune forme de valeur trouvée dans la procédure. Les essais emploient des valeurs factices qui remplacent
  les noms dans l'environnement des enfants.
- **Intouchables** : liste inchangée (58936096, 58936099, 58936100, 60480302, 60599797, 60670453), identique à celle de l'aide v3 ; aucune
  commande n'en nomme une. Pour information : selon `registres/arrets.md` (00:47Z et 02:32Z), seules 58936096, 58936099 et 58936100 sont encore
  listées ; l'inventaire d'avant aura donc trois témoins.
- **Incidents de ma main** : (i) premier lancement de l'essai de l'outil refusé par le banc parce que j'avais créé d'avance son dossier
  jetable (« File exists ») ; dossier vide retiré, relancé : sans effet. (ii) Le crochet de ma session a bloqué une commande d'essai qui
  contenait le texte d'un arrêt par motif (dans une chaîne de test, rien n'était exécuté) ; non contourné : le cas a été retiré, et le
  programme d'essai du crochet a été écrit par l'outil d'écriture de fichier puis joué. Aucun autre.

## Consignes (pour la session mère)

- **V1 — K6 tel que les consignes de la mère le disent.** Sous l'autonomie en cours (GO-2026-11-15-07, fin 08:13Z) : **aucune impression après
  03:40Z**, le mot de présence de 2.6 ne levant pas cet interdit ; une impression plus tardive demande un mot de Lazar qui l'autorise
  nommément (horaire décalé), ou une ligne d'autonomie neuve. Le **feu du pilote réel** (et celui de relance) après la fin de l'autonomie, ou
  hors de toute autonomie : seulement sur un mot de Lazar tapé dans la session mère ; sans lui, `feu-arret` ou délai laissé courir (arrêt (A)),
  puis section 11.
- **V2 — Datation du mot.** `date -u` joué par la session mère au premier geste après le mot de Lazar, consigné, puis juste avant
  l'impression ; écart de plus de dix minutes : rien n'est imprimé. Demander à Lazar d'être présent pour l'heure (délai de la phrase), non la
  seule demi-heure ; impression et création aussitôt après le mot.
- **V3 — Section 13.** Tenir l'**autodestruction du loueur à l'échéance pour non éprouvée** (la minuterie a été armée en v13, elle n'a pas
  agi) : le rappel à l'échéance + 5 minutes (K7) et la section 11 restent le moyen sûr de fermeture.
- **V4 — Identifiant pour Lazar.** Message à Lazar dès la création (identifiant, étiquette, échéance), le préavis ne pouvant pas les porter.
- **V5 — GO-2026-11-15-08 pour la v14.** La mère écrit sa lecture (tenu pour valoir v14), par exemple dans des consignes pour la v14, avant le
  préavis.
- **V6 — Différentiel incomplet** (d1, d2) : à noter dans la prochaine version ; sans effet sur le jeu, aucune pièce n'est à refaire.
