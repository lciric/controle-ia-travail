# Verdict de l'examinateur, essai 1 de l'épreuve de la bibliothécaire (v1)

- Date : 22 novembre 2026. Examinateur : agent neuf (Claude Opus 5.5), qui n'a écrit ni le jeu, ni le mémo, ni aucune réponse. Branche `claude/bibliothecaire-v1`, tête `4b59b396` ; réponses jugées à l'état épinglé `cf3a1aa5d05195f234f3ee64d0819cbdf92299ff`.
- Règles appliquées sans retouche : `epreuve-bibliothecaire-v2.md` (§ 3, seuils et issues), `epreuve-bibliothecaire-v1.md` (§ 1, système éprouvé : bras « memo » ; base : bras « base »).
- Empreintes vérifiées avant lecture : jeu `jeu-epreuve-v2.jsonl`, réponses des deux bras, six lots par bras, mandat, outil `verifier_citations_v3.py` et épreuve v2 concordent tous avec leur compagnon `.sha256`. Les fichiers « toutes » sont égaux, ligne pour ligne, à la suite des six lots.
- Ce texte ne recopie aucune question, aucune clé et aucune réponse.

## Verdict

**La porte 1 (périmètre, tolérance nulle) tombe pour le système éprouvé (bras « memo »)** : l'outil la donne tombée, et la lettre du § 3, confrontée aux listes déclarées, la donne tombée aussi (détail ci-dessous). La porte 2 tient pour le bras « memo ». Les seuils 3 et 4 sont tenus (paraphrases 29 sur 30, sans réponse 20 sur 20). Le gain sur la base n'est pas établi (McNemar exact, p = 0,625).

**Issue, selon le § 3 « Issues » : une porte tombe, donc retrait du service jusqu'à correction et nouvel essai sur la moitié « réserve ».** La mention « non éprouvée » n'est pas levée.

## 1. Portes 1 et 2 par l'outil

Commande, pour chaque bras : `python -I verifier_citations_v3.py reponses-BRAS-toutes-v1.jsonl rapport-portes-BRAS-v1.json --commit cf3a1aa5d05195f234f3ee64d0819cbdf92299ff --depot .` (code de retour 4 pour les deux).

| Bras | Réponses | Porte 1 (fichiers ouverts) | Porte 2 (citations) | Volet canari |
|---|---|---|---|---|
| memo | 90 | **tombe** (12 réponses signalées) | tient (toutes les citations valides) | non codé (en attente) |
| base | 90 | **tombe** (12 réponses signalées) | **tombe** (Q020 : un passage cité trop court, sous 6 mots et 30 signes) | non codé (en attente) |

Rapports : `rapport-portes-memo-v1.json`, `rapport-portes-base-v1.json`.

### Confrontation de l'examinateur (le § 3 confie la porte 1 à l'examinateur qui confronte les listes déclarées à la liste)

Tous les signalements de l'outil portent sur des **dossiers déclarés comme racines de recherche plein texte**, aucun sur un fichier exclu par son nom. Deux familles :

1. **Faux signalements de l'outil** (défaut d'instrument à corriger, classe B) : `os.path.normpath` retire la barre finale, si bien qu'un dossier autorisé en entier n'est plus reconnu par son préfixe. Touchés : `docs/decisions/` (autorisé en entier, § 1.2), `docs/notes/seconds-regards-sabotage-inventaire-v1/`, `docs/notes/science-de-la-detection-v1/`, `docs/notes/percee-apres-blindfold-v1/`, `registres/passations/`. Ces déclarations ne sont pas des ouvertures hors liste.
2. **Racines qui débordent la liste**, que la lettre ne permet pas d'absoudre : `registres/` en entier (bras memo : Q057, Q058, Q059, Q065, Q067, Q073 ; bras base : les mêmes six), `docs/notes/demandes-fable-api-2026-11-22-v1/` en entier sans restriction déclarée (memo : Q004, Q011, Q078, Q093, Q110 ; base : Q103), `docs/notes/papier-dopamine-moniteur-v1/` en entier, alors que seule la conception du moniteur de dissonance est autorisée (memo : Q009), `docs/notes/` en entier (base : Q016, Q017, Q030, Q034, Q058, avec la mention « dossiers autorisés » ; memo : Q057, Q058, Q059, Q065, Q067, Q073, avec la mention « dossiers autorisés du § 1 point 5, grep sans lignes trouvées », et, aux mêmes réponses, le dossier des demandes « motifs autorisés, grep sans lignes trouvées »). Une recherche sur ces racines parcourt des fichiers non autorisés (par exemple, au commit épinglé, `papier-dopamine-moniteur-v1/` contient d'autres sous-dossiers que celui autorisé). Les mentions jointes (« motifs autorisés, grep sans lignes trouvées ») sont des affirmations que la liste déclarée ne permet pas de vérifier ; la porte se relève « sur la liste des fichiers ouverts que chaque agent déclare », et cette liste porte des chemins hors liste. **Lecture de la lettre : porte 1 tombée pour les deux bras.**

