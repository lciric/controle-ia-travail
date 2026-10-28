# Contre-lecture du code de l'orchestrateur du pôle, version 0.7.0, socle Fable (versions 1 à 3) — rapport v2

Contre-lecteur : sous-agent neuf, Opus 5.5 (règle R2 ; auteur du socle : Fable 5.1). En-tête écrit à 18:45 UTC (heure lue
sur `date -u` : 18:45:31) ; revue commencée à 18:00:50 UTC. Exploratoire : aucune dépense, aucun appel de modèle, aucun
fichier du dépôt modifié ; tout est dans ce dossier
(`/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/contre-lecture-v7-fable-v2/`).

**Objet.** `…/pole-scientifique-automatique-v1/orchestrateur-pole-v7/`, instantané copié à 18:01 UTC dans
`copie-orchestrateur-pole-v7/` et vérifié par `EMPREINTES-orchestrateur-pole-v7-v9.txt` (`a44d70b3…`, 99 fichiers
conformes). **Périmètre** : ce que listent les LISEZMOI v1 à v3 (monde sur banque, nul informé, sans urne, banques T0.5
v1 et v2, proposeur scripté, règle e-BH, e-valeur arrêtée, témoins sans agents, signal « pas de dents »), dans l'état
actuel du code, et leurs interactions avec le juge et la mémoire. Les états v1 à v4 ont été relus dans l'historique git
(commits `7c1806ca`, `e2887115`, `0b9efe2f`, `4621df29`) pour dire d'où vient chaque défaut.
**Pendant la revue**, une v10 a été validée dans le dossier d'origine (commit `219c0287`, 18:13 UTC : `pole/adaptateurs.py`,
script et essais du duel) ; elle ne touche aucun fichier du socle (comparaison des empreintes v9 et v10) : les constats
valent pour v10.

## Verdict

1. **À corriger avant le duel payé.** Le juge par fiche tient : richesse = vraisemblance de la fiche sur le maximum,
   instant par instant, des membres du nul (aveugles, urne, connu, archive, ajustés), sans lecture de l'avenir ; le gel et
   le monde sur banque sont propres ; la banque v2 se refait octet pour octet.
2. Mais une banque figée sert **les mêmes lignes d'épreuve à toutes les générations**, et trois mécanismes cassent alors
   les garanties annoncées, dans les réglages mêmes du duel : l'héritage de la preuve multiplie des e-valeurs calculées sur
   les mêmes lignes (C1) ; la règle e-BH calcule k* avec les témoins vrais (et les éliminées par la marge) et fixe m après
   les issues (C2, C3) ; « sans urne » laisse promouvoir une loi « sans remise » qui n'emploie aucun trait (C4).
3. S'y ajoutent des fuites vers les agents (témoins reconnaissables à leur énoncé, texte du vérificateur et richesse
   jusqu'aux consignes, banque lisible par un script écrit par l'agent : C5 à C7). Corrections locales, quelques lignes
   chacune : **pas à refaire**.

## Constats, du plus grave au moins grave

