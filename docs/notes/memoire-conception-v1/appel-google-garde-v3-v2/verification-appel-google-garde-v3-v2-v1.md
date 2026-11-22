# Vérification des corrections — appel_google_garde_v3_v2.py

- **Pièces vérifiées** : `docs/notes/memoire-conception-v1/appel-google-garde-v3-v2/`, sur la branche `claude/bibliothecaire-v1`, commit cc838a1e.
  - `appel_google_garde_v3_v2.py` : empreinte 9d28a2fe…, conforme à son compagnon.
  - `test_appel_google_garde_v3_v2.py` : empreinte cd040cf3…, conforme à son compagnon.
- **Vérificateur** : le contre-lecteur de la v1 (Claude Opus 5.5), en lecture seule, sans réseau, sans modèle externe.

## Verdict

**Non conforme, de peu.** Les sept défauts relevés sur la v1 sont tous corrigés et vérifiés par mutation. La v2 introduit deux défauts nouveaux de gravité moyenne, qui demandent chacun quelques lignes :
- un modèle servi au nom suffixé (`-lite`) est admis comme le modèle demandé ;
- sur un flux coupé, le coût compté vient de l'usage partiel au lieu du pire cas.

Un troisième point moyen ne joue que si plusieurs appels partent en parallèle sur le même journal. Une fois ces trois points corrigés et vérifiés, la pièce est conforme.

## Les sept défauts de la v1, un par un

1. **Plafond de dépense — corrigé.**
   - Plafond de course de 3 USD ; `--plafond-usd` ne peut que le baisser (3,5 et NaN sont refusés).
   - Cumul tenu par le journal : une ligne de réservation au pire cas avant l'envoi, puis une ligne de solde. Si le script meurt entre les deux, le pire cas reste compté.
   - Mutations N12 et N13 : avant le 1er décembre, trois appels au pire cas passent et le quatrième est refusé (2,95 USD déjà comptés + 0,98 > 3). Après le 1er décembre, un seul appel passe (pire cas 1,97 USD).
2. **Garde des motifs cloisonnés — corrigé.** `relecture_fable_api_v5.garde_motifs` est appelée sur l'énoncé exact, avant toute écriture au journal et avant tout envoi (M16 : session et courriel refusés).
3. **Replis silencieux dans le flux — corrigé.**
   - Ligne de données illisible : défaut `FLUX_ILLISIBLE` (M4).
   - Erreur dans le flux : défaut `ERREUR_FLUX` (M5).
   - Erreur réseau : `RESEAU_<type>` (M14).
   - Lignes du flux autres que `data:` : comptées dans le journal, ce qui est acceptable.
4. **Tarif — corrigé.**
   - La page de prix est vérifiée par son empreinte avant l'envoi (40202cdd…, conforme).
   - Je l'ai relue : sections « Gemini 4 Argon » et « Gemini 4 Carbon », onglet Standard. Les deux donnent 2 / 10 USD par million jusqu'au 30 novembre, puis 4 / 20 à partir du 1er décembre. Aucun palier selon la longueur de l'invite.
   - La marge de 1,5 sur la sortie est appliquée.
   - Le majorant des jetons d'entrée (un octet vaut au plus un jeton) est sûr : M15 refusé à 5,78 USD.
5. **Modèle servi — corrigé**, avec le reste nouveau du point 1 ci-dessous. Un modèle servi absent ou différent est un défaut (M6).
6. **Limite de mots — corrigé.**
   - La limite est relue dans l'énoncé (« N mots »). Absente : refus. `--mots` discordant : refus (M12).
   - Le nombre « 2 000 » écrit avec une espace insécable est bien lu (N6).
   - Une concaténation fautive (« fiche 12 2000 mots », lue 122 000) produit un refus, donc reste du côté sûr (N7).
7. **Journal — corrigé.**
   - Le journal porte : les chemins, les empreintes de l'énoncé, de la sortie, du script, des deux gardes et de la page de prix, la dépense déjà faite, le tarif et sa source.
   - Les compagnons `.sha256` de la sortie texte et du `.json` sont écrits.
   - La vérification de non-écrasement (R12) porte aussi sur les compagnons.

## Ce qui reste

