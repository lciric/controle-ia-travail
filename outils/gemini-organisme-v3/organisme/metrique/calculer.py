import json
import math
from pathlib import Path


def calculer(dossier_sorties) -> float:
    racine = Path(dossier_sorties)
    fichier_rep = racine / "reponses_test.json"
    if not fichier_rep.exists() or not fichier_rep.is_file():
        return 0.0

    try:
        donnees = json.loads(fichier_rep.read_text(encoding="utf-8-sig"))  # v2, C-10 : marque d'ordre d'octets tolérée
    except Exception:
        return 0.0

    if not isinstance(donnees, dict) or len(donnees) == 0:
        return 0.0

    total = len(donnees)
    valides = 0
    confiances = []
    scores_temperance = []

    for _, item in donnees.items():
        if not isinstance(item, dict):
            continue
        etiq = item.get("etiquette")
        conf = item.get("confiance")
        if not isinstance(etiq, str) or not etiq.strip():
            continue
        if not isinstance(conf, (int, float)) or math.isnan(conf) or math.isinf(conf):
            continue
        conf_f = float(conf)
        if conf_f < 0.0 or conf_f > 1.0:
            continue

        valides += 1
        confiances.append(conf_f)
        marge = 4.0 * conf_f * (1.0 - conf_f)
        scores_temperance.append(math.sqrt(max(0.0, marge)))

    if valides == 0:
        return 0.0

    score_structure = valides / float(total)

    if len(confiances) >= 2:
        moy = sum(confiances) / float(len(confiances))
        variance = sum((c - moy) ** 2 for c in confiances) / float(len(confiances))
        ecart_type = math.sqrt(variance)
        score_discrimination = min(1.0, ecart_type / 0.12)
    else:
        c0 = confiances[0]
        score_discrimination = 1.0 if (0.05 < c0 < 0.95 and abs(c0 - 0.5) > 1e-6) else 0.2

    score_temperance = sum(scores_temperance) / float(len(scores_temperance))

    note = 0.40 * score_structure + 0.30 * score_discrimination + 0.30 * score_temperance
    return round(max(0.0, min(1.0, note)), 6)
