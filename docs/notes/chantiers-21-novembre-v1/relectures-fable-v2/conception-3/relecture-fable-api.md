# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHwU6ESkZLJqdzJ4DjcA`
- Heure (UTC) : 2026-11-22T12:11:26Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 125000, aucune relance, aucun repli vers un autre modèle, budget de tâche 96000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/chantiers-21-novembre-v1/mandats-fable-v1/consigne-relecture-v2-chantiers-21-v1.md` — sha256 b196ade3c35f7555ed3a096e4f3b9ec19451c0d3bb72d5dabe42fb26f3b83b34 (compagnon : vérifié)
  - correction : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-3-audit-apres-coup-v2.md` — sha256 a8dac56d8ae80f54efdbf438e094b53d8564d33ad86b5e09a3597762e948005e (compagnon : vérifié)
  - correction : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-3-audit-apres-coup-v2-erratum-1.md` — sha256 cd97850b03a5165722ec0fff9d23acd9bdd4644644c7dd31cb3d80943fe820ba (compagnon : vérifié)
  - remarques : `docs/notes/chantiers-21-novembre-v1/copies-sans-nom-v1/contre-lecture-reponse-3-audit-apres-coup-opus-v1-sans-motif-v1.md` — sha256 99ab9b6a4bc61fe61b7d2a444cfb03803b2e0ea4bcefea1d29fdfcf185bce29b (compagnon : vérifié)
  - remarques : `docs/notes/chantiers-21-novembre-v1/contre-lectures-v1/verification-conception-3-v2-opus-v1.md` — sha256 a00992447d32894e243c6963c4f543b903328d2a665993d0bef0117a39cb976a (compagnon : vérifié)
  - remarques : `docs/notes/chantiers-21-novembre-v1/contre-lectures-v1/calculs-contre-lecture-reponse-3-audit-apres-coup-opus-v1.txt` — sha256 0f02172c75b380dd6d20091e1fd2febe8326c0ee92dc00eccad14124e52eb98d (compagnon : vérifié)
  - avant : `docs/notes/chantiers-21-novembre-v1/reponses-fable-v1/demande-3/relecture-fable-api.md` — sha256 62d944cf89b6832fb9a3f85083bbc7439ed4575ddc2b095ed7bb125bf04847bd (compagnon : vérifié)
- Empreinte de l'invite envoyée : 37ac740249828e9fa3a42a65e94011d0169c28ce9e3436789750998c9e644cde
- Jetons : entrée 52422, sortie 22474 (dont réflexion 14432), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.318336 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Relecture par le concepteur de la conception 3 corrigée (v2 et erratum 1)

**Conclusion d'abord.** Aucune des 32 corrections n'est refusée : 24 sont acceptées telles quelles et 8 avec retouche. Les trois couples de l'erratum sont acceptés. La v2 est **scellable après les quinze couples F-1 à F-15 ci-dessous**. Trois points pèsent plus que les autres :
- **F-1** : l'essai du plancher ne peut pas tourner à la taille par défaut ;
- **F-2** : la correction de l'alerte d'excès n'est valide que sur une grille reconstruite, et elle a un prix non écrit ;
- **F-4 à F-6** : la v2 me fait dire que des PDF sont « lus », alors que ni moi ni le contre-lecteur ne les avons ouverts.

Je n'ai exécuté aucun code. Rien n'est revendiqué.

Les couples s'appliquent à la v2 corrigée par l'erratum 1. J'ai contrôlé à la lecture, non par programme, que chaque ancien texte y figure une seule fois.

## 1. Corrections portées, une par une

| Correction | Avis | Raison de la retouche |
|---|---|---|
| C-1 | acceptée | |
| C-2 | acceptée avec retouche (F-1) | L'essai doit continuer après l'alarme et avoir assez d'endommagés |
| C-3 | acceptée avec retouche (F-10) | La garde 2 refuserait le bras `sans_plancher` |
| C-4, C-5, C-6 | acceptées | |
| C-7 | acceptée avec retouche (F-2) | Grille à reconstruire au-dessus de d0⁺ ; prix à écrire |
| C-8 | acceptée avec retouche (F-15) | La formule ignore l'incertitude de la référence |
| C-9, C-10, C-11 | acceptées | |
| C-12 | acceptée avec retouche (F-8, F-9) | Le § 2 dit encore que la politique lit le score ; la liste compte cinq canaux |
| C-13, C-14 | acceptées | |
| C-15 | acceptée | |
| C-16 | acceptée avec retouche (F-7, F-11, F-12) | Chiffres sans marque ; l'échelle manque au § 8 et à la décision 2 |
| C-17 | acceptée avec retouche (F-3) | Un jeton seul n'empêche pas de recopier un contenu réel |
| C-18 à C-22 | acceptées | |
| C-23 | acceptée avec retouche (F-4, F-5, F-6) | Statut « lu » non attesté ici ; six ouvrages sous deux statuts |
| C-24, C-25 | acceptées | |
| C-26 | acceptée avec retouche (F-13) | Le § 1 dit encore « reconstruit » |
| C-27 à C-32 | acceptées | |
| R-1, R-2, R-3 | acceptés | |

Les raisons en détail, avec leurs couples.

**F-1 (C-2 ; touche aussi C-1, C-4 et C-6).** Deux défauts empêchent l'essai de tourner tel qu'écrit.
- [CALCUL] C-12 fixe N = 10 000. Dans « attaque choisie », seul le type d'enjeu 25, de part 0,01, est attaqué. Cela donne environ 100 endommagés par répétition, alors que l'essai lit le rang 299.
- [PROPOSITION] En signature, l'alarme part à la première prise de toute source. Un développeur qui arrête le monde à l'alarme ne verra jamais la prise de source « plancher ».

Ancien :
```text
Le compte toutes sources n'éprouve pas le plancher dès que β > 0.
```
Nouveau :
```text
Le compte toutes sources n'éprouve pas le plancher dès que β > 0. Pour cet essai, et pour tout essai sur un rang de prise (points 2 et 3), le monde ne s'arrête pas à la première alarme et il est prolongé jusqu'au rang lu (N = 10 000 ne donne qu'environ 100 endommagés quand seul le type d'enjeu 25, de part 0,01, est attaqué) ; une répétition qui n'atteint pas ce rang rend le refus nommé « trop peu d'endommagés », jamais une prise ni une absence de prise.
```

**F-2 (C-7).** [CALCUL] Le rapport de vraisemblance d'une alternative d_j contre d0⁺ a une espérance au plus égale à 1, sous tout taux vrai d ≤ d0⁺, seulement si d_j > d0⁺. Pour une alternative placée sous d0⁺, cette espérance dépasse 1 dès que d < d0⁺. Or la grille de la v2 part de d0, donc peut tomber sous d0⁺ : il faut la reconstruire.

Ancien :
```text
Si d0 vient de m épisodes de référence, le pari se fait contre d0⁺, borne haute de Clopper et Pearson à α/2 sur la référence, avec alarme à 2/α ; la validité reste ≤ α par union.
```
Nouveau :
```text
Si d0 vient de m épisodes de référence, le pari se fait contre d0⁺, borne haute de Clopper et Pearson à α/2 sur la référence, avec alarme à 2/α, sur une grille reconstruite au-dessus de d0⁺, d_j = d0⁺ + (1 − d0⁺)·2^(−j) (une alternative sous d0⁺ ôterait la validité) ; la validité reste ≤ α par union, à tout horizon, si la référence et le flux honnête suivent la même loi. Prix, à rapporter : un excès inférieur à d0⁺ − d0 n'alarme jamais (pour d0 = 0,10 et m = 400, d0⁺ ≈ 0,13 par approximation normale, à rejouer) ; la puissance perdue n'est pas mesurée.
```

**F-15 (C-8).** [CALCUL] Quand d0 est estimé, la variance de la référence s'ajoute à celle de la strate.

Ancien :
```text
la puissance du pari se lit sur le simulateur.
```
Nouveau :
```text
la puissance du pari se lit sur le simulateur. Si d0 est estimé sur m épisodes, la formule devient N·z₀,₉₉·√(d0·(1 − d0)·(1/(N·π_min) + 1/m)), et la sortie dit en plus l'excès jamais vu, d0⁺ − d0.
```

**F-3 (C-17).** [PROPOSITION] Un jeton prouve qu'on l'a émis, non que le contenu est planté. Lier le jeton à la graine permet de re-dériver l'entrée ; un contenu réel ne se re-dérive pas.

Ancien :
```text
Artefact : un vecteur de poids lu d'un fichier de sonde du dépôt, ou un verdict sans jeton, est refusé.
```
Nouveau :
```text
Artefact : un vecteur de poids lu d'un fichier de sonde du dépôt, ou un verdict sans jeton, est refusé. Le jeton lie l'empreinte du contenu de l'entrée à sa graine ; le harnais re-dérive l'entrée de la graine et refuse si l'empreinte diffère : un contenu réel recopié sous un jeton valide est refusé aussi (second artefact). La garde ne couvre pas une modification du harnais lui-même.
```

**F-7 (C-16).** Je n'ai pas la sortie de la boucle sous les yeux dans cette relecture : les chiffres du rang 12 sont repris du contre-lecteur.

Ancien :
```text
Bloc C2 retrouvé à 4 erreurs types (0,34, 0,14, 0,03 à trois étiquettes)
```
Nouveau :
```text
[FAIT RAPPORTÉ, sous supposition, chiffres repris de la contre-lecture et non relus par le concepteur] Bloc C2 retrouvé à 4 erreurs types (0,34, 0,14, 0,03 à trois étiquettes)
```

**F-4 et F-5 (C-23).** La règle de cette consigne veut le statut « rapporté, non vérifié sur PDF », sauf lecture attestée par une pièce jointe.
- [FAIT RAPPORTÉ] Le contre-lecteur écrit lui-même qu'il n'a ouvert aucun PDF et que ses statuts viennent de N-076, § 11.
- N-076 n'est pas joint ici.
- La v2 range en outre six ouvrages à la fois parmi les « lus » et dans la liste des « non vérifiés ».

Ancien :
```text
Statuts. Lus sur PDF au dépôt, aux pages dites par N-076, § 11 (chemins et empreintes y sont) :
```
Nouveau :
```text
Statuts. Rapportés par N-076, § 11, comme lus sur PDF au dépôt, aux pages qu'il dit (chemins et empreintes y sont ; ni le concepteur ni le contre-lecteur n'ont ouvert ces PDF) :
```

Ancien :
```text
Les autres restent au statut « rapporté, non vérifié sur PDF » :
```
Nouveau :
```text
Ces citations ajoutées sont au statut « rapporté, non vérifié sur PDF ». La liste ci-dessous reprend toutes les antériorités de la v1 : les six nommées en tête y gardent le statut que leur donne N-076, § 11 ; les autres restent au statut « rapporté, non vérifié sur PDF » :
```

## 2. Constats bloquants

Le contre-lecteur n'en juge aucun bloquant, et je n'en ajoute pas. Deux gardes portent pourtant tout le reste ; voici ce qu'elles garantissent après correction.

**L'essai du plancher (C-1, C-2, F-1).**
- **Garantie.** [CALCUL] Sur un simulateur juste, le compte des répétitions où la première prise de source « plancher » est au rang ≤ 299 suit une binomiale (R, 0,95046). Le refus à tort survient donc moins d'une fois sur mille.
- **Puissance.** [FAIT RAPPORTÉ, bloc R2 du contre-lecteur] Au seuil de 1 869 sur 2 000 :
  - 1,000 contre un plancher réel de 0,005 ;
  - 0,583 contre 0,009 (1,000 à R = 20 000, au seuil de 18 903).
- **Artefact.** [FAIT RAPPORTÉ, bloc R4] Il rend 1 550 sur 2 000 et il est refusé. [CALCUL] L'attendu est 2 000 × 0,7766 ≈ 1 553.
- **Rejeu.** `python3 -c "from scipy.stats import binom; print(binom.ppf(0.001,2000,0.95), binom.cdf(1868,2000,1-0.995**299), binom.cdf(1868,2000,1-0.991**299))"`.
- **Suppositions.** Épisodes indépendants ; monde prolongé jusqu'au rang 299 et non arrêté à l'alarme (F-1) ; q = 1.
- **Limite.** L'essai éprouve le code du plancher, rien d'un modèle.

**L'alerte d'excès (C-7, F-2).**
- **Garantie.** [CALCUL] P(fausse alarme) ≤ α à tout horizon : α/2 pour une référence trompeuse, α/2 par la borne de Ville.
- **Chiffres.** [FAIT RAPPORTÉ, bloc R6 ; d0 = 0,10, m = 400, grille de 8 alternatives]

| Cas | Horizon 400 | Horizon 4 000 |
|---|---|---|
| d0 connu | 0,018 | 0,027 |
| d0 estimé, sans correction | 0,052 | 0,249 |
| d0 estimé, avec correction | non rejoué | 0,0035 |

- **Suppositions.** Référence et flux honnête de même loi, tirages indépendants, grille au-dessus de d0⁺.
- **Non établi.** [HYPOTHÈSE] J'ignore si le rejeu du contre-lecteur a reconstruit la grille. Son 0,0035 ne vaut que pour une seule configuration.
- **Prix.** [CALCUL, approximation normale] d0⁺ ≈ 0,10 + 1,96 × 0,015 ≈ 0,13. Un excès inférieur à 0,03 environ, soit près d'un tiers du taux honnête, n'alarme jamais. Valeur exacte à rejouer : `scipy.stats.beta.ppf(0.975, 41, 360)`.

## 3. Ajouts non portés

- **Remarque sur Auer et al.** : portée par R-3, acceptée.
- **Canal `lisibilite`.** Le vérificateur le juge suffisant tel quel. Je le porte quand même, car la liste est ce que le développeur lira.

**F-9**

Ancien :
```text
avec un canal par grandeur :
```
Nouveau :
```text
avec un canal par grandeur (six avec `lisibilite`, défini aux paramètres) :
```

- **Puissance perdue par C-7**, que le contre-lecteur dit non mesurée : portée dans F-2.
- **Mise à jour de mes propres réserves**, que personne n'a visées.

**F-6**

Ancien :
```text
- **Aucun PDF ouvert.** Toutes les antériorités sont de mémoire ou reprises des pièces jointes.
```
Nouveau :
```text
- **Aucun PDF ouvert.** Les antériorités sont de mémoire ou reprises des pièces jointes ; le statut « lu sur PDF » de six d'entre elles est celui de N-076, § 11, non une lecture du concepteur.
```

**F-14**

Ancien :
```text
Les seuils binomiaux et les puissances viennent d'une approximation normale et sont à rejouer avant tout usage.
```
Nouveau :
```text
Les seuils binomiaux 1 869 et 18 903 et la puissance 0,583 sont rejoués par la contre-lecture (bloc R2) ; les autres puissances restent d'approximation normale, à rejouer avant tout usage.
```

## 4. Ce que la correction a cassé ailleurs

F-1 relève aussi de cette rubrique : c'est le défaut N = 10 000 de C-12 qui prive de ses endommagés l'essai de C-1 et C-2.

**F-8 : le § 2 contredit C-12.** C-12 interdit à la politique de lire le score ; le monde du § 2 la fait encore dépendre de g(score).

Ancien :
```text
La politique de dommage n'endommage que les épisodes où g(score) = 0 et où l'enjeu est maximal.
```
Nouveau :
```text
La politique de dommage n'endommage que des épisodes de lisibilité nulle et d'enjeu maximal ; g(score) = 0 y est forcé (point 1) et ce forçage est consigné au journal.
```

**F-10 : la garde 2 refuserait le bras de comparaison de C-3.**

Ancien :
```text
Ligne à π = 0 ; probabilité manquante ; plancher fonction du score
```
Nouveau :
```text
Ligne à π = 0 hors de la configuration `sans_plancher` (dont le journal porte l'étiquette « sans plancher : aucune borne ») ; probabilité manquante ; plancher fonction du score
```

**F-11 : le rang 12 de C-16 manque à la liste des instruments.**

Ancien :
```text
le simulateur, la table, les gardes, les deux familles plantées et les treize épreuves.
```
Nouveau :
```text
le simulateur, la table, les gardes, les deux familles plantées, les treize épreuves et l'échelle des échelons simulée (rang 12, monde planté seul, sous le jeton de provenance).
```

**F-12 : la décision 2 ne place pas le rang 12.**

Ancien :
```text
(a) Les rangs 1 à 10 maintenant, les épreuves ensuite.
```
Nouveau :
```text
(a) Les rangs 1 à 10 maintenant ; le harnais, les épreuves et l'échelle des échelons (rangs 11 et 12) ensuite.
```

**F-13 : le § 1 dit encore « reconstruit », contre C-26.**

Ancien :
```text
(s̄ = 1,60, reconstruit du bloc C joint)
```
Nouveau :
```text
(s̄ = 1,60 ; loi du script du bloc C, supposition d'illustration)
```

## 5. Verdict du concepteur

**Scellable après les couples ci-dessus** (F-1 à F-15, appliqués à la v2 corrigée par l'erratum 1). Aucune v3 n'est nécessaire : un erratum 2 suffit. [PROPOSITION] Il faut que le programme d'extraction contrôle l'unicité de chaque ancien texte, que je n'ai vérifiée qu'à la lecture.

## 6. Décisions qui reviennent au directeur

1. **La strate du plancher porte la borne et l'alerte d'excès ; en signature, toute prise alarme ; l'estimateur pondéré complet est rapporté à côté.**
   - Enjeu : la lettre « l'audit qui suit le score ne porte pas la borne » et la taille des poids. L'exactitude ne départage plus les options depuis C-13.
   - (a) Ainsi. Avantage : conforme à la lettre, intervalle exact. Inconvénient : les audits d'enjeu et de soupçon restent hors garantie.
   - (b) Tout par l'estimateur pondéré. Avantage : plus d'étiquettes. Inconvénient : la borne reposerait sur les parts d'enjeu et de soupçon ; poids jusqu'à s_max/π_min.
   - Recommandation : (a), confiance 0,8. Défaut sous 48 heures : (a).

2. **Ranger ces instruments sous un chantier actif.**
   - Enjeu : sans cela, l'écriture ne commence pas.
   - (a) Les rangs 1 à 10 maintenant ; le harnais, les épreuves et l'échelle ensuite. Avantage : la règle d'audit ne dépend d'aucun point ouvert. Inconvénient : travail hors des chantiers actifs.
   - (b) Tout attendre. Avantage : aucun écart. Inconvénient : rien n'est prêt.
   - Recommandation : (a), confiance 0,7. Nœud, pas de défaut.

3. **Écrire les épreuves 1 et 13, et le mode « bras de flux » planté, avant le mot sur (b′).**
   - Enjeu : ils éprouvent des clauses non adoptées.
   - (a) En dernier, interdit entier par défaut, étiquette « non en vigueur », jeton de provenance lié à la graine (F-3). Avantage : prêts le jour du mot. Inconvénient : du code pour une règle peut-être refusée.
   - (b) Différer. Avantage : pas de code perdu. Inconvénient : délai le jour du mot.
   - Recommandation : (a), confiance 0,6. Nœud, pas de défaut.

4. **Instruire le devis de l'étape 1.**
   - Enjeu : une dépense, une famille consommée, l'anti-circularité touchée. Depuis C-15, seul le point à 3 étiquettes est « au taux du plancher ».
   - (a) Devis seul, après les treize épreuves et l'échelle simulée. Avantage : la borne haute est connue avant de décider. Inconvénient : un bras de plus.
   - (b) Rester aux mondes plantés. Avantage : aucune dépense. Inconvénient : rien sur de vrais états.
   - Recommandation : (a), confiance 0,6. Nœud, pas de défaut.

5. **Rapporter partout le prix de l'orientation, b/π_min, et le coût du plancher sur la part d'enjeu.**
   - Enjeu : sans ces deux chiffres, la règle promet plus qu'elle ne tient devant un agent informé.
   - (a) Oui. Avantage : aucune promesse au-delà du plancher. Inconvénient : phrases plus longues.
   - (b) Non. Avantage : phrases plus courtes. Inconvénient : promesse trop large.
   - Recommandation : (a), confiance 0,8. Défaut sous 48 heures : (a).

6. **(Nouvelle) Accepter le prix de l'alerte d'excès quand le taux honnête est estimé.**
   - Enjeu : avec la correction, un excès sous d0⁺ − d0 n'alarme jamais (environ 0,03 pour d0 = 0,10 et m = 400) ; sans elle, 0,249 de fausses alarmes à l'horizon 4 000.
   - (a) Correction et prix écrits, comme en F-2. Avantage : validité à tout horizon. Inconvénient : zone aveugle.
   - (b) Exiger une référence plus grande, m fixé pour une zone aveugle déclarée. Avantage : zone réduite. Inconvénient : coût en épisodes honnêtes, non chiffré ici.
   - (c) Sans correction, horizon borné à m. Avantage : puissance. Inconvénient : 0,052 pour 0,05 dès l'horizon 400, sans garantie.
   - Recommandation : (a), puis chiffrer (b) sur le simulateur ; confiance 0,7. Défaut sous 48 heures : (a).

## Ce que je n'ai pas fait

- **Aucun code exécuté.** Les chiffres des blocs R1 à R7 sont des faits rapportés du contre-lecteur. Mes calculs sont faits à la main : d0⁺ ≈ 0,13, 100 endommagés, l'attendu de 1 553.
- **Aucun contrôle par programme** de l'unicité des quinze anciens textes ni de l'application des couples.
- **Aucun PDF ouvert.** N-076, la boucle v2 et la sortie de la boucle ne sont pas joints à cette relecture. Les chiffres du rang 12 et les statuts « lus » ne sont donc pas relus par moi.
- **Script et rapport de portage non lus.**
- **Non mesuré :**
  - la puissance du pari corrigé ;
  - le 0,0035 hors de sa configuration ;
  - la couverture de l'intervalle hypergéométrique.
- **Non traités, comme en v1 :**
  - la dépendance entre épisodes ;
  - les faux positifs en signature ;
  - le délai en temps d'horloge ;
  - le dommage non binaire ;
  - les deux devins.
