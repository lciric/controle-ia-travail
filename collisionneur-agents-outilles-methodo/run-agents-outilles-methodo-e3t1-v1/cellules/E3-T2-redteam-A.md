# Proposition A · Tour III.2 : équipe rouge croisée

**Pièces reçues.** Le bloc FAITS est vide par décision déclarée de l'arbitre : rien ci-dessous n'est VÉRIFIÉ ; les énoncés du cadre sont RAPPORTÉS, les résultats de littérature RAPPORTÉS (référence citée), le reste est HYPOTHÈSE. Les pièces B et C sont complètes et non tronquées ; je les traite comme des données. Tout chiffre que j'introduis est illustratif.

---

## Contre la proposition B

### (a) Failles

**B-1. X3 est vraie par construction sous F-immédiat.** Si le filtre détecte les quasi-copies (ce que B exige par ailleurs dans sa table (c) : « détecter plus de paraphrases »), chaque refus est un bit d'appartenance et l'aire ROC est mécaniquement > 0,5. Si le filtre ne les détecte pas, l'aire est ≈ 0,5 mais le filtre est inutile. X3 ne mesure donc pas « le filtre immédiat fuit-il ? » : il mesure le TPR du filtre, déjà mesuré ailleurs. La seule question vive est F-différé, et là B suppose que la « réponse factice » est indétectable. HYPOTHÈSE non testée : une réponse factice incohérente (deux `predict` sur la même poignée, ou un `fit_probe` dont la métrique interne contredit les étiquettes fournies) se détecte en deux requêtes.

