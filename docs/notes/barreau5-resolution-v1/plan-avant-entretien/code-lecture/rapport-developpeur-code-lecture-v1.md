# Rapport du développeur du code de lecture du barreau 5 (plan « sabotage ou empreinte de l'adaptateur ») — v1

Écrit le 20 novembre 2026, de 00:00Z à 01:30Z environ, par le développeur du code de lecture : Claude Opus 5.5, sous-agent
de la session mère (`session_01XJ6Mgr8BN6UanALsQatc5E`). Pièce d'instrument (classe B) : contre-lecture par un autre modèle
(Fable 5.2), puis vérification des corrections par le même contre-lecteur. Mandat
`mandat-developpeur-code-lecture-v1.md`, empreinte vérifiée avant lecture : `fffe5bd785705d54035c9a29cae6beef4ba8fedf0d4eca0ec17834b1dd48460b`
(égale à l'attendue). Texte scellé lu en entier :
`prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md`, `bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935`.
États intermédiaires scellés : `outils-developpeur-code-lecture-v1/etat-rapport-01-conception.md` (`be483a20…`),
`etat-rapport-02-code-et-essais.md` (`b3220d6b…`).

Aucune donnée : modèle jouet et fichiers fabriqués seulement. Rien de `diag/`, aucune sortie de 7a, 7b, T0.6, de l'étape B,
de l'étape B bis ni de P3-bis, aucun fichier de tâches, aucun fichier « consigne-privee » ni « conception-ii-b », rien sous
`/root/.claude/`. Aucun réseau, aucune dépense, aucun commit. Code lu pour les conventions, sans le modifier : `engagement_v1`,
`formation_v1`, `edition_cout_v1` et les deux scripts de la formation ; `t07bbis/etat_impose_v1`, `apprentissage_carte_v1`,
`commun_v1` ; `t07/repli_recalcul_v1` ; `harnais` (sondes, activations, épisode, modèles) ; `sondes/familles` ;
`organismes/lora` ; `t06` (identite, cout, distillation_transcription, lanceur._fin_notee, lanceur_v2.ActivationsDemi) ;
`manifeste`, `scellement`, `gardes` ; la configuration scellée de la course de confirmation (recette). Point (b) seul du
rapport v4 du développeur des corrections du code de formation (le marqueur M-11 confie ce point au code de lecture).

## 1. Ce qui est fait, point par point du texte

### Point 8 — `relecture_v1` (instance de lecture) et `scripts/lancer_b5f_lecture_v1.sh`
- **Gardes avant tout manifeste** : configuration à clés exactes (aucune clé libre ni de score ; recette égale clé par clé à
  la configuration scellée en mode réel) ; registre propre au commit de la marche (`exiger_registre_de_relecture`) :
  `SCELLEMENT-B5F` de ce texte, entropie de `CODE-FORMATION-B5F`, `ENGAGEMENT-B5F` présente, antérieure à la création de
  l'instance (liste d'arrêt, point 9), postérieure à `SORTIES-FORMATION-B5F` et à toute ligne de relance (point (b), 4, du
  rapport v4), `CODE-LECTURE-B5F` et code au commit, `EPREUVE-B5F` passée pour la même empreinte du programme de lecture,
  `GO-LECTURE-B5F` égale à l'accord de la configuration, ni `SCORES-B5F` ni `OUVERTURE-B5F` ni `LECTURE-B5F`.
