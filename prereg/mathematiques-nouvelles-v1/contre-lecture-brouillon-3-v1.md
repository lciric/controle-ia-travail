# Contre-lecture du brouillon 3 du préenregistrement du pilote « oracles plantés » — v1

- Nature : contre-lecture R2, pièce de classe A. Contre-lecteur : un Opus 5.5 neuf (`claude-opus-5-5`), qui n'a écrit ni ce préenregistrement, ni le plan, ni le code. Date : 2026-11-22. Dépense : 0 USD. Aucun appel de modèle, aucun réseau. Aucun fichier existant modifié.
- Pièce relue : `prereg/mathematiques-nouvelles-v1/preenregistrement-pilote-generation-v1-brouillon-3.md`, `e33d7bec1f9c606d0cac96836e3748a02cc50444bcde689165e1280d32b655bb` (scellement vérifié « OK »). Les numéros de ligne renvoient à ce fichier.
- Pièces lues, toutes vérifiées « OK » par `controle_ia.scellement verifier` :
  - la provenance `LISEZMOI-brouillon-3-et-devis-v3-v1.md` (`77c9fbf9…`) ;
  - le devis v3 `devis-pilote-generation-v3-brouillon.md` (`5c8a0f68…`) ;
  - le rejeu du devis : `calculs-v3/` (script `5d2b9d8a…`, sortie `efcbc21f…`, note des écarts `60ba28c2…`) ;
  - le brouillon 1 (`7f04e367…`) et le gabarit `prereg/gabarit-preregistrement-v1.md` ;
  - l'erratum 1 du plan (`1827b680…`) ;
  - les notes du concepteur `notes-au-directeur-fable-v1.md` et `-v2.md` ;
  - pour le code : la note de choix v6 (`7c996b82…`), le rapport des essais R5 v6 (`0e6b4338…`) et la vérification `verification-corrections-lot-b1-v5.md` (`045030e2…`). Dans `src/controle_ia/oracles_plantes_v6/` (commit `35ac9e10738ccaac486ec9b9684fe70441f6371a`), seuls `forme_seule.mesurer` et l'appel au registre dans `rejeu.py` ont été lus.
  - En appui : § 3.2 de la note du pilier (lignes 200 à 212) et lignes 80 à 97 du code R du score apparié (`5248271a…`).
- Rien n'a été lu des fichiers interdits (« consigne-privee », « conception-ii-b », « verite », « rendu », « scores », `matiere-premiere/`, `quarantaine/`, `archives-reponses-modeles/`), ni d'une autre branche.

## Sortie du validateur

`controle_ia.prereg.problemes` sur le brouillon 3 :

```
- section vide ou à remplir : Plan d'analyse
- section vide ou à remplir : Liste d'arrêt
- section vide ou à remplir : Contre-lecture
```

Le validateur ne nomme pas les autres blancs : COMMIT-CODE (en-tête, hors section) et ANTÉRIORITÉ (section non exigée). Il les verrait seulement une fois ces trois sections remplies. Il ne verra jamais CONSIGNES, SCRIPT-ANALYSE ni la date (« à porter au scellement »), qui ne portent pas le marqueur (remarque 17).

## Verdict

Le brouillon 3 **n'est pas scellable en l'état**, indépendamment de ses blancs. Je compte **6 remarques bloquantes**, **13 à corriger** et **8 mineures**.

Le fait nouveau pèse sur tout le reste. L'aire du classifieur de style qui fait foi est au-dessus de 0,75 sur les 42 racines d'essai (de 0,939 à 0,982). Sur la banque réelle, la branche « aire > 0,75 » de H3 est donc connue d'avance, à quelques chances près. Or c'est la branche que le texte définit le moins bien : aucun seuil, et une comparaison gagnée par S par construction.

## Remarques

### 1. Sous la branche « aire > 0,75 », H3 n'a ni seuil ni critère réfutable, et sa seule affirmation est acquise à S par construction — bloquante

- **Lieu** : § Seuil, lignes 105 à 107 ; table, ligne 195 ; schéma de sortie, ligne 230.
- **Preuve**
  - La ligne 107 dit « H3 n'affirme que sur les contre-exemples vérifiés (critères gelés) ». Aucun critère sur les contre-exemples vérifiés n'est gelé : ni seuil, ni intervalle, ni règle de verdict. Les intervalles de P5 (ligne 49) sont des prédictions, pas des critères.
  - La ligne 195 rend affirmable « S produit des contre-exemples vérifiés sur telle part des faux, N aucun par construction ». « Telle part » n'est pas chiffrée. « N aucun par construction » rend la comparaison gagnée d'avance, de signe connu (R3) : le run ne peut pas montrer le contraire.
  - Le schéma de sortie n'est fixé que pour S (ligne 230). Si N peut écrire des instances dans sa réponse, « aucun par construction » est faux. Si N ne le peut pas, la comparaison n'a pas de sens.
  - La note du code v6 (ligne 68) et le rapport R5 v6 (ligne 33) mesurent l'aire qui fait foi au-dessus de 0,75 sur les 42 racines : cette branche est celle qui sera lue.
