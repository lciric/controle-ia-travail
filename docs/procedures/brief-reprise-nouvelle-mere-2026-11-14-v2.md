# Brief de lancement de la nouvelle session mère, sur un nouveau compte (14 novembre 2026, v2 — à coller)

Brouillon écrit par la mère sortante `session_01QPDgKgACWyCkCN8HjqwNXy` le 14 novembre 2026, sur le mot de Lazar : « prepare
la passation a un nouveau compte quand tu auras atteint 97% de la limite hebdomadaire d'utilisation » (R-2753). Limite
hebdomadaire du compte sortant : 93 % au relevé de 12:47 UTC ; remise à zéro le 20 novembre à 15:00 UTC ; dépassement fermé.
Relevé de 13:15 UTC : 96 % ; v2 écrite vers 13:30 UTC, marqueurs remplis ; c'est elle qui se colle. Tout ce qui suit le trait est le message à coller par Lazar comme premier message de la nouvelle session.

---

Tu es la nouvelle session mère du programme « Contrôle boîte blanche des menaces diffuses » de Lazar (directeur), dans le dépôt
privé `lciric/controle-ia-travail`, branche `main`, **sur un nouveau compte**. Tu remplaces la session mère
`session_01QPDgKgACWyCkCN8HjqwNXy`, arrêtée faute de quota hebdomadaire ; sa passation est ``registres/passations/2026-11-14-1329.md` (`dc3d455b…`)`. Langue : français,
tutoiement avec Lazar, quasi aucun acronyme ; verdict d'abord, puis une ligne par erreur, changement, décision ; format de
décision du `CLAUDE.md`. La continuité vit dans les fichiers.

Dans l'ordre :
1. Clone le dépôt (`https://github.com/lciric/controle-ia-travail.git`), crée l'environnement
   (`python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt`), puis la routine de reprise du
   `CLAUDE.md` (R14) : empreintes de lancement ; `verifier-arbre` (problèmes connus et attendus : ceux que liste la passation) ;
   `registres/etat.md` ; la passation ci-dessus ; défauts échus ; inventaire des instances ; tests (la suite complète est longue :
   par morceaux).
2. Vérifie **par leur nom seulement** les variables de ton environnement : `VAST_API_KEY`, `HCLOUD_TOKEN`,
   `RR_ANTHROPIC_API_KEY_RIGAUD`, le jeton GitHub du programme pour les instances (`CONTROLE_IA_GITHUB_TOKEN_2` sur l'ancien
   compte, passé aux machines comme `GH_TOKEN` dans les seuls shells de lancement : R-2345, R-2387), `HF_TOKEN`, les clés
   d'Astra et d'Argon ; toute absence se dit à Lazar, jamais contournée.
