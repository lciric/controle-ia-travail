"""Brouillon 3 = brouillon 2 + les remplacements AP-1 à AP-10 de la contre-lecture 1, appliqués mot pour mot (voie B,
décision de conv-audit, sans contre-lecture 2), avec les seules adaptations décidées par la session (marquées SESSION) :
AP-1 (heures du brouillon 3 écrites), AP-5 option (b) et la phrase « nœud de Lazar », AP-7 et AP-8 (version scellée de
l'analyse secondaire citée au lieu du brouillon 4 ; omission de la lecture par épisode consignée par la session), AP-4
(entrée « Contre-lecture 1 » remplie dans le brouillon final).

Gardes : empreintes du brouillon 2 et du rapport vérifiées ; chaque ancien texte présent exactement le nombre de fois
attendu (1, sauf l'heure d'AP-1 : 13) ; brouillon 3 absent avant l'écriture (R12). Aucun autre fichier n'est écrit.
Usage, depuis la racine du dépôt : PYTHONPATH=src python <ce fichier>
"""
import hashlib
import sys
from pathlib import Path

D = Path("brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1")
B2 = D / "preenregistrement-analyse-principale-r1-r2-v1-brouillon2.md"
B3 = D / "preenregistrement-analyse-principale-r1-r2-v1-brouillon3.md"
RAPPORT = D / "contre-lecture-preenregistrement-analyse-principale-r1-r2-v1.md"
SHA_B2 = "fb1373931d0865715b6f3962c66f1384f62f266b500026acb4af87a658f8f41f"
SHA_RAPPORT = "eff5d4cacad00e7da4dd0d28df024516d976fa2b6e084bfbdede96352ab04606"
SECONDAIRE = ("`prereg/analyse-blanche-noire-v3.md`, sha256 "
              "`1f6a6da2c551060a5f90ff3358b0aaf276dd9f336a5b953e6d93233c8c581fa9`, commit `7a238666`, R-1096")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


R = []   # (identifiant, ancien, nouveau, nombre d'occurrences attendu)

# AP-1 — heures
R.append(("AP-1 a", "2 novembre 2026 ≈ 00:45 Paris", "2 novembre 2026 ≈ 00:45 UTC (≈ 01:45 heure de Paris)", 13))
R.append(("AP-1 b (SESSION : heures du brouillon 3 écrites)", "brouillon 2 entre 00:47 et 01:05 ;",
          "brouillon 2 et code v2 entre ≈ 00:45 et 00:51 (heures de modification : constantes_v2.py 00:45:55, "
          "brouillon 2 00:50:04 ; commit 32179148 à 00:51:25) ; brouillon 3 (corrections de la contre-lecture 1) : "
          "le 2 novembre 2026 entre 01:15 et 01:45 UTC, par le script `appliquer-contre-lecture-1-v1.py` ;", 1))

