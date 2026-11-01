# Consigne pour l'implémentation indépendante B — version 2

À transmettre à l'agent B par la session principale. Écrite le 1er novembre 2026 (≈ 22:30 UTC). Cette consigne ne contient **rien** du code de la course : seulement la spécification v2 et la liste des exigences.

## 1. Ta tâche, en deux lignes

Tu as écrit B v1 d'après la spécification v1, validée au bit sur la course originale, et tu as relevé quinze ambiguïtés. La **spécification v2** les tranche (son § 0 dit, point par point, ce qui change et si tu dois changer). Écris **B v2**, conforme à la v2, dans des **fichiers neufs**, valide-la (spécification v2, § 12), et rends un rapport.

## 2. Ce que tu reçois, et rien d'autre

Dans `/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/` :
- `entrees/specification-statistique-decisive-v2.md` — la spécification v2, copiée par la session principale ; empreinte SHA-256 attendue : `977dd9092cbd3715bd2cc9b5d5839f276242ad3f9df6302d383555f2b2ff511a` (version du 1er novembre 2026 ; si la session principale te transmet une autre empreinte, c'est elle qui vaut ; si l'empreinte du fichier diffère de celle qu'on t'a transmise, arrête-toi et dis-le) ;
- `entrees/resultats-regles-defense.json` (`d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b`) et `entrees/analyse-regles-defense.json` (`18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42`) — inchangés ;
- `entrees/specification-statistique-decisive-v1.md` et tes propres fichiers v1 : tu peux les lire et partir d'eux, **sans les modifier** (R12).

## 3. Ce qui t'est interdit

- Ouvrir quoi que ce soit hors du dossier `implementation-b/` (lecture, exécution, `git show`, `git log -p`, recherche) ; seule exception, plus tard et sur ordre : les quatre fichiers de la course nommés en X4 et leurs compagnons. Sont interdits en particulier le code de la course, ses essais, l'arène, les préenregistrements, les contre-lectures, les registres. Si la spécification te semble insuffisante, **n'en cherche pas l'explication ailleurs** : écris l'ambiguïté dans ton rapport (section « Ambiguïtés restantes »), choisis la lecture la plus prudente (celle qui arrête ou marque plutôt que celle qui laisse passer) et continue.
- Importer un module du dépôt (`controle_ia` compris) : seulement la bibliothèque standard de Python et numpy.
- Réseau, appel de modèle, commit, fichier compagnon `.sha256` (la session principale scelle et commite tes fichiers), modification ou suppression d'un fichier existant, écrasement d'un fichier de sortie.
- Lire un résultat de la réplication : tu ne seras lancée dessus qu'après le scellement du préenregistrement, sur ordre de la session principale.

## 4. Environnement

