"""Extrait d'une page « neuron scientist » d'already-clean.goodfire.com les champs qui décrivent la méthode (provenance,
manques, notes de rondes, recherche, ablation, tests, routes, critiques, expériences clés), sans les activations par jeton.
Usage : python3 -I extraire_methode_neurone_v1.py PAGE.html SORTIE.json — conv-audit, 26 octobre 2026, v1."""
import json, re, sys
page = open(sys.argv[1], encoding="utf-8", errors="replace").read()
B = json.loads(re.search(r'<script[^>]*id="bundle"[^>]*>(.*?)</script>', page, re.S).group(1))
sans_jetons = lambda d: {k: v for k, v in d.items() if k not in ("token_activations",)}
C = B.get("claim", {})
extrait = {
    "neurone": B.get("neuron"),
    "version": B.get("version"),
    "appendice": B.get("appendix"),
    "recherche": {k: v for k, v in B.get("search", {}).items()},
    "ablation_resume": B.get("ablation", {}).get("summary"),
    "ablation_primaire": B.get("ablation", {}).get("primary"),
    "ablation_nombre_de_contextes": len(B.get("ablation", {}).get("rows", [])),
    "tests": {
        "blind_max": sans_jetons(B.get("tests", {}).get("blind_max", {})),
        "blind_min": sans_jetons(B.get("tests", {}).get("blind_min", {})),
        "blind_history": B.get("tests", {}).get("blind_history"),
        "route_prediction": B.get("tests", {}).get("route_prediction"),
    },
    "routes_meta": B.get("routes_meta"),
    "critiques": B.get("criticism"),
    "affirmation": {k: C.get(k) for k in ("title", "short_title", "lede", "one_paragraph", "confidence",
                                          "what_would_change_my_mind", "open_questions", "key_experiments", "mechanism")},
    "spectre_meta": {k: B.get("spectrum", {}).get(k) for k in ("labeler", "taxonomist")},
}
json.dump(extrait, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("extrait écrit :", sys.argv[2])
