# Vérification de la v4 du paquet de publication sur l'évasion sous filtrage pendant l'entraînement après pré-entraînement — v1

- **Contre-lecteur** : le même sous-agent Opus 5.5 qui a vérifié les v3. Je n'ai écrit aucune pièce. Aucun fichier du dépôt n'a été modifié (`git status --short` vide à la fin). Les scripts n'ont tourné que sur des copies, avec `python3 -I`.
- **Objet** : branche `papier-d/evasion-post-entrainement-v1`, commit `c033c218`. P désigne `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1`.

## Verdict

**Fidèle, avec trois réserves mineures et sans défaut bloquant ni majeur.**

- **Défauts de la v3 et reports** : les quatre défauts B-1 à B-4 sont corrigés. Les cinq reports sont faits ; le compagnon d'empreinte de Carbon est désigné, et la décision sur l'ancien fichier reste à la mère.
- **Hypothèses H1 à H3** : elles ont disparu des quatre pièces publiques. Les ouvertures neuves ne revendiquent ni nécessité ni suffisance.
- **Phrases ajoutées** : elles sont vraies.
- **Régressions** : aucune. Les tables sont identiques à celles de la v2 et de la variante B, et les dix corrections de l'audit sont toujours portées.
- **Test interne** : `test_mort_halberstadt_v3.py` ne peut réécrire aucun fichier existant, donc aucun JSON scellé.
- **Table v4** : exacte sur les quatorze cases sondées, avec une seule affirmation exagérée (défaut 2).

## Points vérifiés

1. **Défauts B-1 à B-4 et les cinq reports**
   - **B-1, la suffisance de H1 à H3** : corrigé. Le paragraphe est retiré du billet (l. 92) et du manuscrit (l. 211). Erratum 2, l. 9-13.
   - **B-2, le « < 1 »** : corrigé. Le point 4(a) du manuscrit dit « equals one only if $\beta_v = 0$ ». La proposition dit « strictly below one when $\beta_v > 0$ » ; c'est exact pour la masse furtive absolue limite. Billet, § 3, point 3.
   - **B-3, le chiffre de la niche** : corrigé. Le texte, la légende et la remarque donnent 0,827382, ainsi que le billet. La cellule 0,827379 de la ligne en gras de la table 3 est correcte : c'est $\pi_B(h)$ au seuil arrondi.
   - **B-4, l'antériorité dans le commentaire** : corrigé. Le commentaire a sa dernière phrase avec Price, Robertson, Fisher, et Korbak, Perez et Buckley 2022.
   - **Reports 1 à 5** :
     - l'ouverture neuve de la section 3 est en place ;
     - le compagnon `.v2.sha256` de Carbon est désigné ;
     - la phrase sur Korbak et al. 2022 est ajoutée ;
     - la formule « for every η … can be small » est reprise ;
     - « $\pi_A \propto \beta\,\pi_{no}$ » figure dans la remarque du manuscrit, au § 2 du billet, au point 2 du commentaire et dans le README.
2. **H1 à H3 et l'ouverture neuve.**
   - **Absence de H1 à H3** : aucune occurrence de « (H1) », « H2 », « H3 » ni « arises in particular » dans le billet, le commentaire, le manuscrit `.tex` et son PDF (sondé par `pdftotext`), ni dans le README.
   - **Contre-exemple invoqué par l'ouverture, recalculé** : $\beta_{\text{boucle}} = (0{,}1 ; 0{,}5 ; 0{,}9)$ et $\beta_{\text{audit}} = (0{,}1 ; 0{,}95 ; 0{,}45)$. La covariance vaut $+0{,}0467$.
   - **Trajectoire de la survie à l'audit sous la pénalité**, en fonction de $k$ :
     - à $k = 2$, elle monte à $0{,}543$ ;
     - à $k = 10$, elle redescend à $0{,}459$ ;
     - quand $k \to \infty$, elle tend vers $0{,}45$, sous la valeur de base $0{,}5$.
   - **Conclusion** : la phrase « does not by itself make audit survival rise at high pressure » est vraie.
3. **Phrases ajoutées.**
   - **$\pi_A \propto \beta\,\pi_{no}$** : vrai. On a $\beta e^{\eta R}\pi_0/Z_A = \beta \cdot (e^{\eta R}\pi_0/Z_{no}) \cdot Z_{no}/Z_A$. Tirer selon $\pi_{no}$, puis rejeter avec la probabilité $1-\beta$ et retirer jusqu'à l'acceptation, donne exactement cette loi, pourvu que $\mathbb{E}_{\pi_{no}}\beta > 0$.
   - **Part furtive constante en $\eta$ sous A, à récompenses égales** : vrai. La cote vaut $\beta_f p_f e^{\eta\Delta R}/(\beta_v p_v e^{\eta\Delta R}) = \beta_f p_f/(\beta_v p_v)$, indépendante de $\eta$. Le script v4 le vérifie en rationnels exacts pour quatre valeurs de $E = e^{\eta\Delta R}$, par des assertions.
