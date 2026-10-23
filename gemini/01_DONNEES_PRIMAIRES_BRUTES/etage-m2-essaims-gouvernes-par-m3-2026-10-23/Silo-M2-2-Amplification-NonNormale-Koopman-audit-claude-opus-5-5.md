NB_FAILLES_M2: 13

**Pièces manquantes (Règle 2).**
- Les paramètres `{lettre}`, `{autres}`, `{mots}` et `{marqueur}` ne sont pas résolus.
- La « matrice de prédation apprise en M3 » est absente. J'audite donc sur critères explicites.
- Les propositions des autres lettres sont absentes.
- Les résumés de 2403.00447v3 et 2010.00268v1 sont coupés, comme le signale déjà le pont.

---

## (1) Le résumé soutient-il l'opérateur ?

**F1. Le résumé ne soutient pas l'opérateur.**
- La citation d'ancrage figure mot pour mot dans le résumé transmis : le statut RAPPORTÉ est correct pour la phrase elle-même.
- Ce résumé traite de trajectoires de dynamiques en temps continu, localement Lipschitz, qui convergent vers un système dynamique projeté (PDS) quand le paramètre de la CBF tend vers l'infini.
- L'opérateur du pont est une application statique, appliquée une fois par couche et par token. Les couches ne sont pas un temps continu, et il n'y a ni champ de vecteurs ni trajectoire.
- *Correctif :* étiqueter explicitement « transfert CBF → flux résiduel » comme HYPOTHÈSE. Retirer toute formulation qui suggère que l'article la couvre.
- Les quatre autres résumés (2406.02709, 2003.05711, 2010.00268, 0904.2875) ne sont pas invoqués. Aucun ne soutient l'opérateur.

