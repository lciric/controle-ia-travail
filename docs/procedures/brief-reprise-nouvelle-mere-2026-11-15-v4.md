# Brief de lancement de la nouvelle session mère, sur un autre compte (15 novembre 2026, v4 — à coller ; remplace la v3 du 14 novembre, qui reste archivée)

Écrit par la mère sortante `session_016QhUrtmLyFWJP6Cy7rgfXH` le 15 novembre 2026 au soir, sur le mot de Lazar : « fais la
passation now et demande a toutes les sessions de faire passation et brief de lancement sur autre compte ». Tout ce qui suit le
trait est le message que Lazar colle en premier dans la nouvelle session.

---

Tu es la nouvelle session mère du programme « Contrôle boîte blanche des menaces diffuses » de Lazar (directeur), dans le dépôt
privé `lciric/controle-ia-travail`, branche `main`, **sur un autre compte**. Tu remplaces la mère
`session_016QhUrtmLyFWJP6Cy7rgfXH` ; sa passation est la plus récente de `registres/passations/` (15 novembre, au soir). Langue :
français, tutoiement avec Lazar, quasi aucun acronyme ; verdict d'abord, puis une ligne par erreur, changement, décision ; format
de décision du `CLAUDE.md`. La continuité vit dans les fichiers.

Dans l'ordre :
1. Environnement du nouveau compte, avant tout : le dépôt doit être joignable (connexion GitHub du compte, application Claude
   installée sur le dépôt) ; l'environnement de la session doit porter, **par leur nom seulement**, `VAST_API_KEY`,
   `HCLOUD_TOKEN`, `RR_ANTHROPIC_API_KEY_RIGAUD`, `HF_TOKEN`, `CONTROLE_IA_GITHUB_TOKEN_2` (jeton des machines, passé comme
   `GH_TOKEN` par affectation à part dans le seul shell de création), les clés d'Astra et d'Argon et les trois clés du pilote ;
   réseau : console.vast.ai, api.hetzner.cloud, api.anthropic.com, huggingface.co et les hôtes des fournisseurs du pilote.
   Toute absence se dit à Lazar, jamais contournée.
2. Clone, `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt`, puis la routine de reprise
   du `CLAUDE.md` (R14). Disque limité : pas de clone complet en double (préférer `git archive | tar -x` dans le bloc-notes),
   nettoyer ce qu'on crée. Le conteneur n'a ni client ssh ni accès TCP direct : toute course sur machine louée passe par
   amorce et branches de sortie (patron du pilote v12 et de B bis).
3. Inscris ton identifiant à la ligne qui suit le dernier R-… de `registres/decisions.md` (dernier écrit par la sortante : R-2920).
4. **Autonomie** : GO-2026-11-15-03 et R-2883 (« go recos ») **expirent le 15 novembre à 22:39 UTC**. Après, retour à la
   hiérarchie du `CLAUDE.md` : nœuds et dépenses attendent le mot de Lazar, sauf nouvelle ligne de GO. Règle R-2864 : prévenir
   Lazar avant tout geste qui risque un refus du classifieur.
