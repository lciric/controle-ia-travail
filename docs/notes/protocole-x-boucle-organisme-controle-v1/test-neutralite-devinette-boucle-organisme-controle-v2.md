# Test de neutralité et test de devinette à l'aveugle sur les textes destinés au collisionneur (version 2)

## 1. Cadre d'intervention et attestation d'étanchéité préalable

Le présent examen est réalisé par un lecteur neuf intervenant totalement à l'aveugle (dans le cadre des accords d'exécution numérotés `GO-2026-11-23-33` et `GO-2026-11-23-34`, où le préfixe `GO` désigne un feu vert d'exécution). Au moment de rédiger et d'enregistrer ce rapport, **aucun autre fichier de travail** n'a été ouvert ni consulté en dehors des cinq pièces strictement autorisées :

1. `faits-neutres-boucle-organisme-controle-v2.md` (dossier `scratch/protocole-x-boucle-organisme-controle/`) ;
2. `question-neutre-collisionneur-boucle-organisme-controle-v2.md` (même dossier) ;
3. `question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md` (même dossier) ;
4. `sous-question-organisme-boucle-controle-v2.md` (même dossier) ;
5. `docs/notes/collisionneur-v9/collisionneur_v9_v8d.py` (dépôt `controle-ia-travail`, exécuté en lecture seule avec la variable d'environnement `PYTHONDONTWRITEBYTECODE=1` interdisant l'écriture de fichiers compilés intermédiaires).

En particulier, ni les versions initiales des faits ou questions, ni les demandes reformulées, ni les réponses approfondies, ni le premier rapport de neutralité, ni les devis n'ont été lus avant l'achèvement complet du présent rapport.

### Échelle de notation employée

Chaque texte reçoit un score d'orientation compris entre `0,00` et `1,00`, avec un seuil d'admission strict fixé à `< 0,50` :

- **`0,00` à `0,15` (neutralité très élevée)** : seuls transparaissent le périmètre factuel du problème, les contraintes matérielles ou les règles générales d'intégrité scientifique ; aucune piste algorithmique, formelle ou architecturale n'est suggérée.
- **`0,16` à `0,30` (neutralité solide, cadrage méthodologique visible)** : le texte désigne explicitement certaines classes de risques ou d'exigences de validité que toute solution devra satisfaire, ce qui laisse deviner les angles morts redoutés par l'auteur, mais sans nommer ni favoriser aucun mécanisme de résolution particulier.
- **`0,31` à `0,49` (admissible sous réserve, orientation perceptible)** : le vocabulaire ou le découpage canalise l'exploration vers un sous-espace restreint d'approches, tout en laissant subsister une pluralité réelle d'hypothèses concurrentes.
- **`0,50` à `1,00` (rejeté, souffle la réponse)** : le texte contient des indices directifs permettant de reconstruire la thèse préférée de l'auteur, disqualifie d'avance des familles légitimes ou dicte implicitement l'architecture attendue.

---

## 2. Vérification mécanique de la garde de motifs (`motifs_trouves`)

L'importation sans écriture disque du module `collisionneur_v9_v8d.py` et l'application de la fonction `motifs_trouves` (qui détecte sept catégories interdites : nom de personne, identifiant de session, identifiant unique universel à trente-six caractères hexadécimaux et tirets, adresse de courriel, chemin interne au dépôt ou au système de fichiers, identifiant d'accord d'exécution et identifiant de registre de décisions) donnent les résultats suivants, tant sur les octets décodés en format de transformation universel sur huit bits que sur la chaîne normalisée par `lire_entree` et sur les invitations complètes d'étage III reconstituées avec préambule, balises d'empreinte et consignes :

