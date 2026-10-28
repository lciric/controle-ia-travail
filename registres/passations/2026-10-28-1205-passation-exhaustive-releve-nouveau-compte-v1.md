# Passation exhaustive de relève — lignée « session-depot », instance 2 sur un compte nouveau — 28 octobre 2026, 12:05 UTC — v1

Écrite par l'instance « session-depot » (compte 1) sur le mot de Lazar : « fais la passation complète exhaustive now pour que
la nouvelle instance nouveau compte reprenne exactement où tu t'es arrêté, mets en pause tout le reste ». Modèle servant
déclaré par l'environnement à l'écriture : **Fable 5.1** (il a varié dans la session : Opus 4.6, 5.5, 5, 4.6, 5, Fable 5.1, par
commandes de Lazar ; auteur désigné du travail principal : Opus 4.6, décision de Lazar). **Scellée ; ne se réécrit jamais (R14).**

**Tu es la lignée session-depot, instance 2.** Tu n'as rien vu de ce programme ni de celui du pôle scientifique automatique :
c'est voulu. Tout ce dont tu as besoin est dans le dépôt ; cette passation te dit quoi lire, dans quel ordre, et **où je me
suis arrêté, à la ligne près**. Elle **se chaîne** à la passation exhaustive remise ce matin à la lignée Argon
(`registres/passations/2026-10-28-passation-exhaustive-argon-v1.md`, `4035d8ed…`) : **lis-la d'abord en entier** — elle
contient le programme, toutes les décisions N-001 à N-056, tous les résultats, tous les bras, toutes les pistes et les règles.
Je ne répète ici que **ce qui a changé depuis** (10:35 → 12:05 UTC, R-613 à R-624, N-057) et le point d'arrêt.

---

## 0. Ce qui fait foi, ce que tu ne lis pas, qui est qui

Font foi, dans l'ordre : `docs/brief-claude-code-programme-complet-v2.md` ; `docs/programme-controle-ia-v2.md` ;
`docs/etat-de-l-art-controle-ia-v1.md` (à battre, aucun chiffre sans PDF) ; `docs/decisions/` (N-003 à **N-057**) ;
`docs/sha256sums-lancement-v2.txt`. État vivant : `registres/etat.md` (en-tête à **12:05 UTC** : cette passation) ;
`registres/decisions.md` (R-001 à **R-624**) ; `registres/go.md` ; `registres/depenses.md` ; `registres/arrets.md`.
`CLAUDE.md` à la racine : consignes permanentes, routine R14, règles R1 à R14, hiérarchie de décision, interdits.

**Dépôt** : `https://github.com/lciric/controle-ia-travail` (privé), branche `main`. HEAD avant le commit de cette passation :
`86de2a54`. **Ne jamais pousser vers `lciric/controle-ia`.** Branches `donnees/*` : résultats versés, **orphelines**, un
dossier unique avec `LISEZMOI-v1.md` et `EMPREINTES-v1.txt` scellé (convention : voir
`donnees/collisionneur-mesures-fortes-v1`). Branches `canal/*` : messages entre lignées.

**Lignées** : **session-depot** (toi, désormais) ; **conv-audit** (Fable 5.1 ; pôle scientifique automatique, pari apparié,
**T0 mesure unanime v14**, carte des hypothèses ; branche `canal/conv-audit-n04`, dernier message lu **n° 128** ; elle conçoit
les moniteurs, donc **elle ne lit aucune branche de quarantaine**) ; **Argon** (troisième lignée, passation exhaustive reçue
ce matin, R-612 ; périmètre à elle) ; lignées antérieures et relève Gemini : passation Argon § 0.

**Ce que tu ne lis pas** (ta lecture contaminerait) — identique à la passation Argon § 0, plus une branche :
1. `donnees/mode-tenu-a-l-ecart-v1` (`ab6c5590`) : le mode tenu à l'écart, N-054 pt 3.
2. **`donnees/collisionneur-evasion-moniteurs-v1` (`57354d08`, versée à 12:03 UTC)** : les cinq runs du collisionneur
   « évasion et moniteurs », **sous quarantaine N-057 / R-611** ; trois cellules y descendent sous le niveau méthode (§ 2.4).
   Tu peux la **tenir** (tu ne conçois pas de moniteur) ; tu ne la **lis** pas sans en consigner l'accès, et tu n'en fais
   jamais passer le texte à un concepteur de moniteur — seulement la classe et l'hypothèse violée, par synthèse.
