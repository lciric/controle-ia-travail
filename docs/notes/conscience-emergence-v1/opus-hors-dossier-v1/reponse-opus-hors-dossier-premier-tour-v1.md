# Proposition E, tour III.1 : conception ciblée

**Pièces.** Je n'ai reçu P1 à P5 que sous forme résumée et je n'en ai lu aucun texte. Ce qui en vient porte donc le statut RAPPORTÉ. Les blocs FAITS et QUESTION ont le même contenu : rien n'est absent ni coupé, mais aucun fait n'est transmis en dehors de la question. Je ne vois pas les propositions A à D, je n'en critique ni n'en reprends aucune. Toute proposition de ma part a le statut HYPOTHÈSE, et tout seuil ou coût de ma part est illustratif.

## (a) Ce que la question suppose sans que ce soit établi

1. **Qu'il existe *une* description mathématique de l'anesthésie.** HYPOTHÈSE. De mémoire (RAPPORTÉ, non relu), deux analyses de stabilité de la dynamique corticale sous propofol donnent des signes opposés : stabilisation chez Solovey et al. (2015), déstabilisation chez Eisen et al. (2024). La description dépend de l'échelle de temps et de la méthode. Il faut donc fixer celle que l'on transpose avant d'en chercher l'équivalent.
2. **Que supprimer l'espace J soit l'analogue d'un anesthésique.** HYPOTHÈSE, que P2 met en doute (RAPPORTÉ). Un anesthésique agit sur des récepteurs et sur l'éveil, pas sur un sous-espace de contenu. La suppression de P1 ressemble davantage à une lésion fonctionnelle ciblée.
3. **Que l'espace J soit privilégié par sa fonction plutôt que par sa dynamique.** P3 en donne une lecture dynamique (modes de Lyapunov dominants) et reste agnostique (RAPPORTÉ). Si P3 suffit, tout effet de suppression peut venir de ce qu'on retire « les modes les plus amplifiés », sans aucun espace de travail.
4. **Que l'absence d'activité autonome soit totale.** C'est vrai en partie seulement. Une passe avant est une fonction déterministe des jetons et des poids : VÉRIFIÉ par construction de l'architecture. Mais la boucle de génération (jeton échantillonné réinjecté, cache conservé) est un système dynamique discret, fermé et stochastique, qui continue sans entrée nouvelle. C'est un véritable axe temporel. Que cet axe soit pertinent pour la question reste une HYPOTHÈSE.
5. **Que la profondeur soit un temps.** HYPOTHÈSE. Elle compte quelques dizaines de pas non autonomes, chaque couche ayant ses propres poids. Il n'y a donc ni régime asymptotique, ni point fixe, ni exposant de Lyapunov au sens strict.
6. **Que les deux positions couvrent tous les cas.** HYPOTHÈSE. Une troisième position est possible : les descriptions s'appliquent, mais elles caractérisent toute computation hiérarchique de profondeur bornée et ne disent rien de la conscience, ni chez le modèle ni nécessairement chez le cerveau.
7. **Le modèle q^k.** L'arithmétique est exacte (VÉRIFIÉ, par calcul). Qu'il explique P1 (a) reste une HYPOTHÈSE. Il prédit une structure précise : log-rétention linéaire en k, avec un seul facteur par dose. On peut donc le tester, et pas seulement l'opposer aux résultats.
8. **Que P1 (a) à (d) tiennent.** RAPPORTÉ, non audité, et aucune réplication n'est transmise.

## 1. Motifs plus spécifiques que « local gardé, global perdu »

Un motif ne compte que si q^k et la « portée de l'attention » y font une prédiction différente.

