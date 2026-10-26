# Points de la boucle extérieure du pilote 4 à trancher par Lazar — v1

Écrit par conv-audit le 2026-10-26 à 05:39:44 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
Cette pièce répond au constat CLB3-04 de la vérification de la v3 de la boucle extérieure
(`rapport-verification-boucle-exterieure-v3.md`, `1a7873e269529e09de2b1ade0f4ca723383647b2bcc19966f7849e2d5af9fa6a`) :
chaque point est posé au format de décision. Le protocole v3 de la boucle la cite au lieu de reposer les points lui-même.
Aucun score ni aucun fait de course n'est lu ici.

Format de chaque point : décision en une phrase ; enjeu ; options, avec avantage et inconvénient ; recommandation et
confiance ; défaut sous 48 heures (jamais pour une dépense) ; moment où la réponse est nécessaire.

## Point 1 — Famille de modèle du contre-lecteur

- **Décision** : le contre-lecteur, l'agent chargé de casser exprès les verdicts de l'analyste, est-il de la même famille
  de modèle que l'analyste ?
- **Enjeu** : un contre-lecteur de la même famille peut partager les angles morts de l'analyste et laisser passer un faux
  verdict. Une autre famille ne peut pas être Gemini (les organismes sont des Gemini, et rien de la lecture ne leur est
  servi) : il faudrait un modèle d'un autre fournisseur, donc un compte, une clé et une dépense, par session-depot.
- **Options** :
  - (a) même famille : un sous-agent Claude neuf, au modèle écrit dans son brief. Avantage : aucune dépense, tout de suite.
    Inconvénient : ses erreurs peuvent aller dans le même sens que celles de l'analyste.
  - (b) famille différente, d'un autre fournisseur que Google, appelée par session-depot. Avantage : des erreurs moins
    corrélées. Inconvénient : un compte et une dépense (deux nœuds de décision), du délai, et un brief à porter sur un
    autre outil.
  - (c) (a) partout, et (b) en plus sur la ronde 1 seulement. Avantage : mesure une fois la corrélation des deux familles.
    Inconvénient : le compte et la dépense de (b), et deux contre-lectures à concilier.
- **Recommandation** : (a), confiance moyenne. La partie A du contre-lecteur s'écrit déjà à l'aveugle et s'empreinte
  avant toute lecture de l'analyse, ce qui coupe l'ancrage. Et pendant la boucle, seuls des faits mécaniques motivent une
  correction (registre v3, § 0.6), ce qui laisse peu de place aux goûts propres d'une famille.
- **Défaut sous 48 heures** : (a). La synthèse « neuron explorer » (décision 2) n'en donnait pas ; j'en donne un, parce
  que (a) ne dépense rien et que, sans défaut, aucune proposition ne sort d'une ronde avant ta réponse.
- **Nécessaire** : avant la contre-lecture de la ronde 1.

## Point 2 — Graines de plus

Posé à part ce matin, après la synthèse du tour « graines » (`synthese-collisionneur-graines-v1.md`,
`b8cdeb5c18335b1c94417ca2f820404a07b68309550a5fe11ec52bc8c3a2df2a`) : (a) trois graines par course ; (b) un contrôle bon
marché d'abord (organisme figé rejoué), puis (a) peut-être ; (c) aucune graine sur la v3, le bruit entre graines mesuré
dans le pilote (b). Recommandation : (c), confiance moyenne. Défaut : aucun (dépense). La retenue de lecture tient
jusqu'à ta réponse, et la boucle ne démarre pas avant.

## Point 3 — Plafond de dépense des relances

- **Décision** : combien la boucle peut-elle dépenser en relances, c'est-à-dire en courses nouvelles d'un objet corrigé ?
- **Enjeu** : une relance est une course entière (31,57 USD constatés pour la course M, R-494 ; 75 USD au pire). Chaque
  relance relit la même part `test` de 36 tâches, et chaque lecture l'use un peu plus (le sur-ajustement adaptatif de ta
  question de 05:06, heure de Paris). Sans plafond, chaque relance attend ton mot à son GO.
- **Options** :
  - (a) une relance au plus (75 USD). Avantage : vérifie une correction. Inconvénient : une seconde correction attend un
    mot nouveau.
  - (b) deux relances (150 USD), le maximum que le protocole permet par objet. Avantage : deux corrections vérifiées.
    Inconvénient : deux lectures de plus de la même part `test`, et le double de dépense.
  - (c) aucune relance dans ce pilote. Avantage : rien n'est dépensé. Inconvénient : les corrections attendent le pilote 5
    et ses tâches fraîches (N-049) ; la boucle ne vérifie rien elle-même.
- **Recommandation** : (a), confiance moyenne : une relance suffit à voir si une correction agit sur le fait mécanique
  qu'elle visait, et la vraie vérification se fait sur des tâches fraîches.
- **Défaut** : aucun (dépense).
- **Nécessaire** : au premier devis de relance, pas avant.

## Point 4 — Symétrie d'effort avant le pilote décisif (b)

