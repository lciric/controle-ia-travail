# Essai Lean D-1a, troisième essai : vérification des corrections de la contre-lecture (v1)

- **Quoi** : vérification courte, par le même contre-lecteur, des corrections demandées dans `contre-lecture-corrections-essai-3-v1.md` (`59b0ec03…6eec`). Classe B. Aucune dépense, aucune machine.
- **Qui** : Claude Fable 5.2, le 21 novembre 2026. Développeur : Claude Opus 5.5.
- **Lu** : branche `prep/lean-outillage-d1a-v11`, commit `47c7faaf` (code au commit `3c2f35dd`). Point de départ : `corrections-contre-lecture-essai-3-v1.md` (`f1e2ed8e…1751`). Puis `executeur_bac_v8.py` et `epreuve_isolement_v8.py` par différence avec les v7 ; `attendus-v7.json` par différence avec les v6 ; `piloter_poste_v12.sh` par différence avec le v11 ; l'erratum 1 du rapport des causes ; de la procédure v12 (`10872ae6…3cac`), l'en-tête, « Changements depuis v11 » et la section 8. Empreintes compagnes vérifiées. Aucun fichier existant modifié ni supprimé entre `6675009c` et `47c7faaf`.

## 1. Verdict

**Conforme, prêt pour le quatrième essai.**

Les deux points bloquants sont fermés. Les critères de décision écrits par le développeur (tolérance de 0,05 s ; moitié, quart, 1 Gio) sont vérifiés et **retenus tels quels**, avec deux précisions de portée (§ 3) qui ne changent ni le code ni un seuil.

Limite de cette vérification : je n'ai pas relu le reste de la procédure v12 (sections 0 à 7, création et destruction de la machine). C'est l'ordre d'un essai payant ; sa chaîne propre ne relève pas de ce mandat.

## 2. Les deux points bloquants

**B1, fermé.** `juger_limite_lean` (`epreuve_isolement_v8.py`, l. 209 à 223) juge la compilation seule : résultat systemd `oom-kill`, incident de la compilation « mémoire », code non nul, pas de « ALLOUE ». `incident_bac` n'y entre plus. L'exécuteur v8 expose `incident_compilation` et `incident_noyau` à part. Mon objet de contrôle rejoué sur le code v8 : compilation en échec d'elle-même, vérificateur tué par la mémoire, deux écarts rendus ; objet vrai, zéro écart. Dans les attendus, seul ce cas change.

**B2, fermé.** `relever_memoire_pic` (`executeur_bac_v8.py`, l. 212 à 219) attrape toute erreur du système et l'erreur de valeur. Mes objets rejoués : « No such device », contenu vide, contenu non entier rendent « aucun relevé » ; un contenu entier est lu.

## 3. Les critères de décision, vérifiés

**Tolérance de 0,05 s sur « délai » : retenue.** Rejoué : 31 ms et 4,949 s ne sortent pas « délai » ; 4,95 s et 5,011 s sortent « délai » ; à la limite de production (1 800 s), 1 799,9 s rien, 1 799,96 s « délai ». La tolérance est absolue, donc négligeable en production. Elle ne donne rien à un item : il doit brûler la limite à 0,05 s près. La lecture du cas hors tolérance est écrite d'avance (procédure, § 8.3) : non conforme, aucun reclassement à la main. C'est la bonne lecture.

**Seuils de mémoire (pic de la tranche au plus la moitié de la machine ; mémoire disponible au plus bas au moins le quart ; recoupement à 1 Gio près) : retenus.** Les sept critères sont appliqués par `juger_parallele` comme la procédure les écrit (§ 8.5). Rejoué sur six objets : un cas sain compté ; pic au-delà de la moitié, recoupement manqué, mémoire disponible trop basse, tranche sans relevé, passage avec incident, chacun refusé pour son motif. Le pic du noyau compte aussi les pages de fichiers : le critère de la moitié est prudent. Le critère du quart prend le plus grand des deux comptes : il ne dépend pas d'un creux bref que le relevé de `/proc/meminfo` aurait manqué.

