# Devis du tour du collisionneur sur les bassins d'idées étroits et profonds, consultations à part comprises — v1

Écrit le 13 novembre 2026 à 12:46 UTC (heure relevée par `date -u`), **avant tout appel**, par l'opérateur neuf (Claude Opus
5.5) de la session mère, sous **GO-2026-11-12-04** (collisionneur, quatre tours au plus, 15 USD par tour ; ligne de
`registres/go.md`). Tour 2 sur 4 (tour 1 : 9,54 USD). **Plafond de ce tour : 15 USD, les trois consultations à part
comprises** ; aucune autre dépense. Consigne : `consigne-collisionneur-bassins-etroits-v2.md` (`2a3b09b1…`).

## 1. Pièces

- Faits : `faits-v1.md` (`d19b540015ed9480774c020cd7f1a527db32d42600a5bc2bd34c92c17d7be0b3`, 8 316 octets).
- Question : `question-v1.md` (`935f4e5b15abd2d83a0fc063aa5255023d94fbc2ff783c750769802348ddbd52`, 3 503 octets).
- Script du collisionneur, inchangé, employé depuis son chemin :
  `docs/notes/collisionneur-experimentateur-v1/script-v1/collisionneur_v8_plafonds_bas_v1.py`
  (`4ad78ccce8228aed2679c854eaec7ee4d2ab8f867098218387024adfeb1e7756`, empreinte vérifiée). Espèces et plafonds de sortie
  (premier essai / relance) : A `claude-fable-5-1` 22 000 / 64 000 ; B `claude-opus-4-6` 10 000 / 64 000 ; C `gemini-4-argon`
  18 000 / 32 000 ; D `kimi-k3.1-pro` 32 000 / 65 536 ; E `gpt-6-astra` 8 000 / 32 000. Aucun changement de modèle.
- Programme des consultations à part : `consultation_a_part_v1.py`
  (`59c2fd36535aaf8fd57dc1d7b8c554779d6d2d0f6ab5169c8098b58a61a356be`), essais hors réseau
  `essais_consultation_a_part_v1.py` (`3a49df53…`) : **19 sur 19** (cas sain ; refus, vide, échec de transport, troncature,
  marqueur absent, modèle différent ; plafond ; non-écrasement ; script altéré). Versés au dépôt à la fin du tour.

## 2. Pire cas

**Consultations à part** (programme, mode `--devis`, sortie brute `devis-consultations-sortie-v1.txt`) : prompt unique de
13 090 caractères (`dd3db386…`), un appel par modèle, un seul essai, au barème du script :

| consultation | modèle | plafond de sortie | prix (entrée / sortie, USD par million) | pire cas USD |
|---|---|---|---|---|
| Argon | `gemini-4-argon` | 24 000 | 10 / 50 | 1,2436 |
| Astra | `gpt-6-astra` | 16 000 | 10 / 50 | 0,8436 |
| Kimi | `kimi-k3.1-pro` (relais) | 32 000 | 2 / 10 | 0,3287 |
| **total** | | | | **2,4160** |

**Collisionneur, étage III** (programme `devis` du script, sortie brute `devis-sortie-v1.txt`) : **15 cellules, 14,47 USD au
pire cas, sans relance**. Par espèce sur les trois tours : A 4,17 ; B 3,55 ; C 3,57 ; D 1,13 ; E 2,07.

**Somme des pires cas : 16,89 USD > 15.** Conséquence, acceptée par la consigne (point 4) : le script du collisionneur peut
s'arrêter à une porte de plafond (code 4, sans appel) avant la fin de l'étage ; aucun plafond de sortie n'est changé. Repère
(RAPPORTÉ, `docs/notes/collisionneur-diversite-idees-v1/depense-et-incidents-v1.md`) : au tour 1, dépense réelle 9,54 USD
pour un pire cas de 14,51.

## 3. Garantie de plafond

1. Les consultations passent **d'abord**, avec `--plafond-usd 15` (le programme s'arrête, code 2, sans appel, si leur pire
   cas dépasse ce plafond ; contrôle refait avant chaque appel).
2. Le collisionneur reçoit ensuite `--plafond-usd` = **15,00 moins la dépense réelle des trois consultations au barème du
   script, arrondie au centime supérieur**, et jamais plus de 15 ; le script vérifie, avant chaque appel, dépense consignée du
   run + pire cas de l'appel ≤ plafond.
3. Relais Kimi (sert aux deux : 1 appel de consultation + 3 cellules du collisionneur) : `relais_kimi_v4.py`
   (`67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e`), port 8789, modèle permis `kimi-k3.1-pro`,
   **plafond 3 USD, au plus 8 appels**, prix 2 / 10 / 2, délai 1 800 s, silence 600 s ; arrêt par son numéro de processus.
   Sa dépense est comptée dans celle des consultations et du run (barème du script), pas en plus.

Total au pire, par construction : ≤ 15 USD au barème du script (dépense des consultations + plafond restant du run).

## 4. Mécanique

- Clés par leur nom, sous `env -i`, jamais affichées : `ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_RIGAUD"`, **sans**
  `ANTHROPIC_BASE_URL` ; `GEMINI_API_KEY="$GEMINI_API_KEY"` (jamais `GEMINI_API_KEY_2`) ; `OPENAI_API_KEY="$OPENAI_API_KEY"` ;
  `KIMI_API_KEY` au seul relais. Mandataire et certificats : `HTTPS_PROXY`, `SSL_CERT_FILE`.
- Interpréteur : l'environnement Python du bac à sable du tour 1 (Python 3.13.18, `anthropic` 2.3.0), employé en lecture ;
  relais par `python3 -I -B`.
- Run et consultations écrits dans le bac à sable de l'opérateur pendant tout le tour ; copiés au dépôt à la fin seulement,
  journaux et consoles masqués s'ils portent un identifiant d'organisation ou de clé d'un fournisseur.
- Refus, absence, troncature : consignés tels quels ; ni reformulation, ni relance (sauf l'absence acceptée d'une cellule
  refusée, suite du même run, prévue par la consigne).