- **Correction proposée** (à écrire par le concepteur ; les valeurs entre crochets sont à fixer par lui, avant toute donnée)
  - Donner à N le même schéma de sortie que S (`verdict`, `contre_exemples`, `raison`) et vérifier ses instances par T6, chez le conteneur de confiance, comme celles de S.
  - Remplacer la ligne 107 par : « Au-dessus : la course a lieu. H3 se lit alors sur v_b, la part des 75 faux où le bras b rend au moins une instance vérifiée par T6, b ∈ {S, N}. Δ_v = v_S − v_N est apparié et se lit par le même score, aux mêmes valeurs critiques. « S ajoute en preuve » si S_v(0) ≥ 2,2504. « S produit des contre-exemples vérifiés » si la borne basse de Clopper–Pearson de v_S est ≥ [0,30]. « S n'en produit pas assez » si sa borne haute est < [0,30]. Sinon non concluant. Les verdicts déclarés (r_b, φ_b, Δ) passent en description. »
  - Remplacer la ligne 195 par la ligne correspondante de la table, sans « N aucun par construction ».

### 2. La table de H3 ne dit pas quelles lignes valent dans quelle branche d'aire, et deux lignes deviennent vides de sens sous la branche haute — bloquante

- **Lieu** : table, lignes 193 à 197 ; ligne 104.
- **Preuve**
  - Seule la ligne 193 porte « aire ≤ 0,75 », et seule la ligne 195 porte « aire > 0,75 ». Les lignes 194, 196 et 197 ne disent pas leur branche. Or « S n'ajoute pas δ » (ligne 196) et « borne haute de φ_S > 0,10 » (ligne 197) lisent les verdicts déclarés, que la ligne 107 renvoie en description.
  - Sous la règle « S ne tue que par contre-exemple vérifié » (ligne 194 ; sensibilité, ligne 170), φ_S est nul par construction : aucune instance d'un énoncé vrai jusqu'à 3N ne passe T6. Le critère « φ_S ≤ 0,10 » y est donc vide.
  - « rappel sur les pièges non porté par des contre-exemples vérifiés » (ligne 194) n'est pas chiffré : quelle part des pièges déclarés « faux » doit être sans instance vérifiée ?
- **Correction proposée**
  - Ajouter une colonne « branche d'aire » à chaque ligne de H3 (« ≤ 0,75 », « > 0,75 », « les deux »).
  - Ligne 197 : « H3, aire ≤ 0,75 : borne haute de φ_S > 0,10 | S non utilisable comme filtre | rapporté en tête ».
  - Ligne 194 : « … mais moins de [la moitié] des pièges déclarés « faux » par S portent une instance vérifiée par T6 ».
  - Ajouter : « Sous la règle « S ne tue que par contre-exemple vérifié », φ_S = 0 par construction ; il n'est pas lu. »

### 3. Le seuil d'emploi 0,75 est en attente d'une décision prise après la mesure, et la mesure n'est pas au dépôt — bloquante

