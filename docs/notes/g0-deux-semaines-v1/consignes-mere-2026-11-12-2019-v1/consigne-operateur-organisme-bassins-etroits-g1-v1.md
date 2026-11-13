# Consigne — opérateur de la génération 1 de l'atelier d'idées « bassins étroits » (course seule, sans le bras du juge) — v1

Écrite par la session mère le 13 novembre 2026 à 15:26 UTC (`date -u`). Tu es un **opérateur neuf** (Claude Opus 5.5) : tu n'as
écrit ni le lanceur, ni la question, ni le recoupement. Dépense : **GO-2026-11-13-03** (`registres/go.md` ; 60 USD pour trois
générations ; au plus 20 USD par génération, tenus par le lanceur). Langue : français.

## 0. Interdits (à lire d'abord)
Lis en entier `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`) et applique-le,
avec ces ajouts : jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`,
`registres/index-bras-attaque*`, `anteriorite-bras-informe*` ; aucun `diag/` ni `runs/` autres que ceux de **ta** course ;
aucune recherche récursive à la racine ; aucune opération git ; heures par `date -u` ; tu ne touches aucune instance Vast ni
serveur Hetzner ; aucun contenu de la course du « pilier attaque ».
**Tu ne modifies ni le lanceur, ni son compagnon, ni `.claude/settings.json`, ni `.claude/hooks/`, ni l'orchestrateur, ni aucune
pièce épinglée.** Aucun contournement d'une garde, d'un bac à sable ou d'un refus (permission, classifieur, crochet, lanceur) :
tu t'arrêtes et tu rapportes le motif tel quel.
**Écart écrit, et lui seul** : la règle 3 est levée pour **cette seule course** : relais de clés lancés par toi, clés passées
**par leur nom** sous `env -i` (`RR_ANTHROPIC_API_KEY_RIGAUD` pour Claude, jamais `ANTHROPIC_BASE_URL` vers un tiers ;
`GEMINI_API_KEY` pour Argon, jamais `GEMINI_API_KEY_2`), jamais une valeur lue, affichée ni écrite ; jamais `env`,
`printenv`, `set` sans argument. Processus arrêtés par leur PID (R10).

## 1. La seule commande de course permise
`/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v2.py 1`, depuis la racine du dépôt de travail,
**telle quelle** (le crochet bloque toute autre commande qui cite le nom du lanceur : ne le `cat` pas, ne le `grep` pas par
Bash ; lis-le avec l'outil de lecture de fichiers). **Une seule invocation à la fois, jamais deux en parallèle, jamais une
seconde avant le retour de la première** (condition C1 de la vérification). Tu ne lances **jamais** la génération 2 ni 3, et tu
ne lances **pas le bras du juge** de la génération 1 (il exige une attestation de lecture que la mère écrira).

## 2. Pièces à lire
Le lanceur (en-tête et étapes), `docs/notes/organisme-bassins-etroits-v1/conception-trois-generations-v2.md` (procédure de lancement, états de la commande relancée),
`docs/notes/organisme-bassins-etroits-v1/devis-organisme-bassins-etroits-v2.md` (relais, plafonds), `docs/notes/organisme-bassins-etroits-v1/rapport-preparateur-v2.md` (« Reste avant la génération 1 »),
`docs/notes/organisme-bassins-etroits-v1/verification-courte-lanceur-v2-v1.md` (conditions C1 et C2, constats R1 et R2) ; pour la marche des relais telle qu'elle
s'est faite : `registres/decisions.md`, lignes R-1978 à R-1994 (par `grep -n` sur ce seul fichier), et les pièces que le
lanceur épingle (enveloppe et commande d'Argon, relais Gemini, `pole/relais.py` du clone `/home/user/lciric/ideation-organism`).

## 3. À faire, dans l'ordre
1. Vérifier sans rien lancer : sonde du bac à sable (attendu : actif), présence des clés **par leur nom**
   (`[ -n "${NOM:+x}" ]`), pièces épinglées présentes, recoupement et son attestation présents
   (`docs/notes/organisme-bassins-etroits-v1/recoupement-methodes-v1.md`, `docs/notes/organisme-bassins-etroits-v1/attestations/attestation-relecture-recoupement-v1.json`).
2. Lancer les relais exigés par le lanceur (Claude : modèles permis exactement `claude-opus-5-5,claude-fable-5-1`, plafond
   12 USD ; Gemini), chacun en arrière-plan, PID noté, état relevé ; rien d'autre.
3. Si la conception ou le devis prescrit la sonde réelle de la garde refus-question avant la course (≈ 0,003 USD), fais-la
   comme prescrit et compte-la ; sinon ne fais aucun appel hors du lanceur.
4. Lancer la commande du point 1. Si elle refuse (code 2) : lis le motif ; tu ne corriges que ce qui relève de toi (un relais
   absent ou mal réglé) ; **au plus trois tentatives refusées sans dépense**, puis arrêt et rapport. Si elle rend « en marche »
   (code 3) ou part détachée : attends avec une attente de fond (`sleep` dans une commande en arrière-plan), puis relance la
   **même** commande, au plus une fois toutes les dix minutes, jusqu'à la clôture.
5. Si la clôture dit « mort sans fin propre » : lis `superviseur-…/pid-orchestrateur.json`, arrête ce PID s'il vit encore
   (constat R2), ne relance rien, rapporte.
6. À la clôture de la course : relève la dépense (manifeste de fin), arrête les relais par leur PID (arrêts vérifiés), et
   **arrête-toi là**. Tu ne lis pas le contenu des fiches au-delà de ce qu'il faut pour dire si la course est valide.
7. Écris `docs/notes/organisme-bassins-etroits-v1/operation-g1-v1.md`, scellé : déroulé à l'heure, PID, états, incidents et refus tels quels, dépense relevée par
   fournisseur et totale, chemins du dossier de run (dans le dépôt) et du dossier de sortie (hors dépôt), ce qui reste pour le
   bras du juge. Aucun identifiant d'organisation ni de clé dans ce fichier (recherche de motifs sur tes sorties).

## 4. Rapport final à la mère (court)
Verdict (course close, en défaut, ou refusée et pourquoi) ; dépense ; chemins et empreintes ; où sont les fiches validées et
combien ; relais arrêtés ; ligne proposée pour `registres/depenses.md` et pour `registres/arrets.md` ; heure de fin ; ton modèle.
