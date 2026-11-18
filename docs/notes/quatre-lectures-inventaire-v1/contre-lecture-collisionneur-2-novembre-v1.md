# Contre-lecture de la note « Collisionneur à cinq espèces du 2 novembre : sélection d'une génération à l'autre, et vérification non circulaire du bac à sable » — v1

Contre-lecteur : sous-agent neuf (Opus 5.5, `claude-opus-5-5`), règle R2 ; je n'ai écrit ni la note, ni ses critères, ni aucune cellule, ni les lectures vérifiées d'espèce seule. Lancé par la session mère sous l'autonomie GO-2026-11-18-05 et le « go » de Lazar aux quatre lectures sans dépense (R-3168, R-3170). Écrit le 2026-11-18 entre 04:20 et 05:15 UTC environ. Aucune dépense, aucun appel de modèle, aucune clé lue, aucun commit, aucune poussée.

**Note contre-lue** : `docs/notes/quatre-lectures-inventaire-v1/collisionneur-2-novembre-v1.md`, empreinte `c49808606ad1d46f06226b89b4fb113bfdc3a57e8a19633b4adaa3320bd41d2f` (scellement vérifié : OK ; suivie dans git depuis le commit `2005f3ae`). Critères de lecture scellés avant ouverture : `criteres-lecture-collisionneur-2-novembre-v1.md`, `4f5604b5c2bfd39e79d96264e7164662515d1e6d8b23d3aa91b22f13ad415f87` (OK).

## Verdict

**À corriger.** La note est solide sur l'essentiel : l'intégrité des pièces, les positions de chaque espèce et la grande majorité des citations se vérifient ; aucun chiffre de l'état de l'art n'est donné pour vérifié ; aucune zone n'est dite vierge ; aucun résultat sous embargo n'est cité. Il y a quatorze corrections, toutes de fait : comptes d'accord contraires à ses propres critères scellés, deux positions d'Argon seul exagérées, une remarque du lecteur présentée comme un fait, un passage qu'elle a déclaré exclu mais qu'elle résume quand même, deux renvois vers des passages exclus, six oublis, une heure de fin fausse. **J'écris moi-même la version 2** : `collisionneur-2-novembre-v2.md`, dans le même dossier. Je ne touche pas à la version 1.

## Sources rouvertes