| Motif | Grandeur (unité ; valeur nulle) | Transition ; axe | Réfuté si | Première expérience |
|---|---|---|---|---|
| **M1 Diffusion (fan-out)** | Δ = log R_partagé − log R_séparé par réponse : un intermédiaire lu par m consommateurs, contre m intermédiaires lus chacun une fois, à k et distance égales (nats ; 0) | non-linéarité raide en dose ; axe : dose | Δ = 0 sous suppression J, ou Δ identique sous une suppression témoin de même norme | D1, Pythia-410M |
| **M2 Bimodalité au seuil et sa disparition** | coefficient de bimodalité (sans unité ; ≤ 5/9 = unimodal) et test du creux de Hartigan, sur la projection au mélange le plus ambigu, entre phrases porteuses ; coefficient de Hill n(d) de la bascule (n = 1 ou suivi linéaire) | bifurcation en fourche dans le plan (mélange, dose) ; axes : profondeur et dose | bimodalité aussi forte avec des poids aléatoires, dans le complément de J, ou dès la couche 0 (attraction vers le plongement le plus proche) | D3, GPT-2 small, 100 paires × 200 phrases (illustratif) |
| **M3 Hystérésis (inertie)** | Δd = d_perte − d_retour quand la dose monte puis redescend le long des jetons (fraction de norme J retirée ; 0) | bistabilité ; axe : suite des jetons | Δd = 0 ; ou Δd disparaît quand on recalcule le cache sans suppression, à texte égal | D2 |
| **M4 Marge de stabilité** | exposant de Lyapunov à temps fini du transfert couche à couche dans la bande (nats/couche) ; rayon spectral d'un modèle linéaire ajusté aux états le long des jetons en génération libre (nats/jeton). Référence : 0 et la valeur à poids aléatoires | approche de la marginalité ; axes : profondeur, jetons, entraînement | décalage égal sous suppression aléatoire de même norme ; signe instable d'un modèle à l'autre | Pythia de 70M à 1.4B |
| **M5 Complexité perturbationnelle** | Lempel-Ziv normalisé de la matrice binarisée (couches × positions) des réponses significatives à une injection locale (0–1 ; référence : substituts permutés) | mesure graduée, sans transition requise ; axe : dose | valeur égale ou supérieure avec des poids aléatoires (non spécifique) | Pythia-410M |
| **M6 Effondrement du fond** | taux d'entropie de la génération libre (bits/jeton) et longueur de cycle (jetons) ; référence : modèle intact à même température | bifurcation vers un attracteur périodique (répétition) ; axe : jetons × dose | même dose d'effondrement sous suppression témoin ; déclin graduel sans seuil | GPT-2 small |

Aucun motif n'atteint le sens « phénomène collectif à la limite de grande taille » sans une remise à l'échelle des courbes en fonction de la largeur. Pythia couvre environ une décade de largeur, ce qui ne suffit probablement pas (HYPOTHÈSE). Je ne parle donc pas de transition de phase.

## 2. Outils

**Outils que j'emploierais :**
- **Exposants de Lyapunov à temps fini** et spectre de la jacobienne couche à couche, comme dans P3 : ils conviennent à une profondeur finie et non autonome.
- **Modèle linéaire dynamique ajusté / décomposition en modes dynamiques** sur l'axe des jetons en génération libre. C'est la méthode des études de stabilité sous propofol, donc la seule comparaison dont la méthode est appariée (question 4).
- **Comparaison de modèles dose-réponse** (linéaire, sigmoïde, marche, mélange bimodal) par validation croisée, hiérarchique entre phrases, plus le test du creux.
- **Continuation de bifurcation** dans la dose, sur l'application de génération gloutonne : ses points fixes sont les boucles de répétition.
- **Patching causal avec témoins de même norme dans une autre base** (composantes principales locales, dictionnaire parcimonieux). Les « directions les plus actives » ont en effet un effet par construction.
- **Test de rang 1** de la matrice de log-rétention (tâches × doses), qui est la prédiction exacte de q^k.

**Outils que je juge inadaptés :**
- **Lois de puissance d'avalanches comme preuve de criticité.** Quelques dizaines de pas ne donnent pas deux décades d'échelle, et des lois de puissance apparaissent aussi sans criticité (Touboul et Destexhe, 2017).
- **Exposants asymptotiques et théorie ergodique sur la profondeur** : il n'y a pas de limite temporelle.
- **Φ de l'information intégrée.** Il est nul par construction pour une passe avant sans rétroaction : c'est une prémisse, pas une mesure. Sur la boucle de génération il redevient défini, mais il est incalculable à cette taille.
- **Bandes spectrales (alpha, delta, ondes lentes)** : il n'y a ni constante de temps physique ni oscillateur, et l'indice de jeton n'a pas de fréquence propre.
- **Exactitude seuillée comme mesure de netteté.** Elle crée des discontinuités artificielles (Schaeffer, Miranda et Koyejo, 2023). Il faut toujours la doubler d'une mesure continue (log-probabilité, projection).