4. **Absence de régression.**
   - **Tables du manuscrit** : les 112 valeurs ont la même empreinte que la v2 et la variante B (`450cacdb…`).
   - **Tables du billet** : même empreinte que la v2 et la variante B (`9af53501…`).
   - **Sortie du script** : le JSON v4 est identique à celui de la variante B pour toutes les rubriques sauf le nom du script ; je l'ai comparé par programme.
   - **Reproduction** : le script v4, lancé sur une copie, rend `exemples-verifies-papier-v4.json` octet pour octet, avec et sans `--out`, et refuse d'écraser.
   - **Dix corrections de l'audit** : le diff par mots entre la variante B et la v4 ne touche que les passages des défauts B-1 à B-4 et des reports. Les dix corrections sont donc intactes.
   - **Empreintes** : les huit compagnons `.sha256` des fichiers v4 concordent. Le PDF fait 11 pages et correspond au `.tex`.
5. **`test_mort_halberstadt_v3.py`.**
   - **Sans argument** : arrêt sur le message d'usage.
   - **Chemin existant** : « refus d'écraser ».
   - **Conséquence** : il ne peut réécrire aucun JSON scellé, puisque tous existent.
   - **Six essais** : ils passent, et la sortie est identique octet pour octet à `resultats-test-mort-halberstadt-v2.json`.
6. **Table v4, sondée sur quatorze cases.**
   - **Cases sondées** : les lignes 1 à 9 du tableau des changements, plus les quatre vérifications annoncées. Toutes sont exactes, sauf la ligne 8 (défaut 2).

## Défauts

1. **Mineur — la non-suffisance sous la pénalité est affirmée sans être exhibée.**
   - *Où* : billet v4, l. 92 ; manuscrit v4, l. 211.
   - *Constat* : la non-suffisance d'une covariance positive est affirmée, mais le contre-exemple ne figure dans aucune pièce publique. Il n'est que dans l'erratum 2, qui est interne. Le script ne le recalcule pas, alors que le billet et le README annoncent qu'il « recomputes every number » et « checks the counterexamples ».
   - *Ambiguïté* : la tournure « does not by itself make … rise » peut se lire « ne fait jamais monter », ce qui serait faux à faible pression (0,543 à $k = 2$).
   - *Correction proposée* : écrire « need not make audit survival rise at high pressure ». Ajouter l'exemple à la remarque « Placement is not covariance » : (0,1 ; 0,5 ; 0,9) et (0,1 ; 0,95 ; 0,45), avec 0,5 → 0,543 à $k = 2$, puis → 0,459 à $k = 10$. L'ajouter aussi au script, avec une covariance exacte $7/150$.
2. **Mineur — `test_mort_halberstadt_v3.py` peut écrire à côté de lui-même.**
   - *Constat* : il n'écrase rien, mais il peut créer un fichier neuf à côté de lui-même. Sur une copie, l'argument `resultats-test-mort-halberstadt-v1.json`, passé depuis son dossier, a été accepté. La table v4, ligne 8, affirme pourtant « aucune écriture à côté du script ». Sa docstring (l. 12) parle encore de « la v2 » et cite « Dilemme Rejet-Pénalité » et « 0 / 10 000 » (l. 10-11), sans que ce soit public.
   - *Correction proposée* : retirer de la table « aucune écriture à côté du script », ou refuser `sortie.parent == dossier du script` dans une v4 du test.
3. **Mineur, cosmétique — rubrique du JSON v4 et nouveaux contrôles.**
   - *Constat* : dans le JSON v4, la rubrique s'appelle encore `exact_checks_v3`. Les deux contrôles nouveaux (rejet unique à l'inférence, part constante) n'existent que comme assertions et n'apparaissent pas dans la sortie.
   - *Correction proposée* : renommer la rubrique en `exact_checks` et y consigner les deux contrôles.

## Réserves inchangées

- **Références à vérifier sur PDF (R7)** avant diffusion : Price, Robertson, Fisher, Korbak et al. 2022 et 2025, Bailey et al. 2024.
- **Compagnon de Carbon** : l'ancien, à chemin étranger, reste en place ; décision de la mère.
- **Pièces hors du paquet** : l'avis d'opportunité et la feuille de route v2 gardent encore « classification exhaustive en 3 régimes ».

## Commandes lancées (lecture ou copies dans le bloc-notes)

```
git log --oneline -6 ; git status --short
cat -n correctif-1-variante-b-v1.md table-corrections-audit-v4.md erratum-2-…md
git diff --no-index --word-diff=plain <variante B v3> <v4>   (billet, commentaire, README, manuscrit, script)
grep -n -E "(H1)|H2|H3|arises in particular|requires|sufficient|necessary|exhaustive|…" <quatre pièces v4>
cp verifier_exemples_papier_v4.py → bloc-notes ; python3 -I … > so.json ; --out o.json (×2 : refus) ; cmp avec le JSON scellé
python3 -I -c "comparaison des JSON v4 et variante B par rubrique"
awk/grep des valeurs des tables + md5sum (manuscrit et billet v4)
sha256sum -c <compagnons v4, erratum 2, test v3>
cp test_mort_halberstadt_v3.py → bloc-notes ; sans argument ; r.json ; r.json (refus) ; nom à côté du script (accepté)
pdftotext main-v4.pdf + grep ; pdfinfo
calcul à la main du contre-exemple sous la pénalité (déjà fait dans la vérification des v3)
```