- Branche `donnees/collisionneur-v8-runs-v2`, commit `0e7b3e5` (R-1039), extrait seul sous `…/scratchpad/quatre-lectures/extrait/collisionneur-v8-runs-v2/`. Chemins dans la branche : `donnees/collisionneur-v8-runs-v1/selection-generations-v1/` (abrégé **sél/**, cellules sous `run-selection-generations-v1-e3-v1/cellules/`) et `…/bac-a-sable-v1/` (abrégé **bac/**, cellules sous `run-bac-a-sable-v1-e3-v1/cellules/`). Le commit court n'est pas vérifiable dans l'extrait (aucun fichier d'origine) ; il concorde avec R-1039 et R-1050 (`0e7b3e59`).
- Au dépôt : `docs/notes/reponses-especes-seules-2026-11-01-v1/lecture-verifiee-selection-generations-v2.md` (`79e17284…`, recalculée), `lecture-verifiee-bac-a-sable-v2.md` (`d7e19d88…`), `lecture-verifiee-bac-a-sable-kimi-v1.md` (`ef98275d…`) ; `registres/decisions.md` (R-830, R-959, R-973, R-975, R-986, R-990, R-1039, R-1049, R-1050, R-2528, R-3051) ; `registres/go.md` (GO-2026-11-01-07 et -08) ; `registres/etat.md` l. 316 ; inventaire `b49dc246…` (§§ A.4, B, C, E).
- Lu par moi : les deux questions ; les dix cellules de réponse (troisième tour), **sauf** les passages que la note déclare exclus, que j'ai sautés (voir § 3) ; les conceptions (premier tour) par sections (sél/A l. 5-24 ; sél/B l. 180-189 ; sél/C l. 32-45 ; sél/D l. 1-30, 59-70 ; sél/E l. 25-88 ; bac/A l. 93-101 ; bac/C Q1 à Q4, Q6, Q7 ; bac/E l. 7-66, 153-176 ; lignes isolées repérées par recherche dans bac/B, bac/D) ; les journaux et états des deux tours, par script (champs de contrôle seulement). Pas lu : les critiques croisées, les invites, les relais de Kimi, les scripts.

## 1. Intégrité (refaite)

- **Empreintes** : 133 fichiers dans l'extrait, 133 compagnons, 0 écart. Question et faits : `c899221888d1…`, `7c3404f477c7…` (sélection) et `26f2db15e6ab…`, `24064c98d197…` (bac). Ils égalent GO-2026-11-01-07/-08 (`registres/go.md` l. 181-182) et R-959. Les copies servies (`question-etage3.md`, `faits.md` du dossier de run) égalent les originaux. Aucun fichier « EMPREINTES » dans l'extrait : confirmé.
- **Journaux** (`journal.jsonl`) : 31 lignes, 30 cellules. Modèle servi = modèle demandé ; marqueur de fin présent ; aucune catégorie de refus. Seul échec : sél/critique croisée D, essai 1, `HTTP 429` « engine overloaded », 0 USD, repris en essai 2. B = `claude-opus-4-6` partout. Totaux des états : 16,38 et 16,24 USD. La note est exacte sur tous ces points.
- **Registres** : R-1049 (barème 15/75 pour Opus 4.6, environ trois fois le tarif) et R-1050 (option 1, runs gardés, B = Opus 4.6) sont cités fidèlement. La ligne 316 de `registres/etat.md` dit bien « inutile en l'état » (0 fiche traduite sur 15). R-986 précise que 0 sur 15 est le verdict « non lisible » (L2), et 0 sur 8 le verdict « inutile » (L3). La note recopie la ligne d'état telle quelle : je ne compte pas cela comme une erreur de la note.
- **Exclusions** : les tailles déclarées sont exactes (bac/C réponse 29 151 ; bac/B réponse 19 921 et conception 23 894 ; bac/A réponse 20 244 ; sél/C réponse 26 465 ; sél/E réponse 20 571 octets). Le classement prudent en famille 2 de l'opérateur qui exploite les scores est cohérent avec l'inventaire, § C, qui range « attaque de Goodhart du juge de l'organisme » en famille 2.

## 2. Citations tirées et rouvertes (32 au total, dont 30 justes)

Les citations sont tirées sur tout le texte, avec au moins deux par espèce et par tour. **Juste** = la position citée se lit à l'endroit indiqué.

| # | affirmation de la note (espèce) | rouvert à | verdict |
|---|---|---|---|
| 1 | règle du pôle « indécise → test plus puissant, ou retirée après deux essais » contre « non concluante ne passe pas » (A) | sél/`E3-T1-conception-A.md` l. 14 (S6) ; question l. 3 (objectif de Lazar) | juste |
| 2 | 85 à 95 % des fiches jamais jugées (A) | sél/`E3-T3-reponse-A.md` l. 119 ; conception l. 13 (S5) | juste |
| 3 | critique « la plus lourde », reçue de C, sur la traduisibilité (A) | sél/réponse A l. 43 | juste |
| 4 | ≥ 200 témoins par bras, 0 appel (A) | sél/réponse A l. 28, 87 | juste |
| 5 | pare-feu de N-053 : protège l'affinage, pas la sélection (A) | sél/conception A l. 16 (S8) | juste |
| 6 | 1 témoin vrai promu sur 5 au moins, 5 moniteurs, « connu + 0 » (B) | sél/`E3-T3-reponse-B.md` l. 183-187 | juste |
| 7 | puissance ≈ 0,55 à 40 fiches par bras, illustratif (B) | sél/réponse B l. 237 | juste |
| 8 | ablation ≥ 60 USD, illustratif (B) | sél/réponse B l. 289 | juste |
| 9 | quatre états, non concluante retirée (C) | sél/`E3-T3-reponse-C.md` l. 123 ; conception C l. 36 | juste |
| 10 | survivantes « avec leur gain de richesse » servies aux proposeurs (C) | sél/`E3-T1-conception-C.md` l. 38 | juste |
| 11 | « la littérature … montre que … biais d'ancrage lexical » : affirmation sans source (C) | sél/conception C l. 38 | juste (bien signalée comme hypothèse) |
| 12 | arrêt de la reproduction sur plusieurs générations si l'héritage est réfuté (C) | sél/réponse C l. 109 | juste |
| 13 | trois états administratifs, différée hors population reproductrice (D) | sél/`E3-T1-conception-D.md` l. 21-29 ; réponse D l. 100 | juste |
| 14 | « je ne revendique donc aucun vide bibliographique » (D) | sél/conception D l. 19 | juste |
| 15 | « ne pas fabriquer de survivantes », publier le rendement nul (E) | sél/`E3-T1-conception-E.md` l. 77, 87 | juste |
| 16 | allocation indépendante, « sans prétendre avoir réfuté l'héritabilité » (E) | sél/`E3-T3-reponse-E.md` l. 205 | juste |
| 17 | pas de rang par défaut (E) | sél/conception E l. 57 | juste |
| 18 | « L'empreinte n'est qu'un index ; la vérification est le rejeu » (A) | bac/`E3-T1-conception-A.md` l. 95 | juste |
| 19 | verdict libellé « identique, portable, dépendant de la donnée, confiné » (A) | bac/`E3-T3-reponse-A.md` l. 101 | juste |
| 20 | dossier partagé, la v48 n'interdit pas un cache, question de contrat (A) | bac/réponse A l. 30 (thème 16), 85 | juste |
| 21 | circularité d'Avalon « ne s'applique pas directement » (B) | bac/`E3-T3-reponse-B.md` l. 175 | juste |
| 22 | B retire son instrument de journal (B) | bac/réponse B l. 87-89 | juste |
| 23 | `bwrap` durci suffit (0,85) si le vérificateur est la session ; WebAssembly (C) | bac/`E3-T1-conception-C.md` l. 39, 41 | juste |
| 24 | attestation matérielle : confiance 0,10 contre la menace d'Avalon (C) | bac/conception C l. 62 | juste |
| 25 | erreurs rendues sans valeur numérique ; arrêt au premier succès (C) | bac/`E3-T3-reponse-C.md` l. 19, 113 | juste |
| 26 | sensibilité des suites par ablation, ablation fantôme (D) | bac/`E3-T3-reponse-D.md` l. 84-86 | juste |
| 27 | capture avant exécution (D) | bac/`E3-T1-conception-D.md` l. 13 | juste |
| 28 | décodage de l'archive hors du poste de Lazar (E) | bac/`E3-T1-conception-E.md` l. 50 | juste |
| 29 | producteur et auto-déclaration exclus de la base (E) | bac/`E3-T3-reponse-E.md` l. 178 | juste |
| 30 | Kimi seul : confiance 0,72 (Q5), 0,86 (Q6) ; « même engagement » ≠ « domaine interdit » | lecture vérifiée sélection v2, § 2.2 | juste |
| 31 | Argon seul : « jugeable si au moins 3 promues en génération 1 » | lecture vérifiée sélection v2, § 1.2, Q6 : « au moins 3 fiches **en sortie 1** » (du pont) | **fausse** |
| 32 | Argon seul : « Transmis : Argon seul (classement) » ; « C et Argon seul oui » ; « C et Argon seul contre D, E et Kimi seul » | lecture vérifiée sélection v2, § 1.2 Q3 (transmission complète **contre** dissociation, sans choix) et § 1.4 (« le statut du rang transmis n'est pas discuté ; il est transmis en mécanisme A ») | **exagérée** |

Vérifiés en plus : les quatre espèces qui disent « aucun `bwrap` réel » dans les pièces (bac/réponse A l. 97, B l. 177, D l. 104, E l. 168) ; le contrat de sortie en cinq points d'E (sél/conception E l. 63-69) ; les trois critères de C pour la sortie (sél/conception C l. 39) ; la grille de niches de C (l. 40) ; les positions d'Argon seul et de Kimi seul sur le bac (lectures v2 § 1.2 et Kimi v1 § 2).

## 3. Règles R7 et R8, avis et faits, cloisonnement

- **R7** : aucune référence n'est donnée pour vérifiée. POPPER, les antériorités du bac et les chiffres des espèces sont dits « illustratifs » ou « non vérifiés » (§ 3.3, Q7). Conforme.
- **R8** : aucune zone vierge revendiquée. La note relève même la phrase de D. Conforme.
- **Avis présenté comme un fait (1 cas)** : sél/Q3 et § 4. « Servir un score du juge aux proposeurs **touche** l'invariant … (N-053) » est écrit comme un constat. Cette affirmation n'est d'aucune espèce : c'est une lecture du rédacteur, et elle est discutable. Le juge du pôle n'est pas un moniteur, les proposeurs ne sont pas entraînés, et A lui-même tient que ce pare-feu protège l'affinage seulement. À marquer « remarque du lecteur ».
- **Cloisonnement, une incohérence** : la note range « la famille 3 de sondes hors système de fichiers » (bac/réponse A, E3') parmi les passages exclus qu'elle « ne résume ni ne reformule ». Puis elle la résume au bac, Q5 : « une classe de sondes hors système de fichiers, dont la non-détection est attendue et comptée comme couverture manquante (A) ». Le même contenu figure hors du passage exclu (bac/réponse A l. 20, thème 6), et il est défensif. Mais la note doit tenir sa propre règle : je retire la phrase dans la v2. Le reste des exclusions est tenu. Seuls subsistent deux rôles de méthode sans contenu, comme annoncé.
- **Deux renvois vers des passages exclus** : sél/Q2, ligne C (« E2 », le passage exclu de sél/réponse C) ; sél/Q2, ligne E (« sans contrôle positif d'adaptation, aucune conclusion de sûreté », qui renvoie à la cellule entière, dont le passage exclu). Je ne les ai pas vérifiés dans les passages exclus, que je n'ai pas ouverts. Le contenu se lit ailleurs. Pour C : sél/réponse C l. 22 (nul hétérogène, les meilleures ensemencent même sous le seuil) et l. 124, 131 (épreuve fraîche par génération). Pour E : sél/réponse E l. 61 (« contrôle positif d'adaptation », accepté « comme limite de portée »), dont la formule de la note force le sens. Je recite dans la v2.
- **Embargo** : rien de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis ; rien sous `diag/`. La référence à R-986 et R-990 porte sur l'épreuve fraîche du pont, hors embargo. Conforme.

## 4. Écarts aux critères scellés de la note

Ses critères (point 5) disent : « accord » si au moins quatre des sept sources, « majorité » à trois ; sinon « divergence » ou « propre à une espèce ». La note écrit **Accord** pour des positions tenues par trois sources, voire deux :

- **trois sources** : sél/Q2 (A, D, E) ; sél/Q3 (E, Kimi seul, B indirectement) ; sél/Q4 (A, C, D) ; sél/Q5 (A, D, E) ; bac/Q2 (A, C, Argon seul) et (A, D, E) ; bac/Q3 (D, E, Kimi seul) ;
- **deux sources** : sél/Q4 (E, Kimi seul) ; bac/Q7 (D, E).

Sur le bac, deux des groupes de trois comptent en outre deux fois un même modèle : C avec Argon seul, D avec Kimi seul. Enfin, sél/Q1 écrit « six sources sur sept » pour « plus de deux états ». Or Argon seul laisse le choix entre deux et trois états sans trancher (lecture v2, § 1.2 et § 1.4 : « aucune option retenue par question »). L'accord tient à cinq sources, plus B en creux.

## 5. Oublis

1. **B, bac, expérience 1 corrigée** : « excès de faux positifs dû à l'agent ». 50 fiches à effet nul sont traitées par l'agent à trois exécutions et par un script mécanique fixe ; test de McNemar ; contrôle sur 10 fiches à effet planté. B note que trois exécutions portent le taux de franchissement par fiche jusqu'à ≈ 0,14 (illustratif), et c'est le poste dominant de sa séquence (bac/réponse B l. 11, 107-123, 207). La note n'en dit rien. Or cette expérience touche directement l'accord nouveau sur le chiffre auto-déclaré et la boucle de retour. C mesure la même chose dans sa strate 2 (bac/réponse C l. 75).
2. **E, bac, sonde réseau** : E dit avoir vérifié dans le code servi que la sonde classe un délai dépassé comme « fermée ». Il demande qu'un délai seul devienne « indéterminé », par un essai de régression déterministe, avant l'épreuve de la garde G8 entière (bac/conception E l. 32, 91, 159 ; réponse E l. 158-162). C'est le seul défaut de code concret signalé par une espèce. Il est absent de la note.
3. **C, sélection** : « il ne faut pas dépasser 2 générations » tant que l'ablation n'a pas réfuté l'absence d'héritage utile (sél/réponse C l. 125). Le point sert directement la course à plusieurs générations, et il est absent.
4. **Dérive vers la testabilité** : la critique vient de A. D et E la transforment en mesure : lignées perdues selon le code de différé et la disponibilité de l'instrument (sél/réponse D l. 47 ; réponse E l. 21 et « Dérive instrumentale »). Absente.
5. **D, bac** : en repli, D garde l'option « ne pas exécuter l'artefact », c'est-à-dire le traiter comme donnée, reconstruire depuis la source, ou différer (bac/conception D l. 124 ; réponse D l. 29). Absente.
6. **Bac, Q4, antériorités et une divergence de libellé** : Thompson, Wheeler, programmation en N versions. La date d'Avizienis varie : 1977 avec Chen chez C, 1985 chez E. D retire sa référence. Rien de cela n'est rapporté, ni marqué non vérifié. Au bac, Q1, sur la question posée (« change-t-elle la classe ? »), C et Argon seul répondent oui ; A répond « change la frontière, pas la classe » (bac/conception A l. 74). L'accord de la note masque cette divergence.

Pas d'oubli de cellule ni d'espèce : les cinq espèces, les deux espèces seules et les trente cellules sont présentes.

## 6. Corrections, une ligne chacune (toutes appliquées dans la v2)

1. Comptes d'accord : passer à « majorité » les sept positions à trois sources et à « avis partagé par deux sources » les deux positions à deux sources (§ 4), en signalant les doubles comptes de modèle.
2. Sélection, Q1 : « six sources sur sept » devient « cinq sources (A, C, D, E, Kimi seul), B en creux ; Argon seul laisse le choix ouvert ».
3. Argon seul, Q6 : « au moins 3 promues » devient « au moins 3 fiches en sortie 1 du pont ».
4. Argon seul et le rang (Q3, § 3.1, § 4) : il ne « veut » pas servir le rang ; il le transmet dans l'une de ses deux variantes, sans choisir ni discuter.
5. N-053 : « touche l'invariant » devient une « remarque du lecteur, non des espèces », avec les raisons d'en douter.
6. Bac, Q5 : retirer le résumé de la classe de sondes hors système de fichiers, que la note a elle-même déclarée exclue.
7. Sélection, Q2 : recitation de C (l. 22, 124, 131 au lieu d'« E2 ») et d'E (l. 61, « limite de portée »).
8. Bac, Q7 : « signal de récompense » est de D seul ; E dit « exploratoire ».
9. Sélection, Q7 : POPPER est donné pour le plus proche par A, B, Argon seul et Kimi seul ; C le cite parmi d'autres ; E ne le nomme pas.
10. Ajouter l'expérience « excès de faux positifs dû à l'agent » (B), aux bac Q2 et § 3.2.
11. Ajouter la correction de la sonde réseau proposée par E, aux bac Q7 et § 3.2.
12. Ajouter la borne « pas plus de deux générations » (C) et la mesure de la dérive vers la testabilité (D, E), aux sélection Q6 et § 3.1.
13. Ajouter le repli « ne pas exécuter » (D), les antériorités non vérifiées du bac Q4 et la divergence « classe ou frontière » du bac Q1.
14. En-tête : l'heure de fin d'écriture est 04:17 UTC, pas 04:40. Le fichier est modifié à 04:17:13 et scellé à 04:17:21.

## 7. Ce que je n'ai pas pu vérifier

- Que les critères ont été scellés avant l'ouverture des cellules : leur date de modification (04:08) précède celle de la note (04:17). Les dates d'accès aux cellules ne sont pas une preuve (mes propres lectures les modifient).
- Le contenu des passages exclus, que je n'ai pas ouverts. Je n'ai donc vérifié ni les deux renvois du § 3, ni le classement de chaque passage dans la famille 2 au-delà du titre et de l'inventaire.
- Le commit court `0e7b3e5` : il est absent de l'extrait ; seule sa concordance avec R-1039 et R-1050 est vérifiée.
- Le rendu du rédacteur dit le compagnon `.sha256` « pas encore suivi dans git » : il l'est depuis le commit `2005f3ae` (04:17:39 UTC), qui contient la version scellée.
