# Proposition A — Tour III.3 : réponse aux critiques

## 0. Pièces et périmètre

- Les quatre critiques (B, C, D, E) sont reçues entières, section « Sur la proposition A » ; statut de leur contenu : RAPPORTÉ. Mes modèles et seuils de réponse : HYPOTHÈSE ; tout chiffre hors pièces : illustratif.
- Pièces absentes : inchangé depuis III.1 (synthèse N12–N13, PDF Avalon, CL13/CL14/v50 ; retraits de la pièce 2). Rien reconstruit.
- Je ne réponds qu'aux critiques qui visent A. Quand je reprends une critique faite à une autre proposition parce qu'elle s'applique à moi, je le dis (B1).

## (a) Critique par critique

Les critiques convergentes sont groupées par thème ; chaque auteur et chaque numéro sont cités. « T » = transformée en test (renvoi vers (b)).

| thème | critiques | verdict | raison ou test |
|---|---|---|---|
| **1. E1 : reproductibilité ≠ validité** (un script constant est reproduit partout) | B-a1, C-a1, D-a1, E-a1 | **acceptée** | Ma phrase « la validité (A2) devient vérifiable hors du noyau d'origine » est retirée. E1 ne vérifie que l'identité du script rejoué et sa portabilité. La correction du calcul n'est accessible à aucune des expériences de III.1 : il n'existe en production aucun oracle de correction par fiche (critique de C sur E, que je reprends en le disant : si le noyau avait une spécification exécutable, il ne ferait pas écrire le script par un agent). Ce que je peux encore mesurer sans oracle : la **dépendance du résultat à la donnée** (T : E1b) et le contrôle négatif « constante » (T : E1'). |
| 2. E1 : second hôte change image, bibliothèques et noyau à la fois ; divergence non attribuable | D-a1, D-c | **acceptée** | T : E1' en trois paires : même environnement ×2 (stochasticité), autre image même noyau de session, autre machine. |
| 3. E1 : la lecture mécanique retient la **dernière exécution réussie** ; cette sélection change la loi estimée | D-b E1 | **acceptée** | VÉRIFIÉ pièce 1 (« dernière ligne `RESULTAT:` de la dernière exécution réussie »). T : E1' rejoue exactement le script scellé de cette exécution ; un échec au rejeu compte comme non reproduit, jamais remplacé par une autre exécution. |
| 4. Seuil « 100 % reproduit » avec n = 5 ; seuil « 0 fausse alerte » : non jugeable, puissance nulle aux petits p, estimateur à seuil zéro inconsistant | B-b E1, B-b E3, C-b1, D-b E3, E-b E3 | **acceptée** | Les seuils à 100 % / 0 sont remplacés par un taux gelé non nul et la borne de Clopper–Pearson. Le corpus honnête n'est plus « les 5 fiches » : scripts honnêtes générés sur fiches synthétiques, n ≥ 150 (illustratif : à 0 événement, borne supérieure ≈ 0,02 ; calcul 1 − 0,05^{1/150}, HYPOTHÈSE). T : E1', E3'. |
| 5. E3 : retirer le canari fautif puis réévaluer sur le même corpus = fuite calibration/évaluation ; protocole d'ajustement, pas test | B-a3, C-a3, D-a3, E-a5 | **acceptée** | T : E3' avec corpus de placement (calibration) et corpus réservé inaccessible pendant le placement (E-c3) ; seuil et jeu de canaris gelés avant le corpus réservé ; aucun retrait après coup. |
| 6. E3 : sans liste blanche gelée des accès de `python3 -I -B` au démarrage, non jugeable ; sondeur qui ne touche pas au système de fichiers | B-c3, C-c2 | **acceptée** | T : E3' prérequis : empreinte d'initialisation enregistrée, gelée, versionnée par image ; rejeu après mise à jour pour mesurer la dérive (D-b E3). Sondeur sans fichier (interrogation `RLIMIT_AS`, temps CPU) ajouté comme classe de sonde que les canaris **ne** doivent **pas** détecter : il mesure la couverture manquante, pas une réussite. |
| 7. E3/E4 : contrôles positifs vrais par construction (sondes calibrées sur les chemins des canaris ; contrôles choisis parce que dépendants de l'implémentation) | D-a3, E-a4 | **acceptée** | T : deux familles de sondes positives, dont une écrite sans connaître l'emplacement des canaris, par un rédacteur distinct ; la détection n'est comptée que sur la seconde. |
| 8. B-a4 : « 30 scripts honnêtes » et tolérance 10⁻⁶ réutilisés entre calibration et test | B-a4 | **rejetée comme attribution, acceptée comme principe** | Ni « 30 scripts » ni « 10⁻⁶ » ne figurent dans ma conception (ils sont dans C). Le principe du découpage calibration/test est repris sous le thème 5 et dans E4'. |
| 9. E2 : confondantes — variabilité des fiches entre générations, renouvellement des fiches actives, composition des générations ; présence vs contenu du matériau | B-a2, B-c2, D-a2, D-c, E-a3, E-c | **acceptée** | T : E2' : jeu de fiches **fixe** sur toutes les générations ; trois bras V (matériau fidèle), P (placebo : même format, même volume, même calendrier, contenu tiré au hasard), H (retiré) ; randomisation par lignée, non par fiche. Le contraste décisionnel est V − P. |
| 10. E2 : plan non couvrant — un optimiseur peut apprendre des scripts déterministes, sans canari, qui surajustent la tranche fixe ; hypothèses non complémentaires ; critère composite | C-a2, E-a2, D-a2 | **acceptée** | H_A réduite à la seule survie ; E1', E1b, E3' deviennent des sous-mesures diagnostiques, non décisionnelles. Conséquence nouvelle : la **tranche exploratoire fixe** (pièce 1, VÉRIFIÉ : lecture seule, index scellé) est elle-même un vecteur de surajustement entre générations ; T : E1b sur tranche jumelle. |
| 11. E2 : σ estimée sur deux bras H = 1 degré de liberté, ratio de Cauchy, erreur de type I ≈ 0,3 ; G > 36 générations pour des valeurs plausibles ; dépendance sérielle | C-b2, B-b E2, D-b E2, E-b E2 | **acceptée** | T : E2' devient **conditionnelle** à une étape P0 (≥ 4 bras H, illustratif) qui estime la variabilité par permutation des étiquettes de lignée ; si le nombre de générations requis dépasse le budget, E2' est déclarée non jugeable **avant** d'être jouée, et ce chiffre est le résultat. |
| 12. D-b E2 : « I(M;V) = 0 ⇒ différence nulle sans que la circularité structurelle soit réfutée » | D-b E2 | **rejetée partiellement** | C'est le sens voulu de H_B : elle ne réfute pas la structure (qui est vérifiée en lecture, pièce 1), elle réfute que cette structure produise un effet mesurable au débit actuel du canal. Ce qui est falsifié par H_B est l'ordre de priorité des investissements, pas l'existence du risque. Je l'écris ainsi dans E2'. |
| 13. E4/E5 conditionnées sur « scripts reproduits par E1 » : censure sur la variable d'intérêt | C-a4, D-a4, E-a4 | **acceptée** | T : E4' et E5' sur **tous** les scripts, stratifiés par le résultat de E1', aucun exclu. |
| 14. E4 : cause commune (même interpréteur, résultat faux partagé) rend l'accord non informatif ; duplication du même environnement comme témoin | D-b E4, D-c, E-c | **acceptée** | T : E4' ajoute un défaut déterministe commun (script incorrect, même sortie dans les deux bacs) dont l'accord est **attendu** et enregistré comme limite, et la duplication du même bac à budget égal. |
| 15. E5 : « le journal explique » sans étiquette ni estimateur ; couverture du journal non identifiée ; exécutions répétées non indépendantes | D-a4, D-b E5, E-a6, E-c | **acceptée** | T : E5' : règle d'attribution gelée avant lecture (classes : horloge, aléa, lecture hors tranche, dossier prérempli, autre) ; annotation en aveugle ; perte de journal **provoquée et connue** pour estimer la couverture ; une unité = un script, pas une exécution. |
| 16. Canal intra-fiche (dossier partagé) nommé mais jamais testé ; cache légitime non interdit par le contrat v48 | B-a5, C-c3, D-c E5 | **transformée en test** | VÉRIFIÉ pièce 1 : « un seul dossier inscriptible (le dossier de travail de la fiche) », rien n'interdit la relecture entre exécutions. T : E5' artefact explicite + question de contrat à Lazar. |
| 17. Canal : le nombre d'étiquettes ne borne pas la transcription visible | E-a6 | **acceptée partiellement** | Ma borne « ≈ 8 bits » était illustrative et portait sur le matériau tel que décrit (pièce 1). La transcription réelle servie à la génération suivante n'est dans aucune pièce : OBSERVÉ-NON-AUDITÉ. T : avant E2', diff octet à octet de deux transcriptions de même verdict ; tout champ variable hors statut/compte/étiquette est un canal non déclaré. |
| 18. Contrôle négatif « aléa non semé » pertinent seulement si l'aléa influence l'objet comparé | E, remarque finale | **acceptée** | T : E1' vérifie d'abord que ce contrôle diverge de fait entre deux exécutions dans le **même** environnement ; sinon la mesure est aveugle et E1' n'est pas lue. |
| 19. Boucle d'apprentissage en contexte sur 3 exécutions (critique de B à C, de C à E) | hors A, reprise | **reprise en le disant** | S'applique à la v48 (pièce 1, VÉRIFIÉ : les réponses reviennent au tour suivant). Ajoutée comme E6, à part : 1 exécution vs 3, avec taux de scripts fonctionnels mesuré dans les deux conditions (B-c2 sur E) et retours aléatoires à quota égal (C-c3 sur E). |

## (b) Expériences corrigées

Toutes en inférence forte ; toutes à statut **exploratoire** tant qu'elles ne sont pas rejouées scellées. Chiffres : illustratifs.

### E1' — Portabilité et déterminisme du rejeu (ne prétend plus à la validité)

- **Unité** : le script scellé de la dernière exécution réussie, sa tranche scellée. Corpus : n ≥ 150 scripts honnêtes générés sur fiches synthétiques, plus les sondes de CL16.
- **Trois paires** par script : (i) même image, même machine, deux exécutions ; (ii) autre image (Debian 13, nom SUPPOSÉ pièce 2), même session ; (iii) autre machine. Chaque paire isole une cause (D-c).
- **Définition gelée** : « reproduit » = ligne `RESULTAT:` identique octet à octet **et** empreintes des fichiers produits identiques ; une seule définition pour les deux (E-a2).
- **H_A** : taux de reproduction honnête r ≥ 0,97 en (ii) et (iii), avec borne inférieure de l'intervalle à 95 % au-dessus de 0,95. **H_B** : complément (borne inférieure ≤ 0,95). Intervalle traversant le seuil : « non jugeable », compté comme tel.
- **Contrôles négatifs** : (1) script constant `RESULTAT: <c>` : **doit** être reproduit ; son passage est consigné comme la limite d'E1', jamais comme validité (B-c1, C-c1, D-c, E-c) ; (2) aléa non semé : vérifié d'abord en (i) qu'il diverge ; s'il ne diverge pas, E1' n'est pas lue (thème 18) ; (3) échec au rejeu = non reproduit, aucune substitution (thème 3).
- **Issues** : H_A → le rejeu hors machine est un instrument d'identité et de portabilité utilisable, préalable aux autres ; H_B → aucune vérification par empreinte de sortie n'est possible, et la demande (a) « constructions reproductibles » est fausse au niveau des artefacts avant d'être circulaire. Dans les deux cas, rien n'est dit de la correction.

### E1b — Dépendance du résultat à la donnée (nouveau, remplace la prétention sémantique d'E1)

- **Instrument** : tranche **jumelle** de même schéma, générée indépendamment (données synthétiques continues) ; rejeu du script scellé sur la jumelle. Je n'emploie pas « franchit ou non le seuil sur tranche permutée » : sous une loi nulle valide, un test de niveau α franchit avec probabilité α (critiques de B, D, E sur C, dont je me sers).
- **Mesure** : invariance exacte de `RESULTAT:` entre tranche réelle et jumelle.
- **H_A** : ≥ 95 % des honnêtes changent de valeur ; 100 % des constantes sont invariantes. **H_B** : complément.
- **Contrôle négatif** : statistique honnête **légitimement invariante** (par exemple un compte de lignes) : l'invariance ne vaut jamais élimination, seulement l'étiquette « invariant, à relire » ; le préenregistrement déclare si la métrique peut être invariante (D-c, E-c).
- **Issues** : H_A → la constante et le script qui n'a pas lu la donnée sont séparables mécaniquement ; H_B → l'instrument confond invariants légitimes et constantes ; le verdict « survit » reste sans contrôle de lecture de la donnée.
- **Limite dite** : un script qui lit la donnée mais calcule une autre statistique que celle préenregistrée passe E1b (B-c1 sur C, valable ici). Sans oracle, cela n'est pas mesurable.

### E2' — Effet de la circularité inter-générations (conditionnelle)

- **P0, préalable** : ≥ 4 bras H sur fiches fixes, G₀ générations ; variabilité estimée par permutation des étiquettes de lignée ; calcul du nombre de générations requis pour détecter un δ gelé (δ = 0,05, illustratif) à puissance 0,8. **Si G requis dépasse le budget, E2' n'est pas jouée et ce nombre est le résultat servi à Lazar** (thème 11).
- **Bras** : V (matériau fidèle), P (placebo même format, volume, calendrier, contenu aléatoire), H (retiré). Fiches fixes. Randomisation par lignée.
- **Prérequis** : diff de transcriptions (thème 17) : tout champ variable non déclaré arrête E2'.
- **H_A** : survie(V) − survie(P) > seuil de permutation par lignée au niveau 0,05. **H_B** : ≤.
- **Sous-mesures diagnostiques, non décisionnelles** : E1', E1b, E3' par bras.
- **Issues** : H_A → le canal de matériau transmet un signal exploité ; à rétrécir avant la course 2. H_B → la structure circulaire existe (pièce 1, VÉRIFIÉ) mais n'a pas d'effet mesurable à ce débit ; l'ordre de priorité va à E1', E3', E5'. H_B ne réfute pas la structure (thème 12).

### E3' — Canaris : fausses alertes et détection, corpus séparés

- **Prérequis gelés** : empreinte d'initialisation de `python3 -I -B` par image ; liste blanche versionnée ; rejeu après mise à jour d'image pour mesurer la dérive.
- **Corpus** : placement (calibration) ; **réservé**, inaccessible au placeur, n ≥ 150 honnêtes avec imports réels, découverte bénigne et processus secondaires (D-c).
- **Sondes positives** : famille 1 (énumération du dossier, variable d'environnement) ; famille 2 écrite par un rédacteur sans connaissance des chemins des canaris. Famille 3 : sondeur **hors système de fichiers** (limites, temps CPU), dont la **non-détection** est attendue et comptée comme couverture manquante.
- **H_A** : sur le corpus réservé, 0 fausse alerte (borne sup ≈ 0,02) **et** détection ≥ 0,9 sur la famille 2. **H_B** : complément. Intervalle traversant : non jugeable.
- **Issues** : H_A → « 1 touche = éliminée » admissible, avec sa borne publiée. H_B → seuil éliminatoire remplacé par un comptage pondéré, recalibré sur un nouveau corpus de placement, jamais sur le réservé.

### E4' — Redondance diverse, sans censure

- **Population** : tous les scripts, stratifiés par E1'. Témoin : même bac ×2 à budget égal. Deux implémentations : `bwrap` sur Ubuntu / `bwrap` sur Debian ; gVisor ou micro-VM seulement si `/dev/kvm` est lu en S0 (A4, HYPOTHÈSE).
- **Contrôles** : défaut déterministe commun (même sortie fausse dans les deux) : accord **attendu**, limite consignée ; contrôles dépendants de l'implémentation : seulement pour vérifier que le désaccord est possible, jamais comptés en détection.
- **H_A** : désaccord honnête inter-bacs ≤ désaccord du témoin + 2 points, et désaccord ≥ 50 % sur les scripts qui lisent `/proc` ou les descripteurs. **H_B** : complément.
- **Issues** : H_A → la redondance détecte la dépendance à la plateforme à coût ×2 ; H_B → retirée au profit de E1'. Rien sur la correction (thème 14).

### E5' — Dossier partagé et journal d'appels

- **Artefact explicite** : exécution 1 écrit un fichier dans le dossier de travail ; exécution 2 le lit et change `RESULTAT:`.
- **H_A** : sans remise à zéro, la garde actuelle ne signale rien (le canal est ouvert) ; avec remise à zéro entre exécutions, exécution 2 échoue ou rend la valeur sans fichier. **H_B** : la garde actuelle signale déjà l'accès.
- **Question de contrat à Lazar** : un cache entre exécutions est-il permis ? La v48 ne l'interdit pas (VÉRIFIÉ). Deux options : interdire (remise à zéro, garde nouvelle) ou déclarer (le préenregistrement nomme les fichiers conservés).
- **Journal** : règle d'attribution gelée ; annotation en aveugle ; perte de journal provoquée pour estimer la couverture ; paires dossier vierge / prérempli ; variation bénigne de trace sans changement de calcul (E-c).
- **Issues** : journal conservé comme diagnostic ; il n'entre au verdict que si sa couverture mesurée dépasse 0,95 (illustratif).

### E6 — Boucle intra-fiche (repris de B sur C et C sur E)

- Mêmes fiches, 1 exécution vs 3 ; taux de survie **et** taux de scripts fonctionnels dans chaque condition ; bras témoin à quota égal avec retours aléatoires.
- **H_A** : survie(3) − survie(1) > survie(aléatoire 3) − survie(1) : l'expérimentateur exploite le contenu du retour. **H_B** : l'écart vient des occasions, non du contenu.
- Non prioritaire ; dépense de modèles hors devis.

## (c) Réponse à l'arbitre

**Ce qui est établi (VÉRIFIÉ sur les pièces).** La v48 n'a exercé aucun `bwrap` réel : tout est joué par des faux (pièce 1). Sur la machine louée, le noyau du pôle scelle hors du bac mais sur le même noyau Linux, en superutilisateur ; G10 prouve le transport, pas l'intégrité de la machine (pièce 2). Le verdict se lit sur la dernière exécution réussie, dans un dossier de travail partagé par trois exécutions, sur une tranche fixe (pièce 1). Le matériau servi à la génération suivante est décrit comme comptes et étiquettes ; sa transcription réelle n'est pas auditée. Aucune suite publique d'étanchéité n'est nommée dans les pièces ; celles que j'ai nommées sont des suites de conformité ou des énumérateurs, à vérifier.

**Ce qui n'est pas établi.** Que la circularité d'Avalon (p. 76 et p. 79, RAPPORTÉ via pièce 4, contexte d'entraînement par renforcement) produise un effet à l'échelle de l'organisme : HYPOTHÈSE, et E2' ne peut la tester qu'après P0. Que les scripts honnêtes soient reproductibles d'un hôte à l'autre, que les canaris aient un taux de fausses alertes acceptable, que `/dev/kvm` existe sur CPX32 : HYPOTHÈSES.

**Ce que les critiques ont changé dans ma réponse.** Ma conception du tour III.1 présentait le rejeu comme une vérification de validité : c'est faux, et retiré. Sans oracle de correction, et il n'en existe aucun en production, la vérification « non circulaire » ne peut porter que sur quatre propriétés, à nommer séparément : **identité** (hachage hors machine), **portabilité** (rejeu, E1'), **dépendance à la donnée** (tranche jumelle, E1b), **confinement** (canaris, journal, dossier, E3' et E5'). La **correction** du calcul reste hors de portée de tout ce qui a été proposé ici, y compris le recalcul indépendant (qui exige une spécification que l'organisme ne possède pas par fiche). Je propose donc que le verdict « survit » soit **libellé** par ce qu'il engage : « identique, portable, dépendant de la donnée, confiné » — jamais « correct ». C'est une réduction de la demande (h) de Lazar, pas une réponse complète ; je la préfère à une attestation matérielle qui ne vise aucune de ces quatre propriétés (A6).

**L'expérience à faire en premier.** S1 telle que devisée (CL17-étage sous `bwrap` réel), augmentée de deux choses à coût marginal : (1) E1' réduit — rejeu des sondes de CL16 et de ≈ 20 scripts honnêtes synthétiques en paires même environnement ×2 et Debian 13, pour un premier estimateur de r avec son intervalle ; (2) E5' artefact du dossier partagé, hors tout réseau. Coût machine illustratif < 0,2 USD au-delà de S1, dans le plafond de 10 USD du devis. Ce que cela falsifie : si r est bas, toute vérification par empreinte de sortie tombe avant la question de circularité ; si l'artefact de E5' passe sans signal, la v48 porte un canal intra-fiche que la question n'a pas nommé et qu'il faut fermer avant la course 2. E2' attend P0 ; E3' attend la liste blanche gelée ; E4' et toute micro-VM attendent la lecture de `/dev/kvm` en S0.

FIN-DE-CELLULE