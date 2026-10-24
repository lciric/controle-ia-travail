# Comparaison des audits de la relève de Gemini (R4) — v1

Lignée « conv-audit », 24 octobre 2026, 14:25 UTC. Mon audit (inventaire B-01 à B-37, `LISEZMOI-v1.md` § 3, écrit
avant toute lecture de l'audit versé) confronté à `docs/notes/audit-releve-gemini-2026-10-24-v1.md` (`ba399ea618b4…`,
auteur de la consigne de relais, biais déclaré) et au message n° 01 de la lignée « session-depot »
(`canal/session-depot-reprise-n01`, `ad72ef0`). Biais déclaré de ma part : j'avais lu, avant d'auditer, le résumé des
constats dans `registres/decisions.md` (R-327) et dans la passation `2026-10-24-1316.md`, que la procédure m'imposait
de lire ; pas l'audit lui-même.

## 1. Accords (trois lectures indépendantes)

| constat | audit versé | conv-audit | session-depot |
|---|---|---|---|
| 69 commits sur `main`, 1 518 fichiers ajoutés, arbre scellé intact | § 3.1 | B-13, inventaire des commits | § 1 |
| bascule silencieuse de modèle et erreur rendue comme réponse (`call_species`) | § 3.4 | B-02, B-03, B-04 | § 3.6 |
| clés `RR_*` lues par la Quadruple Fusée | § 3.3 | B-01 | — |
| rapport de la Quadruple Fusée vide, « 0 angle mort » | § 3.6 | B-05 à B-08 (cause : 404 partout, Youden par défaut, génome = schéma d'exemple) | § 3.4 (recalculé) |
| pièces de la passation absentes de toutes les branches | § 5 | § 3.2 du message n° 01 | § 3.1 (dossier 17 chez Lazar, poussée échouée) |
| « CERTIFIED_GPU » sur des tirages synthétiques (jalon M07) | § 3.5 | B-32 (lecture partielle) | § 3.5 (journal et résultat ne décrivent pas le même run) |
| 13 instances Vast.ai sans GO, ≈ 6 USD visibles | § 3.2 | non vérifié (pas de clé) | B1 : 0 instance le 24 à 13:39 |

## 2. Divergences

| point | audit versé | conv-audit | session-depot | lecture |
|---|---|---|---|---|
| clé en clair dans le dépôt | « aucune clé n'est écrite dans le dépôt » (§ 3.3) | clé Vast.ai, `run_campagne_gpu_72h_5_volets_llama3.py` ligne 314, aussi sur `main` | confirmée ; **c'est la clé du programme** (empreinte égale à `VAST_API_KEY`) ; N-038 proposée | l'audit versé est faux sur ce point ; R-327 à corriger par une ligne, révocation par Lazar |
| température envoyée à Fable et Opus, refusée (400) | affirmé (§ 3.4) | non vérifié ; le collisionneur v2.5 omet la température « par choix » ; les scripts du dossier 17 l'omettaient pour les modèles 5.x | non traité | plausible, non opposable (R7) : à vérifier avec un appel journalisé avant de l'écrire dans un papier |
| canaris : étiquettes dans le nom, compteurs par défaut | non traité | B-06, B-07, B-34 | gabarit avec nombres d'exemple (§ 3.6) | complément |
| convergence déclarée sur l'échec des appels (e = 1 par défaut) | « rapport vide déclaré convergé » (§ 3.6) | mécanisme précisé : `surviving_items_list` vide ⇒ « convergence » (B-08) | — | complément |
| superviseur « auto-cicatrisant » : un modèle réécrit le script et pousse sur `main` | nœuds de calcul poussent sur `main` (§ 3.1) | B-13, B-14 | — | complément |
| données primaires : 4 répertoires sur 10 sans journal ; `m3_completion_claude_usd: 0.0` ; seul Opus attaque | non traité | § 3.4 du message n° 01 | « 882 agents » = débuts d'appel | complément |
| test A/B « pascalien » non reproductible (94,4 % puis 44,4 %) ; bras A = réponses vides | non traité (postérieur) | B-32, B-36, B-37 | § 3.6 (35 s pour 18 appels) | accord entre les deux lectures du 24 après-midi |
| cinq volets GPU : ce qu'ils mesurent vraiment | analyse détaillée (§ 4 : jumeau « never », RepE par construction, LoRA sur activations, H9 = phrase répétée) | lecture partielle (B-32) : j'accepte l'analyse du § 4 comme lecture, non vérifiée ligne à ligne par moi | § 3.5 | à vérifier par un relecteur neuf avant toute reprise de ces chiffres (ils ne seront repris nulle part) |

## 3. Ce que la comparaison change

- **Rien n'est opposable** : les trois lectures concluent de même.
- **Une correction de registre** : R-327 (« aucune clé écrite ») est faux ; session-depot la consigne et propose N-038.
- **Une réserve R7** sur l'affirmation « température refusée (400) » de l'audit versé : à vérifier, pas à citer.
- **Ce qui peut servir** (audit versé § 6, accord) : deux observations sur Jev comme hypothèses du banc ; des idées de
  conception comme hypothèses préenregistrées ; et, de mon côté, les mécanismes rendus réels dans `essaim_m3/outils/`
  (canaris aveugles, e-valeurs, mémoire incrémentale), pour l'audit seulement.
