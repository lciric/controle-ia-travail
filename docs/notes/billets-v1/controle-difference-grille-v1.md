# Contrôle de la différence, avant gel, de la grille des gestes de rédaction des billets — rapport v1

Contrôleur neuf (sous-agent), mandat `mandat-controle-difference-grille-v1.md` (`a6c57bfb5123…`, empreinte vérifiée). Le 2026-11-18. La grille n'a pas été modifiée. Grille contrôlée : `grille-gestes-v1.md`, `e9d058c9586b739daacbb67aeb7ce0c00010a545c63625e9c4cdbe0231c73ac2` (identique à l'attendue). Brouillon 3 : `7cc5a181ca8b…` (compagnon vérifié).

## Verdict

**À geler après ces trois couples exacts** (section « Couples »). Rien d'interdit n'a changé ; les trois couples corrigent chacun un passage qui, lu à la lettre, déborde ce que la section 10.5 permet (ou chiffre trop exactement). Après les couples, la grille change d'empreinte : la vérification des citations, l'essai d'analyse (qui cite l'empreinte de la grille) et le fichier des différences sont à rejouer sur la grille corrigée avant scellement.

## Point 1 — le `diff -u` et les trois titres

- Rejeu de `diff -u grille-gestes-v1-brouillon3.md grille-gestes-v1.md` : 250 lignes, 22 morceaux ; **identique** à celui du fichier des différences (hors les deux lignes d'horodatage, qui portent la date des fichiers).
- Les 26 changements annoncés correspondent aux 22 morceaux : titre, statut, 16 lignes de gestes, deux morceaux de 4.2, 4.5, début de 5, puce de 5.3, ligne de 5.5, section 12 et pièces.
- Chacune des 16 lignes de gestes changées (G02, G03, G04, G07, G10, G11, G12, G13, G14, G16, G17, G18, G19, G20, G23, G25) est **la ligne « Cas limites » seule, à laquelle on a ajouté à la fin** une phrase commençant par « Après l'essai pilote » (contrôle par programme : l'ancienne ligne est un préfixe strict de la nouvelle ; aucune autre ligne du geste n'a bougé).
- Paliers recalculés par moi sur les deux dépôts (désaccords sur l'indicateur ; doutes) avec la règle de 10.5 : **0 écart** avec `pilote-analyse-v1.json` ; 17 désaccords au total ; neuf gestes à « inchangé » (G01, G05, G06, G08, G09, G15, G21, G22, G24), seize à « préciser un cas limite permis » (G12, G16, G18, G20 par désaccords ; les douze autres par doutes) ; aucun geste à quatre désaccords ou plus. Les seize gestes changés sont exactement les seize du palier ; les neuf autres sont intacts à la lettre.
- Les autres changements se rattachent à (b) ou (c) : 4.2 (nom du script, masquage renforcé, limites du masquage), 4.5 et début de 5 (noms de script), puce « Aveugle » de 5.3 (description « sans billets reconnus ou devinés »), ligne de 5.5 (limite de l'aveugle), titre, statut, section 12, pièces. Aucun changement hors de ces trois titres.

## Point 2 — ce que 10.5 et 10.6 interdisent : inchangé

Contrôles par programme :
- Les 25 gestes lus par `lire_grille` (question, modalités, indicateur, analyse, consigne) : **égaux** entre brouillon 3 et version.
- Sections identiques mot pour mot : 0, 1, 5.1, 5.2, 5.4, 4.1, 4.3, 4.4, 6, 7, 8 (règle du gabarit), 9, 10 (dont 10.5 et 10.6), 11, tout le bloc B (objections). Section 5.3 identique hors la puce « Aveugle » (qui garde la phrase de sensibilité d'origine et ajoute la description) : plan, seuil de 0,60, prévalence 10 % et 90 %, Holm, puissance, graines (`17963430407690202368587404665739133625`, `spawn(4)`, `spawn(28)`), tout inchangé. Section 5.5 identique hors la seule ligne de l'aveugle.
- `analyser_codage_v2.py` contre `analyser_codage_v3.py` (`72a8e488…` contre `4a8b3440…`, compagnon vérifié) : la différence de source est **le commentaire d'en-tête et un bloc de dix lignes** (`description_sans_reconnus_ni_devines`), placé après le calcul des consignes, de la fiabilité et de la sensibilité ; il ne modifie aucune donnée lue ensuite. Constantes (`ENTROPIE`, `B`, `SEUIL_KAPPA`, `ENSEMBLES`) identiques.
- Rejeu de l'essai synthétique v2 (sur brouillon 3) et v3 (sur la version) dans `/tmp` : **sortie identique hors la clé ajoutée et les chemins d'entrée** (ensembles 62/23, 44/13, 58/20, 42/11 ; m = 20 ; fiabilité, consignes, objections). Le rejeu v2 est identique à l'essai scellé v2.
- Réserve technique (hors grille) : le rejeu v3 **n'est pas identique octet pour octet à `essai-analyse-synthetique-v3.json`**, et seulement sur le bloc « aveugle » synthétique (paris justes, description). Cause : `synthetique()` tire les paris par `list(PARIS)`, et `PARIS` est un ensemble de chaînes (`controler_depot_v1.py`, ligne 23) ; l'ordre dépend de la graine de hachage de Python, donc de l'exécution. Vérifié avec `PYTHONHASHSEED=1` et `2` : résultats différents entre eux. Défaut ancien (présent dans la version 2), sans effet sur aucune décision ni sur le mode réel ; il enfreint seulement la reproductibilité de l'essai (R9). 10.5 permet de corriger toute faute de script par nouvelle version (`sorted(PARIS)`) ; à décider par la session mère, il ne bloque pas le gel de la grille.

## Point 3 — les seize phrases « Après l'essai pilote »

Origine vérifiée : les désaccords et doutes des deux dépôts contiennent bien les situations visées (par exemple G10 : « particularly harmful » ; G12 : variantes des auteurs contre chiffre d'un article antérieur ; G16 : « do not differentiate » et « not a variational vs deterministic issue » ; G19 : lien entre cause et contrôle, « may mainly caused » ; G20 : « we suggest pooling », accessibilité, abandon ; G25 : « I'd love to hear your thoughts »). Aucune ne vient d'une préférence nouvelle.
Treize phrases précisent un cas limite sans toucher modalité, indicateur ni sens (G02, G04, G07, G11, G12, G13, G14, G16, G17, G18, G20, G23, G25). Trois appellent une retouche :
1. **G10** : « la phrase doit dire *ce que le résultat change* pour la sûreté… » est plus étroit que la règle, qui demande une phrase reliant « le résultat **ou la question étudiée** » à la sûreté avec un mot de la liste. Telle quelle, la phrase écarte des billets que la règle compte : elle redéfinit l'indicateur `en-tête`.
2. **G03** : « un billet qui reproduit un effet et montre en même temps qu'il exige des contrôles ou s'accompagne d'une dégradation → `mixte` » ne garde pas la condition de la règle (« les auteurs mettent en avant **à égalité** un oui et un non »). Lue à la lettre, tout billet positif assorti d'une réserve devient `mixte` : elle élargit la modalité.
3. Section 4.2 (point 4 plus bas) : décompte présenté comme total alors qu'il porte sur une liste fixe de 25 noms.
Observations sans couple : G19 ajoute une condition de proximité (« même paragraphe, ou renvoi explicite ») que la règle ne dit pas, mais elle opérationnalise « lui répond » (le désaccord réel du pilote portait là-dessus) et ne contredit pas « avant ou après, dans n'importe quel ordre » ; je la laisse, la session mère peut en juger autrement. G11 (capture d'invite et de réponse → `autre-figure`) est cohérent avec la convention « des auteurs » de la section 1.

## Point 4 — masquage renforcé

- Rejeu de `mesurer_traces_masquage_v1.py` sur les 58 copies de développement (dossiers de travail sous `/tmp`, supprimés) : **sortie identique à `traces-masquage-dev-v1.json`** (`f126354e…`). Décomptes confirmés : hôtes de liens identifiants 48 billets (379 liens) → 0 ; hôte du forum voisin 15 billets (96) → 0 ; lignes d'auteurs 5 billets (7) → 0 ; parties de noms d'auteurs 4 → 5 billets ; prénoms de tiers masqués par erreur 7 → 2 billets ; organisations 39 sur 58 (27 sur 36 bien notés, 12 sur 22 appariés) avant et après ; marqueur `[AUTEUR]` 22 → 21 billets (17 sur 36 bien notés et 4 sur 22 appariés après). Borne : minimum et médiane 250 mots réels, 0 borne dans un marqueur, 0 billet trop court.
- Les cinq parties de noms restées, regardées dans leur contexte : trois prénoms de tiers homonymes gardés à dessein (liste d'auteurs d'un autre article), deux noms d'auteurs absents ou écrits autrement au manifeste. C'est ce que la grille écrit.
- Script v3 contre v2 : la différence ne porte que sur le masquage (parties dès trois lettres, lignes d'auteurs, hôtes) et le numéro de version ; les deux appels, les refus et la borne de 250 mots sont inchangés. Gardes rejouées sur v3 : tenue à l'écart sans `--go` → refus avant toute lecture (code 2) ; `--go` mal formé → refus ; passe 2 sans les deux dépôts et la grille → refus. Pas de `--go` valide essayé : cela aurait lu la tenue à l'écart.
- Limites écrites avec décomptes (4.2 « Ce qui ne peut pas être masqué ») : oui, organisations, marqueur d'auteur, noms réels des pseudonymes, chercheurs cités, titre, présentations de soi, notes d'édition, revue annuelle, longueur, mémoire des codeurs. Retouche : le décompte « 39 sur 58 » est celui d'une liste fixe de 25 organisations (`mesurer_traces_masquage_v1.py`) ; c'est un minimum, pas un total (couple 3). Observation : l'essai des gardes scellé (`essai-copies-neutres-dev-v2.json`) porte sur le script v2 ; aucun essai scellé pour v3 (mes rejeux ne le remplacent pas).

## Point 5 — citations

Rejeu de `verifier_citations_v3.py` (avec la liste pilote, les marquages et l'essai v3) : **sortie identique à `verification-citations-version-v1.json`** (`616cf99a…`). 125 citations vérifiées, 0 échec, 0 problème de structure, essai conforme (cite l'empreinte de la grille), 42 billets cités en A et B (le champ « références distinctes » en compte 43 parce qu'il inclut un titre cité autrement ; sans conséquence). Intersection des billets cités avec les douze du pilote et avec les deux billets marqués : **vide** ; aucun des quinze identifiants n'apparaît dans la grille.
Réserve : les formules entre guillemets des phrases « Après l'essai pilote » (37 formules) ne portent pas d'identifiant et ne sont pas vérifiées. Quatorze se retrouvent mot pour mot dans les copies du pilote (par exemple « finds systematic defects », « very well-aligned », « it's not a variational vs deterministic issue », « like most people »), d'autres en sont proches. La section 12 le dit (« schémas courts, certaines reprises des copies pilotes ; ce ne sont pas des exemples de la grille »). Ce ne sont pas des exemples au sens du format de la section 1 ni du vérificateur ; je ne les corrige pas. À savoir : 10.5 parle d'un exemple « tiré des billets de développement non pilotes ».

## Réserves sans couple

- La phrase de 5.5 « si les paris justes de la tenue dépassent nettement la part des appariés et des bien notés, toute consigne est à lire comme… » fixe une lecture conditionnelle avec un seuil non chiffré (« nettement »). Elle reste dans le titre (b) et ne change aucune règle de décision ; mais une lecture qui dépend d'un seuil laissé libre n'est pas gelée au sens du préenregistrement. Décision laissée à la session mère.
- Les noms de modèles des deux codeurs (« Sonnet 5.5 », « Fable 5.2 ») en 5.5 et 12 ne se vérifient dans aucune pièce que j'avais le droit d'ouvrir ; les chiffres de l'aveugle, eux, sont confirmés : classes des douze billets (2 bien notés, 10 appariés peu notés) ; C1 7 justes, 1 faux, 4 « ne sait pas », 1 reconnu ; C2 12 justes, 5 reconnus.

## Couples (passage d'origine entier → passage corrigé)

Chaque couple se trouve une seule fois dans `grille-gestes-v1.md` ; appliqués sur une copie, ils laissent les 25 gestes lus par `lire_grille` égaux à ceux de la version.

**Couple 1 (G10, ligne « Cas limites »)**
Origine : `un mot de la liste qui qualifie le comportement étudié sans le relier à un risque pour la sûreté des systèmes (« two biases that seem particularly harmful ») ne compte pas : la phrase doit dire ce que le résultat change pour la sûreté, la surveillance, l'audit ou le contrôle.`
Corrigé : `un mot de la liste qui qualifie le comportement étudié sans le relier à un risque pour la sûreté des systèmes (« two biases that seem particularly harmful ») ne compte pas : la phrase doit relier le résultat ou la question étudiée à la sûreté, à la surveillance, à l'audit ou au contrôle des systèmes.`

**Couple 2 (G03, ligne « Cas limites »)**
Origine : `un billet qui reproduit un effet et montre en même temps qu'il exige des contrôles ou s'accompagne d'une dégradation → `mixte`.`
Corrigé : `un billet qui reproduit un effet et dont les auteurs mettent en avant, à égalité avec lui, qu'il exige des contrôles ou s'accompagne d'une dégradation → `mixte` ; si cette réserve est secondaire → `positif`.`

**Couple 3 (section 4.2, « Ce qui ne peut pas être masqué par programme »)**
Origine : `(39 billets de développement sur 58, 27 des 36 bien notés et 12 des 22 appariés ; ils ne sont pas au manifeste`
Corrigé : `(au moins 39 billets de développement sur 58, 27 des 36 bien notés et 12 des 22 appariés, décomptés sur une liste fixe de 25 noms ; ils ne sont pas au manifeste`

## Lectures hors mandat

Aucune. Le manifeste v2 a été lu par les scripts du mandat (classes, appariement), jamais ouvert à la main sur la tenue à l'écart ; aucun texte de la tenue à l'écart, rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/`. Aucune requête réseau. Copies de travail dans `/tmp/ctrl`, supprimées.
