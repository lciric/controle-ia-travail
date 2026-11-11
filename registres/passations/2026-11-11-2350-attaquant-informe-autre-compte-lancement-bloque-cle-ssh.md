# Session « attaquant informé » sur l'autre compte — témoin de Bailey prêt, lancement bloqué sur l'accès `ssh` au compte Vast — 11 novembre 2026, 23:50 UTC

Session neuve `session_01XJ6MgnEhQMZteN9F8a1BST` (autre compte), brief de passation v2. Branche
`claude/compassionate-meitner-d4ryyk`, tête lue `35680167`. Ne se réécrit pas (R12). Fait suite à
`2026-11-11-2320-attaquant-informe-autre-compte-lancement-bloque-acces.md` (session `session_01XJ6Mgqg6DeUDvNm87LXApc`),
dont les deux blocages (réseau, clés) **ne se reproduisent pas ici**.

## Verdict
Témoin **non lancé**. Tout est prêt sauf un point : la conduite pilote l'instance par `ssh`, et le compte Vast ne porte
qu'une clé publique (`lazar-vast`, identifiant 900705), dont ce conteneur n'a pas la clé privée. L'ajout d'une clé de
session au compte (`vastai create ssh-key`) a été **refusé par le classifieur de permissions** (« ajout d'un accès »).
Consigné ; l'écriture est arrêtée sur ce point, sans contournement (ni attache par instance, ni autre voie). Aucune
instance créée, aucune dépense.

## Constaté (sans lecture de note ni de résultat)
- `VAST_API_KEY`, `HF_TOKEN` : présentes (noms seuls vérifiés). `console.vast.ai` et `huggingface.co` joignables.
- Routine R14 : `docs/sha256sums-lancement-v2.txt` conforme ; `verifier-arbre` : les deux mêmes écarts antérieurs que la
  note de 23:20, hors du code du run ; `registres/etat.md` non lu (cloison du brief v2).
- `.venv` Python 3.11 : `requirements-cpu.txt`, `hydra-core`, `pandas`, `vastai` 1.11.0. Essais
  `test_temoin_bailey_condition6_v13.py` (`7505596e…`) et `test_temoin_bailey_analyse_v3.py` (`8cca01f1…`) :
  **175 passés**. `lanceur_v13.py` `9257266f…`, `instance_v12.py` `de466986…` : conformes à l'addendum 2.
- GO relus sur `origin/main` au commit `4c0a3791b638c29f6897e91857542d0aec6cfaac` (2026-11-11T23:33:00Z,
  `git fetch --depth=5 origin +refs/heads/main:refs/remotes/origin/main`) : `GO-2026-11-10-10` l. 300, `-11-01` l. 305,
  `-11-02` l. 306 ; échéance 2026-11-30 ; aucune révocation.
- Aucune instance Bailey antérieure dans `registres/depenses.md` (branche et `main`) : `instances_anterieures=[]`.
- Inventaire `vastai show instances` (R14) : 58936096, 58936099, 58936100 arrêtées, non touchées ; **60218139**, étiquette
  `t06-v2`, A100 SXM4, **en marche depuis 2026-11-11T14:19:57Z**, carte occupée (≈ 86 %), image `python:3.11-bookworm` :
  hors de ce poste (T0.6, autre session), **non touchée, aucun résultat lu** ; à signaler à la mère, qui en a la charge.
  Lecture 35 : le champ `label` est présent dans `show instances --raw`.
- Client `ssh` absent du conteneur : `openssh-client` installé (`apt`).
- Addendum 2 du témoin déposé chez le tiers le **2026-11-11T23:13:50Z** (note `…-2315-…`) : avant tout lancement ;
  l'ordre de lancement le dira.

## Choix de l'image (routine ; à inscrire au registre des décisions sur `main` par la mère)
Exigences de `lanceur_v13.script_amorce` : `git` (premier geste : `git init` du dépôt public), commande `python3.11` dans
le `PATH` d'une commande `ssh` non interactive, `venv`, pilote de carte.
- Rejetée : `pytorch/pytorch:2.4.1-cuda12.1-cudnn9-devel`. Son étape finale (`Dockerfile` v2.4.1, l. 81-109) n'installe
  que `ca-certificates`, `libjpeg-dev`, `libpng-dev` : pas de `git` ; Python 3.11 seulement dans `/opt/conda/bin`.
- Rejetée : `vastai/base-image:cuda-12.1.1-cudnn8-devel-ubuntu22.04-py311-2026-10-23`. `git` présent, mais Python 3.11
  seulement dans `/venv/main` (Conda) et dans les dossiers de `uv`. `/etc/environment`, lu par `pam_env` pour le `ssh`
  non interactif, reçoit le `PATH` de l'image, sans `/venv/main/bin` (`ROOT/etc/vast_boot.d/10-prep-env.sh`, dépôt
  `vast-ai/base-image` au commit `8f516b9`).
