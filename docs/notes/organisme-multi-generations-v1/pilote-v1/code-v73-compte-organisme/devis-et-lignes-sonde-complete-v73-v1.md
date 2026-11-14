# Sonde complète des quatre relais (configuration v12, lanceur v73) — devis, commande et texte des deux lignes de GO proposées — v1

Écrit par la session du compte organisme (modèle A) à 2026-11-14T10:54:09Z (`date -u`), pour la mère, qui le soumet à Lazar (R-2712). **Aucune
ligne n'est inscrite ; rien n'est lancé.** Les lignes GO-2026-11-13-04 et -05 ont servi (sonde v71) ; GO-2026-11-14-02 a servi
(sonde du seul relais Astra). Le mode réel du pilote exige le relevé de **cette** sonde (version `releve-sonde-pilote-v72`, fait par
le lanceur v73 sous la configuration v12 : empreintes de la configuration et du code au relevé).

## Ce qu'elle fait

Sous-commande `sonde` du lanceur v73 (`demonstrations/pilote_mr2_v73.py`, `88f99766…`), module de la sonde v72
(`636d5a95…`), configuration v12 (`f69503dd…`) : quatre relais (`fable52`, `opus55`, `argon`, `astra`), deux appels chacun
(borne gelée, puis 256 jetons), consignes v12 (94 et 99 octets) ; deux lignes à part, lues au montant exact (s1 4,39 ; s2 3,68) ;
registre des lancements (une seule exécution par ligne) ; relevé et dossier entier versés ; `bloc --releve-sonde` rend alors le bloc
gelé définitif du texte du pilote, si toutes les conclusions sont vraies (dont `reflexion_observee` pour `argon` et `astra`).

## Devis (USD ; prix de la configuration, standard pour Astra et Argon supposé au même barème ; console lue par Lazar)

| relais | ligne | pire cas, borne gelée | pire cas, 256 jetons | pire cas | part (plafond du relais) | attendu (estimé) |
|---|---|---|---|---|---|---|
| `fable52` (64 000) | s1 | 2,568992 | 0,019232 | 2,588224 | 2,59 | < 0,40 |
| `opus55` (89 000) | s1 | 1,784496 | 0,009616 | 1,794112 | 1,80 | < 0,20 |
| `argon` (36 000) | s2 | 1,811240 | 0,024040 | 1,835280 | 1,84 | < 0,20 |
| `astra` (36 000) | s2 | 1,811240 | 0,024040 | 1,835280 | 1,84 | ≈ 0,02 (mesuré à la sonde d'un relais : 0,0167) |
| **total** | | | | **8,052896** | **s1 4,39 ; s2 3,68** | **< 0,85** |

Réserves de coût : le pire cas d'`argon` (réflexion « ajoutée ») n'est borné par la borne gelée que si le plafond de sortie couvre
la réflexion ; sinon un dépassement est **constaté après coup** (arrêt, relevé partiel, `astra` non sondé, appelé après) ; un tel
relevé partiel est refusé par le mode réel. Les consignes v12 font réfléchir aussi les deux relais de Claude à la borne gelée.

## Commande exacte (une seule invocation ; identifiants des lignes à recopier à l'inscription)

```
cd /home/user/controle-ia-travail && env -i PATH=/usr/bin:/bin HOME=/root HTTPS_PROXY="$HTTPS_PROXY" NO_PROXY="$NO_PROXY" \
    SSL_CERT_FILE="$SSL_CERT_FILE" REQUESTS_CA_BUNDLE="$REQUESTS_CA_BUNDLE" RR_ANTHROPIC_API_KEY_RIGAUD="$RR_ANTHROPIC_API_KEY_RIGAUD" \
    GEMINI_API_KEY="$GEMINI_API_KEY" OPENAI_API_KEY="$OPENAI_API_KEY" \
    /usr/local/bin/python3 -I -B ARBRE_V73/orchestrator/demonstrations/pilote_mr2_v73.py sonde \
    --go-sonde-credits GO-S1 --go-sonde-hors GO-S2 --registre-go REGISTRE_GO_DE_MAIN \
    --registre-lancements /home/user/hors-depot/lancements-sonde-pilote-mr2.jsonl \
    --sortie /home/user/hors-depot/sonde-complete-v73 --borne-courte
```

`ARBRE_V73` : l'arbre reconstruit depuis le paquet `organisme-v73-pilote-mr2-compte-organisme-v1.bundle` (`2b4017c7…`, prérequis
`e7daf32`) ; `REGISTRE_GO_DE_MAIN` : copie hors dépôt de `registres/go.md` de `main` portant les deux lignes (empreinte au
journal) ; registre des lancements : celui de la sonde d'Astra (versé, `lancements-sonde-pilote-mr2-apres-sonde-un-astra.jsonl`).
Avant l'appel : noms non vides (par leur nom), dossier de sortie absent, ports 8811 à 8814 libres ; aucune `ANTHROPIC_BASE_URL`.
Puis `bloc --releve-sonde /home/user/hors-depot/sonde-complete-v73/releve-sonde-pilote-v72.json` après la lecture des prix.

## Lignes proposées, mot pour mot, non inscrites

```
| GO-AAAA-MM-JJ-NN (s1) | AAAA-MM-JJ | calcul | Pilote MR-2 : sonde des deux relais sur crédits de Claude (configuration v12, lanceur v73), avant le scellement du texte : par relais, un appel à la borne gelée et un à 256 jetons, consignes de la configuration v12 (écrites pour faire réfléchir ; 100 octets au plus), par la sous-commande « sonde » du lanceur v73 ; seulement après le code v73 contre-lu ; une seule exécution (registre des lancements de la sonde) ; aucun monde, aucun résultat ; relevé et dossier entier versés, relevé cité au bloc gelé du texte ; prix rapprochés de la console par Lazar ; jamais de ligne d'extension ; arrêt par identifiant (R10) | 4.39 USD | 2026-11-30 | Lazar | R-2621, R-2690, R-2712 ; mot de Lazar à recopier |
| GO-AAAA-MM-JJ-NN (s2) | AAAA-MM-JJ | calcul | Pilote MR-2 : sonde des deux relais hors crédits (configuration v12, lanceur v73), mêmes conditions que la ligne s1 | 3.68 USD | 2026-11-30 | Lazar | R-2621, R-2690, R-2712 ; mot de Lazar à recopier |
```

Le lecteur gelé lit le montant exact (4.39 ; 3.68) et exige « sonde » et « crédits de Claude » (s1), « sonde » et « hors crédits »
(s2) au périmètre ; identifiants inscrits nus (R-2599). Recommandation : s1 et s2 ensemble (le relevé n'est valable qu'avec les huit
appels), une seule session tenante désignée par écrit, le crochet de garde chargé dans cette session.
