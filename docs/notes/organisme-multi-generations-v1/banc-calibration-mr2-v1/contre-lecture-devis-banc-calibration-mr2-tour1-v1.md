# Contre-lecture du devis du banc de calibration MR-2 — tour 1 — v1

- **Lecteur** : modèle C, contre-lecteur neuf (R2) ; pièce écrite par le modèle A ; corrections par le modèle A.
- **Pièce lue en entier** : `devis-banc-calibration-mr2-v1.md`, empreinte `6172ae590c29901a040bd39804177a844e74b9f9f7589acf22b7b5e22ca942db` (égale à son compagnon).
- **Heures** (`date -u`) : début 2026-11-16 20:51:46Z ; fin : dernière ligne (6e section).

## Verdict : corrections (2 majeures, 5 mineures)

La conception est saine : le banc est bien une simulation sans appel de modèle, il joue ce que le texte scellé et le verdict demandent,
les chiffres de coût et de durée se recomptent, et aucun lancement n'est demandé. Il faut pourtant corriger deux omissions qui
pèsent sur les décisions de Lazar (condition de la course non remplie, arrêt contradictoire avec le dénominateur) et cinq imprécisions.

## 1. Fidélité au texte scellé et au verdict : tenue

- Verdict lu par `git show` sur `origin/verdict/pilote-mr2-v74-v14-v1` : issue P-2 sans réserve ; phrase « banc de 24 mondes de calibration (code v68 gelé) : P_CACHÉE := p_c ponctuel, P_VUE := 0,25 supposée ; la règle de garde de la conception v4 y décide de la course ; le banc rapporte aussi la règle aux deux bornes de l'intervalle (mesure, ne décide pas) » recopiée **mot pour mot** par la pièce ; `P_CACHEE_banc = 0,0`, `P_VUE_banc = 0,25` exacts ; x = 0 sur n = 14, intervalle [0 ; 0,043] exacts.
- Texte scellé relu (branche `prep/pilote-mr2-compte-organisme-v1`) : empreinte recalculée `8aa33014…` égale. « Le banc ne mesure rien sur les proposeurs » : présent (E-1). « Jamais réutilisés (ni au banc de 24 mondes, ni en test) » : présent ; la pièce en tire correctement un secret de calibration neuf.
- Recalcul de la borne haute : 1 − 0,025^(1/14) = 0,23163 ; 1 − (1 − 0,23163)^(1/6) = 0,04296 ; la pièce a raison de ne pas figer l'arrondi (0,042965 contre 0,043).
- Code : `monde_riche_v4.py` recalculé `4b165847…` égal ; ligne 42 `P_CACHEE, P_VUE = 0.02, 0.25` ; `course` lit `P_CACHEE` à chaque appel (ligne 223) ; `partie` tire les mondes de `cle("monde-mr1-v4-calibration-developpement", r)` (ligne 275) ; `resume` compte sur les mondes conformes (`garde * 2 >= len(ok)`) ; flux `oracle-v4`, `v4-gen`, `v4-juge`, `v4-mort` indexés par `w` : tout est exact. La pièce a raison que `partie` ne peut pas servir telle quelle.
- Règle de garde (conception v4 §3.1) et définitions §3.2 (dénominateur proposé « tous les mondes tirés », code sur les conformes, « aucun nouveau tirage de mondes de calibration » après échec) : recopiés fidèlement. « Calcul seul, aucune ligne de GO » : conception v4 §5, ligne 294, exact.
- Lecture de « code v68 gelé » : le texte scellé (ligne 534, bloc gelé ligne 572) place `monde_riche_v4.py` dans `orchestrator/mr2_v68/outils-v4/` ; la lecture « arbre v68 à v74 du pilote » est cohérente. Le brouillon 3 de la course (ordre D-2, règle de garde en dernier ; §16.1 point 5 : banc plus large) est bien un autre banc : question Q-B2 correctement posée (voir majeure 2).
- Lignes de GO citées (314, 315, 332, 333, 349 de `registres/go.md`), mot de Lazar R-3015 : verbatim exact.

## 2. Recompte du coût et de la durée

Pièce de dépense recalculée au commit `2f7acc1d` : `53c72308…` égale.

