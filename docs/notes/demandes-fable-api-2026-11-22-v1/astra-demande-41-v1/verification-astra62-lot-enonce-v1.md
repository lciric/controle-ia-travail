# Vérification du script de lot Astra 6.2 pour un énoncé scellé — v1 (22 novembre 2026)

Pièce d'instrument (classe B). Contre-lecture en lecture seule, sans réseau, par une session fille (Opus 5.5).
Pièces lues : `astra62_lot_enonce_v1.py` (b88cba81…6630bc) et `test_astra62_lot_enonce_v1.py` (b88b277d…bd9f37),
compagnons conformes ; source `astra62_lots_v1.py` et sa vérification, branche `lot/compte-organisme-v1` ;
garde `src/controle_ia/relecture_fable_api_v5.py` (052ea1e2…8423bdb8, compagnon conforme), fonction `garde_motifs`.
Mutations et sondes faites hors du dépôt, dans le bloc-notes de la session.

## Verdict
CONFORME AVEC RÉSERVES. Aucun défaut fort. Deux défauts moyens, à corriger avant la relève (le premier) et avant
la soumission (le second). Une réponse incomplète ne peut pas être écrite comme réponse.

## 1. Écart à la source
L'écart se limite pour l'essentiel à ce que dit le docstring. Écarts non dits, tous sans danger :
- `main` prend un paramètre `transport` (pour les essais) ;
- `--registre-go` n'a plus de défaut et devient exigé (c'est la correction de la réserve 3, non nommée ainsi) ;
- la ligne de soumission du journal porte en plus l'empreinte de l'énoncé, l'effort et la sortie maximale ;
- la relève exige aussi `--enonce` et `--empreinte`, mais ne s'en sert que pour les vérifier (voir défaut moyen 1) ;
- `soumettre` lit l'identifiant par `.get("id")` au lieu de `["id"]` : une réponse sans identifiant ne bloque plus
  (voir défaut faible 3).

## 2. Gardes, par mutation (22 mutations, 17 essais)
Tuées (un essai échoue) : compagnon de l'énoncé, garde de motifs, GO, pire au-delà du plafond (et pire sans la
sortie), relève incohérente (supprimée, ou réduite à « l'identifiant est présent »), sortie du lot non JSON,
réseau, relève répétée, fin autre que « stop », modèle servi autre, texte vide, effort.
Survivantes (aucun essai ne la tient ; le code réel est juste, vérifié par sonde) :
- empreinte du fichier contre `--empreinte` : un fichier modifié avec son compagnon et `--empreinte` d'origine n'est
  testé nulle part. Sonde : refus correct.
- clé affichée sur la sortie ou l'erreur standard : l'essai ne regarde que le journal. Sonde (soumission, relève,
  refus) : la clé n'apparaît ni sur les sorties, ni au journal, ni dans les fichiers écrits.
- lecture du lot non JSON (`json_ou_refus`) : non testée. Sonde : refus nommé.
- mode « xb » des fichiers neufs : masqué par le contrôle du dossier neuf.
- texte fait de blancs : seul le texte vide est testé. Sonde : « défaut », correct.
- ligne en erreur ou statut autre que 200 avec fin « stop » : non testé. Sonde : « défaut », correct.
- refus des redirections : non testé (comme dans la source).

## 3. Calcul du pire
Majorant, sous réserve du tarif. Entrée : octets du JSON des messages (au moins un octet par jeton ; les caractères
non ASCII comptent six octets ; l'enveloppe JSON couvre les jetons de cadrage du message). Sortie : 96 000 jetons au
tarif de sortie. Les jetons de raisonnement sont compris dans `max_completion_tokens` et dans `completion_tokens`,
donc dans le pire et dans le coût relevé. Pire à vide : 1,92 USD ; plafond atteint vers 616 000 octets d'énoncé.
Le tarif des lots (5 / 20 USD le million) est repris du lot 12 et n'est pas vérifiable ici sans réseau ; un éventuel
tarif majoré pour les invites très longues n'est pas prévu (sans objet si l'énoncé est court).

## 4. Réponse incomplète écrite comme réponse
Aucune voie trouvée. « Réponse » exige à la fois : fin « stop », modèle servi conforme (`gpt-6.2-astra` ou suffixe
de chiffres ; `gpt-6.2-astra-mini` refusé), texte non vide après retrait des blancs, pas de champ d'erreur, statut 200,
une seule ligne d'identifiant attendu, nombre égal au total du lot. Fins « length », filtre, refus du modèle (contenu
nul), statut 500, ligne en erreur : toutes rendent « défaut ». Seule voie restante : une réponse complète, mais d'un
autre lot (défaut moyen 1).

## 5. Réserves de la vérification du lot 12
1. Sortie non JSON : corrigée (refus nommé, code 2, brut versé avant, journal vide) ; étendue à la lecture du lot.
2. Relève répétée : corrigée (refus nommé avant toute écriture, dossier neuf exigé).
3. Registre de GO par défaut : corrigée (exigé). Erreur réseau : corrigée pour `URLError` et `OSError` ; restent non
   rattrapées `http.client.IncompleteRead` et les erreurs de `e.read()` (défaut faible 1).

## Défauts
Moyens :
1. La relève n'est liée ni à la soumission ni à l'énoncé : tout lot portant l'identifiant « astra62-enonce » est
   écrit comme réponse à l'énoncé donné (sonde : lot étranger, « completed », fichier de réponse écrit).
   Correction : exiger que `--lot` égale le `lot_id` de la ligne de soumission du journal et que l'empreinte de
   l'énoncé égale son `enonce_sha256`.
2. Rien n'empêche deux soumissions avec deux journaux différents (sonde : deux lots créés), soit le double du
   plafond de 5 USD sous un seul GO. Correction : un témoin de soumission unique par énoncé (fichier neuf en « x »
   à côté de l'énoncé ou chemin de journal fixé), refus s'il existe.
Faibles :
1. Traces au lieu de refus nommés (code 1, mais rien ne part) : compagnon vide (`IndexError`), énoncé ou registre
   absent (`FileNotFoundError`), lot JSON qui n'est pas un objet (`AttributeError`), `IncompleteRead`.
   Correction : rattraper ces cas en `Refus`.
2. Lot « expired », « failed » ou « cancelled » : rien n'est relevé, pas même le fichier d'erreurs.
   Correction : relever aussi les fichiers présents de ces lots, en « défaut ».
3. Téléversement sans identifiant : la création du lot part avec `input_file_id` nul ; lot sans identifiant :
   journal à `null`, code 0. Correction : refuser si l'identifiant manque.
4. Le fichier de défaut s'appelle `reponse-astra62-v1.defaut.md` : un motif `reponse-astra62-v1*` le prend avec la
   réponse. Correction : le nommer `defaut-astra62-v1.md`.
5. Trous d'essais listés au point 2. Correction : un essai par mutation survivante.
6. Le GO vérifié n'est qu'un début de ligne ; GO-2026-11-22-74 est absent de `registres/go.md` au commit 337ce6c3d
   (refus attendu tant qu'il n'y est pas). Information, pas un défaut du code.

## Essais lancés
- `PYTHONPATH=src python -m pytest -q test_astra62_lot_enonce_v1.py` : 17 réussis.
- 22 mutations : 15 tuées, 7 survivantes (point 2).
- 20 sondes sur le code réel, transport factice, aucun appel réseau (résultats cités plus haut).
