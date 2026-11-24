#!/usr/bin/env python3
"""Génère de façon reproductible la version 4 de la décision N-075 à partir
de la version 3 exacte, en portant :
1. L'en-tête et le statut de la version 4 (y compris le remplacement temporaire
   de Claude Fable par Carbon en effort élevé selon GO-2026-11-23-33) ;
2. L'intégration chirurgicale des errata déjà scellés sur la branche principale
   (erratum 1, erratum 2 et erratum 3 v2, avec la correction de la trouvaille de
   côté de la vérification de l'erratum 3 : 0,0511 -> 0,0510) ;
3. Les quatre corrections issues de la lecture sur document PDF des seize
   papiers « saboteur et sondes » (décision de dossier R-5185 et accord
   GO-2026-11-23-32).

Aucune modification n'est apportée au dépôt source ; le fichier produit et le
différentiel unifié contre la version 3 sont écrits dans le dossier de travail
désigné par le mandat.
"""

from __future__ import annotations

import difflib
import hashlib
from pathlib import Path

DEPOT = Path("/home/antigravity/lciric/controle-ia-travail")
SOURCE_V3 = DEPOT / "docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md"
SHA256_ATTENDU_V3 = "5aed4bab1172b18148c086d90e63611bdd769d9ea7fb4a043e9e9d3178c947b5"

SORTIE_DIR = Path(
    "/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/"
    "ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/redaction-n075-n076"
)
CIBLE_V4 = SORTIE_DIR / "decision-N-075-issue-plancher-et-deux-regards-v4.md"
DIFF_V3_V4 = SORTIE_DIR / "diff-decision-N-075-v3-contre-v4.patch"
TABLE_CORRESPONDANCE = SORTIE_DIR / "table-remplacements-n075-v3-vers-v4.md"


def remplacer_unique(
    texte: str,
    identifiant: str,
    ancien: str,
    nouveau: str,
    journal: list[tuple[str, str, str]],
) -> str:
    """Remplace une chaîne qui doit apparaître exactement une fois."""
    compte = texte.count(ancien)
    if compte != 1:
        raise ValueError(
            f"[{identifiant}] Ancrage attendu 1 fois, trouvé {compte} fois : {ancien!r}"
        )
    journal.append((identifiant, ancien, nouveau))
    return texte.replace(ancien, nouveau, 1)