Tout (essais, validation, et plus tard la course) avec **`/home/claude/controle-ia-travail/.venv/bin/python`** (Python 3.13.18, numpy 2.4.6 : l'environnement de la course). Ta validation v1 a été faite avec numpy 2.5.3 ; elle est à refaire dans cet environnement. Versions écrites dans la sortie et dans le rapport.

## 5. Fichiers à écrire (noms versionnés, neufs)

Dans `implementation-b/` : `implementation_b_v2.py`, `test_implementation_b_v2.py`, `validation-b-v2.md`, `validation-b-v2.json`, `sortie-b-originale-v2.json`. Aucun autre fichier, sauf des fichiers temporaires d'essai dans un dossier temporaire du système, supprimés à la fin.

## 6. Exigences

**X1 — Spécification v2, § 0.** Pour chaque ligne marquée « oui », implémente la décision ; pour chaque ligne « à confirmer », dis dans le rapport si B v1 le faisait déjà, et aligne-toi sinon ; pour chaque ligne « non », confirme que B v1 le faisait ainsi. En particulier :
- vérifications de E2 (§ 3, points 1 à 5) et gardes neuves de E1 (`delta`, `config_sha256`, `lam` et `reference`) : arrêt d'entrée, code 2 ;
- compagnons d'empreinte : nom `<fichier>.sha256`, empreinte **et** nom de base vérifiés (§ 3) ;
- entrée E5 (analyse de A) : lue seulement après ta propre statistique ; concordance calculée par toi (§ 11.2) ; discordance de niveau arrêt → code 3 ;
- « graines neuves » sur V, X̄ et (ii), seuil « strictement plus de 2 » (§ 10.3) → code 3 ;
- codes de sortie 0, 2, 3 et champ `lecture_autorisee` (§ 11.1) ;
- deux issues globales, brute et après déclencheurs, avec « V0 : non évaluée par B » (§ 10.4) ;
- frontière numérique sans court-circuit, comparaisons sur valeurs brutes exclues, cos_moyen de T4 inclus, héritage des marques (§ 8) ;
- contrôles de santé évalués par budget, déclenchés si au moins un budget (§ 7) ; seuil de T3 `0x1.fffffff768fa1p-1` ;
- contenu de la sortie (§ 11.1) et **table de correspondance** « élément de la spécification → clé JSON » dans le rapport.

**X2 — Validation complète (spécification v2, § 12)** : 12.1 course originale (écart ≤ 10⁻⁹ sur 16 contrastes × 2 budgets ; classes, contrôles et verdicts attendus) ; 12.2 **une ligne d'essai par ligne** de chaque table, verdict, issue, contrôle et déclencheur, sur entrées synthétiques, dont « R0 > R2 », « R0 ≳ R2 », « R2 ≳ R0 », « R2 > R0 », « R4 > R2 », « R2 > R4 », Table C lignes 2, 3, 5, 6, TR3, TR4, la ligne inatteignable et la frontière (marque et héritage) ; 12.3 gardes de la réplication, cas (a) à (e) ; 12.4 entiers de plus de 2⁶³ (lecture, comparaison, écriture exactes) et règle D sur les trois vecteurs ; 12.5 gardes d'entrée, cas sain et artefact (code 2, aucune sortie). Garde chaque essai de mutation de B v1 qui reste pertinent et ajoute ceux des exigences neuves.

**X3 — Rapport `validation-b-v2.md`** (et la même matière en `validation-b-v2.json`) : verdict en tête ; versions ; empreintes des entrées ; tableau du § 0 de la spécification avec, pour chaque point, « déjà ainsi en v1 » ou « changé en v2 » ; résultats de X2 (comptes d'essais, écarts maximaux, durées) ; **liste exhaustive des fichiers que tu as ouverts** pendant tout ton travail (lecture ou exécution, chemin complet), y compris ceux de v1 ; table de correspondance des clés ; **commande exacte** pour la course (voir X4) ; ce que la validation ne couvre pas ; ambiguïtés restantes ; le nom du modèle qui t'anime (famille et version).

**X4 — Commande pour la course**, écrite dans le rapport, avec des chemins à compléter par la session principale : entrées E1 `diag/<run>/resultats-regles-defense.json`, E2 `runs/<run>/manifeste.json`, E3 `prereg/preregistrement-replication-regles-defense-convergence-v1.md`, E5 `diag/<run>/analyse-regles-defense.json` (chacune avec son compagnon), E4 les deux fichiers de `entrees/` ; sortie `implementation-b/sortie-b-replication-v2.json` (neuve). Aucune option ne peut changer un seuil, sauter une vérification ou forcer une racine ; toute option qui touche une ligne du § 10.4 a une valeur par défaut neutre et sa valeur est écrite dans la sortie.

## 7. Ce que tu rends à la session principale

Un message court : verdict de la validation ; chemins et empreintes SHA-256 des cinq fichiers du § 5 ; nombre d'essais (passés, échoués) et de mutations détectées ; durée ; liste des fichiers ouverts ; ambiguïtés restantes. Rien d'autre n'est attendu de toi avant la course.
