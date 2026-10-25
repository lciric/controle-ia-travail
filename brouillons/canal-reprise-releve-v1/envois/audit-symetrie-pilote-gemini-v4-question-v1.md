# Audit de symétrie (R4) du rapport mécanique v1 du pilote `pilote-gemini-organisme-v4-question-v1` — retour du sous-agent neuf, tel quel

Lancé par la lignée « conv-audit » le 25 octobre 2026 à 08:43 UTC ; fini à 08:55 UTC (12 min). Dossier remis au
sous-agent (lecture seule) : le préenregistrement scellé `1c5b6f7d…`, `LANCEMENT.md`, l'extrait mécanique, les deux
journaux d'appels, la copie de la réponse, la sortie d'erreur du lanceur, `principal.py` et `mitose_spectrale.py` de la v4,
l'extrait `appeler_anthropic` de `collisionneur_v2.py`, et le rapport v1 à auditer. Aucun score dans ces pièces. Le
sous-agent n'avait écrit ni le préenregistrement ni le rapport. Son retour, sans changement :

---

**Audit de symétrie (R4) — pilote `pilote-gemini-organisme-v4-question-v1`, rapport mécanique v1**

**(a) Verdict** : rapport exact sur tous les comptes (aucun écart, même d'une unité, sur appels, statuts, espèces, rôles, plafonds, jetons, durées, coûts, dates, empreintes, structure de la réponse) ; **à corriger ou préciser sur neuf points de formulation ou d'attribution** (b), dont deux touchent la symétrie (b1, b9 ; d1).

**(b) Écarts et imprécisions**
1. § 2 / § 4.1 — l'échec « HTTP 200 APIStatusError » (g000, `organisme-0040`, 07:54:38.017 UTC, 5,317 s) porte **le même message** « Your credit balance is too low… » (`journal-appels-g000.jsonl`) : c'est le premier échec de crédit, reçu dans le flux. Le rapport le laisse sans cause. Les 84 + 127 `ECHEC_API` portent tous ce message, identifiants de requête tous distincts.
2. § 4.1 « épuisé **tôt** dans g000 » : bascule à l'appel 40 sur 123, après 39 appels servis, 1,9754 USD de cumul, 329,7 s sur 352 (07:49:08.337 → 07:54:38.017). Tôt en appels (32 %), tard en temps (94 %). Donner numéro et heure.
3. § 1 « appel de contrôle par espèce **OK** » : `LANCEMENT.md` l. 13 n'atteste que « présent et non vide ; statut vérifié par l'outil de session-depot, non par ce script ». Le statut OK n'est pas dans les pièces.
4. § 4.2 `output_config={"effort": "high"}` : l'extrait de l'appelant (l. 11) écrit `EFFORT`, constante hors extrait ; « high » non vérifiable ici.
5. § 4.2 range la troncature d'Argon (`organisme-0126`) sous « réflexion comptée » : **4 149 caractères visibles pour 1 200 jetons (3,46 car./jeton)**, contre 0 à 1,98 car./jeton sur les 32 appels Fable `TRONQUE`/`VIDE`. Pour Argon le texte visible remplit le plafond : cause distincte (consigne de la question en trois parties puis JSON en fin, 1 200 jetons).
6. § 2 / § 3 : la 5ᵉ caste (`arbitre_synthese_contradictoire`, Opus) a reçu la consigne de caste ordinaire à **1 200**, non la synthèse à 1 500 : `principal-v4.py` l. 337, `est_arbitre` exige au moins une contribution. Le préenregistrement annonçait 1 500. « 5 à 1 200 » est exact ; dire pourquoi.
7. § 4.3 « cyber (tâches de la famille contrôle de délégation) » : le journal ne porte ni identifiant de tâche ni famille (`sha256_prompt` seul) ; non vérifiable. « reasoning_extraction (la consigne demande un champ raisonnement) » : le champ existe (l. 294) ; le lien avec la catégorie est une conjecture, à dire comme telle.
8. § 5 « la partie scores … sera vide ou **dégénérée** » : adjectif sur des scores non lus (« tout adjectif sur un score » interdit) ; la déduction depuis `n_reponses_test` = 0 est mécanique, la formuler sans qualifier.
9. § 4.2 « le journal du noyau ne garde pas les types de blocs » : exact, mais l'appelant les calcule (`types_blocs`, l. 24) : l'information existait et a été perdue au journal — défaut côté noyau, à nommer.

Vérifié conforme : empreintes recalculées des 7 pièces = rapport et `LANCEMENT.md` (dont préenregistrement `1c5b6f7d…`, graine écrite dedans) ; coûts de chaque appel = tarif 10/50 (Fable, Argon), cumuls cohérents ; 32/32 `TRONQUE`/`VIDE` à `usage.sortie` = `max_tokens` ; aucun chevauchement d'appels ; manifeste = ligne de commande scellée (160/20/1 800/4 096/40, cibles g001, `especes_amorcage` vide, isolation 4/4, collisionneur conforme, commit `2d01805a`, noyau `68494279`, organisme `c5ada335`, question `d967b212`) ; essais 113 + 0 + 1 = 114 ; réponse : texte d'abstention identique au code (l. 552-569), bloc ORGANISATION = journal (128/0/128, 0,07391 USD).

**(c) Les deux causes du rapport**
- Établi : 211/211 `ECHEC_API` = message de crédit du fournisseur, Opus compris (2/2) ; aucun appel Anthropic servi après 07:54:38 ; les 32 appels Fable servis non refusés finissent tous à `max_tokens` ; garde de temps jamais approchée (352 s < 1 350) ; `erreurs` de l'organisme vides.
- Probable : jetons de sortie non textuels sur **chaque** appel Fable servi (0 à 1,98 car./jeton ; 5 appels à 0 caractère pour 640 ou 1 024 jetons) — compatible avec une réflexion comptée dans le plafond ; sans outil, aucun autre type de bloc n'explique des jetons sans texte.
- Indécidable : valeur de `EFFORT` ; présence effective de blocs de réflexion (non journalisés) ; si 640 auraient suffi sans jetons cachés (analyse par étiquette puis JSON en fin, entrées de 298 à 10 047 jetons) ; solde réel au départ ; les 5,3 s de l'appel 40 (reprises du SDK invisibles) ; si un texte `TRONQUE` contenait un objet JSON (l'organisme jette tout texte non `OK`, l. 85 et 107).

