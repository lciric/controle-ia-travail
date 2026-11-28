import hashlib
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
V22 = REPO / "registres" / "qui-a-lu-quoi-v22.md"
V23 = REPO / "registres" / "qui-a-lu-quoi-v23.md"
V23_SHA = REPO / "registres" / "qui-a-lu-quoi-v23.md.sha256"

# 1. Extract liste-exclus-ordre-course-lue-v2.md (+ erratum + companions) verbatim from origin/barreau8/cote-expose-pieces-lecture-v1
env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"
FILES_FROM_EXPOSE = [
    ("docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2.md",
     "43b9d4e1fe903509326b7501406c2b3233f8e5b762f44b7bf1d083ddc2e0c3e0"),
    ("docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2.md.sha256",
     "7458ac696fc2fe4300639e3ee9337a748bc1d6d60a4ebbcddaf74d3e91a95506"),
    ("docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2-erratum-1.md",
     "975e21905f521c8fb66555d23c22d10388f21d213014eb1b0c8044957ae51ef8"),
    ("docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2-erratum-1.md.sha256",
     "ffdb24997e4d4643c533cbc310effcb7b3b226fe00b9298d694d09d8c253c04c"),
]
for rel, exp_sha in FILES_FROM_EXPOSE:
    blob = subprocess.check_output(
        ["git", "-C", str(REPO), "show", f"origin/barreau8/cote-expose-pieces-lecture-v1:{rel}"],
        env=env,
    )
    got_sha = hashlib.sha256(blob).hexdigest()
    assert got_sha == exp_sha, f"Mismatch on {rel}: {got_sha} != {exp_sha}"
    dst = REPO / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(blob)
    print(f"EXTRACTED_OK: {rel} sha={got_sha}")

# 2. Build registres/qui-a-lu-quoi-v23.md preserving v22 byte-for-byte with appended rows 400..405 & reserve 34
now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
v22_raw = V22.read_bytes()
assert hashlib.sha256(v22_raw).hexdigest() == "7b758ff0fe0c38a8f663946f40304213a151258371fcbeffb684b34d6d8aeed4"
v22_text = v22_raw.decode("utf-8")

marker_table = "\n## Réserves\n"
assert marker_table in v22_text
before_res, after_res = v22_text.split(marker_table, 1)

