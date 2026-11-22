# Vérification des corrections du brouillon 4 du préenregistrement du pilote « oracles plantés » — v1

- Nature : vérification des corrections (R2, classe A), faite par le même contre-lecteur que `contre-lecture-brouillon-3-v1.md` (`65152d7f…`) : Opus 5.5 (`claude-opus-5-5`), qui n'a écrit ni le brouillon, ni le devis, ni le code, ni la sonde. Date : 2026-11-22. Dépense : 0 USD. Aucun appel de modèle, aucun réseau. Aucun fichier existant modifié.
- Pièce relue : `prereg/mathematiques-nouvelles-v1/preenregistrement-pilote-generation-v1-brouillon-4-v2.md`, `212c6eca7833…` (« OK » au contrôle), commit `649e3438`. Les numéros de ligne renvoient à ce fichier.
- Pièces lues, toutes « OK » au contrôle :
  - le devis v4 `devis-pilote-generation-v4-brouillon.md` (`411844ee…`) ;
  - les notes `notes-au-directeur-fable-b4-v2.md` (`06a92833…`) ;
  - `empreintes-code-lot-b1-v6.md` (`831e7b3b…`) ;
  - sous `calculs-v4/`, les sorties seulement : celle de la sonde (`e6ae3d49…`) et celle du script du devis (`8194b015…`). Le rejeu du devis et de la sonde a été vérifié en parallèle par un autre Opus ; je ne l'ai pas refait.
- Recoupements faits ici :
  - les 30 empreintes du relevé du code v6 sont égales aux fichiers du disque et à ceux du commit `35ac9e10` ;
  - les empreintes citées de POPPER, de la note sur Lean, de `parametres_v6.json`, de N-067 et du mandat sont égales aux fichiers ;
  - les seuils k(n) du test des signes, recalculés par `scipy.stats`, sont égaux à ceux du texte ;
  - la grille de calibrage de la table des valeurs critiques couvre n de 40 à 150 et une discordance de 0,01 à 0,8.
- Rien n'a été lu des fichiers interdits, ni d'une autre branche.

## Sortie du validateur

`controle_ia.prereg.problemes` sur le brouillon 4 :

```
- section vide ou à remplir : Seuil
- section vide ou à remplir : Plan d'analyse
- section vide ou à remplir : Liste d'arrêt
- section vide ou à remplir : Contre-lecture
```

Ces quatre sections portent des blancs déclarés : DÉCISION-SEUIL, LISTE-DES-CONNUS et CONSIGNES, PLAFOND-GO, ÉCHÉANCE et ESSAIS-R5, CONTRE-LECTURE. Le validateur ne voit pas DATE (en-tête) ni ANTÉRIORITÉ (section non exigée), mais ces deux blancs portent maintenant le marqueur.

## Verdict

Des 27 corrections, **22 tiennent** et **5 tiennent avec réserve** ; **aucune ne tient pas**. La relecture de ce qui est neuf trouve **11 remarques**, numérotées de 28 à 38 : **1 bloquante**, **3 à corriger**, **7 mineures**.

La bloquante touche la comparaison de H2 : la configuration à deux familles et le témoin n'ont pas le même dessin d'appels, et cet écart se mêle à l'effet de la composition (remarque 28). Hors ce point et les blancs déclarés, le brouillon serait scellable après les corrections 29 à 31.

## Les 27 corrections, une par une