- **Lieu** : ligne 105 ; notes au directeur v2, lignes 30 à 33 et 46.
- **Preuve**
  - Le seuil a été écrit avant la mesure (« Je n'ai pas éprouvé que la version 6 passe sous 0,75 »). La décision du directeur, elle, viendra après : l'aire est connue sur 42 racines d'essai, de 0,939 à 0,982.
  - Un seuil relevé au-dessus de 0,982 ferait lire H3 « comme écrit » par une décision prise en connaissant l'instrument. Ce n'est pas un résultat de course, mais c'est un critère de lecture fixé après coup (R1).
  - Les chiffres 0,939 à 0,982 viennent de `balayage_v6.py` et `v6-aires.json` « du bloc-notes », hors dépôt (rapport R5 v6, ligne 33) : ils ne renvoient à aucun chemin ni à aucune empreinte (R6).
- **Correction proposée**
  - Verser au dépôt, scellés, `balayage_v6.py`, `v6-aires.json` et leur sortie (R-3661, R6), avant que la décision ne les cite.
  - Porter la décision au texte avant le scellement, sous l'une de deux formes :
    - (a) garder 0,75, et écrire : « Sur les 42 racines d'essai, l'aire qui fait foi va de 0,939 à 0,982 (chemin, empreinte). La branche « aire > 0,75 » est attendue. Les critères de la remarque 1 sont la lecture principale de H3. » ;
    - (b) une version 7 des gabarits (pièges à borne naturelle), et un rejeu avant le scellement.
  - Tout autre seuil doit être motivé sans renvoi aux valeurs mesurées, et dit fixé après leur lecture.

### 4. Les verdicts de H1, l'hypothèse primaire, se recouvrent, l'un d'eux manque à la table, et le niveau annoncé est faux — bloquante

- **Lieu** : lignes 95 à 97, 109, 189 à 191 et 272.
- **Preuve**
  - « Confirmé » exige trois conditions « pour une configuration au moins ». « Réfuté » s'écrit « borne haute < 0,25, ou retrouvées < 1,0 pour les deux », sans dire si la borne haute est celle d'une configuration ou des deux. Lue pour une seule, une issue (configuration A confirmée, configuration B de borne haute < 0,25) est à la fois confirmée et réfutée.
  - La condition « battre la base « grammaire aléatoire » d'au moins 0,15 en précision » (ligne 272) n'est ni dans le § Seuil ni dans la table. Elle n'a pas d'estimateur : est-ce la différence ponctuelle, ou une borne ?
  - « H1 seule primaire, à 0,05 unilatéral » (ligne 109) est faux deux fois. La borne basse à 90 % est comparée à 0,15, non à 0,25 : elle n'établit pas « précision ≥ 0,25 » à 0,05. Deux configurations donnent deux chances de confirmer : le niveau d'ensemble peut aller jusqu'à 0,10.
  - « Retrouvées ≥ 2,0 » est ponctuel, sans intervalle (ligne 95). Pour la configuration à deux familles, la ligne 78 ne dit pas si les vérités distinctes s'unissent entre les deux proposeurs.
- **Correction proposée**
  - Lignes 95 à 97 : « « utilisable » si, pour une configuration au moins, la précision est ≥ 0,25, sa borne basse ≥ 0,15, les retrouvées par monde ≥ 2,0, et la précision dépasse celle de la base « grammaire aléatoire » d'au moins 0,15 (différence ponctuelle). « Non utilisable » si, pour les deux configurations, la borne haute de la précision est < 0,25 ou les retrouvées sont < 1,0. Sinon non concluant. »
  - Porter la même rédaction dans la table, lignes 189 et 190.
  - Ligne 109 : « H1 seule primaire. La règle de confirmation est descriptive, à deux configurations, sans niveau d'erreur nominal. Aucune correction entre hypothèses ; le rapport le dit. »
  - Ligne 78 : « pour la configuration à deux familles, une vérité est retrouvée si l'un des deux proposeurs la retrouve ».

### 5. La graine racine est un blanc à remplir avant le scellement, alors que les clés et la banque doivent être tirées après — bloquante

- **Lieu** : ligne 171 (« SeedSequence(À REMPLIR : GRAINE-RACINE) ») ; lignes 117, 183 et 304 ; « Pièces à remplir », ligne 301.
- **Preuve**
  - Le validateur refuse tout « À REMPLIR » : remplir ce blanc mettrait la valeur dans le texte avant le scellement.
  - Avec la racine connue, quiconque tient le code v6 calcule la banque, les clés et l'aire de style avant le scellement. Il pourrait choisir sa racine, y compris pour la branche de H3.
  - Cela contredit trois phrases du texte : « Clés. Tirées après le scellement » (ligne 117), « La même commande retire une racine » (ligne 183) et « [consignes] scellées avant le tirage de la graine » (ligne 304). Le brouillon 1 disait « tirée au scellement et inscrite au manifeste » (ligne 67).
  - La source du tirage n'est pas dite.
- **Correction proposée**
  - Ligne 171 : « Racine `numpy.random.SeedSequence(r)`, r entier de 128 bits tiré par `secrets.randbits(128)` dans la commande qui scelle ce texte, après le calcul de son empreinte. r et l'empreinte du texte scellé vont au manifeste. r n'est jamais écrit dans ce texte. »
  - Retirer GRAINE-RACINE de la ligne 301.

### 6. Mal défini, le faux « connu » de H4 punirait une réponse juste — bloquante pour la lecture de H4, à corriger pour le scellement si H4 sort des affirmations

- **Lieu** : lignes 27, 54, 85, 108 et 199.
- **Preuve**
  - Les vérités plantées sont, par gabarit, des instances de théorèmes connus : Scheffé, Le Cam, Fréchet, Markov, Cassini, addition, duplication (ligne 248). Un juge qui étiquette « connu » l'instance d'une identité de Cassini a raison sur le théorème ; il est pourtant compté en faux « connu ».
  - « Neufs par construction » (ligne 27) n'est vrai que du texte exact. La note du pilier, § 3.2 (lignes 211 et 212), dit que les mondes plantés « ne servent donc pas à mesurer le juge de nouveauté ».
  - Les 20 énoncés de mondes ne sont pas désignés : ni leur strate, ni leur tirage (aucun enfant de graine).
  - « Faux « connu » ≤ 0,10 » ne dit pas s'il s'agit d'un taux ponctuel ou d'une borne. Sur 20 items, une borne haute ≤ 0,10 est impossible : 0 sur 20 donne déjà 0,168.
  - Les effectifs des strates « célèbre » et « obscure » des 40 connus ne sont pas fixés, alors que P6 les compare. « Pièces lues » n'est pas défini : on ne sait pas ce que le juge reçoit.
- **Correction proposée**
  - « Les 20 énoncés de mondes sont tirés par l'enfant [7] parmi les faux tôt, les pièges et les vérités à littéral tiré (gabarits F1-c, F1-d, F2-c, F2-d, F3-d). Ils ne comprennent aucune vérité structurelle. « Connu » y est faux seulement si le juge cite une référence à l'énoncé lui-même, et non au théorème dont il est une instance. Le seuil est un taux ponctuel : au plus 2 sur 20. »
  - Fixer les strates à 20 « célèbres » et 20 « obscurs ».
  - Renvoyer la définition des pièces servies au juge aux CONSIGNES, nommées ici.

### 7. H2 : l'unité de la différence, le « coût apparié », le k du vote et le seuil en cas d'ex æquo sont indéfinis — à corriger

- **Lieu** : lignes 25, 43, 79 et 98.
- **Preuve**
  - « Différence par monde Y_multi(w) − Y_témoin(w), à 24 propositions par configuration » (ligne 79) ne dit pas si Y compte des retrouvées ou des retrouvées par dollar. H2 parle « par dollar » ; le brouillon 1 disait « en nombre de vérités retrouvées ».
  - « Coût apparié » est faux jusqu'au 30 novembre. À l'attendu, une configuration à deux familles coûte 12 × 0,10 + 12 × 0,05 = 1,80 par monde, le témoin 24 × 0,10 = 2,40 (devis v3, § 2).
  - « Vote à k » : k n'est donné nulle part, ni ce que le vote choisit.
  - Avec des ex æquo, il reste n < 12 mondes, et « au moins 10 sur 12 » devient ambigu : 10 sur 11 donne un niveau de 0,0059 ; avec 9 mondes, le seuil ne peut pas être atteint.
  - P4 (ligne 43) ne dit pas si le « rapport des rendements » est un rapport de sommes ou une moyenne de rapports par monde.
- **Correction proposée**
  - Ligne 79 : « Y_c(w) = retrouvées de la configuration c au monde w / dollars mesurés de c au monde w ».
  - Ligne 98 : « Sur les n mondes sans ex æquo, « deux familles supérieures » si les différences positives atteignent le plus petit k tel que P(Binomiale(n, 1/2) ≥ k) ≤ 0,025 (k = 10 pour n = 12, 10 pour n = 11, 9 pour n = 10, 8 pour n = 9, 8 pour n = 8). Symétrique pour le témoin. »
  - Remplacer « coût apparié » par « propositions appariées (24) ; coût mesuré », et définir k.
  - P4 : « rapport des sommes sur les 12 mondes ».

### 8. L'état initial du registre de lignée de la course n'est pas dit ; une mort par héritage peut lire la clé, ou dépendre de l'ordre des blocs — à corriger

- **Lieu** : lignes 65 et 154 ; code, `rejeu.py` lignes 135 et 136.
- **Preuve**
  - Au rejeu, la banque plantée passe par un registre. Les pièges y meurent par T6, avec un témoin dans ]N .. 3N], pris de la clé. La vérification v5 (§ 3) écrit : « Le piège tué par T6 transmet toujours sa mort aux huit reformulations. »
  - Si le registre « unique » de la course (ligne 154) part de celui du rejeu, une proposition égale à un piège meurt par héritage d'une instance de la clé. Elle sort alors du numérateur de la précision, au lieu d'y compter comme vraie-bornée.
  - Si le registre reçoit les morts de S par `appliquer_t6` (ligne 154), le sort d'une proposition dépend de l'ordre des blocs : S passe-t-il avant ou après les proposeurs sur ce monde ?
