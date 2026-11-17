# Contre-lecture courte (R2) — essai d'invariance au lot, v3 (commit ab16240b)

**Verdict : prêt** (aucune bloquante, aucune majeure ; deux réserves mineures à noter, non bloquantes).

Lecteur neuf. Lu : diffs v2 → v3 du module, des essais, du préenregistrement, de l'amorce, de l'essai à blanc et du dépôt réduit. Les 13 essais passent (2 min 09, processeur) ; les six empreintes compagnons de la v3 se vérifient. Essai à blanc lu, non rejoué. Rien exécuté du dépôt voisin, rien ouvert sous `diag/`.

## M1, M2, M3 de la contre-lecture v2
- **M1 (issue « établie » trop large) : corrigé.** `lire_issue` (module l. 171-179) sépare « invariance établie » (lots 64, 1 et 7 identiques au lot 16, aux trois couches) de « identité 16/64 établie, invariance non établie » (lot 64 identique, lot 1 ou 7 différent) ; le § 4 du préenregistrement porte les mêmes trois lignes décisives et la même condition. Texte et code coïncident ; toute combinaison des témoins et des égalités mène à une issue unique. Le champ `lots_1_et_7_identiques` est versé au résultat.
- **M2 (carte) : corrigé.** `verifier_carte` (l. 200-203) est appelée à chaque exécution de l'étape, que le chargement soit réel ou injecté. L'essai `test_etape_sur_contexte` la passe dans les deux sens : acceptée pour « NVIDIA A100-SXM4-40GB », refusée pour « processeur », « …-80GB », « …-PCIE-40GB » et la chaîne vide. Seul reste, en mineure, que le contrôle a lieu après le chargement des poids (voir m1).
- **M3 (préenregistrement) : corrigé.** `Arret` si le fichier manque, avant le chargement ; plus de `None` ; l'essai vérifie l'arrêt, puis que `sha256` = empreinte du fichier. Le chemin versé est le v3, copié par le dépôt réduit v12 (l. 55-56 du diff).

## Mineures de la v2
- m1 (C2/C4 pour « réfutée ») : gardé, désormais déclaré comme choix prudent au § 4 et en tête du module, avec « un écart 16/64 avec un témoin en défaut est rapporté, sans issue ». Accepté.
- m2 (docstring périmé) : corrigé (préenregistrement v3, cinq témoins).
- m3 (échéances) : `ECHEANCES` non changé dans le code, mais le § 7 cite les échéances codées (0,65 h attendu haut, 1,8 h au pire, hors pip) et les totaux sont recalés (0,35 à 0,6 h ; coût 0,22 à 0,37 USD ; ligne 5,4 à 6,0). Accepté.
- m4 (textes de l'amorce) : en-tête l. 37 et message de commit corrigés ; les noms de fichiers d'état en `…-b-alpha` restent, cosmétique.
- m5 (essai à blanc) : cas `runid-balpha` attendant le code 17 ajouté, et son dossier nettoyé.
- m6 à m8 : sans changement, hors pièces (le feu de la mère doit citer `GO-2026-11-17-04`).

## Sur la substitution des lots dans l'essai des deux issues positives
**Suffisant pour ce que l'essai doit prouver, avec deux réserves.** Sur processeur le calcul n'est pas invariant au lot (22 tâches sur 24), donc l'identité réelle ne peut pas être produite ; substituer au lot 64, 1 ou 7 la série du lot 16 (avec décalage de 1e-3 sur le lot 7 pour la première issue) isole la bonne chose : la **règle de lecture**, indépendante du matériel. Ce qui reste exercé pour de vrai : les formes des passes (C1 lit les passes réelles, car `vraie(…, lot, formes)` est appelée d'abord), les rejeux C3 et C3b (déterministes sur processeur), C2, C4, et le chemin de comparaison par empreinte (égalité exacte via C3 ; inégalité via `Bruyant` et le décalage).
- Réserve a (mineure) : l'égalité entre deux **formes différentes** n'est jamais produite réellement ; elle est simulée. C'est inévitable ici et sans risque : `comparer` ne dépend pas de la forme, seulement des tenseurs rendus.
- Réserve b (mineure) : il manque deux combinaisons du tableau : lot 64 différent avec lots 1 et 7 identiques (attendu « réfutée »), et lot 64 identique, lot 1 différent, lot 7 identique (attendu « identité 16/64… »). La logique `all(…)` les couvre par construction ; une paramétrisation de `fausse_avec` sur ces deux cas coûte trois lignes. Le test `test_cas_sain_miniature` accepte les trois issues positives ou négatives, ce qui est voulu (processeur).

## Défauts nouveaux
Aucun bloquant ni majeur. Deux notes : (m1) le contrôle de la carte reste après le chargement de 16 Go (lire `torch.cuda.get_device_name` avant `from_pretrained` économiserait quelques minutes en cas de carte inattendue ; l'amorce refuse déjà au code 11 si `CARTE_ATTENDUE` est posée) ; (m2) les deux combinaisons ci-dessus. À sceller en l'état si Lazar et la mère n'y tiennent pas ; sinon une v4 pour ces deux points seulement.
