# Sonde complète des quatre relais sous le code v74 — devis, commande et texte des deux lignes de GO proposées — v1

Écrit par la session du compte organisme (modèle A) à 2026-11-14T12:23:11Z (`date -u`), pour la mère (R-2738), qui les inscrit sur le mot de Lazar
« Option (a) ». **Aucune ligne n'est inscrite ; rien n'est lancé.** Lignes déjà servies : GO-2026-11-13-04 et -05 (sonde v71),
GO-2026-11-14-02 (sonde du seul relais Astra), GO-2026-11-14-07 et -08 (sonde complète v73, relevé `35afab77…`, refusé au bloc :
Argon sans réflexion, règle non confirmable). Le mode réel exige un relevé fait **sous le code v74** (version `releve-sonde-pilote-v74`,
empreintes du code et de la configuration au relevé) : le relevé v73 ne le remplace pas.

## Ce qu'elle fait

Sous-commande `sonde` du lanceur v74 (`demonstrations/pilote_mr2_v74.py`), module de la sonde v74 (`pole/sonde_pilote_v74.py`),
configuration v12 (`f69503dd…`, inchangée) : quatre relais, deux appels chacun (borne gelée, puis 256 jetons), consignes v12 ;
conclusions v74 (pour Argon : règle confirmée **ou** « aucune réflexion cachée » : aucun champ de réflexion aux deux appels et total
d'usage = entrée + sortie) ; relevé et dossier entier versés ; puis `bloc --releve-sonde` rend le bloc gelé définitif si toutes les
conclusions exigées sont vraies. Si Argon est dit « sans réflexion », le mode réel du pilote s'arrêtera si un champ de réflexion lui
apparaît.

## Devis (USD ; prix de la configuration ; console lue par Lazar)

| relais | ligne | pire cas | part (plafond du relais) | mesuré à la sonde complète v73 (mêmes consignes) |
|---|---|---|---|---|
| `fable52` | s1 | 2,588224 | 2,59 | 0,018528 |
| `opus55` | s1 | 1,794112 | 1,80 | 0,009184 |
| `argon` | s2 | 1,835280 | 1,84 | 0,03505 |
| `astra` | s2 | 1,835280 | 1,84 | 0,0165 |
| **total** | | **8,052896** | **s1 4,39 ; s2 3,68** | **0,079262** (attendu du même ordre) |

Même réserve qu'à la v73 : le pire cas d'Argon n'est borné par la borne gelée que si son plafond de sortie couvre la réflexion ;
sous la v74, une réflexion qui apparaîtrait à la sonde ferait juger la règle par les votes (et serait comptée par la règle gelée,
« ajoutée », la plus prudente pour le coût).

## Commande exacte (une seule invocation)

```
cd /home/user/controle-ia-travail && env -i PATH=/usr/bin:/bin HOME=/root HTTPS_PROXY="$HTTPS_PROXY" NO_PROXY="$NO_PROXY" \
    SSL_CERT_FILE="$SSL_CERT_FILE" REQUESTS_CA_BUNDLE="$REQUESTS_CA_BUNDLE" RR_ANTHROPIC_API_KEY_RIGAUD="$RR_ANTHROPIC_API_KEY_RIGAUD" \
    GEMINI_API_KEY="$GEMINI_API_KEY" OPENAI_API_KEY="$OPENAI_API_KEY" \
    /usr/local/bin/python3 -I -B ARBRE_V74/orchestrator/demonstrations/pilote_mr2_v74.py sonde \
    --go-sonde-credits GO-S1 --go-sonde-hors GO-S2 --registre-go REGISTRE_GO_DE_MAIN \
    --registre-lancements /home/user/hors-depot/lancements-sonde-pilote-mr2.jsonl \
    --sortie /home/user/hors-depot/sonde-complete-v74 --borne-courte
```

`ARBRE_V74` : l'arbre de l'organisme reconstruit depuis le paquet v74 (`organisme-v74-pilote-mr2-compte-organisme-v1.bundle`,
`1cda2feb88e297d758bed7d0bb30d93cbe9b196ac3ab789826d39cfa4506d48b`, tête `605e0f60f3eed0948948e6a4eb15cb73de1d03de`, prérequis `e7daf32`, contre lequel il est fait) ; `REGISTRE_GO_DE_MAIN` : copie hors dépôt de `registres/go.md` de `main` portant les deux lignes (empreinte au
journal) ; registre des lancements : celui qui porte déjà les lignes servies (versé après la sonde v73). Contrôles avant l'appel :
noms non vides (par leur nom), dossier de sortie absent, ports 8811 à 8814 libres, lignes lues au montant exact par le lecteur gelé,
premier lancement admis, arbre propre à la tête du paquet. Puis `bloc --releve-sonde /home/user/hors-depot/sonde-complete-v74/releve-sonde-pilote-v74.json`.

## Lignes proposées, mot pour mot, non inscrites

```
| GO-AAAA-MM-JJ-NN (s1) | AAAA-MM-JJ | calcul | Pilote MR-2 : sonde des deux relais sur crédits de Claude (configuration v12, lanceur v74), avant le scellement du texte : par relais, un appel à la borne gelée et un à 256 jetons, consignes de la configuration v12 (écrites pour faire réfléchir ; 100 octets au plus), par la sous-commande « sonde » du lanceur v74 ; seulement après le code v74 contre-lu ; une seule exécution (registre des lancements de la sonde) ; aucun monde, aucun résultat ; relevé et dossier entier versés, relevé cité au bloc gelé du texte ; prix rapprochés de la console par Lazar ; jamais de ligne d'extension ; arrêt par identifiant (R10) | 4.39 USD | 2026-11-30 | Lazar | R-2621, R-2690, R-2731, R-2738 ; mot direct de Lazar, verbatim : « Option (a) : code v74, réflexion absente sans effet » |
| GO-AAAA-MM-JJ-NN (s2) | AAAA-MM-JJ | calcul | Pilote MR-2 : sonde des deux relais hors crédits (configuration v12, lanceur v74), mêmes conditions que la ligne s1 | 3.68 USD | 2026-11-30 | Lazar | R-2621, R-2690, R-2731, R-2738 ; même mot direct de Lazar |
```

Le lecteur gelé lit le montant exact (4.39 ; 3.68) et exige « sonde » et « crédits de Claude » (s1), « sonde » et « hors crédits »
(s2) ; identifiants inscrits nus. À inscrire ensemble : le relevé n'est valable qu'avec les huit appels.
