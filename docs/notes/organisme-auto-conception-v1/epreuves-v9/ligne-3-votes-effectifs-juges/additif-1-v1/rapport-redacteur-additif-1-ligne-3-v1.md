# Rapport du rédacteur — additif 1 au préenregistrement de la ligne 3 (version 7) — v1

Pièce de travail (classe C). Écrite le 2026-11-20 (temps universel), sur le mandat `mandat-redacteur-additif-1-ligne-3-points-a-e-v1.md` (`98cd555e809aa3385ba6a5c7bb2a0a50f16da6c714ea76cefc421947fa894972`, égale à son compagnon).

## Verdict

L'additif est écrit : `additif-1-preenregistrement-ligne-3-votes-effectifs-juges-v7-v1.md` (empreinte dans son compagnon). Il donne une règle écrite d'avance pour A, B, C, D, E, les silences 1 et 2, F à J et les quatorze autres choix déclarés du développeur. Il ne change aucune hypothèse, prédiction, seuil ni critère gelé. Le code v2 suit déjà toutes les règles, sauf deux ajouts à l'alarme, faits après les tirages. Deux nœuds pour Lazar, tous deux sur l'ajout éventuel d'un critère gelé ; sans son mot, l'additif s'applique tel quel et ne change rien au texte.

## Sources (chemin, empreinte recalculée)

Dossier de la ligne (LIGNE) : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/`.

| pièce | sha256 |
|---|---|
| texte, version 7 : `git show origin/main:prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md`, après `git fetch origin main` (tête `732d73379643f10f1398282fa1e178d49bce6fe2`) | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` (commence par `4e3680d9`, comme attendu) |
| devis, version 7 : `git show origin/main:prereg/organisme-auto-conception-v9/devis-ligne-3-etage-payant-v7.md` (extrait, non lu) | `382ea448db3ba8f5d69df1f3566165d1028ad8aceddfc8c538c522b838f58270` |
| `LIGNE/code-etage-1-v1/rapport-developpeur-code-etage-1-ligne-3-v1.md` | `ee8cd1b4504a0d55f64b6da3006a336a732be50bf0e8b7796df2c050e11eefdb` |
| `LIGNE/code-etage-1-v2/rapport-developpeur-code-etage-1-ligne-3-v2.md` | `995bd5f48494e9a241fcb5c7824c59105d0ddf0c0f8cc95702e942bdcf58903c` |
| `LIGNE/code-etage-1-v1/contre-lecture-v1/contre-lecture-code-etage-1-ligne-3-v1.md` | `3aed6849c76a4ed421207470e4a6b8a45fcecf6a8ef5325a5203c84fda2f85ff` |
| `LIGNE/code-etage-1-v2/verification-corrections-code-etage-1-ligne-3-v1.md` | `09e462b9f42ccd7d11828c2f630a2cd6a6d205f2e1e15948c1a62b0664506186` |
| `LIGNE/code-etage-1-v2/banc_juges_scriptes_ligne_3_v2.py` | `ffc330839de048891bdbd323b8c19c04289386f9379492440a13e7df4c09b5b3` |
| `LIGNE/calcul_predictions_ligne_3_v2.py` (lignes du bras R seulement, par recherche dans ce seul fichier) | `802d4dd26d66ead35326cef2d77c8a55e12c11b89a4ddbce4d9a115927428dc6` |
| `LIGNE/calcul-predictions-ligne-3-v2.json` (empreinte seule, non ouvert) | `2cf1eba7e4fce530e14b4045574f7c4ff97fdb94367aef740c5c274a14eae724` |

Lu dans le texte : de l'en-tête à « Voisins du catalogue », et l'annexe A. Non relus : la section « Contre-lecture » et les six différentiels. Lu dans le code v2 : graines et grille (lignes 1 à 245), estimateur et rééchantillonnage (400 à 530), bras et cellule d'agrégation (620 à 820), monde de puissance et ρ′ − ρ (825 à 1045), alarme, configuration, critères et exécution (1220 à 1525). Non lus dans le code : les lois d'erreur (245 à 400), le double rendu et la garde de cadrage (1045 à 1220), la fin du fichier.

## Choix, point par point, et pourquoi