- **Correction proposée** : ajouter à la ligne 154 : « Le registre de la course part vide. Il ne reçoit que les morts des propositions des proposeurs et du témoin, et la base « grammaire aléatoire » tient le sien. Les morts que S établit sur la sous-banque vont à un registre à part, qui ne se transmet pas aux propositions. Les comptes de mort par héritage sont rapportés par source. »

### 9. La réserve de A6 suppose une borne de concurrence que le texte ne fixe pas, et le « pire cas » a disparu — à corriger

- **Lieu** : ligne 212 ; devis v3, § 3, ligne 48.
- **Preuve**
  - Le montant de 5,93 correspond à trois agents S au plafond, avec leur relecteur au pire, plus deux propositions et un jugement au pire. Il ne couvre les appels en vol que si le harnais n'en lance jamais davantage.
  - Le brouillon 1 écrivait « pire cas des appels en vol + pire cas du prochain appel ». Le brouillon 3 écrit « appels en vol + prochain appel », sans dire à quel coût ces appels sont comptés.
- **Correction proposée** : ligne 212 : « A6 : dépense + pire cas des appels en vol + pire cas du prochain appel > plafond ⇒ plus de lancement. Le harnais n'a jamais plus de trois items S, deux propositions et un jugement en vol à la fois ; la garde est éprouvée sur un dépassement de cette borne. Réserve 5,93 USD (devis v3, § 3). »

