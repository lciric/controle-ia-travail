# LISEZMOI — kit de lancement des runs de nuit R1, R2 et R4 (GO-2026-11-01-13) — v2

Remplace `LISEZMOI-runs-r1-r2-r4-v1.md` (gardé, R12) après la contre-lecture 1
(`docs/notes/runs-r1-r2-r4-v1/contre-lecture-runs-r1-r2-r4-v1.md`, `1f768dd4…`) et le n° 330 de conv-audit. Branche locale
`prep/runs-r1-r2-r4-v1`, sans dépense ni instance. **Rien n'est scellé.** Devis : `devis-runs-r1-r2-r4-v2.md`.

## Ce qui se lance, et sous quelle condition

- **R1 seul** (rejeu, activations) : prêt après scellement. Instance A, `ETAPES=rejeu` (défaut).
- **R2** (juges 3B et 8B sur les actions de P3) : **suspendu à la confirmation de Lazar sur l'exception à N-029** (la
  comparaison boîte noire « ne se lit pas sur les textes de P3 », section 2). Confirmation consignée en une ligne dans
  `registres/decisions.md`, puis instance A avec `ETAPES="rejeu juge3b juge8b"` (ou une instance A′ avec `ETAPES="juge3b
  juge8b"` si R1 est déjà fait, branche neuve `calcul/r2-reel-v1`).
- **R4** (seconde dose) : indépendant. Instance B.

## Pièces (brouillon 2)