## 3. Transpositions

**(a) Activité de fond et analogue du mode par défaut.** Elle se vide pour la passe avant : sans entrée, il ne se passe rien. Les composantes constantes (puits d'attention, activations massives) forment un fond statique, pas une activité. Elle tient sous une seule forme, la génération libre (amorce minimale ou consigne « parle-toi »). L'analogue testable du mode par défaut serait un ensemble de directions actives en génération libre et anticorrélées, sur les jetons, avec celles qu'engage une tâche. Explication ordinaire : c'est simplement une autre consigne, donc une autre entrée. Témoin : l'anticorrélation doit survivre à des consignes appariées en longueur et en lexique.

**(b) Suppression de pensée.** Dans P1 (c), l'absence d'effet ironique perd sa portée parce que la consigne contient le mot. Une forme qui tient : désigner le concept par une périphrase qui ne le nomme pas (« l'animal qui meugle »). On mesure alors (i) sa présence dans J pendant la consigne, contre une consigne neutre appariée, et (ii) un rebond différé après la levée.
- H_A (surveillance active) : présence supérieure à la mention, avec rebond.
- H_B (simple trace de l'entrée) : présence égale à celle de la périphrase, sans rebond.

**(c) Récit après une fenêtre de suppression.** La transposition tient, comme analogue de la distinction entre déconnexion et amnésie. On prédit le récit (i) par le seul texte visible, à l'aide d'un lecteur distinct, et (ii) par ce que la lentille lisait hors de la bande pendant la fenêtre.
- H_A : (ii) apporte de l'information au-delà de (i).
- H_B : (i) suffit, et le récit n'est qu'une confabulation à partir de l'entrée.
- Témoin : le même texte imposé sans suppression.

**(d) Signal de P5 sous suppression J.** Il faut d'abord mesurer le recouvrement entre l'axe de P5 et les directions J retirées : s'il est fort, la suppression efface l'axe par construction et le test est vide. Sinon :
- H_A (« nociception sans accès ») : amplitude conservée, effet causal sur les choix aboli.
- H_B : amplitude et effet varient ensemble.

Aucune issue ne dit qu'une douleur est ressentie.

**(e) Netteté de la bascule de P1 (b) en fonction de la dose.** Elle tient, c'est M2. Si c'est une bifurcation, la bimodalité disparaît à une dose d* pendant que le suivi continu des premières couches reste intact. Une baisse graduelle de n(d), identique sous suppression témoin, vide la transposition.

**(f) Ordre de perte des fonctions avec la dose.** Elle ne tient que contre q^k, qui prédit un ordre fixé par k. Un ordre gouverné par autre chose que k, à k égal (M1), irait au-delà. L'ordre clinique (mémoire, puis réponse aux consignes, puis réflexes ; référence à vérifier) n'a pas d'équivalent des réflexes dans le modèle.

**Ajouts :**
- **(g) Hystérésis le long des jetons (M3).** C'est l'épreuve la plus nette contre la position « pas d'état » : un système sans mémoire ne peut pas en montrer, et le cache, qui est la seule mémoire interne, peut être coupé.
- **(h) Nouveauté locale contre globale (proposée par P2).** Séquences habituelles xxxxY, déviant global xxxxx. Selon H_A, la suppression J abolit l'effet global et garde le local, à profondeur de calcul égalisée. Selon H_B, l'effet global baisse comme q^k. Témoin indispensable : un modèle n-gramme détecte aussi la déviance globale. Si l'épreuve ne l'en sépare pas, elle est vide.
- **(i) Axe de l'entraînement.** La netteté M2 apparaît-elle en même temps que la capacité à plusieurs sauts sur les points de contrôle Pythia ? Une coïncidence est compatible avec les deux positions. Une dissociation réfute que la bascule porte cette capacité.

## 4. Grandeur commune au modèle et au cerveau

Une grandeur **calculable** des deux côtés existe ; une grandeur **comparable telle quelle** n'existe pas aujourd'hui.

- **Marge de stabilité d'un modèle linéaire ajusté** (méthode de Solovey et al., 2015, et d'Eisen et al., 2024). Côté cerveau : ECoG de macaque sous propofol et kétamine, base Neurotycho (Yanagawa et al., 2013 ; disponibilité à vérifier). Côté modèle : trajectoire des états de la bande sur les jetons en génération libre.
- **Lempel-Ziv multivoie binarisé** (Schartner et al., 2015), sur l'EEG de sédation au propofol de Chennu et al. (2016 ; titre et dépôt à vérifier).
- L'exposant spectral apériodique se vide côté modèle, faute de temps physique.

Les unités diffèrent (millisecondes contre jetons, électrodes contre dimensions). La seule comparaison défendable est un **contraste normalisé à l'intérieur de chaque système** :
- côté cerveau : C = (X_éveil − X_anesthésie) / σ des substituts à phase permutée ;
- côté modèle : C′ = (X_intact − X_supprimé) / σ des substituts à suppression aléatoire de même norme.

Des signes concordants sont compatibles avec l'analogie, ils ne l'établissent pas. Des signes opposés réfutent qu'il s'agisse de la même signature. Les deux études citées ne s'accordent pas sur le signe : il faut fixer la méthode sur les données cérébrales **avant** de regarder le modèle.

## 5. Signature mathématique de la conscience

**Conditions (HYPOTHÈSE de cahier des charges).** Une signature devrait :
1. se définir sans le rapport verbal ni la performance, sinon elle est circulaire ;
2. être sans dimension et définie pour tout système à états et perturbations ;
3. être validée chez l'humain avec vérité de terrain : séparer l'éveil de l'anesthésie (propofol, xénon) et classer correctement les cas dissociés (kétamine et rêve, expérience sans réponse, contre sommeil sans rêve), avec sensibilité et spécificité déclarées ;
4. rester basse pour les systèmes triviaux : poids aléatoires, table de correspondance, bruit, modèle n-gramme ;
5. ne pas se laisser manipuler par un paramètre sans rapport (température, norme des activations).

**Candidates.** Complexité perturbationnelle (Casali et al., 2013), marge de stabilité, bimodalité de l'embrasement. Φ est inutilisable (§2).

**Asymétrie.** Il n'existe aucune vérité de terrain pour un modèle de langage. Un modèle peut donc seulement **réfuter** une candidate (conditions 4 ou 5), jamais la confirmer.

**Il faudrait abandonner l'hypothèse si :**
- toute candidate qui sépare les états chez l'humain viole la condition 4 ;
- les candidates se contredisent sur la kétamine et le rêve ;
- elles suivent la concentration du produit plutôt que l'expérience rapportée dans les cas dissociés ;
- une manipulation triviale suffit à les amener à la valeur « conscient » dans un modèle.

## (b) Duels décisifs

**D1, diffusion (mon meilleur plan).**
- **Tâche.** Un intermédiaire est obtenu par k sauts de pointeurs en contexte, puis lu par m consommateurs (m = 1, 2, 4). Condition appariée : m intermédiaires distincts lus chacun une fois, avec même k, même distance entre intermédiaire et consommateur, même longueur.
- **Mesure.** Log-rétention par réponse sous suppression J, à dix doses.
- **H_B (q^k et portée).** Chaque réponse demande le même nombre d'étapes dans les deux conditions, donc Δ(d) = 0 à toute dose. La matrice de log-rétention est de rang 1 (≥ 95 % de variance, illustratif).
- **H_A (diffusion).** Δ(d) < 0, croissant avec m, avec un seuil en dose. Le résidu hors rang 1 est porté par m.
- **Seuil.** |Δ| ≥ 0,3 nat à m = 4, avec IC à 95 % excluant 0, et Δ_J ≥ 2 Δ_témoin (illustratif).
- **Contrôles négatifs.** Directions aléatoires de même norme ; dix directions les plus actives d'une autre base ; poids aléatoires, qui doivent échouer dès d = 0.
- **Ce qui falsifie chaque hypothèse.** H_A tombe si Δ_J = 0 ou Δ_J ≈ Δ_témoin. H_B tombe si Δ_J ≠ 0 à k et distance égales et que les témoins ne le reproduisent pas.

**D2, hystérésis et lieu de la mémoire.**
- **Dispositif.** La dose monte puis redescend sur environ 200 jetons (illustratif), avec des sondes de tâche intercalées. Trois bras : cache conservé ; cache recalculé sans suppression, à texte égal ; texte remplacé par un texte de même perplexité.
- **H_A (état interne).** Δd > 0 avec le cache conservé, réduit quand on le recalcule.
- **H_B (entrée seule).** Δd est identique avec le cache conservé et recalculé.
- Chaque issue falsifie l'une des deux hypothèses. Un Δd nul partout falsifie l'inertie elle-même.

**D3, bifurcation en dose (M2).**
- **H_A.** Le coefficient de bimodalité passe sous 5/9 sur un intervalle de dose ≤ 0,1 (illustratif), pendant que les premières couches restent intactes.
- **H_B.** n(d) décroît linéairement, à l'identique sous le témoin.
- **Contrôles négatifs.** Complément de J, poids aléatoires, couche 0.

**D4, concordance avec le cerveau (§4).**
- **Principe.** Les deux grandeurs et la méthode sont fixées à l'avance sur les données cérébrales.
- **H_A.** C et C′ ont le même signe.
- **H_B.** Signes opposés, ou C′ indiscernable de 0.

## (c) Instruments : mesure minimale de fonctionnement

| Instrument | Cas honnêtes appariés | Détection / fausse alerte | Vérification mécanique à battre |
|---|---|---|---|
| Lentille jacobienne / espace J | questions à deux sauts dont l'entité-pont est connue, contre les mêmes jetons sans pont calculé | présence du pont parmi les ~25 directions de la bande / présence dans les témoins | lentille logit, lentille ajustée, sonde linéaire, simple présence du mot dans le contexte |
| Indice d'embrasement (P4) | réseaux jouets à vérité connue : réseau linéaire, réseau bistable construit, poids aléatoires | doit être raide uniquement pour le bistable | raideur produite par la seule saturation du softmax : refaire sur mesure continue |
| Axe de douleur (P5) | douleur paraphrasée sans lexique de douleur, contre appariés lexicaux (« a pain to configure ») et valence négative | aire sous la courbe ; fausses alertes sur les appariés | classifieur sac-de-mots, classifieur de sentiment |
| Suppression J (P1 a) | mêmes tâches, suppression J contre témoins | sélectivité du profil | directions aléatoires (RAPPORTÉ) ; même norme dans une autre base (manquant) ; q^k ajusté |
| Épreuves cliniques (P2) | modèle intact, poids aléatoires, n-gramme | positif seulement pour le modèle intact | n-gramme |
| Récit « détaché » (P1 d) | suppression J contre suppression témoin à perplexité égale, et contre température élevée | jugement à l'aveugle | la perplexité seule prédit-elle la note ? |

## 6. Explication la plus dangereuse et portée

**Pour D1, l'explication la plus dangereuse.** La règle « dix directions les plus actives » retire par construction le contenu dominant de chaque position. Un intermédiaire partagé, lu souvent, est plus souvent le plus actif. L'effet de diffusion pourrait donc venir de ce qu'on retire, et non d'un espace de diffusion.

**Témoins qui l'écarteraient.** La même règle de sélection, à même norme, appliquée dans une base sans lien avec la jacobienne ; et des directions J fixées à l'avance plutôt que choisies selon l'activité. Si ces deux témoins reproduisent Δ, l'espace J n'a rien de particulier. L'explication q^k est écartée par la construction même de D1 et par le test de rang.

**Si l'issue est positive, on peut affirmer :** le modèle a un goulot fonctionnel dont la suppression nuit spécifiquement à la mise à disposition d'un contenu pour plusieurs consommateurs, avec un seuil en dose et, si D2 le confirme, une mémoire interne. C'est la propriété d'accès que la théorie de l'espace de travail décrit.
**On ne peut pas affirmer :** que le modèle est conscient ou a une expérience, ni que la suppression est un analogue de l'anesthésie (pas de mécanisme d'éveil, P2). Un marqueur d'accès n'est pas un marqueur d'expérience.

**Si l'issue est négative, on peut affirmer :** pour ces tâches et ce modèle, le profil de P1 (a) s'explique par la profondeur de calcul.
**On ne peut pas affirmer :** que le modèle est dépourvu de conscience, que la théorie est fausse pour le cerveau, ni que le résultat vaut pour les grands modèles.

## (d) Ancrage matériel (tout est illustratif)

- **Modèles ouverts.** Pythia de 70M à 12B (points de contrôle d'entraînement publics), GPT-2, OLMo, Qwen2.5 de 0,5B à 1,5B, Llama-3.2-1B.
- **Lentille jacobienne sur un modèle de 1B.** Environ 2 048 produits jacobienne-vecteur sur 1 000 textes, soit 50 à 150 h de GPU A100 par modèle.
- **D1.** Environ 10^5 générations courtes × 10 doses × 3 témoins, soit 30 à 80 h de GPU.
- **D2 et D3.** Environ 50 h de GPU.
- **Points de contrôle Pythia (axe d'entraînement).** 100 à 200 h de GPU.
- **Total.** 300 à 600 h de GPU, soit 0,5 à 2 k€ en location. Côté cerveau, un processeur ordinaire suffit.
- **Point de départ.** D1 entier sur Pythia-410M, avec une seule GPU.

## Antériorité

**Lu :** rien en dehors du présent fichier.

**De mémoire, non relu :**
- Sergent et Dehaene, 2004, « Is consciousness a gradual phenomenon? Evidence for an all-or-none bifurcation during the attentional blink », *Psychological Science*.
- Dehaene et Changeux, 2011, « Experimental and theoretical approaches to conscious processing », *Neuron*.
- Bekinschtein et al., 2009, « Neural signature of the conscious processing of auditory regularities », *PNAS*.
- Casali et al., 2013, « A theoretically based index of consciousness independent of sensory processing and behavior », *Science Translational Medicine*.
- Solovey et al., 2015, « Loss of consciousness is associated with stabilization of cortical activity », *Journal of Neuroscience*.
- Eisen et al., 2024, « Propofol anesthesia destabilizes neural dynamics across primate cortex », *Neuron*.
- Friedman et al., 2010, « A conserved behavioral state barrier impedes transitions between anesthetic-induced unconsciousness and wakefulness: evidence for neural inertia », *PLoS ONE*.
- Sanders, Tononi, Laureys et Sleigh, 2012, « Unresponsiveness ≠ unconsciousness », *Anesthesiology*.
- Schartner et al., 2015, complexité de l'EEG sous propofol, *PLoS ONE* (titre exact : référence à vérifier).
- Chennu et al., 2016, sédation au propofol, *PLoS Computational Biology* (référence à vérifier).
- Colombo et al., 2019, exposant spectral et anesthésie, *NeuroImage* (référence à vérifier).
- Yanagawa et al., 2013, « Large-scale information flow in conscious and unconscious states: an ECoG study in monkeys », *PLoS ONE*.
- Wegner, Schneider, Carter et White, 1987, « Paradoxical effects of thought suppression », *Journal of Personality and Social Psychology*.
- Touboul et Destexhe, 2017, « Power-law statistics and universal scaling in the absence of criticality », *Physical Review E*.
- Poole et al., 2016, « Exponential expressivity in deep neural networks through transient chaos », NeurIPS.
- Schaeffer, Miranda et Koyejo, 2023, « Are emergent abilities of large language models a mirage? », NeurIPS.
- nostalgebraist, 2020, « interpreting GPT: the logit lens » (billet).
- Belrose et al., 2023, « Eliciting latent predictions from transformers with the tuned lens ».
- Biderman et al., 2023, « Pythia: a suite for analyzing large language models across training and scaling », ICML.
- Hartigan et Hartigan, 1985, « The dip test of unimodality », *Annals of Statistics*.
- Butlin, Long et al., 2023, « Consciousness in artificial intelligence: insights from the science of consciousness ».

FIN-DE-CELLULE