### 10. Les documents qui font foi sont ceux de la version 5, pas de la v6 ; COMMIT-CODE peut être rempli — à corriger

- **Lieu** : lignes 6, 11, 12, 221, 229, 249 et 250.
- **Preuve**
  - L'en-tête cite la note v5 (`6c71414b…`), le rapport R5 v5 (`0923bcc2…`) et la vérification `01a7258d…` (fichier `verification-corrections-lot-b1-v4.md`). La sortie citée est celle du devis v2 (`724e2b79…`), alors que P7 renvoie à « bloc 8 » de la sortie v3.
  - Les lignes 229, 249 et 250 renvoient à la « note v5 ».
  - Le code v6 existe (commit `35ac9e10738ccaac486ec9b9684fe70441f6371a`, 233 essais passés). Sa vérification par le même contre-lecteur ne relève aucune bloquante (`045030e2…`).
  - La ligne 221 dit A1 « à rejouer en version 6 » : c'est fait (rapport R5 v6, lignes 16 et 22 à 27).
- **Correction proposée**
  - Citer à la place la note v6 (`7c996b824155…`, empreinte entière), le rapport R5 v6 (`0e6b4338ef26…`), la vérification `verification-corrections-lot-b1-v5.md` (`045030e2a76b…`), `parametres_v6.json` (empreinte de son compagnon), la sortie v3 (`efcbc21f768a…`) et la note des écarts v3 (`60ba28c23c92…`).
  - Remplir COMMIT-CODE avec le commit `35ac9e10…` et les empreintes du paquet v6, mot pour mot.
  - Ligne 221 : « A1 est éprouvée en version 6 (rapport `0e6b4338…`) ».

### 11. « Le texte ne se répète plus d'un monde à l'autre » est faux — à corriger

- **Lieu** : ligne 246.
- **Preuve**
  - La note v6 (ligne 68 et § 11) compte 17 textes de vérités répétés d'un monde à l'autre : bornes naturelles et vérités structurelles. La vérification v5 (§ 1) en compte 16. Les deux comptes ne concordent pas.
  - Ces répétitions retirent environ deux tiers des vérités de l'aire « hors textes vus » : il en reste 30 à 32 sur 96.
- **Correction proposée**
  - Ligne 246 : « … le texte de ces cinq gabarits ne se répète plus d'un monde à l'autre. Les autres vérités en répètent [n] (rejeu v6, compte à fixer entre 16 et 17), écartées de l'aire hors textes vus. »
  - Faire trancher l'écart 16 contre 17 par le rejeu.

### 12. La certification des pièges ne dit rien de la redite, et le code a choisi seul — à corriger