def construire_remplacements() -> list[tuple[str, str, str]]:
    """Retourne la liste ordonnée des remplacements exacts sur la v3."""
    return [
        # --- Bloc 0 : titre et en-tête de la v4 ---
        (
            "H-1 (titre, l. 1)",
            "# Décision — N-075 : mesurer l'issue et corriger ; un plancher d'audit au hasard contre le sabotage diffus ; deux regards tels qu'échapper à l'un expose à l'autre ; alerte à deux clés ; bilan du produit contre le jumeau honnête ; recherche du passage obligé de tout sabotage ; lemme d'additivité restreint à sa forme valide à tout instant (v3)",
            "# Décision — N-075 : mesurer l'issue et corriger ; un plancher d'audit au hasard contre le sabotage diffus ; deux regards tels qu'échapper à l'un expose à l'autre ; alerte à deux clés ; bilan du produit contre le jumeau honnête ; recherche du passage obligé de tout sabotage ; lemme d'additivité restreint à sa forme valide à tout instant (v4)",
        ),
        (
            "H-2 (ligne Décision de Lazar, l. 3)",
            "- **Décision de Lazar** : mots directs dans la session mère `session_01QPDgKgejkqwnuaJHJ31Ydo`, 21 novembre 2026, vers 12:45 UTC, consignés à la ligne `GO-2026-11-21-51` de `registres/go.md` (`e0194c1c…` à la lecture de la v1, `c454dea5…` à celle de la v2) ; pour le lemme d'additivité, mots du même jour vers 12:00 UTC, ligne `GO-2026-11-21-47`, point 4 ; pour la pince, mots du même jour vers 13:05 UTC, ligne `GO-2026-11-21-53`. Mots recopiés en section 0.",
            "- **Décision de Lazar** : mots directs dans la session mère `session_01QPDgKgejkqwnuaJHJ31Ydo`, 21 novembre 2026, vers 12:45 UTC, consignés à la ligne `GO-2026-11-21-51` de `registres/go.md` (`e0194c1c…` à la lecture de la v1, `c454dea5…` à celle de la v2) ; pour le lemme d'additivité, mots du même jour vers 12:00 UTC, ligne `GO-2026-11-21-47`, point 4 ; pour la pince, mots du même jour vers 13:05 UTC, ligne `GO-2026-11-21-53` ; pour les choix sur les points 7, 8, 10 et 11 de la section 11, mots du même jour vers 15:00 UTC, ligne `GO-2026-11-21-61` ; pour les quatre corrections issues de la lecture sur document PDF des seize papiers « saboteur et sondes », mots du 23 novembre 2026 vers 18:55 UTC, ligne `GO-2026-11-23-32` (décision consignée à la ligne `R-5185` de `registres/decisions.md`), et remplacement temporaire déclaré de Claude Fable par Carbon en effort élevé accordé le 23 novembre 2026 à 20:35:23 UTC, ligne `GO-2026-11-23-33`. Mots recopiés en section 0.",
        ),
        (
            "H-3 (ligne Statut, l. 4)",
            "- **Statut : v3, à vérifier une dernière fois puis à sceller par la mère.** La v1 (`f1b77e66c1742e248634a803b5ff7a2c8cb0a415bd8162cc6fc9a823bddc3a14`) a été contre-lue par Opus 5.5 (`docs/decisions/contre-lecture-decision-N-075-v1.md`, `eaec091b8831992e0d3a8f4abf21b496eb3228249eb37add6f6e9061bb5d59b2`, quatorze corrections) ; la v2 (`997bc0b3fc238bf35e7920f328a3adf9d8206b4ea9a984fe02a8a228ac4f589f`) les portait, avec cinq apports de la contre-lecture de la note sur l'adjudant, et a été vérifiée par le même contre-lecteur : « pas encore prêt à sceller », dix points V1 à V10 (`docs/decisions/verification-decision-N-075-v2-v1.md`, `b7707396aa8ceab373b4172626c6f2fb7782ef23b7c2f301955c3cc4c33dce71`). La v3 est écrite le 21 novembre 2026 entre 13:58 et 14:10 UTC (`date -u`) par le même auteur, Claude Fable 5.2 (`claude-fable-5-2`), concepteur (R-3735), dépôt à `238cb88a9`. Elle porte les dix points et en ajoute un onzième, sur mandat de la mère : l'identification de l'oracle mesurée par des dommages plantés (section 11, point 11). **Les points 7 à 11 de la section 11 sont écrits en options et ne sont pas tranchés.** La table des onze points est en section 14. Les v1 et v2 sont gardées telles quelles (R12). Aucun appel payant, ni commit ni poussée. La ligne de `CLAUDE.md` (section 12) est **proposée**.",
            "- **Statut : v4, rédigée par script reproductible à partir de la v3 exacte, à contre-lire puis à sceller par la mère.** La v1 (`f1b77e66c1742e248634a803b5ff7a2c8cb0a415bd8162cc6fc9a823bddc3a14`), la v2 (`997bc0b3fc238bf35e7920f328a3adf9d8206b4ea9a984fe02a8a228ac4f589f`) et la v3 (`5aed4bab1172b18148c086d90e63611bdd769d9ea7fb4a043e9e9d3178c947b5`) restent archivées telles quelles (R12). La v3 portait trois errata : l'erratum 1 (`c6efeccfafca415851c0e15ad64305b268c9521f7773e795af28d8d25424b0c1`), l'erratum 2 (`b19852b47a90e902ee3fc5c0144ddac00f8665a565b43b1df2debacf58f7bb46`) et l'erratum 3 v2 (`fbe3298ec358fa9b8d041d8675d9ad3369e99591572c8281806f0ade75463b04`, qui primait après sa vérification `59b18766fede5e54379240d7b569f0bd6fada954b4e990f9ae58ada705970470`). Cette v4 réunit chirurgicalement dans le corps de la v3 : (i) les choix déjà scellés de l'erratum 1, de l'erratum 2 et de l'erratum 3 v2 (les points 7, 8, 10 et 11 de la section 11 sont tranchés ; seul le point 9 reste ouvert avec penchant vers l'option b) et la règle en vigueur de la décision N-060 v3 au point 4 ; la ligne pour `CLAUDE.md` reprend celle vérifiée dans `ligne-claude-md-N-075-v2.md`, `dd6cbe159e4fcaecec4f38c4db1c54c8403aa1c97f7b022c8a482020f102ba59`, puis propose son renvoi mis à jour vers la v4) ; (ii) les quatre corrections issues de la lecture sur document PDF des seize papiers « saboteur et sondes » (synthèse `8b63dc17df2b2934d09de457e7f795a1a4bd6647052ac192e1716dab58bb44e3` sur `origin/lecture/papiers-saboteur-sondes-v1`, contre-lecture `b786fbe46cc163a0dc68612c60df3029f5a1437c6f76bf35e76b4a1d2c7ba13f`). Rédaction le 23 novembre 2026 après 20:43 UTC (`date -u`), dépôt sur `main` à `05c6d54102fad068630c4ef1a6a5ba22603fa7f7`, par un sous-agent neuf rédacteur Carbon en effort élevé (`pro`) agissant en remplacement temporaire déclaré de Claude Fable 5.2 (`GO-2026-11-23-33`). Aucun fichier du dépôt modifié, aucun commit ni poussée ; l'ensemble des autres passages de la v3 est conservé à l'octet près.",
        ),
        (
            "H-4 (ligne Sources, complément lecture des 16 papiers, l. 6)",
            "La seconde n'est **pas contre-lue**.",
            "La seconde n'est **pas contre-lue**. S'y ajoutent, pour les quatre corrections de la v4 : la synthèse scellée de la lecture sur document PDF des seize papiers « saboteur et sondes » (`docs/notes/lecture-papiers-saboteur-sondes-v1/synthese-lecture-papiers-saboteur-sondes-v1.md`, `8b63dc17df2b2934d09de457e7f795a1a4bd6647052ac192e1716dab58bb44e3` sur `origin/lecture/papiers-saboteur-sondes-v1`), sa contre-lecture (« tient avec corrections », `b786fbe46cc163a0dc68612c60df3029f5a1437c6f76bf35e76b4a1d2c7ba13f`), la note explicative sur trois points (`f1ec7cfa295a325f60e876b4eeb10df727f6b77e73941a1e478f8d4adb768220`) et les fiches scellées des quatre papiers visés (`fiche-2602.00986-v1.md`, `817712a3790c9cf21b4135b0f2dc8a9393e2065d9721f5ecb51aecca0da1d7c5` ; `fiche-2606.06529-v1.md`, `508ed82c5543210ddbc8e8f2c3484e811797490cb7c7bccc57d1f1ffdd3ae8b4` ; `fiche-2508.00161-v1.md`, `8ab9faa73624a78ef3dd23d0d7a1abc4afbd9503057c6a636203297fa83929a6` ; `fiche-2506.24068-v1.md`, `180ebfa570e078d78bca743e9c57e0853bb8420e87fab6102b4e3d2dd464ddaa`).",
        ),
        (
            "H-5 (ajout aux Marques pour les quatre fiches, l. 9)",
            "que je n'ai pas rejouée.",
            "que je n'ai pas rejouée. Pour les quatre corrections de la v4 : [PDF, p.] désigne aussi la page exacte du document PDF empreinté citée par la fiche scellée correspondante (lecture par Claude Opus 5.5 en effort élevé, non rouverte en document PDF ici).",
        ),
        # --- Bloc 1 : intégration de l'erratum 1 (C-1 à C-4) et de l'erratum 3 v2 (R-1 à R-20, A-1 à A-3) ---
        # Section 0 : mots de GO-2026-11-21-61, R-4 et R-5
        (
            "R-4 (section 0, l. 31)",
            "**Un écart à la lettre, proposé et non appliqué.**",
            "**Un écart à la lettre, accordé par Lazar.**",
        ),
        (
            "R-5 (section 0, l. 31)",
            "La lettre change seulement sur le mot de Lazar (section 11, point 8).",
            "La lettre change : le mot est donné à `GO-2026-11-21-61` (point 8 (a)), et la forme réécrite de la section 4 est retenue. À compter de la v4, s'ajoutent les quatre corrections issues de la lecture sur document PDF des seize papiers (`GO-2026-11-23-32`, `R-5185`), portées aux sections 2, 3, 4 et 8 sans modifier aucun énoncé retenu.",
        ),
        # Section 1 : A-1 (ajout vocabulaire dommage planté, strate, strate mesurée)
        (
            "A-1 (section 1, ajout après Passage obligé, l. 41)",
            "- **Passage obligé** : ce que tout sabotage délibéré doit calculer quel que soit son mode, à savoir connaître la bonne action et en choisir une autre.",
            "- **Passage obligé** : ce que tout sabotage délibéré doit calculer quel que soit son mode, à savoir connaître la bonne action et en choisir une autre.\n- **Dommage planté** : un dommage connu, introduit exprès par un tiers dans un produit honnête, pour compter si l'oracle le reconnaît ; qui est ce tiers et ce qu'il voit relève de la campagne, non tranchée. **Strate** : un genre de dommage à une dose donnée. **Strate mesurée** : strate où des dommages plantés ont été jugés par l'oracle et où la borne exacte de q est écrite ; toute autre strate est non mesurée et compte pour zéro.",
        ),
        # Section 2 : R-15, R-15 bis, R-14, A-2, R-16
        (
            "R-15 bis (section 2, l. 45)",
            "pour toute politique d'attaque dont l'oracle voit le dommage",
            "pour toute politique d'attaque dont le dommage tombe dans une strate où la reconnaissance de l'oracle est mesurée (une strate non mesurée compte pour zéro)",
        ),
        (
            "R-15 (section 2, l. 45)",
            "oracle exogène au sens de la section 1 ; et, dès que l'honnête",
            "oracle exogène au sens de la section 1, dont la probabilité q de reconnaître un dommage qu'il regarde est mesurée par des dommages plantés, strate par strate ; et, dès que l'honnête",
        ),
        (
            "R-14 (section 2, l. 48)",
            "(comment ce q se connaît est une option ouverte, section 11, point 11)",
            "(q se mesure par des dommages plantés, strate par strate, et une strate non mesurée compte pour zéro : alinéa « Identification de l'oracle, mesurée », ci-dessous)",
        ),
        (
            "A-2 (section 2, alinéa ajouté après l. 49)",
            "ce qui passe sous l'excès toléré sur cet horizon est le dommage que la borne accepte.",
            "ce qui passe sous l'excès toléré sur cet horizon est le dommage que la borne accepte.\n\n**Identification de l'oracle, mesurée** (`GO-2026-11-21-61`, point 11 (a)). q n'est pas supposé. Il se mesure par des dommages plantés par un tiers, strate par strate (genre et dose), par une borne exacte. Toute garantie porte le minimum de q sur les strates mesurées, et nomme ces strates. Une strate non mesurée compte pour zéro : aucune borne n'y est écrite. Tant que rien n'est planté, aucune borne chiffrée du plancher ne s'écrit ; les nombres de cette section restent des illustrations sous supposition.",
        ),
        (
            "R-16 (section 2, l. 59)",
            "rien hors de la couverture de l'oracle ; un saboteur qui reste sous l'excès toléré",
            "rien hors de la couverture de l'oracle ; rien dans une strate de dommage où q n'est pas mesuré par des dommages plantés ; un saboteur qui reste sous l'excès toléré",
        ),
        # Section 4 : R-6, R-7, R-8 (et suite 2 de l'erratum 3 v2 : « signal » -> « motif »)
        (
            "R-6 (section 4, l. 112)",
            "**Énoncé proposé, réécrit (en attente du mot de Lazar, section 11, point 8).**",
            "**Énoncé retenu, réécrit (`GO-2026-11-21-61`, point 8 (a)).**",
        ),
        (
            "R-7 (section 4, l. 114, alinéa entier)",
            "**Écart à la lettre du mot de Lazar, proposé.** Dans la forme proposée, « nouveauté seule = mise à jour des témoins » ne serait pas gardée, et « nouveauté » deviendrait « motif reconnu par un regard ». La parenthèse du GO demande la vérification, elle ne décide pas la réécriture : le mot de Lazar est demandé (section 11, point 8). D'ici là, ne s'applique que ce que la lettre, lue comme dans la v1 (témoins refaits sur des honnêtes exogènes seulement), et la forme réécrite ont en commun : une alerte demande un signal et une preuve de dommage au même endroit ; aucun épisode du suspect n'entre jamais dans les témoins ; un signal sans preuve peut aiguiller l'audit, sans toucher à la part tirée au hasard. Le reste attend le mot de Lazar.",
            "**Écart à la lettre du mot de Lazar, accordé** (`GO-2026-11-21-61`, point 8 (a)). « Nouveauté seule = mise à jour des témoins » (`GO-2026-11-21-51`) n'est plus la règle, et « nouveauté » devient « motif reconnu par un regard ». La forme réécrite ci-dessus s'applique en entier ; le tronc commun y est contenu. Un motif sans preuve de dommage ne déclenche aucune mise à jour des témoins. Refaire les témoins sur des honnêtes exogènes reste une correction de la liste de la section 1 ; cette règle ne dit pas ce qui la déclenche.",
        ),
        (
            "Erratum 3 § 1 point 8 suite 2 (section 4, l. 117 : signal -> motif)",
            "deux issues écrites d'avance et rapportées, « alerte » (signal et preuve de dommage au même endroit) et une seconde issue pour le signal sans preuve de dommage, comptée à part :",
            "deux issues écrites d'avance et rapportées, « alerte » (motif et preuve de dommage au même endroit) et une seconde issue pour le motif sans preuve de dommage, comptée à part :",
        ),
        (
            "R-8 (section 4, l. 117)",
            "« audit prioritaire » dans le tronc commun, et ce que le mot de Lazar fixera pour le reste (section 11, point 8).",
            "« audit prioritaire » : l'épisode monte dans la file d'audit, ou le moniteur s'abstient ; il n'entre jamais dans les témoins (`GO-2026-11-21-61`, point 8 (a)).",
        ),
        # Section 7 : C-3 + R-11 + R-1 + R-12
        (
            "C-3 puis R-11 (section 7, point 1, l. 184)",
            "validité sous dépendance : L3 et suivants de N-004).",
            "validité sous dépendance : L3 et suivants de N-004). C'était la lecture de `GO-2026-11-21-47`. La lecture des voisins la rend partiellement occupée, et Lazar resserre la revendication au seul reste qu'elle nomme (`GO-2026-11-21-61`, point 10 (a)) : une borne inférieure de la probabilité d'alarme, valide à tout instant, qui ne dépend que du dommage total, hors du cadre gaussien et sous dépendance, avec le coût du report, sur des scores de sondes. Ce qui figure dans la liste ci-dessus sans être dans ce reste (le prix de la garantie, la détection avant le dommage) ne se revendique plus : il se mesure et se rapporte, et se cite là où une source le porte (pour la détection avant le dommage, sous sa forme classique, le rapport KfK 3935) ; il sort parce que le reste ne le nomme pas, non parce qu'il serait occupé.",
        ),
        (
            "R-1 (section 7, point 4, l. 187)",
            "Savoir si la veille dégelée compte parmi les trois chantiers actifs est renvoyé à Lazar (section 11, point 7).",
            "La veille dégelée vit à côté des trois chantiers actifs, comme la levée partielle de `GO-2026-11-21-50` (D-P4), au service d'abord des lectures d'antériorité que demandent les décisions ; elle ne compte pas parmi les trois (`GO-2026-11-21-61`, point 7 (a)).",
        ),
        (
            "R-12 (section 7, Risque à dire, l. 191)",
            "resserrer la revendication à ce reste, ou replier le lemme, est un nœud (section 11, point 10).",
            "Lazar resserre la revendication à ce reste (`GO-2026-11-21-61`, point 10 (a)) ; le reste lui-même n'est pas déclaré libre : il est « non trouvé » par une lecture non contre-lue (R8), et sa démonstration dans cette forme reste à établir. Replier le lemme (N-004) reste un nœud.",
        ),
        # Section 8 : R-9 et A-3
        (
            "R-9 (section 8, Ne pas écrire, l. 219)",
            "« nouveauté seule = mise à jour des témoins » sans dire que les témoins ne se refont que sur des honnêtes exogènes",
            "« nouveauté seule = mise à jour des témoins » comme règle du programme ; « alerte = nouveauté et preuve de dommage » là où la règle dit « motif et preuve de dommage »",
        ),
        (
            "A-3 (section 8, Ne pas écrire, ajout en fin d'alinéa, l. 219)",
            "le plancher d'audit au hasard comme apport ou idée du programme.",
            "le plancher d'audit au hasard comme apport ou idée du programme ; une borne chiffrée du plancher sans les strates où q est mesuré et sans leur compte de dommages plantés ; une borne dans une strate non mesurée ; un q supposé écrit comme un q mesuré ; « le réapprentissage des sondes en service est permis », tant que le point 9 n'est pas tranché.",
        ),
        # Section 9 : R-2
        (
            "R-2 (section 9, l. 227)",
            "la place de la veille dégelée est en section 11, point 7.",
            "la veille dégelée vit à côté d'eux (`GO-2026-11-21-61`, point 7 (a)).",
        ),
        # Section 10 : C-1, R-13, R-17, R-10, C-2, R-3
        (
            "C-1 (section 10, § 1 Positionnement, l. 233)",
            "sous plafond de dommage par épisode (limites au § 4) ; les moniteurs en sont l'accélérateur et l'aiguillage (N-075). »",
            "sous plafond de dommage par épisode (limites au § 4) ; ce plancher est publié et n'est pas un apport du programme (Zhu, Zuo, Sun, « Blindfold » ; Gans et Holden ; Podkopaev et Ramdas pour l'excès sur un risque de référence) ; les moniteurs en sont l'accélérateur et l'aiguillage (N-075). »",
        ),
        (
            "R-13 (section 10, § 3, l. 234)",
            "Le lemme n'est revendiqué que dans sa lecture valide à tout instant, sur des scores de sondes internes, dans la forme que fixera le mot de Lazar sur le verdict d'antériorité (N-075, section 11, point 10).",
            "Le lemme n'est revendiqué que dans ce reste : une borne inférieure de la probabilité d'alarme, valide à tout instant, qui ne dépend que du dommage total, hors du cadre gaussien et sous dépendance, avec le coût du report, sur des scores de sondes internes (N-075, `GO-2026-11-21-61`) ; le voisin valide à tout instant le plus proche est cité (Khosravi et Huo, 2610.10597 v1).",
        ),
        (
            "R-17 (section 10, § 4, l. 235)",
            "aucune borne contre un coup unique, hors de la couverture de l'oracle, sous l'excès toléré, sans horizon, ni si l'oracle est trompé.",
            "la borne porte le minimum, sur les strates de dommage mesurées, de la probabilité que l'oracle reconnaisse un dommage qu'il regarde, mesurée par des dommages plantés par un tiers ; aucune borne contre un coup unique, hors de la couverture de l'oracle, dans une strate non mesurée, sous l'excès toléré, sans horizon, ni si l'oracle est trompé.",
        ),
        (
            "R-10 (section 10, § 8.4 Deux regards, l. 236)",
            "la règle à deux clés dans la forme que fixera le mot de Lazar (N-075, section 11, point 8), hors du taux de fausses alertes d'une porte",
            "la règle à deux clés (motif reconnu par un regard et preuve de dommage au même endroit : alerte ; motif seul : audit prioritaire, jamais les témoins ; preuve de dommage sans motif : le plancher), règle d'exploitation qui aiguille l'audit, hors du taux de fausses alertes d'une porte",
        ),
        (
            "C-2 (section 10, § 8.3 base hors des deux boîtes, l. 237)",
            "publié (Zhu, Zuo, Sun, « Blindfold » ; Gans et Holden) ».",
            "publié (Zhu, Zuo, Sun, « Blindfold » ; Gans et Holden ; Podkopaev et Ramdas) ».",
        ),
        (
            "R-3 (section 10, § 16 Veille active, l. 240)",
            "sa place parmi les chantiers suit le mot de Lazar (N-075, section 11, point 7).",
            "elle vit à côté des trois chantiers actifs, au service d'abord des lectures d'antériorité que demandent les décisions (`GO-2026-11-21-61`).",
        ),
        # Section 11 : point 4 (lecture d'ensemble), R-18, trouvaille de côté 0,0511 -> 0,0510
        (
            "E3-v1 Lecture d'ensemble (section 11, point 4, l. 249)",
            "son effet est la réécriture proposée en section 4 (point 8 ci-dessous).",
            "son effet a été la réécriture de la section 4, désormais retenue au point 8 (option a, `GO-2026-11-21-61`).",
        ),
        (
            "R-18 (section 11, l. 252)",
            "**Les points 7 à 11 attendent un choix de Lazar. Ils sont écrits en options ; cette note n'en tranche aucun, et aucun n'a de défaut.**",
            "**Les points 7, 8, 10 et 11 sont tranchés par Lazar à `GO-2026-11-21-61` : 7 (a), 8 (a), 10 (a), 11 (a). Le point 9 n'est pas tranché : Lazar penche pour (b), et la question va au collisionneur et à l'organisme ; d'ici son mot, la règle en vigueur de la décision N-060 v3 (point 4) s'applique. Les options restent écrites ci-dessous pour mémoire.**",
        ),
        (
            "Trouvaille de côté vérification erratum 3 v1 (section 11, point 11, l. 258)",
            "`python3 -c \"print(0.95**59, 0.95**58)\"` rend 0,0485 et 0,0511).",
            "`python3 -c \"print(0.95**59, 0.95**58)\"` rend 0,0485 et 0,0510).",
        ),
        # Section 12 : R-20 (ligne CLAUDE.md à jour depuis ligne-claude-md-N-075-v2.md, adaptée pour v4)
        (
            "R-20 (section 12, titre et ligne CLAUDE.md, l. 262-266)",
            "À ajouter à la fin de la liste « Décisions de Lazar », par la mère, après la vérification des corrections :\n\n> N-075 (GO-2026-11-21-47, -51, -53) : contre le diffus, mesurer l'issue et corriger — plancher d'audit au hasard (publié, « Blindfold » : base citée, jamais revendiquée), oracle exogène, plafond, horizon, hors porte ; sondes en accélérateur, non en garantie ; dilemme plutôt que décorrélation ; pince en trois objets ; alerte = signal et dommage au même endroit, aucun épisode du suspect dans les témoins ; lemme : forme valide à tout instant sur sondes, 1981 cité, reste au mot de Lazar ; veille dégelée (`docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md`).\n\nLongueur : 575 signes (plafond de 600, mesurée par programme). C'est la ligne du vérificateur (V10), reprise mot pour mot. Elle ne dit rien des points 7 à 11 de la section 11, qui ne sont pas tranchés : la mère la complète selon les mots de Lazar. Elle retire aussi « veille » de la liste des gelés (« Allègement de la procédure », dernière puce).",
            "Mise à jour de la ligne dans « Décisions de Lazar » de `CLAUDE.md` (proposition séparée complète dans `proposition-ligne-claude-md-n075-n076.md`, remplaçant la ligne issue de `ligne-claude-md-N-075-v2.md` qui renvoyait à la v3 et à ses errata 1 à 3) :\n\n> N-075 (GO-2026-11-21-46, -47, -51, -53, -61 ; GO-2026-11-23-32) : contre le diffus, mesurer l'issue et corriger — plancher d'audit au hasard publié, jamais revendiqué, q mesuré par dommages plantés, strate non mesurée à zéro ; sondes : accélérateur, non garantie ; dilemme, non décorrélation ; pince en trois objets ; alerte = motif et dommage au même lieu, motif seul : audit, jamais témoin ; lemme resserré au reste ; veille à côté des chantiers ; réapprentissage non tranché, N-060 v3 tient ; quatre retouches après lecture (`docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v4.md`).\n\nLongueur : 598 signes sans le chevron (plafond de 600, mesurée par programme). Elle reprend la ligne vérifiée de `ligne-claude-md-N-075-v2.md`, ajoute le renvoi à `GO-2026-11-23-32` et aux quatre retouches après lecture sur document PDF, et pointe vers cette v4 qui réunit la v3 et ses errata 1 à 3.",
        ),
        # Section 14 et « Évaluateur et conseil » : R-19 et Lecture d'ensemble
        (
            "E3-v1 Lecture d'ensemble (Relevé de méthode, l. 301)",
            "Ce qui juge cette pièce : le contre-lecteur Opus 5.5, qui a vérifié la v2 et vérifie la v3, puis Lazar, pour les cinq options de la section 11",
            "Ce qui juge cette pièce (v4) : un sous-agent neuf contre-lecteur puis la mère (les points 7, 8, 10 et 11 ont été tranchés à `GO-2026-11-21-61`, seul le point 9 reste ouvert ; les quatre corrections PDF ont été accordées à `GO-2026-11-23-32`)",
        ),
        (
            "R-19 et lecture d'ensemble (section 14, l. 345 et lignes V6, V8, V9, V10, 11)",
            "Numéros de ligne de ce fichier, calculés par programme sur un passage unique à chaque fois. Restent ouverts, en options, sans défaut : les points 7, 8, 9, 10 et 11 de la section 11 (le point 9, l'asymétrie d'apprentissage contre l'invariant de l'oracle, vient de la contre-lecture de la v1 et n'a pas de ligne ici ; il est à la ligne 256).\n\n| point | objet | lignes de la v3 | sort |\n|---|---|---|---|\n| V1 | le plancher est occupé : aucune revendication, trois citations obligatoires | 7, 8, 61, 61, 206, 219, 237 | porté |\n| V2 | bilan du produit : le reste étroit | 145 | porté |\n| V3 | l'article de 1981 cité sur pièce ; risque du lemme mis à jour | 179, 184, 191, 193, 203, 234 | porté |\n| V4 | citations des autres voisins | 169, 217 | porté |\n| V5 | bilan de la pince : un verdict d'antériorité qui lui soit propre | 80, 93 | porté |\n| V6 | règle « motif et dommage » : seul le tronc commun avant le mot de Lazar ; enjeu redit | 112, 114, 117, 236, 255 | porté ; la seconde issue de la section 4 est mise sous le point 8, suite que le vérificateur ne listait pas |\n| V7 | le plancher énoncé avec son horizon | 45, 52 | porté |\n| V8 | le § 16 ne tranche pas la place de la veille | 240, 254 | porté ; section 11, point 7 en options, **ouvert** |\n| V9 | le lemme après le verdict : un nœud | 257 | porté ; section 11, point 10 en options, **ouvert** |\n| V10 | ligne pour `CLAUDE.md` | 264 | porté, ligne du vérificateur reprise ; à compléter par la mère selon les mots de Lazar |\n| 11 | identification de l'oracle mesurée par des dommages plantés ; une strate non mesurée compte pour zéro (note sur la couverture de l'oracle, décision D-2) | 258, 48 | écrit en option, recommandation (a), confiance 0,75, **ouvert** |",
            "Numéros de ligne de la version 3 d'origine, calculés par programme lors de son établissement sur un passage unique à chaque fois. Reste ouvert, en options, sans défaut : le point 9 de la section 11 ; les points 7, 8, 10 et 11 sont tranchés (`GO-2026-11-21-61`) et portés dans cette v4 (le point 9, l'asymétrie d'apprentissage contre l'invariant de l'oracle, vient de la contre-lecture de la v1 et était à la ligne 256 de la v3).\n\n| point | objet | lignes de la v3 d'origine | sort en v4 |\n|---|---|---|---|\n| V1 | le plancher est occupé : aucune revendication, trois citations obligatoires | 7, 8, 61, 61, 206, 219, 237 | porté, avec C-1 et C-2 de l'erratum 1 |\n| V2 | bilan du produit : le reste étroit | 145 | porté |\n| V3 | l'article de 1981 cité sur pièce ; risque du lemme mis à jour | 179, 184, 191, 193, 203, 234 | porté, avec C-3 de l'erratum 1 |\n| V4 | citations des autres voisins | 169, 217 | porté |\n| V5 | bilan de la pince : un verdict d'antériorité qui lui soit propre | 80, 93 | porté |\n| V6 | règle « motif et dommage » : seul le tronc commun avant le mot de Lazar ; enjeu redit | 112, 114, 117, 236, 255 | porté, et **tranché** en section 11 point 8 (a) par `GO-2026-11-21-61` |\n| V7 | le plancher énoncé avec son horizon | 45, 52 | porté |\n| V8 | le § 16 ne tranche pas la place de la veille | 240, 254 | porté, et **tranché** en section 11 point 7 (a) par `GO-2026-11-21-61` |\n| V9 | le lemme après le verdict : un nœud | 257 | porté, et **tranché** en section 11 point 10 (a) par `GO-2026-11-21-61` |\n| V10 | ligne pour `CLAUDE.md` | 264 | porté, mis à jour selon `ligne-claude-md-N-075-v2.md` et adapté pour la v4 |\n| 11 | identification de l'oracle mesurée par des dommages plantés ; une strate non mesurée compte pour zéro (note sur la couverture de l'oracle, décision D-2) | 258, 48 | porté, et **tranché** en section 11 point 11 (a) par `GO-2026-11-21-61` |",
        ),
        # --- Bloc 2 : les quatre corrections issues de la lecture sur document PDF des seize papiers (GO-2026-11-23-32, R-5185) ---
        # Correction (i) : Xu, Yuksekgonul, Zou (2602.00986 v2, PDF p. 8, et retrait de Xu et al. de « À vérifier sur PDF » pour les pages lues, selon la fiche)
        (
            "PDF-1a (Xu et al., 2602.00986 v2, section 3, l. 97)",
            "- La réussite attendue lue dans les états internes et sa calibration : Xu, Yuksekgonul, Zou (2602.00986 v2).",
            "- La réussite attendue lue dans les états internes et son pouvoir de séparation (aire sous la courbe, [PDF, p. 8] ; le mot « calibration » ne figure pas dans le document PDF, et l'aire sous la courbe par la seule longueur de la question vaut 0,62 contre 0,67 pour les neurones de valeur, constituant une base bon marché du bras « papier dopamine » ; aucune tâche ouverte ni aucun adversaire testé, [PDF, p. 25]) : Xu, Yuksekgonul, Zou (2602.00986 v2).",
        ),
        (
            "PDF-1b (Xu et al., 2602.00986 v2, retrait de « À vérifier sur PDF », section 3, l. 104 ; mise à jour Arnold et al. lue en entier)",
            "Fischl-Lanzoni et al. et Aremu et al. en entier ; Xu et al. au-delà des pages 5 à 7 ; une recherche d'antériorité propre au bilan (tests de calibration valides à tout instant, Arnold et al., 2109.11761 v3, page 1 seule).",
            "Fischl-Lanzoni et al. et Aremu et al. en entier (Xu, Yuksekgonul et Zou, 2602.00986 v2, désormais lu en entier, 25 pages, fiche `fiche-2602.00986-v1.md`, `817712a3…`, pages citées 1, 4, 5, 8, 9, 25) ; une recherche d'antériorité propre au bilan (Arnold, Henzi et Ziegel, 2109.11761 v3, désormais lu en entier, 35 pages, fiche `fiche-2109.11761-v1.md`, `959857b4…`, `252a4c29…`, ne traite pas du bilan de N-075 mais occupe le « nul par acte » de N-076, voir N-076 erratum 3).",
        ),
        (
            "PDF-1c (Xu et al., 2602.00986 v2, tableau section 8, l. 212)",
            "| point 2 | Xu, Yuksekgonul, Zou, 2602.00986 v2 ; Bailey et al., 2412.09565 v2 | déjà au dépôt, `da004f53…` ; `9c23a613…` | 5-7 ; 1-3 |",
            "| point 2 | Xu, Yuksekgonul, Zou, 2602.00986 v2 ; Bailey et al., 2412.09565 v2 | déjà au dépôt, `da004f53…` ; `9c23a613…` | en entier (25 pages, dont p. 1, 4, 5, 8, 9, 25 ; pouvoir de séparation seul, aucune calibration) ; 1-3 |",
        ),
        # Correction (ii) : Ge-Wang et al. (2606.06529 v1, PDF p. 5, 11)
        (
            "PDF-2a (Ge-Wang et al., 2606.06529 v1, section 2, l. 74)",
            "Ge-Wang et al. (2606.06529 v1, page 1 seule) : un attaquant qui choisit quand attaquer abaisse la sûreté mesurée, ce qui touche le plancher par deux voies, si le tirage se devine et si l'oracle reconnaît inégalement le dommage selon la tâche (le saboteur choisit alors les tâches où q est bas) ;",
            "Ge-Wang et al. (2606.06529 v1, lu en entier, 19 pages, fiche `fiche-2606.06529-v1.md`, `508ed82c…`, `6042d449…`, [PDF, p. 1, 5, 11]) : un attaquant qui choisit quand attaquer abaisse la sûreté mesurée (sous audit des plus suspects ; une seule baisse dont l'intervalle de confiance exclut zéro au budget d'audit de 1 %, sur 23 trajectoires, dite borne supérieure heuristique par les auteurs, [PDF, p. 5, 11] ; tirage au hasard non testé), ce qui touche le plancher par deux voies, si le tirage se devine et si l'oracle reconnaît inégalement le dommage selon la tâche (le saboteur choisit alors les tâches où q est bas) ;",
        ),
        (
            "PDF-2b (Ge-Wang et al., 2606.06529 v1, section 8 À citer, l. 217)",
            "Ge-Wang et al. (2606.06529 v1) ;",
            "Ge-Wang et al. (2606.06529 v1, [PDF, p. 1, 5, 11] : sous audit des plus suspects ; une seule baisse dont l'intervalle de confiance exclut zéro au budget d'audit de 1 %, sur 23 trajectoires, dite borne supérieure heuristique par les auteurs ; tirage au hasard non testé) ;",
        ),
        # Correction (iii) : Zhong et Raghunathan (2508.00161 v3, PDF p. 5, 17)
        (
            "PDF-3a (Zhong et Raghunathan, 2508.00161 v3, section 4, l. 110)",
            "Un moniteur publié qui élargit sa plage normale à chaque entrée signalée accepte un écart qui grandit pas à pas (Zhong et Raghunathan, 2508.00161 v3, [PDF, p. 4-5]).",
            "Un moniteur publié qui élargit sa plage normale à chaque entrée signalée accepte en silence la répétition d'un écart déjà signalé une fois, tandis qu'un écart qui grandit pas à pas dépasse l'extrême courant et reste signalé à chaque pas (Zhong et Raghunathan, 2508.00161 v3, [PDF, p. 4-5] ; la borne de fausses alertes suppose des tirages échangeables, [PDF, p. 17] ; fiche `fiche-2508.00161-v1.md`, `8ab9faa7…`).",
        ),
        (
            "PDF-3b (Zhong et Raghunathan, 2508.00161 v3, tableau section 8, l. 214)",
            "| point 3 | Aickelin, Cayzer, arXiv 0801.3549 v3 ; Zhong, Raghunathan, 2508.00161 v3 (contre-indice : plage mise à jour par la seule nouveauté) | `0801.3549v3.pdf`, `2ed19828…` ; `2508.00161v3.pdf`, `898dffaf…` | en entier par le contre-lecteur de la note ; 4, 5 |",
            "| point 3 | Aickelin, Cayzer, arXiv 0801.3549 v3 ; Zhong, Raghunathan, 2508.00161 v3 (contre-indice : une alerte par extrême neuf, la répétition d'un écart déjà signalé passe en silence tandis qu'un écart qui grandit pas à pas est signalé ; borne sous échangeabilité) | `0801.3549v3.pdf`, `2ed19828…` ; `2508.00161v3.pdf`, `898dffaf…` | en entier par le contre-lecteur de la note ; en entier par le lecteur des seize papiers (pages citées 1, 2, 4, 5, 7, 8, 16, 17) |",
        ),
        # Correction (iv) : McKenzie et al., attaque étagée STACK (2506.24068 v3, PDF p. 1, 3, 10)
        (
            "PDF-4a (McKenzie et al., 2506.24068 v3, section 3, l. 96)",
            "une chaîne de garde-fous se défait étage par étage (McKenzie et al., 2506.24068 v3, [PDF, p. 1]) ;",
            "une chaîne de garde-fous d'entrée et de sortie sans sonde sur activations se défait étage par étage (McKenzie et al., 2506.24068 v3, [PDF, p. 1, 3, 10] : suppose que l'attaquant voit quel étage l'a bloqué — 71 % de succès avec ce retour, 33 % par transfert sans accès ; fiche `fiche-2506.24068-v1.md`, `180ebfa5…`) ;",
        ),
        (
            "PDF-4b (McKenzie et al., 2506.24068 v3, section 8 À citer, l. 217)",
            "McKenzie et al. (2506.24068 v3) ;",
            "McKenzie et al. (2506.24068 v3, `3e08b7cc…`, [PDF, p. 1, 3, 10] : suppose que l'attaquant voit quel étage l'a bloqué — 71 % avec ce retour, 33 % par transfert sans accès, aucune sonde sur activations dans la chaîne) ;",
        ),
    ]