- **Retenue : `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04`** (configuration
  `sha256:ff5fe688608be260bd6c0cde161cf7bd394f41526610a9addf406a535cdc150a`). `apt` y installe `git`, `openssh-server`,
  `python3.11-dev` et `python3.11-venv` (dépôt `deadsnakes`) dans `/usr/bin`. L'image exige un pilote compatible
  CUDA 12.4 (`NVIDIA_REQUIRE_CUDA=cuda>=12.4`) : les offres sont filtrées sur `cuda_vers>=12.4`. Le `torch` du manifeste
  (2.4.1, PyPI) apporte ses propres bibliothèques CUDA. Non éprouvée sur une vraie instance, comme l'amorce elle-même.

## Offre relevée (lecture seule, `vastai search offers`, 23:46 UTC)
Filtre : A100 SXM4, une carte, au moins 79 Go de mémoire de carte, au moins 140 Go de mémoire vive allouée (la garde
prend le minimum de `MemTotal` et de `memory.max`), au moins 220 Go de disque, fiabilité au-dessus de 0,98, CUDA 12.4 ou
plus, deux ports directs, offres vérifiées. Trois offres ; la moins chère : **49739788**, 1,149 USD de l'heure hors
stockage (0,33 USD par Go et par mois), Japon, 256 Go de mémoire, fiabilité 0,994, pilote 595.91.07 (CUDA 13.2), débit
descendant 4,2 Gbit/s, durée maximale 351 heures. **À relire au lancement** (le taux réel c est relevé par la conduite
après la création).

## Pièces prêtes
- Manifeste : `runs/temoin-bailey-v1-20261111/manifeste-local-v3.json`
  (`69143b990725fa827f49b69e7209d6c30ffc87c04ba50c370a25e47ad3693cd2`, scellé ; écrit par
  `lanceur_v13.manifeste_depuis_versions_figees`, `commit_code` `4988f3f442c670887a0e8ad15ddfbac68a173d03`, B = 75,
  `GO-2026-11-10-10` ; graines 1394228342 et 1865327867, égales au texte).
- Script de conduite : `runs/temoin-bailey-v1-20261111/lancer-conduite-v1.py`
  (`a970abc08834249f698bff9e208cd0646a9e240eb84bf719ee95c5270067297a`) ; refuse de tourner sans `GO_ID` et `DEPOT_URL`
  (éprouvé : code 2, rien créé). Sortie de la conduite : `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v1`
  (chemin absolu, le même pour `reprendre`, A-1).
- Clé `ssh` de session, **locale seulement** : `~/.ssh/id_ed25519`, empreinte
  `SHA256:ewBln+4RHDnCKVZSPnkke4U1FVBDauXtbfifZi6z8TA`. Clé publique (non secrète) :
  `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIC7N8XJbDqr0KLudgIi2usKCVWfStfqMFPyYAiZSPkfT session-temoin-bailey-20261111`.
  Elle vit dans ce conteneur : s'il est repris par la plateforme, elle est perdue ; il en faudra une nouvelle.

## Ce qu'il faut à Lazar (nœud : accès au compte)
Une des deux voies :
1. Coller toi-même la clé publique ci-dessus dans la console Vast (compte, rubrique des clés `ssh`) ;
2. ou me dire en clair de l'ajouter moi-même par `vastai create ssh-key` (le classifieur peut redemander une
   autorisation dans l'application).
La clé est à retirer du compte après la destruction de l'instance, en fin de run.

## Prochaine action
Une fois la clé sur le compte : `vastai show ssh-keys` ; relire l'offre ; consigner l'ordre de lancement (GO, B, taux
relevé, offre, image, `DEPOT_URL`, commit du code, addendum 2 daté chez le tiers à 23:13:50Z) ; lancer
`lancer-conduite-v1.py` détaché sous `GO_ID=GO-2026-11-10-10`, PID consigné ; se reprogrammer au plus toutes les
90 minutes.

## Relais
Pour la session-dépôt (`session_013QMaymMAdDjNfPoz8ySwTc`, autre compte, injoignable d'ici : `list_sessions` ne la
montre pas) : chemin et empreinte de cette note (compagnon `.sha256`) et du manifeste ci-dessus, par Lazar.

## Instances actives
Aucune créée par cette session.