- **Lieu** : ligne 255 ; note v6, ligne 60 ; vérification v5, remarque 25.
- **Preuve** : le code v6 n'applique plus T5 aux pièges à la plantation. C'est un écart déclaré, « à faire approuver ». Sur la racine 20261122, deux pièges d'un même monde ont le même profil : le second qu'un proposeur avancerait serait compté redite.
- **Correction proposée** : ligne 255 : « Piège : vivant, vrai-borné, non trivial, tué à 3N, revérifié par T6. Aucune condition de redite entre pièges. Les redites par l'étage 3 seul entre énoncés plantés sont comptées et rapportées. »

### 13. L'audit de symétrie n'est pas symétrique — à corriger

- **Lieu** : ligne 201 (R4).
- **Preuve** : l'audit se déclenche sur un rapport de H2 > 2, mais pas sur un rapport < 0,5. Il se déclenche si H4 tient, mais pas sur un échec extrême (faux « neuf » ≥ 0,95). Rien ne déclenche d'audit sur H3 : ni Δ très grand, ni r_S = 1, ni Δ négatif.
- **Correction proposée** : ligne 201 : « Symétrie : H1 confirmée avec précision > 0,60, ou réfutée avec précision < 0,05 ; rapport de H2 > 2 ou < 0,5 ; |Δ| > 0,50, ou r_S ou r_N = 1 ; H4 tenue, ou faux « neuf » ≥ 0,95 ⇒ audit avant remise (…) ».

### 14. Ce qu'on fait quand la fumée échoue pour Opus ou pour Argon n'est pas dit — à corriger

- **Lieu** : lignes 127 à 131, 200 et 208.
- **Preuve** : R1 ne couvre que Astra et Kimi, et « aucun autre repli » est écrit. Pour un échec d'Opus (proposeur, témoin, S et N) ou d'Argon, la table dit « R1 appliqué ». A2 arrête « la configuration », mot qui ne s'applique pas au juge ni au relecteur.
- **Correction proposée** : « Fumée ou A2 en échec pour Opus ou pour Argon ⇒ aucun lancement, retour au directeur. Pour Astra ou Kimi ⇒ R1. »

### 15. Le seuil des réfutations fausses et son dénominateur sont ambigus — à corriger

- **Lieu** : lignes 84 et 104.
- **Preuve** : le brouillon 1 lisait le seuil 0,10 sur la borne haute ; le brouillon 3 écrit « seuil 0,10 » sans dire sur quoi. On ne sait pas non plus si le dénominateur porte sur les 150 items analysés seulement, ou aussi sur les témoins et les seconds services.
- **Correction proposée** : « Réfutations fausses : rapportées aux réfutations déclarées par S sur les 150 items analysés (premier service). Seuil sur la borne haute de Clopper–Pearson à 97,5 %. »

### 16. A4 ne définit ni l'« alerte » ni le « manque » pour les verdicts « indecis » et « plafond » — à corriger

- **Lieu** : ligne 210.
- **Preuve**
  - Un « indecis » ou un « plafond » (A7) sur un témoin grossier n'est classé ni comme manque ni comme réussite.
  - A4 lit en cours de course la clé des témoins, alors que l'ordre ouvre les clés au pas 7 (ligne 140).
- **Correction proposée** : « Alerte : verdict « faux » sur un témoin trivial. Manque : tout verdict autre que « faux » sur un témoin grossier, y compris « indecis » et « plafond ». Seul le code lit la clé des 48 témoins hors analyse en cours de course ; aucun agent ne la lit. »

### 17. Des blancs ne portent pas le marqueur, et le validateur ne les verra jamais — à corriger

- **Lieu** : ligne 5 (date), lignes 304 et 306 (CONSIGNES, SCRIPT-ANALYSE).
- **Preuve**
  - Ni CONSIGNES ni SCRIPT-ANALYSE ne portent « À REMPLIR » dans le corps. La date est écrite « à porter » : la casse ne correspond pas au marqueur.
  - Une fois les autres blancs remplis, le validateur passerait.
  - SCRIPT-ANALYSE est dit « scellé avant la course » (pas 4, après le scellement de ce texte, ligne 136) : il n'a pas à être un blanc de ce texte.
- **Correction proposée**
  - Ligne 5 : « Date : À REMPLIR : DATE ».
  - Inscrire « À REMPLIR : CONSIGNES (chemin et empreinte) » au § Plan d'analyse.
  - Retirer SCRIPT-ANALYSE des « Pièces à remplir », et écrire au pas 4 : « script d'analyse scellé, contre-lu, avant le pas 5 ; son empreinte va au manifeste ».

### 18. La branche « aire ≤ 0,75 » n'a jamais été éprouvée, et aucune garde ne contrôle le contexte neuf par item — à corriger