# AP-2 — étape 0.f, textes de P3 : vérification seulement
R.append(("AP-2 a",
          "; **restaurer, dans l'arbre séparé seulement** (rien n'est écrit dans l'arbre principal), les textes de P3, "
          "absents du disque de travail (R11 : vérifié) : `git show a6c550ea76df6e086c90c1c9e7ef417f59ae658f:donnees/"
          "20261019-230011-p3-reel/textes-actions-p3.jsonl > donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl` "
          "puis `git show a6c550ea76df6e086c90c1c9e7ef417f59ae658f:donnees/20261019-230011-p3-reel/textes-actions-p3."
          "jsonl.sha256 > donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl.sha256` ; vérifier `sha256sum donnees/"
          "20261019-230011-p3-reel/textes-actions-p3.jsonl` = `ba05fa13af2dd4f935334438b44d2d27fbc655a970721b10b90bd94b5846f284` "
          "(empreinte que citent `diag/20261019-230011-p3-reel/resume.json` et `episodes-p3.json`, et "
          "`constantes_v1.EMPREINTES_P3`) et `PYTHONPATH=src python -m controle_ia.scellement verifier donnees/"
          "20261019-230011-p3-reel/textes-actions-p3.jsonl` ; `donnees/` est ignoré par git : l'arbre reste propre.",
          "; **textes de P3** : `donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl` et son compagnon `.sha256` sont "
          "suivis par git (au commit `32179148`, objet `bad1403f1454f46de23adbbee59da8586170c7ec` ; présents dans l'arbre "
          "principal, vérifié par la contre-lecture 1 le 2 novembre 2026 vers 01:00 UTC) : `git worktree add` les écrit "
          "dans l'arbre séparé. Vérifier sur disque et par empreinte (R11) : `git rev-parse HEAD:donnees/"
          "20261019-230011-p3-reel/textes-actions-p3.jsonl` → `bad1403f1454f46de23adbbee59da8586170c7ec` ; `sha256sum "
          "donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl` → "
          "`ba05fa13af2dd4f935334438b44d2d27fbc655a970721b10b90bd94b5846f284` (empreinte que citent "
          "`diag/20261019-230011-p3-reel/resume.json` et `episodes-p3.json`, et `constantes_v1.EMPREINTES_P3`) ; "
          "`PYTHONPATH=src python -m controle_ia.scellement verifier donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl`. "
          "Aucune restauration ni écriture par redirection sur ce fichier ; s'il manque ou si une vérification échoue, ne "
          "pas lancer et signaler (une restauration depuis `a6c550ea`, hors de l'historique de la branche, serait un geste "
          "neuf, déclaré).", 1))
R.append(("AP-2 b", "(`ba05fa13…` aux trois), sans en lire le contenu.",
          "(`ba05fa13…` aux trois), sans en lire le contenu. Le fichier est aussi présent dans l'arbre principal et suivi "
          "par git (constat de la contre-lecture 1 ; l'auteur l'avait cru absent).", 1))

# AP-3 — réception des sorties et ordre
R.append(("AP-3 a", "(aucun `git fetch` de cette branche, aucune lecture de ses fichiers, avant le scellement et la "
                    "vérification e).",
          "(aucun `git fetch` de cette branche **dans ce dépôt**, arbres de travail compris — ils partagent objets et "
          "références —, aucune lecture de ses fichiers, avant le scellement et la vérification e ; avant 0.0, la session "
          "consigne au registre l'état des références `calcul/r1-r2-reel-v1` du dépôt, présentes ou non, sans en ouvrir "
          "aucun fichier).", 1))
R.append(("AP-3 b",
          "Récupérer les sorties du fournisseur (`git fetch` de la seule refspec de la branche de résultats, dans l'arbre "
          "séparé) : `donnees/<run>/`, `runs/<run>/manifeste.json`, `diag/<run>/rejeu-activations.json` ou `arret.json`, "
          "et les mêmes pour chaque juge ; vérifier leurs empreintes (`.sha256` compagnons) **sans ouvrir aucun `.npz`** ;",
          "Récupérer les sorties du fournisseur, pour chaque run (rejeu, juge 3B, juge 8B) : `git fetch origin "
          "calcul/r1-r2-reel-v1` (seule refspec) ; `git checkout FETCH_HEAD -- runs/<run> diag/<run>` (manifeste, "
          "`rejeu-activations.json` ou `arret.json`, `juge-actions.json`, compagnons) puis **commit de ces seuls chemins** "
          "(`runs/` et `diag/` ne sont pas ignorés : sans ce commit, la commande décisive s'arrête sur « arbre de travail "
          "non propre ») ; les fichiers `donnees/<run>/…` sont écrits dans l'arbre séparé **sans passer par l'index** "
          "(`git show FETCH_HEAD:<chemin> > <chemin>`, fichiers absents auparavant ; `donnees/` est ignoré) ; jamais de "
          "`git merge` de la branche de résultats ; vérifier leurs empreintes (`.sha256` compagnons) **sans ouvrir aucun "
          "`.npz`** ; `git status --porcelain --untracked-files=all` vide ;", 1))