| n° | objet | sort | preuve |
|---|---|---|---|
| 1 | H3 sans critère dans la branche haute | **tient avec réserve** | N reçoit le schéma de S et passe par T6 (lignes 83, 139 et 184). E1 à E5 sont chiffrées (lignes 101 à 106). « N aucun par construction » a disparu. J'accepte le refus motivé du seuil absolu sur v_S : la sonde (`e6ae3d49…`) montre qu'une règle sans calcul atteint 0,80 à 0,907 ; ce seuil aurait été acquis d'avance. Réserve : la sortie de S est rédigée par le relecteur (remarque 30). |
| 2 | branches de la table de H3 ; taux de fausses morts de S vide ; « non porté » | **tient** | La colonne « branche d'aire » est ajoutée (lignes 236 à 247). La ligne 117 dit que le taux de fausses morts de S est nul par construction. « Non porté » est remplacé par « V1 sans E1 » (ligne 244). |
| 3 | seuil 0,75 décidé après la mesure ; mesure hors dépôt | **tient avec réserve** | La mesure est versée et contrôlée « OK » (`v6-aires.json`, `32cd1781…` ; `v6-balayage.txt`, `180edc16…`). Le texte dit le seuil « gardé après lecture » (lignes 94 et 110) et la branche haute « attendue » (P12). Le blanc DÉCISION-SEUIL est ouvert. Réserve : le blanc admet « le défaut échu ». Un défaut de 48 heures vaut pour une proposition avec recommandation ; pour un seuil d'une pièce de classe A, je recommande un mot explicite du directeur. |
| 4 | verdicts de H1 recouvrants ; base absente ; niveau faux | **tient** | Les lignes 96 à 99 et 232 à 234 sont disjointes : « réfuté » porte sur les deux configurations, et le cas limite va à « non concluant ». La base est dans le critère. La ligne 120 dit la règle descriptive, sans niveau nominal. La ligne 77 définit l'union des deux proposeurs. |
| 5 | graine racine en blanc | **tient avec réserve** | Trois racines de 128 bits sont tirées après l'empreinte du texte. Le manifeste poussé ne porte que leurs empreintes, et un second manifeste pour le même texte arrête tout (lignes 221 à 224). Le blanc a disparu. Réserve : le lieu de garde des racines n'est pas dit (remarque 34). |
| 6 | faux « connu » de H4 | **tient** | Les 20 items sont des énoncés faux, 10 faux tôt et 10 pièges, tirés par l'enfant (7, 1) (ligne 158). Strates de 20 et 20. Taux ponctuel, au plus 2 sur 20 (ligne 119). Ce que le juge reçoit est fixé (ligne 159). La liste source est un blanc marqué. J'accepte la variante qui écarte les vérités à littéral tiré. |
| 7 | H2 : unité, coût apparié, k, ex æquo, rapport | **tient avec réserve** | Y_c(w) est défini par dollar (ligne 80). Les k(n) sont justes (recalculés). « 24 tirages, sans vote, coût mesuré » est écrit (ligne 22). Rapport des sommes. Réserves : la règle du prix unique d'Argon n'atteint pas son but (remarque 29), et le dessin d'appels des deux configurations diffère (remarque 28). |
| 8 | état initial du registre de lignée | **tient** | Trois registres, vides au départ ; les morts établies par S et N vont à part ; comptes par source (lignes 185 à 190). |
| 9 | réserve de A6 et borne de concurrence | **tient** | « Pire cas » est rétabli, les créneaux sont écrits, la garde est éprouvée sur un dépassement (ligne 264). 3 × 1,644 + 2 × 0,496 + 0,576 = 6,50 : je retrouve le calcul. |
| 10 | documents de la version 5 ; COMMIT-CODE | **tient** | COMMIT-CODE est rempli (ligne 9). Les 30 empreintes du relevé concordent avec le disque et avec le commit `35ac9e10`. La table des empreintes porte les pièces de la version 6 en empreintes entières (lignes 352 à 384). |
| 11 | « le texte ne se répète plus » | **tient** | La phrase est restreinte aux cinq gabarits à k (ligne 299). Le compte de 16 à 18 textes selon la racine se retrouve dans la sonde (colonne « vérités répétées »). |
| 12 | certification des pièges et redite | **tient** | Ligne 307 et choix approuvé avec sa raison (ligne 312). |
| 13 | audit de symétrie | **tient** | Ligne 253 : les déclencheurs vont dans les deux sens pour chaque hypothèse. |
| 14 | fumée en échec pour Opus ou Argon | **tient** | Lignes 152, 251 et 260. |
| 15 | réfutations fausses : dénominateur et borne | **tient** | Ligne 85 (150 items, premier service), ligne 106 (borne haute) et ligne 90 (Clopper–Pearson à 97,5 %). |
| 16 | A4 : alerte et manque | **tient** | Ligne 262. |
| 17 | blancs sans marqueur | **tient avec réserve** | DATE, CONSIGNES et LISTE-DES-CONNUS portent le marqueur ; le script d'analyse sort des blancs (ligne 397). Réserve : le choix du périmètre par le directeur reste un blanc caché (remarque 31), et la procédure de la date est contradictoire (remarque 32). |
| 18 | branche basse jamais éprouvée ; contexte neuf sans garde | **tient** | La banque artefact d'aire ≤ 0,75 est aux essais R5 (ligne 274). A8 exige un seul item par journal (ligne 266). |
| 19 | trois écarts du devis v3 | **tient** | Devis v4, en-tête et §§ 2, 3 et 10. |
| 20 | « nouveau » et « nouvelle » en étiquettes | **tient** | Aucune occurrence comme étiquette (recherche faite) ; « neufs par construction » a disparu. |
| 21 | citations obligatoires | **tient** | Ligne 19, avec le chemin et l'empreinte de POPPER, égale au fichier. CADS est rétabli (ligne 336). |
| 22 | source du fait sur Lean | **tient** | Ligne 27 ; l'empreinte `5748817e…` est égale au fichier. |
| 23 | A9 « par identifiant » | **tient** | Ligne 267. |
| 24 | exception « retrouvée » asymétrique | **tient** | Ligne 75. |
| 25 | A5 : « proposeur » | **tient** | Ligne 263. |
| 26 | aire sans intervalle | **tient** | Ligne 87, enfant (10, 2) ; un flux propre à la tâche est mieux que celui que je proposais (10, 0). |
| 27 | course arrêtée en route | **tient** | Ligne 252, avec un seuil d'effectif par hypothèse. Les valeurs critiques pour n de 40 à 150 sont bien dans la table (grille vérifiée). |

