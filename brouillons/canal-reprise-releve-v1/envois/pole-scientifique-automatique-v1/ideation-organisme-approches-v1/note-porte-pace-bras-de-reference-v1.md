# Porte PACE, bras de référence du juge figé — note v1

29 octobre 2026. Sous-agent de la lignée conv-audit. Exploratoire, non préenregistré ; processeur seul, aucune dépense. Suite de la décision de Lazar (29 octobre, 01:15 heure de Paris) : « porte PACE comme bras de référence du juge figé ». **Bras de référence ; jamais une sélection d'agent (N-053).** Seule source sur PACE : `../corpus-primaire-v4/extrait-2606.08106-v1.md` (pages du PDF entre crochets) ; lecture d'appui : `../corpus-primaire-v4/lecture-PACE-contre-Q2-v1.md`.

Fichiers neufs (orchestrateur v7, prise v38, aucun fichier existant modifié) : `pole/porte_pace.py`, `essais/test_v7_porte_pace.py`, `demonstrations/porte_pace_v1.py`.

## 1. Ce qui est repris de PACE

- **Appariement** : référence et candidat notés sur les mêmes instances ; w = 1 si seul le candidat a juste, w = 0 si seule la référence a juste, égalités écartées (paires de McNemar) [p.4].
- **Règle de pari** : E₀ = 1, E ← E·(1 + λ(2w − 1)), λ ∈ [0 ; 1) (équation (2)) ; λ = 0,5 et α = 0,05 par défaut [p.4].
- **Seuil et arrêt** : validation dès que E ≥ 1/α ; évaluation incrémentale, arrêt au premier franchissement ; rejet si le budget s'épuise [p.4]. Garantie par candidat (Ville), « not a run-level familywise bound » [p.5 ; p.9, tableau 3].
- **Témoin planté à gain connu**, contrôle positif, « a unit test for acceptors » [p.6].
- **Jeu d'audit neuf**, jamais lu par la règle : fausse validation si l'écart audité est ≤ 0, nuisible s'il est < 0 [p.6].
- **Acceptation gloutonne** comme référence : « keep it if the score went up » [p.1] ; « reused dev score ticks up » [p.2, figure 1].

**Réduction à nos briques.** Avec v = (candidat juste) − (référence juste), le facteur de PACE vaut 1 + λ·v ; une égalité donne v = 0, donc un facteur 1 (« écartée » revient à multiplier par 1). La porte est exactement `pari_apparie.trajectoire_log_richesse(v, lambdas=(λ,))` lue contre log(1/α). Un essai le vérifie contre le produit écrit à la main. Seul écart de domaine : PACE admet λ = 0, que la brique refuse ; il est traité à part.

## 2. Ce qui est inféré (marqué [INFÉRÉ] dans le module)

- **Taille de lot** : « a fixed batch size unless noted » [p.4], valeur absente (algorithme 1 coupé, p.5) ; défaut 10. Le franchissement est testé après chaque paire [p.4] ; le lot ne compte que dans le coût.
- **Budget** = tout le jeu de développement fourni (n = 40 dans PACE [p.6]).
- **Glouton strict** : équation (1) coupée [p.4] ; « went up », « ticks up » [p.1-2] lus comme une hausse stricte.
- **Référence fixe** : dans PACE le candidat validé devient le titulaire [p.3] ; ici aucun candidat ne devient la référence, parce que N-053 interdit toute sélection. C'est un écart volontaire à la boucle de PACE.
- **Monde simulé** : exactitudes de Bernoulli, aléa d'instance partagé avec probabilité ρ = 0,5, référence à 0,35, jeu de développement réutilisé pour toute la suite [p.6, « small reused dev »], nul exact (même exactitude) à la place du régime stochastique de PACE.
- **Correction de la consigne** : la consigne parlait d'un candidat comparé à la référence « sur un jeu d'audit neuf ». Dans l'extrait, la porte lit le jeu de **développement** réutilisé, et l'audit sert **seulement** à étiqueter [p.6]. Le module suit l'extrait.

## 3. En quoi notre pari apparié diffère

Notre bras lit les mêmes contrastes v. Quatre différences :

1. **Borne de boucle** : e-processus arrêté à m/α, puis lecture **e-BH** sur la suite (budgets α/m, `ebh_pondere`). Sous le nul global, la probabilité d'au moins une fausse promotion dans la suite est ≤ α. PACE ne borne que chaque candidat [p.5]. Dans le pôle, cette borne passe par la `Course` (dépense α_g par génération, héritage, journal) ; le bras de comparaison n'utilise qu'une famille unique de taille m déclarée avant lecture (simplification dite).
2. **Garde δ** : un second processus contre « E[g] ≥ δ » (excès de faux positifs du candidat), qui entre dans le minimum. PACE n'en a pas.
3. **Parts bornées et mélange** : v est un contraste de parts dans [−1 ; 1] (règle double), pas seulement une issue juste ou faux, et la mise est un mélange sur Λ = {0,1 ; 0,3 ; 0,6 ; 0,9}, au lieu d'un λ fixe.
4. **Témoins plantés des deux signes** : nos témoins vrais à plusieurs forces, nos « faux nul exact » et « signe inversé » sont injectés dans la course. PACE n'a qu'un contrôle positif [p.6] et un régime nul global [p.6-7].

## 4. Ce que le bras de référence mesure : ce que nos ajouts achètent et ce qu'ils coûtent

