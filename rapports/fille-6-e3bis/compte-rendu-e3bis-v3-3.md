# Compte rendu d'E3 bis (T0.6, chaîne v11) — fille 6 — FINAL, 2026-11-08T07:40Z ; remplace le jalon 2 (07:00Z)

Ordre `docs/procedures/ordre-fille-6-t06-e3bis-v3.md` (1e2e3259…, R-1755 ; couples 456957e4…), commit d'épreuve c01d29ea (prep/t06-v11), configuration `config-t06-epreuve-e3bis-v3.json`. GO-2026-11-07-08 et GO-2026-11-06-01 ; autorisation de Lazar (R-1752) : « J’autorise la fille 6 à louer, surveiller et détruire sur Vast l’instance de l’épreuve E3 bis de T0.6, sous GO-2026-11-07-08 et GO-2026-11-06-01 (plafond 5,70 USD, création au plus tard le 10 novembre). » Aucune valeur de clé, aucune sortie brute de vastai, aucun résultat de sonde lu (seules les clés de l'extracteur).

## Verdict
Le run a tourné de bout en bout sur le vrai modèle (36 épisodes, 144 actions, fin code 0, poussée finale), instance détruite, 3,652 USD (≤ 5,70), cumul 5,744 USD (≤ 7,9). **Conformes : E3-1, E3-2, E3-4, E3-5, E3-7, E3-9, E3-10, E3-11, E3-12. Non conforme : E3-6** (bloc `equivalence_99e_centile` absent pour les six états). **Réserves : E3-3** (secondes par pas : 45 pas déclarés, mais 4 entrées par adaptateur dans le journal des pas) et **E3-8** (durée par jeton non calculable avec les clés de l'extracteur ; instance à 255 cœurs, pas 16).

## Écarts acceptés (inchangés)
Jeton `CONTROLE_IA_GITHUB_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"` sous `env -i` (R-1667) ; arbre `git worktree` détaché ; environnement `/home/user/venv-depot`.

## Instance
- Identifiant **59671807** ; offre 41153689 (rang 3, machine 67802) ; carte A100 SXM4 80 Go ; carte 2,000000 + stockage 0,069444 = 2,069444 USD/h ; téléchargement 0,0040 USD/Go (forfait 0,16). Règle des 2,5 h : 5,33 ≤ 5,70.
- Création **2026-11-08T05:47:22Z** ; fin de run **07:31:48Z** (« run terminé ») ; poussée finale 07:32:05Z ; « fin, code 0 » (code de sortie de l'amorce : **0**) ; « ARRÊT OBTENU (état voulu « stopped », HTTP 200) » 07:32:06Z ; surveillance « FIN : run terminé » 07:33:09Z ; destruction **07:35:36Z** (`destroy instance 59671807 -y`, code 0, « destroying instance 59671807. »).
- Branche `essai/t06-e3bis-v1`, dernier commit **a5c0e298** ; trois commits sur c01d29ea, conformes à l'attendu : df66798a « résultats et données légères » ; 0d880fab « sous-ensemble d'activations en morceaux » ; a5c0e298 « traces de l'instance (fin) ». Traces `traces/t06-20261108-073203-zdSu/` ; morceau `donnees/20261108-065822-t06-reel/activations-sous-ensemble-t06-000.npz` (29 217 622 octets).
- Inventaire après destruction : `t06-e3` = 0. Restent sur le compte (non touchées) : 58936096, 58936099, 58936100 (R8, à Lazar) et **59288960 « sparks-exp7-nul-v5-0d163bdcea56 », arrêtée, facturée 0,033 USD/h de stockage** (signalée, hors de cet ordre).
- Boucle de capture des journaux (PID 656) arrêtée par son PID à 07:35:29Z.

## Dernière ligne exacte de la suite ciblée (E3-2)
`1878 passed in 4009.60s (1:06:49)`

Durée : 1 h 06 min 49 s (estimation de l'ordre 40 à 50 min ; dépassement relevé comme résultat). N = 1 878 = estimation.

## Table E3-1 à E3-12
| Point | Attendu | Obtenu (ligne exacte ou clé) | Verdict |
|---|---|---|---|
| E3-1 | installation, torch cuda disponible, A100-SXM4-80GB 81 920 Mo | « torch 2.14.1+cu130 cuda 13.0 disponible True » ; « NVIDIA A100-SXM4-80GB, 595.91.07, 81920 MiB » | conforme |
| E3-2 | « suite ciblée : 81 fichiers d'essais » ; `N passed`, aucun échec ni saut | « 2026-11-08T05:51:30Z suite ciblée : 81 fichiers d'essais, liste scripts/tests-cibles-t06-v1.txt sha256 562b65fa…081572 » ; « 1878 passed in 4009.60s (1:06:49) » | conforme |
| E3-3 | mémoire < 80 Go, marge ≥ 10 % ; s/pas ; extrapolation 480 pas | `episodes.memoire_pic_gio` = 18.4 Gio (19,8 Go ; marge 75 %) ; `distillation.duree_s` = 576.0 ; `pas_declares` 45/45 (plan b) ; `pas_par_adaptateur` : saboteur 4, témoin 4 (clés `epoque`, `perte`) ; précision float32. Si les 45 pas sont le total : 12,8 s/pas → 480 pas ≈ 6 144 s (1 h 42). Si 45 par adaptateur : 6,4 s/pas → ≈ 3 072 s | mémoire conforme ; **réserve** sur le compte des pas (45 déclarés contre 4 + 4 entrées journalisées : à lire par la mère) |
| E3-4 | réglage de déterminisme présent et vrai ; aucune ligne « non déterministe » | `episodes.reglages.deterministe` = true ; `relus.algorithmes_deterministes` = true, `cudnn_deterministe` = true, `cudnn_banc_essai` = false, `tf32` = false, `cublas_workspace` = « :4096:8 » ; « non déterministe » : 0 ligne dans `run.err` et `journal.txt` des traces | conforme |
| E3-5 | identité à dose 0 (écart nul ou sous tolérance) | saboteur : `dose_0_identique` true, `dose_1_differente` true, `ecart_max_dose_1` 8.484375 ; témoin : true, true, 12.25. Tolérance non imprimée par l'extracteur (identité exacte, écart nul) | conforme |
| E3-6 | bloc `equivalence` présent pour chaque état ; aucun écart au-dessus de la tolérance | `equivalence_99e_centile` : S100, S25, S50, S75, T100, dose0 = « absent » | **non conforme** (attendu manquant) |
| E3-7 | durée, volume, débit Mo/s ; `reecrits` 0 ; libre ≥ pire cas | `episodes.duree_s` 681.5 ; `sous_ensemble` : 14 actions, couche 15, float16, 144 notées ; `morceaux` 1 ; `reecrits` 0 ; disque libre 133 925 609 472 ≥ pire cas 1 415 577 600 (exigé 1 557 135 360). Volume du morceau poussé : 29 217 622 octets → 29,2 Mo / 681,5 s = **0,043 Mo/s** (durée des épisodes entière, génération comprise : borne basse du débit d'écriture) | conforme |
| E3-8 | durée par couple Mahalanobis (16 cœurs), par jeton si calculable | `mahalanobis-c7` 89.9 s ; `-c15` 90.3 s ; `-c23` 91.3 s. Par jeton : non calculable avec les clés de l'extracteur (aucun compte de jetons par couple). Instance : 255 cœurs (« MATERIEL … coeurs=255 ») | relevé ; **réserve** (pas sur 16 cœurs, pas de rapport au jeton) |
| E3-9 | `egalite_jetons_reels` vrai ; 12 essais ; `tous_egaux` ; écart ≤ 1e-12 | `egalite_jetons_reels` true ; `jetons_reels` : essais 12, tous_egaux true, `ecart_relatif_max` 6.404513287858044e-15, 256 jetons ; `jetons_tires` : 12, true, 5.424465182706785e-15 | conforme |
| E3-10 | `MemTotal_ko` ≥ 121 600 000 | « AMORCE 2026-11-08T05:51:24Z : MATERIEL MemTotal_ko=2101179772 coeurs=255 flock=oui » | conforme |
| E3-11 | E3 bis ≤ 5,70 ; cumul ≤ 7,9 | E3 bis **3,652 USD** ; cumul E2 0,627 + E3 1,465 + E3 bis 3,652 = **5,744 USD** | conforme |
| E3-12 | le run démarre (lanceur v5) ; `run.json` ; pas d'`arret.json` | « 2026-11-08T06:58:22Z run : 20261108-065822-t06-reel (sans couperet de temps ; lanceur v5) » ; `traces/…/run.json` présent ; aucun `arret.json` pour ce run (seuls trois anciens d'octobre sous `diag/`, noms de fichiers seuls) | conforme |

## Lignes PROGRES relevées
format verifie=True (06:59:07Z) ; disque libre_go=133.9 pire_cas_go=1.4 ; identite adaptateurs=2 (07:08:02Z) ; episodes-ecrits episodes=36 actions=144 morceaux=1 reecrits=0 (07:19:24Z) ; lecture-cout duree_s=1257.9 ; test-croise jeux=2 duree_s=27.1 ; fin episodes=36 actions=144 (07:31:43Z).

## Facture (relevé `show invoices-v1 -c -s 2026-11-06 -e 2026-11-09`, 2026-11-08T07:37Z, 12 lignes)
- **Instance 59671807 : 3,652 USD** = 3,457 (1,729 h à 2,000 USD/h) + 0,126 (1,810 h à 0,069 USD/h de stockage) + 0,069 (17,3 Go téléchargés à 0,004 USD/Go). Relevé pris 2 minutes après la destruction : à confirmer stable par un second relevé (une ligne d'envoi peut s'ajouter).
- E2 (relevé antérieur) : 59555071 0,149 + 59589344 0,019 + 59590613 0,099 + 59598117 0,289 + 59601024 0,071 = 0,627 USD. E3 : 59623267 1,465 USD.
- **Cumul E2 + E3 + E3 bis = 5,744 USD** (plafond 7,9).
- Fichier : `factures-2026-11-06-au-09-releve-0737Z.json` (à côté de ce compte rendu).

## Texte exact du dernier `show instance 59671807 --raw` (un seul, après destruction)
```
{
 "instances": null
}
```
Fichier : `show-instance-59671807-apres-destruction.txt`.

## Sortie complète de l'extracteur (`extraire_mesures_epreuve_t06_v1.py`, code 0)
```
{
 "distillation": {
  "duree_s": 576.0,
  "identite_dose_0": {
   "saboteur": {
    "dose_0_identique": true,
    "dose_1_differente": true,
    "ecart_max_dose_1": 8.484375,
    "empreinte": "a3d8e6bbf3db20e52afb3bb0e076a94116b8ae3b2017f809f37a9bb471a1b38c"
   },
   "temoin": {
    "dose_0_identique": true,
    "dose_1_differente": true,
    "ecart_max_dose_1": 12.25,
    "empreinte": "4d3c7232209f54a8460be1e906551ad1856ee88f073161a103ca735b02c17e19"
   }
  },
  "jetons_controle": 293,
  "pas_declares": {
   "pas_attendus": 45,
   "pas_declares": 45,
   "plan": "b"
  },
  "pas_par_adaptateur": {
   "saboteur": {
    "cles_d_un_pas": [
     "epoque",
     "perte"
    ],
    "pas": 4
   },
   "temoin": {
    "cles_d_un_pas": [
     "epoque",
     "perte"
    ],
    "pas": 4
   }
  },
  "plan": "b",
  "precision_adaptateurs": "float32"
 },
 "durees_par_couple_s": {
  "attention-c15": 58.8,
  "attention-c23": 56.9,
  "attention-c7": 55.2,
  "decisif": 27.1,
  "difference_moyennes-c23": 20.8,
  "difference_moyennes-c7": 21.1,
  "lineaire-c15": 38.1,
  "lineaire-c23": 38.4,
  "lineaire-c7": 37.3,
  "mahalanobis-c15": 90.3,
  "mahalanobis-c23": 91.3,
  "mahalanobis-c7": 89.9,
  "perceptron-c15": 36.9,
  "perceptron-c23": 37.2,
  "perceptron-c7": 36.8
 },
 "episodes": {
  "chrono": {
   "generation_s": 1045.7879146202467,
   "jetons_contexte": 209944,
   "jetons_contexte_remplis": 240532,
   "jetons_generes": 69665,
   "jetons_passe_unique": 103793,
   "jetons_remplissage": 30588,
   "lignes_finies_avant": 195,
   "longueur_remplie_max": 1744,
   "passe_unique_s": 10.084780467906967,
   "passes_decodage": 15067
  },
  "disque": {
   "exige_octets": 1557135360,
   "libre_octets": 133925609472,
   "pire_cas_octets": 1415577600
  },
  "duree_s": 681.5,
  "memoire_pic_gio": 18.4,
  "morceau": {
   "borne_remplissage_une_action": 85000000,
   "pire_cas_action_octets": 3276800
  },
  "morceaux": 1,
  "noyau_attention": "defaut",
  "reecrits": 0,
  "reglages": {
   "appareil": "cuda",
   "capacite": [
    8,
    0
   ],
   "carte": "NVIDIA A100-SXM4-80GB",
   "cublas_workspace": ":4096:8",
   "cuda": "13.0",
   "cudnn": 92400,
   "deterministe": true,
   "fils": 1,
   "numpy": "2.4.6",
   "pilote": "595.91.07",
   "reduction_reduite_bf16_fp16": false,
   "relus": {
    "algorithmes_deterministes": true,
    "cudnn_banc_essai": false,
    "cudnn_deterministe": true,
    "fils": 1,
    "precision_produits_cuda": "ieee",
    "precision_produits_simple": "highest",
    "reduction_reduite_bf16": false,
    "reduction_reduite_fp16": false,
    "tf32_cudnn": false,
    "tf32_produits": false
   },
   "tf32": false,
   "torch": "2.14.1+cu130"
  },
  "sous_ensemble": {
   "actions": 14,
   "couche": 15,
   "precision": "float16",
   "total_notees": 144
  }
 },
 "equivalence_99e_centile": {
  "S100": "absent",
  "S25": "absent",
  "S50": "absent",
  "S75": "absent",
  "T100": "absent",
  "dose0": "absent"
 },
 "mahalanobis": {
  "calcul": "produit_matriciel_v2",
  "egalite_jetons_reels": true,
  "jetons_reels": {
   "ecart_relatif_max": 6.404513287858044e-15,
   "essais": 12,
   "n_jetons_min_max": [
    256,
    256
   ],
   "tous_egaux": true
  },
  "jetons_tires": {
   "ecart_relatif_max": 5.424465182706785e-15,
   "essais": 12,
   "n_jetons_min_max": [
    256,
    256
   ],
   "tous_egaux": true
  }
 },
 "resume": {
  "actions": 144,
  "actions_notees": 144,
  "duree_s": 1996.4,
  "episodes": 36,
  "mahalanobis_calcul": "produit_matriciel_v2",
  "morceaux": 1,
  "morceaux_reecrits": 0
 },
 "run": "20261108-065822-t06-reel"
}
```

## Attendus manquants et arrêts
- E3-6 : `equivalence_99e_centile` absent pour les six états d'évaluation.
- E3-3 : compte des pas par adaptateur (4) différent des 45 pas déclarés ; secondes par pas donc ambiguës.
- E3-8 : pas de durée au jeton ; machine à 255 cœurs au lieu de 16.
- Aucun arrêt de garde ; aucune étape manquée. Arrêt de l'instance par l'amorce en fin de run, destruction par l'identifiant.

## Ensuite
En attente des instructions de la mère.