## Remarques neuves

### 28. Les deux configurations comparées par H2 n'ont pas le même dessin d'appels — bloquante

- **Lieu** : ligne 140 (« le proposeur reçoit … ses propres propositions antérieures dans ce monde, jamais celles d'un autre proposeur ») ; ligne 70 (la redite se compte sur la liste commune à la configuration) ; lignes 22 et 64.
- **Preuve**
  - Le témoin est une seule chaîne de 24 appels d'Opus. Chaque appel voit les 23 propositions précédentes, et le modèle peut donc éviter de se répéter.
  - Dans la configuration à deux familles, il y a deux chaînes de 12 appels. Chacune ne voit que ses 11 propositions précédentes. Pourtant, la redite (ligne 70) et l'union des retrouvées (ligne 77) se comptent sur la configuration entière. Une proposition d'Argon qui répète une proposition d'Opus, qu'Argon ne pouvait pas voir, est comptée comme redite et n'ajoute aucune vérité retrouvée.
  - La différence par monde de H2 et la précision de H1 mêlent donc deux effets : la composition (deux familles contre une) et le dessin (une chaîne de 24 avec tout le contexte, contre deux chaînes de 12 aveugles l'une à l'autre).
  - Le témoin n'est plus non plus « k tirages » au sens de N-045 v2 : ses tirages ne sont pas indépendants, puisque chacun voit les précédents.
  - Le sens du biais est connu d'avance : il désavantage les deux familles. Un verdict « témoin supérieur » serait en partie fabriqué par le dessin (R3, R4).
- **Correction proposée** (choix du concepteur ; je recommande la première forme, qui garde le témoin de N-045)
  - Ligne 140 : « Une proposition par appel. Dans chaque configuration, chaque modèle forme une chaîne de 12 appels par monde. Chaque appel voit les propositions antérieures de sa propre chaîne, jamais leur issue, jamais celles d'une autre chaîne. Le témoin est formé de deux chaînes d'Opus de 12, indépendantes ; la configuration à deux familles, d'une chaîne d'Opus et d'une chaîne d'Argon. »
  - Ligne 22 : « … le témoin à un modèle (Opus, deux chaînes de 12 par monde) … ».
  - Autre forme : les deux chaînes de chaque configuration voient la liste commune de la configuration, et le témoin garde une chaîne de 24. Le contexte est alors égal, mais Argon voit les textes d'Opus.
  - Le devis ne change pas : le nombre d'appels est le même.

### 29. La règle du prix unique d'Argon n'assure pas un prix unique — à corriger

- **Lieu** : ligne 175 ; devis v4, lignes 33 et 89 à 90.
- **Preuve**
  - La règle interdit seulement les appels d'Argon entre le 30 novembre 2026 à 00:00 UTC et le 2 décembre 2026 à 00:00 UTC. Une course qui commence avant le 30 novembre et reprend après le 2 décembre la respecte, tout en payant Argon à deux prix.
  - Le « sinon » ne couvre que les appels faits dans la fenêtre.
  - Le verdict de H2 n'est pas dit lu au prix payé, à côté d'une sensibilité qui ne le change pas.
- **Correction proposée** : ligne 175 : « Un seul prix d'Argon. Toutes les propositions d'Argon de la course sont faites avant le 30 novembre 2026 à 00:00 UTC, ou toutes après le 2 décembre 2026 à 00:00 UTC. Sinon, H2 est lue en description. Le verdict de H2 se lit au prix payé ; la lecture à l'autre prix est une sensibilité, qui ne change pas le verdict. »

### 30. La sortie du bras S est rédigée par le relecteur, qui peut ajouter ses propres instances — à corriger

- **Lieu** : ligne 139 (« La sortie du bras S est celle que rend le relecteur, dans ce schéma, après lecture de la sortie de l'agent et de sa trace ») ; lignes 23 et 83.
- **Preuve**
  - Rien n'interdit au relecteur (Kimi, sans outil) d'écrire des instances qui ne sont pas de l'agent, par exemple les valeurs extrêmes de la règle aveugle.
  - v_S mesurerait alors « Opus avec outil, plus Kimi », et non l'agent à outil. E1 et E4 ne pourraient plus se lire comme l'effet de l'outil.
  - La sensibilité « S avant relecture » le montre après coup, sans l'empêcher.
- **Correction proposée** : ajouter à la ligne 139 : « Le relecteur choisit et ordonne au plus trois instances parmi celles que l'agent a avancées. Il n'en ajoute aucune, et peut changer le verdict. Le code retire avant T6 toute instance absente de la sortie de l'agent, et compte ces retraits. »

### 31. Le périmètre de la course est un blanc caché — à corriger

- **Lieu** : « Pièces à remplir », lignes 387 à 397 ; devis v4, § 8 ; notes, nœud 1.
- **Preuve** : le texte est écrit pour l'option (a), où les bras S et N sont courus. Le directeur peut choisir (b) ou (c), qui demandent un brouillon 5. Rien ne porte le marqueur : on pourrait sceller le texte sans que ce choix soit fait.
- **Correction proposée** : ajouter, en tête du Plan d'analyse : « Périmètre : bras S et N courus (option (a) du devis v4, § 8). Décision du directeur : À REMPLIR : PÉRIMÈTRE (identifiant du mot). » ; ajouter PÉRIMÈTRE aux pièces à remplir.

### 32. La procédure de la date se contredit — mineure

- **Lieu** : ligne 8 (« portée par `date -u` dans la commande de scellement ») ; ligne 221 (la commande calcule l'empreinte, puis tire).
- **Preuve**
  - Le validateur refuse tout « À REMPLIR » avant le scellement : la date ne peut donc pas être portée par la commande qui scelle.
  - Si elle l'était, l'empreinte devrait être calculée après l'avoir écrite.
- **Correction proposée** : « Date : À REMPLIR : DATE (portée par `date -u` juste avant la commande de scellement ; l'empreinte est calculée sur le texte daté). »

### 33. E4 mesure S contre une règle choisie par qui connaissait les gabarits — mineure

- **Lieu** : lignes 105 et 236 ; ligne 321.
- **Preuve**
  - Les valeurs (3N, 1, N + 1) ont été choisies par le concepteur des gabarits. La règle est un plancher (« A est un plancher, non un maximum »).
  - Le gain possible de S tient dans quatre gabarits : F1 « puissance majorée à un pas », F3 « résidu atteint tôt », « résidu évité » et « rang d'apparition » (sonde, par gabarit).
  - La lecture « S entre au pilote 2 » (ligne 236) généralise au-delà de ce que E4 établit.
- **Correction proposée** : ligne 236, lecture : « S dépasse cette règle aveugle A, sur cette banque. Le gain se lit par gabarit (les quatre gabarits hors de portée de A) ; S entre au pilote 2 comme proposeur de contre-exemples vérifiés, à éprouver sur la version 7. »

### 34. Le lieu de garde des racines n'est pas dit — mineure

- **Lieu** : ligne 223 (« Les racines elles-mêmes vivent avec les clés, hors de la branche »).
- **Preuve**
  - Si le conteneur de confiance est perdu avant le pas 8, les racines sont perdues. Les clés ne se recalculent plus, et l'engagement par empreinte ne peut plus être ouvert (R-3661).
  - Le texte ne dit pas non plus qui peut les lire avant le pas 8.
- **Correction proposée** : « Les racines sont écrites, scellées, dans le dossier des clés du conteneur de confiance, avec une copie chiffrée hors de la branche dont l'emplacement est consigné au manifeste de scellement. Seul le code de plantation et d'analyse les lit avant le pas 8. »

### 35. A14 ne dit pas comment reprendre après un arrêt — mineure

- **Lieu** : ligne 272.
- **Preuve** : seule A10 dit « toute reprise attend un devis relu et un GO ». Après un arrêt par projection, on ne sait pas si les blocs déjà courus restent dans la mesure.
- **Correction proposée** : ajouter : « Une reprise attend un devis v5 relu et un GO. Les blocs déjà courus restent dans la mesure ; les profils de jetons mesurés ne changent aucun critère. »

### 36. L'échangeabilité des items est mise à mal par la règle aveugle — mineure

- **Lieu** : lignes 89, 101 et 208.
- **Preuve**
  - Les discordances qui feront E4 tiennent dans 7 à 15 items de quatre gabarits.
  - Le score apparié et ses valeurs critiques, calibrées pour deux bras aléatoires, traitent les 75 items comme échangeables. Or l'un des bras, la règle aveugle, est fixé d'avance par la banque.
  - La sensibilité par gabarit existe (ligne 208), mais elle n'est pas rapportée à côté de chaque verdict.
- **Correction proposée** : ajouter à la ligne 105 : « E4 est rapportée avec l'intervalle du rééchantillonnage par gabarit (enfant (5, 1)) ; si cet intervalle contient 0, la ligne de la table le dit. »

### 37. La première rédaction écartée n'est pas versée — mineure

- **Lieu** : ligne 5 ; notes, § D.
- **Preuve**
  - « Seule cette ligne diffère » ne peut pas être contrôlé : `28ef25bd…` n'est pas au dépôt.
  - La raison donnée (une mention à ne pas écrire au dépôt) interdit le versement tel quel, non une preuve.
- **Correction proposée** : verser la différence (`diff`) entre les deux rédactions, la ligne « Auteur » remplacée par « [ligne retirée] », avec les deux empreintes ; ou dire où la première rédaction est gardée.

### 38. La prédiction sur v_N est presque irréfutable — mineure

- **Lieu** : ligne 43 (« v_N dans [0,15 ; 0,85] … je ne sais pas »).
- **Preuve**
  - L'intervalle couvre presque tout. Avec B servi en nombre et trois instances, N peut imiter la règle aveugle, qui touche 0,80 à 0,907.
  - Le haut de l'intervalle est donc plausible sans aucun calcul.
- **Correction proposée** : écrire un intervalle réfutable, par exemple « v_N dans [0,60 ; 0,95], centre 0,80, confiance 0,4 : la lecture nue peut avancer les valeurs extrêmes ». Ou dire explicitement que P5 sur v_N n'est pas une prédiction (« non prédite »).

## Ce qui reste avant le scellement

- **Blancs déclarés** : DATE, DÉCISION-SEUIL, PLAFOND-GO, ÉCHÉANCE, ANTÉRIORITÉ, LISTE-DES-CONNUS, CONSIGNES, ESSAIS-R5 et CONTRE-LECTURE. S'y ajoute PÉRIMÈTRE (remarque 31).
- **Remarques à reprendre** : la bloquante (28) et les trois à corriger (29 à 31). Les mineures (32 à 38) peuvent passer en errata.
- **Ensuite** : une vérification de ces corrections par le même contre-lecteur.
