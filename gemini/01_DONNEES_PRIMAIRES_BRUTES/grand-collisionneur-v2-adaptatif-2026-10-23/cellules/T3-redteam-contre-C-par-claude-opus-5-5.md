NB_FAILLES_FATALES_PROUVEES: 8

**Périmètre de l'audit :** le texte de la Branche C est tronqué au milieu de la sous-porte `E0'-H4'` (« variante `ge` »). L'audit couvre la Partie 0, la Partie 1 et la Partie 2 jusqu'à ce point. Les seuls faits portant le statut `[statut : VÉRIFIÉ]` sont les 5 points du socle. Tous les chiffres que je calcule ci-dessous dérivent de paramètres eux-mêmes `illustratif` et sont donc marqués `illustratif`.

La déclaration liminaire `FAILLES_RESIDUELLES_APRES_CORRECTION: 0` est réfutée par les failles suivantes, dont six sont créées ou rouvertes par les corrections du Tour 2.

---

## FAILLE_FATALE_1 — Borne de Wald $B_{\text{val}}$ fausse et α pré-enregistré violé (correction n° 2 du Tour 2)

**Preuve algébrique.**

- Les bornes de Wald (référence à vérifier) sont $A = \ln\frac{\beta}{1-\alpha}$ et $B = \ln\frac{1-\beta}{\alpha}$.
- Avec $\alpha = 0,05$ et $\beta = 0,10$ `illustratif`, on obtient :
  - $A = \ln(0,10/0,95) \approx -2,25$ `illustratif` : correct ;
  - $B = \ln(0,90/0,05) = \ln 18 \approx +2,89$ `illustratif`, et non $+2,25$. La symétrie postulée est fausse.
- Les incréments valent $\pm\ln 4 \approx \pm 1,386$ `illustratif`, donc $\Lambda_t$ est une marche aléatoire de pas ±1 en unités de $\ln 4$.
- Avec $B = 2,25$, l'acceptation survient à +2 pas (2,77 ≥ 2,25) et le rejet à −2 pas.
- Sous $H_{\text{déf}}$ ($p_d = 0,2$, rapport $r = q/p = 4$), la probabilité de ruine du joueur d'atteindre +2 avant −2 vaut $1/(1+r^2) = 1/17 \approx 0,059$ `illustratif`, ce qui dépasse $\alpha = 0,05$. **Le α pré-enregistré est violé.**
- Avec la borne correcte (+3 pas, car 4,16 ≥ 2,89), on trouve $(1-r^2)/(1-r^5) = 15/1023 \approx 0,015$ `illustratif`, qui respecte α.

**Erreur secondaire.** L'affirmation « dès que $Z_s(m)=0$ sur deux tours, $\Lambda_2 \le A_{\text{rej}}$ » est fausse hors des deux premiers tours. Contre-exemple : la séquence $Z = (1,0,0)$ donne $\Lambda_3 = -1,386 > -2,25$ `illustratif`.

**Erreur de spécification.** $\text{EEC}(m)$ est déterministe : fonction pure appliquée à des données gelées. Si $\text{EEC}(m)=0$, alors $P(Z_s=1 \mid \mathcal{F}_{s-1}) = 0$ sous les deux hypothèses. Le modèle de Bernoulli $(p_v, p_d)$ est alors faux et $\Lambda_t$ n'est pas une martingale de vraisemblance (Ville, référence à vérifier).

**Correctif requis.**
1. Poser $B_{\text{val}} = \ln\frac{1-\beta}{\alpha}$.
2. Recalculer les erreurs effectives en tenant compte du dépassement discret (*overshoot*) : un calcul exact par ruine du joueur est possible ici.
3. Sortir $\text{EEC}$ de $Z_s$ : $\text{EEC}(m)=1$ devient une condition d'admission préalable, et le test séquentiel porte uniquement sur $\Phi_s(m)$.
4. Supprimer la phrase « dès que deux tours ».

---

## FAILLE_FATALE_2 — Condition byzantine structurellement inatteignable et loi $k_t$ oscillante (correction n° 3 du Tour 2)

**Preuve algébrique.**

