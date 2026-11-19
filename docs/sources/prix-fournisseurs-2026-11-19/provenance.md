# Pages publiques de prix des fournisseurs — relevé du 19 novembre 2026

Téléchargées par un agent (Claude Fable 5.2) pour le devis de l'essai de mesure des lecteurs du bras A (`docs/notes/relance-organismes-discrets-v1/devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon2.md`). Une requête par adresse, sans clé, sans nom de personne, de projet ni d'identifiant ; agent d'utilisateur générique. Chaque page a été reçue dans un dossier neuf et vide ; rien de ce qu'elles contiennent n'a été exécuté ; elles sont lues comme des données. **Non scellées par l'auteur** : les empreintes ci-dessous sont celles calculées au versement, à refaire au scellement.

| fichier | adresse demandée | adresse finale | heure UTC (`date -u`) | code | octets | sha256 |
|---|---|---|---|---|---|---|
| `platform-claude-com-docs-en-about-claude-pricing-20261119T095216Z.html` | `https://platform.claude.com/docs/en/about-claude/pricing` | la même | 2026-11-19T09:52:16Z | 200 | 787 545 | `78aff5c8d73a0da27bbb5abe03fa58320612e14bdef5873dc9aaa2ac34fcb03d` |
| `aistudio-google-com-docs-pricing-20261119T095218Z.html` | `https://aistudio.google.com/docs/pricing` | la même | 2026-11-19T09:52:18Z | 200 | 153 791 | `89c58281ba7e9e96084866d0a1b1441f1f5d582269242386c6ca1cf916533963` |
| `ai-google-dev-gemini-api-docs-pricing-redirigee-20261119T095217Z.html` | `https://ai.google.dev/gemini-api/docs/pricing` | `https://aistudio.google.com/docs/pricing` (redirection) | 2026-11-19T09:52:17Z | 200 | 153 773 | `ca4eade07e8290dc81af7a481d4c5bd10169ce9ee494d48254c70ca27fefad8f` |
| `developers-openai-com-api-docs-pricing-refus-403-20261119T095218Z.txt` | `https://developers.openai.com/api/docs/pricing` | la même | 2026-11-19T09:52:18Z | **403** | 70 | `bdc7cafb9dbc7163e670946762eb809ac6ce101e06bc18f8386d74ceae8c2551` |

## Ce que les pages disent (lu par programme, balises retirées)

- **Anthropic** : Claude Fable 5.2, entrée 8 et sortie 40 dollars par million de jetons ; Claude Opus 5.5, 4 et 20 ; Claude Sonnet 5.5, 2 et 10 ; Claude Haiku 5.5, 0,10 et 0,50 pour les entrées de 100 000 jetons au plus (tableau des prix des modèles ; le fichier est du HTML en longues lignes, sans numéro de ligne utile).
- **Google** : section « Gemini 4 Carbon » (`gemini-4-carbon`), onglet « Standard », lignes 115 à 163 du fichier `aistudio-…` : entrée « $2.00 through November 30, 2026. $4.00 starting December 1, 2026. » (lignes 154 à 156) ; sortie, « including thinking tokens », « $10.00 through November 30, 2026. $20.00 starting December 1, 2026. » (lignes 160 à 163). Les deux fichiers de Google diffèrent de 18 octets (à partir du caractère 1 491) : même page, servie deux fois.
- **OpenAI** : **page non lisible** depuis cette session (code 403, corps « Forbidden » et un identifiant de requête du site) ; requête non reprise. Le prix de `gpt-6.2-astra` reste celui de la page versée et scellée le 18 novembre : `docs/sources/tarifs-openai-v2/developers-openai-com-api-docs-pricing-2026-11-18.html` (`35a048294e2f…`), 8 et 40.