- **Lieu** : lignes 105, 119 et 214 ; rapport R5 v6, ligne 17 (« — » en colonne artefact).
- **Preuve**
  - La comparaison au seuil n'a été éprouvée que sur des aires au-dessus : les 42 racines le sont. Aucun essai ne fait basculer la lecture.
  - « Chaque item est jugé dans un contexte neuf » (ligne 119) n'a ni garde ni contrôle.
- **Correction proposée**
  - Ajouter aux essais R5 une banque artefact dont l'aire est ≤ 0,75, pour montrer que le code bascule.
  - Étendre A8 : « … et chaque journal d'appel de S et de N ne contient qu'un seul item ; sinon arrêt ».

### 19. Le devis v3 porte encore trois écarts relevés par le rejeu — à corriger (dans le devis)

- **Lieu** : devis v3, lignes 3, 27 et 49 ; note des écarts, verdict et § 2, ligne 8.
- **Preuve**
  - « 192,79 × 1,5 + réserve = 294,90 » : avec la réserve de 5,93, le calcul donne 295,11. Le plafond de 300 ne change pas.
  - L'en-tête renvoie à la sortie du script v2, au lieu de la v3.
  - Le § 2 ne dit pas que le bas prend le juge Astra.
- **Correction proposée** : « 192,79 × 1,5 + 5,93 = 295,11 (sortie v3, bloc 7), arrondi à la dizaine supérieure : 300 » ; « Chaque chiffre vient de la sortie du script v3 (`efcbc21f…`) » ; au § 2 : « Le bas prend le juge Astra. »

### 20. Les mots « nouveau » et « nouvelle » sont employés comme étiquettes — mineure

- **Lieu** : lignes 58 (« par construction, nouvelle ») et 105 (« nouveau, convention supposée »).
- **Correction proposée** : « (par construction, ajoutée au brouillon 3) » ; « (ajouté au brouillon 3, convention supposée) ». « Neufs par construction » (ligne 27) se corrige par la remarque 6.

### 21. Les citations obligatoires ne sont que nommées — mineure

- **Lieu** : ligne 22 ; Antériorité, question 5, ligne 288.
- **Preuve**
  - Le texte nomme POPPER, Dwork et al., « The Ladder » et Co-Scientist sans référence. POPPER est au dépôt : `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf`.
  - La question 5 a perdu le nom du banc de criblage séquentiel que citait le brouillon 1 (CADS, par N-067).
- **Correction proposée**
  - « … cite POPPER (Huang et al. 2025, `docs/sources/pdf/huang-2025-icml-…pdf`, empreinte au compagnon), Dwork et al. 2015, « The Ladder » (Blum et Hardt 2015) et Co-Scientist. Seul POPPER est au dépôt ; aucun chiffre n'est repris des quatre (R7). »
  - Question 5 : « (CADS, cité par N-067) ».

### 22. Le fait sur Lean n'a pas de source citée — mineure

- **Lieu** : ligne 30.
- **Correction proposée** : ajouter « (`docs/notes/mathematiques-nouvelles-v1/verification-juge-standard-lean-v4.35.0-v1.md`) ».

### 23. A9 a perdu « par identifiant (R10) » — mineure

- **Lieu** : ligne 215.
- **Correction proposée** : « A9 : minuterie de destruction par identifiant (R10) à 48 heures… »

### 24. L'exception « retrouvée » est asymétrique — mineure (R4)

- **Lieu** : ligne 74.
- **Preuve** : elle lève la redite par l'étage 3 seul pour les retrouvées, pas pour les piégées. Elle relève donc la précision par une règle qui lit la clé.
- **Correction proposée** : ajouter « … La précision sans l'exception est rapportée à côté, au même rang que la précision principale. »

### 25. A5 dit « proposeur » là où il faudrait dire « configuration » — mineure

- **Lieu** : ligne 211.
- **Preuve** : Opus sert à la fois dans la configuration à deux familles et dans le témoin.
- **Correction proposée** : « … pour un modèle dans une configuration, sur les trois premiers mondes… »

### 26. L'aire hors textes vus n'a pas d'intervalle — mineure

- **Lieu** : ligne 86 ; vérification v5, § 4, réserve de description.
- **Preuve** : l'aire repose sur une trentaine de vérités par racine.
- **Correction proposée** : « … rapportée avec un intervalle de rééchantillonnage par monde (enfant (10, 0)) ».

### 27. Rien ne dit comment lire une course arrêtée en cours de route — mineure

