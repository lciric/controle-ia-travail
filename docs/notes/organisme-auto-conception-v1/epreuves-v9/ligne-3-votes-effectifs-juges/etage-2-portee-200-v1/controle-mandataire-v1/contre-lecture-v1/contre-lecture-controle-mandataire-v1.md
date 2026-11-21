# Contre-lecture du contrôle du mandataire, v1

Contre-lecteur du contrôle du mandataire, modèle S. 2026-11-21. Classe B. Pièce de référence : additif 6 v2, § 9 (l. 287 à 323), décision R-4325.

## Verdict : Conforme, avec trois réserves non bloquantes (points 2, 8, 9)

1. **Table d'empreintes** : `sha256sum -c` donne OK pour les quatre fichiers.

2. **Le programme fait ce que la règle exige.** Lu en entier (145 lignes).
   - HTTPS_PROXY non vide : contrôlé (absente, vide, espaces seuls : refus). Contrôle de plus, utile : `https_proxy` minuscule vide ou différente refusée, car urllib la préfère (l. 2546 à 2552).
   - NO_PROXY couvre 127.0.0.1 : contrôlé, chaque forme présente doit couvrir.
   - Bibliothèque standard seule : `ipaddress`, `json`, `os`, `sys`, `urllib.request`. Oui.
   - Aucune fuite : la valeur de HTTPS_PROXY n'entre dans aucun motif. De NO_PROXY ne sort que « 127.0.0.1 », « * » ou une plage réécrite par `ipaddress`. Le motif d'erreur interne ne porte que le nom du type d'exception. Les essais de fuite passent.
   - Codes : 0 si tenu, 3 si refus, erreur interne dans `evaluer` comprise (bloc `except Exception`).
   - **Réserve mineure** : `print` et `json.dumps` sont hors du `try`, et les imports sont avant. Une sortie standard fermée ou un import en échec donnerait une trace et le code 1, non 3. Tout code non nul reste un refus pour un appelant prudent ; à dire dans le mandat de lancement (« tout code autre que 0 est un refus »).

3. **Écart CIDR : lecture d'urllib vérifiée.** `/usr/local/lib/python3.13/urllib/request.py`, l. 2555 à 2587 : `no_proxy == '*'` n'est vrai que pour la valeur entière, sans retrait d'espaces (l. 2570) ; sinon découpage sur les virgules, comparaison de chaînes et de suffixes de nom (l. 2576 à 2585). Aucune lecture de plage CIDR. Les affirmations du développeur sur urllib sont exactes.

4. **Mais la raison donnée est inexacte pour la porte de plafond.** Le rapport (§ 2) dit que la porte enverrait 127.0.0.1 au mandataire avec une plage seule. Or `scripts/porte_plafond_relais_v1.py`, l. 45, ouvre avec `urllib.request.ProxyHandler({})` : la porte **n'emploie aucun mandataire, quel que soit NO_PROXY**. La condition (b) ne protège donc pas la porte. Elle protège, à titre de précaution, les autres clients des relais (client `claude_sdk`, commande du juge Argon, python lancé par le script bash), dont je n'ai pas lu le code.

5. **Avis sur l'écart : juste dans le sens, à justifier autrement.** L'écart ne peut produire qu'un refus de trop, jamais un « tenu » de trop : il est sûr (R5, aucun repli silencieux). Il coûte une ligne côté exécutant (ajouter l'élément exact `127.0.0.1`, qu'aucun client courant ne lit mal). Je le garde, en corrigeant la phrase du rapport : l'urllib de la porte n'est pas en cause (point 4) ; le motif est « le seul lecteur de plages n'est pas garanti chez les clients des relais ; l'élément exact est lu par tous ». Le rapport doit nommer qu'il s'agit d'un écart au brief, déjà fait au § 6, n° 1 ; la mère tranche.

6. **Formes en minuscules : justes et cohérentes avec urllib** (`getproxies_environment`, l. 2530 à 2552). Le nom se lit sans tenir compte de la casse à la première passe ; la minuscule gagne à la seconde ; une minuscule vide retire l'entrée. Exiger que chaque forme présente couvre est donc sûr pour urllib et pour les clients qui préfèrent la majuscule. Cas non traité, sans importance sous `env -i` et liste blanche : un nom en casse mixte (`Https_Proxy`).

7. **Essais** : `pytest` rejoué, **36 passed** en 0,28 s. Couverture R5 : chaque condition a un cas sain et des artefacts. HTTPS_PROXY : 4 artefacts, minuscule seule, vide, différente, identique. NO_PROXY : absente, vide, espaces, virgules, sans 127, localhost seul, plage, étoile (3 formes), suffixe, port, minuscules (5 cas). Fuite : 3 en processus, 3 en sous-processus `-I -B`, plus erreur interne.
   - Artefacts manquants, non bloquants : `127.0.0.1/32` ; une plage IPv6 (`::1/128`) ; `HTTP_PROXY`/`http_proxy` hors périmètre ; sortie standard fermée (point 2) ; un test qui fige que la porte est insensible à NO_PROXY (point 4).

8. **Passe** : `/usr/local/bin/python3 -I -B` rejouée vers `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-controle-mandataire/passe-rejouee.txt` ; `cmp` avec `passe-environnement-v1.txt` : **identique** (aucune sortie, empreinte `fea17979…0498`). Réserve connue du rapport : elle juge l'environnement de cette session, non celui de l'exécutant ; elle doit être relancée au mandat de lancement.

9. **Points laissés ouverts au § 6 : aucun ne bloque.**
   - n° 1 : écart CIDR, tranché par la mère ; voir points 4 et 5.
   - n° 2 : client du juge Opus non lu. Conséquence : la règle exige l'élément exact, plus étroite, donc sûre. Non bloquant.
   - n° 3 : le mandat de lancement doit lancer le contrôle dans l'environnement transmis au geste 9, avec `NO_PROXY` et `no_proxy` à la fois ; **à écrire au mandat**, c'est la condition réelle de validité de la passe.
   - n° 4 à 6 : sans effet sur le verdict.

— contre-lecteur du contrôle du mandataire, modèle S
