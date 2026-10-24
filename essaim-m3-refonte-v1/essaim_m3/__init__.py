"""essaim_m3 — refonte v1 de l'architecture d'essaim de Gemini (« Loi L de M3 », quatre fusées
Ω → Alpha → Gamma → Bêta, étages M3 → M2 → M1 → M0), corrigée bug par bug.

Sources de l'architecture (branche `quarantaine/releve-gemini-2026-10-23`, `f5cb537`, lecture seule) :
- `gemini/11_EDIFICE_…/16_QUADRUPLE_FUSEE_OMEGA_ALPHA_GAMMA_BETA/run_quadruple_fusee_omega_alpha_gamma_beta.py` ;
- `gemini/11_EDIFICE_…/16_QUADRUPLE_FUSEE_OMEGA_ALPHA_GAMMA_BETA/self_healing_quad_rocket_supervisor.py` ;
- `gemini/10_ESSAIM_INSPECTION_SCRIPT_L_STAR_V2/` (54 constats de l'essaim d'inspection sur un script absent du dépôt) ;
- le dossier de passation de Gemini du 24 octobre 2026 (données).

Règles du dépôt qui s'appliquent : R1 (préenregistrement avant toute expérience décisive), R3 (aucun run visant un
signe), R5 (toute garde testée sur un cas sain et sur un artefact ; aucun repli silencieux), R6 (empreintes), R9
(graines par SeedSequence, manifeste par run), R12 (versions dans les noms, rien n'est écrasé).

Aucun module de ce paquet n'appelle une interface de programmation sans un appelant fourni explicitement ; le mode
réel exige un GO de dépense (`registres/go.md`) et les clés dans l'environnement sous les noms `ANTHROPIC_API_KEY` et
`GEMINI_API_KEY` (le lanceur y passe la clé des runs, GO-2026-10-24-04 ; `ANTHROPIC_BASE_URL` retirée).
"""

VERSION = "essaim-m3-refonte-v1"