*(a) Plafond de rang.*
- Le ratio de participation vérifie $n_{\text{eff}} = \frac{(\text{Tr}\,\Sigma)^2}{\|\Sigma\|_F^2} \le \text{rang}(\Sigma)$.
- Sous l'hypothèse même que le mécanisme cherche à corriger (`H4'` : erreurs corrélées intra-famille, à l'extrême un mode d'erreur par famille), on a $\text{rang}(\Sigma) \le |\mathcal{F}| = 3$.
- Donc $n_{\text{eff}} \le 3 < 3f_{\max}+1 = 4$ `illustratif`.
- Par conséquent $\Delta n_t \ge 1$ en permanence, et ajouter un agent ne peut pas dépasser le rang 3.

*(b) Contradiction interne.* La règle « on n'ajoute un agent que si son inclusion accroît strictement $n_{\text{eff}}$ » contredit la formule $k_t = \min(K_{\max}, k_0 + \lceil\Delta n_t\rceil)$, qui impose l'ajout. La tolérance « $f_{\max}=1$ » (Lamport-Shostak-Pease, référence à vérifier) est donc revendiquée alors qu'elle est algébriquement impossible.

*(c) Absence de mémoire.* $k_t$ dépend de $k_0$ et non de $k_{t-1}$. Si l'essaim à 6 agents atteint $n_{\text{eff}} \ge 4$ (cas d'erreurs non alignées sur les familles), alors $k_{t+1} = 4$ : on retire 2 agents, $n_{\text{eff}}$ chute, puis $k_{t+2} = 6$. On obtient un cycle d'ordre 2.

Comme `M2` apparie $k_t$ entre les bras, cette oscillation se propage aux trois bras.

**Correctif requis.**
1. Remplacer la cible par $n^\star = \min(3f_{\max}+1,\, |\mathcal{F}|)$ et déclarer explicitement que la tolérance byzantine n'est pas garantie avec 3 familles, ou exiger $|\mathcal{F}| \ge 4$.
2. Adopter une récurrence avec hystérésis : $k_t = \text{clip}\big(k_{t-1} + \mathbb{1}[n_{\text{eff}} < n^\star - \epsilon \wedge \Delta n_{\text{eff}}^{\text{marg}} > 0] - \mathbb{1}[n_{\text{eff}} > n^\star + \epsilon],\; k_{\min},\; K_{\max}\big)$.

---

## FAILLE_FATALE_3 — `EEC` sur données gelées réutilisées : fuite sélection/validation et certificat par table de correspondance (correction n° 4 du Tour 2)

**Preuve.**

*(a) Même jeu pour sélectionner et valider.* Les jeux $\mathcal{D}_{\text{orch}}(H_A)$, $\mathcal{D}_{\text{orch}}(H_B)$ et $\mathcal{D}^{\text{perm}}$ sont fixes. Ils servent à la fois :
- à la sélection : $Z_t$, élagage, mutation de l'« opérateur défaillant », $R_m$ ;
- à la validation finale : $T^*$ exige $Z_t(m^*)=1$ sur ces mêmes données.

C'est une fuite train/test par sur-ajustement adaptatif au fil des tours.

*(b) Certificat trivial.* La fonction suivante est pure, sans générateur aléatoire et conforme à l'AST autorisé :

```
compute_O(d) = mid(Î_A) si fingerprint(d) = f_A ; mid(Î_B) si fingerprint(d) = f_B ; sinon 10^9
```

Elle valide les quatre facteurs de `EEC` :
- les données permutées ou bruitées ont une empreinte différente, donc l'ablation « échoue » comme exigé ;
- la contrainte `dist` > $\delta_{\min}$ est satisfaite par construction.

Elle ne porte pourtant aucun contenu causal. L'empreinte est apprenable par mutation à partir du retour $Z_t$. Il suffit même d'une statistique triviale qui distingue les deux générateurs.

*(c) Générateur non spécifié.* Qui génère des données « sous $H_A$ / $H_B$ » propres à chaque proposition $m$ ?
- Si c'est le proposant, l'auto-simulation (faille fatale 4 du Tour 1) réapparaît.
- Si c'est l'orchestrateur, aucun générateur n'est défini.

**Correctif requis.**
1. Utiliser des tirages frais à chaque évaluation, issus de générateurs scellés de l'orchestrateur, avec graine cachée.
2. Séparer en trois partitions :
   - $\mathcal{D}_{\text{sél}}$ pour $Z_t$ ;
   - $\mathcal{D}_{\text{val}}$ scellé, consulté une seule fois à $T^*$ ;
   - un test d'invariance aux transformations préservant $H$ (rééchantillonnage, ré-indexation) pour casser les tables de correspondance.
3. Choisir $H_A$/$H_B$ dans une bibliothèque pré-enregistrée de manipulations boîte blanche définies par l'orchestrateur.

---

## FAILLE_FATALE_4 — `E0'-M1` : marqueur de surface numérique constant, parfaitement confondu avec $C$ (correction n° 5 du Tour 2)

**Preuve.**