- **Décision** : le pilote (b) compare-t-il la v6.2.1 et la v5.3 telles que livrées, ou la v6.2.1 corrigée par la boucle ?
- **Enjeu** : la v5.3 ne court pas dans ce pilote et ne reçoit aucune ronde ; la v6.2.1 peut en recevoir jusqu'à trois. Si
  (b) prend la v6.2.1 corrigée, la comparaison mesure aussi l'effort de correction, et sa forme penche d'un côté (R3).
- **Options** (protocole v2, § 8) :
  - (a) les deux objets tels que livrés (`7ea3270` ; `4ecba58`). Avantage : la comparaison ne penche pas par sa forme ; les
    hypothèses de (b) restent telles qu'écrites. Inconvénient : les corrections de la boucle n'entrent pas dans (b) ;
    elles attendent un palier suivant.
  - (b) la v6.2.1 corrigée contre la v5.3 livrée, l'inégalité d'effort déclarée par le texte de (b) avant son scellement.
    Avantage : (b) profite des corrections. Inconvénient : la question devient « l'organisme complexe corrigé contre
    l'organisme simple livré », une comparaison penchée par construction.
  - (c) la v5.3 reçoit autant de rondes que la v6.2.1. Avantage : la symétrie rétablie. Inconvénient : des courses de la
    v5.3, donc une dépense, et du délai avant (b).
- **Recommandation** : (a), confiance moyenne.
- **Défaut sous 48 heures** : (a), qui ne dépense rien et ne change aucune hypothèse.
- **Nécessaire** : avant l'écriture du texte du pilote (b).

## Point 5 — Ordre des courses M et S pour la correction de la ronde 1 (tranché par conv-audit, pour information)

Le texte v5 interdit toute comparaison entre les deux courses, verdicts des agents compris. La v3 de la boucle mettait
pourtant en regard, fiche par fiche, les verdicts de M et de S pour décider d'une correction (constat CLB3-02). Règle
écrite avant toute lecture, qui la remplace : **la course M motive la correction de la ronde 1 ; la course S ne la motive
que si aucune fiche de M n'en motive ; les verdicts de S sont rapportés à part, jamais mis en regard de ceux de M.** La
correction se propose après la lecture de M ; le correcteur n'attend la course S que si M ne motive rien. Le point
« correction après M sans attendre S » n'a donc plus à t'être posé. Tu peux reprendre cette règle, par exemple pour
permettre de mettre en regard les libellés mécaniques des deux courses afin de s'abstenir, jamais afin d'attribuer.

## Point 6 — Question servie par une relance

- **Décision** : une relance tourne-t-elle sur la question M ou sur la question S ?
- **Enjeu** : la question est servie à la génération 1 et peut orienter les réécritures de l'organisme ; une relance ne
  vérifie une correction que si elle tourne dans les conditions qui l'ont motivée.
- **Options** :
  - (a) la question de la course qui a motivé la correction (M sous la règle du point 5, S sinon). Avantage : des
    conditions identiques. Inconvénient : la question de la relance n'est connue qu'après la lecture.
  - (b) toujours M. Avantage : la continuité avec le second pilote. Inconvénient : change les conditions quand S a motivé
    la correction.
  - (c) toujours S. Avantage : ta question la plus récente (R-492). Inconvénient : change les conditions quand M a motivé
    la correction, le cas le plus probable sous le point 5.
- **Recommandation** : (a), confiance moyenne à haute.
- **Défaut** : aucun (dépense).
- **Nécessaire** : au GO de la relance.

## Point 7 — Seuils 0,01 (stagnation) et 0,03 (retour arrière) de la v6.2.1

- **Décision** : garde-t-on ces deux seuils de l'objet, ou les change-t-on, hors de toute course ?
- **Enjeu** : ils sont de l'ordre du poids d'une tâche dans le score rendu à l'organisme (entre 1/72 et 1/12, registre v3,
  § 0.5, calcul sans score). La mutation et le retour arrière se déclenchent donc sur des écarts d'une tâche, que le bruit
  produit seul. Ce point se pose avant toute lecture, indépendamment de ce que montreront les courses ; changer un seuil
  est une correction de l'objet, donc une ronde et une relance.
- **Options** :
  - (a) garder. Avantage : rien ne change, l'objet de (b) reste tel que livré. Inconvénient : les deux mécanismes
    réagissent au bruit ; c'est rapporté, pas corrigé.
  - (b) un seuil au pas de la mesure, ou une fenêtre sur deux différences. Avantage : moins de déclenchements sur le
    bruit. Inconvénient : une ronde et une dépense, et le bruit doit être connu pour régler le seuil.
  - (c) la mutation désactivée en génération notée. Avantage : plus de réaction au bruit pendant la notation.
    Inconvénient : retire un mécanisme que la v6.2.1 revendique.
- **Recommandation** : (a) pour le pilote 4 et le pilote (b) ; la question revient au texte du pilote 5, où les tâches
  fraîches rendent le bruit mesurable. Confiance moyenne.
- **Défaut sous 48 heures** : (a) ; garder ne dépense rien, et tout changement attend ton mot.
- **Nécessaire** : avant une ronde 2, pas avant.

## Ce que j'envoie à Lazar maintenant

Le point 1 seulement : il est le seul nécessaire au démarrage de la ronde 1. Le point 2 est déjà posé ; le point 5 est
une information ; les points 3, 4, 6 et 7 lui seront posés au moment écrit sous chacun, en citant cette pièce.