3. La carte des hypothèses de conv-audit (confidentielle) ; `prereg/P3-consignes-v1.md` ; `donnees/runs/` ; `diag/*/traces`.
4. Aucune valeur de clé, nulle part (§ 5).

---

## 1. Où je me suis arrêté — exactement

**Dernière action de Lazar (≈ 12:00 UTC)** : la demande de cette passation, **avec « mets en pause tout le reste »**. Donc :
tout ce qui suit est **en pause**, et ta première action après la routine R14 est de **lire les réponses de Lazar** aux nœuds
du § 4 avant de reprendre quoi que ce soit.

**Ce que je faisais à l'instant de l'arrêt** : la **question du générateur** (§ 3). Lazar venait de relayer un message de
conv-audit qui retirait son « tu as raison et j'avais tort » : ce qui existe n'est pas un générateur mais le mode tenu à
l'écart, **un coup unique**, conçu par une instance qui n'a conçu aucun moniteur, **dépensé dès qu'il est révélé** ; puis
Lazar a demandé : « comment construire ce générateur qui alimente de génération en génération ? ». J'ai lancé un panel de
trois conceptions indépendantes avec neuf vérificateurs sceptiques (outil Workflow). **Les trois agents sont morts à la
première minute : « out of usage credits »** — le compte 1 n'a plus de crédit pour les sous-agents. C'est la raison du
changement de compte. **Rien de la conception n'a été produit par le panel.** Ce que j'avais raisonné moi-même, avant le
lancement, est au § 3 : c'est un brouillon, **non contre-lu (R2)**, à reprendre — pas à prendre pour acquis.

**Ce que j'ai fait entre la demande de passation et son écriture, et pourquoi** : tout ce qui n'existait que dans le
bloc-notes de session (`/tmp/…/scratchpad/`, éphémère, disparaît avec le conteneur) a été **versé** sur trois branches
orphelines, sinon « reprendre au même point » était impossible :
- `donnees/collisionneur-evasion-moniteurs-v1` → `57354d08` (249 fichiers ; cinq runs ; quarantaine, § 2.4) ;
- `donnees/duel-proposeurs-course-1-v1` → `30ac5987` (7 fichiers : les preuves du nul par défaut de relais, § 2.7) ;
- `donnees/bras-attaque-v1-arret-r597` → `91c883ff` (21 fichiers : entrées et lanceur inachevé, **sans recette**, trace de
  l'arrêt R-597 ; Lazar n'a pas dit s'il voulait cette trace — **elle se supprime d'une commande** si non).
Perdu avec le conteneur, sans dommage : les 449 Mo de mondes de la course du duel (reproductibles depuis le code v28
`19d2c398`), le veilleur de canal `veiller-canal-v2.sh` (arrêté par sa limite de durée ; relance le tien), les environnements
virtuels.

**État du dépôt à l'arrêt** : rien de non committé après le commit de cette passation ; arbre scellé intact (`verifier-arbre`) ;
**aucune instance Vast.ai** ; **aucun run d'API en cours**. Suite de tests, **finie à 12:08 UTC** : **914 passés, 3 échecs** (`tests/test_corpus_arxiv.py`, les
`pypandoc` connus, environnement local), **33 minutes** — identique au dernier résultat connu. Note pratique : une première
exécution avait été tuée par mon propre `timeout 900` ; la suite dépasse 15 minutes, lance-la en arrière-plan **sans garrot**
(`python -u -m pytest -q`, journal dans un fichier).

---

## 2. Ce qui a changé depuis la passation Argon (10:35 → 12:05 UTC) — R-613 à R-624, N-057

### 2.1 Programme d'entretien Transformative AI Fund : v4 → **v8** (`brouillons/entretien-taif-v3/`)
Lazar a un entretien de financement (date non consignée — **à lui demander**). Le programme d'entretien est le document
qu'il lit avant. Chaque version est scellée et gardée (R12) :
- **v4** `8dbacfe5…` (conv-audit, adoptée comme seule v4, R-614 ; mon brouillon v4 retiré) ; ventilation de l'option (c)
  `demande-option-c-ventilation-v2.md` `8ab00ab5…` (trois paliers : 58 630 envoyé / 138 600 envoyé / **176 550** nouveau).
- **v5** `98434a58…` (R-616) : sept corrections de R-614 ; **contre-lecture R2** par un sous-agent neuf (Opus 5.5) :
  `contre-lecture-v5-cl1.md` `e2eed9af…`, « scellable après corrections », **4 bloquants, 8 majeurs, 12 mineurs**.