| Fichier examiné | Octets | Caractères (`lire_entree`) | Empreinte cryptographique à 256 bits (`sha256`) | Résultat de `motifs_trouves` (isolé et assemblé) |
|---|---:|---:|---|---|
| `faits-neutres-boucle-organisme-controle-v2.md` | 4 946 | 4 780 | `032fe7871dbd3a626b12b4ac39fa2bc8a97d3e135598281096a55b2f8da12984` | `[]` (vide, sain) |
| `question-neutre-collisionneur-boucle-organisme-controle-v2.md` | 2 853 | 2 758 | `da1105bc276fa9d94ca34343cd3bd1cb57fec4d428d06193ec318d7c279a4cd7` | `[]` (vide, sain) |
| `question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md` | 2 703 | 2 598 | `ee981d084e5b2706271802a85a70ebfa6f2dfd42e76e82539e8abcc3f12bcef4` | `[]` (vide, sain) |
| `sous-question-organisme-boucle-controle-v2.md` | 786 | 760 | `f532324de0bcda0e7e813e363facabd6bd7857ab005928de29baf2d7db0815e2` | `[]` (vide, sain) |

Aucun motif interdit n'est présent dans aucune des quatre pièces (`motifs_trouves(...) == []` vérifié partout).

---

## 3. Examen individuel à l'aveugle : devinette et neutralité

### 3.1. `faits-neutres-boucle-organisme-controle-v2.md`

#### Test de devinette (ce qu'un lecteur aveugle peut et ne peut pas inférer)

- **Ce qui se devine sur la posture méthodologique de l'auteur :**
  1. L'auteur applique une discipline statistique stricte d'inférence séquentielle valide à tout instant (« garantie de faux positifs toujours valide ») et connaît précisément une limite théorique de l'étalonnage empirique : l'incise « toute accumulation séquentielle étalonnée sur une référence honnête fixe de taille finie plafonne lorsque l'horizon dépasse la taille de cette référence, sauf usage d'un nul par acte » révèle un acquis technique précis déjà établi dans le programme de contrôle.
  2. L'auteur considère la contamination adaptative entre optimisation et évaluation comme une faute rédhibitoire : interdiction d'injecter un score de moniteur dans la sélection d'un agent ou d'un proposeur, familles de sabotage inédites lues une seule fois, banque de validation finale lue une seule fois en fin de boucle, préenregistrement systématique.
  3. L'auteur travaille sous une asymétrie matérielle prononcée (abondance relative de calcul sur processeur central pour les mondes synthétiques de l'organisme, rareté des cartes graphiques pour les modèles ouverts de huit milliards de paramètres). La mise en regard finale (ligne 29) fait ressortir mécaniquement deux tensions structurelles : le fossé de validité entre mondes synthétiques à lois plantées et activations réelles de modèles ouverts, et l'impossibilité d'interroger à haute fréquence les banques finales du programme de contrôle.

- **Ce qu'il est impossible de deviner :**
  - On ne peut deviner **aucune thèse de l'auteur sur la manière de fermer la boucle**. L'auteur préfère-t-il une boucle purement descendante, une remontée d'invariants abstraits anonymisés, une banque intermédiaire d'activations figées rejouables sur processeur, une allocation séquentielle de budget d'erreur statistique, un filtrage bayésien multi-fidélité, une recherche évolutionnaire de diversité, une synthèse symbolique d'opérateurs ou une induction causale sur graphes ? Rien dans le texte ne donne le moindre indice.
  - Sur les trois axes du contrôle (détection séquentielle, corruptibilité rhétorique des juges contre sondes sur l'auteur, essaims à poids partagés), l'exposé décrit les objets d'étude et les mesures visées sans préjuger du verdict empirique ni désigner d'instrument gagnant.

#### Analyse de neutralité et motivation du score

Les contraintes énoncées dans la deuxième et la troisième sections limitent certes l'espace des architectures recevables (toute boucle d'apprentissage par renforcement direct sur les scores des moniteurs ou sur la banque finale est exclue par les règles existantes), mais il s'agit de **contraintes constitutives réelles du dispositif existant**, indispensables pour éviter que les répondants ne travaillent hors sujet. Le ton est strictement descriptif, exempt d'adjectifs valorisants sur une piste donnée ; l'expression « idées profondes, de nouveaux objets mathématiques, des protocoles d'audit ou des scénarios de défaillance » couvre un spectre large et équilibré de livrables possibles. Seule la mention très spécifique du « nul par acte » signale un intérêt technique particulier de l'équipe en statistique séquentielle, sans toutefois orienter l'architecture de l'organisme d'idéation.