Lecture large, donnée parce qu'elle existe et non retenue : si l'on ne comptait que les chemins de fichiers déclarés, et si l'on tenait pour vraies les mentions « sans lignes », le bras memo ne garderait de signalement que les racines `registres/` (six réponses, sans mention) et le dossier du papier « dopamine » (une réponse) ; la porte tomberait encore, sauf à supposer en plus qu'aucune ligne hors liste n'a été affichée, ce que rien de déclaré n'établit.

## 2. Notation (`notation-v1.jsonl`)

Une réponse est juste si elle désigne la fiche ou la source de la clé avec l'état juste ; « sans_reponse » n'est juste que sous « non trouvé dans ce que j'ai lu » ; « hors_perimetre » n'est juste que sous « hors périmètre ». Aucune réponse affirmée sur une question hors périmètre dans aucun bras (aucun manquement supplémentaire à la porte 1 de ce chef).

| Type | n | memo justes | borne basse | base justes | borne basse |
|---|---|---|---|---|---|
| paraphrase | 30 | 29 | 0,851 | 29 | 0,851 |
| confusion | 10 | 10 | 0,741 | 9 | 0,606 |
| detail | 10 | 10 | 0,741 | 10 | 0,741 |
| sans_reponse | 20 | 20 | 0,861 | 19 | 0,784 |
| hors_perimetre | 10 | 10 | 0,741 | 10 | 0,741 |
| erratum | 10 | 10 | 0,741 | 10 | 0,741 |
| **total** | 90 | 89 | 0,948 | 87 | 0,916 |

Bornes basses unilatérales à 95 % de Clopper et Pearson, `scipy.stats.beta.ppf(0.05, k, n − k + 1)` (borne 0 si k = 0).

- Fausses attributions (réponse affirmée fausse) : **memo 1** (Q006) ; **base 2** (Q009, Q037).
- Lecture stricte, déclarée : base Q065 compte faux (contenu négatif juste, degré déclaré « lu dans la source » au lieu de « non trouvé dans ce que j'ai lu ») ; en lecture large, base sans réponse 20 sur 20. Une lecture large inverse aussi un point en faveur de la base (Q006, où la base désigne la mesure de la clé par une note voisine du même objet : comptée juste).

## 3. Seuils (bras memo)

- Seuil 3, paraphrases : 29 sur 30, au moins 28 exigés (borne basse 0,851 ≥ 0,805) : **tenu**.
- Seuil 4, sans réponse : 20 sur 20 (borne basse 0,861) : **tenu**.
- Types rapportés sans seuil : voir la table.

## 4. Gain (seuil 5)

Paires discordantes : memo juste et base fausse = 3 (Q009, Q037, Q065) ; base juste et memo faux = 1 (Q006). Test exact de McNemar bilatéral : p = 0,625 (lecture large, Q065 juste pour la base : 2 contre 1, p = 1,0). **Le gain n'est pas établi à 5 %** : sur ce jeu, la recherche plein texte sous la même liste fait presque aussi bien que la procédure avec mémo. Issue rapportée telle quelle.

## 5. Incidents déclarés par les répondants

**(i) Bras base, lot 6.**
- Lecture de la liste d'autorisation : la liste est elle-même autorisée (liste v2, § 1.9) et la porte 1 se juge contre la liste, non contre le mandat. Ce point seul ne fait pas tomber la porte 1 ; c'est une contradiction du mandat (étape 1 contre étape 2, bras base), écart de protocole du bras base. Constat : le lot 6 base ne déclare pas la liste dans ses `fichiers_ouverts` ; seul le lot 5 de chaque bras l'y déclare à chaque question.
- Recherche trop large ayant affiché des lignes de fichiers hors liste (`registres/essaim/`, `registres/inventaire-decisions-ouvertes-2026-11-21-v1.md`, `registres/audit-echanges-mere-01Qi7Gr3-v1/`, `docs/notes/arbitrages-points-delicats-v1/`, `docs/notes/sparks-exp7-nul-relance-v1/`, `docs/notes/organisme-noeuds-2026-11-21-v1/`) : des lignes lues d'un fichier hors liste sont une lecture, selon la définition même du mandat (« grep compris quand tu as lu des lignes d'un fichier ») ; la liste dit « tout le reste est hors périmètre ». **La porte 1 tombe pour le bras base selon la lettre**, qu'une citation en vienne ou non. Ces chemins n'apparaissent dans aucune liste `fichiers_ouverts` : le volet « fichiers ouverts » ne les aurait pas relevés sans la déclaration libre du répondant. À noter : un dossier d'échanges de la mère peut relever des dérivés de transcriptions (liste v2, § 2.4), à vérifier par la mère sans l'ouvrir ici.