# AP-4 — parade de Q9
R.append(("AP-4 a", "0. **Avant l'étape a** : l'empreinte du brouillon final contre-lu est inscrite au registre de "
                    "conv-audit et poussée (parade de Q9) ; aucune variante de ce texte n'est scellée hors du dépôt.",
          "0. **Avant l'étape a** : l'entrée « Contre-lecture 1 » est écrite **dans le brouillon final** (elle ne dépend "
          "pas du commit) ; il n'y reste qu'un marqueur, la ligne « Commit du code d'analyse ». L'empreinte de ce brouillon "
          "final est inscrite au registre de conv-audit et poussée (parade de Q9) ; aucune variante de ce texte n'est "
          "scellée hors du dépôt.", 1))
R.append(("AP-4 b", "n'y remplacer que les deux marqueurs (commit cité ; entrée de la contre-lecture), vérifier par "
                    "`diff` et par `controle_ia.prereg.problemes` (vide)",
          "n'y remplacer que le marqueur du commit cité (40 caractères de `git rev-parse HEAD` après l'étape a), vérifier "
          "par `diff` contre le brouillon final inscrit au registre que seule cette ligne diffère, et que "
          "`controle_ia.prereg.problemes` est vide", 1))
R.append(("AP-4 c", "est un nœud de Lazar (règle du fournisseur, « Statut ») et suspend le lancement.",
          "est un nœud de Lazar (règle du fournisseur, « Statut ») et suspend le lancement. Il vérifie aussi que le texte "
          "scellé ne diffère du brouillon final inscrit au registre que par la ligne du commit cité, et, dans `git reflog` "
          "de la branche, qu'aucun « commit (amend) » ni « reset » ne touche le commit cité.", 1))
R.append(("AP-4 d", "aucune variante n'est scellée hors du dépôt ;",
          "aucune variante n'est scellée hors du dépôt ; liberté résiduelle, déclarée : l'empreinte scellée dépend encore "
          "des 40 caractères du commit cité (date comprise) ; la parade en est procédurale (commit unique, créé juste après "
          "la poussée du registre, vérifié par le lecteur de l'étape e) ;", 1))
R.append(("AP-4 e",
          "Deux marqueurs restent, remplis au scellement (étape 0.c) et rien d'autre : la ligne « Commit du code "
          "d'analyse » (40 caractères de `git rev-parse HEAD` après le commit de l'étape 0.a) ; l'entrée « Contre-lecture "
          "1 » ci-dessous (sous-agent neuf, brouillon relu et son empreinte, rapport et son empreinte, verdict, traitement "
          "de chaque remarque, essais après corrections).",
          "Un marqueur reste, rempli au scellement (étape 0.c) et rien d'autre : la ligne « Commit du code d'analyse » "
          "(40 caractères de `git rev-parse HEAD` après le commit de l'étape 0.a). L'entrée « Contre-lecture 1 » est "
          "remplie dans le brouillon final, avant l'inscription de son empreinte au registre (étape 0.0).", 1))
R.append(("AP-4 f (entrée « Contre-lecture 1 », gabarit du rapport rempli)",
          "- **Contre-lecture 1** (R2) : `À REMPLIR au scellement : sous-agent neuf (Claude), qui n'a écrit ni ce texte, "
          "ni le code, ni le texte du fournisseur, ni l'analyse secondaire ; brouillon relu et son empreinte ; rapport et son "
          "empreinte ; verdict ; traitement de chaque remarque (accepté, refusé et pourquoi) ; essais après corrections`.",
          "- **Contre-lecture 1** (R2) : sous-agent neuf (Claude, Opus 5.5), qui n'a écrit ni ce texte, ni le code, ni le "
          "texte du fournisseur, ni l'analyse secondaire, ni leurs contre-lectures ; brouillon relu : "
          "`brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/preenregistrement-analyse-principale-r1-r2-v1-"
          "brouillon2.md`, sha256 `fb1373931d0865715b6f3962c66f1384f62f266b500026acb4af87a658f8f41f` (commit `32179148`) ; "
          "rapport : `brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/contre-lecture-preenregistrement-analyse-"
          "principale-r1-r2-v1.md`, sha256 `eff5d4cacad00e7da4dd0d28df024516d976fa2b6e084bfbdede96352ab04606` (commit "
          "`346ce542`) ; verdict « scellable après corrections mineures (listées) », aucun écart de fond non déclaré au "
          "fournisseur ; traitement : AP-1 à AP-10 acceptées, appliquées mot pour mot par le script "
          "`appliquer-contre-lecture-1-v1.py` (sortie `appliquer-contre-lecture-1-v1-sortie.txt`), avec les seules "
          "adaptations décidées par conv-audit : AP-1, heures du brouillon 3 écrites ; AP-5, option (b) (texte seul, "
          "aucun code v3), plus la phrase « nœud de Lazar » si le lecteur de concordance juge la garde contraire à la "
          "règle `moyenne` du fournisseur ; AP-7 et AP-8, version scellée de l'analyse secondaire citée (" + SECONDAIRE +
          ") au lieu du brouillon 4, et omission de la lecture par épisode consignée par la session ; AP-6 sous sa forme "
          "texte (pas de code v3) ; suggestions non bloquantes non appliquées (voie B : exactement AP-1 à AP-10) ; "
          "**écart déclaré : pas de contre-lecture 2 ; textes AP écrits par le contre-lecteur, appliqués mot pour mot** ; "
          "essais après corrections : 24 réussis (code inchangé).", 1))