- **Score d'orientation attribué : `0,14` / `1,00` — ADMIS** (largement inférieur au seuil strict de `0,50`).

---

### 3.2. `question-neutre-collisionneur-boucle-organisme-controle-v2.md`

#### Test de devinette (ce qu'un lecteur aveugle peut et ne peut pas inférer)

- **Ce qui se devine sur les préoccupations et soupçons de l'auteur :**
  1. Le point 3 (« Formalisation mathématique et conditions de validité de la boucle fermée ») dévoile quatre verrous précis que l'auteur juge centraux : (a) le risque de circularité statistique d'une boucle fermée ; (b) la nécessité d'un arbitrage quantitatif explicite entre le coût des épreuves et le rendement de découverte ; (c) le risque d'effondrement de la validité lorsqu'on quitte les environnements synthétiques ; (d) le besoin de contrôles négatifs capables de démasquer une boucle illusoire.
  2. Le point 4 (« notamment lorsque des modèles pré-entraînés interviennent » à propos des fuites d'information statistiques ou temporelles) laisse deviner sans ambiguïté que l'auteur soupçonne une fuite temporelle par mémorisation préalable dans les poids des modèles pré-entraînés lorsque l'organisme explore des graphes scientifiques historiques datés.
  3. Le point 7 montre que l'auteur privilégie une hiérarchisation coût-efficacité multiplicative pénalisant fortement la lourdeur matérielle ou humaine (diviseur `coût` de `1` à `5`), tout en sachant que cette agrégation comporte une part d'arbitraire puisqu'il exige une étude de sensibilité du classement à une variation de pondération.

- **Ce qu'il est impossible de deviner :**
  - La formulation « le couplage entre l'organisme d'idéation et le programme de contrôle **dans ses directions utiles** » est remarquablement prudente : elle ne présuppose même pas que les deux sens de la boucle doivent avoir le même poids ou la même granularité, et laisse au répondant la liberté de restreindre ou d'asymétriser un canal s'il le juge dangereux.
  - Aucune famille algorithmique n'est soufflée au point 4 (« Compare plusieurs familles d'approches distinctes » ne nomme aucune méthode).
  - Aucun formalisme mathématique n'est soufflé au point 3 (ni théorie de l'information, ni analyse de données adaptative, ni contrôle stochastique multi-étapes, ni bornes de transfert de distribution, ni filtrations temporelles).
  - Aucune parade spécifique contre la contamination temporelle des modèles pré-entraînés n'est suggérée.

#### Analyse de neutralité et motivation du score

La question guide davantage l'attention thématique que les seuls faits : en nommant explicitement l'arbitrage coût/rendement, la sortie du synthétique et la fuite temporelle des modèles pré-entraînés dans les points 3 et 4, elle fournit déjà aux modèles une partie de la grille critique que le point 1 (« Ce qu'un expert du domaine ferait ici, et que la demande d'origine omet ») leur demande par ailleurs d'identifier d'eux-mêmes. Cependant, **poser des exigences de validité épistémique n'équivaut pas à souffler la solution** : toutes les exigences formulées sont des conditions nécessaires d'intégrité scientifique découlant logiquement des faits (graphes datés + modèles pré-entraînés = question de l'étanchéité temporelle ; processeur synthétique + cartes graphiques rares = question du transfert et de l'allocation budgétaire). Les duels d'hypothèses exclusives (hypothèse première `H_A` contre hypothèse seconde `H_B`) imposent la réfutabilité sans dicter le contenu des cinq chantiers.