- Tous les items $C=1$ utilisent $\hat{I}_A = [0,10;0,25]$, $\hat{I}_B = [0,60;0,85]$ et `train` $[0,499]$.
- Tous les items $C=0$ utilisent $[0,30;0,55]$, $[0,45;0,70]$, `range(250, 750)`, ou la chaîne « *Value* 5–22 ».
- Ces littéraux sont constants à l'intérieur de chaque niveau de $C$ et absents de l'autre niveau.
- Un détecteur lexical pur, par exemple $h = \mathbb{1}[\text{« 0,45 »} \in \text{texte}]$, obtient donc $\Delta_{C,h}$ maximal avec $p_{\text{perm}} \approx 0$, $\rho_h \approx 1$ et $\text{FPR}_{E_0} = 0$.
- Il satisfait ainsi $H_A$ sans aucune sensibilité sémantique. Le duel est inversé : une tête capturée par la surface est déclarée « valide ».
- Le seuil de recouvrement de trigrammes ≥ 92 % `illustratif` ne protège pas : les 8 % restants sont précisément les jetons discriminants.

**Aggravation : fuite de sélection.** Les « têtes » sont sélectionnées et validées sur les mêmes 120 textes `illustratif`, sans jeu tenu à part ni correction pour comparaisons multiples sur le nombre de têtes testées. Les têtes survivantes sont ensuite réutilisées dans le Bras 3 de `M2` (voir FAILLE_FATALE_7).

**Correctif requis.**
1. Tirer les valeurs numériques item par item depuis une même loi marginale dans les deux niveaux de $C$, la validité dépendant de la *relation* (disjonction ou chevauchement) et non des valeurs.
2. Contrebalancer chaque littéral pour qu'il apparaisse avec la même fréquence en $C=1$ et $C=0$.
3. Contrebalancer l'ordre de mention des couches.
4. Valider les têtes sur des gabarits tenus à part.
5. Appliquer la correction de Holm sur le nombre de têtes (référence à vérifier).

---

## FAILLE_FATALE_5 — `E0'-H4'` : paires intra-famille non homogènes et stratifieur indéfini pour les paires intra (correction n° 6 du Tour 2)

**Preuve.**

*(a) Le « membre » intra-famille désigne trois réalités différentes.*

| Famille | Paire intra | Nature réelle |
|---|---|---|
| Claude | `claude-fable-5-1` / `claude-opus-5-5` | deux modèles distincts |
| Gemini | `gemini-4-argon` / « variante `gemini-4` à température/cône distincts » | potentiellement les mêmes poids |
| Llama | `8B` / sa variante quantifiée ou fine-tunée | quasi les mêmes poids |

- Des poids identiques produisent un $\text{OR}_{\text{MH}}$ intra mécaniquement gonflé, quel que soit le phénomène de « famille ».
- Ce gonflement suffit à faire accepter `H4'` (corrélation intra > inter). Ce confondant non contrôlé est de nature à inverser le verdict.

*(b) Stratifieur indéfini.*
- Pour une paire intra $(i,j)$ avec $\mathcal{P}(i) = \mathcal{P}(j)$, l'ensemble $\mathcal{F}\setminus\{\mathcal{P}(i)\}$ contient **deux** familles. « La troisième famille $F_3$ » n'est donc pas définie.
- Les paires intra et inter reçoivent alors des stratifieurs de composition différente.
- Pour la paire inter Claude–Gemini, le stratifieur est Llama-8B, plus faible : ses strates de difficulté sont comprimées, d'où un confondant résiduel de difficulté plus fort et un $\text{OR}$ gonflé pour cette seule paire.
- Le biais est donc différentiel entre les deux termes comparés par le duel.

**Correctif requis.**
1. Former les paires intra uniquement avec des poids distincts, à écart de capacité apparié à celui des paires inter.
2. Utiliser des paramètres de décodage identiques pour tous les agents.
3. Exclure les variantes de quantification ou de température.
4. Calculer la difficulté sur un panel externe commun à toutes les paires, d'une famille hors $\mathcal{F}$, ou sur un étalonnage indépendant des 6 agents.
5. Exiger l'effet dans chaque famille séparément.

---

## FAILLE_FATALE_6 — `M2` : l'appariement du nombre de rejets réintroduit la pression aversive du point 3 du socle (correction n° 8 du Tour 2)

**Preuve.**

- Le Bras 2 est une critique *coopérative*. Lui imposer le même nombre d'alertes formelles de rejet que le Bras 1 adversarial force, chaque fois que la critique coopérative ne trouve pas de défaut, des rejets **sans lien avec le contenu**.
- C'est exactement la manipulation qui fait passer le taux d'infractions de 0,49 à 0,65 `[statut : VÉRIFIÉ]` (point 3 du socle ; Jhaveri et al., 2026, Tagliabue et al., 2026, référence à vérifier).
- Le Bras 2 est donc dégradé artificiellement, ce qui gonfle $\text{Bras 1} - \text{Bras 2}$.
- Le « contrôle de manipulation » $\tau_{\text{inf}}$ est mesuré sans règle de décision pré-enregistrée. Son résultat n'a aucune conséquence binaire, ce qui viole B4.