# AP-5 — garde « activation non finie », option (b) (SESSION : phrase « nœud de Lazar »)
R.append(("AP-5 (b) (SESSION : phrase « nœud de Lazar »)", "**activation non finie sur une action éligible**",
          "**activation non finie sur une action éligible** (les trois tableaux, diagnostics compris ; seule source connue "
          "possible : `maximum_hors_cout` d'une action dont tout l'empan est dans le champ COST, que le code du fournisseur "
          "laisse non fini ; cas jugé rare, non mesuré ; la garde lit `moyenne` comme contrôle d'intégrité, jamais comme "
          "score ; si le lecteur de concordance (étape 0.e) juge cette lecture contraire à la règle du fournisseur « tout "
          "emploi de `moyenne` hors du bras de diagnostic est un nœud » (l. 36-37), c'est un nœud de Lazar)", 1))

# AP-6 — plancher et ligne W − T
R.append(("AP-6", "« sous son plancher » : rappel ponctuel de W à 1 % ≤ plancher.",
          "« sous son plancher » : rappel ponctuel de W à 1 % ≤ plancher. La préséance du plancher vaut pour les lignes de "
          "P-R1 et de P-R2 contre J3s ; les lignes de W − T et de W − J8s gardent leur phrase, la réserve majeure « W non "
          "lisible comme sonde, quel que soit Δ » étant écrite dans la même issue : aucune citation de W − T ou W − J8s "
          "sans elle.", 1))

# AP-7 — tables de concordance (SESSION : version scellée de l'analyse secondaire)
R.append(("AP-7 a", "| 30 | Asymétrie d'accès ; R2 sans effet sur G1 et G0 | 41-44, 73-75 | portée en tête de l'issue |\n",
          "| 30 | Asymétrie d'accès ; R2 sans effet sur G1 et G0 | 41-44, 73-75 | portée en tête de l'issue |\n"
          "| 31 | « Activation non finie ou hors de l'étendue du float16 : arrêt » (arrêt du run chez le fournisseur) | 208 | "
          "étendu à l'analyse : valeur non finie sur une action éligible, trois tableaux (AP-5 de la contre-lecture 1) |\n"
          "| 32 | « une action en anomalie de masse garde son score renormalisé et son drapeau » | 168-169 | Métrique 3 ; "
          "part rapportée (Seuil) |\n", 1))
R.append(("AP-7 b", "sur **huit points** (décompte confirmé par conv-audit, R-1091) :",
          "sur **huit points de fond** (décompte de ce texte ; la ligne R-1091 du registre ne le donne pas) :", 1))
R.append(("AP-7 c", "contre le **maximum** à la couche 15",
          "contre le **maximum** à la couche 15 (régularisation λ = 10 contre C = 1, soit λ = 1)", 1))
