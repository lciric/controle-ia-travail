P = [
("""# clonage (VC2-depense-03), repli de l'affichage (VC2-donnees-01).
# Usage : essais_verifications_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE""",
"""# clonage (VC2-depense-03), repli de l'affichage (VC2-donnees-01).
# Chaîne v4 (traitement de la vérification « fidélité » de la chaîne v2) : vingt-sept rapports (VC2-fidelite-01) ;
# types « décision », « règle », « lecture complémentaire » (R-281) inconnus : une telle ligne qui nomme l'un des cinq
# identifiants arrête en code 2 (X09 à X11, G10e2), témoins X12 (type « décision » sans identifiant) et G10e (mention
# libre dans un GO de calcul) ; registres réels relus à la tête de origin/main (VC2-fidelite-06) ; journal de la
# répétition : sixième passage (délai externe), récupération du sixième passage au motif TERM, heure limite relue, en
# repli déclaré et dépassée, état et heure limite dans le refus des traces, repli des textes absents (J34 à J42).
# Usage : essais_verifications_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE"""),
("""cas_go G10e-ligne-qui-mentionne-une-revocation 0 "$GO conforme" cat \\
    "$(ajout_go "| GO-2026-10-20-97 | $JOUR | décision | essai : aucune révocation de $GO ni de R-269 | — | $JOUR | Lazar | essai |")" cat""",
"""# chaîne v4 (VC2-fidelite-06) : la mention libre reste sans effet dans un GO d'un type de l'en-tête (G10e) ; dans un GO de
# type « décision » (R-281, hors de l'en-tête), elle arrête (G10e2, forme voisine : type inconnu qui nomme un identifiant)
cas_go G10e-ligne-qui-mentionne-une-revocation 0 "$GO conforme" cat \\
    "$(ajout_go "| GO-2026-10-20-97 | $JOUR | calcul | essai : aucune révocation de $GO ni de R-269 | 1 USD | $JOUR | Lazar | essai |")" cat
cas_go G10e2-ligne-de-type-decision-qui-mentionne-un-identifiant 2 "révocation possible sous une forme voisine" cat \\
    "$(ajout_go "| GO-2026-10-20-97 | $JOUR | décision | essai : aucune révocation de $GO ni de R-269 | — | $JOUR | Lazar | essai |")" cat"""),
("""# registres réels du dépôt de travail, à la tête de main (git show, lecture seule ; chaîne v3 : relus après la correction
# de VC2-depense-01) : aucune fausse alerte, accord fabriqué ajouté ; puis l'arbre de travail, s'il en diffère
DT=/home/user/controle-ia-travail
GIT_OPTIONAL_LOCKS=0 git -C "$DT" --no-optional-locks show main:registres/go.md > "$R/go-reel.md" \\
    && GIT_OPTIONAL_LOCKS=0 git -C "$DT" --no-optional-locks show main:registres/decisions.md > "$R/decisions-reel.md" || exit 2
echo "registres réels lus à la tête de main ($(GIT_OPTIONAL_LOCKS=0 git -C "$DT" --no-optional-locks rev-parse main)) : go.md""",
"""# chaîne v4 (VC2-fidelite-06) : types écrits par R-281 hors de l'en-tête, qui nomment l'un des cinq identifiants sans
# forme de révocation (X09 à X11 : code 2, lignes affichées) ; témoin X12 : type « décision » sans aucun des cinq
cas_go X09-go-de-type-decision-qui-dit-lazar-revoque 2 "révocation possible sous une forme voisine" cat \\
    "$(ajout_go "| GO-2026-10-21-01 | $JOUR | décision | Lazar révoque R-269 (essai) | — | $JOUR | Lazar | essai |")" cat
grep -q "^    registres/go.md, ligne [0-9]* : | GO-2026-10-21-01 | $JOUR | décision | Lazar révoque R-269" "$R/sortie-X09-go-de-type-decision-qui-dit-lazar-revoque.txt" \\
    && echo "    X09 : ligne de la forme voisine affichée : CONFORME" || { echo "    X09 : ligne de la forme voisine non affichée : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
cas_go X10-go-de-type-regle-qui-nomme-le-go-cite 2 "révocation possible sous une forme voisine" cat \\
    "$(ajout_go "| GO-2026-10-21-01 | $JOUR | règle | GO-2026-10-20-07 suspendu (essai) | — | $JOUR | Lazar | essai |")" cat
cas_go X11-go-de-type-lecture-complementaire-qui-nomme-la-phase 2 "révocation possible sous une forme voisine" cat \\
    "$(ajout_go "| GO-2026-10-21-01 | $JOUR | lecture complémentaire | fin de GO-2026-10-04-08 (essai) | — | $JOUR | Lazar | essai |")" cat
cas_go X12-go-de-type-decision-sans-identifiant 0 "$GO conforme" cat \\
    "$(ajout_go "| GO-2026-10-21-01 | $JOUR | décision | nœud tranché par Lazar, sans lien avec P4 (essai) | — | $JOUR | Lazar | essai |")" cat
# registres réels du dépôt de travail, à la tête de origin/main (git show, lecture seule ; chaîne v3 : relus après la
# correction de VC2-depense-01 ; chaîne v4 : après celle de VC2-fidelite-06, GO-2026-10-20-12 à -14 étant de type
# « décision ») : aucune fausse alerte, accord fabriqué ajouté ; puis l'arbre de travail, s'il en diffère
DT=/home/user/controle-ia-travail
GIT_OPTIONAL_LOCKS=0 git -C "$DT" --no-optional-locks show origin/main:registres/go.md > "$R/go-reel.md" \\
    && GIT_OPTIONAL_LOCKS=0 git -C "$DT" --no-optional-locks show origin/main:registres/decisions.md > "$R/decisions-reel.md" || exit 2
echo "registres réels lus à la tête de origin/main ($(GIT_OPTIONAL_LOCKS=0 git -C "$DT" --no-optional-locks rev-parse origin/main)) : go.md"""),
("""[ "$(grep -c '^rapport attendu : ' "$R/sortie-K00-noms-exacts.txt")" = 26 ] && echo "    K00 : vingt-six rapports attendus (RAPPORTS_NOMS de la chaîne v3) : CONFORME" \\""",
"""[ "$(grep -c '^rapport attendu : ' "$R/sortie-K00-noms-exacts.txt")" = 27 ] && echo "    K00 : vingt-sept rapports attendus (RAPPORTS_NOMS de la chaîne v4) : CONFORME" \\"""),
("""module_rep J33-refus-de-trop 1 "récupérations refusées en code 2 attendues" "sed '\\$a récupération (autre) : code 2 ; essai'\"""",
"""module_rep J33-refus-de-trop 1 "récupérations refusées en code 2 attendues" "sed '\\$a récupération (autre) : code 2 ; essai'"
# chaîne v4 : sixième passage (VC2-fidelite-07) ; heure limite (VC2-fidelite-03) ; refus des traces (VC2-fidelite-04) ;
# repli des textes absents (VC2-fidelite-08)
module_rep J34-passage-6-absent 1 "passage : passage 6-delai-externe : code 1" "sed '/^passage 6-delai-externe : /d'"
module_rep J35-passage-6-sans-term 1 "« signal TERM reçu (délai externe du run » absent de son journal" "sed '/^    | .*signal TERM reçu (délai externe du run/d'"
module_rep J36-recuperation-6-sans-motif-term 1 "récupération (passage-6-delai-externe)" "sed '/^    --  4a arrêt : /s/signal TERM/autre signal/'"
module_rep J37-etat-absent-du-refus-des-traces 1 "état de l'instance gardée et heure limite de destruction absents du refus" "awk '/^récupération \\\\(artefact-traces-d-un-autre-lancement\\\\)/{print; getline; next} {print}'"
module_rep J38-repli-des-textes-absents-absent 1 "ligne absente ou en double : récupération en repli de l'affichage (artefact-textes-absents)" "sed '/^récupération en repli de l.affichage (artefact-textes-absents)/d'"
module_rep J39-limite-depassee-absente 1 "récupération (limite-depassee)" "sed '/^    --  8 heure limite dépassée de /d'"
module_rep J40-limite-relue-dans-arret-absente 1 "récupération (passage-1-sain)" "sed '/(arrêt relu à /d'"
module_rep J41-repli-declare-absent 1 "récupération (passage-3-traces-seules)" "sed '/(repli déclaré : arret.txt absent ; /d'"
module_rep J42-passage-6-autre-code 1 "passage : passage 6-delai-externe : code 1" "sed 's/^passage 6-delai-externe : code 1 /passage 6-delai-externe : code 124 /'\""""),
]
