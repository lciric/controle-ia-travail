## Périmètre et présupposés

**Pièces absentes de la transmission :** générations complètes (seulement 24 lignes d’échantillon), entrées `R*_input_*.json`, `R6_descriptive_counts.json`, tout le code, les textes d’items, le prompt du juge et les pages des mentors ; je ne peux donc ni exécuter les analyses, ni citer les chercheurs, ni attribuer honnêtement les idées à un mentor.

**Statuts employés :** **OBSERVÉ-NON-AUDITÉ** = visible dans les pièces fournies, sans recalcul indépendant ; **RAPPORTÉ** = affirmation des README ou audits décrits par le dépôt ; **HYPOTHÈSE** = mécanisme ou résultat à tester. Aucun résultat empirique n’est élevé ici au statut **VÉRIFIÉ**.

### (a) Ce que le brief suppose sans que ce soit établi

- **Que la loi soit générale.** Elle est **RAPPORTÉE** pour Llama dans plusieurs lectures et sur items neufs ; R3 rapporte au contraire des régimes *offset* pour Qwen et Mistral, et une attraction seulement critique pour Gemma. R6 réfute la stabilité du point fixe et de son gain selon la dose, pas l’ajustement linéaire à chaque dose.
- **Que la note 1–5 mesure un verdict subjectif valide.** **RAPPORTÉ :** aucune validation humaine R5 n’est publiée ; le prompt du juge est privé, l’alias API non figé, et des réponses neutres identiques ont parfois reçu des notes différentes dans R6. L’accord entre juges sur C1/C2 n’établit pas la validité de construit.
- **Que \(g,\hat c\) identifient un mécanisme d’attraction.** C’est une **HYPOTHÈSE**. Refus notés au milieu, compression d’échelle, longueur, concession rhétorique et changement de justification restent des explications concurrentes.
- **Que les 1 200 textes soient intégralement auditables ici.** Leur publication est **RAPPORTÉE** ; seules 24 réponses sont **OBSERVÉES-NON-AUDITÉES** dans ce paquet.
- **Que la puissance soit calculable maintenant.** Elle ne l’est pas honnêtement sans exécution ni plusieurs entrées `results/`. Elle devra être simulée en rééchantillonnant les items et en conservant les appariements visibles dans `c2a_results.json` et `c2b_results.json`.
- **Nouveauté et mentors :** nouveauté **non cherchée** pour toutes les idées ; pages mentor absentes, donc aucune attribution ni citation inventée.

Les phrases anglaises suivantes sont des **HYPOTHÈSES de résultats possibles**, non des résultats acquis. Les nouveaux plans et coûts sont **illustratifs**.

## Dix résultats possibles et leurs duels décisifs

### 1. *Repeated judging may move the estimated destination without changing any response.*
Le bruit de lecture pourrait déplacer \(\hat c\), plutôt que la dose elle-même ; rival : ce bruit est négligeable devant les déplacements d’items.  
**Duel :** H_A = relecture instable matériellement ; H_B = conclusions invariantes. Relire les mêmes réponses publiques et les neutres R6, ordre randomisé, puis recalculer \(g,\hat c\). **Métrique/seuil :** variance intra-texte et \(\Delta\hat c\) entre lots ; changement de C1/C2/H3 ou IC95 % de \(\Delta\hat c\) excluant 0. **Contrôle négatif :** doublons exacts et identifiants permutés. Oui : une partie de R6 devient instrument-dépendante ; non : H_A est falsifiée dans la limite de précision atteinte.  
**Données/coût/preuve :** aucune génération ; lectures API seulement, quelques dollars ; republication des notes et relecture indépendante Qwen.

### 2. *Pressure may renegotiate the presentation of a verdict rather than simply reverse it.*
Concessions, refus, mentions de l’utilisateur et *hedging* pourraient porter le déplacement ; rival : une loi résiduelle subsiste sans ces marqueurs.  
**Duel :** H_A = compte rendu surfacique suffisant ; H_B = déplacement de polarité indépendant. Annoter les 1 200 textes, avec sous-ensemble humain aveugle. **Métrique/seuil :** gain de SSE hors items et loi résiduelle après stratification ; IC95 % d’amélioration au-dessus de 0. **Contrôle négatif :** annotations permutées ; modèles à battre : longueur seule et lexique de première phrase. Un oui falsifie H_B ; l’absence de gain avec loi résiduelle falsifie H_A.  
**Coût/preuve :** zéro génération ; annotations ouvertes et vérification humaine indépendante.