**F2. L'opérateur n'est pas une CBF et sa limite n'est pas un PDS.**
- On a $B=\tau-\|U^\top h\|^2$.
- **Zone non sûre ($B<0$) :** le coefficient vaut 1, donc l'opérateur fait une projection brute, celle-là même qu'on voulait éviter.
- **Zone sûre ($B>0$) :** l'opérateur intervient quand même, avec un coefficient $1/(1+\gamma B)$. Cela contredit l'intervention minimale propre aux CBF.
- **Quand $\gamma\to\infty$ :** on obtient une annulation complète hors de l'ensemble sûr. Ce n'est pas la projection sur $\{\|U^\top h\|^2\le\tau\}$, qui serait un rétrécissement radial vers $\sqrt{\tau}$.
- *Correctif :* soit $\tilde h = h - \big(1-\sqrt{\tau}/\max(\sqrt{\tau},\|U^\top h\|)\big)\,UU^\top h$ (projection exacte sur l'ensemble sûr), soit une version lissée explicite, avec sa propriété de Lipschitz démontrée et non supposée.

**F3. La prémisse « discontinuité » est mal posée.**
- $h\mapsto h-UU^\top h$ est linéaire, donc continue. La discontinuité d'un PDS concerne son champ de vecteurs en temps continu, pas une projection.
- *Correctif :* reformuler l'HYPOTHÈSE de manière mesurable, par exemple « la projection brute augmente la norme du jacobien inter-couches dans des directions hors de $S_{\text{TD}}$ ».

## (2) Dimensions des tenseurs sur `Llama-3.1-8B-Instruct`

Les valeurs $d=4096$ et 32 couches proviennent de la configuration publique du modèle, pas des faits transmis. Elles sont donc illustratives jusqu'à vérification sur `config.json`. Les couches 2 à 22 donnent bien $L=21$, et `h @ U` donne bien la forme $(T,L,k)$ puis $(T,L)$. La forme est cohérente, la spécification non.

**F4. Le seuil $\tau$ n'est pas normalisé.**
- $\tau=0.20$ (illustratif) s'applique à une énergie brute, avec le même seuil sur 21 couches.
- Si les normes résiduelles dépassent largement $\tau$, ce qui est à vérifier, l'opérateur se réduit partout à la projection brute.
- *Correctif :* utiliser $\|U^\top h\|^2/\|h\|^2$, ou un $\tau_\ell$ calibré par couche sur des prompts neutres.

**F5. Des axes manquent.**
- La dimension token est absente : il faut préciser $(T,N_{\text{tok}},L,d)$ ou la position agrégée.
- Il manque $k$.
- Un $U$ unique pour 21 couches est douteux ; il faut un $U_\ell$ de forme $(L,d,k)$.
- L'indexation est ambiguë : dans `hidden_states`, l'indice 0 correspond aux embeddings.
- Il faut forcer le passage bf16 → float32 avant le calcul.

**F6. La mesure est tautologique.**
- `compute_O` ne précise pas si `h_perturbed` est capturé avant ou après le hook.
- Si l'opérateur est appliqué à chaque couche et que l'énergie est mesurée sur ce même $U$ après le hook, alors $O\approx 0$ par construction. $\hat I_A$ est atteint sans rien démontrer.
- *Correctif :* mesurer l'effet en aval, sur les couches non modifiées ou sur la sortie (taux de comportement aversif, logits), ou sur un sous-espace sondé indépendamment.

**F7. La métrique n'est pas calibrée.**
- Le rapport couche finale / couche initiale n'est pas une amplification transitoire, qui se mesure par un pic intermédiaire $\max_\ell$.
- Rien ne montre que `compute_O` reproduit 0.49 → 0.65 (OBSERVÉ-NON-AUDITÉ) sur la ligne de base.
- Un rapport de 0.49 signifie d'ailleurs une atténuation.
- Le `max` sur $T$ est fragile, et le terme `1e-8` fait exploser le rapport si l'énergie de la couche 2 est quasi nulle.
- *Correctif :* auditer d'abord l'observation de base (n, graines, définition). Utiliser $\max_\ell$, puis un quantile par bootstrap avec intervalle de confiance.

## (3) Confondants et zones mortes

**F8. Zone morte non traitée, ce qui viole B4.**
- Une issue dans $(0.48,\,0.60)$ ne falsifie rien. L'écart de 0.12 *est* la zone morte, contrairement à son intitulé.
- $[0.48,0.49)$ est compatible avec $H_A$ mais exclu de $\hat I_A$.
- Rien n'est prévu au-delà de 2.00.
- *Correctif :* fixer un seuil unique $\theta$ avant l'expérience, avec un test d'équivalence et une marge déclarée. Une issue non concluante doit être déclarée à l'avance comme falsifiant la puissance du dispositif.

**F9. $H_B$ est une disjonction et contient un mécanisme impossible.**
- En zone non sûre, le coefficient vaut 1 quel que soit $\gamma$. Une « fuite due à $\gamma$ fini » ne peut donc pas concerner les états non sûrs.
- *Correctif :* scinder en $H_{B1}$ (dynamique hors de $S_{\text{TD}}$) et $H_{B2}$ (fuite dans la zone sûre). Les départager par un balayage de $\gamma$ : monotonie si $H_{B2}$, plateau si $H_{B1}$.

**F10. Le bras « projection brute » manque.**
- L'hypothèse oppose l'opérateur continu à la projection brute, mais aucun bras ne mesure la projection brute.
- *Correctif :* comparer trois bras (sans intervention, projection brute, opérateur), avec le même budget d'énergie retirée.

**F11. Le contrôle $U_{\text{perm}}$ est mal construit.**
- Si `data['U']` reçoit $U_{\text{perm}}$, la mesure porte sur un autre sous-espace : les résultats ne sont pas comparables.
- Un sous-espace aléatoire de petit rang dans un espace de grande dimension retire très peu d'énergie. Le contrôle tombe donc trivialement dans $\hat I_B$.
- *Correctif :* intervenir avec $U_{\text{perm}}$ et mesurer avec $U$, à énergie retirée appariée. Ajouter un témoin construit à partir d'une sonde sans lien avec l'aversion.

**F12. Aucun garde-fou sur les capacités du modèle.**
- On peut faire baisser $O$ en dégradant le modèle.
- *Correctif :* ajouter un critère de non-régression, par exemple la divergence KL ou la perplexité sur des prompts neutres, avec une borne fixée à l'avance (illustrative).

**F13. Le vocabulaire surinterprète (Règle 5).**
- « Valide l'amortissement » et « prouve l'inefficacité » vont au-delà de ce que le test établit.
- *Correctif :* écrire « $H_A$ non falsifiée » et « $H_A$ falsifiée dans ce dispositif ».
- La présence de modes non-normaux reste une HYPOTHÈSE que `compute_O` ne teste pas. Il faudrait comparer les valeurs singulières et les valeurs propres du jacobien inter-couches.

{marqueur}
