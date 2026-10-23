BASSIN_MATH: Sonde TD-parcimonieuse à coût d'évasion (STP-CE)

**1. Riposte — acceptations sans lissage**
- *Rang 0 / pointeur nul* : **accepté intégralement**. L'artefact était vide ; aucune réfutation algébrique n'est possible contre un fait de livraison. Je ne réécris pas l'histoire : l'époque 2 est un échec de production, pas une base.
- *Fuite d'instruction E1* : **accepté**. Toute « complétion » ultérieure ne lirait que le socle. Parade : la proposition ci-dessous est explicitement dérivée du socle et s'en déclare dépendante ; sa validité ne tient qu'à E0/E1.
- *Monoculture* : **accepté**, mais partiellement : la corrélation d'angles morts est une hypothèse non testée. Je l'inscris comme contrôle (voir E3).
- *Kerckhoffs à coût nul* : **accepté**. Un pipeline qui compte `texte=''` comme « évalué » est exploitable à coût zéro (cf. *Astra*, OpenAI oct. 2026, référence à vérifier). Parade intégrée.
- *Contrôle re-forward thinking plafonné* : **accepté** tel quel, intégré comme E2.

**2. Opérateur corrigé**
Soit $h_t^{(\ell)}$ le flux résiduel, $S$ l'ensemble parcimonieux des *Dopamine Neurons* (couches 5–22, < 1 % des neurones, Xu et al. `arXiv:2602.00986v2`, référence à vérifier). Au lieu de la sonde dense $w^\top h_t$ (plancher `P3`) :

$$\hat{s}