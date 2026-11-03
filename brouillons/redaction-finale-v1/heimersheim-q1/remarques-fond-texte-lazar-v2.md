# Heimersheim Q1 — remarques de fond sur ton texte — v2 (après le vérificateur)

Conv-audit, 3 novembre 2026, vers 20:55 UTC (`date -u`). Ton texte : `reponse-lazar-v1.md` (`d842e467…`). Remplace la v1 de ces remarques ; fusionne mes remarques et le rapport du vérificateur neuf (`verification-texte-lazar-v1.md`, 20:41 → 20:50 UTC).

**Règle du mentor** : texte 100 % humain. Aucune phrase anglaise ici ; je ne cite que tes mots pour situer. Les corrections sont à écrire par toi.

**Verdict** : les chiffres sont presque tous exacts. Il reste des erreurs de sens, dont plusieurs sur les papiers que Heimersheim connaît le mieux (Hua et coll., et le sien).

## Graves : le sens est faux

1. **l. 16, annexe B de Hua et coll.** « couldn't confirm on their smaller model » est faux deux fois. Le modèle de l'annexe est **plus simple** (affiné sur documents synthétiques seuls), pas plus petit. Et les auteurs disent qu'ils **ne peuvent pas exclure** que le pilotage y revienne à dire au modèle qu'il est déployé : c'est l'inverse de « n'ont pas pu confirmer », et ça **sert ta thèse**.
2. **l. 7, ce que pilotent Hua et coll.** Ils pilotent la conscience d'évaluation vers le déploiement ; les indices de type sont ce qu'ils **lisent**. Et Wood Labs n'annonce pas le test : le modèle le **déduit** (ta l. 25 le dit bien, donc la l. 7 la contredit).
3. **l. 17, tableau 16.** 0,34 à 0,60 sont des **taux d'indices de type atteints**, pas des baisses. « Just not as much » n'a pas d'objet : le tableau ne donne aucun chiffre de pilotage. Les auteurs écrivent même que ces phrases ramènent le taux **à un niveau comparable au déploiement**, et que cela affaiblit leur montage.
4. **l. 43, réplication manquée.** « It took both to activate against sycophancy » fait croire à une vraie baisse : les deux causes réunies produisaient une **baisse apparente**, et le README conclut que le sous-espace ne code pas la déférence. La phrase suivante inverse la causalité : la troncature à 300 caractères n'est pas un résultat expliqué, c'est la seconde cause. (« wasn't backing down » : juste.)
5. **l. 47 et 53, D36.**
   - Le critère (c) vient du **dossier de porte du 5 août**, pas du préenregistrement du 29 juillet, qui n'avait **aucun bras « autre item »** ; le bras à 2 % a été ajouté après coup. Dis-le, ou ne dis pas « preregistered » pour ce critère.
   - « Not that of the specific item » va plus loin que le README (« en grande partie ») : 65 % contre 44 %, le contenu de l'item porte une part.
6. **Papier de Ferreira da Silva et Heimersheim (2606.24964)** — c'est le sien, il le verra :
   - l. 71 : p > 2 « pour toutes les directions » : le papier donne des **moyennes et des médianes**, pas un résultat direction par direction.
   - l. 73 : « They didn't provide a value for Llama » : la valeur de Llama est **dans la figure 6** (le texte seul n'en donne pas).
   - l. 73 : « only … layer 2 » : la couche 2 est le **réglage par défaut** ; les ablations perturbent aussi aux couches 5, 10 et 20.
   - l. 73 : la fourchette 2,24 à 2,63 couvre **tous les réglages des ablations** (couches, métriques, seuils, autres modèles), pas seulement les autres modèles.
   - l. 83 : « 70 times more » : écart de **sensibilité** d'au plus 70 entre la direction la moins et la plus réactive (note 1), pas une dose à multiplier par 70.

## Moyens

7. **l. 59, Devbunova** : elle n'emploie **ni paraphrases vérifiées ni perturbations** : quatre cases tirées de jeux de données différents, une seule réécrite par un modèle de langue (DeepSeek-V3), sans vérification d'équivalence décrite. Retire la comparaison ou dis ce qu'elle fait vraiment.
8. **l. 19, (d)** : « There is no attempt » est trop large : le plan 2 × 2 de Devbunova existe. Limite la phrase à Hua et coll.
9. **l. 27, R7** :
   - « The 72B was activated » : R7 n'a **aucune intervention sur les activations**, seulement des notes plantées dans le texte lu ; le 72 milliards est **déplacé**, pas capturé.
   - −0,19 [−0,24 ; −0,11] est la pente du **gain de déférence g**, sous note négative, **à l'intensité standard**, pas « the increase ».
   - « control 1.5B, 3B and 32B » : exact, mais sous la note négative **forte**, et c'est une lecture **descriptive, non préenregistrée**.
10. **l. 109, Institut britannique** : la provenance des quatre vecteurs (fiche système d'Opus 4.6, § 6.5.2) est **exacte** ; mais deux vecteurs n'élèvent pas le désalignement **au-dessus de la base**, ce qui n'est pas « didn't do anything ». « log of the 2 thresholds » : logarithme du **rapport** des deux seuils.
11. **l. 39, trois têtes** : le README dit « **inchangé** » (58,5 → 57,5 %, p = 0,91), pas une baisse.
12. **l. 87 et 89, R6** : sous critique, pas de changement **détectable** (l'intervalle contient 0) ; sous éloge, le gain passe **de** 0,28 **à** 0,80 (« increased by » se lit comme un écart).
13. **l. 91, R6** : chiffres exacts ; sans les 14 items à refus, c'est une analyse **a posteriori, descriptive**.
14. **l. 95, R9-bis** : la direction neutre vient d'une **autre phrase de même registre et de même longueur**, pas de « la même phrase ».
15. **l. 9 et 99** : contradiction interne : « not at the same norm » contre « On the same norm ».

## Légers

16. Le verbe « activate » partout (titre, thèse, § 2 à 7, « activating after layer 1 » chez Janiak, qui est une **perturbation**) : le terme du champ et de la question (c) est le pilotage.
17. l. 57 : « Ferreara » → Ferreira.
18. Section 6 : les cases [X], [Y], [Z] sont vides ; à remplir (seuils et signes, fixés par toi) avant l'envoi.
19. « ICLR 2026 » : non vérifié (OpenReview bloqué) ; garde-le seulement si tu l'as vu.

## Vérifié exact
Chiffres de la version 5 (80, 33, 10 % ; 56,8 → 55,2 % ; 24 vecteurs gaussiens ; 16 paires) ; les mots des deux phrases d'invite (seule la casse diffère : « You », « AI ») ; Devbunova, Singh et Chaudhary, Llama-3.1-8B-Instruct ; 2608.13329 (cosinus 0,9995 entre deux moitiés d'une même invite, 0,3749 entre invites différentes) ; invites FineWeb de 5 jetons, dernier jeton, distance L2 à l'avant-dernière couche ; tous les chiffres de R6, R7, du rang 3 et de D36, et les DOI ; R9 et R9-bis ; 210 paires sur 528 ; p = 2,05 [2,00 ; 2,10] ; les oracles d'activation.
