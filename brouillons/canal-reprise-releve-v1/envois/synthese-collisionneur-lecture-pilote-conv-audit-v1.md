# Synthèse du collisionneur « lecture du pilote, hypothèses, décisif » (trois tours) — conv-audit, v1

Écrite le 26 octobre 2026 à partir de 00:40 UTC (heure lue sur `date -u`), pour Lazar, sur les neuf réponses de la
branche `donnees/collisionneur-lecture-pilote-v1` (`7ac475b`, `EMPREINTES-v1.txt` ; neuf cellules valides, empreintes
vérifiées une à une ; 7,37 USD selon le `LISEZMOI-v1.md` de session-depot). Question : `cdcbd1bb…` (conv-audit, n° 68).
Je n'ai lu que les cellules (`cellules/*.md`), ni les essais ni les journaux. Rien ici n'est opposable (R7) ; les
références citées par les modèles sont à vérifier ; les chiffres sont ceux des modèles, refaits par moi quand je le dis.

## Ce sur quoi les trois modèles convergent après l'équipe rouge et la riposte

1. **Le pilote 4 apprend peu à (b)** : une course par objet ≈ 1 bit par famille ; signe juste ≈ 0,64 à 0,84 selon
   l'effet vrai (Opus, riposte, raisonnement explicite) ; conditionner la direction de (b) sur ce bit fait plus de mal que
   de bien (Fable retire sa proposition de menu d'hypothèses pour cette raison).
2. **La direction est donnée par la question** (Lazar, 00:49) : H_A « la v6.2.1 bat la v5.3 d'au moins δ » contre
   H_B « Δ ≤ 0 » ; δ fixé par l'enjeu, sans score.
3. **À 3 graines par objet** : test exact 3 contre 3, p minimal 1/20 = 0,05 unilatéral, 2/20 = 0,10 bilatéral (refait) ;
   intervalle à 90 % large d'environ 0,2 ; équivalence non concluable sauf δ ≥ 0,2 et écart observé presque nul.
4. **Règle de lecture** : chaque issue doit falsifier quelque chose — point de coupure c = δ/2 (Fable) ou table de lecture
   à quatre cases avec une règle de dessin « largeur planifiée < δ, sinon (b) est déclaré non décisif avant toute course »
   (Opus).
5. **Aucun dispositif à zéro bit** : faits mécaniques (coûts, durées, plantages, types d'erreur) corrélés à l'issue ;
   réserve déclarée sans pouvoir de détection ; une empreinte prouve l'ordre, pas l'ignorance ; une enveloppe à faible
   entropie s'inverse par énumération si elle n'est pas salée ; engagements multiples possibles sans registre unique.
6. **Le contraste v6.2.1 contre v5.3** ne sépare pas la réécriture de la règle de récompense des autres différences de
   code : pour l'isoler, une v6.2.1 « placebo » (mêmes appels de réécriture, sortie jetée par le noyau) ; sinon la
   conclusion porte sur « v6.2.1 contre v5.3 telle que livrée ».
7. **Contrôles demandés** : étalon de dérive des modèles appelés (organisme gelé, consigne fixe, ≈ 20 tâches, avant la
   première course et après la dernière) ; ordre des courses tiré au sort et entrelacé ; règle scellée pour une course
   plantée (aucune relance libre ; graine de remplacement fixée d'avance) ; marqueurs uniques dans `test_final` ; marqueur
   factice pour vérifier qu'aucun flux vu du lanceur ne porte de score ; `test` reçu par l'organisme, donc seule
   `test_final` est propre, et l'écart `test` − `test_final` est confondu par la sélection sur le bruit (placebo de
   rétroaction nécessaire pour l'interpréter).

## L'idée nouvelle

**Verser les deux courses du pilote 4 comme graines de (b)** (Argon ; reprise sous conditions par Fable) : 4 graines par
objet au prix de 3, écart minimal ≈ 20 % plus petit (Fable refait le rapport : 0,80). Conditions : (b) scellé avant toute
lecture du pilote 4 ; règle d'inclusion mécanique scellée (empreintes du code identiques, courses arrivées à la
génération 4 sans erreur fatale, pas de dérive des modèles appelés) ; renoncer explicitement à lire le pilote 4 pour
écrire les hypothèses.

## Désaccords laissés ouverts

- Hypothèse à un sens (charge sur la v6.2.1 ; Argon, Fable) ou symétrique, supériorité et équivalence (Opus) : selon ce
  que Lazar entend par « viser un signe » (R3).
- Course nulle v5.3 contre v5.3 : indispensable (Opus, Argon) ou limite déclarée, la variance venant des graines de (b)
  (Fable).
- Première expérience : marqueur du lanceur (Fable), calcul préalable par script de la valeur du pilote pour (b) (Opus),
  scellement immédiat de (b) avec agrégation (Argon).

## Erreur de la question (la mienne)

« Par famille, 36 et 24 tâches par part » est ambigu : Opus et Argon l'ont lu en partie comme 48 tâches au test final.
La banque v3 sert 60 tâches par part (36 en conscience d'évaluation, 24 en contrôle de délégation). Refaits sur 60 tâches
(erreur type binomiale de la moyenne des familles ≈ 0,056 ; largeur de l'intervalle à 90 % = 2 t σ √(2/n) ; bornes
basses sans variance entre graines) : 3 graines par objet ≈ 0,20 ; 4 ≈ 0,15 ; 6 ≈ 0,12 ; 9 ≈ 0,09 ; 11 ≈ 0,08.

## Décisions soumises à Lazar (26 octobre, vers 00:45 UTC)

1. **Écriture des hypothèses de (b)** : (3+) maintenant, sans score du pilote 4, en y versant ses deux courses comme
   graines (recommandé, confiance moyenne) ; (3) sans les verser ; (2') agent neuf sous enveloppe. Sans réponse, le texte
   du pilote 4 garde (1).
2. **Taille de (b)** : 4 graines par objet (270 / 450 USD) ; plan à deux paliers, +4 graines par objet seulement si
   l'issue est indéterminée (+360 / +600 USD ; recommandé, confiance moyenne) ; 6 graines par objet (450 / 750 USD) ;
   δ à fixer par Lazar sans score (proposé : 0,10). Dépense : pas de défaut.
