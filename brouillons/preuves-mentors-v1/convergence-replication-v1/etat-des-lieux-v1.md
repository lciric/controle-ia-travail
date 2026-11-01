# État des lieux — la course de convergence des règles de défense, avant sa réplication sur graine neuve — v1

Sous-agent neuf (Claude Opus 5.5), 1er novembre 2026, ≈ 21:00 UTC. Rien décidé, rien scellé, rien commité, aucun fichier existant modifié, aucun réseau, aucune ref `donnees/*` lue. Pièces lues dans la branche déjà récupérée `origin/canal/session-depot-reprise-n67` (lecture de ref seulement, extraction dans mon dossier temporaire), empreintes SHA-256 recalculées par `sha256sum` et citées en entier en fin de document.

## 0. En tête : processeur seul, aucun appel payant

- **La course ne fait aucun appel de modèle, aucun appel payant, aucun réseau** : c'est un pilote de mécanisme sur un jeu synthétique (aucun modèle de langage, aucun texte ; préenregistrement scellé, § Résumé point 6 : « Aucune dépense : processeur seulement »). **Devis : 0 USD.** La réplication n'est donc pas un nœud de dépense ; elle reste un nœud « course décisive » (le texte original exigeait un mot de GO distinct de Lazar pour la lancer ; R-1075, « go » du 1er novembre 21:30 heure de Paris, couvre le dossier de preuves, pas explicitement la course).
- **Durée observée de la course originale** : 1 692,7 s de mur (≈ 28 min) sur 2 processus, 3 327 s de processeur cumulé (200 tâches ; 15,9 s par tâche en moyenne au δ 1,4 et 17,4 s au δ 1,6 ; maximum 19,3 s et 20,9 s), sous `timeout 3600`. Cette machine a 2 cœurs, Python 3.13.18, numpy 2.4.6, scipy 1.17.1, et la même chaîne de plateforme que le manifeste original (`Linux-6.18.44-fc-v185-x86_64-with-glibc2.39`) : **même durée attendue, ≈ 28 min de mur, 1 h au plus.**
- **Réplicable sur processeur cette nuit : oui, sous trois conditions** (détail § 7) : (1) un code v3 = copie du code v2 où ne changent que les racines (dérivées de l'empreinte du préenregistrement scellé), l'identité de préenregistrement, le chemin de l'arène (copie suivie par git) et une sérialisation des défenses finales (sortie seulement) — le code v2 refuse toute racine neuve ; (2) les fichiers de la course rapatriés depuis la branche n67 dans cet arbre (ils n'y sont pas) ; (3) le GO de course de Lazar.

## 1. Ce qu'est la course, exactement

**Question posée** (préenregistrement scellé, § Résumé point 1) : dans le jeu synthétique de l'arène v4, laquelle de quatre règles de mise à jour du défenseur laisse le moniteur déployé le moins exploitable après T = 8 tours de coévolution, et une règle quelconque fait-elle mieux que ne rien faire.

**Le monde** (une tâche = un couple (budget δ, instance)) : loi « propre » N(0, I₆) ; loi « cible » par instance = mélange gaussien à K = 3 composantes en dimension d = 6, moyennes de norme 4, écarts-types 1 ; **la même loi cible sert aux deux budgets δ d'une instance**. 100 instances, deux budgets δ ∈ {1,4 ; 1,6} : 200 tâches. Configuration canonique `3fbb27fc…` (la même que l'arène v4).

