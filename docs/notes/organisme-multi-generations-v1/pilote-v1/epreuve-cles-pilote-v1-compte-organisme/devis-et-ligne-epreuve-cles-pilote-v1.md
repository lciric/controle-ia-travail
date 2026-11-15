# Épreuve des trois clés du pilote MR-2 avant le lancement unique — programme, devis, texte de la ligne — v1

- **Auteur** : modèle A (session du compte organisme), à 2026-11-15T07:58:41Z (`date -u`).
- **Mot de Lazar**, tapé dans ce compte, verbatim : « (b) te demander une ligne d’épreuve à part, de quelques centimes ; » (réponse au
  risque posé à la mère dans la réponse à R-2853 : validité des trois clés non prouvée avant le lancement unique). Sans effet de nœud
  avant inscription par la mère. **Aucune ligne n'est inscrite ; rien n'est lancé.**

## Ce que fait l'épreuve

Programme `epreuve_cles_pilote_v1.py` (`f56eaecbe6f79aef7b4d40e794a0f317c8306326d8665ae532bf02efa0d8221f`) : **un appel minimal par clé**, consigne « Réponds par le seul mot OK. » (28 octets),
16 jetons de sortie au plus, aux adresses et aux modèles de la configuration v12 (`f69503dd…`) : `opus55` pour
`RR_ANTHROPIC_API_KEY_RIGAUD` (la même clé sert à `fable52`), `argon` pour `GEMINI_API_KEY`, `astra` pour `OPENAI_API_KEY`. Aucun
monde, aucun texte servi, aucune consigne du pilote, aucun résultat. Il refuse avant tout appel si une clé manque (nom seul affiché)
ou si le pire cas dépasse le montant de la ligne ; il n'imprime que, par clé, le code HTTP, « modèle servi conforme » (vrai ou faux,
jamais l'identifiant), les jetons et le coût aux prix de la configuration ; jamais une clé ni un corps. Aucune reprise. Code 0 si les
trois clés passent, 4 sinon.

Essai sans appel, sur une doublure locale (`essai-local/`) : trois clés factices lues par leur nom, « toutes_valides » vrai ; refus
« clé absente », refus « pire cas au-dessus de la ligne », refus d'une adresse non locale en mode essai ; aucune clé factice dans la
sortie.

## Devis (USD, prix de la configuration v12)

| clé (proposeur) | pire cas : (28 + 1024) jetons d'entrée × prix + 16 × prix de sortie |
|---|---|
| `RR_ANTHROPIC_API_KEY_RIGAUD` (`opus55`, 4 / 20) | 0,004528 |
| `GEMINI_API_KEY` (`argon`, 10 / 50) | 0,01132 |
| `OPENAI_API_KEY` (`astra`, 10 / 50) | 0,01132 |
| **total** | **0,027168** |

Attendu : moins de 0,002 USD. **Réserve** : chez `argon`, que `maxOutputTokens` borne aussi les jetons de réflexion n'est pas
vérifié ; la sonde v74 a montré une réflexion de 786 jetons sur un calcul, aucune sur la consigne « OK » de la sonde v71 ; au pire,
786 jetons de plus coûteraient 0,0393 USD. **Ligne proposée : 0,10 USD**, qui couvre ce cas.

## Où la placer dans la procédure (décision de la mère)

1. **Avant la location** (fin de la section 1) — recommandé : une clé morte arrête tout sans rien avoir loué ni généré ; reste une
   fenêtre de ≈ 2 h jusqu'au lancement, où une clé pourrait encore changer.
2. Juste avant l'étape 9 : fenêtre la plus courte ; mais une clé morte arrive après la location et la génération des mondes (brûlés).

Dans les deux cas, l'épreuve se joue **depuis la session qui lance le pilote** (ce sont ses clés que le pilote enverra), une seule
fois, sous `env -i` :

```
env -i PATH=/usr/bin:/bin HOME=/root HTTPS_PROXY="$HTTPS_PROXY" NO_PROXY="$NO_PROXY" SSL_CERT_FILE="$SSL_CERT_FILE" \
  RR_ANTHROPIC_API_KEY_RIGAUD="$RR_ANTHROPIC_API_KEY_RIGAUD" GEMINI_API_KEY="$GEMINI_API_KEY" OPENAI_API_KEY="$OPENAI_API_KEY" \
  python3 -I -B epreuve_cles_pilote_v1.py ARBRE/orchestrator/exemples/pilote-mr2-v70/configuration-pilote-mr2-v12.json 0.10 SORTIE_HORS_DEPOT.json
```

Code 4 (une clé au moins ne passe pas) : **aucune location, aucun lancement**, nœud. Est-ce un écart au texte scellé ? Le texte ne
prévoit pas cet appel, mais il n'en fait ni un monde, ni un appel du pilote, ni une lecture : à juger par la mère (nœud).

## Ligne proposée, mot pour mot, non inscrite

```
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | Pilote MR-2 : épreuve des trois clés du pilote (Claude, Gemini, OpenAI) avant le lancement unique, un appel minimal par clé (« Réponds par le seul mot OK. », 16 jetons de sortie au plus), modèles de la configuration v12, par le programme epreuve_cles_pilote_v1.py ; aucun monde, aucune consigne du pilote, aucun résultat ; une seule exécution, depuis la session qui lance le pilote ; clés par leur nom sous env -i ; sortie sans clé ni corps ; jamais de ligne d'extension | 0.10 USD | 2026-11-30 | Lazar | R-2853 ; mot direct de Lazar, verbatim : « (b) te demander une ligne d’épreuve à part, de quelques centimes ; » |
```