| Pièce | Rôle |
|---|---|
| `src/controle_ia/runs_nuit/alignement_v1.py` | identité des actions et son empreinte, alignement sur `scores-p3.npz` |
| `src/controle_ia/runs_nuit/rejeu_activations_v1.py` | R1 : rejeu forcé, empreintes de trajectoire et d'activations de P3, fidélité (20 actions), contrôle négatif (18 sur 20), `moyenne` (diagnostic, N-026) et `maximum` |
| `src/controle_ia/runs_nuit/juge_actions_v1.py` | R2 : juge par action, P(Yes), log-probabilités brutes, deux bras, empreintes du modèle |
| `tests/test_runs_nuit_v1.py` | 9 essais (rejeu fidèle et empreintes de P3, texte altéré → « non conforme » sans versement, contrôle négatif non discriminant → arrêt, gardes d'alignement, moyenne de diagnostic, `_f16` sur valeur non finie, gardes de citation du préenregistrement, juge aligné, juge sans texte privé) |
| `scripts/amorce_instance_r1_r2_v1.sh`, `scripts/r1_r2_instance_v1.sh` | instance A ; `ETAPES` choisit R1 seul ou R1 puis R2 ; un arrêt d'une étape n'empêche pas les suivantes |
| `scripts/amorce_instance_r4_v1.sh`, `scripts/p3_instance_r4_v1.sh`, `scripts/r4_suite_instance_v1.sh` | instance B : lanceur de P3 tel quel (suite ciblée), puis juges 3B et 8B, puis rejeu ; résultats partiels poussés au plafond |
| `prereg/R1-R2-rejeu-p3-v1.md` ; `prereg/R1-rejeu-config-v2.json`, `prereg/R2-juge3b-config-v1.json`, `prereg/R2-juge8b-config-v1.json`, `prereg/R2-invite-juge-v1.md` | R1 + R2 |
| `prereg/R4-dose-cout-gonfle-v1.md` ; `prereg/R4-config-v1.json`, `prereg/R4-consignes-dose-faible-v1.md`, `prereg/R4-rejeu-config-v2.json`, `prereg/R4-juge3b-config-v1.json`, `prereg/R4-juge8b-config-v1.json` | R4 |
| `controle_prealable_tokenisation_v1.py` et sa sortie | 2 236 / 2 400 actions conformes, 1 782 en contexte exact |
| `essai_garde_calcul_v1.py` et `essai-garde-calcul-v1.txt` | garde de calcul éprouvée sur la commande exacte (CLR-09) |

Les configurations v1 du rejeu (`R1-rejeu-config-v1.json`, `R4-rejeu-config-v1.json`) restent, non citées. Les deux
préenregistrements passent `controle_ia.prereg.problemes` sans remarque (contre-lecture inscrite).

## Écarts au format de conv-audit (n° 328 et n° 330), à lui envoyer avant tout départ

1. **Fichiers de R1** : `activations-p3-rejeu-v1.npz` porte `moyenne` (2400, 3, 4096) float16 et l'identité (≈ 59 Mo) ;
   `maximum` (facultatif pour toi) est dans `activations-p3-rejeu-v1-maximum.npz`, aux mêmes clés ; complément
   `activations-p3-rejeu-v1-complement-hors-cout.npz` (`maximum_hors_cout`). Format fixe : un seul fichier de 118 Mo
   dépasserait la limite de poussée de GitHub.
2. **`jetons_empan`** = `jetons_notes` de `scores-p3.npz` pour les 2 400 lignes (n° 330) ; la longueur reconstruite par
   le rejeu est dans `jetons_empan_rejeu` ; elle diffère pour les ≈ 164 actions non conformes en longueur.
3. **Champs ajoutés par action** : `conforme_longueur`, `contexte_conforme`, `trajectoire_identique`,
   `activations_identiques`, `ecart_fidelite`, `fidele`, `couches`. Les actions non fidèles doivent être exclues de tous les
   bras de la même façon ; le préenregistrement R1-R2 demande les exclusions par condition et par tâche, et dit que la
   restriction au contexte exact n'est pas la lecture principale.
4. **Verdict de fidélité** : dans `diag/<run>/rejeu-activations.json` (`verdict_fidelite` : « conforme »), rattaché au
   manifeste par son empreinte ; un arrêt écrit `diag/<run>/arret.json` avec « non conforme » (fidélité ou contrôle
   négatif) ou « echec » (toute autre cause). L'empreinte des textes rejoués (`ba05fa13…`) et les couches [7, 15, 23] y
   sont aussi.
5. **Tolérance de fidélité** : 0,02 × (1 + |score|), non la tolérance d'identité du harnais (1e-6, mêmes activations) ;
   éprouvée par un contrôle négatif (contexte faux, 18 sur 20 hors tolérance exigés) ; égalité au bit près mesurée par les
   empreintes d'activations de P3.
6. **Empan** : règle de `premier_test_ia.run.jouer_p3` (jetons de l'action sans le jeton de fin) ; `premier_test_ia/empans.py`
   ne traite que les données génériques.
7. **Juge** : `score` = P(Yes) renormalisée, dans [0, 1] ; `logprob_oui`, `logprob_non`, `masse`, `anomalie` (score gardé,
   drapeau levé), et les mêmes suffixés `_generique` ; bras principal : spécialisé ; contexte vu : énoncé et action seule, ni
   consigne ni indication privées (test) ; juge 8B en plus (`scores-juge8b-p3-v1.npz`). **R2 attend la confirmation de
   Lazar (N-029).**
8. **R4** : 32 tâches, **pas 43** : le dépôt n'a que 96 tâches, dont 36 hors des 60 de P3 (32 de réserve, 4 d'évaluation :
   `2510.25210v1`, `2508.12726v6`, `2506.11784v2`, `2601.16447v1`). R4 garde les 32 de réserve ; ajouter les 4 ou prendre
   des tâches de P3 est à décider. Format de P3 ; dose lisible dans le manifeste du run (configuration avec le chemin et
   l'empreinte des consignes « about 30% higher ») ; activations au format de R1 ; juges 3B et 8B.

## Avant toute dépense (session)

1. Lire ce kit au commit final ; si un point change, nouvelle contre-lecture ciblée (R2).
2. Inscrire le commit final du code à la place de `COMMIT_A_INSCRIRE_AU_SCELLEMENT` dans les deux préenregistrements et
   « Tests attendus » (suite ciblée de 17 fichiers, même liste dans `r1_r2_instance_v1.sh` et `p3_instance_r4_v1.sh`) :
   valeur mesurée ci-dessous, à revérifier au commit cité (`PYTHONPATH=src:tests python -m pytest -q <liste>`).
3. Sceller (R6) :
   ```
   PYTHONPATH=src python -m controle_ia.scellement sceller prereg/R1-rejeu-config-v2.json prereg/R2-juge3b-config-v1.json \
       prereg/R2-juge8b-config-v1.json prereg/R2-invite-juge-v1.md prereg/R4-config-v1.json \
       prereg/R4-consignes-dose-faible-v1.md prereg/R4-rejeu-config-v2.json prereg/R4-juge3b-config-v1.json \
       prereg/R4-juge8b-config-v1.json
   PYTHONPATH=src python -c "from controle_ia.prereg import sceller_prereg as s; print(s('prereg/R1-R2-rejeu-p3-v1.md')); print(s('prereg/R4-dose-cout-gonfle-v1.md'))"
   ```
   Commit de scellement, poussée vers `lciric/controle-ia-travail` (jamais `lciric/controle-ia`), empreintes et écarts
   ci-dessus envoyés à conv-audit avant tout départ.
4. `vastai show instances` ; dépense inscrite d'avance (devis v2).

## Création des instances

Le binaire est appelé par son chemin littéral, terminé par `vastai create instance`, pour que la garde de calcul voie la
commande et vérifie le GO (CLR-09 ; éprouvé : avec `GO_ID=GO-2026-11-01-13`, code 0 ; sans GO, code 2 ; l'ancienne forme
`"$V" create instance` passait sans contrôle).

```
VB=/tmp/claude-0/-home-user-controle-ia-travail/4ff7d1a3-3d12-504e-b550-a8bc2f8510b1/scratchpad/vast183-venv/bin
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true dph_total<=1.40"
$VB/vastai search offers "$FILTRE" -o 'dph_total' --storage 80

# Instance A : R1 seul (ETAPES=rejeu) (R2 : voir la variante après confirmation de Lazar sur N-029)
B64A=$(git show "$COMMIT_A:scripts/amorce_instance_r1_r2_v1.sh" | base64 -w0)
GO_ID=GO-2026-11-01-13 $VB/vastai create instance "$OFFRE_A" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label r1-v1 \
    --env "-e COMMIT=$COMMIT_A -e BRANCHE=calcul/r1-reel-v1 -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
    --entrypoint bash --args -c "echo $B64A | base64 -d > /root/amorce.sh && ETAPES=rejeu bash /root/amorce.sh"
# R1 puis R2 (après confirmation) : même commande, --label r1-r2-v1, BRANCHE=calcul/r1-r2-reel-v1, et
#   --args -c "echo $B64A | base64 -d > /root/amorce.sh && ETAPES='rejeu juge3b juge8b' bash /root/amorce.sh"

# Instance B : R4
B64B=$(git show "$COMMIT_B:scripts/amorce_instance_r4_v1.sh" | base64 -w0)
GO_ID=GO-2026-11-01-13 $VB/vastai create instance "$OFFRE_B" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label r4-dose-v1 \
    --env "-e COMMIT=$COMMIT_B -e PREREG=prereg/R4-dose-cout-gonfle-v1.md -e BRANCHE=calcul/r4-dose-reel-v1 -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
    --entrypoint bash --args -c "echo $B64B | base64 -d > /root/amorce.sh && bash /root/amorce.sh"
```

`ETAPES` passe par la ligne de commande de l'amorce (l'amorce transmet l'environnement au script d'instance). Consigner
chaque identifiant d'instance au registre des dépenses et dans la passation.

## Surveillance (toutes les 10 minutes) et arrêt

```
$VB/vastai show instances --raw | python3 -c 'import json,sys; [print(i["id"], i.get("label"), i.get("actual_status"), i.get("dph_total")) for i in json.load(sys.stdin)]'
$VB/vastai logs <ID> --tail 40
git ls-remote https://github.com/lciric/controle-ia-travail.git 'refs/heads/calcul/*'
```

Jalons A : branche poussée (≈ 3 min) ; « tests : N passed » ; `etape=reconstruction … trajectoires_identiques=…` ;
**`etape=fidelite lecture=conforme`** ; **`etape=controle_negatif lecture=discriminant`** ; `etape=fin fideles=…` ; juges
si autorisés ; « fin ». Jalons B : jalons de P3 (`etape=sondes-figees`, `etape=episodes lot=k/16`), « run terminé »,
puis « suite de R4 : juge poussé », « juge8b poussé », « rejeu poussé », « fin ». **Arrêt (R10)** : à la ligne « fin »,
sur arrêt consigné, au plafond du devis, ou sans ligne nouvelle pendant 20 minutes : `$VB/vastai destroy instance <ID>`,
puis `registres/arrets.md` et `registres/depenses.md`.

## Après les runs

Vérifier les sceaux des sorties ; verser les empreintes à conv-audit ; aucune lecture d'étiquette avant que son analyse
soit scellée et qu'un lecteur neuf ait vérifié la concordance des deux textes. R4 : aucune lecture des colonnes de sondes
ni des activations avant le scellement du verdict de la règle.

## Essais (brouillon 2)

Voir la section ajoutée en fin de fichier après les essais.