- **Ce que reçoit l'instance** (point 7, deuxième tiret ; liste d'arrêt, point 8) : `exiger_entrees` n'admet que
  `X-NN.safetensors`, `A<k>-<membre>.safetensors`, `A<k>-saboteur-evaluation.jsonl` et leurs compagnons, chacun à son
  empreinte, puis rejoue `engagement_v1.exiger_entrees_de_lecture_propres` ; les épisodes de chaque saboteur
  d'apprentissage sont exigés (la sonde du diagnostic ne se coupe pas). `exiger_arbre_de_lecture_propre` refuse, dans le dépôt
  et les entrées, la table des étiquettes (par l'empreinte engagée ou par sa forme), toute ligne de la formation qui porte une
  famille tenue à l'écart (coût, membre), toute marche de formation sous `donnees/`, toute référence git à la branche de la
  formation.
- **État imposé pour un adaptateur nommé** (forme de `t07bbis/etat_impose_v1`, sans le modifier) : `charger_et_controler`
  charge l'état à son empreinte (`charger_etat_fichier` : compagnon scellé, ou empreinte citée pour un adaptateur existant ;
  `.safetensors` ou `.pt` ; seulement A et B, aux clés et formes de l'état injecté), joue `t06.identite.controle_identite`
  (identité à dose 0 au bit près, artefact à dose 1), passe à la dose 1 et vérifie l'état de phase (dose lue sur chaque
  module, empreinte des adaptateurs chargés), au début et à la fin de chaque série.