| contrôle | résultat |
|---|---|
| `fable52` 10,019552 / 4 | 2,504888 ✓ ; complets 10,019552 − 5,585992 = 4,433560 (2 appels) ; tronqués 5,585992 (2 appels, chiffre du verdict) |
| `opus55` 1,057336 / 4 | 0,264334 ✓ ; `argon` 2,47162 / 4 = 0,617905 ✓ ; `astra` 1,67175 / 4 = 0,417938 ✓ |
| durées du verdict | `fable52` 388,8 à 553,2, moyenne 470,6 ✓ ; `opus55` 36,4 à 109,4, moyenne 68,4 ✓ ; `argon` 38,3 à 96,0, moyenne 64,4 ✓ ; `astra` 34,4 à 80,1, moyenne 63,6 ✓ |
| machine du pilote | 1,5706 h × 0,052222 = 0,082018 ✓ (11:26:57Z à 13:01:11Z = 1 h 34 min 14 s) |
| total du pilote | 11,076888 + 4,301309 = 15,378197 ✓ |
| pire cas machine | 17 h × 0,17 = 2,89 ✓ (procédure v14, N1 ; l'offre elle-même est plafonnée à 0,15, soit 2,55) |
| durée attendue | 24 × 9,5 min = 3,8 h ✓ ; total 3,8 + 0,3 + 0,3 + 0,3 = 4,7 h, annoncé ≈ 5 h ✓ |
| durée au pire | 24 × 26,7 min = 10,7 h ✓ (8,9 min × 2 × 1,5 = 26,8) ; total 12,7 h ✓, sous la minuterie de 17 h (marge 4,3 h) |
| durées des 12 parties v4 | 3 min 40 s (monde 3) à 8 min 55 s (monde 4) ✓ par les fichiers `partie-v4-monde-*.json` ; 75,5 min / 12 = 6 min 17 s au journal ✓ (la somme des parties seules fait 5 min 44 s ; la différence est le coût de lancement des processus) ; 12 refus, mondes 4 et 11 à 3 refus ✓ |
| machine : 4 processeurs, 8 Go, 20 Go, 0,15 USD/h, numpy 900 s, minuterie 17 h | tous présents dans la procédure v14 ✓ |

Parts séparées : la pièce met correctement 0 USD sur crédits de Claude (aucun appel) et tout hors crédits ; plafond 0 USD par proposeur et cinq coupures écrites : tenu. Le devis ne tire des mesures par appel du pilote que p_c, l'intervalle et le prix horaire : tenu, et cela se vérifie dans les sections 2 et 5.

## 3. Corrections (couples « ancien → nouveau » ; chaque « ancien » figure une seule fois dans la pièce, vérifié)

### Majeures

**M1 — Liste d'arrêt contre dénominateur (section 6 point 1, section 7 point 5, Q-B3).** La liste d'arrêt à écrire contient « monde sans tirage conforme », alors que Q-B3 (a), recommandée, dit qu'un tel monde « ne garde rien » et compte au dénominateur. Les deux ne tiennent pas ensemble : si l'événement arrête le banc, Q-B3 n'a jamais d'objet. Et l'événement n'est pas rare : en v4, 12 refus pour 12 mondes, soit 0,5 par tirage ; la probabilité qu'un monde échoue 8 tirages est 0,5^8 = 0,004 ; sur 24 mondes, **≈ 9 %** qu'au moins un le soit (indépendance supposée), **≈ 33 %** si le taux de refus vrai est 0,6 (l'intervalle sur 12 sur 24 est large). Le risque n'est pas chiffré dans la pièce.

- Ancien : `(empreinte d'un module, nombre de parties différent de 24, monde sans tirage conforme, exception)`
  Nouveau : `(empreinte d'un module, nombre de parties différent de 24, exception ; un monde sans tirage conforme en 8 n'arrête pas le banc : il est compté selon Q-B3 et rapporté)`
- Ancien : `sous la borne de 8 par monde ; un monde sans tirage conforme pèse selon Q-B3.`
  Nouveau : `sous la borne de 8 par monde ; un monde sans tirage conforme pèse selon Q-B3. Probabilité qu'au moins un des 24 mondes n'en ait aucun : ≈ 9 % au taux de refus observé en v4 (12 refus pour 12 mondes, 0,5 par tirage, indépendance supposée), ≈ 33 % à 0,6 ; l'événement est donc à prévoir, non exceptionnel, et le préenregistrement le traite par Q-B3, sans arrêt.`

**M2 — Condition de la course non remplie sous Q-B2 (a) (section 9).** GO-2026-11-13-01 et -02 (échéance 2026-11-30) exigent « banc de calibration fait (n et seuils fixés par leurs règles) ». Un banc de la règle seule n'accomplit pas cette condition : la pièce le laisse entendre (« le reste du banc de la course se fera plus tard ») sans le dire à Lazar, et le défaut à 48 heures choisirait (a). Lazar doit savoir que (a) laisse la condition ouverte et que le banc plus large reste dû avant la course, à moins qu'il ne la lève.

- Ancien : `confiance 0,55. Défaut sous 48 heures : (a).`
  Nouveau : `confiance 0,55. Défaut sous 48 heures : (a). À savoir avant de choisir : sous (a), la condition « banc de calibration fait (n et seuils fixés par leurs règles) » de GO-2026-11-13-01 et -02 (échéance 2026-11-30) n'est pas remplie par ce banc ; le banc plus large reste dû avant la course, ou un mot de Lazar qui lève cette condition ; le défaut à 48 heures ne la lève pas, et je n'ai pas vérifié que le code v68 de la course existe.`

### Mineures

**m1 — Nombre de lignes du bloc gelé (section 2).** Le bloc gelé porte 13 lignes `orchestrator/mr2_v68/…` (lignes 562 à 574 du texte scellé ; le verdict dit aussi 13), dont deux ne servent pas au banc.
- Ancien : `(12 lignes `orchestrator/mr2_v68/…` du bloc gelé)`
  Nouveau : `(13 lignes `orchestrator/mr2_v68/…` du bloc gelé, dont `mesure_pilote_v4.py` et `seuil_pilote_v1.py`, qui n'entrent pas au banc)`

**m2 — « 0,30 » attendu : arrondi non dit, prix non borné (section 5).** 5 h × 0,052222 = 0,26, pas 0,30 ; et 0,052222 est le prix de l'offre du pilote, non garanti : à 0,15 USD/h (plafond de l'offre), 5 h coûtent 0,75.
- Ancien : `**0,30** (≈ 5 h à 0,052 USD/h, arrondi)`
  Nouveau : `**0,30** (≈ 5 h à 0,052 USD/h = 0,26, arrondi au-dessus ; à 0,15 USD/h, plafond de l'offre, 5 h coûteraient 0,75)`

**m3 — Coûts « chacun » (section 3).** Le verdict ne donne que les sommes (5,585992 pour les deux tronqués) ; 2,792996 et 2,216780 sont des moyennes par différence ou division ; les deux appels complets ont des durées différentes (388,8 s et 430,5 s) et ne coûtent pas le même prix.
- Ancien : `complets 2,216780 chacun ; tronqués 2,792996 chacun (5,585992 pour les deux)`
  Nouveau : `complets 2,216780 en moyenne (4,433560 pour les deux, par différence) ; tronqués 2,792996 en moyenne (5,585992 pour les deux)`

**m4 — Attente à la borne haute sans prédiction chiffrée (section 7 point 4).** Le texte scellé (modèle approché, section Prédiction) place la bascule de la règle à p_c = 0,034 (probabilité 0,5) et à 0,051 (probabilité 0,05). La passe à 0,0430 n'est donc pas acquise d'avance ; la pièce dit seulement que l'information y est. R1 exige une prédiction chiffrée avant le lancement.
- Ancien : `(permise à tort 0,27 si p vaut 0,051, à 14 appels)`
  Nouveau : `(permise à tort 0,27 si p vaut 0,051, à 14 appels) ; le modèle approché du texte scellé place la bascule de la règle à 0,034 (probabilité 0,5) et à 0,051 (probabilité 0,05) : la passe à 0,0430 n'est pas acquise d'avance, et le préenregistrement y écrit sa prédiction chiffrée (R1) et ce que devient un résultat sous 12 sur 24 à cette borne (information rapportée, ne décide pas)`

**m5 — Couplage des deux passes (section 6 point 2).** `course` tire `rng.random()` par composante inconnue ; en génération 1 les connus sont {K1} dans les deux passes, donc le flux est identique (et `_bruiter` consomme un flux indépendant de la taille de S : vérifié lignes 234-242 de `puissance_monde_riche_v1.py`). Dès la génération 2, les connus divergent et les flux aussi. La règle se lit après la génération 1 : la comparaison monde par monde y tient, mais pas au-delà.
- Ancien : `0,0430 consomment donc le même flux et se comparent monde par monde.`
  Nouveau : `0,0430 consomment donc le même flux en génération 1 (les connus y sont {K1} dans les deux passes) et se comparent monde par monde pour la règle, qui se lit après la génération 1 ; leurs flux divergent dès la génération 2.`

## 4. Remarques facultatives (aucune correction exigée)

1. La règle ne lit que la génération 1 et la variante sans masquage une seule génération ; `partie` joue pourtant 3 générations avec masquage et la part marginale. Le lanceur neuf pourrait ne jouer que ce que le préenregistrement décide, ce qui raccourcirait la durée. La pièce est prudente en gardant le temps de la partie entière ; à dire au préenregistrement.
2. La procédure v14 refuse le pilote réel s'il reste moins de 12 h 30 avant l'échéance. La procédure du banc devrait garder une garde équivalente (pire cas 12,7 h contre 17 h de minuterie).
3. La pièce de dépense a été lue en plus du verdict ; elle ne fait pas partie de la sortie du pilote (pièce de la mère, commit `2f7acc1d`) ; aucun écart.
4. Aucun identifiant de modèle de Claude dans la pièce (les noms de proposeurs du pilote sont permis) ; aucune clé ; aucun lancement ; empreintes et lignes de GO citées exactes ; empreinte « `e64458e8…` » du verdict : égale à la ligne de registre.

## 5. Points pour la session mère

1. **Condition de la course (M2)** : le banc de la règle seule ne remplit pas « banc de calibration fait (n et seuils fixés par leurs règles) » de GO-2026-11-13-01 et -02. Lazar doit le savoir avant Q-B2 ; le défaut à 48 heures ne le dit pas.
2. **Arrêt et dénominateur (M1)** : l'événement « monde sans tirage conforme » est probable (≈ 9 % à 33 % selon le taux de refus). Le préenregistrement doit choisir : compter (Q-B3) ou arrêter, pas les deux.
3. **Prédiction à la borne haute (m4)** : à écrire avant le lancement, elle fait partie de R1 ; le résultat à P_CACHÉE = 0 ne dira presque rien (R4 déjà écrit d'avance par la pièce, à garder).
4. **Prix de la machine** : 0,052 USD/h est celui du pilote ; la dépense au pire dépend de l'offre trouvée au moment de la création (0,15 au plus, 0,17 relu au plus).
5. Rien à signaler comme écart à un texte scellé : la pièce n'en change aucun.

## 6. Déclaration d'incident

Aucun incident de ma main. Lu : la pièce, le verdict (par `git show`, sans fetch), le texte scellé du pilote et la procédure v14 (par `git show` sur branches distantes déjà présentes), la pièce de dépense, la conception v4, le code `monde_riche_v4.py`, `puissance_monde_riche_v1.py` (lignes de `_bruiter`), les fichiers `partie-v4-monde-*.json` et le journal v4 (heures et refus seulement), le brouillon 3 (sections citées), `registres/go.md` et `registres/decisions.md` (lignes citées). Rien d'ouvert de la sortie du pilote au-delà du verdict ; aucune branche `calcul/pilote-mr2-v74-entree-*` ; rien de 7a, 7b, T0.6, T0.7, P3-bis, étape B bis, bras d'attaque ; aucune clé lue, ni `env` ni `printenv` ; aucune dépense, machine ni appel externe ; aucun fichier existant modifié ; aucun commit.

Fin : 2026-11-16T20:56:37Z (`date -u`).
