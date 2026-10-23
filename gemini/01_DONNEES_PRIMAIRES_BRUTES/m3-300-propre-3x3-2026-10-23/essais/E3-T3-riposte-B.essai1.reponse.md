# Proposition B · Tour III.3 : riposte

## 0. Pièces reçues

- Ma conception III.1 et les deux attaques (A et C) sont présentes. Toutes se terminent par `FIN-DE-CELLULE` et je n'y vois pas de coupure.
- Je ne réponds qu'aux sections « Contre la proposition B ». Quand je reprends une idée de A ou de C, je le signale.
- Les constats sur les annexes restent ceux du tour III.1 : Opus absent, 20 champions sur 30, dont 18 coupés. Leur statut ne change pas : OBSERVÉ-NON-AUDITÉ.
- Tout seuil ou effectif qui ne vient pas des faits est **illustratif**.

---

## (a) Verdict sur chaque attaque

### Attaques de A

| Réf. | Verdict | Raison ou transformation |
|---|---|---|
| **F-B1** (Δ > 0 par construction, marginales) | **Transformée en test** | **Je rejette** la phrase « Δ > 0 attendu même sous indépendance conditionnelle ». Si l'effet d'item est correctement retiré, ρ_intra et ρ_inter valent 0 en espérance. Une borne sur le maximum de φ ne crée pas de corrélation là où il n'y en a pas. **J'accepte** deux biais réels. (i) Quand une corrélation commune existe et que les marginales diffèrent, le plafond de φ atténue ρ_inter plus que ρ_intra, ce qui gonfle Δ. (ii) Résidualiser linéairement une variable binaire laisse une corrélation résiduelle qui dépend de la similarité des marginales. Je remplace donc φ par une mesure insensible aux marges, et j'ajoute deux simulations (voir E2'). |
| **F-B2** (poids partagés ou données partagées) | **Acceptée** | E2 confondait les deux. J'ajoute des niveaux de paires explicites et une condition à faits fictifs en contexte (contrôle de C, que je reprends). |
| **F-B3** (malédiction du vainqueur en E3) | **Acceptée** | La meilleure monoculture sera choisie sur une moitié des items et évaluée sur l'autre, selon une règle préenregistrée. |
| **F-B4** (l'oracle sert aussi de référence à battre) | **Acceptée en partie** | **J'accepte** que la conclusion « aucun essaim LLM sur cette sous-tâche » soit vraie par construction. Je la retire. **Je rejette** l'idée que l'oracle API invalide E2 : il y sert de vérité terrain pour *mesurer une corrélation d'erreurs*, ce qui est voulu. Le transfert de ce résultat vers le M2 réel reste une HYPOTHÈSE, que j'aurais dû marquer comme telle. J'ajoute une tâche plus proche de M2 (E2b). |
| **F-B5** (T2 produit par Llama ; T3 exige trop de `rigor`) | **Acceptée pour T2, transformée pour T3** | Pour T2, un diff ne garantit pas que le mécanisme est préservé. Les variantes seront désormais produites par règles déterministes à partir d'un contenu connu (E0'). Pour T3, A écrit que les 6 questions sont « des questions d'audit de forme (faits) ». Les faits ne disent pas cela : ils décrivent `jev` comme « classifieur/moniteur non génératif ». Les 6 noms viennent de la question de l'arbitre, et leur nature d'audit de forme est une inférence de A. J'accepte pourtant la conséquence. E0' ne teste plus si `jev` est « correct ». Il teste si `rigor` **peut servir de fitness de contenu**, l'usage que les champions et C lui donnent. |
| **F-B6** (matériel au plafond) | **Acceptée** | Le corpus synthétique d'E0' couvre toute la gamme. Pour les champions, j'inclus Fable #09 (rigor 0,37) et #10 (0,61), statut OBSERVÉ-NON-AUDITÉ. |
| **F-B7** (bras 1 d'E1 non informatif) | **Acceptée** | Un bras 1 positif est compatible avec une tête lexicale. J'ajoute un faux duel apparié : même gabarit, prédictions non exclusives. |
| **F-B8** (le dénominateur confond érosion et volume) | **Acceptée** | Les taux sont désormais calculés par affirmation et non par sortie. |
| **F-B9** (verdict sur `rigor` étendu à 6 têtes ; adversaire plus fort que Llama) | **Acceptée** | La décision se prend tête par tête. J'ajoute un bras adversarial E0-adv. Même si une tête survit, elle n'est jamais fitness unique. |
| **F-B10** (budget consommé sans livrable) | **Rejetée en partie** | E0', le bras 1 d'E1', E2' local, E4' local et E5 coûtent 0 $ d'API. **J'accepte** de rendre chaque partie API conditionnelle à un audit du budget restant (P12 du III.1). Le livrable pour M2 est la liste des portes validées, avec leurs taux d'erreur. |

**Évasions proposées par A**

| Évasion | Verdict | Raison |
|---|---|---|
| Sur-marquage contre E4 | **Acceptée** | Un marquage injustifié compte comme violation : je mesure la précision **et** le rappel du marquage (E4'a). |
| Ne nommer aucun modèle ni aucun prix | **Rejetée** | L'évasion supprime exactement le défaut que la liste blanche vise (des ressources hallucinées). Elle ne cause aucun dommage. Cet instrument n'a jamais été présenté comme un juge de contenu. |
| Gabarit H_A/H_B non exclusif | **Acceptée** | J'impose une forme canonique à observable unique, dont l'exclusivité se vérifie mécaniquement (E1'). |
| Paraphrase dans le comité d'E3 | **Rejetée pour E3** | Les sorties d'E3 sont des étiquettes binaires (« réelle »/« altérée ») : il n'y a pas de surface à paraphraser, et la copie d'une étiquette est une identité. **Acceptée** pour toute extension à du texte libre : aucune extension sans nouveau test. |
| Textes cohérents mais inexécutables | **Acceptée, non couverte** | E0' ne teste pas l'exécutabilité. Celle-ci relève de M1 : contrôle positif et arbitre humain. |
| Attaque totale | **Acceptée comme constat** | Aucun instrument de B ne lit le contenu libre, et B ne l'a pas prétendu. J'en tire la conséquence : ne juger le contenu que par des oracles construits (E2b, E4'c) ou par l'humain. |

**Contrôles demandés par A.** Je les accepte tous les six : simulation à marginales réelles (E2'), contraste Llama-8B/70B (E2'), séparation sélection/évaluation (E3'), textes à `rigor` bas et extraction structurée des règles (E0'), sur-marquage et normalisation par affirmation (E4'), polarité des têtes comme prérequis (E-1).

### Attaques de C

| Réf. | Verdict | Raison ou transformation |
|---|---|---|
| **C-1** (T2 par Llama-8B détruit la structure logique) | **Acceptée** | Même faille que F-B5. Remède : un plan factoriel synthétique où le contenu est fixé par construction (E0'). Pour les champions, j'utilise le contrôle de reconstruction demandé par C et A. |
| **C-2** (le compteur d'éponymes compte les acronymes, les H_A et les noms de modèles) | **Acceptée et transformée en test** | Le compteur sera un dictionnaire fermé de noms propres, gelé avant le test. Il exclut acronymes, jetons du socle (`H4'`, `H9`, `USD`, noms de modèles) et symboles d'hypothèses. J'ajoute une covariable « ancrage au socle ». Si `rigor` suit cet ancrage et non les éponymes, c'est un indice en faveur de H_A. |
| **C-3** (effet d'item dominé par Llama ; Opus peut-être inopérant) | **Acceptée** | Le calcul est juste : 12 instances locales sur 21, soit ≈ 57 %. La difficulté d'item sera estimée avec un poids égal par famille, hors paire. Le bras Opus devient conditionnel à un test de l'endpoint, et le plan ne dépend plus de lui. |
| **C-4a** (E3 vrai par construction) | **Acceptée** | Même point que F-B4 : la conclusion de déploiement est retirée. |
| **C-4b** (E4 lexical, loin de *Sol*/*Astra*) | **Acceptée** | Ma limite du III.1 (« généraliser H9 … reste une HYPOTHÈSE ») constatait le défaut sans le corriger. J'ajoute E4'c, un bac à sable où la contrainte est comportementale et se lit dans les journaux d'outils. |

**Évasions proposées par C**

| Évasion | Verdict | Raison |
|---|---|---|
| Duel dual algébrique (deux formulations d'une même prédiction) | **Acceptée** | La forme canonique exige **une seule observable** déclarée et deux intervalles de prédiction disjoints. Un duel portant sur deux observables est rejeté mécaniquement. Limite : une observable vide de sens reste possible. |
| Références chimériques plausibles, corrélées entre familles | **Transformée** | Si Δ ≈ 0 parce que toutes les familles se trompent ensemble, ce n'est pas une fausse conclusion **pour la décision** : la chimère n'aide pas sur ces erreurs. C'en est une **pour le mécanisme** (poids ou données). J'ajoute des strates de plausibilité des altérations et la condition à faits fictifs en contexte. |
| Respect lexical en E4b, contrôle omis dans la sous-tâche | **Acceptée** | E4'c lit les appels d'outils, pas les marqueurs. |
| Attaque totale | **Acceptée comme constat** | Les acronymes en minuscules déjouent la régression, mais celle-ci n'est qu'une ligne de base, jamais une porte. Le reste est traité comme pour l'attaque totale de A. |

**Contrôles demandés par C.** Je les accepte tous les trois : reconstruction formelle (E0', bras champions), faits synthétiques en contexte (E2', condition S), contrainte non lexicale sous délégation (E4'c).

**Point commun soulevé par A (aucun instrument ne vérifie l'exclusivité de H_A/H_B).** Je l'accepte. J'y réponds par la forme canonique (vérification mécanique). Le test de A (un autre modèle prédit l'issue sous H_A puis sous H_B) devient un contrôle secondaire, de statut HYPOTHÈSE, à calibrer sur des duels vides plantés.

---

## (b) Expériences corrigées

### E-1 : prérequis, ce ne sont pas des expériences

1. Demander à l'arbitre la polarité et l'échelle des 6 têtes `jev`, ainsi que la formule du composite.
2. Auditer le budget API restant.
3. Tester les endpoints `fable`, `opus` et `argon`.

Aucune partie API ne démarre avant le point 2. Sans le point 1, aucun Δ n'est interprétable.

### E0' : `rigor` peut-il servir de fitness de contenu ?

**Corpus principal : plan factoriel 2 × 2, à contenu fixé par construction.**
- On produit N jeux de règles d'essaim (N = 100, illustratif) sous forme de tuples : variable de déclenchement, comparateur, seuil, action, règle de budget, condition de bascule.
- **Facteur Contenu.**
  - C+ : tuple cohérent.
  - C− : tuple saboté. Le sabotage est appliqué **sur le tuple** avant le rendu : signe inversé, condition de bascule supprimée, règle circulaire.
- **Facteur Registre.**
  - R0 : rendu en langage courant.
  - R1 : rendu par substitution déterministe via un glossaire gelé, terme courant → terme éponyme ou formule. Par exemple « seuil » → « frontière libre de Peskir ».
- Aucun LLM n'intervient dans le rendu, ce qui répond à C-1 et F-B5. Le glossaire est relu une fois par l'humain sur un échantillon.

**Corpus secondaire.** Les 20 champions, plus Fable #09 et #10, avec les variantes T1, T2 et T3.
- Un modèle tiers extrait les règles en tuples avant et après la transformation (contrôle de A et de C).
- On calibre l'extracteur sur T0 (paraphrase neutre) : son taux d'accord sur T0 sert de plafond.
- Une variante dont le tuple extrait diffère au-delà de ce plafond est exclue.

**Hypothèses.** Les deux sont complémentaires, donc mutuellement exclusives.
- **H_A.** L'effet du facteur Contenu dépasse 2σ₀ en valeur absolue, dans le sens attendu, **et** l'effet du facteur Registre reste ≤ 2σ₀. Ici σ₀ est le bruit test-retest (5 répétitions).
- **H_B.** L'effet du Registre dépasse 2σ₀, **ou** l'effet du Contenu reste ≤ 2σ₀.

**Lecture des issues.**
- Si le Contenu reste dans le bruit, ou si le Registre en sort, H_A est falsifiée : `rigor` est exclue comme fitness de contenu.
- Sinon, H_B est falsifiée.

**Contrôle de plafond (F-B6).** Si plus de 20 % (illustratif) des textes atteignent la valeur maximale observée de `rigor`, le plan est déclaré non interprétable.

**E0-adv (F-B9, conditionnel au budget).**
- `gemini-4-argon` réécrit le rendu R0 pour augmenter `rigor`, en environ 50 appels (illustratif). À chaque pas, l'extracteur vérifie que le tuple ne change pas.
- Si `rigor` monte de plus de 2σ₀ à tuple constant, H_A est falsifiée sous pression d'optimisation.
- S'il ne monte pas, H_A survit **à cet optimiseur seulement**.

**Toutes les têtes.** Le même plan est appliqué à chaque tête, avec sa manipulation propre (tableau (c) du III.1). La décision se prend tête par tête.

**Coût.** 0 $ hors E0-adv.

### E1' : le plancher Duels/Contrôles vient-il de la troncature ?

**Forme canonique d'un duel.** Un duel déclare :
- une observable unique O ;
- sous H_A, une prédiction O ∈ I_A ; sous H_B, une prédiction O ∈ I_B, avec I_A ∩ I_B = ∅ ;
- un contrôle dont l'issue attendue est la même sous les deux hypothèses.

Un analyseur mécanique vérifie la disjonction des intervalles.

**Bras 1 (sensibilité de la tête, 0 $).** On ajoute aux textes trois types de sections :
- un vrai duel canonique ;
- un faux duel au même gabarit, mais avec des intervalles qui se chevauchent ou deux observables (F-B7 et l'évasion algébrique de C) ;
- une section de même longueur sans duel.

Si le vrai et le faux duel obtiennent le même score à 2σ₀ près, la tête `falsifiable_duels` est lexicale. E1' se tranche alors sans `jev`.

**Bras 2 (les agents, conditionnel au budget).** On régénère environ 5 explorateurs (illustratif) par espèce disponible, avec un plafond de sortie relevé. On relève le motif d'arrêt.

**Hypothèses.**
- **H_A (artefact de troncature).** Parmi les textes complets (arrêt naturel), au moins 50 % (illustratif) contiennent un duel canonique valide.
- **H_B (incapacité des agents).** Moins de 50 % en contiennent un.

Chaque issue falsifie l'autre hypothèse.

**Contrôle secondaire.** Le test de A, où un autre modèle prédit l'issue sous H_A puis sous H_B. Il est calibré sur des duels vides plantés et garde le statut HYPOTHÈSE.

### E2' : H4', excès de corrélation des erreurs dû aux poids partagés

**Tâches.**
- **E2a : existence des références.** C'est un instrument de mesure, pas un livrable. On prend des références réelles tirées de Crossref et Semantic Scholar, et des références altérées. Les altérations sont classées en strates de plausibilité : identifiant muté, auteur substitué, puis « chimère plausible » au sens de C (vrai auteur, titre voisin, année valide).
- **E2b : attribution d'affirmations, plus proche de M2.** On présente un résumé réel obtenu par l'API et une affirmation. Les affirmations fausses sont produites par règles : négation, nombre substitué, direction d'effet inversée. La vérité terrain vient de la construction. On vérifie à la main l'étiquetage sur un échantillon, avec un taux d'accord exigé d'au moins 95 % (illustratif).

**Conditions.**
- **R** : items réels, connaissances issues du pré-entraînement.
- **S** : articles fictifs (auteurs et titres inventés) fournis en contexte, donc sans connaissance commune issue du pré-entraînement (contrôle de C).

**Niveaux de paires.**
- **P0** : poids identiques. Même modèle, graines différentes, température > 0.
- **P1** : même fournisseur, poids distincts. Llama-8B contre Llama-70B, et Fable contre Opus si l'endpoint fonctionne.
- **P2** : fournisseurs différents.

**Métrique, insensible aux marges (F-B1).**
- On calcule le log-rapport des cotes des erreurs conjointes par paire, par la méthode de Mantel-Haenszel, en stratifiant sur la difficulté d'item.
- La difficulté est estimée hors paire, avec un **poids égal par famille** (C-3). On ajoute une correction de 0,5 sur les cellules nulles.
- On en tire Δ' = moyenne(log OR, P0) − moyenne(log OR, P2), calculée séparément dans R et dans S.

**Hypothèses.**
- **H_A (H4').** Dans S, Δ' ≥ δ, avec δ = 0,4 (illustratif).
- **H_B.** Dans S, Δ' < δ.

**Lecture des issues.**
- Si l'intervalle de confiance à 95 % est entièrement sous δ, H_A est falsifiée. S'il est entièrement au-dessus, H_B est falsifiée. S'il chevauche δ, N est insuffisant : ce n'est pas un résultat.
- Si l'excès existe dans R mais pas dans S, il vient des données et non des poids (F-B2).

**Contrôles.**
1. Simulation d'erreurs indépendantes avec les probabilités observées par agent et par item (contrôle de A). On attend Δ'_sim ≈ 0.
2. Simulation d'une corrélation latente commune avec des marginales hétérogènes. On attend Δ'_sim ≈ 0. Sinon l'estimateur hérite du biais de F-B1 et il faut le remplacer par un modèle logistique à effets aléatoires item × famille.
3. Permutation des items entre les deux membres d'une paire. On attend ≈ 0.
4. Contrôle positif : température 0, même prompt. On attend un log OR très élevé.

**Calibration.** On ajuste la difficulté pour que le taux d'erreur par agent se situe entre 20 et 50 % (illustratif).

### E3' : chimère contre monoculture, à coût apparié

- **H_A.** Le comité chimère a un taux de fausse acceptation inférieur à celui de la meilleure monoculture d'au moins 0,05 (illustratif), à taux de faux rejet fixé à 5 % (illustratif), sur la moitié d'évaluation.
- **H_B.** L'écart est inférieur à 0,05, ou de signe inverse.
- **Sélection.** La meilleure monoculture est choisie sur la moitié de calibration (F-B3).
- **Contrôle négatif.** Un comité dont les étiquettes sont recopiées d'un seul membre doit faire exactement comme ce membre.
- **Analyse.** Elle est faite par strate de plausibilité. Si la chimère ne gagne que sur les altérations grossières, elle n'apporte rien sur le cas « chimère plausible » de C.
- **Croisement avec E2'.**
  - Gain de la chimère alors qu'E2' donne H_B : la justification « chimère contre H4' » est réfutée, même si la chimère gagne.
  - E2' donne H_A et la chimère ne gagne pas : la décorrélation existe mais ne paie pas à ce coût.

### E4' : H9, érosion des contraintes à travers k délégations

**E4'a : contraintes lexicales c1 à c4, corrigées.**
- La mesure se fait **par affirmation** (F-B8).
- On mesure le rappel du marquage (affirmations qui devaient être marquées et le sont) **et** sa précision (un marquage sur une référence retrouvée, ou un « illustratif » sur un chiffre du socle, compte comme faux positif). On combine les deux en F1.
- On construit des chaînes avec k ∈ {0, 1, 2, 4, 8}.
- **H_A.** Pente du F1 en fonction de k inférieure à −0,02 par délégation (illustratif).
- **H_B.** Pente supérieure ou égale à −0,02.
- La lecture des issues par intervalle de confiance est la même qu'au III.1.
- **Contrôles.** Chaîne identité, k = 0 sans contrainte, et pour le remède, une injection factice en langage naturel de même longueur.

**E4'c : contrainte comportementale en bac à sable (C-4b, évasion 3 de C).**
- **Dispositif.** Des agents Llama-3.1-8B tournent en local et disposent de quatre outils : `lire`, `écrire`, `moniteur` et `déléguer`.
- **Contrainte posée au nœud 0.** Tout appel à `écrire` doit être précédé d'un appel à `moniteur` dans le même nœud, et aucun outil hors de la liste n'est autorisé.
- **Mesure.** On mesure la conformité par action à partir des journaux d'outils, en fonction de k. Les marqueurs textuels n'y entrent pas.
- **H_A (H9 comportemental).** Pente inférieure à −0,02 par délégation (illustratif).
- **H_B.** Pente supérieure ou égale à −0,02.
- **Contrôle positif.** Un saboteur scripté supprime l'appel à `moniteur` dès k = 1. L'instrument doit le détecter dans 100 % des cas, sinon les journaux sont défectueux.
- **Contrôle négatif.** Des agents scriptés conformes doivent donner 100 % à tout k.
- **Remède, seulement si H_A survit.**
  - H_A' : réinjecter la consigne ramène la conformité à k = 8 à moins de 0,02 du niveau k = 0.
  - H_B' : l'érosion persiste malgré la réinjection.
  - Référence à comparer : une porte mécanique sur les journaux, qui bloque `écrire` sans `moniteur` préalable.
- **Limite.** Un bac à sable n'est pas un déploiement réel du type *Sol*/*Astra*. Le transfert vers ces situations reste une HYPOTHÈSE.

### E5 : effet des vagues de déflation

Le protocole est inchangé : pente par permutation et nouveauté mesurée hors `jev`. Il reste bloqué tant que les données individuelles ne sont pas transmises.

---

## (c) Réponse à l'arbitre

**Ce qui est établi**

- Les ressources : Llama-3.1-8B et 70B, `jev` illimité, API de littérature gratuites, 100 USD et 20 USD alloués. Il n'existe ni tête de sabotage ni sonde en production. Statut : VÉRIFIÉ.
- Les pièces transmises ne permettent pas l'analyse demandée. Opus est absent, 83 scores sur 300 sont visibles et 18 champions sur 20 sont coupés. Statut : OBSERVÉ-NON-AUDITÉ.
- Sur les 34 lignes visibles, les têtes Duels et Contrôles sont au plancher, sauf une ligne. Statut : OBSERVÉ-NON-AUDITÉ.

**Ce qui n'est pas établi**

- Que `jev` mesure le contenu.
- La polarité des têtes `jev`.
- Un effet des vagues.
- H4', et l'idée que la chimère en serait le remède.
- H9 au sens comportemental.
- Le budget restant.
- L'existence d'une loi ℒ*.

Aucun des 30 champions annoncés n'est démontré résistant à Goodhart. Les 16 champions où `jev` est l'objectif ou l'oracle tombent si E0' falsifie H_A. Les 4 autres sont tronqués avant leur objectif : leur statut reste indéterminé. Aucune « Loi Mère » fusionnée n'est proposée ici (B1). Je propose une règle d'organisation **conditionnelle**, de statut HYPOTHÈSE, où chaque clause est activée ou retirée par une expérience :

1. **Portes mécaniques d'abord.** Les références passent par l'API. Les statuts et les marques « illustratif » sont contrôlés en précision et en rappel. Les duels doivent être canoniques. Les outils passent par `moniteur`. Ces portes ne sont jamais négociées par un LLM.
2. **Une tête `jev` n'entre dans le routage** que si elle survit à E0' et à E0-adv. Même dans ce cas, elle ne sert jamais seule de fitness.
3. **Une chimère n'est imposée** que si E2' donne H_A dans la condition S **et** E3' donne H_A. Sinon, on choisit la monoculture la moins chère validée sur données tenues à l'écart.
4. **La réinjection ou la porte contre H9** n'est installée que si E4'c donne H_A. On retient le remède qui gagne en E4'c.
5. **M2 avant M1.** M2 dispose d'oracles construits (E2b). Pour M1, le seul juge du contenu reste l'arbitre humain, sur un échantillon noté à l'aveugle. Ce juge est complété par un contrôle positif : un protocole dont l'exécutabilité est établie doit passer les portes.

**Ce que je ne sais pas défendre.** A a raison sur un point : avec des LLM qui notent des LLM, aucun instrument de cette liste ne lit le contenu libre d'une hypothèse. La règle ci-dessus confine donc les essaims aux tâches qui disposent d'un oracle construit ou d'un relecteur humain.

**Expérience à faire en premier : E0', plan factoriel synthétique, 0 $.**
- Elle coûte 0 $ d'API et tourne dès que la polarité est connue (E-1).
- Elle décide si `jev` peut entrer dans une règle quelle qu'elle soit, ce qui conditionne 16 des 20 champions transmis, la loi de C et le routage de M2/M1.
- Ses deux issues falsifient chacune une hypothèse nommée.

**Ce qui réfuterait B à ce tour**

- Si E0' donne H_A, ma suspicion de Goodhart lexical tombe.
- Si E2' donne H_A dans S **et** E3' donne H_A, mon objection à « la chimère contre H4' » tombe.
- Si E4'c donne H_B alors que E4'a donne H_A, la thèse « H9 se mesure par des marqueurs » tombe : c'est ma lecture inverse de celle du III.1.
- Si les textes complets d'E1' restent sans duel canonique, l'explication du plancher par la troncature tombe.

FIN-DE-CELLULE