- **Lieu** : lignes 207 à 216.
- **Preuve** : A3, A5 et A6 peuvent arrêter un rôle ou la course. Seule H2 dit ce qu'on fait quand il reste moins de 8 mondes.
- **Correction proposée** : « Toute hypothèse dont un rôle est arrêté est « non courue », rapportée telle quelle. H1 sur moins de 12 mondes : description seulement. »

## Ce que H3 peut encore affirmer avec l'aire mesurée (question 7)

- Une aire de 0,94 à 0,98 veut dire ceci : un classifieur sans calcul sépare presque les faux des vérités par la seule surface du texte, sur les deux strates (faux tôt comme pièges). La branche « aire > 0,75 » est donc la branche attendue.
- **Rien sur les verdicts déclarés.** r_S, r_N, φ_b et Δ tels qu'ils sont écrits ne peuvent pas soutenir « S discerne mieux que N ». La fuite gonfle les deux bras et tasse Δ vers le plafond ; elle ne le biaise pas forcément en faveur de S. Mais on ne peut plus séparer la vérité de la forme. Ces mesures restent descriptives.
- **Ce qui reste affirmable, à condition de l'écrire (remarque 1).** La production d'instances vérifiées exactement par T6 ne dépend pas du style : une instance est fausse ou ne l'est pas. Deux affirmations tiennent donc :
  - un taux v_S de contre-exemples vérifiés, avec sa borne et un seuil ;
  - si N reçoit le même schéma de sortie, la différence appariée v_S − v_N, lue par le même score.
- **Ce qui ne l'est pas.** « N aucun par construction » n'est pas une affirmation : c'est un dessin dont le signe est acquis (R3). Et φ_S, sous la règle « S ne tue que par contre-exemple vérifié », est nul par construction (remarque 2).
- **Une voie que le concepteur peut écrire, sans la revendiquer.** Il pourrait apparier Δ par tranches de score de style, en ne gardant que les énoncés dont le score tombe dans la zone où les faux et les vrais se recouvrent. Il faut en fixer le découpage avant toute donnée, et l'effectif y sera faible.

## Les blancs restants (question 8)

| blanc | permis tel quel ? | constat |
|---|---|---|
| COMMIT-CODE | non | Il peut être rempli dès maintenant (v6, `35ac9e10…`, vérifiée), sous réserve que le concepteur approuve la remarque 25 de la vérification (ma remarque 12). |
| GRAINE-RACINE | non | Ce ne doit pas être un blanc : il faut une procédure de tirage au scellement (remarque 5). |
| PLAFOND-GO, ÉCHÉANCE | oui | Ils sont fixés par le GO. Le texte devrait dire qu'ils sont portés avant le scellement. |
| ANTÉRIORITÉ | oui, si le protocole P est exécuté avant le scellement | L'exécutant (ni Opus, ni Argon) et son devis ne sont pas nommés (notes au directeur v2, ligne 49). |
| CONSIGNES | oui | Le blanc n'est pas marqué (remarque 17). |
| ESSAIS-R5 (A2 à A13) | oui | Lot B3. |
| SCRIPT-ANALYSE | à retirer des blancs | Il est scellé après ce texte (remarque 17). |
| CONTRE-LECTURE | oui | Elle est à remplir avec cette pièce et sa vérification. |
| Blancs cachés, non marqués | non | La décision du directeur sur le seuil 0,75 (remarque 3), l'approbation du choix sur les pièges (remarque 12) et la date (remarque 17). |

## Points vérifiés sans remarque

- **Valeurs de bornes et de niveaux.** Clopper–Pearson à 97,5 % : 2 sur 75 donne 0,093 (3 sur 75 : 0,1125) ; 0 sur 40 donne 0,0881. Le niveau du test des signes, 10 sur 12, vaut 0,0193. Calculs faits par `scipy.stats`.
- **Score apparié.** La forme de q et de S(Δ₀) concorde avec `ML_estimate.4` et la statistique T0 du code R (lignes 83 et 93 à 96), avec n₁₀ = n12 et n₀₁ = n21.
- **Effectifs, coûts et P7.** Les effectifs (432, 144, 208, 24 et 24) et les postes du devis v3 se retrouvent au rejeu, au centime près. Les bornes de P7 et les comptes de P9 et P10 aussi (sortie v3, blocs 8 et 9 ; rapport R5 v6).
- **Gardes de la plantation.** La garde de retirage et celle des mondes perturbés ont leur cas sain et leur artefact (rapport R5 v6). La consignation au manifeste d'un triple refus reste à corriger (vérification v5, remarque 24).
- **Phrases interdites.** Aucune phrase du type « vérifié par Lean donc vrai ». Le texte ne revendique aucune nouveauté (ligne 296).