### C1 — Héritage de la preuve sur une banque figée : produit d'e-valeurs calculées sur les mêmes lignes
- **Où** : `pole/memoire.py:13-15` (« le produit des e-valeurs sur des tirages frais reste une e-valeur »), `:214-216`
  (cumul des log W finaux de la classe) ; `pole/cycle.py:562-567` (promue si cumul + log W max ≥ log 1/α), `:711` (le
  cumul s'ajoute à l'e-valeur de la règle e-BH) ; `pole/monde_banque.py:116-127` (le réservoir d'une redite est la même
  partie d'épreuve ; `--tranches` vaut 1 par défaut, `pole/pole.py:291`, et le duel ne le règle pas).
- **Ce qui est faux** : l'héritage suppose des tirages frais ; sur une banque, une redite est éprouvée sur les mêmes
  lignes, donc les mêmes issues : le « produit d'e-valeurs » revient à élever la même richesse au carré, puis au cube…
  Une classe dont le log W final est positif finit promue sans aucune donnée neuve.
- **Gravité** : garantie touchée.
- **Reproduit** :
  - boucle réelle (`e1b`, réglages du bras « informé » de la démonstration et du duel : sans urne, nul informé, e-BH) :
    génération 0, `3B-RESU-jetons_p-plus` éliminée (log W final 1,846, max 2,414, 41 lignes) ; génération 1, même loi,
    autre identifiant et autre énoncé : « redite d'une éliminée … héritage », **mêmes 41 lignes, mêmes issues**,
    **promue** (« survit » ; e-BH, m = 1, log e = 3,692 ≥ 2,996) ;
  - nul de permutation (`e1c`, issues d'épreuve permutées dans chaque moniteur, 200 permutations × 78 fiches = 15 600
    épreuves ; promotion par classe) : urne et nul informé (défaut de la ligne de commande) 0,064 % sans héritage →
    0,35 % après 4 redites ; sans urne et nul informé (duel) 0,49 % → 1,58 % après une redite → 3,09 % après 4 ;
  - limite (`e1d`) : 3,96 % des épreuves (sans urne ; 0,46 % avec urne) ont un log W final > 0 sans être promues ;
    chacune finit promue si on la redit assez (médiane : 3 redites) ;
  - dans le duel (`e16`, bras de référence « mécanique », fonctions du script du duel, mondes de la grammaire v2) : le
    chercheur mécanique est déterministe sur la partie de développement et repropose les mêmes lois à chaque génération ;
    sur 20 mondes (46 générations), **72 gardes « héritage »** (redites d'éliminées éprouvées sur les mêmes lignes) et
    aucune promotion due au seul héritage : le mécanisme joue dans les réglages du duel, son effet dépend des mondes.
- **Origine** : héritage écrit pour un monde à tirages frais (orchestrateur v4, avant v7) ; le monde sur banque de la v1
  (Fable) a retiré la fraîcheur sans retirer l'héritage ; l'ajout du cumul à l'e-valeur e-BH date de la v4 de v7 (Opus).
- **Correction proposée** : sur un monde sur banque, refuser l'héritage (politique « refus ») sauf si la redite est
  éprouvée sur des lignes d'épreuve disjointes de toutes les épreuves précédentes de sa classe (tranches imposées).

### C2 — Règle e-BH : k* calculé avec des fiches qui ne sont pas des découvertes (témoins vrais, éliminées par la règle par fiche)
- **Où** : `pole/cycle.py:686-727` ; `jugees` (`:700-702`) contient les témoins et toute fiche jugée, k* (`:715-719`) est
  calculé sur elles toutes, puis la fonction ne fait que rétrograder (`:724-726`) ; le docstring de v2 et v3 : « Les
  témoins comptent dans m (ils sont jugés comme les autres) ».
- **Ce qui est faux** : la borne e-BH vaut pour l'ensemble rejeté qu'elle calcule. Les découvertes du pôle sont les seules
  fiches réelles promues : un sous-ensemble filtré après coup. Un témoin vrai fort (ou une fille forte éliminée par la marge
  2·δ0, ou une fiche en mode « horizon ») prend un rang dans k* et **abaisse le seuil des fiches réelles** (de m/α à
  m/(2α), m/(4α)…) ; le taux de fausses découvertes parmi les fiches réelles n'est plus borné par α.
- **Gravité** : garantie touchée.
- **Reproduit** (fonction réelle `appliquer_multiplicite`) :
  - cas construit (`e4`) : A forte mais éliminée par la marge, B à log W 3,2 : B est retenue (seuil 20) ; sans A dans k*,
    B ne l'est pas (seuil 40) ;
  - e-valeurs nulles réalistes (martingales de test, 4 000 répétitions ; `e4b`) : 24 fiches dont 3 témoins vrais forts →
    2,3 % de fausses découvertes parmi les réelles (0,9 % si les témoins sortent de k*) ; 40 dont 10 → 4,75 % (0,6 %) ;
    marge (`e4`) : 20 fortes éliminées parmi 40 → 6,9 % (> α ; 0,3 % corrigé) ;
  - pire cas (e-valeurs nulles « tout ou rien », 20 000 répétitions ; `e4c`) : 5,0 % sans témoins ; **16,2 %** avec 3
    témoins vrais parmi 24 ; 23,4 % avec 6 ; 34,2 % avec 10 parmi 40 ;
  - dans le duel (`e16`, `e16b`, 20 mondes, 46 générations) : les 3 témoins vrais (lois exactes du monde) sont retenus
    dans k* dans 37 générations (log e de 5,0 à 6,8 sur les quatre premiers mondes) ; la première fiche réelle passe alors
    au seuil m/(4α) ; 3 des 19 fiches réelles retenues ne le seraient pas sans les témoins dans k* (toutes liées à la
    structure du monde : aucune fausse découverte observée sur ces mondes, mais la borne n'est plus démontrée).
- **Origine** : v2 et v3 (Fable).
- **Correction proposée** : garder m = toutes les fiches gelées (témoins compris) mais calculer k* sur les seules fiches
  réelles qui passent la règle par fiche (e = 0 pour les témoins et pour les éliminées par la marge), et juger les témoins
  par une passe à part.

### C3 — Règle e-BH : m fixé **après** les issues ; l'agent connaît son verdict et peut sortir de m
- **Où** : `pole/cycle.py:700-702` (m = fiches parvenues au jugement, avec `pari`) ; le docstring (`:689-690`, écrit en v4)
  affirme « m = nombre de fiches jugées de la génération, fixé avant toute issue » : c'est faux ; essai qui l'entérine :
  `essais/test_v7_banque.py:144` (une fiche « indécise » donne m = 0).
- **Ce qui est faux** : une fiche dont l'expérimentateur ne rend pas de bloc JSON (ou que le vérificateur ne confirme pas)
  devient « indécise » et sort de m. Or l'expérimentateur peut calculer sa richesse exacte avant de répondre ; s'abstenir
  quand elle est basse fait baisser m et les seuils des autres fiches.
- **Gravité** : garde contournable (garantie touchée dès qu'un agent s'abstient selon sa richesse).
- **Reproduit** :
  - `e15` : avec les seuls `engagement.json` et `mesures.json` de son dossier, sans la graine du noyau, la richesse
    recalculée est **identique** à celle du noyau (log W final 1,845958, max 2,413549) ;
  - `e2` (nul de permutation, 200 permutations, 78 fiches, e-BH réelle) : agents honnêtes, 0 % de fausses promotions dans
    tous les réglages ; agents qui s'abstiennent sous un log W final c : sans urne et nul informé (duel) **6 % à 14,5 %** ;
    sans urne, nul aveugle 8 % à 17 % ; urne et nul informé jusqu'à 3,5 % (contre 0) ; avec m fixé au gel : 0 % ;
  - `e5b` : un expérimentateur qui s'abstient sur les 13 témoins faux fait tomber m de 24 à 11.
  - Dans le duel lui-même, expérimentateur et vérificateur sont simulés (honnêtes) : le défaut n'y est pas exploitable,
    mais il l'est dès qu'un expérimentateur réel sert une banque.
- **Origine** : v2 (Fable) ; affirmation fausse ajoutée en v4 (Opus).
- **Correction proposée** : m = nombre de fiches gelées de la génération (engagement écrit), témoins compris, et e = 0
  pour toute fiche non jugée ; corriger le docstring et l'essai.

### C4 — « Sans urne » sur une banque : une loi « sans remise » sans aucun trait est promue
- **Où** : `pole/cycle.py:75` et `:319`, `pole/pole.py:269` (justification : « banque figée : pas de dérive dans le
  temps ») ; `pole/cycle.py:438-444` (`_controler_pari` ne contrôle que `valider_loi`, donc tout type de
  `selection_pari.TYPES_LOI`, `sans_remise` compris, `:45-46`, `:135-138`) pour la population et la recombinaison (le
  proposeur seul est borné : `pole/proposeur.py:50`).
- **Ce qui est faux** : la condition qui compte n'est pas la dérive mais l'effectif fini : le plan couvre toute la partie
  d'épreuve d'un moniteur (taille 120 ≥ 41 à 75 lignes), donc les issues sont un tirage sans remise ; la marginale ajustée
  ne domine pas cette loi. L'urne (juge v1) avait été construite contre ce tricheur précis
  (`pole/controles_pari_v1.py:339`) ; « sans urne » le rouvre exactement là où il s'applique.
- **Gravité** : garantie touchée sous le nul de permutation, pour les lois qui lisent l'historique (conditionnée à la
  connaissance de la composition d'épreuve — que voient tout expérimentateur et tout vérificateur d'une fiche du moniteur,
  `mesures.json` couvrant toute l'épreuve, et tout lecteur de la banque : C7).
- **Reproduit** (`e3`, banque v2 réelle) : composition exacte → log W final 3,82 à 4,24 pour les cinq moniteurs à trois
  issues (3B:COHERENCE 4,09 ; 3B:NOVELTY 4,24 ; 8B:COHERENCE 4,05 ; 8B:NOVELTY 3,95 ; 8B:RIGOR 3,82) > log 20 = 3,00,
  avec ou sans nul informé ; **avec urne : 0,00 partout** ; composition + 1 par classe : ≤ 2,34 ; boucle réelle (3B:NOVELTY,
  e-BH, m = 1) : « survit ». Pour les lois qui ne lisent que les traits, « sans urne » reste sain ici : 0,49 % de fausses
  promotions par fiche sous le nul de permutation (`e1c`, génération 0).
- **Dans le duel** : population tirée au gabarit, recombinaison simulée, proposeur borné : non exploitable tel que
  configuré ; exploitable par toute population ou recombinaison réelle.
- **Origine** : v1 (Fable).
- **Correction proposée** : sur un monde sur banque, refuser pour toute source les lois qui lisent l'historique des issues
  (`sans_remise`, `moyenne_glissante`, et toute loi composée qui en contient), ou garder l'urne.

### C5 — Témoins reconnaissables à leur énoncé public ; « pas de dents » masquable, contrôle des témoins faux vidable sans signal
- **Où** : `exemples/proposeur_scripte_banque_v1.py:96-103` (« Témoin vrai : … (rang +0,42 en calibrage) », « Témoin faux :
  … suit le trait de bruit », opérateur `monotone:bruit`) ; l'énoncé est dans la vue publique servie à l'expérimentateur et
  au vérificateur (`pole/fiche.py:145-149`, `pole/cycle.py:186-191`) ; `pole/cycle.py:748-753`, `:765-767` (clés
  historiques comptées sur les témoins « testés », indécis compris) ; aucun état pour le côté faux, alors que le côté vrai
  a `etat_dents`.
- **Ce qui est faux** : un témoin reconnaissable cesse de mesurer (la mémoire le dit elle-même : `pole/memoire.py:4-5`).
  Quand les témoins passent par des agents (défaut de `ConfigGeneration` et de la ligne de commande ; la course « (a) bis »
  les demandait avec agents), un agent qui s'abstient sur les « Témoin vrai » change « pas de dents » en « dents non
  mesurées » ; sur les « Témoin faux », il retire tout contrôle fatal, et la qualité affiche « taux de fausses gardées 0,0 »
  avec 13 témoins faux « testés » et **aucun jugé**.
- **Gravité** : fuite et garde contournable.
- **Reproduit** : `e0` (énoncés), `e5` et `e5b` (boucle réelle, banque v2 : honnête → « pas de dents », 5 vrais et 13 faux
  jugés ; abstention sur les vrais → « dents non mesurées » ; abstention sur les faux → 0 faux jugé,
  `taux_fausses_gardees` 0,0, m = 11 sur 24). Avec `--temoins-sans-agent` (démonstrations, duel), le défaut est neutralisé.
- **Origine** : énoncés v1 (Fable) ; signal limité au côté vrai v3 (Fable), clés « jugés » ajoutées en v5 (Opus) sans état
  côté faux. Les témoins d'avant v7 (`exemples/temoins-pari-demo-*.json`) avaient des énoncés neutres.
- **Correction proposée** : énoncés et opérateurs des témoins de même forme que ceux de la population ; un état « contrôle
  des témoins faux non mesuré » quand aucun témoin faux n'est jugé, et les taux calculés sur les seuls jugés.

### C6 — Canaux de texte ouverts vers les agents qui écrivent des lois (issues d'épreuve, richesse)
- **Où** : `pole/cycle.py:38` (`mesures.json` n'est pas dans `EXCLUS_DU_REJEU` : le vérificateur voit les issues d'épreuve),
  `:541-542` (le motif libre du vérificateur entre dans le motif de la fiche), `:573-574` (« log W cumulé x » dans le motif) ;
  `pole/memoire.py:286`, `:296` (motifs servis à la synthèse), `:323` (leçon servie aux expérimentateurs et à la
  recombinaison) ; `pole/recombinaison.py:300`, `:174-175`.
- **Ce qui est faux** : la pièce 6 de la conception (« canaux de texte » : leçons en champs structurés, jamais de prose libre
  servie) est déclarée « à coder » dans les LISEZMOI v1 à v3 et ne l'a été dans aucune version ; sur une banque, toute issue
  d'épreuve qui atteint l'auteur d'une loi compromet les fiches suivantes, éprouvées sur les mêmes lignes.
- **Gravité** : fuite.
- **Reproduit** : `e6` (boucle réelle `executer_pole`, banque jouet des essais) : les 120 issues d'épreuve d'une fiche,
  recopiées par le vérificateur dans son motif, arrivent dans `resume-index.json` servi à la synthèse **et dans la consigne
  de l'agent de recombinaison** ; `e14` (banque v2) : « log W cumulé 0.5116 » arrive dans le résumé de la synthèse, la leçon,
  et les consignes des expérimentateurs et de la recombinaison. Le proposeur, lui, ne reçoit ni motif ni leçon.
- **Origine** : canaux d'avant v7 (mémoire, monde tenu par le noyau) ; nuisibles depuis le monde sur banque (v1, Fable).
- **Correction proposée** : ne servir aux agents que des motifs d'un vocabulaire fixé par l'orchestrateur (ni texte d'agent,
  ni nombre), et des leçons en champs structurés.

### C7 — La banque (issues d'épreuve) est lisible par un agent qui écrit puis exécute un script
- **Où** : `pole/garde_outils.py:283-299` (pour `Write`, seul le chemin est contrôlé, jamais le contenu) ;
  `pole/adaptateurs.py:91` (le bac à sable est éprouvé par `bwrap --ro-bind / /` : tout le système de fichiers en lecture) ;
  la banque et, dans le duel, `verite.json` sont dans le dossier du monde, voisin de celui de la course
  (`monde-XX/monde/` et `monde-XX/<bras>/`).
- **Gravité** : fuite (reproduite pour la garde ; **soupçonnée** pour le bac à sable du SDK, dont la politique de lecture
  n'est pas vérifiable ici).
- **Reproduit** (`e11`, décisions de la garde réelle) : `Read` et `cat` de la banque refusés ; `Write` d'un script qui ouvre
  la banque par son chemin absolu **autorisé**, son exécution **autorisée** ; `python3 -c` avec un chemin ou une remontée
  découpés autorisé. Le LISEZMOI v5 reconnaît la garde contournable et renvoie au bac à sable — qui, éprouvé ainsi, ne
  borne pas la lecture.
- **Origine** : garde v5 (Opus) ; la banque, secret posé sur le disque, vient de la v1 (Fable) ; `verite.json` du duel :
  v10, hors périmètre.
- **Correction proposée** : tenir banque et vérité hors de ce que l'agent peut lire (autre utilisateur, droits 600, ou bac à
  sable à lecture restreinte), et l'éprouver avec un agent réel avant le duel.

### C8 — Les témoins vrais de la banque ne sont pas établis ; « pas de dents » ne se lit pas comme « banque trop petite »
- **Où** : `exemples/proposeur_scripte_banque_v1.py:27`, `:94-99` (seuil |rang| ≥ 0,35 sur la partie de calibrage, sans
  test) ; lecture des LISEZMOI v1 à v3 (« témoins vrais éliminés (banque trop petite : pas de dents) »).
- **Ce qui est faux** : 39 couples (moniteur, trait) essayés ; sous le nul, 4,35 déclarations attendues ; 5 déclarées ;
  valeurs p de permutation 0,040 à 0,120 (une seule sous 5 %, aucune après correction) ; sur l'épreuve, deux des cinq
  changent de signe (rang −0,24 et −0,044 dans le sens déclaré). De plus les cinq témoins vrais sont des **copies exactes**
  de fiches de la population (même loi, même moniteur), et leur verdict diffère parfois de celui de leur copie par le seul
  ordre du plan (égalités départagées par une graine tirée de l'empreinte de la fiche) : sans urne, nul aveugle,
  `3B-RIGO-actions_-plus` est promue par fiche (log W max 3,058) et le témoin vrai identique ne l'est pas (2,274).
- **Gravité** : lecture trompeuse.
- **Reproduit** : `e9` (valeurs p), `e1a` (copies et verdicts).
- **Origine** : v1 (Fable).
- **Correction proposée** : ne déclarer un témoin vrai que sur un test de permutation corrigé pour le nombre de couples
  essayés (ou sur un monde planté), jamais comme copie d'une fiche de la population.

### C9 — La classe d'une redite ignore le moniteur
- **Où** : `pole/memoire.py:96-103` (signature = lois sur une sonde gaussienne, sans moniteur ni banque), `:134-146`.
- **Ce qui est faux** : la même loi posée sur deux moniteurs est « la même classe » : l'héritage passe d'un moniteur à
  l'autre (données différentes et dépendantes : mêmes épisodes, même juge), et par lecture une transposition vers un autre
  moniteur d'une survivante est refusée comme « redite d'une survivante » (stratégie `transposition_moniteur` du
  proposeur).
- **Gravité** : garantie touchée (même mécanisme que C1) et garde de redite fausse.
- **Reproduit** (`e10`, partie b, boucle réelle) : la fiche du moniteur 3B:RIGOR hérite du cumul 1,846 gagné sur
  3B:RESULT_REASONING (non promue ici : sa propre richesse est négative). Le refus de la transposition : par lecture.
- **Origine** : mémoire d'avant v7 ; moniteurs introduits par le monde sur banque (v1, Fable).
- **Correction proposée** : mettre le moniteur et l'empreinte de la banque dans la clé de classe.

### C10 — Repli silencieux : « témoins sans agents » sans monde qui dépose les issues
- **Où** : `pole/cycle.py:598` (condition `self.monde_noyau is not None`), `:133-134` (aucun refus dans `valider`).
- **Ce qui est faux** : `temoins_sans_agent=True` sans banque ni monde du noyau est accepté, et les témoins passent par
  les agents sans motif (R5 : aucun repli silencieux).
- **Gravité** : garde contournable (clarté).
- **Reproduit** : `e10`, partie a (expérimentateur et vérificateur lancés pour le témoin, issue sans marque `sans_agent`).
- **Origine** : v3 (Fable). **Correction proposée** : le refuser dans `ConfigGeneration.valider` (et à la ligne de commande).

### C11 — Reproductibilité
- **Manifeste sans la banque** (`pole/pole.py:74-80`, `pole/outils.py:157-165`) : une course `--monde-banque` ne consigne ni
  le chemin ni l'empreinte de la banque, ni `nul_informe`, ni `tranches`, ni les empreintes des fichiers de population et
  de témoins (reproduit, `e7`). Origine v1 (Fable). Correction : les ajouter aux réglages du manifeste.
- **Scripts « v1 » modifiés en place pour produire la v2** (R12) : `exemples/construire_banque_t05_v1.py` (traits) et
  `exemples/proposeur_scripte_banque_v1.py` ne refont plus la banque ni la population v1 ; la commande du LISEZMOI v3
  (`… construire_banque_t05_v1.py RACINE_MAIN exemples/banque-t05-v1-bis.json`) produirait une banque v2 nommée v1-bis
  (reproduit par comparaison avec le commit `7c1806ca`). Origine v3 (Fable). Correction : nouveau nom pour toute nouvelle
  version.
- **Empreintes v1 à v8 caduques** : le code est édité en place ; `sha256sum -c` échoue sur 21, 21 et 19 fichiers pour les
  empreintes v1, v2, v3 (reproduit) ; ces états ne se retrouvent que par git. Correction : figer chaque version (étiquette
  ou dossier), ou le dire dans chaque LISEZMOI.
- **R9** : `numpy.random.SeedSequence` n'est pas employé ; dérivation par SHA-256 (`pole/outils.py:82-89`), écart documenté
  et déterministe — pas un défaut de reproductibilité.
- Divers : `pole/__pycache__/` présent dans le dossier livré ; `demonstrations/duel_proposeurs_v7.py` hors des empreintes
  v9 au moment de la copie (couvert depuis par les empreintes v10).

### C12 — Honnêteté des essais
- `essais/test_v7_banque.py:144` entérine C3 (m = 0 pour une fiche indécise).
- Aucun essai : loi qui lit l'historique sans urne sur une banque finie (C4) ; témoins dans k* (C2) ; neutralité de
  l'énoncé des témoins (C5) ; héritage sur des lignes réutilisées (C1) ; refus de `temoins_sans_agent` sans monde (C10).
- `essais/test_v7_banque.py:123-124` : `unittest.main()` placé avant les classes `Multiplicite` et
  `TemoinsSansAgentEtSansDents` : lancé directement, le fichier les saute (la découverte les lance).
- Essai du relais intermittent (hors périmètre : v6, réserve v5) : `test_artefact_plafond_atteint` a échoué une fois sur la
  suite complète (201 sur 202 au premier passage, 202 sur 202 au second) et **8 fois sur 64** rejoué sous charge (`e13`,
  toujours « 200 != 402 ») : le relais règle le coût après avoir rendu la réponse (`pole/relais_reel.py:268-279`) ; la
  garantie écrite (dépassement borné par les appels en vol) tient, l'essai suppose plus. Correction : régler le coût avant
  le dernier morceau, ou attendre le journal dans l'essai.

### C13 — Mineurs (clarté)
- `log_richesse_arretee` (arrêt à 1/α, v3) reste dans les résultats (`pole/selection_pari.py:618`,
  `pole/nul_filles_v2.py:225`) alors que la règle e-BH emploie l'arrêt à m/α (v4) : deux « e-valeurs arrêtées » différentes.
- Aide de `--multiplicite` : « (e-valeurs finales) » (`pole/pole.py:271`) — périmé.
- `nombre_issues` absent de la fiche : `moniteur_de` prend celui du moniteur, `preparer_engagement` et `_controler_pari`
  prennent 3 (`pole/monde_banque.py:106`, `pole/cycle.py:311`, `:444`) ; reproduit : une loi à 3 issues est jugée sur un
  moniteur à 2 issues (sans effet sur la validité ; refus confus avec le nul informé).
- Nul informé sans forme ajustée du connu (tempérée, mélangée à l'aveugle) : **soupçonné**, non reproduit sur cette banque
  (`e12` : connu retouché, log W max ≤ 1,16, aucune promotion).

## Ce qui tient
- Richesse = vraisemblance de la fiche sur le **maximum instant par instant** des membres du nul (`selection_pari.py:428-438`,
  `nul_filles_v2.py:216-220`), urne et connu compris.
- **Aucune lecture de l'avenir** : 780 vérifications de préfixe, 0 échec, pour `evaluer` et `evaluer_v2`, pari plein et à
  fraction, avec marginale, uniforme, moyennes glissantes, urne, connu, archive, mélange et membres ajustés (`e8`).
- Ville par fiche pour une loi fixée, sous le nul de permutation : 0,064 % de fausses promotions avec urne, 0,49 % sans urne
  pour des lois sur traits (`e1c`, 15 600 épreuves).
- e-valeur arrêtée (premier instant ≥ m/α, sinon finale) : temps d'arrêt d'un processus dominé par une martingale de test,
  donc e-valeur (lecture), hors héritage (C1) et à m fixé (C3).
- Nul informé ajusté sur la seule partie de calibrage, disjointe de l'épreuve, avant le gel, sous l'empreinte (lecture ;
  essai existant).
- Gel : plan, bibliothèque et moniteur préparés et empreintés avant toute lecture d'issue ; mesures lues après ; refus sans
  dossier ; fiche ou engagement modifiés après le gel rejetés (lecture ; essais existants).
- Monde sur banque : réservoir = épreuve seule, issues lues jamais calculées, instance sans issue exclue, moniteur
  inconnu refusé (lecture ; essais existants).
- Banque v2 refaite **octet pour octet** depuis `main` (`f26cc857…0d71`) ; empreintes des trois sources conformes (`e0`).
- Proposeur scripté : sortie identique quand toutes les issues d'épreuve sont altérées (`e0`) ; il lit pourtant tout le
  fichier.
- Témoins vrais et faux fabriqués sans les données d'épreuve (`e0`) ; témoins sans agents jugés par le noyau seul et
  comptés dans m.
- Écriture scellée sans écrasement (`EcrasementInterdit`), dossier de sortie non vide refusé (lecture).
- Graines déterministes ; ordre secret dérivé de la graine du noyau et de l'empreinte de l'engagement.
- 202 essais : 202 passent au second passage (201 au premier : l'essai intermittent du relais, C12).

## Essais de la contre-lecture
Scripts dans `essais-contre-lecture/`, sorties dans `sorties/` ; interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B` ;
code exécuté : la copie `copie-orchestrateur-pole-v7/` (conforme aux empreintes v9). Empreintes SHA-256 complètes en
annexe (`empreintes-essais-et-sorties-v1.txt`, recopiée ci-dessous).

| essai | objet | sortie |
|---|---|---|
| `e0_banque_et_proposeur_scripte_v1.py` | banque refaite, sources, proposeur scripté et épreuve, énoncés des témoins | `sorties/e0/e0-resultat-v1.json` |
| `e1a_balayage_richesses_v1.py` | richesses des 96 fiches et témoins sur la banque réelle, trois réglages | `sorties/e1a-richesses-v1.json` |
| `e1b_heritage_sur_banque_pipeline_v1.py` | C1, boucle réelle | `sorties/e1b-sans-urne-informe/e1b-resultat-v1.json` |
| `e1c_heritage_nul_permutation_v1.py` | C1, taux sous le nul de permutation | `sorties/e1c-heritage-urne{1,0}-r200-g5-v1.json` |
| `e1d_part_finale_positive_v1.py` | C1, limite | `sorties/e1d-finale-positive-urne{1,0}-r100-v1.json` |
| `e2_ebh_m_apres_issues_v1.py` | C3, abstention selon la richesse | `sorties/e2-ebh-censure-urne*-informe*-r200-v1.json` |
| `e3_sans_urne_loi_sans_remise_v1.py` | C4 | `sorties/e3/e3-resultat-v1.json` |
| `e4_ebh_puis_filtre_v1.py`, `e4b_ebh_temoins_vrais_v1.py`, `e4c_ebh_pire_cas_v1.py` | C2 | `sorties/e4-…`, `sorties/e4b-…`, `sorties/e4c-…` |
| `e5_temoins_reconnaissables_dents_v1.py` | C5 | `sorties/e5/e5-resultat-v1.json` |
| `e5b_qualite_temoins_faux_v2.py` (reprise en script d'une vérification en ligne, dossier `sorties/e5-bis` ; la v1 écrivait par erreur dans `sorties/e5b/inutilise/`, gardée) | C5, C3 (m = 11 sur 24) | `sorties/e5b-v2/e5b-resultat-v2.json` |
| `e17_nombre_issues_defaut_v1.py` (idem) | C13 | `sorties/e17-nombre-issues-v1.json` |
| `e6_canal_texte_verificateur_v1.py` | C6 (issues) | `sorties/e6/e6-resultat-v1.json` |
| `e8_sans_regard_vers_l_avenir_v1.py` | ce qui tient : préfixe | `sorties/e8-prefixe-v1.json` |
| `e9_temoins_vrais_etablis_v1.py` | C8 | `sorties/e9-temoins-vrais-v1.json` |
| `e10_repli_temoins_et_classe_sans_moniteur_v1.py` | C10, C9 | `sorties/e10/e10-resultat-v1.json` |
| `e11_garde_et_banque_v1.py` | C7 | `sorties/e11-garde-banque-v1.json` |
| `e12_connu_retouche_v1.py` | C13 (soupçon non reproduit) | `sorties/e12-connu-retouche-v1.json` |
| `e13_relais_course_v2.sh` (la v1, qui comptait mal, reste) | C12, relais | `sorties/e13/`, `sorties/e13-relais-course-resume-v1.txt` |
| `e14_richesse_dans_la_synthese_v1.py` | C6 (richesse) | `sorties/e14/e14-resultat-v1.json` |
| `e15_richesse_calculable_par_l_agent_v1.py` | C3 | `sorties/e15-richesse-agent-v1.json` |
| `e16_heritage_dans_le_duel_v1.py`, `e16b_resume_v1.py` | C1, C2 dans le duel | `sorties/e16*/`, `sorties/e16b-resume-v1.json` |
| `aide_noyau_v1.py` | appels du noyau sans agent (commun) | — |
| manifeste de la ligne de commande (C11) | course `pole --monde-banque … --sans-nul-informe` | `sorties/e7-cli-banque-a/manifeste.json` |
| suite des 202 essais du dossier, deux passages | | `sortie-essais-complets-v1.txt`, `sortie-essais-complets-v2.txt` |

**Résumé de `e16` et `e16b`** (bras « mécanique » du duel, fonctions du script du duel de l'instantané, 20 mondes de la
grammaire v2, 46 générations) : 72 gardes « héritage » ; 0 promotion due au seul héritage ; 3 témoins vrais retenus dans
k* dans 37 générations sur 46 ; 19 fiches réelles retenues, dont 3 qui ne le seraient pas si les témoins sortaient de k*
(m inchangé) ; 0 promue sans lien avec la structure, 0 témoin faux promu, 9 structures retrouvées.

## Limites de cette contre-lecture
- Aucun agent réel : les abstentions et le texte du vérificateur sont joués par des agents simulés modifiés ; ils montrent
  ce que le code laisse faire, pas ce qu'un modèle ferait.
- La politique de lecture du bac à sable du SDK n'est pas vérifiable ici (C7 soupçonné pour cette part).
- Les taux sous le nul de permutation valent pour cette banque et la population scriptée ; les mondes du duel sont plus
  grands (C1, C2 : mécanismes observés, effets à mesurer sur eux).
- Hors périmètre, lus sans contre-lecture complète : proposeur, nul d'archive ajusté, pari à fraction, plomberie v5, duel.

## Empreintes
### Fichiers lus (instantané v9 copié ; chemins relatifs au dossier `orchestrateur-pole-v7/`)

Lus aussi, sans les recopier : les états v1 à v4 dans l'historique git (commits `7c1806ca`, `e2887115`, `0b9efe2f`,
`4621df29`), et `EMPREINTES-orchestrateur-pole-v7-v10.txt` (`69f4973c938e45a37469ed83d3f35b74a056eef7ed313cfc34b45cc7a4cc593d`)
pour comparer v9 et v10. La même liste en fichier : `empreintes-fichiers-lus-v1.txt`
(`11d32b2f291818e96fa06e8f768ad495a56331ecb87d1ca09b57855bc7928f0f`).

```
73c681a233e9e901207473dfa29aedb175d2ff22b69ef0f3be4cf3176886211c  LISEZMOI-orchestrateur-pole-v7-v1.md
1004f686667bcb19ecccd65ce3bef24750ca90d9b6e206a4f71555e61e1eda4c  LISEZMOI-orchestrateur-pole-v7-v2.md
c8a3eeda6845a0187ff15ebf9d55f0167a67f31a1a6bdbfa7d0efd371058c8c3  LISEZMOI-orchestrateur-pole-v7-v3.md
97203aa119fbcf204e10bdc34663995711c4c58cff272d5fa257dd70831f4c3a  LISEZMOI-orchestrateur-pole-v7-v4.md
d89a1e5d2d2eec1fad60685bb4ce835583d7c53ad8f3f42b34433dc6bb4fa461  LISEZMOI-orchestrateur-pole-v7-v5.md
8d96bf9ff65a20fb96bb512930839e62fcc19426c15d31f21ca33cde6b175a9d  LISEZMOI-orchestrateur-pole-v7-v6.md
4bc261a0ad39ba489a9d2380dd55e3f9bbb74dd24e3efff4beae2ab0502fa476  LISEZMOI-orchestrateur-pole-v7-v7.md
b493cf72c178f6cf5ddd8798c79da7264417f940081f506b4116e284ec39169c  LISEZMOI-orchestrateur-pole-v7-v8.md
c34d005c35064eeb0e920be5b0a9216fac8f3ca624ba9d8fbe3f7a65837d9636  LISEZMOI-orchestrateur-pole-v7-v9.md
31fc8c4bc286341fcbf10181be6779ecd20ddf9de092a2c885ce8d11b27fedee  conception-v7-v1.md
a44d70b31be28989cb426b15dd616c4f559e5903935b011869760969ed01fe09  EMPREINTES-orchestrateur-pole-v7-v9.txt
9ff9d80f2b023401028d42d43211b9b7645c44ef6bfe0bacdc9847c5c63567d3  pole/selection_pari.py
a150eb00d5578a8bc4b558bda250d0f592a0a95079aa3fda179ffe9062c8c936  pole/cycle.py
07df30822394e1e12223b3481e959460fa84babcb1f07a4bc40cc82d26150903  pole/monde_banque.py
0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910  pole/nul_filles_v2.py
069224ac237c4f693e87a75858b0636bcfb579ba0b4dc3382b0fc37bdd53756e  pole/pole.py
02ec39b9b736fc806682f47a54feb89ebe67868a178019581d27df6e6b2a71c4  pole/memoire.py
7c230afed4014e43f131c6c5d4846010df210b6e321f877a47b0150a28d21d0b  pole/fiche.py
966d9553026aad1eb7d97fa677334f1b59f22a39f15eef95134d63bc47634444  pole/outils.py
78abfd4731218e20538418608ebebaca3364206ef6d014b7a34829a3c9fd7e85  pole/caviardage.py
b2aaf3958525e399f0c6453eace41550146327623f95578d64e158bb13e8cae0  pole/monde_noyau.py
be14d44e7a8ebf6b2a71f16b5290555f5d7a11309e5dbf309ce9097f19ae7892  pole/simulation.py
71faad38644c77ae2cc21f23bfb1011c48fe674a08e542983819425ee47bd3d0  pole/recombinaison.py
a77018584ec5d20c25224fc675c412c4606ba3a6ce8dfde6e469a651a425a2ea  pole/proposeur.py
a767967c1184fb94a2907f6cbe7f2bfd1602d4b50de4641abf60097fafa2aea6  pole/adaptateurs.py
e0df9743d80f6b01fbff91961419c94d570dc21683e4f7bf543c2d84713e4d3c  pole/garde_outils.py
6582b786171de18393088b894f21dac66043eaf6741e4e9892697539b5320830  pole/relais_reel.py
82ad20fc6e950402663dc9352873adc9fbf195242cccd963f3173dddcf2f75a7  pole/__main__.py
f7341b965ddba1e0fb21b44d9068f59650d5c77e3175f2b6b7ca879219fa5c9b  pole/__init__.py
f76c88f7980428e7196b3babb8fd172937a59a852885b41eeb74ccaab554dfac  essais/test_v7_banque.py
57d52b96b53cb6bfb7962ee41a29a4f73110a1448f4bd2fe192e19972933d5c8  essais/aides.py
34d4d46ad5b8c1cd150da0933831681fe317daf66e3683edc33cde587eca0f13  essais/test_cycle.py
ff628d0ceb5dceab48dfa467c4aaa2081a6471d036ffdbc9a3b914dae299cfdb  essais/test_v6_relais_reel.py
cdfa818d0f6f9a6740e4dc6d6905d9515ffc617d6d047a7fdf566ffdfb31937d  exemples/proposeur_scripte_banque_v1.py
e83d502cac606e63712c4cde146106551d5324bc3a0ba27ada51d7417c1a5be2  exemples/construire_banque_t05_v1.py
f26cc85794f0e65bca6217911f862414f1489195b9bf3ada51d22a3af0fe0d71  exemples/banque-t05-v2.json
e66a96cdf8f20833f44a8422a512f6bc9c880990ce93c2152406c6243c06082e  exemples/population-banque-t05-v2.json
3c8f65ec89d30f45f6cac36abbe2b5873bbe855c4539a5dd0ae8a297d45356a9  exemples/temoins-banque-t05-v2.json
2aa0984e37d1851fd13af057ecd9e49c545a9234d4846f76b14bd67e9841ea32  exemples/temoins-banque-t05-v1.json
d6bd1b2a133e025af81147db3640e8f3b27ce7a751027ec7bbbf343ae61a0b50  exemples/temoins-pari-demo-4traits-v1.json
fdf4d5c1ca0d2971b416ee5f694deff7a4696fe5defb3a6a1843dffef1231877  exemples/temoins-pari-demo-v1.json
0cbc0bb5493a451d1cb9c223ffa80c0dfd0c3fe9aec6f0711009823ca1611c15  exemples/temoins-demo-v1.json
9ff39b9cf38a0ee2d56906187985c0a626d1add9b73468e3169b362bb3335d50  demonstrations/demo_couche1_v7.py
453ce79498c3b8d8c7f9bba80d313850a2474c2d003f9c2ed4f31fa6056df3fd  demonstrations/duel_proposeurs_v7.py
2bb1f386102ead4cad34618e74f4897a0ccb569bb85d31d3117bf221595bccb2  demonstrations/repetition_duel_v7.py
ef016d250b7b503f705dc95919719c68c8f968534fd901df7364a6062d67cf12  demonstrations/banc_tricheurs_v7.py
```

### Scripts de la contre-lecture (chemins relatifs à ce dossier)

```
7ed8e26b2f39256a12f34e68b921d07d1a70263fe92222d6acc7c3157a1a3ae0  essais-contre-lecture/aide_noyau_v1.py
c3e11a79f185bd7db8baf44926ab1e8864f7f88cd6217ebf20118bb58ef1cf07  essais-contre-lecture/e0_banque_et_proposeur_scripte_v1.py
037f5071e549e30b2e99e29d4103742d2a587665365b9f9ac0eb02e2b2a7c71e  essais-contre-lecture/e10_repli_temoins_et_classe_sans_moniteur_v1.py
894904dd6deef357c904523c6518369a24778017b3f0f02a090691616d9b68ce  essais-contre-lecture/e11_garde_et_banque_v1.py
24a479a1bc4e12851d491716b230ca4023d807df682399ba1ac74837f7b8235f  essais-contre-lecture/e12_connu_retouche_v1.py
d17f6b50bb254c8c220078184dd089fb4269f463d9b29858f77af2d873617240  essais-contre-lecture/e13_relais_course_v1.sh
6cf202ac65aa5d01e7d84c777e5d2a09d9a0e244780d76e222b84bc6ea4038b4  essais-contre-lecture/e13_relais_course_v2.sh
2d62ecc2e2388ab416d7fda243f7087e5d17c053d57abd489f27d04509d2930b  essais-contre-lecture/e14_richesse_dans_la_synthese_v1.py
c7781d7fae11202b022c5f5ddc4df502945dab76727bccd3d2e9450d321f5feb  essais-contre-lecture/e15_richesse_calculable_par_l_agent_v1.py
e84b014ca8796a28340391b82469803915c334cd7a81a0af74f0a0808364c371  essais-contre-lecture/e16_heritage_dans_le_duel_v1.py
27434831bb00fc995d6341d99907d681474c181238fe1ee8a9062a386cefdcba  essais-contre-lecture/e16b_resume_v1.py
91b3c648b2e678367d92e700cb6e4511289f19cf3d8488c28bd9405ad8622000  essais-contre-lecture/e17_nombre_issues_defaut_v1.py
ac3acb8fcb6d0323867db81b633ed08c300046944bf13b334b3e27ed4a1e7702  essais-contre-lecture/e1a_balayage_richesses_v1.py
1b783c20815a434039fb155bf783ae7e22a2a818d8b50d7c6d6199f9b2ac6cab  essais-contre-lecture/e1b_heritage_sur_banque_pipeline_v1.py
5d00e44c36f2a7be6e462d6f7906cb024561f2c2eda77c38b1ae77edb98d0627  essais-contre-lecture/e1c_heritage_nul_permutation_v1.py
06a60a73ec03488d090d01023ac8b3d5f1116e36d1d7d2ad5543d060c9b341b6  essais-contre-lecture/e1d_part_finale_positive_v1.py
a5e520a18e2b1ada5acf7c786f65d26a61e016d283d5fff92e975537887c9f05  essais-contre-lecture/e2_ebh_m_apres_issues_v1.py
677f65c34c8cc38738ec320c27b046032510e2502e0a88df94750dfa571d39be  essais-contre-lecture/e3_sans_urne_loi_sans_remise_v1.py
a8dade76ad19048481149d6659d14af97840c00801acdaec91190073f4da770e  essais-contre-lecture/e4_ebh_puis_filtre_v1.py
d734a649c8bca49984a50ca50f47d5ac69c4053b31184ee4ce8006a80108df2f  essais-contre-lecture/e4b_ebh_temoins_vrais_v1.py
416cab2b5114affc8f1b6f5f407d78de4e7b820fe89821248d6521e05cce2eae  essais-contre-lecture/e4c_ebh_pire_cas_v1.py
c805885ff0147249b9e90557f24e0063759678c16e1cfc7b4a43236a533945da  essais-contre-lecture/e5_temoins_reconnaissables_dents_v1.py
9e0bc6035d487c1865d6170ae59ad3993b741b22f1de2cbfdd33e965efc553cf  essais-contre-lecture/e5b_qualite_temoins_faux_v1.py
e0d2a40da0d36e69d7ad32e73bfe8b0b41ed630a1844565baed43c0559a61687  essais-contre-lecture/e5b_qualite_temoins_faux_v2.py
475a205c663db45e5bf3c155e36372f9f7e55d67fdfe9f908e30d0fe3e52b344  essais-contre-lecture/e6_canal_texte_verificateur_v1.py
23118c2e95b0e6582d6b33b391f5de3eee92766311b0b7d52a4c3e4951b71bd8  essais-contre-lecture/e8_sans_regard_vers_l_avenir_v1.py
1b7aaa9ed4a1714fd5938c070c8fadcf63aac5717ebec07d27167af16986d680  essais-contre-lecture/e9_temoins_vrais_etablis_v1.py
```

### Sorties principales

```
f27f06e2cd7f13223fa34f8441b8cb175a33eba793a76fc121ad21f41e3c0f47  sorties/e0/e0-resultat-v1.json
1b52435efdd563a56317d121c39a3a4d87baa7dd013bad5205166bdc2b7a23c7  sorties/e1a-richesses-v1.json
774e3cd86081a692c92c7f0f28254493857ddb32ddc420f732505e9bb70409d8  sorties/e1b-sans-urne-informe/e1b-resultat-v1.json
26b8f851dac47f55b179c1ac7deef6c95317a8647e3d910890bf3b7018134ee7  sorties/e1c-heritage-urne1-r200-g5-v1.json
5bbe46edc58482b33b3733cdbc439884aeff11be7413bb780d0c68f2e79c1547  sorties/e1c-heritage-urne0-r200-g5-v1.json
2aae1d081e94f3f949bc74fdc4a74feb1e54e822721820e44986e3728531c2e9  sorties/e1d-finale-positive-urne1-r100-v1.json
aa68232a2407c8e9a0f73a95cf8da35b0769b4f66e46fc2ae1f43d3fbd083bb4  sorties/e1d-finale-positive-urne0-r100-v1.json
1f7fd75f4c10e18ea19cd5eb0af9c47bf0a4bca25e0c5434d66370f3770f23ff  sorties/e2-ebh-censure-urne1-informe1-r200-v1.json
d3ae5e969f04865972897d0672edf73454057157a7e883e725b00e3fbcc9e9a1  sorties/e2-ebh-censure-urne0-informe1-r200-v1.json
c940a41446ecdb02a737ec4e22c37ed31e29e9eb02764076a4c4507f2b64dc4c  sorties/e2-ebh-censure-urne0-informe0-r200-v1.json
e95f0afa0578680c811c9f0116cbf94aa0a651c976af507cd1766925322b25cd  sorties/e3/e3-resultat-v1.json
c084eb2fc0cefdc8c553a0e60a48653bbe640cf48a0ddbe49ec9b004e342617a  sorties/e4-ebh-puis-filtre-r4000-v1.json
3d8e3c4eca3742e46634f21986e43755423d62903f813191fc69262e40ac4bae  sorties/e4b-ebh-temoins-vrais-r4000-v1.json
23d3b86526edf6f2934923affc2092dd4ca9c31e9a96990acd342696e901d0c8  sorties/e4c-ebh-pire-cas-r20000-v1.json
1b729f9038c1b02195169dacb3776e53d2cd610d0424f73a31cf7b99f2100cb0  sorties/e5/e5-resultat-v1.json
1cef159fdd7ee6e99070325c1ba186fa8122b4ff3cd749eab742dce67f27d6b0  sorties/e5b/inutilise/e5b-resultat-v1.json
1cef159fdd7ee6e99070325c1ba186fa8122b4ff3cd749eab742dce67f27d6b0  sorties/e5b-v2/e5b-resultat-v2.json
8ec3d3cfee15116c604d08e2a6c93ff29ecea9a7707946ef72c70d2a9f89bc6e  sorties/e6/e6-resultat-v1.json
c18dbc757cb4b9d8d4ef47195a19df829460a09b9eea69b2d308a6bb7db3924f  sorties/e7-cli-banque-a/manifeste.json
d2b228b3ece411cef46a03ab6b31aa22dc8fc3c13bbe418e0b65a7f709e57679  sorties/e8-prefixe-v1.json
b135b5c478f3031823b8e8d797743e8daaefdd07de3e7e621e9adb25316fc667  sorties/e9-temoins-vrais-v1.json
60943438ebe1bf601ef6f3976fd0d97ee78663bfceade1c798d444b071cd2104  sorties/e10/e10-resultat-v1.json
153826bc6c0843a42579803ee341926b0bfc6d63b691b063f4c73b169a4619dc  sorties/e11-garde-banque-v1.json
5785ebfaf190954940e33e4b511438702393b1c5f616c823278841956a1c2cfc  sorties/e12-connu-retouche-v1.json
b5352fed385938ea007d4e50a098abb9f97b8e0a7434f22deb46c0f7cb5e1fb9  sorties/e13-relais-course-resume-v1.txt
04ae4191fc8abaed29253bcc075ccee64b7bc5f02314cd8432b186987521366b  sorties/e14/e14-resultat-v1.json
56af848db4bfb40d88e786e106f5c6fc75271895739c770531a2820393718349  sorties/e15-richesse-agent-v1.json
d946dee511fe67ed0e0e4b88fa63e57796d10a8da9c686280fc98b7eae2a2b3f  sorties/e16/e16-resultat-v1.json
b65ee57de6f293a05fac70b58dc70b534f996da301c3f59a9a1833b148916da0  sorties/e16-bis/e16-resultat-v1.json
6349056ab9cd69116d0f3df0378577d7b4e680c69144de5a5b2f4e56a3dc9a1a  sorties/e16b-resume-v1.json
1437fc532ec79fc34ed1947222c2bcfa482fd925cfacb64b92040691be9e59a6  sorties/e17-nombre-issues-v1.json
a6faaebbeef446c6a8067068c5c62055d785f897e39170c698f0dfb695e13437  sortie-essais-complets-v1.txt
a16881856ad7ef6e3be64202638e5f60e9ecc4ae4964edeb5a0214f216b25021  sortie-essais-complets-v2.txt
```

### Annexe complète

`empreintes-essais-et-sorties-v2.txt` (`d32a85c2085cc1ae0cca6eeca9570252e08daeba58ace13d503be2368ec606e2`, 21 387 lignes) :
toutes les sorties (dossiers des courses compris), les scripts, les deux passages de la suite d'essais et la liste des
fichiers lus. La v1 de l'annexe (`59f5bf7a1791c6e4ff06722fb6fa0772e0bc1b664fdc58f9bc3392e96209178a`), écrite avant les
dernières sorties, reste telle quelle.

## Note de fin : le dossier d'origine bouge (v11 en cours, non validée)

À 18:51 UTC, `git status` montre dans le dossier d'origine des modifications non validées, datées de 18:45 à 18:51 UTC
(une autre session ; aucune de mes commandes n'y écrit) : `pole/cycle.py`, `pole/memoire.py`, `pole/pole.py`,
`pole/adaptateurs.py`, `pole/relais_reel.py`, `pole/proposeurs_references.py`, `demonstrations/duel_proposeurs_v7.py`.
Lues sans contre-lecture, elles visent : m fixé avant les issues (C3) ; e = 0 avant le tri pour une fille sans marge
(une partie de C2 — les témoins vrais restent dans k*) ; tranches exigées avec l'héritage **à la ligne de commande
seulement** (C1 — les bras de référence du duel appellent `executer_pole` directement, `e16`, et n'y passent pas) ;
moniteur dans la signature (C9). Ce rapport porte sur l'instantané v9 (et vaut pour v10) ; la v11 demandera sa propre
contre-lecture.

Heure de fin : Tue Oct 27 18:51:45 UTC 2026 (lue sur `date -u`).
