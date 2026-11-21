# Mot de relance de l'étage 2 de la ligne 3, après la panne du geste 9 — v2

Version 2, écrite le 2026-11-21T09:51:30Z (`date -u`) : la v1 corrigée selon sa vérification (`prereg/organisme-auto-conception-v9/verification-mot-de-relance-etage-2-v1.md`, 18088ca4…), corrections 1 et 2 exigées et 3 et 4 recommandées, toutes portées. V1 écrite par la session mère le 2026-11-21T09:47:04Z (`date -u`), à l'exécutant de l'organisme. Il complète le mot de départ v2 scellé (`prereg/organisme-auto-conception-v9/mot-de-depart-etage-2-ligne-3-v2.md`, c89ec85b…), qui reste en vigueur pour tout ce que ce texte ne change pas. Accord de dépense : GO-2026-11-20-68 (88,36 USD). Mot de Lazar pour la relance, donné dans la session de l'organisme vers 09:44Z, cité par le manifeste du lancement des relais de rang 2 (50dbdf54…) : « je confirme : lance les deux relais de rang 2 et la relance de l'étage 2, sous GO-2026-11-20-68 ».

## La panne

- Geste 9 lancé à 07:03:01Z en tâche de fond de l'outil ; coupé vers 09:03Z par la limite de deux heures de l'outil (sortie « [killed] », ni ligne ni code). Ce n'est pas un arrêt écrit du programme (code 3) : c'est une panne au sens de l'additif 6 (geste 9, « Relance après une panne ») et du mot de départ v2 (pas 5).
- Pas 6 fait : relevé des relais à 09:03Z (relais Claude : 18,848097 USD dépensés, 704 appels, 0 refus ; relais Argon : 1 000 appels, tous au statut 200), arrêt par identifiant de processus (7533 puis 7563, preuve par stat à 09:03:52Z), inventaire de S sans lecture des verdicts (500 entrées de conservation), manifeste v4 (ac4e2b2a…).

## La relance, selon l'additif 6, § 9, et le geste 9

- Relais de rang 2, lancés à l'identique de la procédure du geste 8 : relais Claude au processus 23274, port 8787, plafond 88,36 (égal à la constante PLAFOND_C que le code compare ; écart accepté par la mère, R-4472, à l'option (a) de R-4471 mais à la lettre de l'additif 6, § 9 et § 11, n° 10 : le relais neuf repart de zéro, son plafond ne borne donc plus la dépense de la ligne sur la clé Claude (au pire 18,848097 + 88,36 = 107,208097 USD si le compteur faillait) ; la seule garde de la ligne est le compteur du programme, qui relit son journal et reprend à son propre cumul compté, les deux juges compris, qui doit être au moins égal aux 18,848097 USD relevés au relais Claude de rang 1) ; relais Argon au processus 23457, port 8788, 2 410 appels au plus ; fichiers de rang 2.
- Déclaration v2 : `DECLARATION` = `/home/user/relais-ligne-3-etage-2-portee-200-v1/declaration-relais-ligne-3-etage-2-v2.json`, `HEX_DECLARATION` = `5617d47adf71d0b4e3c2197b5211aeea63ecc5fa2673ec8a792331dd78c69664` ; elle ne diffère de la v1 que par la version et les deux identifiants de processus.
- Même sortie `S`, même banque (`HEX_BANQUE` 70d35e54…), mêmes témoins de plomberie `t01,t07`, même commande ; le compteur relit son journal et ne repart jamais de zéro ; la relance est écrite au manifeste (exécution K + 1).

## Ce que l'exécutant fait, dans cet ordre

1. Pas 1 du mot de départ v2, à l'identique, plus ce mot de relance et son compagnon, avec la déclaration v2 à `HEX_DECLARATION` v2 et les relais vivants aux processus 23274 et 23457 (`stat -c %n /proc/<identifiant>`).
2. Relevé du relais Claude de rang 2 par `curl -s --noproxy '*' http://127.0.0.1:8787/relais/etat`, rendu à la mère avant le lancement (dépense nulle attendue).
3. Contrôle du mandataire, commande à la lettre du mot de départ v2 ; tout code non nul est un refus :