**(d) Causes supplémentaires**
1. **Porte d'entrée sans test de solde** : l'appel de contrôle vérifie qu'un appel passe, pas que le solde couvre le devis (≈ 10-14 USD attendus, 40 au pire) ; le crédit a tenu 1,9754 USD. Garde absente de la liste d'arrêt (ligne « appel de contrôle » du préenregistrement). Le rapport est trop indulgent envers le dispositif sur ce point.
2. **Conception de l'organisme** : JSON exigé en fin après une analyse ouverte, plafonds 640/512/1 024 (`principal-v4.py` l. 284-295, 681, 813, 831) ; tout statut non `OK` jeté ; aucun arrêt sur échec répété : 210 appels après le premier refus de crédit (0 USD, ≈ 1 min). Le préenregistrement annonçait `TRONQUE` « mode d'échec le plus probable » pour cette raison : co-cause avec les jetons cachés chez Fable, seule cause visible chez Argon.
3. **Cascade** : induction `VIDE` → `regles_induites` vide dans les 122 consignes suivantes (l. 806-819, 287) ; sans effet sur le constat, à rapporter.
Liste d'arrêt : plafonds, délais, modèle servi, journal présent, successeur, isolation, relance — rien n'avait à jouer ou a joué ; la garde crédit (402) n'a pas joué sur un 400, dit par le rapport. Lectures : rien d'interdit lu avant le moment du plan § 3 ; le canal latéral (`contexte.json`) n'est ni calculé ni cité.

**(e) Non vérifiable depuis les pièces** : statut de l'appel de contrôle ; `A-POUSSER-v1.txt`, `EMPREINTES-pilote-v1.txt`, `ferme.tar.gz` (1 428 entrées) ; identité du code ayant tourné avec `principal-v4.py` / `mitose_spectrale-v4.py` (seules les tailles 45 801 et 5 510 octets concordent avec l'extrait ; l. 14 `set` confirmée) ; R-389, R-395, CL5-01, CL5-07, `90595ffb`, `224de13` (registres hors pièces) ; ligne du GO tronquée dans le manifeste, nom du pilote non visible ; `reponses_test.json` absent de `fichiers_travail` alors que le code l'écrit toujours (l. 911) — exclusion de l'outil ou déplacement par le noyau, à voir à l'ouverture ; comptage des jetons de réflexion d'Argon par l'appelant Gemini (hors extrait).
