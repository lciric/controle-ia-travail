# Vérification de la correction du relais Gemini v4 (vérification des commandes neutres par lot, constat V-1)

Contre-lecteur neuf, 18 novembre 2026. Je n'ai écrit aucune des pièces lues. Aucun appel réseau vers un fournisseur ; essais
et sondes hors réseau (faux amont local, ports éphémères), `PYTHONDONTWRITEBYTECODE=1`, `python3 -B`, `-p no:cacheprovider` ;
aucun `__pycache__` créé (inventaire avant et après identique, 472 dossiers préexistants). Sondes dans le brouillon de
session, hors du dépôt.

Pièces lues (empreintes SHA-256 au moment de la lecture) :
- `relais_gemini_v4.py` : `12fd475a9d26b9d6a6484249b7afc1f849e6452b6f8b34bada0c7dc2d3d3066a` ;
- `commande_gemini_lot_v1.py` : `9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75` ;
- `test_commande_gemini_lot_v1.py`, `test_relais_gemini_v4_suite_v2.py` (même dossier).

## Verdict

**Autorisable.** La correction de V-1 tient : c'est l'objet vérifié, ré-encodé, qui part à l'amont, avec un `Content-Length`
juste ; aucune des 58 formes détournées essayées sur le corps ne passe ; le corps de la commande passe ; 85 essais passent.
Aucun constat bloquant ni significatif ; six constats mineurs, à reprendre à la prochaine version.

## Points vérifiés

1. **Ce qui part est l'objet ré-encodé** (lignes 328-366, 522-537). Bout en bout, faux amont qui enregistre les octets bruts :
   un corps reçu avec espaces, échappements `_`, `é`, paire de substitution d'émoji arrive à l'amont égal octet pour
   octet à `json.dumps(objet, ensure_ascii=False).encode("utf-8")`, différent des octets reçus ; `Content-Length` amont = 191 =
   longueur du corps reçu par l'amont. La vérification précède le compte du lot et l'envoi (ligne 522 avant 527) ; un refus
   ne compte ni appel ni lot. Un `Content-Length` client plus court que le corps : JSON tronqué, 403, rien envoyé.
2. **Formes détournées** (58 cas sur `motif_contenu_lot`, plus 6 bout en bout). Refusées : clé en double à chaque niveau
   (racine, `batch`, `input_config`, élément, `request`, `generationConfig`, `thinkingConfig`, et aussi dans `contents` et
   `metadata`), y compris une double écrite par échappement (`display_name`) ; `inputConfig`, `displayName`,
   `generation_config`, `thinking_config`, `system_instruction`, `safety_settings` ; `batch.model` (aussi écrit `model`),
   `model` par requête, à l'élément, à la racine, sous `requests` ; `file_name` (lot depuis un fichier) ; `tools`,
   `toolConfig`, `tool_config`, `cachedContent`, `cached_content`, `candidateCount`, `candidate_count`, `thinkingLevel`,
   `labels` ; clé vide, clé avec caractère nul ; types inattendus à chaque niveau (liste, chaîne, `null`) ; liste de requêtes
   vide ou objet au lieu de liste ; deux requêtes au-delà de la borne ; marque d'ordre d'octets, texte après l'objet, deux
   objets, Latin-1. Rien n'atteint l'amont dans ces cas.
3. **Corps de la commande** (lignes 175-178 de `commande_gemini_lot_v1.py`, encodé comme ligne 86) : passe ; l'amont reçoit
   le même objet, `Content-Length` juste. Couvert aussi par l'essai `test_sain_par_le_relais`.
4. **Essais** : `test_commande_gemini_lot_v1.py` et `test_relais_gemini_v4_suite_v2.py` : 85 passent (40 s).
5. **En-tête, point 6** (lignes 22-26) : vrai pour l'essentiel (lecture sans clé en double, liste de clés permises, champs
   nommés refusés, objet ré-encodé qui part, lots retenus en mémoire). Une imprécision, constat M-4.

## Constats (tous mineurs)

- **M-1 — Chaîne de requête et en-têtes du client relayés tels quels** (lignes 179-181, 532). Sur `batchGenerateContent`,
  `?batch.model=models/autre&$fields=name&alt=json` part tel quel à l'amont, ainsi que `Content-Type`,
  `X-HTTP-Method-Override` et `X-Goog-FieldMask` posés par le client. Mineur : avec le corps entier lié à la requête, la
  transcription HTTP de Google ne lie pas de champ par la chaîne de requête (seuls les paramètres système restent) ; je ne
  peux pas le vérifier hors réseau. Correction peu coûteuse : refuser toute chaîne de requête et ne relayer que
  `Content-Type: application/json` sur la création d'un lot (la commande n'utilise ni l'une ni les autres).
- **M-2 — Deux entrées font tomber le traitement sans réponse** (lignes 333 et 366). Une chaîne avec une demi-paire de
  substitution isolée (`"\ud800"`) passe la lecture puis lève `UnicodeEncodeError` au ré-encodage, hors du `try` ; un
  imbriquement de 100 000 crochets lève `RecursionError` (non rattrapée). Le client reçoit une connexion coupée, sans 403
  ni ligne de journal ni compte de refus ; rien n'est envoyé, le relais reste vivant. À rattraper en refus 403.
- **M-3 — `NaN` et `Infinity` passent** (ligne 333, ré-encodés ligne 366) : JSON non standard envoyé, que l'amont refusera,
  après que le lot a été compté dans `--max-lots`. `parse_constant` qui refuse suffit.
- **M-4 — Clés vérifiées à chaque niveau parcouru, pas à tous les niveaux** (lignes 302-312, en-tête ligne 23). L'intérieur
  de `contents`, `systemInstruction`, `safetySettings` et `metadata` n'est vérifié que pour les clés en double ; par exemple
  `metadata: {"model": …, "tools": […]}` passe (sans effet : les métadonnées d'une requête sont opaques pour l'amont), et
  `{"request": {}}` passe. L'en-tête « à chaque niveau » est à lire « à chaque niveau de l'enveloppe du lot ».
- **M-5 — Borne d'octets et compteur sur le corps reçu, pas sur le corps envoyé** (lignes 520, 527, 261). Le ré-encodage
  ajoute des espaces après `:` et `,` : +15 % mesuré sur un corps compact ordinaire, +50 % pour une liste de petits nombres ;
  un corps reçu sous `--max-octets-corps` peut partir au-dessus, et `octets_envoyes` de `/relais/etat` compte les octets reçus.
  Sans effet sur le coût (le texte, donc les jetons, est inchangé). Corriger par `separators=(",", ":")` et une borne
  vérifiée sur `len(corps)`.
- **M-6 — L'essai `test_relais_relaie_l_objet_verifie_reencode`** (lignes 338-347 des essais) compare l'objet relu par le faux
  amont, pas les octets ni `Content-Length` ; il ne distinguerait pas un relais qui renverrait les octets reçus d'un corps
  sans double ni clé interdite mais à espaces différents. Mon essai bout en bout (point 1) couvre ce manque.
