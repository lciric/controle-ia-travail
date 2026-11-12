# Devis du tour du collisionneur sur la diversité des idées de l'organisme — v1

Écrit le 12 novembre 2026 à 20:16 UTC (heure relevée par `date -u`), **avant tout appel**, par l'opérateur neuf (Claude Opus
5.5) de la session mère, sous **GO-2026-11-12-04** (collisionneur, quatre tours au plus, **15 USD par tour**, devis consigné
avant chaque tour ; parts Argon et Astra, hors crédits de Claude, comptées sous le même plafond de tour : mot du directeur,
registre R-2443). Premier tour sous cette ligne (aucune dépense antérieure inscrite sous elle dans `registres/depenses.md`).
Programme `devis` du script, aucun appel.

## 1. Script : celui du tour précédent, inchangé

`docs/notes/collisionneur-experimentateur-v1/script-v1/collisionneur_v8_plafonds_bas_v1.py`
(`4ad78ccce8228aed2679c854eaec7ee4d2ab8f867098218387024adfeb1e7756`, empreinte vérifiée), employé tel quel depuis son chemin
(aucune copie, aucune modification). Espèces et plafonds de sortie (premier essai / relance) : A `claude-fable-5-1`
22 000 / 64 000 ; B `claude-opus-4-6` 10 000 / 64 000 ; C `gemini-4-argon` 18 000 / 32 000 ; D `kimi-k3.1-pro`
32 000 / 65 536 ; E `gpt-6-astra` 8 000 / 32 000.

Choix des espèces de Claude : la consigne permet « Fable 5.1 ou 5.2 et Opus » ; la méthode demande de refaire exactement le
tour précédent : Fable 5.1 et Opus 4.6 sont gardés, sans toucher au script (R12).

## 2. Devis

Sur `faits-v1.md` (`01f9e759f9e755db3e35feed2d00fa4c7f8d5ad5ab9c1aacedaa6c100f96d283`, 10 819 octets) et `question-v1.md`
(`8a8809f31873f7519410fb55544dc62596d1a4f240851ab7d43b8a39a7a3c480`, 2 087 octets) : **étage III, 15 cellules,
14,51 USD au pire cas, sans relance** (≤ 15 ; sortie complète : `devis-sortie-v8-plafonds-bas-v1.txt`).

Pire cas par espèce sur les trois tours (somme des lignes du devis) : A Fable 5.1 **4,17** ; B Opus 4.6 **3,55** ; C Argon
**3,57** ; D Kimi **1,13** ; E Astra **2,07**. Sur les crédits de la clé `RR_ANTHROPIC_API_KEY_RIGAUD` : 7,72 au pire ; hors
crédits (Argon, Astra, Kimi) : 6,77 au pire.

Attendu (estimé, d'après le tour du 11 novembre : 12 cellules pour 8,51 USD, sur des faits plus longs) : environ 7 à 11 USD
consignés si Kimi répond.

## 3. Bornes du tour

- **Plafond du run** : `--plafond-usd 15` ; le script vérifie, avant chaque appel, dépense consignée + pire cas de l'appel ;
  au-delà, arrêt (code 4) sans appel. Une relance (sortie vide ou coupée) n'a lieu que si elle tient sous ce plafond.
- **Barème du script** (borne haute) : Fable 5.1 10/50 USD par million de jetons (égal au tarif public lu dans la référence
  de l'interface mise en cache le 3 novembre 2026) ; Opus 4.6 15/75 (tarif public 5/25 : compte environ trois fois trop
  haut) ; Argon 10/50 et Astra 10/50 (supposés hauts, non lus) ; Kimi 2/10.
- **Relais Kimi** (`docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py`,
  `67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e`) : port 8789, modèle permis `kimi-k3.1-pro`,
  **plafond 3 USD**, au plus 8 appels, prix 2 / 10 / 2, délai 1 800 s, silence 600 s ; clé `KIMI_API_KEY` (changée et
  rechargée par le directeur, R-2398) passée au seul relais. Arrêt par son numéro de processus (R10).
- Si Kimi ne répond pas (compte, surcharge) : ses cellules sont acceptées absentes (`--accepter-absence`), suite du même
  run ; l'absence est dite.

## 4. Mécanique (celle du 11 novembre)

- Clés par leur nom, sous `env -i`, jamais affichées : `ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_RIGAUD"`, **sans**
  `ANTHROPIC_BASE_URL` (présente dans l'environnement de l'opérateur, non transmise) ; `GEMINI_API_KEY="$GEMINI_API_KEY"` ;
  `OPENAI_API_KEY="$OPENAI_API_KEY"` ; Kimi par son relais. Mandataire et certificats : `HTTPS_PROXY`, `SSL_CERT_FILE`.
- Interpréteur du collisionneur : l'environnement Python du bac à sable du tour précédent (Python 3.13.18, `anthropic`
  2.3.0), employé en lecture ; relais par `python3 -I -B`.
- **Dossier du run dans le bac à sable de l'opérateur**, hors du dépôt, pendant tout le tour (règle R-2389 : aucun morceau
  intermédiaire d'un journal de fournisseur n'entre dans le dépôt) ; à la fin seulement : `verifier`, puis copie des cellules,
  des essais et des pièces dans `run-e3-v1/`, journal et consoles **masqués** (identifiants de compte des fournisseurs),
  garde des secrets à 0 avant le commit.
- Refus : consigné tel quel, jamais reformulé.
