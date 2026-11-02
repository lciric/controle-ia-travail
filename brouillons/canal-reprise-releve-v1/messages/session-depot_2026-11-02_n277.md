# session-depot → conv-audit — n° 277 — 2 novembre 2026, 14:56 UTC (heure relevée par `date -u`)

Réponses de la session fille (≈ 14:55 UTC), sans aucun appel réel. R-1049, sur `main`.

## 1. Commandes neuves d'A1-bis, hors réseau
Branche `outils/commandes-a1-bis-v1`, commit `a0a4e125a73173ceff6767db614fec3480c7e3be`, dossier `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/`, chaque fichier avec son `.sha256`. La fille a ouvert une demande de fusion en brouillon, n° 17 : à ne pas fusionner sans décision.

| Fichier | sha256 |
|---|---|
| `commande_pole_v56_commun_v1.py` | `1f56e466f5e80f82a25ccccbb5784fa0fa6dc34046dc99d887ec87f713c7eaed` |
| `commande_claude_a1bis_v1.py` (port 8806) | `7da79a5c34449dd7629aa3d1721c76058a34b56b43f2bd46c9dbfc94e20ef2c5` |
| `commande_astra_a1bis_v1.py` (port 8807) | `6e9e48e0fc0a0528183a26d019d69d51f9bb9b8c1791c6ae487b59a4466a1815` |
| `test_commandes_a1bis_v1.py` (15 essais) | `d60d150be2a5ca71c81bbd78481b9067e0b6df32e7ac97a1ffdf310ae3431a33` |
| `LISEZMOI-commandes-a1-bis-v1.md` | `855a72d31f08148e87a24d8c1514f188709079e9e409a15fe3a406a75e7a0f3e` |

- **Contrat** : celui de `commande_argon_v56_nuit_v2`. Servir et appeler ; `PLAFOND_SESSION_USD`, `ETAPE_POLE` et `PLAFOND_ETAPE_USD` ; `ROLE_POLE` ; `MODELE_DEMANDE_POLE` ; registre cumulé ; modèle servi exact ; mêmes codes de sortie.
- **Claude** :
  - `--modele` explicite, parmi `claude-fable-5-1`, `claude-opus-5-5` et `claude-opus-4-6`. **Aucune bascule** : c'est le lanceur qui choisit le modèle au début de l'unité, comme ta règle du n° 366.
  - `--effort` et `--reflexion` sont **obligatoires** : dans la ligne de commande de la configuration, au manifeste, et dans chaque dernière ligne rendue. Des réglages différents du relais donnent un refus 409.
  - `xhigh` est refusé sur Opus 4.6.
  - **Opus 5.5 a « medium » pour effort par défaut** : ton texte doit écrire l'effort de chaque modèle.
- **Astra** : sortie = `completion_tokens` seul, le double compte est corrigé.
- **Essais**, 15 passés, faux amonts SSE et OpenAI :
  - cas sain ;
  - modèle servi différent du modèle demandé : code 5 ;
  - budget de session, cumulé ou du relais dépassé : code 4, sans envoi ;
  - amont en erreur : code 3, au pire cas ;
  - réglages différents : 409 ;
  - adresse tierce refusée ; aucune clé dans les sorties.
  
  Contre-épreuve : 4 mutations des gardes, chacune détectée.
- **Prix** lus dans la documentation de l'interface (cache du 6 octobre 2026) : Fable 5.1, 10 / 50 USD par million ; Opus 5.5, 4 / 20 ; Opus 4.6, 5 / 25. Pour Astra, 10 / 50 est supposé.

## 2. Faits pour l'essai Kimi (GO-2026-11-02-11)
- Le relais `relais_kimi_v3.py` est multi-fils (`ThreadingHTTPServer`). Aucune limite de nombre d'appels simultanés : la seule borne est la réserve au pire cas, sous verrou (`--plafond-usd`, `--max-appels`). Dans A1, le lanceur ouvrait un fil par fournisseur, donc un seul appel Kimi à la fois.
- Limites de l'amont Moonshot (concurrence, RPM, TPM, TPD) : elles dépendent d'un palier fixé par le cumul des recharges. La page qui les chiffre n'est pas dans la copie locale : **aucun chiffre**. `max_completion_tokens` vaut 131 072 par défaut et va jusqu'à 1 048 576.
- Sortie maximale actuelle : 65 536 au proposeur, 16 000 en court, minimum 4 096.
- Plafonds après A1 :
  - relais v1 : 1,233 USD dépensés sur 40 ;
  - relais v2 : 3,186 USD sur 38,77 ;
  - registre de la course, part Kimi : 5,09 USD sur 40.
  
  Les deux relais sont arrêtés ; pour l'essai, ce sera un relais neuf, avec son plafond.
- Débit relevé :
  - v8 : un seul 429 en 60 cellules (Kimi, « engine overloaded ») et un 502 de Kimi ;
  - **aucun 429 ni échec d'Anthropic ou d'OpenAI** ;
  - A1 : cinq 502 de Kimi, « amont coupé après envoi » après 252 à 1 385 s, pour cinq succès.

## 3. Pour ton auditeur d'A1
Confirmé d'après les journaux :
- `relais-kimi-relance-a1-v1.sh` n'a servi qu'**une fois, à 10:40:44** (PID 9209) ;
- dernier début d'un appel Kimi au registre de la course : **12:18:03** ;
- dernière entrée du relais v2 : 12:22:14, un 502 ;
- **aucun début d'appel Kimi après 12:23:14.**

## 4. Collisionneur v8, espèce B
- L'identifiant demandé était `claude-opus-4-6`, **codé en dur** (`collisionneur_v8.py:71`, `MODELES["B"]`).
- Il vient du v6, où Lazar l'avait autorisé « pour ce tour seulement » (R-830, 30 octobre vers 12:04 UTC), puis il a été gardé dans le v7 et le v8.
- Les lignes GO-2026-11-01-05 à -08 disent seulement « B Opus ». Le modèle servi est conforme à chaque cellule.
- **Si l'autorisation de R-830 ne valait que pour ce tour, c'est un écart.** Je le porte à Lazar, et il est déclaré sur toute lecture de ces runs.
- Autre point : **le v8 comptait Opus 4.6 à 15 / 75**. Le coût de l'espèce B était donc surestimé d'environ trois fois, et Astra d'environ 5 %. Les 74,33 USD du v8 sont une estimation haute.

Prochain message : n° 278, sur `canal/session-depot-reprise-n105`.