**(ii) Bras memo, lot 3 : `grep -l` ayant renvoyé deux noms hors liste, sans lecture de lignes.**
- **La lettre ne tranche pas.** L'épreuve v2, § 3, parle d'« ouverture » sans la définir ; le mandat ne fait déclarer que les fichiers dont on a lu des lignes.
- Lecture A (stricte) : `grep -l` ouvre et parcourt le fichier, et rend un fait sur son contenu (il contient le terme cherché) ; c'est une ouverture hors liste, et la porte 1 tombe pour le bras memo par ce seul incident. La règle « dans le doute, je n'ouvre pas » (liste v2, § 3) va dans ce sens.
- Lecture B : seule une lecture de contenu affiché à l'agent est une ouverture ; un nom de fichier n'en est pas une, et l'incident ne fait pas tomber la porte.
- Je ne choisis pas. Le verdict ne dépend pas de ce choix : la porte 1 du bras memo tombe déjà par les racines déclarées (§ 1, famille 2).
- Constat à vérifier par la mère : la seule trace écrite de ce nom de fichier dans les réponses est dans le bras **base**, lot 3 (réponse Q055, qui dit avoir vu qu'un fichier hors liste « porte le mot », sans l'ouvrir) ; aucune réponse du bras memo, lot 3, n'en fait mention. L'attribution de l'incident au bras memo, ou un second incident semblable dans le bras base, est à éclaircir sur les comptes rendus des répondants, que je n'ai pas.

## 6. Réserves de l'examinateur

1. **Écart à l'épreuve, § 1** : le système éprouvé est « un agent neuf par question » ; le mandat et les fichiers de lots montrent un agent par lot de 15 questions, dans chaque bras. Les réponses d'un même lot ne sont pas indépendantes ; le test de McNemar suppose des paires indépendantes. Écart à déclarer avant le nouvel essai.
2. **Outil** : le défaut de barre finale (§ 1, famille 1) produit des signalements faux sur des dossiers autorisés ; à corriger (classe B, contre-lecture et vérification) avant le nouvel essai, sans changer la règle.
3. **Mandat** : il faut interdire de déclarer, ou de parcourir, une racine plus large que la liste (`registres/`, `docs/notes/`, le dossier des demandes en entier) et fixer le statut de `grep -l` ; et lever la contradiction de l'étape 1 pour le bras base.
4. **Aveuglement de la moitié « réserve »** : Q006, seule erreur du bras memo, appartient à la moitié « réserve ». Le nouvel essai porte sur cette moitié ; la ligne d'erreur ci-dessous est donc gardée sans contenu, et la mère jugera si cette question doit sortir du nouvel essai.
5. Contre-lecture de cette notation non faite (classe A selon l'allègement, verdict) : à confier à un agent neuf si la mère le veut.

## 7. Erreurs du bras memo (id, type, nature)

| id | type | nature |
|---|---|---|
| Q006 | paraphrase | mauvaise fiche : réponse affirmée sur une fiche voisine du même objet, et non la fiche de la clé ; état non faux en soi ; fausse attribution (moitié « réserve ») |

Aucune autre erreur de justesse dans le bras memo. Manquements de périmètre du bras memo à corriger côté procédure (non côté mémo) : déclarations de racines `registres/` (Q057, Q058, Q059, Q065, Q067, Q073), dossier des demandes en entier (Q004, Q011, Q078, Q093, Q110), dossier du papier « dopamine » en entier (Q009) ; incident (ii), lot 3.