### 3. *The pressured displacement may live after the opening verdict, not in it.*
Le modèle pourrait maintenir son engagement initial puis modifier sa justification ; rival : l’ouverture porte déjà tout le déplacement.  
**Duel :** H_A = effet localisé dans l’ouverture ; H_B = effet localisé après elle. Faire relire séparément première phrase, reste et texte entier. **Métrique/seuil :** \(\Delta\) par segment et contraste \(\Delta_{\text{ouverture}}-\Delta_{\text{reste}}\), IC95 % apparié. **Contrôle négatif :** paires dont l’ouverture est identique et doublons relus. Les deux localisations pures sont falsifiables ; une mixture devra être rapportée comme telle.  
**Coût/preuve :** textes existants, lectures ouvertes seulement ; annotation humaine du locus de verdict.

### 4. *Praise may move free-text rhetoric while leaving the model’s stated verdict unchanged.*
R2 suggère une dissociation de canaux ; rival : l’auto-notation directe est un instrument trop insensible.  
**Duel :** H_A = dissociation réelle ; H_B = artefact R2. Joindre aux données existantes l’auto-notation par Llama de ses propres réponses libres, après un test de calibration sur verdicts explicites. **Métrique/seuil :** contraste de \(\Delta\) entre lecture directe, auto-relecture et juge ; IC95 % excluant 0, sous réserve que le test de calibration réussisse. **Contrôle négatif :** textes synthétiques à verdict constant, neutre apparié.  
**Coût/preuve :** aucune nouvelle réponse libre ; calcul 8B seulement ; réplication sur une autre famille.

### 5. *Reader-specific destinations may collapse after calibration on neutral responses alone.*
Les cibles différentes de Claude, Qwen-7B et Qwen-72B pourraient refléter des échelles distinctes ; rival : elles restent propre au lecteur après calibration.  
**Duel :** H_A = destination latente commune ; H_B = destinations spécifiques. Ajuster une transformation affine uniquement sur le neutre, tester sur les réponses pressées et items réservés. **Métrique/seuil :** écarts résiduels de \(\hat c\), avec marge d’équivalence tirée du bruit mesuré en idée 1 ; comparaison de SSE hors échantillon. **Contrôle négatif :** identifiants de réponses permutés ; références sans calibration et moyenne seule.  
**Coût/preuve :** réutilisation ou nouvelles lectures ouvertes ; recalcul public des transformations.

### 6. *Neutral response variance may predict which items pressure captures.*
Un \(g\) unique pourrait masquer une susceptibilité liée à l’incertitude de l’item ; rival : le \(g\) fixe suffit hors échantillon.  
**Duel :** H_A = \(g\) fixe transportable ; H_B = variance neutre prédictive d’un gain variable. Ajuster sur campagne 1, tester sans réajustement sur R4 et R6-standard. **Métrique/seuil :** différence de SSE hors items contre la loi publiée, IC95 % supérieur à 0 dans les deux bras. **Contrôle négatif :** variances permutées entre items ; prédicteurs longueur et moyenne seule à battre.  
**Coût/preuve :** analyse seule, **0 $** si les entrées publiques sont récupérées ; recalcul intégral par instance neuve.

### 7. *Floor and ceiling geometry may explain much of the criticism–praise asymmetry.*
La distance disponible sur l’échelle pourrait produire l’asymétrie ; rival : il reste un effet propre à la direction sociale.  
**Duel :** H_A = géométrie bornée suffisante ; H_B = asymétrie résiduelle directionnelle. Construire un nul borné conservant moyenne et variance neutres, puis tester sur campagne 1 et R2. **Métrique/seuil :** asymétrie résiduelle après appariement sur \(p_0\) et variance ; IC95 % et transport hors items. **Contrôle négatif :** échange des bras et subdivisions neutres.  
**Coût/preuve :** `c2a_results.json`, `c2b_results.json`, sorties R2 ; **0 $**, entièrement recalculable.

### 8. *The moving destination may track wording identity rather than perceived intensity.*
R6 confond intensité, longueur et construction lexicale ; rival : une intensité perçue commune prédit les cibles à travers paraphrases.  
**Duel :** H_A = intensité causale ; H_B = identité/longueur de formulation. Croiser paraphrases, longueur et intensité, avec prétest humain des phrases seules ; mêmes items et graines Llama. **Métrique/seuil :** prédiction de \(\hat c\) sur formulations réservées et contraste monotone ; IC95 % apparié. **Contrôle négatif :** phrase standard répétée et ajout non évaluatif ; modèle nombre-de-mots à battre.  
**Coût/preuve :** nouvelles générations 8B et juges, quelques dizaines de dollars au plus ; réplication indépendante des lectures.

### 9. *Evaluative anchors may reproduce attraction without any social praise or blame.*
L’effet pourrait être un ancrage évaluatif générique ; rival : il exige une pression sociale à la première personne.  
**Duel :** H_A = spécificité sociale ; H_B = ancrage générique. Comparer critique/éloge utilisateur, verdict attribué à un tiers et cote non sociale, en appariant longueur et contenu. **Métrique/seuil :** contrastes de \(g,\hat c\) et transport sans réajustement ; équivalence bornée par le bruit de lecture. **Contrôle négatif :** phrase non évaluative et neutre répété ; ancre numérique mécanique à battre.  
**Coût/preuve :** génération Llama seulement au départ ; vérification sur Qwen ou Mistral pour distinguer sujet et instrument.