R.append(("AP-7 d", "(8) 10 plis et cinq découpages contre 5 plis.",
          "(8) 10 plis et cinq découpages contre 5 plis ; s'y ajoutent des différences de détail : plancher (directions "
          "dans la covariance des activations moyennes contre directions gaussiennes normées sur entrées centrées "
          "réduites), nombre de tirages.", 1))
R.append(("AP-7 e (SESSION : brouillon 5 scellé au lieu du brouillon 4)", "L'analyse secondaire (brouillon 3 et code v3,",
          "L'analyse secondaire (version scellée, brouillon 5 : " + SECONDAIRE + ", et code v3 ; la concordance vaut pour "
          "cette version scellée, vérifiée à l'étape 0.e ;", 1))

# AP-8 — références à jour (SESSION : brouillon 5 scellé ; omission consignée par la session)
R.append(("AP-8 a (SESSION : brouillon 5 scellé au lieu du brouillon 4)",
          "analyse secondaire, brouillon 3 (`addadee095efccf1fadbbc0306bca131bb5bd07f216fec80988a48d0ea9222f3`).",
          "analyse secondaire, brouillon 3 (`addadee095efccf1fadbbc0306bca131bb5bd07f216fec80988a48d0ea9222f3`), lu par "
          "l'auteur ; sa version scellée (brouillon 5) : " + SECONDAIRE + " ; la concordance B vaut pour elle.", 1))
R.append(("AP-8 b (SESSION : omission consignée par la session)",
          "**Lecture par épisode (agrégateur séquentiel) en descriptif : omise** dans ce texte.",
          "**Lecture par épisode (agrégateur séquentiel) en descriptif : omise** dans ce texte ; R-1091 la permettait en "
          "descriptif « si cela ne coûte presque rien » : l'omission est la décision de conv-audit, consignée au registre "
          "(annoncée sous R-1098 ; raison retenue : ce ne serait pas « presque gratuit »).", 1))

# AP-9 — trois précisions
R.append(("AP-9 a", "« coût absent » = coût non lu ;",
          "« coût absent » = coût non lu ; l'effectif de calibrage de T est rapporté au « coût lu » (fini et ≥ 0), qui ne "
          "diffère du « coût lisible » de P3 et de C (> 0) que par les coûts nuls ;", 1))
R.append(("AP-9 b", "il ne change aucune ligne (la table gelée ne nomme que la mention).",
          "il ne change aucune ligne de lecture (la table gelée ne nomme que la mention) ; un changement de sa classe "
          "entre 1 % et 2 % déclenche la réserve « seuil fragile ».", 1))
R.append(("AP-9 c", "éligibles signalées au seuil de W ; « contraire » si part ≥ 0,5 × rappel(W).",
          "éligibles signalées au seuil de W ; « contraire » si part ≥ 0,5 × rappel(W). Cas limite, lu à la lettre : si "
          "rappel(W) = 0, toute part, nulle comprise, est « contraire ».", 1))

# AP-10
R.append(("AP-10", "Recopiée du texte du fournisseur (l. 51-75), sans changement.",
          "Reprise du texte du fournisseur (l. 51-75), sans changement de fond (sigles de ce texte ajoutés).", 1))


def main() -> int:
    for p, attendu in ((B2, SHA_B2), (RAPPORT, SHA_RAPPORT)):
        obtenu = sha(p)
        print(f"empreinte {p.name} : {obtenu} {'OK' if obtenu == attendu else 'DIFFÉRENTE'}")
        if obtenu != attendu:
            return 1
    if B3.exists():
        print(f"{B3} existe déjà (R12) : arrêt")
        return 1
    s = B2.read_text(encoding="utf-8")
    for ident, ancien, nouveau, n in R:
        k = s.count(ancien)
        print(f"{ident} : {k} occurrence(s) de l'ancien texte, {n} attendue(s) — {'OK' if k == n else 'ÉCHEC'}")
        if k != n:
            return 1
        s = s.replace(ancien, nouveau)
    s = s.replace("— v1 — brouillon 2", "— v1 — brouillon 3", 1)
    print("titre : « brouillon 2 » → « brouillon 3 »")
    B3.write_text(s, encoding="utf-8")
    print(f"écrit : {B3} ; sha256 {sha(B3)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