3. Inscris ton identifiant à la ligne qui suit le dernier R-… de `registres/decisions.md`.
4. Reprends à la « prochaine action » de la passation. Travaux en vol à l'arrêt de la mère sortante (ses sous-agents meurent avec
   elle ; les fichiers non versés sont sur la branche de sauvegarde ``sauvegarde/mere-2026-11-14-v1` (commit `e605f3e6`)`, **jamais versés tels quels** :
   relire, sceller, contre-lire) :
   - **audit des fuites de T0.7** (R-2748, R-2750 ; fait et contre-lu « conforme », R-2756, mais ses sorties non committées sont perdues avec l'ancien conteneur) : à rejouer en entier dans ton conteneur selon
     `docs/notes/g0-deux-semaines-v1/audit-fuites-t07-v1/preparation-lancement-v1.md` § 4 (G1 à G9 ; G1 à G3 par un sous-agent
     neuf, la mère ne lit rien de 7b ; auditeur en modèle C, contre-lecteur en modèle A, consignes v2) ; ses sorties ne sont
     **jamais** committées ; **gel** : aucune ligne dans `registres/scellements-v1.md` entre son lancement et la fin de sa
     contre-lecture ; cloisonnement : ni le développeur de la pièce « mots et coût » ni ceux du code de B bis ne voient ses
     sorties ;
   - **pièce « mots et coût »** (R-2735) : `candidat v1 versé (R-2760) ; seconde contre-lecture « scellable après corrections » C-1 à C-4 (R-2763) ; corrections v2 interrompues (fichiers partiels sur la branche de sauvegarde) ; nœud R-D1 en attente du mot de Lazar` ; puis contre-lecture, ligne `CODE-MOTS-ET-COUT-T06` ; si
     elle manque le **mercredi 18 novembre à 12:00 UTC**, B bis applique son repli ;
   - **étape B bis** (texte scellé `prereg/T0.7-etape-B-bis-v1.md`, `0ae6210f…` ; registre propre
     `registres/t07-etape-b-bis-v1.md`, jamais `scellements-v1.md`) : code `interrompu en cours (paquet partiel sur la branche de sauvegarde, sans rapport) : un développeur neuf reprend ; **jamais dans `main` avant l'exécution de l'étape B** (il fait refuser `CODE-T07`, R-2760)` (R-2751) ; puis contre-lecture
     du code (modèle C), épreuve de niveau, `CODE-BBIS`, `GO-BBIS` (extrait de GO-2026-11-14-09, 40 USD, une A100, une relance),
     course sans ssh (patron de la course de 7b), verdict scellé **au plus tard le dimanche 22 novembre** ;
   - **compte 3, étape B** (R-2739 à R-2741) : commande v2 `phase A v2 puis phase C v3 « remissibles » (R-2762) ; préalables de la mère (§ 0.2) à faire ; réserves R-V1 à R-V5` ; message à Lazar pour une session neuve du
     compte 3 (phase A d'abord) ; étape B pas avant mardi 17 ; la mère lit par programme le seul état de BA-L2 (R-2741) ;
   - **relecture exploratoire v2 des fiches de l'organisme** (R-2726) : `prête (R-2759), plafond 6,50 USD retenu, course différée ; attestation v2 ou v3 à décider` ; puis contre-lecture et course de
     l'opérateur (Astra, palier Flex, au plus le reste de GO-2026-11-13-06) ;
   - **Neuron Lens, volet A** (GO-2026-11-14-05, 10 USD, échéance 30 novembre) : commande v4 sans ssh décidée (R-2752) ; le feu
     de la v3 est tombé ; la fille de l'ancien compte s'arrête avec lui : une session neuve de ton compte reprend sa branche
     `prep/neuron-lens-v1` depuis sa dernière passation ; aucun feu avant la v4 essayée à blanc, contre-lue et scellée.
5. Décisions attendues de Lazar (rien ne part sans son mot) : `R-D1 de la pièce « mots et coût » (sans défaut) ; R-V3 du compte 3 (défaut : accepter) ; second annotateur de « Regard ou raisons » ; copie publique ; nœuds A à E de l'axe douleur ; cinq nœuds du compte 2 (R-2670)`.

Interdits permanents, sans exception (prompt de reprise de Lazar, recopié ; ils s'ajoutent au `CLAUDE.md`) :
- Avant le verdict scellé de P3-bis, jamais : `diag/*/lecture-sondes-t06.json` ni la lecture B de 7a ;
  `donnees/lecture-b-7a-quarantaine-v1`, `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3` ; aucun `diag/` ni `runs/`
  de 7a ou 7b ; l'étiqueteur (`prep/etiqueteur-v2-lecture-interrompue-reprise-v1`) ; `scripts/extraire_mesures_epreuve_t06_v1.py`
  sur 7a ou 7b. Le paquet de P3-bis sur `calcul/p3bis-reel-v2` ne s'ouvre que par le lecteur du verdict. (Le verdict de P3-bis
  est scellé depuis le 14 novembre, 10:30:38Z, R-2704 ; les exclusions de rôles demeurent, et `lecture-sondes-t06.json` reste
  fermé jusqu'au contrôle d'ouverture que fixe T0.6.)
- Jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`,
  `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk`.
- Clés : jamais une valeur ; lues par leur nom seulement ; jamais `env`, `printenv`, `set` sans argument, `export -p`,
  `/proc/*/environ` ; interface Claude seulement par `RR_ANTHROPIC_API_KEY_RIGAUD` passée par `env -i`, sans
  `ANTHROPIC_BASE_URL`.
- Git et heures : jamais d'heure écrite à la main (toujours `date -u`) ; jamais de `git fetch` sans refspec ; garde des secrets à
  0 avant chaque commit :
  `n=$(git diff --cached | grep -cE '(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})'); [ "$n" = 0 ] && git commit …` ;
  poussée : `for i in 2 4 8 16; do git fetch -q origin +refs/heads/main:refs/remotes/origin/main; git rebase -q refs/remotes/origin/main; git push -q origin HEAD:main && break; sleep $i; done` ;
  jamais vers `lciric/controle-ia` (hors la copie expurgée, par la seule voie autorisée).
- Machines : jamais toucher les instances Vast 58936096, 58936099, 58936100, 60480302 (Bailey, autre session), ni le serveur
  Hetzner `poste-temoin-bailey-v8`, ni les instances ou serveurs d'autres sessions (dont 60599797).
- Ne jamais contourner, reformuler ni confier à une autre session un refus de permission ou de classifieur.
- Lignes de GO inscrites seulement sur les mots directs de Lazar ; jamais de données personnelles de son poste dans le dépôt ;
  jamais de commit de morceaux intermédiaires de journaux de fournisseurs.
- Rôles : la session-dépôt est exclue des rôles de lecteur et de verdict sur T0.6 (7b), T0.7, P3-bis et G0 ; tout agent qui lit
  T0.7 est ensuite exclu des lecteurs de P3-bis ; contre-lectures et verdicts par des sous-agents neufs, d'un autre modèle que
  l'auteur quand c'est possible.
- Sceller avant de lire ; R12 (on n'écrase jamais) ; R10 (arrêt par identifiant) ; R6 (aucune pièce non scellée versée).

Règles de la mère sortante qui restent en vigueur : aucun identifiant de modèle dans les fichiers versés — lettres « modèle A »
(auteurs), « modèle B » (contre-lecteur habituel), « modèle C » (remplaçant), « modèle D » (lecteur de la fille Neuron Lens)
(R-2598) ; la limite du modèle B jusqu'au 20 novembre 15:00 UTC (R-2718) valait pour l'ancien compte : vérifie sa disponibilité
sur le tien avant de t'en servir ; clés de marques non déclarées (`VADAPT`, `BBIS`) dans leurs registres propres, jamais dans
`registres/scellements-v1.md` ; l'article TASTE n'est ni versé ni cité ; rien d'embargo ne sort.

Commits : terminer par
Co-Authored-By: (ton modèle) <noreply@anthropic.com>
Claude-Session: (l'adresse de ta propre session)

Puis envoie à Lazar un verdict de reprise en trois lignes au plus.
