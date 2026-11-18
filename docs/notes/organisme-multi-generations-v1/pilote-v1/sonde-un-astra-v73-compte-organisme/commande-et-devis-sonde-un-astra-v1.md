# Sonde du seul relais Astra (GO-2026-11-14-02) — commande exacte et devis, écrits avant l'appel — v1

Écrit par la session du compte organisme (modèle A), à 2026-11-14T10:04:39Z (`date -u`), **avant tout appel**. Ligne : **GO-2026-11-14-02**
(`registres/go.md` de `main` à `d871d513`, ligne 321 ; calcul ; 2 USD ; échéance 2026-11-30 ; accordée par Lazar, R-2694) :
« sonde neuve du seul relais Astra, par le compte organisme, code v72 après ses corrections et leur relecture, commande exacte et
devis écrits avant l'appel, pire cas ≤ 2 USD ; une seule invocation ; clé lue par son nom sous `env -i` ».

## Code

- Arbre de l'organisme `/home/user/arbre-organisme-co/organisme`, branche `prep/organisme-v72-pilote-mr2-compte-organisme-v1`,
  tête `b3a83da` (v72 jalon 2 `e6a3a11` + v73 ; ajouts seuls contre `e7daf32`). Module de la sonde **v72** (jalon 2, ses
  corrections relues : pièce de relecture citée au journal provisoire) ; **lanceur v73**, parce que le lanceur v72 ne sait sonder
  que les quatre relais ensemble, sous les deux lignes s1 et s2 (4,39 et 3,68 USD au montant exact) : la sous-commande neuve
  `sonde-un` (v73) sonde un seul relais sous une seule ligne, au montant exact de 2 USD, mots « sonde » et « seul relais Astra »
  exigés au périmètre (lecteur gelé `lire_go_de_lignes`).
- Configuration v12 (`f69503dd…`), consignes : borne gelée (36 000 jetons) « Combien d'entiers de 1 à 10000 sont divisibles par
  7 ou 11, mais pas par 13 ? Le seul nombre. » (94 octets) ; borne courte (256 jetons) « Énumère un à un les nombres premiers entre
  1000 et 1200, en justifiant chacun par ses divisions. » (99 octets). Aucun réglage envoyé (Q-4).

## Devis (USD)

| appel | pire cas (règle de la commande : (octets + 1 024) × 10 / 10⁶ + borne × 50 / 10⁶ ; prix standard lu, R-2677) | attendu (estimé) |
|---|---|---|
| borne gelée (36 000 jetons) | 1,811240 | < 0,15 (un nombre, réflexion de quelques centaines à quelques milliers de jetons) |
| borne courte (256 jetons) | 0,024040 | ≈ 0,013 |
| **total** | **1,835280** (≤ part du relais 1,84 ≤ ligne 2,00) | **< 0,20** |

Plafond du relais : 1,84 USD (part d'Astra à la sonde de la configuration) ; deux appels au plus ; un coût lu au-dessus du pire cas
d'un appel arrête la sonde (relevé partiel). Prix réels : console lue par Lazar.

## Commande exacte (une seule invocation)

```
cd /home/user/controle-ia-travail && env -i PATH=/usr/bin:/bin HOME=/root HTTPS_PROXY="$HTTPS_PROXY" NO_PROXY="$NO_PROXY" \
    SSL_CERT_FILE="$SSL_CERT_FILE" REQUESTS_CA_BUNDLE="$REQUESTS_CA_BUNDLE" OPENAI_API_KEY="$OPENAI_API_KEY" \
    /usr/local/bin/python3 -I -B /home/user/arbre-organisme-co/organisme/orchestrator/demonstrations/pilote_mr2_v73.py sonde-un \
    --proposeur astra --go-sonde GO-2026-11-14-02 --registre-go /home/user/hors-depot/go-main-d871d513.md \
    --registre-lancements /home/user/hors-depot/lancements-sonde-pilote-mr2.jsonl --sortie /home/user/hors-depot/sonde-un-astra-v73
```

- `go-main-d871d513.md` : copie de `registres/go.md` de `main` à `d871d513` (`7082dee3…`), hors de tout dépôt.
- `lancements-sonde-pilote-mr2.jsonl` : registre des lancements de la sonde, hors de tout dépôt, amorcé par la copie du registre
  versé de la sonde v71 (`83634068…`, une ligne sous GO-2026-11-13-04 et -05) ; la ligne GO-2026-11-14-02 n'y figure pas.
- `HTTP_PROXY` n'est pas transmise : elle est absente de cette session (testée par son nom). Aucune `ANTHROPIC_BASE_URL`, aucune
  autre clé. Le crochet de garde du dépôt n'est pas chargé dans cette session (PO-001) : la session tient seule la garde.

## Vérifié à sec (sans relais, sans appel, sans clé)

La ligne réelle passe le lecteur gelé (calcul, Lazar, 2.0 USD lus, échéance 2026-11-30) ; pire cas 1,835280 ≤ part 1,84 ≤ 2 ;
premier lancement admis par le registre ; adresse d'amont `https://api.openai.com/v1/chat/completions` ; borne 36 000 ; consignes 94
et 99 octets. Essais de `sonde-un` sur la doublure : cas sain, cinq artefacts (proposeur, montant, périmètre, ligne absente, sortie
existante, clé absente), second lancement refusé, réflexion nulle nommée.

## Après l'appel

Relevé `releve-sonde-un-relais-v73.json` et dossier entier versés (pièces des deux appels, journal du relais), ligne du registre des
lancements, dépense calculée ; rapprochement de la console par Lazar. Ce relevé ne sert pas au mode réel du pilote.
