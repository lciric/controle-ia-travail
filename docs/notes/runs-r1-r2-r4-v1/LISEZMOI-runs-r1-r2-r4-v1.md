# LISEZMOI — kit de lancement des runs de nuit R1, R2 et R4 (GO-2026-11-01-13) — v1

Préparé sur la branche locale `prep/runs-r1-r2-r4-v1`, sans dépense ni instance. **Rien n'est scellé** : scellement,
contre-lectures, création d'instance et dépense restent à la session « session-depot », sous le GO-2026-11-01-13
(plafond 25 USD, `registres/go.md`). Devis : `docs/notes/runs-r1-r2-r4-v1/devis-runs-r1-r2-r4-v1.md`.

## Pièces

| Pièce | Rôle |
|---|---|
| `src/controle_ia/runs_nuit/alignement_v1.py` | identité des actions (`episode`, `pas`, `condition`, `tache`) et son empreinte, alignement sur `scores-p3.npz` |
| `src/controle_ia/runs_nuit/rejeu_activations_v1.py` | R1 : rejeu forcé, contexte exact, couches 7, 15, 23, `moyenne` (diagnostic, N-026) et `maximum` en float16, contrôle de fidélité |
| `src/controle_ia/runs_nuit/juge_actions_v1.py` | R2 : juge par action, P(Yes) et log-probabilités brutes, bras spécialisé (principal) et générique |
| `tests/test_runs_nuit_v1.py` | 5 essais jouet (rejeu fidèle au bit, texte altéré → arrêt sans versement, gardes d'alignement, moyenne de diagnostic, juge aligné) |
| `scripts/amorce_instance_r1_r2_v1.sh`, `scripts/r1_r2_instance_v1.sh` | instance A (R1 puis R2 3B puis R2 8B) |
| `scripts/amorce_instance_r4_v1.sh`, `scripts/p3_instance_r4_v1.sh`, `scripts/r4_suite_instance_v1.sh` | instance B (lanceur de P3 tel quel, script d'instance de P3 décliné avec la suite ciblée, préenregistrement de R4 ; puis rejeu et juge) |
| `prereg/R1-R2-rejeu-p3-v1.md` ; `prereg/R1-rejeu-config-v1.json`, `prereg/R2-juge3b-config-v1.json`, `prereg/R2-juge8b-config-v1.json`, `prereg/R2-invite-juge-v1.md` | préenregistrement et pièces de R1 + R2 |
| `prereg/R4-dose-cout-gonfle-v1.md` ; `prereg/R4-config-v1.json`, `prereg/R4-consignes-dose-faible-v1.md`, `prereg/R4-rejeu-config-v1.json`, `prereg/R4-juge3b-config-v1.json` | préenregistrement et pièces de R4 |

Les deux préenregistrements passent `controle_ia.prereg.problemes` à une remarque près, attendue : « contre-lecture 1
sans ses deux empreintes » (la contre-lecture R2 n'est pas faite).

## Réponse au point (a) et contrôle préalable

Le rejeu forcé dans le contexte exact est possible sans relancer l'environnement : l'environnement (a) se rejoue depuis
les textes, les consignes viennent du fichier scellé de P3 ; seuls les identifiants générés manquent. Mesuré hors carte
avec le tokeniseur de P3 (`controle_prealable_tokenisation_v1.py`, sortie `controle-prealable-tokenisation-v1.txt`) :
2 236 actions sur 2 400 retrouvent exactement leurs jetons (93 %), 1 782 en contexte exact (74 %). Les autres sont
signalées par action (`conforme_longueur`, `contexte_conforme`, `ecart_fidelite`, `fidele`) ; l'échantillon du contrôle
de fidélité est tiré parmi les actions en contexte exact (≥ 378 par condition).

## Avant toute dépense (session)

1. Contre-lecture R2 de chaque préenregistrement par un sous-agent neuf (fichiers à lui donner : le préenregistrement, ses
   pièces, les modules `runs_nuit`, les scripts, `prereg/P3-premier-test-i-a-v1.md`, le message n° 328) ; traiter ; inscrire
   la section « Contre-lecture » (empreinte du brouillon relu, rapport et son empreinte).
2. Commit final du code (`src/`, `tests/`, `scripts/` gelés) : inscrire son empreinte complète à la place de
   `COMMIT_A_INSCRIRE_AU_SCELLEMENT` dans les deux préenregistrements (`prereg/` est hors de l'arbre gelé) ; inscrire
   « Tests attendus » : le nombre de la suite ciblée (même liste dans `r1_r2_instance_v1.sh` et `p3_instance_r4_v1.sh`),
   relu au commit cité (`PYTHONPATH=src:tests python -m pytest -q <liste>`) ; inscrit provisoirement : 123 (mesuré le
   1er novembre vers 21:29 UTC, 123 passés en 462 s), à revérifier si la contre-lecture change le code ou les tests.
3. Sceller (R6) :
   ```
   PYTHONPATH=src python -m controle_ia.scellement sceller prereg/R1-rejeu-config-v1.json prereg/R2-juge3b-config-v1.json \
       prereg/R2-juge8b-config-v1.json prereg/R2-invite-juge-v1.md prereg/R4-config-v1.json \
       prereg/R4-consignes-dose-faible-v1.md prereg/R4-rejeu-config-v1.json prereg/R4-juge3b-config-v1.json
   PYTHONPATH=src python -c "from controle_ia.prereg import sceller_prereg as s; print(s('prereg/R1-R2-rejeu-p3-v1.md')); print(s('prereg/R4-dose-cout-gonfle-v1.md'))"
   ```
   Les empreintes citées dans les configurations et les préenregistrements (consignes de R4 `3c229074…`, invite
   `44d48a28…`, configurations) doivent rester égales : toute retouche d'un fichier cité change son empreinte et doit
   être reportée partout. Commit de scellement (`COMMIT_A`, `COMMIT_B` : un seul commit peut servir aux deux), poussée
   vers `lciric/controle-ia-travail` (jamais `lciric/controle-ia`), **empreintes des deux préenregistrements publiées à
   conv-audit avant tout départ** ; conv-audit scelle son analyse avant toute lecture.
4. Contrôles : `vastai show instances` (aucune instance du programme oubliée) ; crédit (le compte se recharge seul,
   R-283) ; dépense inscrite d'avance dans `registres/depenses.md` (attendu et pire cas du devis).

## Création des instances (session, après GO valide et sceaux)

Variables : `V` = binaire vastai de la session (par exemple
`/tmp/claude-0/-home-user-controle-ia-travail/4ff7d1a3-3d12-504e-b550-a8bc2f8510b1/scratchpad/vast183-venv/bin/vastai`),
`HF_TOKEN` (licences Llama 3.1 **et 3.2** acceptées), `CONTROLE_IA_GITHUB_TOKEN` (jeton à grain fin du dépôt de travail).

```
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true"
"$V" search offers "$FILTRE" -o 'dph_total' --storage 80
# deux offres distinctes : OFFRE_A, OFFRE_B ; prix lu ≤ 1,40 USD/h

# Instance A : R1 puis R2
B64A=$(git show "$COMMIT_A:scripts/amorce_instance_r1_r2_v1.sh" | base64 -w0)
GO_ID=GO-2026-11-01-13 "$V" create instance "$OFFRE_A" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label r1-r2-v1 \
    --env "-e COMMIT=$COMMIT_A -e BRANCHE=calcul/r1-r2-reel-v1 -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
    --entrypoint bash --args -c "echo $B64A | base64 -d > /root/amorce.sh && bash /root/amorce.sh"

# Instance B : R4
B64B=$(git show "$COMMIT_B:scripts/amorce_instance_r4_v1.sh" | base64 -w0)
GO_ID=GO-2026-11-01-13 "$V" create instance "$OFFRE_B" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label r4-dose-v1 \
    --env "-e COMMIT=$COMMIT_B -e PREREG=prereg/R4-dose-cout-gonfle-v1.md -e BRANCHE=calcul/r4-dose-reel-v1 -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
    --entrypoint bash --args -c "echo $B64B | base64 -d > /root/amorce.sh && bash /root/amorce.sh"
```

Consigner chaque identifiant d'instance (`new_contract`) au registre des dépenses et dans la passation.

## Surveillance (toutes les 10 minutes)

```
"$V" show instances --raw | python3 -c 'import json,sys; [print(i["id"], i.get("label"), i.get("actual_status"), i.get("dph_total")) for i in json.load(sys.stdin)]'
"$V" logs <ID_A> --tail 40      # journal : lignes horodatées et lignes « PROGRES … clé=valeur », aucun texte d'action
"$V" logs <ID_B> --tail 40
git ls-remote https://github.com/lciric/controle-ia-travail.git 'refs/heads/calcul/r1-r2-reel-v1' 'refs/heads/calcul/r4-dose-reel-v1'
```

Jalons attendus. A : « branche … poussée avant l'installation » (≈ 3 min), « tests : N passed » (≈ 30 min),
`etape=reconstruction conformes=… contextes_conformes=…`, **`etape=fidelite lecture=conforme`** (sinon : arrêt consigné,
rien n'est versé ; repli = relance de l'environnement, devis neuf), `etape=fin fideles=…`, juges 3B puis 8B, « fin ».
B : jalons de P3 (`etape=sondes-figees`, `etape=episodes lot=k/16`), « fin », puis « suite de R4 : rejeu poussé », « juge
poussé », « fin ».

**Arrêt (R10)** : dès la ligne « fin » (ou « AMORCE … fin, code … »), ou sur arrêt consigné, ou au plafond du devis :
`"$V" destroy instance <ID>` (par identifiant, jamais par motif), puis `registres/arrets.md` et `registres/depenses.md`
(coût lu par `"$V" show invoices` ou sur le compte). Une instance qui ne progresse plus pendant 20 minutes (aucune ligne
nouvelle) s'arrête de même.

## Après les runs (sans lecture d'étiquette)

Vérifier les sceaux des sorties sur les branches (`python -m controle_ia.scellement verifier …`), verser les empreintes à
conv-audit ; aucune lecture des étiquettes avant que son analyse soit scellée (n° 328). Pour R4 : aucune lecture des
colonnes de sondes ni des activations (P-015 (b)).

## Essai jouet (fait le 1er novembre vers 21:20 UTC, hors réseau, sur processeur)

Dépôt distant local ; un run de P3 jouet (3 tâches × 4 conditions, 36 actions) comme source ; puis
`amorce_instance_r1_r2_v1.sh` en mode jouet (`PREREG_ABSENT=1`, étapes rejeu et juge 3B, suite ciblée réduite au fichier
des runs de nuit) : branche poussée avant installation, tests, `etape=reconstruction conformes=28 contextes_conformes=24
actions=36`, `etape=fidelite lecture=conforme ecart_max=0.000e+00`, `fideles=28 notees=36`, juge (deux bras, 0 anomalie),
fin, poussée des sorties (`activations-p3-rejeu-v1.npz`, complément, `scores-juge3b-p3-v1.npz`) ; puis
`r4_suite_instance_v1.sh` sur ce clone (rejeu et juge du run source, poussés). Le modèle jouet échantillonne parfois un
jeton spécial que le texte stocké efface : ces actions sont « non conformes en longueur », la suite de leur épisode
« hors contexte exact », signalées par action ; le même mécanisme vaut pour une tokenisation non canonique du 8B. Une
première répétition, dont le dépôt local manquait des invites transcrites, s'est arrêtée aux tests et a consigné l'arrêt
(cas d'artefact de la garde). Non répété en jouet : le passage de R4 par `p3_instance.sh` (script inchangé de P3, déjà
éprouvé par P3 et ses tests).