### 10. *Monitor deference may collapse when a note contradicts an unambiguous verdict.*
R7 pourrait mesurer suivisme d’instruction ; rival : le moniteur intègre la note comme indice et résiste lorsqu’elle est contredite.  
**Duel :** H_A = suivisme indépendant du texte ; H_B = intégration probante. Étendre R7 aux notes congruentes, contradictoires et sans rapport, sur réponses à verdict explicite. **Métrique/seuil :** gain de déférence, taux de fausse alerte et pente taille–gain ; seuils M1/M3 existants et règle d’engagement R7. **Contrôle négatif :** réponse identique sans note, note véridique décrivant le verdict déjà présent ; moniteur mécanique « toujours 1/5 » à battre.  
**Coût/preuve :** aucune génération de réponses ; Qwen ouverts, logits publiés et recalcul externe.

## (c) Validation minimale des instruments

| Instrument | Cas appariés honnêtes et mesure minimale | Vérifications mécaniques à battre |
|---|---|---|
| Juge Claude et lecteurs Qwen 1–5 | **Détection :** flips de verdict construits et relus par humains aveugles. **Fausses alertes :** même texte, paraphrase, allongement ou *hedging* sans changement de verdict. Rapporter taux par bras, dose et famille. | Note extraite d’une phrase explicite, lexique de première phrase, longueur seule, moyenne par item. |
| Auto-notation R2 | Calibration sur réponses dont le verdict chiffré est explicite ; détection de changements imposés, aucune variation sur entrée strictement identique. Publier masse des chiffres et désaccords argmax/\(r\). | Argmax seul, extraction du chiffre présent, classement par mots de polarité. |
| Juge par paires du programme antérieur | Détection sur paires ne différant que par le verdict ; fausse alerte sur doublons, reformulations et changements stylistiques. | Accord avec un lexique et comparaison première phrase/dernière phrase. |
| Motifs fixes refus/contre-pieds R6 | Corpus annoté incluant refus implicites et désaccords ; négations, citations et mentions non performatives comme cas honnêtes. | Les motifs R6 eux-mêmes et un classifieur longueur-seule. |
| Analyses figées et moniteurs R7 | Données synthétiques sous attraction, *offset*, absence d’effet, régression et refus-au-milieu ; taux de détection et faux positifs par scénario. | Aucun changement, déplacement constant, moyenne du corpus, modèle refus-seul ; tests métamorphiques d’échange de bras et de permutation d’items. |

## (d) Ancrage matériel, classement et falsification

**Matériel :** Llama-3.1-8B, Qwen2.5-7B/72B et autres tailles R7 sont ouverts ; Mistral-7B et Gemma-2-9B servent de réplication. Le brief donne 450 générations 8B float32 ≈ 1 h 30 sur 48 Go. **RAPPORTÉ :** R4 a coûté 2,39 $ pour 900 générations et lectures ; R6, 24,7 $ pour 5 400 ; R1b, environ 0,63 $ sur deux A100 80 Go. Toute extrapolation budgétaire ci-dessus reste **illustrative**.

**Classement valeur/coût :** **6, 7, 2, 1, 4, 3, 5, 10, 8, 9**. La première est première parce qu’elle peut réfuter le paramètre central \(g\) par recalcul public, sans nouvelle dépense.

**Trois observations falsifiantes :**
1. Sur nouveaux items, la loi campagne-1 ne bat ni déplacement constant ni absence de changement : futur analogue de `results/R4/R4_output_items60.txt`, avec C3 faux.
2. Les déplacements s’éloignent de la cible ou C4 échoue dans les deux bras : même fichier R4 et son entrée par item.
3. À formulation standard et sur graines fraîches, C1 disparaît, ou une structure résiduelle non linéaire bat la droite hors items : `R6_llama_standard_output_items30_K5.txt`, `R6_llama_dose_output.txt` et un nouveau fichier de résidus préenregistré. R3 réfute déjà l’universalité inter-familles ; R6 réfute déjà la stabilité dose–point fixe.

**Contenu textuel visible mais non généralisable :** dans les 24 lignes **OBSERVÉES-NON-AUDITÉES**, on voit maintien explicite sous éloge, concession à la critique, recentrage « plus objectif », verdict initial suivi de nuances et un refus sous éloge. Seule l’analyse complète proposée en idées 2–3 dira leur fréquence et leur contribution.

**Non vérifié :** chaîne de custody et CI ; antériorité Zenodo ; audits privés ; textes complets et prompt du juge ; entrées R* absentes ; code figé ; puissance ; validité humaine ; pages mentor ; nouveauté bibliographique ; coûts des nouvelles extensions.

FIN-DE-CELLULE