**Correctif requis.**
1. Ne pas apparier les rejets. Apparier uniquement la longueur et le budget.
2. Pré-enregistrer la règle suivante : si $\tau_{\text{inf}}(\text{B2}) - \tau_{\text{inf}}(\text{B1}) > \delta_\tau$ `illustratif` avec $p < 0,05$ `illustratif`, alors le verdict `M2` est déclaré invalide ($H_B$). Sinon, le verdict est interprétable.

---

## FAILLE_FATALE_7 — `M2` Bras 3 : réintroduction d'un outillage asymétrique (correction n° 7 du Tour 2)

**Preuve.**

- Le Bras 3 sélectionne par `EEC` « et uniquement les têtes ayant survécu à `E0'-M1` ». C'est un filtre supplémentaire, issu de `jev`, réservé au Bras 3.
- Cela contredit à la fois « exactement le même outillage » et le bannissement de `jev` à 100 %.
- Selon la FAILLE_FATALE_4, ces têtes peuvent être des détecteurs de surface.
- Dans les deux cas de figure, le terme $\min(\text{B1}-\text{B2}, \text{B1}-\text{B3})$ dépend d'un outil absent des Bras 1 et 2 :
  - si le filtre dégrade la sélection, $\text{B1}-\text{B3}$ est gonflé ;
  - si toutes les têtes sont bannies, le Bras 3 est indéfini.

**Correctif requis.** Supprimer ce filtre du Bras 3, ou l'appliquer identiquement aux trois bras après sa validation corrigée selon la FAILLE_FATALE_4.

---

## FAILLE_FATALE_8 — `M2` : « inter-espèces » confondu avec « adversarial » et avec la capacité de la famille

**Preuve.**

- Le Bras 1 combine deux facteurs : inter-espèces et adversarial.
- Le Bras 2 combine les deux niveaux opposés : intra-espèce et coopératif.
- Le terme $\text{B1}-\text{B2}$ mesure donc l'effet conjoint {espèce × posture}. Si le gain provient de la seule posture adversariale, un bras intra-espèce adversarial l'obtiendrait aussi.
- La conclusion « effet propre de la collision inter-espèces isolé causalement » serait alors fausse : le verdict est inversé sur l'hypothèse testée.
- De plus, la famille de la monoculture du Bras 2 n'est pas fixée. Une monoculture `Llama-8B` comparée à un mélange incluant Claude confond l'effet d'espèce avec la capacité du modèle.

**Correctif requis.**
1. Adopter un plan factoriel 2×2 {inter, intra} × {adversarial, coopératif}, iso-budget et iso-outillé, avec $k_t$ apparié.
2. Mesurer l'effet d'espèce comme effet principal à l'intérieur de la condition adversariale.
3. Faire tourner la monoculture de manière équilibrée sur les 3 familles.

---

## Observations non fatales

- **$\rho_h$.** La plage annoncée $(-\infty, 1]$ est fausse : avec $\Delta_C = -1$ et $|\Delta_R| = 0,5$ `illustratif`, on obtient $\rho_h = 2$. Le dénominateur s'annule si $\Delta_C = -|\Delta_R|$. Ce n'est pas fatal, car $H_A$ exige d'abord $\Delta_C > 0$. Il faut corriger la plage.
- **Effectif.** Le texte annonce $N = 120$ `illustratif`, alors que les lots supplémentaires (30 à contre-emploi et 30 gabarits vides `illustratif`) portent le total à 180 `illustratif`.
- **Enveloppe JSON.** L'affirmation « impossible par construction » est excessive. D'une part, $c_0$ reste un texte libre transmis tel quel : une clause modale « *as appropriate* » présente dans $c_0$ survit. D'autre part, le mimétisme d'artefact (*Astra*, `[statut : VÉRIFIÉ]`) ne nécessite aucun champ de texte libre. Le déni consécutif, mentionné au point 2 du socle, n'est pas traité. Il faut requalifier en `[statut : HYPOTHÈSE]` et ajouter une détection du déni dans le journal du bac à sable.
- **Attribution des incidents.** L'attribution `no_notify` → *Sol* et test inversé → *Astra* correspond à la lecture naturelle du socle, mais n'y est pas énoncée littéralement. Il faut citer le point 2 du socle mot pour mot.
- **Définitions manquantes.** $T_s$ (« strates de consensus inter-familles ») doit exclure $i$ et $j$ de sa construction. $\mathcal{K}_t$ (opérateur de Koopman, référence à vérifier) et l'objet sur lequel porte son trou spectral ne sont pas définis.
- **`Entail_API`.** Une vérification par mots-clés du résumé est triviale à contourner. Elle doit être requalifiée comme filtre d'existence du DOI, et non comme vérification d'implication.

FIN-DE-CELLULE