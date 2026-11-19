# Inventaire des sorties des courses de la lecture par lentille neuronale, versées sur la branche de la session — v1

- Heure (UTC) : 2026-11-19T08:07:36Z. Session `session_013QMaykLXtozHttcSQ4ke1s`, branche `claude/brave-galileo-jhp684`.
- Origine : règle de Lazar « il faut TOUJOURS recuperer ce qui est recuperable » (mot direct vers 08:04Z, relayé par la mère, R-3661).
- Méthode : chaque course a poussé ses sorties sur sa branche de calcul ; copie ici des dossiers `diag/<run>` et `runs/<run>` depuis cette
  branche (source), et de son état final dans `docs/notes/neuron-lens-v1/etats-finaux-courses/` ; empreintes des compagnons recalculées ;
  compagnons posés au versement sur les journaux d'étape qui n'en avaient pas (intégrité attestée depuis ce versement seulement).
- Aucun contenu de mesure n'a été lu pour cet inventaire (noms, tailles, empreintes, états seulement).

| course | machine (loueur) | branche de calcul (tête) | état final | exclus | fichiers versés | compagnons d'origine conformes | journaux scellés au versement | taille |
|---|---|---|---|---|---|---|---|---|
| volet A | 60671759 | `calcul/neuron-lens-volet-a-v1` (`3edbc315`) | course terminee | 0 | 7 | 7 sur 7 | 0 | 9.2M |
| B-α, premier lancement | 60770175 | `calcul/neuron-lens-b-alpha-v1` (`0db7f30a`) | arret code 20 (course en echec (code 20)) | 0 | 10 | 8 sur 8 | 2 | 3.6M |
| B-α, relance | 60773264 | `calcul/neuron-lens-b-alpha-v2` (`850a9638`) | arret code 20 (course en echec (code 20)) | 0 | 23 | 16 sur 16 | 7 | 13M |
| B-α, commande v5 | 60783204 | `calcul/neuron-lens-b-alpha-v3` (`cb4bf642`) | course terminee | 0 | 30 | 22 sur 22 | 8 | 16M |
| B-α, recourse contre ablation (A100) | 61001440 | `calcul/neuron-lens-b-alpha-v6` (`ea814779`) | course terminee | 0 | 40 | 30 sur 30 | 10 | 20M |
| essai d'invariance au lot (A100) | 61053329 | `calcul/neuron-lens-audit-invariance-v1` (`efccbcff`) | course terminee | 0 | 11 | 10 sur 10 | 1 | 3.6M |
| tranche de l'ajustement de nos lentilles (H100) | 61287124 | `calcul/neuron-lens-b-beta-v1` (`eb1cd36f`) | course terminee | 0 | 51 | 33 sur 33 | 18 | 6.4M |

**Rien n'a été exclu** d'une poussée par aucune course (`exclus=0` partout). Une seule machine de lentilles n'a laissé aucune sortie : 60669495
(volet A, créée malgré un refus du loueur, jamais démarrée, arrêtée le 2026-11-14 ; `registres/arrets.md`) — rien à récupérer.

**Irrécupérable, déclaré** : les fichiers lourds restés sur les machines louées et détruits avec elles, par construction des commandes
(fichiers de plus de 95 Mo exclus des poussées ; lieu L1 pour la tranche de l'ajustement) : fichiers d'ajustement et exports de nos
lentilles R et S (empreintes et tailles versées dans `b-beta-ajustement-R.json`, `b-beta-ajustement-S.json`, `b-beta-export.json`),
activations et fichiers `-causal.pt` de chaque course (empreintes versées). Leur réajustement fait l'objet du devis
`devis-reajustement/devis-reajustement-lentilles-b-beta-v1.md`.