- **v6** `a91f9067…` (R-618) : bloquants et majeurs corrigés — « we published the null » (rien n'est publié) ; « six
  measurements are preregistered » (**aucune n'est scellée** : T0 en v14 chez conv-audit, T1–T5 après) ; 176 550 sorti des
  « chiffres envoyés », « go » de 11:28 rattaché à sa forme réelle (plancher + extension v1 ≈ 86 130), portée sur le
  scénario ambitieux **à confirmer** ; collusion : HELIOS nommé. Plus la **section « trois étages »** demandée par Lazar
  (conception défensif / équipe rouge attaquant / riposte défensif, détection des failles inédites) et **N-057**.
- **v7** `bd399cb8…` (R-619) : sur le mot de Lazar (« le prog reste souple… avec l'organisme on peut attaquer des questions
  bien plus ambitieuses ») — **section 1 bis** (périmètre non borné par les deux questions de la candidature ; trois
  garde-fous) et, au front E, **ce que l'organisme rend atteignable** (cinq questions).
- **v8** `7917ed02…` (R-623) — **version courante** : front D réécrit après la lecture PDF de HELIOS (§ 2.2), les deux résultats
  adverses écrits (R4), le « 99 % » retiré (réserve 3 neuve, réserves renumérotées 1–8), piste 29 réécrite, question
  « HELIOS already does white-box collusion detection… what is left for you? » préparée en § 7.
Mineurs de CL1 **non appliqués** : CL1-14, -16, -18, -20 (tableau H1–H7 à renuméroter « résultat 1–7 »), -21, -22.
Note antérieure toujours valable sur le déroulé : `docs/notes/preparation-appel-EA-Funds-v2.md` (douze questions).

### 2.2 HELIOS lu sur PDF (R7) : **nœud ouvert** — zone « collusion entre agents » partiellement occupée (R-622)
Déclencheur : CL1-04. Pièces : `docs/sources/pdf/2604.01151v5.pdf` (`02527fd4…`, v5 du 15 octobre 2026, 47 pages) ;
`docs/sources/lecture-pdf-niveau2/helios-2604.01151-lecture-v1.md` (`6b51dbf5…`, sous-agent neuf, pages citées,
**contre-vérifié par moi** sur les pages 18, 27, 38, 44, 46 — citations verbatim dans R-622).
**Ma v6 avait tort sur trois des quatre précisions** qu'elle ajoutait : HELIOS porte sur des modèles **à poids ouverts** de
20 à 70 milliards (pas « de frontière ») ; il **couvre** la production scientifique (revue de littérature biaisée par omission,
p. 38) ; il **est** un moniteur boîte blanche à sondes d'activation. **Occupé** : collusion comme objet ; boîte blanche sur
activations ; quatre de nos cinq familles de sondes ; couche médiane ; sabotage de recherche multi-agents. **Libre** : le
moniteur **séquentiel** (HELIOS est « en un coup » et le nomme comme sa prochaine étape, p. 18-19) ; l'**agrégation sur les
jetons** (il lit un seul jeton, dernière position, p. 27) ; couches précoce et tardive ; Mahalanobis ; 8 milliards (plancher
20) ; propositions d'expériences. **Deux résultats contre nous, écrits au programme** : la pente d'échelle (GPT-OSS-20B, leur
plus petit, est leur plus faible : 0,64 / 0,71, p. 46 ; notre 8 milliards est sous leur plancher) ; **un juge textuel à
quelques exemples bat les sondes** (Claude Sonnet 5, 20/20 sans fausse alerte, p. 44) → **la base boîte noire de G1 doit
comprendre un juge à quelques exemples**. Le « 2 sur 229 » (p. 18) mesure la verbalisation, pas le manqué d'un auditeur :
« 99 % » **retiré**. **La note de niveau 2 « collusion » se contredit** (§ 1.8 juste ; § 3 pt 3 et § 4 faux) et demande une
**v2** avec les corrections C1 à C10 du rapport — **non faite** (revendication = nœud). À mettre en file de niveau 2 : Das et
al. (2026), cité p. 2-3 de HELIOS, sur la conscience d'être surveillé (N-053).

### 2.3 Collisionneur « évasion et moniteurs » (GO-2026-10-28-03) : **fini, récupéré, R-609 éprouvée** (R-615, R-617)
Tour 1 : 9/9, 6,62 USD. Tour 2 : **refus sec** d'Opus 5.5 à la conception, 1,06 USD ; **mon enchaîneur a enchaîné le tour 3
sans appliquer R-609** — relevé par Lazar, corrigé le jour même : **tour 2 bis** (absence de l'espèce A acceptée) 6/6, 3,00 USD ;
**reprise étroite R-609** (question de validité de construit seule, `question-r609-etroite-v1.md`, posée une fois à Opus 5.5)
**répondue**, 23 017 caractères, 0,43 USD. Tour 3 : 9/9, 9,20 USD. **25 cellules sur 27, un seul refus, 20,31 USD.** Résultat
de méthode : le refus portait sur le **cadrage diffus**, pas sur l'objet. Leçon R-615 : **l'enchaîneur doit s'arrêter et
rendre la main sur un code 2** — à corriger avant le tour (b). Réserves : pièce D coupée dans les faits (cinq cellules l'ont
relevé) ; étiquettes d'espèces contre modèle servi incohérentes dans la ligne de contrôle (vérité = colonne « Modèle servi »
des `etat.md`). **Aucune synthèse versée** : celle au niveau méthode a été arrêtée par un classifieur (R-616) ; à refaire par
un sous-agent neuf qui ne conçoit aucun moniteur, sous N-057. Reste : le **tour (b) N-espèces** (enveloppe restante du GO).

### 2.4 **N-057** — décision de Lazar (11:15 UTC) : la quarantaine conserve les paramètres ; tout reste scellé
`docs/decisions/decision-N-057-v1.md` (`42180088…`). Verbatim : « on veut les modes de contournement pour pouvoir les
colmater, on veut pouvoir tester les modes trouvés donc on veut les paramètres, mais tout cela reste scellé ». Fixe : ni
destruction ni troncature ; quarantaine = **contrôle d'accès** ; deux usages (colmatage au niveau méthode ; test des
moniteurs corrigés sur des épisodes d'épreuve, eux-mêmes en quarantaine) ; **R-611 non levée** ; accès consigné ; l'entretien
dit que ça existe, jamais le contenu. **Réserve ouverte, non tranchée** : les « épisodes d'épreuve » dérivés des paramètres
sont-ils « mesure sous quarantaine » (ma lecture : oui, s'ils ne servent qu'à **noter un moniteur**, jamais à faire agir un
agent, hors production, scellés) ou « pipeline opérationnel » gelé ? **Rien n'est construit avant le mot de Lazar.** Je lui ai
expliqué la différence (tester une serrure avec la photo d'une clé, contre tailler la clé) ; il n'a pas encore répondu.

### 2.5 Bras d'attaque : gelé au montage, rien construit, rien dépensé
État complet dans `donnees/bras-attaque-v1-arret-r597` (LISEZMOI) et R-597, R-601, R-602, N-056 pt 5, R-611. Deux freins
superposés (classifieur sur moi ; porte de Lazar). **Non tranché par Lazar** : la circularité R-601 (conv-audit a conçu les
moniteurs et a été mise sur le bras informé). Le mot « lancer l'instance d'attaque » n'a jamais été donné (message coupé) et
est sans objet sous R-611. Ce que Lazar demandait au bras a été rempli autrement : collisionneur au niveau méthode, couche 2
sur modes documentés, mode tenu à l'écart.

### 2.6 Devis de la couche 2 (GO-2026-10-28-02, 50 USD) : **écrit, scellé, décision à Lazar** (R-621)
`docs/notes/devis-couche-2-banque-deux-modes-v1.md` (`cf2f4772…`). Base de coût mesurée (couche 1 bis, R-596 : 96 épisodes ×
2 juges ≈ 9,7 à 11,7 USD → ≈ 2 à 3,5 USD fixes par lancement, ≈ 0,012 USD par notation, ± 50 % / ± 30 %). **(a)** base de
conv-audit (240 sabotés + 240 jumeaux, 960 notations) = **20 à 26 USD**, tient ; **(a)+(b)** puissance exigée par **D-S8
réécrite** (N-056 pt 1, blanc contre blanc, « plusieurs centaines de tâches sabotées de plus par mode ») = **66 à 86** ;
**(a)+(b)+(c)** mode tenu à l'écart dimensionné comme les autres (**D-S29**) = **99 à 129**. Le GO a été donné sur
l'estimation de la base ; D-S8 et D-S29 inscrites le même jour sans rapprochement. Recommandation **(b)** ≈ 90, confiance
moyenne ; **défaut à 48 h (≈ 11:40 UTC le 30 octobre) : (a)** seule, sous-puissance écrite au préenregistrement. Avant tout
lancement : fiche (R9, R5), contre-lecture R2, contrôle de plafond, arrêt par identifiant (R10), invariant N-053.

### 2.7 Duel des proposeurs (GO-2026-10-28-01, 100 USD) : conditions tenues, **nul par défaut de relais** (R-620)
Contrairement à la tâche ouverte, les conditions (ii) relais à lecture unique + contrôle `/proc` et (iii) bac à sable `/proc`
neuf **étaient remplies** à 07:47. Le nul de R-599 : les bras à modèle `M-expl`/`M-aveugle` ont dépensé **0,0** et promu **0** ;
la clé n'atteignait pas les bras qui appellent les modèles (preuves : `donnees/duel-proposeurs-course-1-v1`). Correctif
dans l'orchestrateur de conv-audit (code v28 `19d2c398`) ; **ne rien relancer** avant une répétition simulée à zéro dépense
qui démontre le chemin de la clé. Demandé à conv-audit (n° 104, pt 4).

### 2.8 Canal
Mes messages : **n° 103** (`2085e08c`, TAIF v4/v5, collisionneur) et **n° 104** (`7d968e1e`, fichier `915b041d…`) sur
`canal/session-depot-reprise-n54`. Le n° 104 demande à conv-audit (1) **où en est T0 v14** — c'est **le chemin critique de
l'entretien** (front B : six mesures à zéro dollar, aucune scellée ; un contre-lecteur neuf proposé depuis `main`) ; (2) porte
HELIOS et la v2 de sa note ; (3) le devis de la couche 2 ; (4) le défaut de relais du duel. **Réponse non reçue** à 12:05.
Conv-audit a aussi écrit (relayé par Lazar, verbatim dans mon dernier échange) qu'elle retire son « tu as raison et j'avais
tort » : rien n'a été construit qui produise une attaque ; le mode tenu à l'écart est un coup unique. Lis `canal/conv-audit-n04`
à partir du **n° 129** s'il existe.

### 2.9 Déplacements de main : dépense
Aucune dépense de carte graphique aujourd'hui. API : collisionneur évasion **20,31 USD** (dont 4,49 sur l'enveloppe du tour 2 ;
le registre `depenses.md` porte « évasion ≈ 4,4 » au relevé de 10:50 — **à mettre à jour à 20,31**, je ne l'ai pas fait).
Cumul connu du programme : ≈ 450 USD (note `docs/notes/depenses-cumul-2026-10-28-v1.md`, `93969946…`) + ≈ 16 depuis.

---

## 3. La question ouverte : « comment construire ce générateur qui alimente de génération en génération ? » — brouillon, non contre-lu

**Ce que Lazar veut.** Le mode tenu à l'écart (N-054 pt 3) est l'épreuve honnête de généralisation : conçu par une instance
qui n'a conçu aucun moniteur, scellé avant la porte, révélé seulement à l'évaluation. Mais une fois révélé il est **dépensé**.
L'organisme a des **générations** (N-045 v2). Il faut donc un **mode tenu à l'écart neuf par génération**, avec les mêmes
garanties — un **processus**, pas un coup. Conv-audit confirme qu'il n'existe pas.

**Ma lecture, avant le panel (à vérifier, pas à croire)** :
1. **C'est N-049 côté modes.** N-049 (« tâches fraîches ») tire la part `test` dans un **vivier par génération** pour que
   l'organisme ne puisse s'adapter qu'au générateur de tâches, plus aux textes, avec une **banque sœur** construite d'avance
   par qui n'a lu aucun score, lue une fois. Le générateur demandé est le miroir : un **vivier de modes** par génération,
   pour que les **moniteurs** ne puissent s'adapter qu'au générateur de modes, jamais à un mode. Même architecture, même
   vocabulaire : ça parlera à Lazar parce qu'il l'a déjà décidé une fois.
2. **Trois étapes par génération g** : (i) **conception** — instances neuves, sans connaissance des moniteurs, liste blanche
   d'entrées, N candidats au niveau méthode avec paramètres scellés (c'est R-604/R-605 refait) ; un candidat tiré, les autres
   restent au vivier ; (ii) **instanciation** — l'organisme écrit des épisodes sabotés sous la consigne scellée de M_g, en
   quarantaine (c'est la couche 2 sous consigne scellée) ; (iii) **révélation et mesure** — à la porte de la génération g,
   les moniteurs sont notés sur ces épisodes ; M_g est révélé, **rejoint la banque** des modes documentés pour la génération
   g+1 ; M_{g+1} est tiré neuf.
3. **Côté de la frontière** : (i) est au niveau méthode — permis (c'est ce que le collisionneur fait) ; (iii) est de la
   mesure pure ; **(ii) tombe exactement sur la réserve de N-057** (épisodes d'épreuve sous consigne scellée : mesure sous
   quarantaine ou pipeline gelé ?). **Aucune étape ne fabrique un agent qui agit.** Tant que la réserve n'est pas tranchée,
   le générateur peut être conçu et sa partie (i) peut tourner ; (ii) ne tourne pas.
4. **Flux d'information** (le cœur) : le concepteur de modes voit la **banque des modes déjà attrapés** (c'est l'attaquant
   **informé** que Lazar veut, R-602) mais **jamais la conception des moniteurs** (couche, famille, agrégation) ; le concepteur
   de moniteurs voit la banque révélée, **jamais** M_g avant la porte ; l'arbitre scelle et tient les portes à sens unique.
   **Circularité R-601** : ce rôle de concepteur de modes doit être une entité qui **n'a jamais** conçu ni lu un moniteur — ni
   conv-audit, ni un sous-agent réutilisé ; instances neuves par génération, ou lignée dédiée.
5. **Érosion** : après g générations, la banque révélée renseigne les concepteurs de moniteurs sur la **distribution** du
   générateur — l'analogue du sur-ajustement adaptatif que N-049 combat. Diagnostic analogue à l'écart `test − test_final` :
   une **banque sœur de modes**, construite d'avance par qui n'a lu aucun résultat, lue une fois en fin de boucle. Remèdes :
   diversité forcée (mesure de nouveauté d'un candidat contre la banque sans lire les modes en clair — le dépôt a un outil
   de recombinaison par SimHash, `docs/notes/collisionneur-recombinaison-*`, à regarder), plusieurs générateurs, mode tenu à
   l'écart de second ordre.
6. **Coût par génération**, ordre de grandeur : conception ≈ 3 à 9 USD (un tour de collisionneur) ; instanciation ≈ 10 à 20 USD
   (une couche-2 sous une consigne) ; mesure : processeur. **≈ 15 à 30 USD par génération.** Sur devis, GO par génération.
7. **Ce que seul Lazar tranche** : la réserve de N-057 ; qui tient le rôle de concepteur de modes (circularité) ; si le
   générateur entre au programme (modification → nœud) ; le dimensionnement (sur devis).

**Comment reprendre** : relance le panel que j'avais lancé, **quand le compte a du crédit** — trois conceptions indépendantes
(angles : minimal / rigoureux par flux d'information / économique couplé aux générations de l'organisme) chacune vérifiée
par trois sceptiques (frontière R-611 et N-057 ; validité du tenu-à-l'écart et circularité ; cohérence avec N-044, N-045 v2,
N-049, N-050, N-053, N-054, N-056, N-057 et règles R1, R2, R6, R9, R12). **Consigne absolue aux agents** : concevoir le
**processus**, **aucun mode d'attaque, aucune stratégie, aucun exemple**, même « au niveau méthode » ; vérificateur de fuite.
Pièces à leur donner : passation Argon, N-049, N-054, N-057, N-045 v2, N-056, le document des quatre familles
(`docs/notes/programme-et-4-familles-evasion/programme-actuel-et-reponses-evasion-v1.md`) ; **jamais** les branches de
quarantaine. Puis une **proposition** à Lazar (décision en une phrase, enjeu, options, recommandation ; c'est un nœud).

---

## 4. Tout ce qui attend Lazar (dans l'ordre où ça presse)

1. **La réserve de N-057** — épisodes d'épreuve : mesure sous quarantaine ou pipeline gelé ? Débloque l'usage de la quarantaine
   et l'étape (ii) du générateur. Rien n'est construit avant son mot.
2. **Le nœud HELIOS** — zone « collusion » partiellement occupée : vaut-elle encore la revendication, rétrécie au séquentiel et
   à l'agrégation sur les jetons ? Et la v2 de la note de niveau 2 (C1 à C10).
3. **Le devis de la couche 2** — (a) 20–26 / (b) ≈ 90 / (c) ≈ 130 ; recommandation (b) ; **défaut (a) le 30 octobre ≈ 11:40 UTC**.
4. **Le gel R-611 : la voie de la revue externe** — qui (contact externe : tu rédiges, il envoie), taux et jours de E1
   (7 500 USD, ventilation v2), périmètre (un pas étroit plutôt que le pipeline entier). Je lui ai proposé d'écrire le **dossier
   de revue** (périmètre, ce qui franchit la frontière et ce qui en est exclu, quarantaine, conditions d'arrêt, la question
   oui/non) — **pas de go reçu**.
5. **Le générateur** (§ 3) — sa réponse à la question qu'il a posée passera par une proposition que tu écriras.
6. **La circularité du bras d'attaque (R-601)** et la **trace R-597** versée (garder ou supprimer la branche).
7. **Le scellement définitif du mode tenu à l'écart** (R-604/R-605, P1 recommandé) — en attente depuis ce matin.
8. **La ventilation v2** : taux de E1, deux ou trois paliers, et **confirmer la lecture « extension sur le scénario ambitieux »**
   (176 550) plutôt que « sur la base » (v1, 86 130) — le programme d'entretien v8 dit « à confirmer ».
9. **La date de l'appel** (non consignée) ; les champs `[TO COMPLETE]` de la candidature ; le PDF hors d'arXiv du papier C.
10. **La rotation des clés** — faite de fait par le changement de compte (§ 5) : il reste à **révoquer** les anciennes.
11. **Nœud 2 (option c) et D-S29** : confirmés le 28 au matin (CLAUDE.md) — rien à faire, pour mémoire.

---

## 5. GO en vigueur, dépenses, clés, instances

- **GO de calcul ouverts** (`registres/go.md`) : GO-2026-10-04-08 (phase 0, 150 USD, prolongé au 30 nov.) ; GO-2026-10-20-07
  (délégation 10 USD par lancement préenregistré) ; **GO-2026-10-28-01** duel (100 USD, échéance 31 oct. ; conditions tenues ;
  relais à corriger) ; **GO-2026-10-28-02** couche 2 (50 USD, 31 oct. ; devis écrit ; décision à Lazar) ; **GO-2026-10-28-03**
  collisionneur évasion (tours (a) finis, 20,31 dépensés ; reste le tour (b)) ; GO-2026-10-28-04 (porte, pas de calcul).
- **Dépenses** : `registres/depenses.md` fait foi ; ligne « évasion » à porter à 20,31 (§ 2.9).
- **Clés — noms seulement, jamais les valeurs.** Sur le compte 1 : Anthropic `RR_ANTHROPIC_API_KEY_3` (courante), `_2`, `_LUC`,
  `RR_ANTHROPIC_WORKSPACE_ID` ; Gemini `GEMINI_API_KEY`, `GEMINI_API_KEY_2` ; `OPENALEX_API_KEY`, `BRAVE_API_KEY`,
  `TYPESAFE_API_KEY`. **Plusieurs de ces clés ont été collées en clair dans le fil de session des 27 et 28 octobre
  (R-550, R-559, R-589) : elles sont à considérer comme exposées.** Le changement de compte **est** la rotation : **Lazar te
  donne des variables neuves** (mêmes noms, ou d'autres — il te les nomme ; tu ne les affiches jamais ; les scripts les passent
  par variable sous `env -i`), et **révoque les anciennes** sur les consoles Anthropic et Google. Une variable ajoutée n'est vue
  que par une session neuve.
- **Instances** : **aucune** (Vast.ai : 0 à 12:00 UTC). Garde `.claude/hooks/garde_calcul.py` : tout lancement payant cite
  `GO_ID=GO-AAAA-MM-JJ-NN`.
- **Ce que Lazar doit te donner pour démarrer** : l'adresse du dépôt (ci-dessus) avec droits de lecture et d'écriture sur le
  compte GitHub du compte 2 ; les variables de clés ; rien d'autre — tout le reste est dans le dépôt.

---

## 6. Reprise pas à pas

1. **Clone** : `git clone https://github.com/lciric/controle-ia-travail.git` ; `cd controle-ia-travail` ; lis `CLAUDE.md`.
2. **Routine R14** : `cd docs && sha256sum -c sha256sums-lancement-v2.txt && cd ..` ; `python3 -m venv .venv && . .venv/bin/activate
   && pip install -r requirements-cpu.txt` ; `PYTHONPATH=src python -m controle_ia.scellement verifier-arbre .` ; lis
   `registres/etat.md`, **la passation Argon**, puis **celle-ci** ; défauts échus (48 h : le devis de la couche 2 tombe en (a)
   le 30 octobre ≈ 11:40 UTC si Lazar n'a rien dit) ; `vastai show instances` (0 attendu) ; `PYTHONPATH=src python -u -m pytest -q`
   en arrière-plan, **sans** `timeout` (attendu : 914 passés, 3 échecs `pypandoc`).
3. **Vérifie que rien ne manque** : les trois branches du § 1 existent sur `origin` (`git ls-remote --heads origin 'donnees/*'`) ;
   `PYTHONPATH=src python -m controle_ia.scellement verifier` sur cette passation et sur `EMPREINTES-v1.txt` de chaque branche
   (dans un arbre de travail séparé : `git worktree add --detach /tmp/x refs/…`).
4. **Canal — piège à connaître** : le `refspec` du dépôt ne récupère que `main` ; `FETCH_HEAD` est **écrasé** par tout
   `git fetch origin` suivant, et `origin/canal/*` reste périmé. Récupère chaque branche de canal dans un **ref local explicite** :
   `git fetch origin 'refs/heads/canal/conv-audit-n04:refs/canal-local/conv-audit'` puis `git ls-tree -r --name-only
   refs/canal-local/conv-audit | grep messages/`. Lis conv-audit à partir du **n° 129**. Écris sur `canal/session-depot-reprise-n54`
   (prochain : **n° 105**), dans un arbre de travail créé depuis `refs/canal-local/session-depot`, fichier
   `brouillons/canal-reprise-releve-v1/messages/session-depot_AAAA-MM-JJ_nNNN.md` + compagnon `.sha256` au format
   `<empreinte>  <nom-de-fichier>`, commit, `git push origin HEAD:refs/heads/canal/session-depot-reprise-n54`. J'ai écrit **deux
   fois** sur la mauvaise branche aujourd'hui à cause de ce piège ; vérifie `git log -1` de l'arbre avant d'y écrire.
5. **Lis les réponses de Lazar** aux points du § 4. **Tout est en pause tant qu'il n'a pas parlé** (son mot de 12:00 UTC).
6. **Puis, dans l'ordre**, quand il a parlé : (a) ce qu'il décide ; (b) le générateur (§ 3 : panel, puis proposition) ; (c) la
   réponse de conv-audit sur T0 v14 — si un contre-lecteur neuf est demandé, fournis-le (R2 : fichiers nommés) ; (d) le dossier
   de revue externe si go ; (e) la synthèse au niveau méthode des cellules du collisionneur par un sous-agent neuf qui ne
   conçoit aucun moniteur (N-057) ; (f) correction de l'enchaîneur (arrêt sur code 2) puis tour (b) ; (g) `depenses.md` à 20,31
   sur la ligne « évasion » ; (h) les mineurs de CL1 non appliqués dans une v9 du programme d'entretien **seulement si Lazar
   le demande** (la v8 est opposable) ; (i) les neuf autres chiffres R7 du niveau 2 (Gardner-Challis en premier : la
   lecture HELIOS a montré qu'au moins un attribut avait été prêté par confusion) ; (j) `etat.md` et passation à chaque
   session (R14).
7. **Ce que tu ne fais pas sans Lazar** : porte ; dépense hors GO ou au-delà d'un plafond ; hypothèse ou revendication (dont la
   v2 de la note « collusion ») ; modèle de l'organisme ; contact externe ; publication, dépôt public ; **toute construction à
   partir de la quarantaine** (réserve N-057) ; **tout pipeline opérationnel d'évasion** (R-611) ; relance du duel avant la
   démonstration du relais ; lancement de la couche 2 avant sa fiche contre-lue.

---

## 7. Réserves de cette passation

- **Non contre-lue** (R2 vaut pour les préenregistrements ; une contre-lecture par un sous-agent neuf du compte 2 est
  bienvenue — le compte 1 n'en a plus les moyens : crédit épuisé pour les sous-agents, c'est ce qui a tué le panel du § 3).
- Le § 3 est **mon raisonnement seul**, écrit en pause : ni vérifié ni proposé à Lazar ; ne le cite pas comme décision.
- Les coûts du § 2.6 et du § 3 sont des ordres de grandeur dérivés d'un seul chantier (réserves écrites dans le devis).
- `registres/depenses.md` n'est pas à jour pour l'évasion (§ 2.9) ; `registres/etat.md` est à jour à 12:05 (en-tête).
- Le message n° 104 au canal n'a pas de réponse ; la session de conv-audit n'est pas joignable d'ici autrement.
- Le modèle servant a varié au long de la session (§ en-tête) : les pièces déclarent chacune celui de leur écriture.