- **Score d'orientation attribué : `0,22` / `1,00` — ADMIS** (nettement inférieur au seuil strict de `0,50`).

---

### 3.3. `question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md`

#### Test de devinette (ce qu'un lecteur aveugle peut et ne peut pas inférer)

- **Ce qui se devine sur les préférences de l'auteur :**
  1. On devine uniquement l'éthique méthodologique générale du protocole : méfiance envers les mécanismes illusoires en boucle fermée, exigence d'étanchéité des mesures, appel à une vérification indépendante hors de l'équipe de conception, discipline d'inférence forte par duels falsifiables (`H_A` contre `H_B`) munis de contrôles négatifs, et souci d'économie de calcul via la même règle de classement pondérée par le coût.

- **Ce qu'il est impossible de deviner :**
  - Contrairement à `question-neutre-collisionneur-boucle-organisme-controle-v2.md`, un lecteur qui ne lirait que ce texte témoin ne peut même pas deviner quels sous-risques précis préoccupent particulièrement l'auteur (ni la fuite temporelle spécifique aux modèles pré-entraînés, ni la modélisation formelle du compromis coût/rendement multi-fidélité, ni la rupture de validité propre aux mondes synthétiques ne sont pointés dans les consignes des points 3 et 4, qui restent formulées en termes très généraux : « quels risques statistiques, algorithmiques ou épistémiques menacent une telle boucle fermée » et « comment garantir la validité des mesures »).
  - *Observation rédactionnelle mineure sans incidence sur la neutralité* : le point 6 demande une reformulation « qui intègre les quatre points précédents » alors qu'il est précédé de cinq points numérotés de 1 à 5 ; cette légère imprécision de décompte n'introduit aucun biais directionnel.

#### Analyse de neutralité et motivation du score

Ce texte remplit exemplairement sa fonction de **bras témoin neutre** : il aligne le format de sortie, la profondeur attendue et la métrique de priorisation sur la question principale afin de rendre les réponses comparables, tout en retirant le guidage analytique fin des points 3 et 4. Il permettra ainsi de vérifier si les diagnostics et architectures proposés par les modèles sous la question principale émergent déjà spontanément à partir des seuls faits ou s'ils dépendent du cadrage plus explicite de la question principale.

- **Score d'orientation attribué : `0,09` / `1,00` — ADMIS** (très largement inférieur au seuil strict de `0,50`).

---

### 3.4. `sous-question-organisme-boucle-controle-v2.md`

#### Test de devinette (ce qu'un lecteur aveugle peut et ne peut pas inférer)

- **Ce qui se devine sur les attentes de l'auteur :**
  1. Le triplet « concepts mathématiques, **signatures** ou protocoles réellement exploitables » introduit le substantif « signatures » (absent tel quel des trois autres textes). Un lecteur attentif peut en inférer que l'auteur songe notamment à l'extraction d'invariants ou de signatures quantitatives sur les activations internes ou les trajectoires multi-agents pour alimenter les sondes boîte blanche.
  2. La fin du paragraphe (« sans sur-apprentissage des évaluations ni perte de validité hors des bancs synthétiques », « conditions statistiques, budgétaires et temporelles », « contrôle négatif falsifiable sur un cas nul sans progrès réel ») révèle la même tétrade de préoccupations défensives que la question principale : refus de l'adaptation aux banques d'essai, défiance envers les artefacts purement synthétiques, vigilance sur les coupures temporelles et exigence d'un test d'invalidation sur un régime de bruit ou de stagnation (« cas nul sans progrès réel »).

- **Ce qu'il est impossible de deviner :**
  - Le mot « signatures » étant encadré à parts égales par « concepts mathématiques » et « protocoles », aucune nature d'objet n'est imposée.
  - Les « mécanismes formels ou algorithmiques retenus » restent entièrement à inventer par le répondant : aucun algorithme d'exploration, aucun schéma de rétroaction, aucun estimateur statistique ni aucune construction précise du « cas nul sans progrès réel » n'est esquissé.