**Les deux joueurs** (formalisation, § 1.1–1.2 ; jeu à somme nulle, gain = taux de détection) :
- **l'attaquant** choisit les 36 paramètres θ = (μ, σ) d'un mélange gaussien à 3 composantes, dans la boîte |μ| ≤ 5, σ ∈ [0,5 ; 1,5], sous la contrainte de comportement « distance de Wasserstein d'ordre 2 (moyenne quadratique sur les composantes) à la cible ≤ δ » ; il joue une **meilleure réponse locale** (programmation quadratique séquentielle depuis plusieurs départs, objectif lissé, choix final sur le taux dur par Monte-Carlo) contre la défense déployée, en dernier à chaque tour ;
- **le défenseur** déploie un **moniteur linéaire** (score w·x + b, 7 paramètres), seuillé au quantile 1 − α de 20 000 échantillons propres communs (α = 0,01 : le taux de fausses alertes est une contrainte, pas un gain) ; il le réentraîne (quasi-Newton à mémoire limitée, 8 départs, objectif de détection lissé : l'oracle « détection ») selon sa règle ; une défense « mélange » tire un moniteur au hasard selon des poids p à chaque requête.

**Les cinq variantes comparées** (gel v2 § 2 ; chacune sa trajectoire, moniteur commun M0 au tour 0 entraîné contre la loi cible) :

| Code | Surnom | Mise à jour du défenseur | Déployé |
|---|---|---|---|
| R0 | **défense figée** (témoin) | aucune : M0 jamais réentraîné | 1 moniteur, 7 paramètres |
| R1 | **dernière attaque** | réentraîné contre la seule attaque du tour | 1 moniteur |
| R2 | **historique** (référence ; = bras A de l'arène v4 au bit) | réentraîné contre le mélange uniforme de toutes les attaques passées, cible comprise | 1 moniteur |
| R3 | **mélange d'équilibre** (= bras B de l'arène v4 au bit) | oracle double tronqué : poids d'équilibre p du jeu restreint (programme linéaire), moniteur nouveau entraîné contre la stratégie d'équilibre q de l'attaquant | **mélange aléatoire de jusqu'à 9 moniteurs** (63 paramètres déployés, 7 par requête) |
| R4 | **régularisation vers le passé** | comme R2, plus la pénalité 2λ(1 − cos(w, u)), λ* = 0,3, u = moyenne des directions passées | 1 moniteur |

**Les mesures** (préenregistrement scellé, § Métrique) :
- **V** (« détection finale ») : la défense finale est figée, l'attaquant joue en dernier deux fois — **standard** (12 départs tirés, un départ vers l'origine, les 8 attaques passées ; 512 tirages de Monte-Carlo par composante ; 100 itérations) puis **renforcé** (48 départs plus les précédents ; 200 itérations) — chaque réponse est évaluée sur 19 998 échantillons frais ; **V = la plus basse des deux détections** ; exploitabilité finale X = 1 − V. Mesure principale de HR0, HR1, HR3.
- **X̄** (« exploitabilité moyenne au fil des tours ») = moyenne sur les 8 tours de 1 − (détection de la défense du tour contre l'attaquant léger du tour). Mesure principale de HR2.
- **(ii)** : détection moyenne sur 50 lois « tenues à l'écart » par tâche (racine à part, jamais vues par un entraînement) ; indicateurs de cycle I1, I2, I3 ; coût.

**Taille par cellule** : une cellule = (variante, δ) ; **N = 100 instances par δ** ; 200 tâches × 5 variantes = 1 000 trajectoires. Les contrastes sont **appariés par instance** (même cible, même M0, mêmes lois tenues ; graines de la trajectoire et de la finale propres à chaque règle).

**Graines** : racine principale **20266201**, racine des lois tenues **20266202**, écrites au gel v1 (09:52 UTC) avant toute exécution et jamais employées avant la décision ; chaque tirage `SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_règle, tour, rôle, …))` ; rééchantillonnage `SeedSequence(entropy=20266201, spawn_key=(code_delta, code_contraste, 0, 0, 99))`.

**Le run** : `diag/20261101-160323-regles-defense-convergence/` (résultats `d07ece47…`, analyse `18b80112…`), manifeste `runs/20261101-160323-regles-defense-convergence/manifeste.json` (`36db58cf…`), créé le 1er novembre 2026 à 16:03:25 UTC, commit `1dc492ba`, commande `arene_regles_defense_v2.py decision --prereg …/preregistrement-regles-defense-convergence-v1.md --instances 0:100 --run-id 20261101-160323-regles-defense-convergence --lambda 0.3 --reference moyenne --processus 2`, dépôt propre, aucune réserve ; 0 entraînement non convergé sur 6 800, 0 départ non fini sur 127 000, fausses alertes toutes dans α ± 0,005 (lecture, § 1).

## 2. Où est le code

Tout est dans la branche `origin/canal/session-depot-reprise-n67` ; **rien de la course n'existe dans cet arbre de travail** (`canal/conv-audit-n04`) : ni `docs/notes/convergence-defense-v1/`, ni le préenregistrement, ni `diag/` ni `runs/` du run (vérifié sur disque).

| Pièce | Chemin (branche n67) | Empreinte |
|---|---|---|
| Code de la course (v2) | `docs/notes/convergence-defense-v1/regles-defense-v1/arene_regles_defense_v2.py` | `9f0dcf5e…` |
| Essais (25) | `…/regles-defense-v1/test_arene_regles_defense_v2.py` | `78d979ab…` |
| Gel v2 (écrit avant exécution, épinglé dans le code) | `…/regles-defense-v1/gel-regles-defense-v2.md` | `9977d7df…` |
| Arène v4 (le jeu, l'attaquant, la finale, les quantiles) | chargée par chemin : `donnees/argon-seul-convergence-v1/arene_melange_v4.py` | `70c77fd5…` |

**Point d'attention — l'arène v4** : le code v2 la charge à `donnees/argon-seul-convergence-v1/arene_melange_v4.py` (ligne 73), dossier **ignoré par git** et absent de la branche n67 comme de cet arbre. Une **copie identique au bit** (`70c77fd5…`, recalculée) est suivie par git dans cet arbre : `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/arene_melange_v4.py`. Je l'ai lue (elle n'est pas sous `donnees/`). Pour la réplication, je recommande que le code v3 la charge à ce chemin suivi (même empreinte vérifiée au chargement) : la course ne dépendra plus d'un fichier hors de git.

## 3. Où est la statistique décisive (fichier, fonction, lignes)

Dans `arene_regles_defense_v2.py` (`9f0dcf5e…`) :
- **valeurs par tâche** : V = `V_iii_final`, produite par `finale_regle` (l. 517–533) qui appelle `phase_finale` de l'arène v4 (l. 1145–1183 du fichier v4 : `V = min(V_std, V_renf)`, l. 1160) ; X̄ = `exploitabilite_moyenne_tours` (l. 296–304), calculée dans `trajectoire_regle` (l. 420–514, l. 509) ;
- **contrastes appariés et intervalles** : `analyser_regles` (l. 651–684) — par δ, tâches triées par instance, différences variante − R2 pour les mesures de `MESURES_CONTRASTE` (l. 592–594 : V code 0, (ii) code 1, X finale code 2, X̄ code 8) — et `_boot` (l. 598–602) : 20 000 rééchantillonnages appariés des instances, générateur `gen_regles(racine, code_delta, 200 + 100 × code_mesure + rang, 0, 0, 99)` (l. 187–191), quantiles par la fonction `_q` de l'arène v4 (l. 1314–1315 : `numpy.quantile`, méthode linéaire) aux dix niveaux `QUANTILES` (l. 161 du v4) ; rôle de rééchantillonnage 99 (`ROLE_REECH`, l. 152 du v4) ;
- **appel en décision** : `main`, l. 832 : `analyser_regles(res, RACINE_DECISION)` — la racine du rééchantillonnage est la racine principale ;
- **règle de lecture** : **pas dans le code** ; elle est dans le texte scellé (§ « Critères de lecture gelés » : Table A l. 277–287, Table B l. 289–300, Table B′ l. 302–313) et a été appliquée par un lecteur neuf, qui a recalculé toute la statistique à partir des résultats bruts avec numpy seul (écart 0,0 avec l'analyse du code).

J'ai recodé cette statistique depuis ma propre spécification écrite (sans importer le code) : **écart 0,0** sur les moyennes, écarts-types et dix quantiles des 16 contrastes × 2 δ de l'analyse scellée (script de vérification dans mon dossier temporaire, non versé).

## 4. Ce que dit le préenregistrement scellé

Fichier `prereg/preregistrement-regles-defense-convergence-v1.md`, `d82dea33…` (identique au bit au brouillon 4 ; scellé au commit `1dc492ba`, R-966), identifiant PREREG-REGLES-DEFENSE-V2.

- **HR1 « le mélange bat l'historique »** (déclarée « principale, plomberie ») : Δ(R3, R2) = moyenne de V(R3) − V(R2) ≥ m = 0,02 aux deux δ ; lue **par la Table A seule** : confirmée si est ≥ 0,02 et borne basse B2 > 0 aux deux δ ; réfutée si borne haute B2 < 0 à un δ. P1 : signe +, « ≥ +0,05 », confiance 0,9.
- **HR0 « réentraîner vaut mieux que ne rien faire »** : R2 moins exploitable que R0 d'au moins m ; Table B, classe « R2 > R0 » aux deux δ ; **réfutée si « R0 > R2 », « R0 ≳ R2 » ou « ≈ » à un δ**. P13 : signe −, confiance 0,5, **réserve déclarée d'avance** : les pilotes indiquaient le contraire.
- **HR3 « la régularisation ne nuit pas »** : classe « R4 > R2 », « R4 ≳ R2 » ou « ≈ » aux deux δ et dégénérescence S12 non déclenchée ; réfutée si « R2 > R4 » à un δ.
- **HR2 « oublier coûte »** : sur X̄, classe « R2 > R1 » aux deux δ (Table B′).
- **Bornes** (rééchantillonnage, quantiles) : B2 = [q0,00625 ; q0,99375] ; B8 = [q0,003125 ; q0,996875] ; E8 = [q0,00625 ; q0,99375] ; marge m = 0,02 ; classes testées dans un ordre fixe, la première vraie décide.
- **Déclencheurs d'audit symétriques** : contradiction d'une prédiction ferme dans les deux sens (P1, P12, P13, P7, P11), trop beau ou trop mauvais (S10), mélange dégénéré, R4 dégénéré, optimiseur, dérive des fausses alertes, « conforme et trop propre ».

## 5. Ce que la lecture a appliqué

Lecture préenregistrée (lecteur neuf, `lecture-course-regles-defense-v1.md`, `24081eed…`), puis audit (`audit-trop-beau-course-regles-defense-v1.md`, `7e81d094…`), puis conversion mécanique des verdicts consignée par session-depot (R-976) :

| Hypothèse | Chiffres (δ 1,4 ; δ 1,6) | Lecture | Statut final |
|---|---|---|---|
| HR1 (le mélange bat l'historique) | Δ(R3, R2) sur V : +0,1045 [B2 +0,0906 ; +0,1185] ; +0,1236 [+0,1127 ; +0,1341] | Table A ligne 4 aux deux δ | **confirmée** |
| HR0 (réentraîner vaut mieux que rien) | Δ(R0, R2) sur V : +0,0024 [E8 −0,0088 ; +0,0134] ; +0,0037 [−0,0056 ; +0,0133] | « ≈ » aux deux δ ; déclencheur 1 (P13) → Table B bloquée → audit « pas d'artefact » | **réfutée** : la défense figée fait aussi bien que l'historique, à 0,02 près |
| HR3 (la régularisation ne nuit pas) | Δ(R4, R2) sur V : +0,0202 [B8 +0,0102 ; +0,0331] ; +0,0142 [+0,0064 ; +0,0240] | « R4 ≳ R2 » aux deux δ, S12 non déclenché (5 et 2 tâches sur 100) | **confirmée** (après l'audit) |
| HR2 (oublier coûte) | D̄(R1, R2) sur X̄ : +0,0262 [B8 +0,0201 ; +0,0329] ; +0,0162 [+0,0115 ; +0,0214] | « R2 > R1 » puis « R2 ≳ R1 » ; déclencheur 1 (P12) → audit « pas d'artefact » | **non tranchée** |

Autres lectures recopiées : sur les lois tenues à l'écart, la défense figée détecte **mieux** que l'historique (+0,052 [B8 +0,036 ; +0,069] et +0,060 [+0,044 ; +0,077]) ; le mélange régresse (−0,066 ; −0,077) ; R2 ne progresse pas et revient vers d'anciennes attaques (Table D ligne 2) ; coût R3 ≈ 2 × R2.

**Ce que la réplication peut et ne peut pas tester.** Le rapport signal sur erreur-type de HR1 est déjà de 18,5 (δ 1,4) et 28,9 (δ 1,6) : la chance d'une graine favorable est pratiquement exclue par la course elle-même ; la réplication protège surtout contre une erreur propre à une graine ou à un chemin de code, et donne une preuve procédurale (graine que personne n'a choisie, statistique recodée indépendamment). Pour HR0, la marge est plus mince (la borne haute de E8 est à 1,5 erreur-type de la frontière m au δ 1,4, à 1,7 au δ 1,6) : **probabilité de réplication ≈ 0,90** si la vérité est celle de la course (§ Seuil du brouillon de préenregistrement).

## 6. Ce qui, dans la course originale, pourrait avoir fait le résultat (réserves)

1. **La graine** — racines écrites au gel avant toute exécution, jamais employées avant la décision : aucun choix de graine sur résultat. Mais une seule graine : c'est l'objet de la réplication.
2. **La règle de lecture** — (a) la réfutation de HR0 passe par l'**équivalence à m = 0,02 près**, soit ≈ 17 % du niveau de V au δ 1,4 (V ≈ 0,12) et ≈ 30 % au δ 1,6 (V ≈ 0,065) : « ≈ » veut dire « pas d'avantage de plus de 0,02 », pas « aucune différence » ; la classe « ≈ » exige m > 0,0134 au δ 1,4 et m > 0,0133 au δ 1,6 (bornes hautes de E8), en deçà elle deviendrait « ? » ; (b) les verdicts de HR0, HR2 et HR3 étaient suspendus par le déclencheur 1 et ont été rendus **mécaniquement** après l'audit (R-976), sans document de lecture séparé ; (c) B2 est plus large que le Bonferroni exact pour deux tests (ses quantiles 0,00625 / 0,99375 sont ceux de quatre tests selon le commentaire de l'arène v4, l. 159–161) : conservateur, sans effet sur HR1.
3. **L'échelle et la conception** — c'est là qu'un mentor attaquera après la graine, et la réplication sur graine neuve **n'y répond pas** :
   - **capacité déployée** : R3 déploie un mélange aléatoire de jusqu'à 9 moniteurs (63 paramètres) contre un seul pour R2 ; « classe égale » ne vaut que par requête. Que la stratégie mixte d'équilibre batte un hyperplan pur face à un attaquant qui répond en dernier est attendu du théorème du minimax quand il n'y a pas de point-selle pur — le texte lui-même appelle HR1 « plomberie ». Au pilote de l'arène v4 (non opposable), des combinaisons **déterministes** des mêmes moniteurs battaient nettement le mélange (B − C3 = −0,19 / −0,14 ; B − D = −0,23 / −0,18 ; chiffres recoupés dans `argon-seul-convergence-v1/lecture-verifiee-avis-argon-convergence-v1.md` § 1.2) ;
   - **attaquant local** : standard et renforcé sont le même optimiseur local ; contre un mélange de 9 moniteurs, l'objectif de l'attaquant est plus multimodal, et un optimiseur local pourrait y sous-estimer l'exploitabilité **davantage** que contre un hyperplan unique, ce qui gonflerait HR1. L'attaquant indépendant de l'arène v4 (stratégie d'évolution, plus de départs) n'a été branché ni dans la course ni dans l'audit (audit § 9 : les défenses finales ne sont pas sérialisées). C'est **la menace la plus sérieuse non traitée** ;
   - **le monde** : d = 6, K = 3, T = 8, deux budgets δ **choisis sur le seul bras A = R2** (règle de recalibrage du v4 : là où l'historique détecte peu) ; les deux δ partagent la cible de chaque instance (corrélation entre δ du contraste R3 − R2 : 0,45 ; R0 − R2 : 0,20) : « aux deux δ » n'est pas deux confirmations indépendantes ;
   - **HR0** pourrait refléter un **plancher de la classe linéaire** : l'audit (§ 3) mesure une corrélation de V par tâche de 0,82 à 0,95 entre règles linéaires et un V de R0 atteint dès le premier attaquant léger ; « ne rien faire fait aussi bien » serait alors une propriété de l'hyperplan dans ce monde, non un constat général sur le réentraînement.
4. **Bruit de graine par règle dans la finale** (échantillons frais différents par règle) : bruit sans biais, effet ≤ 0,003 mesuré par l'audit (§ 2).

## 7. Conditions de lancement de la réplication (résumé ; détail dans le brouillon de préenregistrement)

1. Rapatrier dans cet arbre, depuis `origin/canal/session-depot-reprise-n67` (lecture de ref permise, aucune ref `donnees/*`), `docs/notes/convergence-defense-v1/`, le préenregistrement scellé et son compagnon, `diag/` et `runs/` du run original.
2. Écrire le code v3 (copie de v2 ; liste fermée de changements : racines dérivées par la règle D, identité, chemin de l'arène suivi par git, option de sérialisation des défenses finales) et ses essais, dont **un essai lent de non-régression** : v3 rejoue deux tâches de la course originale sur ses racines d'origine et rend les mêmes valeurs au bit.
3. Écrire et sceller l'implémentation indépendante de la statistique (autre agent, depuis la spécification) ; la valider sur la course originale (écart ≤ 10⁻⁹).
4. Contre-lecture du préenregistrement (R2), scellement, commit (le manifeste exige un arbre propre), GO de Lazar, une seule invocation (≈ 28 min).

## 8. Empreintes recalculées (sha256sum, 1er novembre 2026 ≈ 21:00 UTC)

```
d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d  prereg/preregistrement-regles-defense-convergence-v1.md (n67)
9f0dcf5e0d10fe93dd19c318f076728d62b64734161dc72b40a812a817340da3  docs/notes/convergence-defense-v1/regles-defense-v1/arene_regles_defense_v2.py (n67)
78d979ab76bbe4b3ad6b55be77bf2b745a4457940eb9cb4c16a3ee87ef324b81  docs/notes/convergence-defense-v1/regles-defense-v1/test_arene_regles_defense_v2.py (n67)
9977d7df7f87f081f3c89709c6f36ab2c3861cb06c972dffbabe0e777e9910f3  docs/notes/convergence-defense-v1/regles-defense-v1/gel-regles-defense-v2.md (n67)
70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61  brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/arene_melange_v4.py (cet arbre ; = donnees/argon-seul-convergence-v1/arene_melange_v4.py du manifeste)
d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b  diag/20261101-160323-regles-defense-convergence/resultats-regles-defense.json (n67)
18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42  diag/20261101-160323-regles-defense-convergence/analyse-regles-defense.json (n67)
36db58cfac9bfc4cf199ca5cdf74ac17ea24afab84b95ffd0aac945b922a6720  runs/20261101-160323-regles-defense-convergence/manifeste.json (n67)
767aa28fb8cee94a1a130c151d7ed4487985d8f4fb2efdcd7ab805efc59e4bcd  runs/20261101-160323-regles-defense-convergence/pids-travail.txt (n67)
24081eed65cebd8dd01d6e17ec76c5a6433d171da68ccbaa50657421cd7c4a23  lecture-course-regles-defense-v1.md (n67, deux copies identiques : docs/notes/…/regles-defense-v1/ et brouillons/…/convergence-resultats-v1/)
7e81d094868e0d9cd2c03b73b5ca80cd0cd028b717a8085e027182fb57bd9966  audit-trop-beau-course-regles-defense-v1.md (n67, deux copies identiques)
a277a5ba28e36c4a4042ef0905510ec9e1772954a5fe29dbd1a4eb7f49d92a77  docs/notes/convergence-defense-v1/formalisation-jeu-convergence-v1.md (n67)
c5ba88fc6ec874dce22bcc6fbb1d1ae8544cabd17ce36dfc6a0266722222f227  docs/notes/convergence-defense-v1/regles-defense-v1/contre-lecture-2-prereg-regles-defense-v3.md (n67)
8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e  prereg/gabarit-preregistrement-v1.md (cet arbre = n67)
```

Bibliothèque (cet arbre = n67 = bloc d'identité) : `gardes.py` `a83c48ce…`, `prereg.py` `3b2e3ee5…`, `scellement.py` `93beeb1c…`, `manifeste.py` `1a5c7464…`.