Démonstration (`python3 -B demonstrations/porte_pace_v1.py`, graine 20261029, `numpy.random.SeedSequence`, 200 suites de 20 candidats par ligne, audit de 120 instances, 11 secondes) :

| régime | n_dev | bras | fausses par suite | suites avec ≥ 1 fausse | témoin validé |
|---|---|---|---|---|---|
| nulle | 40 | PACE | 0,110 | 8,5 % | — |
| nulle | 40 | pari apparié | 0,000 | 0,0 % | — |
| nulle | 40 | glouton | 8,905 | 99,0 % | — |
| gain | 40 | PACE | 0,025 | 2,0 % | 90 % |
| gain | 40 | pari apparié | 0,000 | 0,0 % | 50 % |
| gain | 40 | glouton | 4,220 | 89,0 % | 100 % |
| nulle | 120 | PACE | 0,570 | 32,0 % | — |
| nulle | 120 | pari apparié | 0,005 | 0,5 % | — |
| gain | 120 | PACE | 0,160 | 14,0 % | 100 % |
| gain | 120 | pari apparié | 0,010 | 1,0 % | 100 % |
| tricheur | 120 | PACE | 0,085 | 7,0 % | 100 % |
| tricheur | 120 | pari apparié | 0,000 | 0,0 % | 0 % |

Lecture, sur un jouet :

- **La borne de boucle achète le taux de famille.** Avec 20 candidats nuls sur 120 instances, PACE valide en moyenne 0,57 candidat faux par suite. C'est environ 2,9 % par candidat, sous α comme promis, mais 32 % des suites contiennent au moins une fausse validation. Notre bras reste à 0,5 % des suites.
- **Elle se paie en puissance sur petit jeu.** À 40 instances, le témoin planté (+0,35) passe la porte de PACE dans 90 % des suites, et notre bras dans 50 % seulement (seuil m/α = 400 au lieu de 20, mélange sur Λ). À 120 instances, les deux le valident toujours.
- **La garde achète le refus du tricheur.** Un candidat qui gagne en exactitude mais tire des faux positifs (excès 0,15 > δ = 0,05) est validé par PACE et par le glouton, jamais par notre bras. Le simulateur le compte comme « vrai » (gain réel positif) : c'est précisément l'angle mort que la garde couvre.
- **Le glouton** reproduit la pathologie décrite par PACE : 85 à 100 % des suites contiennent une fausse validation.

Essais (`essais/test_v7_porte_pace.py`, 18 essais, graines par `numpy.random.SeedSequence` passées à `random.Random`) :

- sous la nulle, la porte valide à 0,045 sur 2 000 répétitions (n = 200 ; α = 0,05) ;
- validité à tout instant : taux 0 ; 0,003 ; 0,0215 ; 0,039 ; 0,045 pour des budgets de 10, 25, 50, 100 et 200, croissants et tous ≤ α. Un test z regardé à chaque instance monte à 0,322 ;
- le glouton monte à 0,448 sous la nulle (n = 40) ;
- sous un gain planté (0,35 → 0,70, n = 40), la porte valide à 0,93 ;
- famille nulle à 10 candidats, développement tiré à neuf : PACE valide 0,032 par candidat et touche 27 % des suites ; notre bras touche 0,7 % des suites ;
- artefacts R5 : NaN, issue hors de {0 ; 1}, longueurs différentes, α hors de ]0 ; 1[, mise hors de [0 ; 1), jeu d'audit vide, budget hors bornes, noms en double. Chacun lève une erreur nommée.

## 5. Ce que le bras ne mesure pas

- Ni un juge-modèle, ni un adversaire, ni une boucle qui s'adapte au jeu. Les candidats sont tirés indépendamment des issues ; la réutilisation adaptative, que PACE laisse « empirical » [p.5], n'est pas simulée.
- Ni la boucle de PACE à titulaire mobile (écart volontaire, N-053).
- Ni la `Course` du pôle : générations, dépense α_g, héritage, journal, fraîcheur. Le bras compare des règles sur une famille unique.
- Ni nos données : tout est synthétique, et aucun chiffre ici n'est opposable à PACE (R7). Les chiffres de PACE ne sont pas reproduits.
- Ni la puissance sur nos effets réels, qui dépend de la banque.

## 6. Réserves

- La porte sous la nulle à 0,045 laisse une marge mince sous α. L'essai est à graine fixe, donc déterministe ; il faut s'attendre à des dépassements de α avec d'autres graines, car le test est sur la fréquence.
- **Constat sur le code existant, non corrigé (R12)** : `pari_apparie.trajectoire_log_garde` borne δ − g par min et max ; un écart g = NaN devient +1, la valeur la plus favorable à la promotion (vérifié : la trajectoire monte). `porte_pace` refuse le NaN en amont ; la correction de `pari_apparie` est à proposer.
- La lecture e-BH de notre bras repose sur des e-valeurs arrêtées sur un même jeu de développement réutilisé. e-BH reste valide sous dépendance arbitraire, mais le nul par candidat n'est exact que si le développement est tiré à neuf (option `dev_reutilise=False`, utilisée par l'essai de famille).

## Commandes

```
cd orchestrateur-pole-v7
python3 -B -m unittest essais.test_v7_porte_pace
python3 -B -m unittest discover -s essais -t . -p 'test_*.py' 2>&1 | tail -3   # 339 essais, OK
python3 -B demonstrations/porte_pace_v1.py --graine 20261029 --repetitions 200
```
