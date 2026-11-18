# Prix publics des quatre relais, rapprochés des coûts du relevé de la sonde v74 — v2

- **Lecteur** : modèle A (session du compte organisme), sur le message tapé dans ce compte : « écris le message pour la nouvelle mère ;
  va regarder les prix toi meme, ecris candidat 4 ». Version 1 écrite à 2026-11-14T16:32:20Z (`date -u`). **Version 2** écrite à 2026-11-14T22:25:52Z (`date -u`) : R12, la v1 (`21bfbbd76dcd4dd5c5219054aa13ec6a93149c51fd48fc046385ca5acf3b8f10`) reste en place ; corrige l'erreur dite au journal (PO-040 : un prix de contexte long d'`astra` qui n'est pas dans la page versée) et dit partout l'**offre standard** (constats rendus en réponse par le lecteur de la vérification courte du candidat 4, journal PO-039).
- **Ce que c'est, et ce que ce n'est pas** : les **prix publics** affichés par les trois fournisseurs (pages officielles, téléchargées le
  2026-11-14 entre 16:30:30Z et 16:30:31Z), rapprochés des coûts que le relevé calcule aux prix de la configuration v12. **Ce n'est pas
  la console** : les montants réellement facturés à chaque compte (remises, crédits, arrondis) ne sont pas lus ; aucune clé ni aucune
  interface de facturation n'a été employée. Proposeurs nommés par leur clé de configuration (R-2598).

## Pages lues

| proposeur | page (fournisseur) | pièce versée | sha256 |
|---|---|---|---|
| `fable52`, `opus55` | page des prix de l'interface de Claude (`platform.claude.com/docs/en/about-claude/pricing.md`) | `pages/anthropic-pricing.md` (page entière) | `048ccb65c7aa39a16f8475d92bec1730bc9e42c63b79085e2f0f1e6e5f867cd1` |
| `argon` | page des prix de l'interface de Gemini (`ai.google.dev/gemini-api/docs/pricing`, redirigée vers `aistudio.google.com/docs/pricing`) | `pages/google-pricing-extrait-section-argon.txt` (extrait de la section ; page brute hors dépôt, `53f3e94f83b0a38a1a108692f639bf63c8eac187c30ce9125a9abdbb3afeb5c5`, non versée : clés publiques de navigateur refusées par la garde des secrets) | `d4485954b319c6668d38c467d2249f59ef1a7e195e762886a2e4d28a74d28391` |
| `astra` | page des prix de l'interface d'OpenAI (`platform.openai.com/docs/pricing`, redirigée vers `developers.openai.com/api/docs/pricing`) | `pages/openai-pricing.html` (page entière) | `099c9496f75ffe6f08a57f30b007c5abf79f6eb26ecba5ddecf50ffdf4ec8028` |

Les pages portent les identifiants des modèles : elles restent sur cette branche (règle de R-2731 pour les pièces brutes).

## Prix de l'offre standard (USD par million de jetons)

Seule l'offre standard sert : les relais appellent chaque fournisseur sans mode rapide ni lot. Les pages affichent aussi des offres
rapides plus chères que la configuration (pour `fable52`, `opus55` et `astra`) et des offres par lot moins chères : elles ne
s'appliquent pas aux appels du pilote ni de la sonde.

| proposeur | configuration v12 (entrée / sortie) | prix public lu (entrée / sortie) | écart |
|---|---|---|---|
| `fable52` | 8 / 40 | 8 / 40 | égal |
| `opus55` | 4 / 20 | 4 / 20 | égal |
| `argon` | 10 / 50 (« barème prudent supposé ») | **2 / 10 jusqu'au 30 novembre 2026 ; 4 / 20 à partir du 1er décembre 2026** ; « Output price (including thinking tokens) » | public **au-dessous** de la configuration, avant comme après le 1er décembre |
| `astra` | 10 / 50 (« barème prudent supposé ») | 10 / 50 (offre courte, au plus 272 000 jetons d'entrée ; le prix de l'offre longue n'est pas dans la page versée, qui n'en porte que le bouton ; hors de portée : texte servi au plus 52 000 octets) | égal |

**Aucun prix public de l'offre standard (entrée ou sortie) ne dépasse celui de la configuration v12**, ni aujourd'hui ni après le
1er décembre : les pires
cas et les parts restent des bornes (préalable 3 du préenregistrement). Non lu sur la page d'OpenAI : que les jetons de raisonnement
soient facturés comme sortie (la page ne le dit pas ; le compte de sortie du fournisseur les inclut, `completion_tokens` ⊇
`reasoning_tokens`, et le relevé les compte ainsi).

## Rapprochement (programme `rapprocher_prix_v1.py`, `224c99d6919beb5e5465e89af505aecb722631b51e03e4d8229d7f78b5953d5c` ; sortie `rapprochement-prix-sonde-v74-v1.json`, `af1f80f25c6bc8441438419bb74607977c0907218fde3b2457c0567c47a3f2f9`)

Par appel : jetons d'entrée de l'usage brut, sortie comptée du relevé ; coût aux prix de la configuration recalculé (**égal au coût du
relevé pour les huit appels**) et coût aux prix publics.

| proposeur | appel | entrée | sortie comptée | coût du relevé | coût aux prix publics |
|---|---|---|---|---|---|
| `fable52` | borne gelée | 58 | 191 | 0,008104 | 0,008104 |
| `fable52` | borne courte | 48 | 256 | 0,010624 | 0,010624 |
| `opus55` | borne gelée | 58 | 198 | 0,004192 | 0,004192 |
| `opus55` | borne courte | 48 | 256 | 0,005312 | 0,005312 |
| `argon` | borne gelée | 69 | 794 | 0,04039 | 0,008078 |
| `argon` | borne courte | 61 | 256 | 0,01341 | 0,002682 |
| `astra` | borne gelée | 38 | 72 | 0,00398 | 0,00398 |
| `astra` | borne courte | 32 | 256 | 0,01312 | 0,01312 |
| **total** | | | | **0,099132** | **0,056092** |

La dépense à inscrire reste celle du relevé (**0,099132 USD**, prix de la configuration, prudente) ; aux prix publics de l'offre
standard, elle serait de
0,056092 USD (`argon` cinq fois moins cher que sa configuration jusqu'au 30 novembre). Le montant réellement facturé n'est lu que
sur les consoles des comptes.

## Réserves

1. Prix publics, non facturés : un compte peut être facturé autrement (crédits, remises). La lecture de la console prévue par le
   candidat 3 (préalable 3) n'est pas faite ; ce relevé la remplace sur le seul message cité, ce qui change un préalable du texte :
   **à inscrire par la mère** (nœud).
2. Le prix d'`argon` double le 1er décembre 2026 ; il reste sous la configuration. Le pilote (échéance des lignes : 30 novembre)
   tournerait sous le prix actuel.