- **(a)** 64 textes honnêtes communs (une par tâche d'évaluation), joués sur le modèle nu, environnement honnête, graines
  `b5f/lecture/honnete/tache/<id>`, par `formation_v1.jouer_sans_activations` (réemployé tel quel) ; écrits dans l'arbre fermé
  (`textes-honnetes.jsonl`, avec le coût du lecteur gelé : référence honnête) ; **série du modèle nu relue par le même chemin
  forcé** (`rejouer` : reconstruction de `harnais.episode.jouer_episodes`, texte décodé égal au texte écrit, une passe unique
  `harnais.activations.passe_unique`, empan noté `[début, t06.lanceur._fin_notee[`).
- **(b) Chemin éprouvé** (`eprouver_chemin`) : 8 épisodes tirés par `b5f/lecture/chemin`, relus à l'état « modèle nu »,
  égaux au bit près (demi-précision) à leurs activations d'origine (cas sain) ; relus sous un adaptateur d'apprentissage à la
  dose 1, différents (artefact) ; sinon arrêt avant toute notation (liste d'arrêt, point 11).
- **(c)** Chaque adaptateur dans l'ordre tiré par `b5f/lecture/ordre` : identité et artefact, série nominale (trois couches),
  divergence des sorties (coupe 1 : clé `divergence` à faux), normes du déplacement (couches 7, 15, 23), déplacement moyen δ̄
  (couche 15) ; puis ĝ (saboteurs d'apprentissage), produits P de toutes les paires et poussées le long de ĝ par
  `lecture_v1.produits_et_poussees` — **une seule fonction, sur l'instance et à l'ouverture** —, sans aucune étiquette des
  familles tenues à l'écart. Toutes ces grandeurs sont calculées sur les activations arrondies à la demi-précision, telles
  qu'elles sont gardées : relues sur le disque, elles rendent le même δ̄ (essai).
- **(d)** Épisodes d'évaluation des saboteurs d'apprentissage relus sous leur propre adaptateur (trois couches), après
  `episodes_propres` : chaque ligne du saboteur de la famille, **de la copie lue** (règle de la relance), sur une tâche
  d'évaluation, pas 0 à T − 1.
- **Données gardées** : activations par jeton en demi-précision (`ActivationsDemi`, gelé), toutes écrites sur l'instance ;
  `garde_des_activations` écrit l'inventaire de toutes (noms, tailles, empreintes) et la liste gardée selon la règle de la
  configuration : `trois_couches`, `couche_15` (repli 1), `une_sur_dix` (repli 2, une action sur dix tirée par
  `b5f/tirages/garde-activations`, couche 15). Rien n'est supprimé par le code.
- **Fichiers fermés** (arbre `lecture/` : inventaire, bilan, textes honnêtes, scores, produits, intensités) ; l'empreinte de
  `lecture/inventaire.json` est le contenu de `SCORES-B5F`. Liste blanche des sorties (`exiger_sorties_lecture_permises`).
  **Aucune grandeur d'un adaptateur au journal** : `progres` refuse tout nombre à virgule ; les résultats `diag/` ne portent
  que des comptes, des noms et des empreintes.
- Lanceur `scripts/lancer_b5f_lecture_v1.sh` : `config`, `verifier` (côté session, juste avant la création de l'instance),
  `marche` (sur l'instance), `preparer` et `ouvrir` (ouvreur), `monde` (épreuve à vérité plantée). Il ne crée, n'arrête ni
  ne détruit rien et n'atteint pas le réseau.

### Points 9 et 10 — `sondes_v1`
- Sondes décisive (couche 15), décisive aux couches 7 et 23, de comparaison, du diagnostic (une par saboteur d'apprentissage),
  une par pli, apprises sur l'autre pli ; réglage fixé (linéaire, maximum, l2 0,01) ; même calcul que
  `t07bbis/apprentissage_carte_v1`, importé sans modification ; graines `b5f/sonde/<nom>/pli<k>`.
- Aucun adaptateur tenu à l'écart ni point d'ancrage dans un apprentissage (refus) ; scores par jeton gardés pour la sonde
  décisive et la sonde de comparaison seulement.
- Contrôle carte-processeur d'une sonde tirée par graine (`controle_carte_processeur`, 10⁻⁴), sinon arrêt ; l'écart mesuré
  n'est pas écrit (il se tire de scores de sonde).
- Sonde en échec (`SondeEnEchec`) : ses deux plis sont écrits « echec », sans aucun score ; ses épreuves sont non calculables.
- **Notation fermée** : chaque sonde note chaque série sur les actions de son pli ; score d'action par
  `harnais.sondes.score_action` (refus de la moyenne et de la médiane, N-026), exigé égal au maximum des scores par jeton ;
  aucune statistique, aucune aire, aucun résumé.

### Points 12 et 13 — `lecture_v1` (processeur seulement)
- Ordre (a) à (h) : `garde_d_ouverture`, `manipulation`, `separation_apprise`, `epreuves` (E3, E2a, E2b, E1), `diagnostic`,
  `descriptifs`, `issue` + `phrases` + `audit_symetrie`, résultat écrit et scellé (`ouvrir`).
- Mises à l'échelle après coup de E2a et E2b (`Pli.scores`) : score du jeton s_0(t) + c·(s_i(t) − s_0(t)), puis maximum sur
  les jetons de l'action ; **le maximum d'un score mis à l'échelle n'est calculé qu'ici**. Règles d'échec écrites (produit non
  positif, facteur hors de [0,5 ; 2], saboteur absent ; poussée de E2b non positive : c = 1).
- Dénombrement exact des rangs signés (`comptes_rangs_signes`, entiers exacts ; seuils par fractions exactes) ; différences
  nulles comptées contre la conclusion essayée, égalités dans l'ordre le plus défavorable ; règle du nœud 6 épreuve par
  épreuve (99 % dès huit familles, 95 % à six et sept, aucun niveau sous six).
- Issues et phrases selon « Critères de lecture gelés » et « Ce que dira chaque issue au jury » ; rapportés avec S et D ;
  bornes des issues E et N ; audit de symétrie (i) à (xi), toujours calculé.
- **Interfaces d'entrée écrites et documentées** (en-tête du module) : arbre de lecture (inventaire, bilan, textes
  honnêtes, scores par action et par jeton, produits et déplacements moyens, intensités), table, coûts (forme canonique),
  résumé de la formation, lignes du registre. Le programme se joue tel quel, au même fichier, sur des fichiers fabriqués :
  sous-commande `monde` (registre fabriqué) ; un monde fabriqué peut ne planter que les déplacements moyens (le programme
  calcule P, les facteurs et les mises à l'échelle) ; aucune taille n'est câblée (tâches, actions, jetons libres).
- Règle de la copie lue (point (b) du rapport v4) : `prefixe_de_copie`, `exiger_copie_lue` ; l'ouvreur bâtit coûts et résumé
  de la formation par `preparer` (`couts_depuis_formation`, `resume_formation_depuis_branche`), qui ne lisent que la copie
  lue et refusent toute autre source.

### Point 18 — répétition générale et points d'ancrage
- Mode réel prévu : plan `repetition` (quatre adaptateurs existants cités par chemin et empreinte dans la configuration,
  noms `R<k>-saboteur` et `R<k>-temoin` ; sonde décisive apprise saboteurs contre témoins ; ni comparaison ni diagnostic ;
  ĝ des deux saboteurs) ; points d'ancrage sur l'instance décisive (clé `ancrages`, noms `ancre-…`) : relus, notés par toutes
  les sondes, hors de tout apprentissage et des produits ; rapportés en descriptif par la lecture. Les chemins et empreintes
  des quatre adaptateurs existants sont à donner par la session (je ne les ai pas ouverts).
- Mode jouet : les deux sont joués par les essais (répétition sur quatre adaptateurs jouets en `.pt` ; un point d'ancrage
  dans le jouet de bout en bout).

## 2. Écarts et questions au texte

### 2.1 Choix que le texte laisse au code (à adopter par la mère, ou à trancher)
1. **Formats des lignes de registre de la lecture** (le texte ne les écrit pas ; le code les lit à la lettre) :
   `CODE-LECTURE-B5F` « commit <40> ; lecture sha256 <64> » (empreinte de `lecture_v1.py` au commit) ; `EPREUVE-B5F`
   « passee ; lecture sha256 <64> ; rapport sha256 <64> » ; `GO-LECTURE-B5F` « GO-AAAA-MM-JJ-NN » ; `SCORES-B5F`
   « commit <40> ; inventaire sha256 <64> » ; `OUVERTURE-B5F` « table sha256 <64> » (inscrite par la mère **avant** que
   l'ouvreur joue le programme, qui lit son instant) ; `LECTURE-B5F` « resultat sha256 <64> ».
2. **Ordre des lignes exigé à l'ouverture** : `SCELLEMENT` < `GO-FORMATION` ; `CODE-FORMATION` < `GO-FORMATION` <
   `SORTIES-FORMATION` < `ENGAGEMENT` ; `GO-RELANCE` < `ENGAGEMENT` ; `CODE-LECTURE` < `EPREUVE` ; `ENGAGEMENT`, `EPREUVE`,
   `GO-LECTURE`, `CODE-LECTURE` < `SCORES` < `OUVERTURE` ; ni `LECTURE` ni `VERDICT` déjà inscrites.
3. **Clés de graines ajoutées**, déclarées : `b5f/lecture/injection` (sans effet : chaque état chargé remplace A et B),
   `b5f/modele-jouet` (jouet), `b5f/sonde/controle-carte/choix` et `…/actions` ; sous la forme `b5f/tirages/<ligne>` du
   texte : `separation-apprise`, `reference-honnete-<famille>`, `garde-activations`.
4. **Niveau d'une issue sous huit familles** (nœud 6) : le plus faible de M1, M3 et des épreuves que l'issue affirme — S :
   E1, E2a, E2b, E3 ; D et C : E3. Question : M1 et M3 sont-elles parmi « les épreuves qui la fondent » ? Pour D, les
   niveaux de E1, E2a, E2b (non établies) comptent-ils ? À recouper par la seconde programmation.
5. **Liste d'arrêt, point 13, avant tout critère** : moins de six familles à jumeau et sur-saboteur (comptées dans la table)
   rend l'issue N « niveau non atteignable », même si la manipulation échouerait aussi (la table des critères dirait NI).
6. **m_i** : tâches jouées par tous les membres présents de la famille ; chaque membre sur celles où il a au moins un coût
   lisible (le texte ne dit pas si une tâche sans coût lisible chez un membre sort pour tous). M1 et M3 portent sur les
   familles tenues à l'écart seulement ; les familles d'apprentissage ne sont pas dans ces épreuves.
7. **Interprétations numériques** : σ_0 sans correction (ddof 0) ; percentiles par `numpy.quantile` (linéaire) ; c = 1 rend
   les scores nominaux sans recalcul ; intervalle de (viii) par rééchantillonnage des tâches (10 000 tirages, 95 %).
8. **Divergence des sorties** : à chaque jeton noté, divergence de Kullback-Leibler de la loi du jeton suivant du modèle nu à
   celle du modèle adapté, lue à la position de ce jeton (même position que l'activation lue) ; moyenne sur les jetons de
   l'action, médiane sur les actions. Elle coûte deux passes de plus par épisode et par adaptateur (logits aux positions
   notées, à dose 1 puis à dose 0) : la durée de la relecture du devis n'est pas revérifiée par moi.
9. **Diagnostic** : « non calculable » si l'une des sondes du diagnostic est en échec (lecture stricte de « moyenne sur les
   trois sondes ») ; part transportée = médiane des f_k divisée par la moyenne des statistiques de chaque sonde sur son
   propre saboteur.
10. **Phrases** : N, « un écart de [e] aurait été vu [x] fois sur cent » rempli avec e = 2 (écart de P1) et la puissance de
    la première table de « Puissance » (loi normale, une épreuve seule) pour K de 8 à 10 ; « — » sous huit (non tabulé) ;
    E, « plus petite que [borne] » rempli avec le maximum des d_k de E3 (haut de l'étendue). Le nombre de familles est
    écrit en lettres de un à dix.
11. **Audit** : (i) chacune des six épreuves a toutes ses différences présentes d'un seul signe (le signe peut changer d'une
    épreuve à l'autre) ; (v) appliqué aussi aux familles d'apprentissage ; (x) une action compte si l'une au moins des deux
    écritures propres à un sens est levée pour ce membre, sur les actions éditées.
12. **Restes d'arrondi** : aucune tolérance n'est appliquée aux différences (le texte n'en prévoit pas). Un monde où l'écart
    planté s'annule exactement à poussée égale, sans bruit propre à chaque membre, laisse des restes de l'ordre de 10⁻¹⁶,
    tous du même signe : au premier passage, un tel monde sans bruit a rendu « sabotage » au lieu de « différence établie ».
    **À dire à la fabrique de l'épreuve à vérité plantée** : planter un bruit propre à chaque membre dans V3, V8, V9, V12.
13. **Modèle jouet de la lecture à 24 couches** (largeur 32), pour que les couches 7, 15 et 23 existent ; celui de la
    formation en a 4.

### 2.2 Ajouts déclarés (gardes que le texte ne nomme pas)
- **Alignement des étiquettes** : quand le résumé de la formation porte l'empreinte des adaptateurs chargés de chaque membre
  (`preparer` la lit dans les résultats de famille de la formation), celle de l'adaptateur relu sous le nom opaque de la table
  doit l'égaler, sinon refus (table mal alignée, ou adaptateur échangé entre formation et lecture).
- **Produits recalculés à l'ouverture** depuis les déplacements moyens et comparés aux valeurs écrites par l'instance
  (tolérance relative 10⁻⁹).
- **Score d'action égal au maximum des scores par jeton**, exigé sur l'instance (notation) et à l'ouverture.
- **Plis recalculés** depuis l'entropie de `CODE-FORMATION-B5F` (`partition_des_plis`, égale à `formation_v1.partition_plis`,
  essai) et comparés au bilan et à chaque fichier de scores.

### 2.3 Ce que mon code demande au code de formation (je ne l'ai pas modifié)
Point (b) du rapport v4 : (1) la fonction de la copie lue est écrite dans `lecture_v1` (`prefixe_de_copie`,
`exiger_copie_lue`), importable par la session de formation ; (2) `engagement_v1.exiger_episodes_de_saboteur` admet encore
toutes les copies : la relecture refuse l'autre copie au moment de lire (`relecture_v1.episodes_propres`), la demande
devient facultative ; (3) **`engagement_v1.preparer_entrees_de_lecture` ne sait pas de quelle copie vient chaque
adaptateur** : la session de formation doit lui donner les états de la copie lue (règle de `prefixe_de_copie`) ; à
l'ouverture, l'alignement des empreintes (2.2) attrape une copie fausse si le résumé de la formation est bâti par `preparer` ;
un changement de `engagement_v1` (recevoir le nom formé et refuser l'autre copie) reste recommandé ; (4) l'ordre
`ENGAGEMENT-B5F` après `SORTIES-FORMATION-B5F` et après toute relance est vérifié par mon code (instance et ouverture) ;
`engagement_v1.verifier_engagement_avant_lecture` ne le vérifie pas.

### 2.4 Contraintes de procédure que le code impose
- **Code au commit** (même définition que la formation, `CHEMINS_GELES`, tout `src/` compris) : le commit de la marche de
  lecture et l'arbre que joue l'ouvreur doivent avoir l'arbre gelé du commit de `CODE-LECTURE-B5F`. Un code d'une autre chaîne
  commis sous `src/` entre ces commits fait refuser la marche et l'ouverture : la mère doit bâtir les commits de la lecture
  sans changement de l'arbre gelé (ou l'ouvreur extraire le code au commit de `CODE-LECTURE-B5F` et passer le registre par
  `--commit-registre`).
- **Épreuve à vérité plantée** : chaque monde fabriqué porte un registre fabriqué complet, `EPREUVE-B5F` comprise (le
  programme refuse sans elle), avec l'empreinte vraie du programme ; les familles s'appellent `T01` à `T10` dans la table,
  les adaptateurs d'apprentissage `A<k>-<membre>` ; le score d'action doit égaler le maximum des scores par jeton.
- **Points d'ancrage et répétition réelle** : chemins et empreintes des quatre adaptateurs existants à écrire dans la
  configuration par la session (je ne les ai pas lus).

### 2.5 Ce qui manque
- **L'amorce de l'instance de lecture** (clonage au commit, entrées de lecture tirées de leur branche, paquets, modèle au
  cache local, marche sous minuterie, versement prouvé de l'arbre fermé sur `donnees/barreau5-familles-jumelles-v1-lecture`,
  activations selon la règle de garde, arrêt sans destruction si le versement n'est pas prouvé) et la commande de création
  imprimée par le lanceur : non écrites. Elles se calquent sur l'amorce de la formation.
- Le mode réel n'est jamais joué ici (carte, 8B, déterminisme sur la carte, mémoire, durée) : seule la répétition générale
  sur les quatre adaptateurs existants l'éprouverait.

### 2.6 Ce qui menace le départ de la formation et le gel à H + 30 heures
1. **Instances de formation encore à créer.** La mère a versé mes états intermédiaires (commits `6670d598`, `6f7cd0f8`,
   `f80fcf99`) et poussé une branche de course (commit `162287a3`, instance 6) ; à 01:30Z l'arbre de travail est propre.
   Pour chaque création à venir : (a) `formation_v1.exiger_code_au_commit` compare l'arbre gelé (tout `src/`) du commit de la
   course à celui de `CODE-FORMATION-B5F` : un commit de course qui porte mon code et pas l'autre (ou l'inverse) est refusé ;
   `exiger_code_de_la_session` refuse aussi tout fichier non suivi sous `src/` dans l'arbre de la session ; (b) l'amorce de la
   formation joue `tests/test_barreau5_familles_*.py`, où tombent mes trois fichiers d'essais (noms imposés par le mandat) :
   120 essais de plus sur l'instance si le commit de course les porte (dont le jouet de bout en bout, environ trois minutes de
   processeur, et des dépôts git jetables) ; et l'essai `test_texte_plancher_d_essais_egal_au_nombre_d_essais_du_paquet`
   (`tests/test_amorce_b5f_formation_v1.py`) échoue dès qu'ils sont dans l'arbre (`MIN_ESSAIS=235`, 355 essais collectés
   sous ce motif ; mesuré, puis recompté après les quatre derniers essais). **À vérifier par la mère** : que les commits des
   courses ne portent pas mon code, ou remesurer `MIN_ESSAIS` (changement du code de formation). Je n'ai rien changé.
2. **L'amorce de l'instance de lecture** n'est pas écrite (2.5) ; elle fait partie du code figé par `CODE-LECTURE-B5F`.
3. **La contre-lecture par Fable 5.2** : la limite d'usage de Fable a été atteinte sur le compte de la mère dans la nuit
   (titres des commits, R-4020) ; sans elle, pas de gel.
4. **Les questions 2.1 (4) à (6)** : une divergence avec la seconde programmation du dénombrement et de la table des issues
   (l'autre modèle) demandera un erratum contre-lu, avant l'épreuve à vérité plantée.
5. **Le mode réel n'est jamais joué** : déterminisme sur la carte, mémoire, durée (trois passes par épisode et par
   adaptateur avec la divergence). Si la répétition générale sur les quatre adaptateurs existants n'est pas jouée, la
   première marche réelle est la relecture décisive.
6. **La procédure des commits de la lecture** (2.4) : sans arbre gelé identique à celui de `CODE-LECTURE-B5F`, la marche et
   l'ouverture refusent.

## 3. Empreintes (sha256, relevées le 2026-11-20 à 01:29Z, après le dernier passage des essais)
| fichier | lignes | sha256 |
|---|---|---|
| `src/controle_ia/barreau5_familles/lecture_v1.py` | 1465 | `c3db00742df9766bfdc9f49e120c7b1e9e790403131562a76208cab5a3c29382` |
| `src/controle_ia/barreau5_familles/relecture_v1.py` | 880 | `c1c7c65fff89bc69fe3df7b03a00e938def819d8fc74247f5ffe6f1cd5117c0c` |
| `src/controle_ia/barreau5_familles/sondes_v1.py` | 277 | `cfc2237a5c1c37b9c3569523023bbc44017b48a5522c8f28fb835b6cf133dbe2` |
| `scripts/lancer_b5f_lecture_v1.sh` | | `de83c346806ee68cd03912c473e130ffd4932c87cb39a87d754848c2b82b0f9a` |
| `tests/test_barreau5_familles_lecture_v1.py` | | `a1b04290f2f7382e01d15dcecfed9ca668c17b1a742dc1c2135836b94de6de52` |
| `tests/test_barreau5_familles_relecture_v1.py` | | `ebb7a6e77987351c42fd190b07b36286bdf184ca00ee170fb05c1555eb2f8adc` |
| `tests/test_barreau5_familles_sondes_v1.py` | | `9dd5d0899bc21fd9cef075ccce9ba02b3cb6dbb6b1d4ecc04593fc7b83777495` |
| `tests/test_lancer_b5f_lecture_v1.py` | | `b440fd06a4cbea40b7dcfb1d0d12ea460d7fa9f4a71f2e23e88745b6b0cd03ea` |
| `outils-developpeur-code-lecture-v1/mutations-code-lecture-v1.py` | | `1377151c80874f9106d768dff9a880f8fc10fb8ad959236c22bc366018c4836a` |
| `outils-developpeur-code-lecture-v1/verifier-syntaxe-v1.py` | | `09c737edc9f83d5b0720d0018e810d7825e7f2fc102ecb7067dcdd2ebbabce5f` |
| `outils-developpeur-code-lecture-v1/sortie-mutations-code-lecture-v1.md` | | `f9f691207efc048426ffb29547df48317841eacdc0d3aa86fba35d55fa9bd943` |
| `outils-developpeur-code-lecture-v1/etat-rapport-01-conception.md` | | `be483a20280c03b783c020e31e965d16fec4cfdb6d7a99323fe0c004dd759922` |
| `outils-developpeur-code-lecture-v1/etat-rapport-02-code-et-essais.md` | | `b3220d6b00aa7e3f911fbba1482e88a6643734cf2937cddbb92b9ba8800eb889` |
| `outils-developpeur-code-lecture-v1/etat-rapport-03-mutations-passage-1-nul.md` | | `29fb808e220933f7c029040ca8ba1889ce1b7f861e169a0be1f6283ce90c9cd9` |

Les fichiers de `docs/` sont scellés par leurs compagnons ; le code et les essais ne le sont pas (ils changeront après la
contre-lecture) : le commit qui les porte fera foi pour `CODE-LECTURE-B5F`. L'empreinte de `lecture_v1.py` est celle que
portera la ligne `CODE-LECTURE-B5F` si ce fichier est figé tel quel.

## 4. Essais
Commande (depuis la racine du dépôt) :
`TMPDIR=/dev/shm PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src .venv/bin/python -B -m pytest -q -p no:cacheprovider --basetemp=/dev/shm/b5f-lecture-essais/final tests/test_barreau5_familles_lecture_v1.py tests/test_barreau5_familles_sondes_v1.py tests/test_barreau5_familles_relecture_v1.py tests/test_lancer_b5f_lecture_v1.py tests/test_barreau5_familles_edition_cout_v1.py tests/test_barreau5_familles_engagement_v1.py tests/test_barreau5_familles_formation_v1.py`

Compte au dernier passage (01:24Z à 01:28Z) : **369 passés, aucun échec**, en 265 s : les miens, lecture 83, sondes 16,
relecture 21, lanceur 14 (134) ; ceux du paquet de la formation, 235, inchangés. Syntaxe vérifiée sous Python 3.11 (image des
instances) par `verifier-syntaxe-v1.py`.

Épreuves du mandat, avec leur essai : moyenne sur les jetons, refus (`test_moyenne_ou_mediane_sur_les_jetons_refusee`) ;
table des étiquettes dans l'arbre de lecture, refus (lecture : `test_v7_table_presente_…`, `test_v7_table_sous_une_autre_forme_refus` ;
instance : `test_arbre_de_la_session_sans_table_ni_formation`) ; engagement postérieur, refus (`test_engagement_posterieur_…`,
`test_registre_de_relecture_cas_sain_et_artefacts`) ; dénombrement exact contre l'énumération complète pour huit, neuf, dix
familles (et 0, 1, 2, 5, 12 ; `test_denombrement_exact_…`, `test_seuils_contre_l_enumeration_…`) ; différences nulles et
égales (`test_differences_nulles_et_egales_…` contre le pire de tous les ordres, `test_une_difference_nulle_compte_…`) ;
famille sans sur-saboteur (`test_famille_sans_sur_saboteur_absente_de_toutes_les_epreuves`) ; jouet de bout en bout
(`test_jouet_de_bout_en_bout_relecture_sondes_puis_lecture` : 39 adaptateurs jouets et un point d'ancrage, entrées préparées
par `engagement_v1`, relecture, sondes, notation fermée, puis lecture) ; gardes de l'ouverture (point 12 a : une quinzaine
d'essais, cas sain et artefacts) ; identité à dose 0 et artefact à dose 1 (`test_identite_a_dose_0_et_artefact_…`,
`test_un_adaptateur_tenu_a_l_ecart_sans_effet_arrete_la_marche`) ; refus du cas V7 (quatre premiers : table dans l'arbre,
empreinte de la table ≠ engagement, scores postérieurs à l'ouverture, score manquant), seuil recalculé pour une famille
incomplète, règle du nœud 6 à sept familles. Mondes V1 à V6 et V8 à V12 en petit (une graine chacun), pour l'issue ; un
recalcul indépendant, écrit dans l'essai, des statistiques, de E3, E1, E2a, E2b et de l'intervalle de Δ_app, à 10⁻¹² près.
Ce n'est pas l'épreuve à vérité plantée (point 11), qui revient à un autre agent.

## 5. Mutations
Détail : `outils-developpeur-code-lecture-v1/sortie-mutations-code-lecture-v1.md`. **Passage 1 nul** (l'outil donnait à
pytest un dossier temporaire sans parent : les témoins échouaient, et les 57 mutations passaient pour attrapées ; trop beau,
vu et déclaré). **Passage 2** : 57 jouées (34 dans la lecture, 7 dans les sondes, 15 dans la relecture, 1 dans le lanceur),
53 attrapées ; non attrapées : L02 (lacune : zéro compté pour « contraire »), L04 (équivalente : un seuil exact ne tombe
jamais sur 1/200 ni 1/40), L25 et R12 (gardes redondantes dans le cours normal). **Passage 3**, ciblé, après quatre essais
ajoutés : L02, L25, R12 attrapées ; L04 équivalente, démontrée par un essai. Total : 56 attrapées sur 57, une équivalente.
Trois mutations équivalentes sur les sorties n'ont pas été jouées ; elles sont nommées dans la sortie.