Deux précisions de portée, à garder en tête à la lecture :
1. **Ce que « compté » veut dire.** La mesure porte sur l'item sain. Elle vaut pour cette machine (32 857 436 160 octets) et ces limites. Pour des items quelconques, la borne est arithmétique : trois unités à 6 Gio chacune, sans mémoire d'échange, font 18 Gio au plus. La procédure le dit à sa manière (« à l'empreinte mesurée ») ; c'est suffisant.
2. **La durée de vie de la tranche réservée.** Si systemd retirait la tranche quand elle est vide, entre deux unités, le plus-haut du noyau repartirait de zéro ; le relevé resterait un minorant, mais perdrait plus que « la dernière période ». Non éprouvé ici. Le critère de recoupement couvre ce cas : la machine aurait perdu plus que la tranche ne compte, et le passage ne serait pas compté. Indice à lire sur la machine : un nombre de relevés de la tranche très inférieur à la durée du bloc divisée par 0,1 s.

## 4. Les points non bloquants

- R1 : fait (tolérance, essais, deux mutations, lecture écrite d'avance).
- R2 : fait (arrêt avant tout item si un genre d'isolement n'a pas de cas sain).
- R3 : fait (erratum 1, les deux phrases corrigées comme demandé).
- R4 : non fait dans le code, dit comme tel ; la procédure fait lire le détail des trois tentatives réseau et lit « non éprouvé » un programme non lancé. Acceptable.
- R5 : fait pour le seuil de trois relevés ; l'allongement de 0,1 s de la durée murale reste, dit comme tel. Acceptable.
- Les trois phrases sur « délai » sont dans la procédure (§ 8.3), mot pour mot.

Une incohérence relevée en passant, hors du code : le rapport des causes (§ 8) écrit « 0,84 USD restant sur 65 » ; la procédure v12 écrit « 0,84 USD dépensés sur 65 », avec `--deja-depense-usd 0.84`. La suite des essais (0,28, puis 0,56, puis 0,84) donne raison à la procédure. À corriger par un erratum du rapport, sans effet sur l'essai.

## 5. Rejoué

- Chaîne Lean épinglée présente (Lean 4.35.0, commit `eb6cafb7…`).
- Essais v8 de l'exécuteur et de l'épreuve, et essai du pilote v12, avec la chaîne : **102 réussis, 0 sauté**.
- `mutations_gardes_v12.py`, avec la chaîne, dossier neuf : **61 tuées sur 61**, témoin 102 réussis.
- Mes objets de contrôle sur le code v8 : § 2 et § 3.
- Non rejoués : l'essai hors machine v4 de 39 cas (journal lu : conforme, empreinte juste) ; la suite entière du harnais ; les 151 essais v7 et v8 réunis annoncés par le développeur (je n'ai rejoué que les 102 des fichiers v8 et v12).
- Fichiers temporaires et arbre de vérification supprimés.

## 6. Ce qui reste, et que seule la machine dira

Rien de ce qui passe par systemd et bwrap n'est éprouvé hors machine : le classement « délai » et sa marge ; le chemin du cgroupe des unités ; la création de la tranche réservée et son cgroupe ; le classement « mémoire » du cas Lean ; les issues des sondes v3 sous l'utilisateur `bac`. La section 8 de la procédure écrit d'avance la lecture de chacun, y compris le cas où la mesure de mémoire échoue (aucun passage en parallèle compté). Aucun « conforme » ne dépend d'un pic de mémoire.

## Relevé de méthode

**Chaîne de raisonnement.**
1. B1 fermé : `epreuve_isolement_v8.py`, l. 209 à 223 ; objet faux rejoué, deux écarts ; mutation e801 tuée.
2. B2 fermé : `executeur_bac_v8.py`, l. 212 à 219 ; trois objets rejoués.
3. Tolérance : `executeur_bac_v8.py`, l. 90 et 208 ; six seuils rejoués.
4. Critères de mémoire : `juger_parallele` ; six objets rejoués ; procédure v12, § 8.5.
5. La tranche réservée vit pendant tout le bloc parallèle : **supposé**.
6. L'écart entre le compte du noyau et celui du cgroupe tient dans 0,05 s : **supposé**, une mesure à 11 ms.

**Objets de contrôle.** Faux : compilation en échec propre et vérificateur tué (écart attendu, écart rendu). Vrai : compilation en `oom-kill` (zéro écart). Faux : pic de tranche à 2 Gio quand la machine en perd 7 (refus attendu et rendu). Vrai : 7 Gio de pic, 7 Gio de baisse (compté).

**Premier pas non justifié.** Le pas 5, puis le pas 6. Les justifierait : le quatrième essai lui-même. La procédure écrit d'avance la lecture si l'un des deux tombe.

**Mode d'échec affecté.** Aucune ligne dans le mandat. Visé : « épreuve qui ne peut pas échouer, ou pas réussir ».

**Trouvaille de côté.** Sans objet : rien vu hors de la cible, sinon l'incohérence de « restant » et « dépensés » du § 4.

**Évaluateur et conseil.** Juges : les essais, les mutations, puis la machine. Par où un bon jugement non mérité : tout ce qui touche systemd est joué sur des fichiers et des bacs factices écrits par l'auteur ; la section 8 est ce qui empêche de lire après coup.