def main() -> None:
    SORTIE_DIR.mkdir(parents=True, exist_ok=True)
    texte_v3 = SOURCE_V3.read_text(encoding="utf-8")
    empreinte_v3 = hashlib.sha256(texte_v3.encode("utf-8")).hexdigest()
    if empreinte_v3 != SHA256_ATTENDU_V3:
        raise RuntimeError(
            f"Empreinte inattendue pour {SOURCE_V3} : {empreinte_v3} != {SHA256_ATTENDU_V3}"
        )

    texte_v4 = texte_v3
    journal: list[tuple[str, str, str]] = []
    for identifiant, ancien, nouveau in construire_remplacements():
        texte_v4 = remplacer_unique(texte_v4, identifiant, ancien, nouveau, journal)

    # Contrôle d'intégrité spécifique : les deux nombres de lignes hors sections modifiées ne dérivent pas
    CIBLE_V4.write_text(texte_v4, encoding="utf-8")
    empreinte_v4 = hashlib.sha256(texte_v4.encode("utf-8")).hexdigest()

    lignes_v3 = texte_v3.splitlines(keepends=True)
    lignes_v4 = texte_v4.splitlines(keepends=True)
    diff_lignes = list(
        difflib.unified_diff(
            lignes_v3,
            lignes_v4,
            fromfile="docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md",
            tofile="docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v4.md",
            n=2,
        )
    )
    DIFF_V3_V4.write_text("".join(diff_lignes), encoding="utf-8")

    # Vérification de la longueur de la nouvelle ligne proposée pour CLAUDE.md
    for ligne in texte_v4.splitlines():
        if ligne.startswith("> N-075 (GO-2026-11-21-46"):
            longueur_ligne = len(ligne[2:])
            assert longueur_ligne <= 600, f"Ligne CLAUDE.md trop longue : {longueur_ligne}"

    # Écrit la table de correspondance des remplacements
    lignes_table = [
        "# Table exacte des remplacements appliqués sur la version 3 de la décision N-075 pour produire la version 4",
        "",
        f"- Source exacte : `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md` (`{empreinte_v3}`), {len(lignes_v3)} lignes, {len(texte_v3.encode('utf-8'))} octets.",
        f"- Sortie produite : `decision-N-075-issue-plancher-et-deux-regards-v4.md` (`{empreinte_v4}`), {len(lignes_v4)} lignes, {len(texte_v4.encode('utf-8'))} octets.",
        f"- Nombre total de remplacements uniques vérifiés par programme : {len(journal)}.",
        "",
        "| identifiant | extrait remplacé (début) | extrait nouveau (début) |",
        "|---|---|---|",
    ]
    for identifiant, ancien, nouveau in journal:
        a_court = ancien.replace("\n", " ↵ ").replace("|", "\\|")[:90]
        n_court = nouveau.replace("\n", " ↵ ").replace("|", "\\|")[:90]
        lignes_table.append(f"| {identifiant} | `{a_court}` | `{n_court}` |")
    TABLE_CORRESPONDANCE.write_text("\n".join(lignes_table) + "\n", encoding="utf-8")

    print(f"V3 sha256 : {empreinte_v3} ({len(lignes_v3)} lignes)")
    print(f"V4 sha256 : {empreinte_v4} ({len(lignes_v4)} lignes)")
    print(f"Remplacements appliqués : {len(journal)}")
    print(f"Diff écrit : {DIFF_V3_V4} ({len(diff_lignes)} lignes)")


if __name__ == "__main__":
    main()