- **A.** Je reprends le monde du code (loi 1 emboîtée, taux 0,20, 100 témoins sans partage) : il reproduit ce que l'étage 2 lit (ρ sur les premiers rendus, ρ′ entre deux rendus, sur 100 témoins sans étalonnage) et le taux de la règle du nombre de témoins. J'ajoute ce que le texte laissait flou : le chiffre qui répond est la puissance « des deux juges à la fois » (le rang 2 exige les deux), et ce chiffre n'entre dans aucune règle gelée. La loi 3 n'y est pas jouée : la difficulté y est commune à toutes les lectures, donc ρ′ = ρ.
- **B.** Le compte des cellules du texte (« quatre sous la loi 1, deux sous la loi 3 » contre l'unanimité) et le calcul de référence (aucun ρ′ hors du bras R) fixent qu'une cellule de ces mondes est une valeur de ρ seule : ρ′ y est un paramètre à fixer, non une dimension. Je fixe ρ′ = 0, la valeur où le bras R aide le moins les autres comparaisons sous Holm, donc celle que « la plus basse » du texte retiendrait. C'est un raisonnement, non un calcul ; je le dis dans l'additif. Je tranche ce point comme une question de conception, sur le précédent de la question Q7 du texte (« la cellule où se lit la puissance qui décide »), tranchée par le rédacteur de la version 4. Si la mère y voit un nœud, le format est plus bas (nœud éventuel).
- **C.** Juge 1 dans la grille, juge 2 dans le monde de puissance : sans effet sur aucune loi là où les juges ont le même profil. Seul le profil inégal en dépend (le juge 1 y est le plus exact) ; l'additif impose la mention. Je n'ai pas demandé de jouer le bras R pour chaque juge : ce serait changer les tirages pour une lecture descriptive.
- **D.** La composition du code est reprise ligne à ligne. Deux limites sont écrites : un seul sens de bascule de sévérité, pas de collège. Un seul juge est la lecture la plus étroite : le texte n'écrit ni taux ni corrélation d'un second juge pour ce bras.
- **E.** Je n'ajoute pas de ligne à la table gelée. La règle écrit ce qui est déjà gelé (pas d'étage 2, aucune dépense, par la règle du nombre de témoins et la liste d'arrêt), le libellé du cas, et un audit de symétrie pour toute issue non monotone. Elle précise aussi que les cellules de la règle sont à deux juges (la loi 3 n'est jouée qu'à deux juges).
- **Silence 1.** Les deux lectures sont rendues sous deux noms ; aucune n'entre dans un seuil, donc rendre les deux ne laisse aucun choix après lecture.
- **Silence 2.** Aucun mot pour la carte : il faudrait des seuils neufs. L'alarme se lit contre P6, à la lettre de sa clause de réfutation, sur des comptes entiers, clause par clause et par m. Je demande au code de calculer ces deux clauses comme aide, plutôt que de les laisser à la main.
- **F à J.** F : l'aide mécanique est gardée, l'agent neuf applique lui-même les critères et compare. G et I : sans objet pour le texte. H : les essais se font contre la version 2 du calcul, mêmes valeurs. J : la durée n'est ni critère ni garde ; j'ai ajouté la règle d'une exécution interrompue avant d'écrire son résultat (relance à l'identique, déclarée), que le texte ne disait pas et qu'une exécution de près de deux heures en un seul processus rend utile.
- **Autres choix (1 à 9, 11, 12, 15, 16, 18, et C2).** Repris comme règles, sur la foi de la contre-lecture du code ; je n'ai vérifié dans le code que les choix 1, 2 et 3. Le choix 3 est plus strict que la formule du texte à cinq juges ; il ne touche aucune cellule qui décide.

## Ce que le code doit changer (pour un développeur d'un autre modèle)

1. `cellule_alarme` : ajouter la part (b) « parmi toutes les suites en alarme » et les quatre comptes.
2. Critères mécaniques : ajouter, par m, les deux clauses de P6 sur comptes entiers, le mot de P6, et la mention « mesurée, sans mot » pour la carte.

Aucun tirage, aucune graine, aucune mesure existante ne change ; le développeur le montre sur la racine des essais.

## Nœuds pour Lazar

**Nœud 1 — table gelée de l'estimateur (point E).**
- *Décision.* Ajouter ou non, avant l'étage 1, une ligne à la table gelée pour l'issue « la tolérance tient à n = 50 et à aucun n plus grand ».
- *Enjeu.* Sans ligne, si l'issue se présente, son mot se décide après lecture. Ses effets, eux, sont déjà gelés : pas d'étage 2, aucune dépense.
- *Option (a) — ne rien ajouter.* La règle E de l'additif s'applique : « cas non prévu », audit de symétrie, retour à Lazar si le cas se présente. Avantage : aucun critère gelé ne change, aucune version neuve ; le texte prédit que la tolérance manque à n = 50 (P1), le cas est donc peu probable. Inconvénient : un mot resterait à donner après lecture.
- *Option (b) — élargir la troisième ligne* (« ne tient à aucun n de 100 à 400 » : « non »). Avantage : tout est écrit d'avance. Inconvénient : change un critère gelé ; version 8 du texte, vérification, scellement, avant tout calcul.
- *Option (c) — ajouter une ligne « non concluant : résultat non monotone ».* Avantage : écrit d'avance, sans lire un « non » dans un résultat suspect. Inconvénient : même coût que (b), et un mot de plus dans la table.
- *Recommandation.* (a), confiance 0,7.
- *Défaut.* Aucun : c'est un changement de critère gelé. Sans mot de Lazar, rien n'est ajouté, ce qui revient à (a).

**Nœud 2 — mot de la carte de l'alarme (silence 2).**
- *Décision.* Donner ou non à la carte `fcbf4a2dd1a57` une règle de mot (« tient », « réfuté », « sans prise ») à l'étage 1.
- *Enjeu.* Le texte promet trois mots possibles par bras, mais n'écrit aucune règle pour cette carte. Une règle demande des seuils neufs sur la détection et le délai.
- *Option (a) — aucun mot.* L'alarme est mesurée et lue contre la prédiction P6 seulement (règle de l'additif). Avantage : aucun critère neuf ; l'alarme ne porte rien du « oui » de la ligne, et changer réellement un juge est déjà un nœud (réserve 11). Inconvénient : la carte sort de l'étage 1 sans mot.
- *Option (b) — écrire une règle de mot.* Avantage : la carte est lue comme les autres. Inconvénient : seuils choisis par nous, critère gelé neuf ; version 8, vérification, scellement, avant tout calcul.
- *Recommandation.* (a), confiance 0,75.
- *Défaut.* Aucun : c'est un critère gelé neuf. Sans mot de Lazar, aucun mot n'est donné, ce qui revient à (a).

**Nœud éventuel — ρ′ du bras R hors de son monde (point B), seulement si la mère ne le tient pas pour une question de conception.**
- *Décision.* Fixer ρ′ = 0 pour le bras R dans les mondes de puissance plantés pour l'unanimité et pour le juge seul.
- *Enjeu.* Ce choix entre dans la puissance qui décide, donc dans la possibilité d'un « oui » à l'étage 2.
- *Option (a) — ρ′ = 0.* Avantage : le compte des cellules du texte est tenu ; c'est, par raisonnement, la valeur la plus basse, celle que le texte fait décider ; aucun changement de code. Inconvénient : raisonnement non calculé.
- *Option (b) — jouer ρ′ = 0 ; 0,5 ; 0,9 et garder la plus basse.* Avantage : « la plus basse » est mesurée, non raisonnée. Inconvénient : trois fois plus de cellules que le compte du texte dans ces mondes, tirages changés, code à reprendre.
- *Recommandation.* (a), confiance 0,75.
- *Défaut sous 48 heures.* (a).

## Ce qui reste à faire, hors de mon mandat

- Contre-lecture de l'additif par un agent neuf d'un autre modèle, qui ne l'a pas écrit (règle R2), avant le scellement par la mère.
- Les deux ajouts au code, leur vérification, puis l'additif de code.

## Ce que je n'ai pas fait

- Aucun calcul de l'étage 1, aucun chronométrage, aucun tirage, aucun essai lancé ; aucune graine dérivée.
- Aucune écriture dans le dépôt, aucun commit ; seul `git fetch origin main` a touché le dépôt (références distantes).
- Aucune commande sous `archives-reponses-modeles/` ni sous `/root/.claude/` ; aucun appel à un fournisseur ; aucune dépense.
- Je n'ai pas ajouté de mesure neuve à la puissance de ρ′ − ρ (par exemple la part de lectures « nul ou négatif » à écart planté positif) : ce serait une mesure que le texte ne demande pas.

## Refus et écarts

Aucun refus d'outil ni de classifieur. Un écart de forme, sans effet : le devis a été extrait dans mon dossier comme le mandat le demande, mais je ne l'ai pas lu, aucun point ne le touchant. Les deux extraits (`preenregistrement-…-v7.md`, `devis-…-v7.md`) restent dans mon dossier, sans compagnon : ce ne sont pas des pièces rendues.

Rédacteur neuf, modèle F.