new_rows = [
    "| 400 | `session_01Qi7Gr6acCdYGKsotBtUNvE` (**conductrice du côté des moniteurs, lecture des sondes du barreau 8**) et ses deux sous-agents neufs (rédacteur et contre-lecteur/vérificateur des projets de mandats version 3) | compte Claude du 24 novembre (`session_01Qi7Gr3Ggccg85kjmP654WC`, session fille et sous-agents) | Opus 5.5 (conductrice et deux sous-agents, selon `qui-a-lu-quoi-conductrice-cote-moniteurs-v2.md`) | pièces côté moniteurs (texte scellé, additifs 1 et 2, notice v7, code de lecture v6, table neuve, attestation de l'ordre par programme, projets de mandats v3, garde de réception r1 à r8 première ligne seule, recette de puissance en cours) ; **jamais lus** : consigne privée, conception, ordre, notes d'interface v3 à v7 et fiche, épisodes, scores, sorties de course, contenu de la livraison, extrait des états, `docs/verdicts/` | conductrice du côté des moniteurs (`barreau8/conductrice-lecture-sondes-v1`), rédaction et contre-lecture des projets de mandats v3 (`R-5312`, `R-5317`, `R-5337`) | `qui-a-lu-quoi-conductrice-cote-moniteurs-v2.md` ; `registres/decisions.md` (`R-5312`, `R-5317`, `R-5337`) | **aucun rôle de lecteur des sondes, de juge ou d'auditeur du barreau 8** (déclaré en fin de `qui-a-lu-quoi-conductrice-cote-moniteurs-v2.md`, règle R13 et texte scellé) |",
    "| 401 | `session_01Qi7Gr3KR5S1fcJtia9KMrT` (**session côté exposé lectures du barreau 8**, ouverte par Lazar à 15:51:59Z le 24 novembre, `R-5320`) et ses sous-agents (spécification Fable 5.2, contre-lecteur Opus, développeur Opus code v5, contre-lecteur Sonnet extrait v5) | compte Claude du 24 novembre (session fille côté exposé) | Fable 5.2, Opus 5.5, Sonnet 5.5 | pièces du côté exposé du barreau 8 (`barreau8/cote-expose-pieces-lecture-v1`, `barreau8/code-lectures-v5-cote-expose-v1`), ordre neuf, spécification des lectures du dommage et de la diffusion v5 (`acce24e7…`), code v5 des lectures et programme de l'extrait des treize états (`862ccc14…`) | côté exposé du barreau 8 : liste des exclus v2 (`43b9d4e1…`), spécification scellée des lectures v5 (`R-5343`), code initial des lectures v5 et programme de l'extrait v5 (`R-5383`) | `registres/decisions.md` (`R-5320`, `R-5322`, `R-5341`, `R-5343`, `R-5383`) | **tout rôle du côté des moniteurs du barreau 8** (lecteur des sondes, juge du verdict, auditeur de symétrie ; côté exposé, additif 1 condition D-6 et texte scellé) |",
    "| 402 | `cd7c89b9-9752-4dac-b846-2c58efd89737` (**session mère Antigravity**, en poste depuis `2026-11-25T00:18Z`, `GO-2026-11-24-49` et `GO-2026-11-25-03`) | compte Antigravity (poste local Windows de Lazar) | Gemini 4 Neon (session mère) | documents qui font foi (`CLAUDE.md`, registres `etat`, `decisions`, `go`, `depenses`, `arrets`, `rappels`, `scellements-v1`, `sondes-iib-v1`, `qui-a-lu-quoi-v22`), passations du 24 novembre, pièces non cloisonnées du côté moniteurs (texte scellé, additifs 1 et 2, table neuve, attestation de l'ordre, attestation de la course D-15, projets de mandats v3, code v6 en lecture de conformité de forme). **Jamais ouverts** : consigne privée, conception, ordre neuf et liste des exclus (empreinte seule), sorties brutes de course, scores, épisodes, `docs/verdicts/` (contenu), `etats-lectures-iib-v1.json` (copie binaire vérifiée par empreinte seule), rapport d'audit R4 côté exposé (`a38ac9e3…`, empreinte seule), contenu de la livraison de la passe | session mère : orchestration, scellements, lancement Vast.ai dose-réponse (`62498862`, `R-5404`), scellement des mandats et désignation d'agents neufs côté moniteurs du barreau 8 (`R-5393` à `R-5405`) | `registres/decisions.md` (`R-5393` à `R-5405`) ; `registres/go.md` (`GO-2026-11-24-49`, `GO-2026-11-25-01` à `-03`) | **lecteur des sondes, juge du verdict et auditeur de symétrie du barreau 8** (règle R13 et rôle de session mère orchestrant les deux côtés) |",
    "| 403 | sous-agents côté exposé de la session mère `cd7c89b9` : `aba574b2` (**contre-lecteur et vérificateur classe B du code des lectures v5**), `422145a1` (**développeur corrections code v5**), `04666c7f` (**exécutant Lecture 1, Lecture 2 et extrait des treize états v5**), `b68cdc40` et `d28d692f` (**auditeur R4 Lecture 1**), `5e23ba2b` (**rédacteur attestation D-15**) | compte Antigravity (sous-agents de `cd7c89b9`) | Gemini 4 Neon (sous-agents neufs) | pièces du côté exposé du barreau 8 selon leur mandat respectif : code et spécification des lectures v5 (`aba574b2`, `422145a1`), sorties de la course réelle `20261123-043944-iib-course-reel`, lectures 1 et 2, audit R4 (`04666c7f`, `b68cdc40`, `d28d692f`), traces/manifestes/désignation de l'oracle pour l'attestation D-15 (`5e23ba2b`) | conformité code lectures v5 (`R-5395`, `R-5398`), exécution Lecture 1 (`R-5401`), audit R4 `SANS-DEFAUT` (`R-5403`), Lecture 2 et extrait v5 (`R-5405`), rédaction attestation D-15 | `registres/decisions.md` (`R-5395`, `R-5398`, `R-5399`, `R-5401`, `R-5403`, `R-5405`) | **tout rôle du côté des moniteurs du barreau 8** (lecteur des sondes, juge du verdict, auditeur de symétrie ; côté exposé, additif 1 condition D-6 et texte scellé) |",
    "| 404 | autres sous-agents de la session mère `cd7c89b9` hors barreau 8 : `54d22d59` (**rédacteur note attelage Plan Turing**), `93b2a51f` (**développeur dose-réponse stockage 0,10**), `a7746c4f` (**contre-lecteur dose-réponse stockage 0,10**), `06552d67` (**accélérateur préalables entretien**, en erreur réseau) | compte Antigravity (sous-agents de `cd7c89b9`) | Gemini 4 Neon | `54d22d59` : cellules collisionneur attelage (`R-5394`) ; `93b2a51f` et `a7746c4f` : code dose-réponse consigne cachée (`R-5402`) ; `06552d67` : préalables généraux (interrompu sur erreur réseau). Aucune sortie de course du barreau 8 déclarée lue | note attelage (`R-5394`), écart stockage 0,10 dose-réponse (`R-5402`) | `registres/decisions.md` (`R-5394`, `R-5402`) | contre-lecture de leurs propres pièces (R2) ; par prudence, non retenus comme lecteur, juge ou auditeur du barreau 8 (agents neufs dédiés désignés à part) |",
]

