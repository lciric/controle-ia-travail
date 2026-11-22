# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChGrMyZbTAiLdm531mLjb`
- Heure (UTC) : 2026-11-21T22:28:24Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/relecture-fable-api-v1/envois/4-configuration-calage-g1/consigne-relecture-v1.md` — sha256 bbd8497213ff1b3078dccc21599741c7b8c8d2ac1346cdb09b50954ef582356f (compagnon : vérifié)
  - correction : `docs/notes/relecture-fable-api-v1/envois/4-configuration-calage-g1/configuration-generation-calage-g1-v2.json` — sha256 22d8af77f62a1f1c7f1cfe3e3173b35643bb9737d73308b677276fc2c8a66796 (compagnon : vérifié)
  - correction : `docs/notes/relecture-fable-api-v1/envois/4-configuration-calage-g1/note-configuration-calage-g1-v2.md` — sha256 7b8e03b889393f7ef6008ee2716d6cdc3da703ed9601455c73445e85b721417b (compagnon : vérifié)
  - remarques : `docs/notes/relecture-fable-api-v1/envois/4-configuration-calage-g1/contre-lecture-configuration-calage-g1-opus-v1.md` — sha256 67d3d0d14bcd42132fa82cb0a1d4945076531a4ba8e0f6e2357595d2bc6c3bde (compagnon : vérifié)
- Empreinte de l'invite envoyée : 9291095e260a21ee0d637e580fad5ba8626107c006771c2404319d91afe9b310
- Jetons : entrée 68928, sortie 50663 (dont réflexion 46643), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 2.577944 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
à corriger

Les remarques C2, C3, m1, m2, m3, m5 et celles des § 4 et § 7 sont portées exactement, et m4 est laissé ouvert à bon droit. Deux points étroits empêchent « conforme » : une règle de lecture du fichier de classe A énonce sans exception un contrôle qui en a deux, et la note donne à m4 une classe que la contre-lecture ne lui donne pas. Je n'ai rien exécuté : tout ce qui suit vient de la lecture des trois pièces jointes.

## Corrections demandées

**1. Configuration, `regles_de_lecture`, cinquième règle (C1, point 1).**

La règle dit que toute entrée « repris d'une pièce scellée » ou « lu dans le code » à valeur courte porte sa valeur dans un extrait, et que le programme le contrôle. Deux entrées de ce champ ne la tiennent pas :

- `echantillonnage.troncature` vaut « aucune », et son seul extrait est la ligne du tirage multinomial ;
- `outils.outils_exposes` vaut `[]`, et aucun de ses trois extraits ne porte une liste vide.

La note dit la dispense (table et verdict), le fichier non. Cette dispense est un choix du correcteur : C1 dit « pour toute entrée ». Elle est raisonnable, mais elle doit être écrite dans la pièce qui sera scellée. Texte de remplacement de la règle :

> « Une entrée « repris d'une pièce scellée » ou « lu dans le code » dont la valeur est un nombre, une chaîne courte (40 caractères au plus) ou une liste porte sa valeur, sérialisée, dans l'extrait d'au moins une de ses sources ; une source JSON est lue à sa clé, et sa valeur doit être celle de l'entrée. Deux entrées, qui disent une absence qu'aucun extrait ne peut porter, en sont dispensées : `echantillonnage.troncature` (« aucune ») et `outils.outils_exposes` (liste vide) ; une garde du programme de validation fixe chacune. La révision est celle de T0.7, l. 1057. Le programme de validation le contrôle. »

Un point voisin est à vérifier sur le programme avant de récrire. `garde_d_equivalence.quantile` vaut 0,99, et sa première source est JSON (`P3-premier-test-config-v1.json:48`), où la clé vaut « q99 ». Lue à la lettre, la règle la refuse, alors que le programme ne signale aucun défaut. S'il traite ce couple à part, ajouter après la phrase des dispenses :

> « Pour `garde_d_equivalence.quantile`, la source `prereg/P3-premier-test-config-v1.json:48` porte « q99 », lu comme 0,99. »

**2. Note, classe du nœud m4.**

La contre-lecture ne classe pas m4, et l'option 1 modifie `harnais.fichiers`, donc la pièce de classe A. Deux remplacements :

- Verdict : « Un nœud ouvert s'y ajoute, sur les fichiers des fonctions de montage (§ 9). »
- Titre : « ## 9. Nœud ouvert de la v2 (m4) »

## Remarque par remarque

| Remarque | Portée ? | Constat |
|---|---|---|
| C1.1 | oui, sauf la dispense tue dans le fichier | Vingt entrées relèvent de la règle : je retrouve ce compte. Les dix-huit autres portent leur valeur dans un extrait ou à une clé JSON, sous la réserve du quantile. Le contrôle lui-même ne se voit que sur le programme. |
| C1.2 | oui dans le fichier | La règle est écrite, et l'extrait de T0.7:1057 porte la révision. Le contrôle est à voir sur le programme. |
| C1.3 | invérifiable ici | Les six cas exigés figurent parmi les douze annoncés. Le reste tient au programme et à sa sortie. |
| C1.4 | oui | Le verdict de la note dit ce que le programme garde et ne garde pas. |
| C2.1 à C2.4 | oui | L'entrée `releve_de_reference` porte les quatre points ; `portee` et les six `ou_s_ecrit_la_valeur` sont accordés. |
| C3.1 à C3.4 | oui | L'entrée `type_conserve` porte les quatre points, le précédent de T0.7 est au § 2.10, et le nœud reste conditionnel. |
| m1 | oui | Toutes les sources du banc lisent le brouillon 14 ; l'empreinte et le commit s'accordent avec la contre-lecture ; les décalages de 14 sont justes. |
| m2 | oui | Une seule valeur, « :4096:8 ». |
| m3 | oui | jinja2 est nommé hors de `valeur`, ce que permet « au moins ». La raison donnée tient aux programmes. |
| m4 | laissé ouvert, à bon droit | La contre-lecture donne bien une alternative. |
| m5 | oui | Les deux pièces sont ajoutées ; leurs préfixes d'empreinte s'accordent. |
| § 4 et § 7 | oui | Les trois phrases sont reprises presque mot pour mot ; les recommandations de l'auteur ne sont pas touchées. |
| Erratum 1 | intégré | Jugé sur le seul compte rendu de la contre-lecture, l'erratum n'étant pas joint. |

## Ajouts hors des remarques

Aucun ne change une valeur de génération. À faire valider avec les entrées, qui portent déjà « choix, à faire valider » :

- **La dispense des deux entrées d'absence** : voir la correction 1.
- **Le seuil de 40 caractères** pour « chaîne courte ». Il inclut la révision et exclut `type_de_capture` (43 caractères) et `classe`.
- **`unicite`** : « il ne se remplace que par une version nouvelle de ce fichier ». C'est une règle neuve. Elle découle du nom écrit en dur, mais un relevé de référence fautif oblige alors à une version nouvelle de la configuration.
- **`conversion`** : « nommée au manifeste avec son fichier et son empreinte » et « sans conversion, le type conservé est le type de capture ».
- **`comparaison`** : la commande d'un programme de classe B est écrite dans la pièce de classe A, sans chemin ni empreinte.
- **Le nom du relevé de référence.** Je le tiens pour la façon minimale de le « désigner ».
- **Programme** : le douzième artefact (quantile 0,95) et « source JSON sans clé désignée = défaut ». Ils vont au-delà du minimum demandé, dans le sens de la remarque.
- **Note § 9** : les deux « conséquences à noter » sont une analyse du correcteur. Elle est utile et ne tranche rien.

Une conséquence de C2 n'est dite nulle part. Les champs n° 1 et 2 du banc citent l'empreinte du relevé de référence, qui n'existe qu'une fois le poste de calage choisi (nœud 4) et le programme de l'opérateur joué en réel, ce qui n'a jamais été fait. Ce n'est pas un défaut de la correction ; c'est à porter au texte du banc.

## Nœuds ouverts : recommandation et confiance, sans trancher

- **m4** : option 2, ne pas geler, confiance 0,6.
  - Geler ne garde rien si le lanceur reproduit les fonctions au lieu de les importer.
  - Cela lierait des fichiers entiers de lanceurs passés. `manifeste.py` devra vraisemblablement changer pour déclarer le type conservé (C3) ; je n'ai pas vu ce fichier.
  - `pieces_citees` porte déjà l'empreinte des cinq fichiers : la contre-lecture du lanceur a une cible exacte.
  - L'argument du coût d'une version nouvelle tombe si la correction 1 en impose une de toute façon.
  - Si les lanceurs importent ces fonctions, je pencherais pour l'option 1.
- **Dispense de la correction 1** : l'accepter et l'écrire, confiance 0,8, une fois les deux gardes vues dans le programme.
- **Nœud 1** : (a), confiance 0,7.
- **Nœud 2** : (a), sous la condition de mesure que pose la contre-lecture, que j'accepte ; confiance 0,7 si l'effet mesuré reste dans le repère, pas de recommandation ferme avant.
- **Nœud 3** : (a), confiance 0,85.
- **Nœud 4** : (a), confiance 0,8.
- **Type conservé (C3)** : pas de nœud aujourd'hui. S'il naît, conserver le float32 des deux côtés et appliquer en aval la même conversion gelée le dissoudrait sans doute ; confiance 0,6.

## Calculs refaits

- **Entrées** : 69, compte confirmé.
- **Pièces citées** : 33, dont deux documents vivants sans empreinte.
- **Sources** : j'en compte 210 sous les entrées et la cohérence. Le total de 211 se retrouve si le programme compte aussi le mot du directeur. L'écart à la v1 est juste : 204 + 4 + 3.
- **Épreuves** : 45 + 12 + 2 + 2 + 1 = 62 artefacts ; 4 + 1 = 5 cas sains.
- **Valeurs nulles** : sept. **Champs du relevé de référence** : sept. **Fichiers gelés** : huit.
- **Contre-lecture** : ses lignes 128 et 139 portent bien les deux extraits cités.
- **Lignes du banc** : 332, 355, 357 et 359 plus 14 donnent 346, 369, 371 et 373.
- **Plafonds** : 10 × 400 = 4 000, sous 16 384 ; 8 × 10 × 400 = 32 000 positions.
- **Empreintes** : toutes celles que donne la contre-lecture, entières ou en préfixe, s'accordent avec le fichier et la note.

## Ce qui ne se vérifie pas ici

- **Sur les programmes seuls** :
  - les contrôles `_valeurs_a_leur_source` et `_revision_de_t07`, les tables `CLES_JSON` et `FIXEES_PAR_UNE_GARDE` ;
  - le traitement du quantile et le refus des douze artefacts ;
  - `--comparer` et son ordre ;
  - la relecture des 211 extraits par l'assembleur ;
  - la lecture de la v2 par le programme de l'opérateur ;
  - la portée de la règle « absent ou non scellé », pour laquelle le programme ne vérifie qu'un compagnon, qui selon le fichier ne vaut pas scellement.
- **Sans la v1** : « sans autre changement ». Je constate seulement que toutes les valeurs énumérées au § 2 de la contre-lecture sont intactes.
- **Sans le dépôt** :
  - les vecteurs d'essai (seul l'échantillon de la garde s'accorde avec la contre-lecture) ;
  - les extraits aux lignes des sources ;
  - les lignes du brouillon 14 citées dans la note seule (83, 344, 353, 354) ;
  - la ligne du registre pour GO-2026-11-21-84, cité sans « chemin:ligne ».