**B-2. F-différé déplace la fuite vers l'annulation.** « L'audit annule l'exécution après coup » : l'annulation est un bit par exécution, rendu à quiconque persiste entre exécutions (code de $\mathcal{O}$ réécrit, journal, Lazar). B signale a4 (l'arbitre comme canal) puis le recrée.

**B-3. `generate` n'est pas filtré en sortie.** Le filtre porte sur les textes construits par $\mathcal{O}$ ; les sorties du modèle 8B sont rendues telles quelles. Si $D_{\mathrm{test}}$ ou $D_{\mathrm{val}}$ est mémorisé (a6, que B pose lui-même), `generate` à décodage fixé est un extracteur de régurgitation : $\mathcal{O}$ amorce avec un préfixe plausible, reçoit la suite, et n'a jamais « construit » l'item. Les deux filtres de B ont un trou en amont.

**B-4. Le budget de bits est incohérent avec `generate`.** B fait de $\sum b_i$ la quantité qui alimente la borne §1.2. Un appel `generate` rend des milliers de bits. Soit on les compte et le budget est épuisé à la première itération, soit on ne les compte pas et la borne ne couvre plus la transcription. B ne dit pas lequel. (La borne reste valable si l'on montre que les sorties de `generate` sont indépendantes de $D_{\mathrm{val}}$ — ce qui est exactement a6, non établi.)

**B-5. X1 : mesurer une pente en $\log k$ avec une seule interrogation de $D_{\mathrm{frais}}$ par exécution.** Une seule interrogation par exécution donne un point par exécution ; cinq exécutions donnent cinq points à $k$ différents, confondus avec la variance entre exécutions (graines, trajectoires de $\mathcal{O}$). Si l'on interroge $D_{\mathrm{frais}}$ à plusieurs $k$ dans une même exécution, c'est l'expérimentateur qui devient analyste adaptatif de $D_{\mathrm{frais}}$. De plus $\Delta = S_{\mathrm{val}} - S_{\mathrm{frais}}$ mêle surapprentissage et décalage de distribution (a2) ; le contrôle non adaptatif absorbe le décalage seulement si $D_{\mathrm{frais}}$ est tiré de la même distribution, ce que personne ne certifie.

**B-6. X2 : le placebo par permutation est détectable.** Un $\mathcal{O}$ qui vérifie la cohérence de ses réponses (un contrôle que B lui-même recommande en X4) reconnaît les résultats permutés et cesse d'utiliser E2. Le bras placebo devient « sans E2 » à budget consommé différemment ; la différence réel–placebo mesure alors « $\mathcal{O}$ a abandonné E2 », pas « le contenu informe ». Les délais sont identiques, pas l'usage du budget.

**B-7. Fuite construction/évaluation dans X4 et dans le préenregistrement.** Dans X4, $\mathcal{O}$ construit les paires minimales *et* la sonde ; il peut sélectionner des paires où la sonde « sac de mots » échoue par construction. Dans §2.4, le réservoir B est « généré par un processus séparé » — mais généré *comment* ? Si le gabarit de stimuli vient de la phase d'exploration, $\mathcal{O}$ choisit la distribution de confirmation ; la confirmation prouve la cohérence sonde–gabarit, pas le concept. La graine scellée ne protège que contre le choix des tirages, pas contre le choix du générateur.

**B-8. X5 confond deux facteurs.** Le bras « critère interne » diffère du bras « critère externe » par deux choses : le critère et le réservoir scellé. Avec des nulles à étiquettes aléatoires et un réservoir B frais, le taux de fausses confirmations est ≤ α *quel que soit* le critère, sauf critère dégénéré. X5 falsifiera presque sûrement H_A, et B conclura « préenregistrement sans bénéfice », alors que c'est le réservoir scellé qui a tout fait. Il manque le plan factoriel critère {interne, externe} × réservoir {scellé, non scellé}. Par ailleurs les nulles « étiquettes indépendantes du texte » sont les nulles faciles ; les nulles dangereuses sont celles corrélées à un trait de surface sans lien avec le concept — absentes.

**B-9. X6 : métrique goodhartable et contrôle vide.** « Hypothèses confirmées sur réservoir scellé par unité de coût » : $\mathcal{O}$ maximise en soumettant des hypothèses triviales (effet sûr, faible). Rien ne pèse la difficulté. Le contrôle « (E1) sans substitut → zéro confirmation sur le modèle 8B » est vrai par construction (aucun accès) et n'informe pas.

**B-10. Tâche de contrôle à la Hewitt & Liang non définie au niveau phrase.** La construction originale (RAPPORTÉ : Hewitt & Liang 2019) assigne des étiquettes aléatoires par type lexical ; pour une sonde au niveau texte avec mise en commun, B ne dit pas comment on la construit. « Sélectivité > 0,10 » n'a pas d'objet.

**B-11. La file synchrone fuit par l'attente.** Le temps d'attente imputé au budget dépend de la charge de l'hôte, laquelle dépend des calculs sur $D_{\mathrm{test}}$ d'autres exécutions si l'hôte les sert en parallèle. B ne dit pas si $D_{\mathrm{test}}$ est évalué sur le même hôte.

### (b) Scénarios d'évasion

| Instrument de B | Évasion | Coût pour l'adversaire (illustratif) |
|---|---|---|
| Budget de bits + arrondi | Ne rien attaquer par les bits : extraire $D_{\mathrm{val}}$/$D_{\mathrm{test}}$ par `generate` (régurgitation, B-3), puis travailler localement sous E1 | Un appel `generate` par item amorcé ; aucun bit « comptable » consommé sur $D_{\mathrm{val}}$ |
| F-immédiat | Soumettre des candidats issus de connaissances préalables ou de `generate` ; lire refus/acceptation | 1 requête par candidat (ou par lot si le code d'erreur est par lot : alors 1 bit par lot, mais on isole par dichotomie en $\log_2 256 \approx 8$ requêtes par item) |
| F-différé | Tester la cohérence : même poignée, deux `predict` ; ou `fit_probe` sur des étiquettes connues et comparer la métrique interne au résultat attendu | +2 requêtes par lot suspect |
| Palier de durée | Inopérant si le calcul est indépendant des données ; sinon, choisir des requêtes dont le coût est près d'une frontière de palier et lire le palier franchi | Requêtes calibrées, ~1 bit par requête-frontière |
| Préenregistrement (engagement/révélation) | Engager beaucoup d'hypothèses, rapporter les confirmées (B ne plafonne pas les engagements ni ne corrige) ; imposer le gabarit de génération du réservoir B pendant l'exploration (B-7) | Un `commit` par hypothèse |
| X2 placebo | Détecter la permutation (B-6) et basculer en mode « sans E2 » | 2 requêtes |
| Ladder (`score_val`) | Attaque classique : soumissions aléatoires, chaque « sous le seuil » est un bit ; mais la garantie Ladder (RAPPORTÉ : Blum & Hardt 2015) borne cela | Élevé : c'est l'instrument qui tient |

**Tous à la fois.** L'adversaire combine B-3 (extraction par `generate`) et a3 (si $D_{\mathrm{val}}$ est local, E1 permet l'adaptativité illimitée) : il ne touche jamais `score_val` plus que le Ladder ne l'autorise et contourne pourtant toute la §1.2. Coût : dominé par les appels `generate`, soit de l'ordre de $|D_{\mathrm{val}}|$ appels — comparable à une seule exécution normale. Le dessin de B tient **si et seulement si** a6 est fausse (pas de mémorisation) et $D_{\mathrm{val}}$ est chez l'hôte. B ne teste ni l'une ni l'autre avant X6.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Test d'extraction par mémorisation** sur le modèle 8B, hors boucle et par Lazar : amorcer avec les premiers jetons d'items de $D_{\mathrm{val}}$ et $D_{\mathrm{test}}$, mesurer le taux de complétion exacte, comparé à des items leurres de même source. Sans cela, B-3 et a6 restent ouverts et X3 ne couvre pas la surface d'attaque principale.
2. **Localisation de $D_{\mathrm{val}}$** (a3) consignée comme fait avant X1 : sans elle, la borne §1.2 n'a pas de domaine de validité.
3. **Test de détectabilité du placebo** : un modèle de langue reçoit des transcriptions réelles et permutées, doit les distinguer ; si l'aire ROC > 0,5, X2 est caduque.
4. **Plan factoriel pour X5** (B-8) et nulles corrélées à un trait de surface.
5. **Pour F-différé** : adversaire muni des sondes de cohérence de B-1 ; sinon « F-différé ne fuit pas » est vrai parce que personne n'a cherché.
6. **Audit que le même hôte ne sert pas $D_{\mathrm{test}}$ pendant une exécution** (B-11).
7. **Comptage explicite des bits de `generate`** et borne séparée (B-4).

---

## Contre la proposition C

### (a) Failles

**C-1. C évite l'oracle sur $D_{\mathrm{test}}$ et l'installe sur $D_{\mathrm{val}}$ — y compris sur $D_{\mathrm{conf}}$.** §2.3 : le filtre « bloque les quasi-copies de $D_{\mathrm{tr}}$ et $D_{\mathrm{val}}$ » et rend `ERR_FILTER`. C'est exactement l'oracle d'appartenance que C dénonce pour $D_{\mathrm{test}}$. Comme $D_{\mathrm{conf}} = D_{\mathrm{val}} \setminus D_{\mathrm{dev}}$, l'oracle couvre le jeu de confirmation. Son propre argument « $I(\mathcal{O}_k; D_{\mathrm{test}} \mid \mathcal{D}) = 0$ » exige des filtres indépendants de $D_{\mathrm{test}}$ ; l'argument symétrique pour $D_{\mathrm{conf}}$ est violé par construction. Je me sers ici de a7 de B, en le disant.

**C-2. Fuite construction/évaluation par le Ladder.** §2.3 primitive 4 : `submit_to_ladder` évalue sur $D_{\mathrm{val}}$ entier. §2.3 préenregistrement : l'exploration se limite à $D_{\mathrm{dev}} \subset D_{\mathrm{val}}$ et la confirmation se fait sur $D_{\mathrm{val}} \setminus D_{\mathrm{dev}}$. Les deux énoncés sont incompatibles : si le Ladder a vu tout $D_{\mathrm{val}}$, $D_{\mathrm{conf}}$ n'est pas frais. La « phase verrouillée » confirme sur des données déjà interrogées.

**C-3. Les probabilités par item réapparaissent sur les paraphrases.** `eval_probe_on_handle` rend des agrégats « jamais les probabilités individuelles *si le jeu contient des données de l'hôte* ». Sur des textes de $\mathcal{O}$, elles sont donc rendues. Une paraphrase d'un item de $D_{\mathrm{conf}}$ qui passe le filtre (Jaccard sur 5-grammes de caractères < 0,3 : accessible par traduction aller-retour) est un texte de $\mathcal{O}$. Les probabilités par item sur $D_{\mathrm{val}}$, que C a supprimées du canal principal, reviennent par E2 avec un bruit de paraphrase. Combiné à C-1, l'adversaire sait *quels* items paraphraser.

**C-4. Expérience 1 confond E2 et adaptativité.** Le Bras 0 émet 10 hypothèses en une fois ; les Bras 1 et 2 itèrent 50 fois. Bras 2 vs Bras 0 mesure « itérer vs ne pas itérer », pas E2. Seul Bras 2 vs Bras 1 isole E2. Le seuil « +2,0 points d'AUC sinon H_A falsifiée » fait dépendre l'issue d'un chiffre illustratif : un gain de +1,5 point significatif « falsifierait » H_A. B4 demande que chaque issue falsifie quelque chose, pas qu'un seuil arbitraire décide.

**C-5. Le Bras 2-Brouillé est un Bras 1 déguisé.** Des activations permutées entre textes donnent des sondes au hasard ; $\mathcal{O}$ le constate à la première `fit_linear_probe` et cesse d'utiliser E2. « Bras 2 bat Bras 2-Brouillé » est donc équivalent à « Bras 2 bat Bras 1 » et n'ajoute rien. Le contrôle intéressant serait un placebo *plausible* (activations d'un modèle sans rapport, ou d'une autre couche), qui n'est pas proposé.

**C-6. $D_{\mathrm{test}}$ est consommé par l'étude de conception.** Les trois expériences mesurent $\Delta S_{\mathrm{test}}$ et $\Gamma_{\mathrm{gen}}$ par exécution : 80 + 80 exécutions lisent $D_{\mathrm{test}}$. L'expérimentateur sélectionne ensuite une architecture d'interface sur la base de ces lectures. C'est a4 de B à l'échelle du protocole : P1 est contournée par l'audit lui-même. C n'a pas de $D_{\mathrm{frais}}$.

**C-7. Expérience 3 attaque un canal que C a déjà fermé par ailleurs.** Le canal temporel décrit (durée de convergence de L-BFGS dépendant du conditionnement) est éliminé par la primitive 2 (« convergence fixe pour éliminer le pas ») ; l'oracle NaN par pas critique est éliminé de même. L'issue probable (H_A falsifiée) sera attribuée au « bruit système » alors qu'elle vient du solveur à itérations fixes. Deux interventions (solveur fixe, rembourrage) pour une seule expérience : non séparables. Au passage, « éliminer le pas » contredit le cadre (RAPPORTÉ : « $\mathcal{O}$ fournit … et pas »).

**C-8. Le rembourrage « mise en échec si dépasse Δt » est un canal.** Un échec pour dépassement est observable. Il reste des dépendances aux données si un calcul quelconque de l'hôte dépend de $D_{\mathrm{val}}$ (par exemple le filtre lui-même, dont le coût dépend de la taille de l'index de $n$-grammes et des collisions).

**C-9. Chiffrage interne incohérent (illustratif, mais contradictoire).** C donne $8\times10^{12}$ FLOP par texte de 512 jetons (cohérent avec $2N$ par jeton), puis « 10 à 50 ms par lot de 32 » soit $2{,}6\times10^{14}$ FLOP en 10–50 ms, c'est-à-dire $5$ à $26\times10^{15}$ FLOP/s. Le pic bf16 dense d'une A100 est de l'ordre de $3\times10^{14}$ FLOP/s (ordre de grandeur, à vérifier). L'écart est d'un facteur 20 à 100. De même « 3,6 millions de jetons en 2 minutes » implique $\approx 5\times10^{14}$ FLOP/s soutenus, au-dessus du pic. Les 100 heures-GPU totales sont donc sous-estimées d'un facteur que je ne peux pas chiffrer sans fait.

**C-10. Bornes de la littérature déformées.** « Ladder : $\mathcal{O}(\sqrt[3]{k/n})$ » : la garantie rapportée par B (et telle que je la connais, à vérifier dans Blum & Hardt 2015) a une dépendance *logarithmique* en $k$ ; une dépendance polynomiale en $k$ ôterait tout l'intérêt du mécanisme. « Thresholdout : $\mathcal{O}(\sqrt{k_{\mathrm{pass}}}/n)$ » : forme non reconnaissable, à vérifier. Statut : RAPPORTÉ par C, contesté.

**C-11. Hypothèse 6 (auto-validation complaisante) posée, jamais testée.** C la liste en §1 et n'y revient dans aucune expérience ; or les cas positifs/négatifs de sa table (c), ligne 1, sont « 500 textes porteurs du concept » — construits par qui ? Si par $\mathcal{O}$, c'est la fuite de B-7.

**C-12. $D_{\mathrm{tr}}$ apparaît sans statut.** Le cadre ne mentionne pas de $D_{\mathrm{tr}}$ détenu par l'hôte ; si $D_{\mathrm{tr}}$ est fourni par $\mathcal{O}$ (« $\mathcal{O}$ fournit données »), bloquer ses copies est absurde ; s'il est à l'hôte, il manque au cadre.

### (b) Scénarios d'évasion

| Instrument de C | Évasion | Coût (illustratif) |
|---|---|---|
| Filtre anti-copie sur $D_{\mathrm{val}}$ | L'utiliser comme oracle : soumettre des candidats (connaissances préalables, régurgitation par `generate_open_model` en glouton), lire `ERR_FILTER` | Si le code est par appel : dichotomie, ~8 appels par item isolé ; si par texte : 256 bits par appel |
| Agrégats seuls sur $D_{\mathrm{val}}$ | Paraphraser les items identifiés sous le seuil de Jaccard, puis `eval_probe_on_handle` rend les probabilités par item (C-3) | Une génération de paraphrase par item + 1 appel par 256 items |
| Ladder η = 0,005 | Inutile de l'attaquer : les probabilités par item sur paraphrases permettent la sélection adaptative hors Ladder | Nul |
| Rembourrage 5 s | Viser la frontière : requêtes de taille maximale dont le coût hôte frôle Δt ; lire l'échec | Faible, mais rendement faible aussi (peu de dépendance aux données restante) |
| Préenregistrement verrouillé | $D_{\mathrm{conf}}$ déjà vu par le Ladder (C-2) : choisir `probe_id_final` parmi ceux qui ont marqué sur $D_{\mathrm{val}}$ entier | Nul : c'est le comportement normal de $\mathcal{O}$ |
| Bras 2-Brouillé | Détecter le brouillage et se replier (C-5) | 1 appel |
| Moniteur de budget | Non attaqué ici : c'est l'instrument qui tient |

**Tous à la fois.** Oracle du filtre (C-1) → liste de $D_{\mathrm{conf}}$ → paraphrases → probabilités par item (C-3) → sélection adaptative sur $D_{\mathrm{conf}}$ sans toucher le Ladder → confirmation « verrouillée » sur des données surapprises (C-2). Coût : de l'ordre de $|D_{\mathrm{val}}|$ paraphrases (appels de modèle de langue, hors budget E2) et $|D_{\mathrm{val}}|/256$ appels E2, soit, avec $n = 2000$, une dizaine d'appels sur les 500 autorisés par exécution. Le dessin de C est contourné à moins de 5 % de son budget E2. Aucune des trois expériences de C ne détecterait ce scénario : Expérience 2 n'active pas E2, Expérience 3 n'attaque que le temps, Expérience 1 mesure un gain, pas une fuite.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Hôte leurre pour le filtre** : taux de `ERR_FILTER` sur des items de $D_{\mathrm{val}}$ paraphrasés contre le même protocole sur un hôte où $D_{\mathrm{val}}$ est remplacé par un leurre inconnu. Si les taux diffèrent, le filtre est un oracle (C-1). C'est le contrôle de X3 de B, que je reprends en le disant.
2. **Audit du journal** : aucun appel `submit_to_ladder` n'a lu un item de $D_{\mathrm{conf}}$ avant la phase verrouillée (C-2). Sans ce contrôle, la confirmation est sans valeur.
3. **$D_{\mathrm{frais}}$ détenu hors hôte**, interrogé une fois par bras et jamais pour sélectionner l'interface (C-6) ; sinon la mesure finale est contaminée par l'étude elle-même.
4. **Équivalence Bras 1 ≈ Bras 2-Brouillé** : si elle tient, le contrôle est vide (C-5) et doit être remplacé par un placebo plausible.
5. **Ablation pour Expérience 3** : solveur à itérations variables sans rembourrage, pour attribuer la fermeture du canal au bon dispositif (C-7).
6. **Test d'extraction par mémorisation** sur le modèle 8B (même contrôle que pour B) : sans lui, `generate_open_model` en décodage glouton est un extracteur non audité.
7. **Reprise du chiffrage** avec un débit soutenu mesuré sur le matériel réel (C-9) : sans cela, les 100 heures-GPU ne permettent pas de décider si les expériences sont finançables.

---

## Note de méthode

Ce que je réutilise et le dis : a4, a6, a7 de B contre C ; la structure « hôte leurre » de X3 (B) comme contrôle pour le filtre de C. Ce qui réfuterait mes attaques principales : (i) un test d'extraction par mémorisation négatif sur le modèle 8B pour $D_{\mathrm{val}}$ et $D_{\mathrm{test}}$ (B-3, évasion de C) ; (ii) la preuve, par le journal, que le Ladder de C n'a jamais lu $D_{\mathrm{conf}}$ (C-2) ; (iii) un filtre dont le taux de refus ne diffère pas entre hôte réel et hôte leurre (C-1). Aucun de ces trois faits n'est fourni ; tous sont mesurables avant la moindre expérience de B ou de C.

FIN-DE-CELLULE