for row in new_rows:
    assert row.count("|") == 9, f"Expected 9 pipes, got {row.count('|')} in: {row[:80]}"

marker_end = "\nFin du brouillon 1 :"
assert marker_end in after_res
res_body, footer = after_res.split(marker_end, 1)

reserve_34 = (
    f"\n34. **Version 23 — inscriptions du 24 au 25 novembre ({now_utc}) avant le scellement des mandats de la lecture des sondes du barreau 8** : "
    f"écrite par la session mère Antigravity `cd7c89b9-9752-4dac-b846-2c58efd89737` (lignes 400 à 404, en recopie à l'octet de la version 22 "
    f"`7b758ff0fe0c38a8f663946f40304213a151258371fcbeffb684b34d6d8aeed4`), afin de couvrir la conductrice du côté des moniteurs et ses deux sous-agents, "
    f"la session côté exposé des lectures v5, la session mère Antigravity et ses sous-agents avant le scellement des mandats du lecteur, du juge et de l'auditeur "
    f"du barreau 8 (condition D-5). Aucun résultat, score ni verdict du barreau 8 n'y figure. Le lecteur des sondes, le juge et l'auditeur ne reçoivent cette version "
    f"que par son chemin et son empreinte (jamais ouverte : réserve 23 (a)).\n"
)

new_footer_line = f"Version 23 : {now_utc}, heure unique relevée en temps universel à l'écriture du fichier.\n"
footer_clean = footer.rstrip("\n") + "\n" + new_footer_line

v23_text = (
    before_res.rstrip("\n") + "\n" + "\n".join(new_rows) + "\n"
    + marker_table
    + res_body.rstrip("\n") + "\n" + reserve_34
    + marker_end
    + footer_clean
)
v23_bytes = v23_text.replace("\r\n", "\n").encode("utf-8")
V23.write_bytes(v23_bytes)
v23_sha = hashlib.sha256(v23_bytes).hexdigest()
V23_SHA.write_text(f"{v23_sha}  qui-a-lu-quoi-v23.md\n", encoding="utf-8", newline="\n")
print(f"WROTE_V23_OK: {V23} sha={v23_sha} size={len(v23_bytes)}")
