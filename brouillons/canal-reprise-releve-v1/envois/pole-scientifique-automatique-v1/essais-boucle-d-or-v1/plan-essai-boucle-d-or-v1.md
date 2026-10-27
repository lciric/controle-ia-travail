# Essai « Boucle d'or » — l'allocateur à fenêtre de Gemini contre des allocateurs qui apprennent — plan v1 (fixé avant tout lancement)

Lignée conv-audit (instance nouvelle), écrit le 27 octobre 2026 à partir de 08:22 UTC (heure lue sur `date -u`), sur le
mot de Lazar de 09:20 heure de Paris, d'après l'avis de l'instance sortante `avis-boucle-d-or-gemini-v1.md`
(`0414f1ab4dc7a76346e885d4b2c2f69293af094fc52db966e1915cb1363000aa`, branche `canal/conv-audit-relais-memoire-v1`, commit
`0ba98ae`). **Exploratoire (R-522), non opposable, lu dans les deux sens.** Ce plan est poussé avant le premier lancement ;
aucun essai, même de fumée, n'a tourné avant lui. Le script PowerShell de Gemini n'est ni lu ni exécuté.

## Question

L'allocateur de Gemini — ne tester que les filles dont les parents ont une similarité de domaine dans une **fenêtre**
(0,12 à 0,26, la bande du milieu de sa simulation) et, dans la fenêtre, viser l'**entropie** maximale du verdict — fait-il
plus de découvertes vraies par dollar que des allocateurs qui **apprennent en ligne**, quand la valeur suit la fenêtre, et
perd-il quand elle ne la suit pas ?

## Monde, candidats, juge

- Par répétition, un réservoir de 300 filles candidates. Chacune : similarité de domaine s tirée uniformément sur
  [0 ; 0,8] (seule information visible des allocateurs) ; elle est **vraie** (contenu neuf sur les traits) avec la
  probabilité v(s) du monde, sinon fausse.
- Vraie : monde = parent A sur la sous-population 0, loi neuve sur la 1 (force tirée uniformément sur [0,3 ; 1,5], pour
  des effets de taille variée) ; la fille prédit exactement cela (forme « fille neuve » de l'expérience 1).
- Fausse : monde tiré parmi « parent A vrai », « parents vrais par sous-population », « mélange des parents » ; la fille
  est une copie du parent A ou une enveloppe aveugle des parents (formes contenues dans le nul augmenté). Le trou connu du
  critère des filles (« parent + loi aveugle ») est **exclu** de cet essai, et dit.
- Tester une fille = le **juge v1** (ordre secret, urne, nul augmenté des parents, marge 2δ₀ = 0,02), 50 tirages de
  calibrage et 200 tirages frais, coût d'un dollar simulé par test. Une découverte vraie = une fille vraie promue.
- Mêmes nombres aléatoires pour tous les allocateurs dans une répétition : le réservoir, les vérités et l'issue du juge
  pour une fille donnée sont les mêmes quel que soit l'allocateur qui la teste.

## Mondes v(s)

| monde | v(s) | la fenêtre devrait |
|---|---|---|
| cloche | 0,5 si 0,12 ≤ s ≤ 0,26, sinon 0,05 | gagner |
| bords | 0,5 si s < 0,06 ou s > 0,6, sinon 0,05 | perdre |
| croissant (proches meilleurs) | 0,05 + 0,55·s/0,8 | perdre |
| décroissant (lointains meilleurs) | 0,60 − 0,55·s/0,8 | perdre |
| plat | 0,2 | ne rien changer |

## Allocateurs (budget : 40 tests par répétition ; une fille au plus une fois ; rien ne leur est donné)

- **hasard** : uniforme parmi les filles non testées.
- **Thompson** : huit cases de s (largeur 0,1), loi bêta(1, 1) par case sur la probabilité de promotion ; à chaque test,
  un tirage par case ; une fille non testée au hasard dans la case du plus grand tirage ; récompense = promotion par le juge.
- **tri par espérance de découvertes par dollar** : mêmes cases, moyenne a posteriori (coût constant) ; égalités tirées au
  hasard.
- **fenêtre (Boucle d'or)** : seulement s dans [0,12 ; 0,26] ; sept cases de largeur 0,02 ; probabilité de promotion
  apprise en ligne par case (moyenne a posteriori bêta(1, 1)) ; choisit la case d'entropie maximale du verdict (la plus
  proche de 0,5) ; fenêtre épuisée → hasard sur le reste (dit au rapport).

## Mesure, seuil, lecture (fixés ici)

- Mesure : découvertes vraies par dollar = filles vraies promues / 40, par répétition ; rapportées aussi : promotions
  fausses par dollar.
- 30 répétitions par monde ; graine maîtresse **20261027** (exploration), dérivation `graine_derivee` (SHA-256).
- Différences appariées, sur les 30 répétitions : D₁ = fenêtre − meilleur des deux allocateurs appris (Thompson ou tri,
  le meilleur des deux choisi par sa moyenne dans ce monde) ; D₂ = fenêtre − hasard. Intervalle à 95 % par rééchantillonnage
  des répétitions (10 000 tirages, graine dérivée de la graine maîtresse).
- **Lecture par monde** : la fenêtre **gagne** si l'intervalle de D₁ est entièrement au-dessus de 0 ; **perd** s'il est
  entièrement au-dessous ; **indistincte** sinon. Même lecture pour D₂ contre le hasard.
- **Verdict d'ensemble** : la fenêtre est **à garder** seulement si elle gagne contre les allocateurs appris dans le monde
  « cloche » **et** ne perd contre eux dans aucun des quatre autres ; **à écarter** si elle perd dans au moins un monde
  où la valeur ne suit pas la fenêtre et ne gagne pas dans « cloche » ; **à garder sous condition** (seulement si l'on sait
  d'avance que la valeur suit la fenêtre) si elle gagne dans « cloche » et perd ailleurs.
- **Mes prédictions** (signées, confiance) : cloche — gagne contre le hasard (0,9), indistincte ou gagne contre les
  appris (0,6) ; bords, croissant, décroissant — perd contre les appris (0,8) ; plat — indistincte (0,8). Verdict
  d'ensemble prédit : « à garder sous condition » (0,6).
- **Ce qui mettrait l'essai en défaut** : Thompson pas meilleur que le hasard dans les mondes non plats (apprentissage
  trop lent pour ce budget : l'essai ne départagerait rien) ; promotions fausses au-dessus de α en moyenne (le juge
  serait en cause, pas l'allocation).