1. **Moyen, ligne 159 : modèle servi au nom suffixé admis.** `servi.startswith(demande + "-")` admet n'importe quel suffixe. Mutation N1 : `gemini-4-argon-lite` est lu comme une réponse (code de sortie 0). Un autre modèle passe ainsi sans GO.
   **Correction** : n'admettre que des suffixes de version, par exemple `re.fullmatch(re.escape(demande) + r"(-\d{3}|-preview-\d{2}-\d{4})?", servi)`, ou une liste fermée. Ajouter l'essai `-lite`.
2. **Moyen, lignes 234 à 236 : coût compté sur un usage partiel.** `usage_lu` ne demande qu'un usage non vide et un code 200. Mutation M8 : un flux coupé sans fin, avec un usage partiel, compte 0,00035 USD au lieu du pire cas. Google a pu facturer davantage. Le même cas se présente avec `FLUX_ILLISIBLE` et `ERREUR_FLUX`.
   **Correction** : compter le coût mesuré seulement si `fin` n'est pas vide et qu'il n'y a pas de défaut de flux ; sinon compter le pire cas.
3. **Moyen si les appels partent en parallèle, lignes 196 à 208 : cumul exposé à une course entre lecture et réservation.** La lecture du journal et la réservation ne sont pas atomiques. Quatre appels lancés en même temps lisent chacun 0 USD et réservent 4 × 0,98 = 3,93 USD. Ce cas n'a pas été testé (pas de parallélisme dans mes essais).
   **Correction** : verrou exclusif `fcntl.flock` sur le journal, de la lecture jusqu'à l'écriture de la réservation. À défaut, écrire en tête du script que les appels d'une même course sont séquentiels.
4. **Faible, ligne 109 : valeur non finie dans le journal.** Mutation N2 : une ligne `{"cout_compte_usd": NaN}` rend la comparaison fausse et l'appel part. Le script n'écrit jamais NaN, donc il faut une édition à la main.
   **Correction** : refuser si `not math.isfinite(valeur)`. On peut aussi exiger que chaque solde suive une réservation de la même sortie (N3 : une ligne à −100 annule le cumul).
5. **Faible, `lire_flux` : morceau mal formé.** Un morceau dont `candidates` contient une chaîne (N9), ou dont un `text` vaut None (N10), lève une exception. L'erreur n'est pas silencieuse : la réservation au pire cas reste au journal. Mais aucun `.json` n'est écrit et le défaut n'est pas nommé.
   **Correction** : contrôler les types et produire `FLUX_ILLISIBLE`.
6. **Faible : la limite de mots écrite en lettres est ignorée.** Mutation N5 : « dix mille mots » avec « 3 mots-clés » donne une limite de 3, et l'appel part. Après l'appel, MAX_TOKENS reste attrapé.
   **Correction** : refuser si l'énoncé contient « mots » sans nombre en chiffres devant chacune de ses mentions, ou exiger que la limite soit écrite en chiffres.
7. **Faible : bascule du tarif fixée au 1er décembre à 00:00, heure de Paris ou UTC.** Si Google bascule plus tôt selon un autre fuseau, un appel du 30 novembre au soir serait compté 0,98 USD au pire cas, alors que le coût réel peut aller jusqu'à environ 1,31 USD.
   **Correction** : prendre le tarif « après » dès le 30 novembre.
8. **Faible : divers.**
   - `appels_avant` compte des lignes du journal : deux par appel.
   - L'empreinte de la garde importée est journalisée, mais pas comparée à l'empreinte scellée.
   - Le journal, écrit par ajouts, n'a pas de compagnon : à sceller en fin de course.
   - `garde_motifs` devient quadratique sur une très longue ligne sans retour à la ligne : 3 millions de signes ont dépassé 120 secondes. Rien ne part, mais le script se bloque.

## Essais lancés

- `pytest` sur `test_appel_google_garde_v3_v2.py` : **22 passed**.
- Mes 18 mutations de la v1, rejouées sur la v2, plus 13 nouvelles : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/mutations_v2.py`.
  - M15 est adaptée en lignes de 80 signes, à cause du blocage de `garde_motifs` (point 8).
  - Les dix-huit anciennes donnent toutes le résultat attendu.
  - Celles qui passent alors qu'elles ne devraient pas : N1, M8 (coût), N2, N3 et N5.
  - N9 et N10 lèvent une exception.

## Non vérifié

- Le parallélisme réel (point 3).
- Le fuseau horaire de la bascule de prix chez Google.
- Les noms de version que Google renvoie réellement dans `modelVersion`.
- Le comportement de facturation sur un flux coupé.