```
env -i PATH="$PATH" HOME="$HOME" GO_ID=GO-2026-11-20-68 HTTPS_PROXY="$HTTPS_PROXY" https_proxy="$https_proxy" NO_PROXY="$NO_PROXY" no_proxy="$no_proxy" SSL_CERT_FILE="$SSL_CERT_FILE" REQUESTS_CA_BUNDLE="$REQUESTS_CA_BUNDLE" CURL_CA_BUNDLE="$CURL_CA_BUNDLE" NODE_EXTRA_CA_CERTS="$NODE_EXTRA_CA_CERTS" /usr/local/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1/controle-mandataire-v1/controler_mandataire_etage_2_v1.py
```

4. `git -C /home/user/controle-ia-travail fetch origin main`.
5. Geste 9, une seule commande, à la lettre, seules `DECLARATION` et `HEX_DECLARATION` remplacées par leurs valeurs v2, **lancée détachée de l'outil** : `setsid nohup <commande> > <journal> 2>&1 &`, identifiant de processus (`$!`) écrit dans un fichier et vérifié par `stat -c %n /proc/<identifiant>` et `/proc/<identifiant>/cmdline` (l'interpréteur et le code d'appel), suivi par ce seul identifiant (R10), jamais par motif ; le code se lit à la seule ligne, écrite au journal : ligne `refus`, 2 ; `arret` nul, 0 ; `arret` nommé, 3 ; processus mort sans ligne, panne :

```
env -i PATH="$PATH" HOME="$HOME" GO_ID=GO-2026-11-20-68 HTTPS_PROXY="$HTTPS_PROXY" https_proxy="$https_proxy" NO_PROXY="$NO_PROXY" no_proxy="$no_proxy" SSL_CERT_FILE="$SSL_CERT_FILE" REQUESTS_CA_BUNDLE="$REQUESTS_CA_BUNDLE" CURL_CA_BUNDLE="$CURL_CA_BUNDLE" NODE_EXTRA_CA_CERTS="$NODE_EXTRA_CA_CERTS" /usr/local/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1/code-appel-v4/epreuve_juges_reels_ligne_3_v4.py --reel --go-id GO-2026-11-20-68 --banque /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1/execution-v1/composition/banque-temoins-ligne-3-v1.json --banque-sha 70d35e5479802ba355ac218e23a93b4f1dc4e29fffe82dfabef5fb5b78394bbd --declaration /home/user/relais-ligne-3-etage-2-portee-200-v1/declaration-relais-ligne-3-etage-2-v2.json --declaration-sha 5617d47adf71d0b4e3c2197b5211aeea63ecc5fa2673ec8a792331dd78c69664 --sortie /home/user/sorties-ligne-3-etage-2-portee-200-v1 --plomberie t01,t07 --nom-cle-claude RR_ANTHROPIC_API_KEY_LUC
```

6. Relevé du relais Claude à mi-course (vers la moitié des appels restants), rendu à la mère sans arrêt : deux lectures : le cumul compté par le programme, relu à son journal, dépense d'avant la panne comprise (ne rien lui ajouter), reste sous 88,36 ; la dépense du relais Claude de rang 2 plus 18,848097 ne dépasse pas ce cumul compté (le compteur ne compte jamais moins que la dépense réelle du juge Opus). Un écart à la seconde lecture est rendu à la mère sur-le-champ. Mêmes deux lectures au relevé de fin (pas 7).
7. À la fin (code 0 ou 3, ou panne) : la seule ligne imprimée et le code ; relevé puis arrêt des relais 23274 et 23457 par identifiant, preuve par stat ; verdicts de la moitié « lecture » déposés scellés, non ouverts avant le geste 12. Une nouvelle panne : mêmes gestes, relance seulement sur un mot de la mère.