#### Analyse de neutralité et motivation du score

Condensée en une seule entrée autonome de sept cent soixante caractères, cette sous-question pose nettement le problème d'ingénierie scientifique sous contraintes sans préempter les réponses. L'orientation résiduelle tient uniquement à l'indice lexical léger du mot « signatures » et à l'énumération explicite des quatre garde-fous de validité (sur-apprentissage, transfert hors synthétique, contraintes statistiques-budgétaires-temporelles, cas nul sans progrès réel), qui balisent la rigueur attendue sans restreindre la liberté de conception théorique ou algorithmique.

- **Score d'orientation attribué : `0,19` / `1,00` — ADMIS** (largement inférieur au seuil strict de `0,50`).

---

## 4. Analyse d'interaction entre les pièces et bilan récapitulatif

Lorsqu'on combine `faits-neutres-boucle-organisme-controle-v2.md` avec chacune des trois formulations interrogatives :

1. **Absence d'effet de tenaille directionnel :** la juxtaposition des faits et de `question-neutre-collisionneur-boucle-organisme-controle-v2.md` ne crée pas de syllogisme caché qui imposerait une unique réponse. Au contraire, il existe une tension féconde et non résolue entre le désir d'orienter l'organisme par les observations du contrôle et l'interdiction stricte d'utiliser les scores des moniteurs comme signal de sélection ou de relire les familles tenues à l'écart. Plusieurs résolutions théoriquement inconciliables restent pleinement ouvertes aux modèles (découplage par abstractions structurelles sans données du contrôle, banques publiques ou jouets d'activations de modèles tiers hors périmètre d'évaluation, budget formel de fuite d'information bornée sur un sas intermédiaire dédié, ou architecture purement unidirectionnelle sur le plan statistique).
2. **Pertinence du contraste entre question principale et question témoin :** l'écart de score d'orientation entre la question principale (`0,22`) et la question témoin (`0,09`) mesure exactement l'apport de structuration analytique des points 3 et 4 (mention explicite du compromis coût/rendement, du transfert hors synthétique et des modèles pré-entraînés), sans qu'aucune des deux ne franchisse ni même n'approche la zone d'orientation critique (`0,50`).

### Tableau récapitulatif des scores et décisions

| Pièce évaluée | `motifs_trouves` | Score d'orientation | Seuil strict | Décision | Motif principal du score résiduel |
|---|---|---:|---:|---|---|
| `faits-neutres-boucle-organisme-controle-v2.md` | `[]` | `0,14` | `< 0,50` | **ADMIS** | Règles d'étanchéité existantes et incise technique sur le « nul par acte », sans aucune piste de couplage soufflée. |
| `question-neutre-collisionneur-boucle-organisme-controle-v2.md` | `[]` | `0,22` | `< 0,50` | **ADMIS** | Cadrage explicite de quatre risques (circularité, coût/rendement, hors synthétique, fuite temporelle des modèles pré-entraînés), mais zéro algorithme ou formalisme soufflé. |
| `question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md` | `[]` | `0,09` | `< 0,50` | **ADMIS** | Seul le cadre général d'inférence forte et de score rapporté au coût est posé ; sous-risques laissés à la découverte spontanée. |
| `sous-question-organisme-boucle-controle-v2.md` | `[]` | `0,19` | `< 0,50` | **ADMIS** | Indice lexical léger (« signatures ») et rappel condensé des conditions statistiques, budgétaires, temporelles et de cas nul. |

**Conclusion générale du test de neutralité et de devinette :** les quatre textes passent haut la main le test de devinette à l'aveugle (scores compris entre `0,09` et `0,22`, tous strictement inférieurs à `0,50`) ainsi que la garde mécanique des motifs interdits (`motifs_trouves(...) == []` sur chaque fichier isolé et assemblé). Ils sont aptes à être soumis au collisionneur sans retouche.