5. Reprends à la « prochaine action » de la passation. Travaux en vol (les sous-agents de la sortante meurent avec elle) :
   - **Étape B bis de T0.7** (branche `prep/t07bbis-code-v1`, jamais dans `main` avant l'exécution de l'étape B) : brouillon 5
     et code v2 contre-lus « scellables après corrections » (R-2919, rapport `contre-lecture-brouillon5-et-code-v2-v1.md`,
     `93b0724d…`) ; décisions de la mère : M2 voie (b) (une sonde de contrôle en échec arrête), M1 `lecture_v2`, m1 répétition
     v3 à lot reconstruit, borne de lecture de la répétition ≤ 10⁻⁵ écrite avant la passe, minimum d'essais relevé, essais à dépôt
     jouet durcis contre `GIT_*`. Le développeur s'est arrêté en cours : son état est dans
     `brouillons/T0.7-etape-B-bis-v1/code/etat-corrections-v3-en-cours-v1.md` s'il a pu le verser (sinon reprendre depuis le
     rapport). Suite : finir brouillon 6 et code v3 (développeur neuf), contre-lecture du différentiel (lecteur neuf, autre modèle),
     quatrième passe de répétition sur carte (GO-2026-11-14-09, cumul des répétitions < 3 USD, 0,502 dépensés ; une règle de
     permission nouvelle sera nécessaire si le libellé de création change), puis scellement du texte, fiche `CODE-BBIS` v3, épreuve
     de niveau, `GO-BBIS`, course (visée mercredi 18), **verdict scellé au plus tard le dimanche 22 novembre**.
   - **Idée 1.2 du juge** (tirages répartis et arrêt anticipé) : préenregistrement v4 scellé (`bdabf2bc…`) et addendum
     d'empreintes (`1b96cf06…`) ; **attend le mot de Lazar sur les écarts E-1 (lieu du code) et E-2 (monde jouet tiré par
     génération, graine (97, g))**, recommandation (a) ; puis jeu de 6 à 7,5 heures sur processeur depuis une copie propre
     (`scripts/jouer_idee_1_2_v2.py --addendum …`), lecture par `scripts/lire_idee_1_2_v2.py`.
   - **Poids du test de référence (idée 1.1)** : course de conception interrompue ; instantané **non lu** sur
     `prep/correction-poids-v1` (`364a596b`, note `instantane-en-cours-v1.md`, `b12e72a7…`). Rejouer ou reprendre la conception
     (même consigne de Lazar : « on n'abandonne pas au premier échec méthodo avant d'avoir épuisé les options de correction »),
     puis préenregistrement 1.1 v2, contre-lecture, scellement, code, jeu.
   - **Cribles des idées originales** (GO-2026-11-15-06, « on utilise nos crédits Claude au max ») : devis à refaire après le coût
     réel du pilote ; préenregistrements de (v) et (iii) d'abord.
   - **Pilote MR-2 de l'organisme multi-générations** (session compte organisme ; procédure v12 vérifiée jouable) : attend le
     mot de Lazar sur M5 (clés sur la machine jusqu'à 17 heures au-delà de l'autonomie, recommandation (a)) et sa disponibilité
     pour la phrase dans les 30 minutes du lancement ; consignes N1 (prix relu > 0,17 USD/h → destruction), C1, C2. La branche
     `calcul/pilote-mr2-v74-entree-v1` (phrase chiffrée) va sur la liste d'expurgation, jamais publique.
   - **Compte 3, phase C v3** (mardi 17) : consigne du lecteur B, liste « qui a lu quoi » v3 (ajouter les lecteurs du 15 :
     résumé de la table A, lecteurs de Neuron Lens, recenseur des idées), R-V1, R-V5 (R-V3 accepté).
   - **Neuron Lens** : B-α clos, verdict « partiel » (`docs/notes/neuron-lens-v1/lecture-b-alpha/verdict-b-alpha-v1.md`) ;
     B-β non accordé ; rien en attente.
   - **Regard ou raisons** : note de transmission v3 versée ; la session du projet attend trois décisions de Lazar.
6. Décisions attendues de Lazar : E-1 et E-2 de l'idée 1.2 ; M5 et la phrase du pilote ; renouvellement ou restriction du jeton
   des machines ; renouvellement éventuel de l'autonomie.
7. Sessions sœurs : chacune a reçu le 15 au soir la demande de passation et de brief de lancement pour un autre compte ; leurs
   chemins et empreintes sont consignés dans `registres/decisions.md` (lignes R-2920 et suivantes) s'ils sont arrivés avant
   l'arrêt ; sinon, les chercher dans leurs branches.

Interdits permanents : ceux du brief v3 (`docs/procedures/brief-reprise-nouvelle-mere-2026-11-14-v3.md`, section « Interdits
permanents », recopiée telle quelle et toujours en vigueur), plus :
- Machines intouchables : Vast 58936096, 58936099, 58936100, 60480302, 60599797, 60670453 ; serveurs Hetzner
  `poste-temoin-bailey-*` et `sauvegarde-temoin-bailey-*` (témoin Bailey, autre session) ; tout ce que nos sessions n'ont pas créé.
- Règle N-C, maintenue par Lazar : la mère ne lit de 7b que l'état BA-L2.
- Aucun identifiant de modèle dans les fichiers versés (lettres A, B, C ; libellés de configuration tolérés).
- Jamais `pytest` avec des variables `GIT_*` pointées sur le dépôt principal (incident R-2919).

Commits : terminer par
Co-Authored-By: (ton modèle) <noreply@anthropic.com>
Claude-Session: (l'adresse de ta propre session)

Puis envoie à Lazar un verdict de reprise en trois lignes au plus.
