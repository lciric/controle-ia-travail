#!/usr/bin/env python3
# Assemblage des faits servis pour trois questions de conv-audit (1er novembre 2026).
# Lit uniquement les extraits déjà tirés de origin/canal/conv-audit-n04 et de main (dossier extr/),
# plus le fichier de faits v2 autorisé. N'écrit que dans donnees/questions-3-novembre-v1/.
import hashlib, re, sys, os

EXTR = '/tmp/claude-0/-home-user-controle-ia-travail/4ff7d1a3-3d12-504e-b550-a8bc2f8510b1/scratchpad/conv/extr/'
DEP = '/home/user/controle-ia-travail/'
OUT = DEP + 'donnees/questions-3-novembre-v1/'
MARQUE = '[retiré, règle 2 : recommandation ou confiance d\'auteur]'
MARQUE_ATT = '[retiré par l\'assembleur : description d\'une sonde de réseau classée « échappement de confinement » par le classifieur, hors du niveau méthode]'

def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()

def mots(t):
    return len(t.split())

def lire(p):
    return open(p, encoding='utf-8').read()

def lignes(t, a, b):
    """lignes a..b (1-based, inclusives)"""
    L = t.split('\n')
    return '\n'.join(L[a-1:b])

retraits = {1: [], 2: [], 3: []}

def retirer(texte, motif, q, etiquette, marque=MARQUE, flags=re.S):
    nouveau, n = re.subn(motif, marque, texte, flags=flags)
    if n == 0:
        raise SystemExit(f'motif introuvable ({etiquette}) : {motif[:60]}')
    retraits[q].append((etiquette, n))
    return nouveau

# ------------------------------------------------------------------ Q1 : convergence v3
q1 = lire(EXTR + 'question-convergence-defense-unique-v3.md')
q1_sha = sha(EXTR + 'question-convergence-defense-unique-v3.md')
v2 = lire(DEP + 'donnees/argon-seul-convergence-v1/faits-convergence-v2-argon-v1.md')
v2_sha = sha(DEP + 'donnees/argon-seul-convergence-v1/faits-convergence-v2-argon-v1.md')
# les trois pièces déjà assemblées (de « ### Pièce 1 » à la fin)
i = v2.index('### Pièce 1')
pieces_v2 = v2[i:]
gel = lire(EXTR + 'gel-conception-arene-melange-v4.md')
gel_sha = sha(EXTR + 'gel-conception-arene-melange-v4.md')
cal_sha = sha(EXTR + 'calibrage-deltas-arene-melange-v4.json')
cal_mots = mots(lire(EXTR + 'calibrage-deltas-arene-melange-v4.json'))
cal_red = lire(EXTR + 'calibrage-reduit.json')
D_ARENE = 'brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/'
pdf_sha = sha(DEP + 'docs/sources/pdf/anteriorite-P-041-v1/2412.09565v2.pdf')

sha_b4 = '305911b7ab1945d7607377ede9c8cbfcf2257834bca6d6aadcf7c19be41f8160'
sha_ver = '28ab322f9d2e6098562d127f20e98560c4b202ef737b75ff217dfe0c9c7672f2'
sha_code = '70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61'

ent1 = f"""# Faits servis — question de convergence v3 (défense unique ré-entraînée, dynamique de meilleure réponse) — v1

Assemblés par un sous-agent neuf (assembleur), 1er novembre 2026, pour trois canaux (Argon seul, Kimi seul, collisionneur à quatre espèces). Dossier de travail hors git. Aucune pièce n'est modifiée sur sa branche ; chaque empreinte ci-dessous est recalculée par `sha256sum` sur le fichier tiré de `origin/canal/conv-audit-n04` (ou de `main` pour le PDF).

- **Question servie** : `question-convergence-defense-unique-v3.md` — `{q1_sha}` ({mots(q1)} mots). Elle remplace la v2 (`08f2b017…`).
- **Base** : les pièces 1 à 3 sont reprises telles quelles de `donnees/argon-seul-convergence-v1/faits-convergence-v2-argon-v1.md` (`{v2_sha}`, assemblé par session-depot pour la v2 ; mêmes pièces, empreintes vérifiées ci-dessous contre la branche). Les pièces 4 et 5 sont ajoutées pour la v3.
- **Règle 2** : aucune ligne retirée. Ces pièces sont un préenregistrement, sa vérification, un code, un gel et un calibrage : leurs « confiances » sont des prédictions préenregistrées sur le pilote, pas des avis sur la question posée ; elles restent. (Même lecture que session-depot pour la v2.)
- **Niveau méthode** : le monde est une famille de lois synthétiques (mélanges gaussiens), sans modèle de langage ni texte ; « l'attaquant » est un choix de paramètres dans une boîte bornée. Aucune pièce du bras d'attaque, aucun mode nommé.

## Pièces

| n° | pièce | chemin d'origine (branche `canal/conv-audit-n04`) | sha256 recalculée | mots | servie |
|---|---|---|---|---|---|
| 1 | préenregistrement, brouillon 4 | `{D_ARENE}preenregistrement-arene-melange-equilibre-v1-brouillon4.md` | `{sha_b4}` | 13 108 | entière |
| 2 | vérification du brouillon 4 | `{D_ARENE}verification-arene-melange-v4-brouillon4.md` | `{sha_ver}` | 3 973 | entière |
| 3 | code du pilote `arene_melange_v4.py` | `{D_ARENE}arene_melange_v4.py` | `{sha_code}` | 14 562 | entier |
| 4 | gel de la conception v4 (nouveau pour la v3) | `{D_ARENE}gel-conception-arene-melange-v4.md` | `{gel_sha}` | {mots(gel)} | entier |
| 5 | calibrage des δ v4 (nouveau pour la v3) | `{D_ARENE}calibrage-deltas-arene-melange-v4.json` | `{cal_sha}` | {cal_mots:,} | extrait : tout sauf la liste `resultats` (432 entrées par tâche) ; voir note |

**Pièces listées mais non servies, et pourquoi** :
- `essai-pilote-arene-melange-v4-detection.json` (`4d1fb23f…`, pilote complet) : non servi (1,38 Mo, trop volumineux pour un appel ; ses résultats sont rapportés par le brouillon 4 et sa vérification, et ses deux moitiés sont empreintées dans le brouillon 4). Même choix que pour la v2.
- PDF de Bailey et collègues, arXiv 2412.09565 (`docs/sources/pdf/anteriorite-P-041-v1/2412.09565v2.pdf` sur `main`, sha256 `{pdf_sha}`, compagnon `.sha256` conforme) : **un PDF n'est pas servi**. Le chemin et l'empreinte sont donnés pour que la session qui lance le canal le joigne si elle le décide.
- Note sur la pièce 5 : le fichier complet fait {cal_mots:,} mots ; la liste `resultats` (432 dictionnaires, un par tâche (δ, instance) : statut de l'attaquant, V par bras et par tour, temps) est remplacée par une ligne qui le dit. Tout le reste (δ choisis, règle, manifeste, moyennes de V(A) par δ, stabilité sous rééchantillonnage, temps) est reproduit tel quel.

---

"""
piece4 = f"### Pièce 4 — gel de la conception v4, écrit avant tout calcul (`gel-conception-arene-melange-v4.md`, `{gel_sha[:12]}…`, entier)\n\n" + gel + "\n\n"
piece5 = f"### Pièce 5 — calibrage des δ v4 (`calibrage-deltas-arene-melange-v4.json`, `{cal_sha[:12]}…`, extrait : liste `resultats` omise)\n\n```json\n" + cal_red + "\n```\n"
faits1 = ent1 + pieces_v2.rstrip('\n') + "\n\n" + piece4 + piece5

# ------------------------------------------------------------------ Q2 : sélection génération à génération
Q2P = '/tmp/claude-0/-home-user-controle-ia-travail/4ff7d1a3-3d12-504e-b550-a8bc2f8510b1/scratchpad/conv/q3/question-selection-generations-v1.md'
q2 = lire(Q2P); q2_sha = sha(Q2P)
PREF = 'brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/'
src2 = {
 'dossier': ('docs/notes/ideation-organisme-v1/explication-organisme-v1/dossier-factuel-organisme-v1.md', EXTR+'q2/dossier-factuel-organisme-v1.md'),
 'integ': (PREF+'integration-proposeurs-ia-v1.md', EXTR+'q2/integration-proposeurs-ia-v1.md'),
 'prog7': (PREF+'programme-conception-organisme-v7.md', EXTR+'q2/programme-conception-organisme-v7.md'),
 'abis': (PREF+'premier-lancement-reel/lecture-lancement-reel-a-bis-v1.md', EXTR+'q2/lecture-lancement-reel-a-bis-v1.md'),
 'c1': (PREF+'demonstration-couche1-v7/lecture-couche1-v7-v2.md', EXTR+'q2/lecture-couche1-v7-v2.md'),
 'cyc': (PREF+'demonstration-cycle-v5/lecture-demonstration-cycle-v5-v1.md', EXTR+'q2/lecture-demonstration-cycle-v5-v1.md'),
 'pont': (PREF+'pont-fiche-loi-v1/conception-pont-fiche-loi-v1.md', EXTR+'q2/conception-pont-fiche-loi-v1.md'),
 'pontl': (PREF+'pont-fiche-loi-v1/LISEZMOI-pont-v1.md', EXTR+'q2/LISEZMOI-pont-v1.md'),
 'prog': ('docs/programme-controle-ia-v2.md', DEP+'docs/programme-controle-ia-v2.md'),
 'n013': ('docs/decisions/decision-N-013-v1.md', DEP+'docs/decisions/decision-N-013-v1.md'),
 'n035': ('docs/decisions/decision-N-035-v1.md', DEP+'docs/decisions/decision-N-035-v1.md'),
}
T2 = {k: lire(v[1]) for k, v in src2.items()}
H2 = {k: sha(v[1]) for k, v in src2.items()}
M2 = {k: mots(T2[k]) for k in src2}

dossier = T2['dossier']
d_s1 = lignes(dossier, 18, 97)
d_s6 = lignes(dossier, 185, 193)
d_s9 = lignes(dossier, 242, 280)
d_s10 = lignes(dossier, 282, 292)
integ = lignes(T2['integ'], 40, 98)
prog7 = lignes(T2['prog7'], 19, 41)
pont = T2['pont']
pont = retirer(pont, r"Recommandation : \(a\) pour le premier essai et la course 2,\n\(c\) à partir de la course 3 ; confiance 0,6\. Défaut sous 48 heures : \(a\)\.", 2, 'pont § h, D-P1 (recommandation, confiance, défaut)')
pont = retirer(pont, r"Recommandation : \(a\), confiance 0,65\. Défaut sous 48 heures : \(a\)\.", 2, 'pont § h, D-P2')
pont = retirer(pont, r"Recommandation :\n\(a\), confiance 0,6\. Défaut sous 48 heures : \(a\)\.", 2, 'pont § h, D-P3')
pont = retirer(pont, r"Recommandation : \(c\), confiance 0,6\. Défaut sous 48 heures : \(a\), le plus prudent \(codé par défaut\)\.", 2, 'pont § h, D-P4')
pont = retirer(pont, r"Recommandation : \(a\), confiance 0,7\. Aucun défaut : j'attends ton mot\.", 2, 'pont § h, D-P5')
prog = lignes(T2['prog'], 88, 115)

def tab(n, titre, cle, extrait):
    ch, _ = src2[cle]
    return f"| {n} | {titre} | `{ch}` | `{H2[cle]}` | {M2[cle]:,} | {extrait} |"

nb_ret2 = sum(n for _, n in retraits[2])
ent2 = f"""# Faits servis — question « boucle de sélection génération à génération de l'organisme d'idéation » v1 — v1

Assemblés par un sous-agent neuf (assembleur), 1er novembre 2026, pour trois canaux (Argon seul, Kimi seul, collisionneur à quatre espèces). Dossier de travail hors git. Pièces tirées de `origin/canal/conv-audit-n04` (sauf mention `main`) ; empreintes recalculées par `sha256sum` sur le fichier entier, même quand un extrait seul est servi.

- **Question servie** : `question-selection-generations-v1.md` — `{q2_sha}` ({mots(q2)} mots).
- **Règle 2** : {nb_ret2} passages retirés, tous dans la pièce 7 (conception du pont, § h « Décisions pour toi ») : les cinq clauses « Recommandation : … ; confiance … ; défaut sous 48 heures : … » des décisions D-P1 à D-P5 sont remplacées par la marque ; la décision, l'enjeu et les options (avantage, inconvénient) restent. Gardés, comme faits et non comme avis sur la question : les « seuils recommandés » de l'étalonnage des juges du pré-pilote (pièce 1, § 6, chiffres de [B10]), les confiances « 0,4 à 0,5 » des analogies des protocelles (pièce 1, § 9.3), « relancer la course 1 : déconseillé (R-737) » (pièce 1, § 10, décision consignée), les probabilités d'originalité des hypothèses (pièce 10, calibrées au 14 septembre, partie du document qui fait foi), « originalité revue à environ 0,35 (mon estimation, non sourcée) » sur HC3 (pièce 11, ne porte pas sur la question), et les options (a), (b), (c) de N-035 dont (a) est « retenue » par Lazar (pièce 12).
- **Niveau méthode** : aucune pièce du bras d'attaque ; rien sur l'auto-organisation inspirée d'Avalon. Les pièces décrivent le pôle (juge figé, gel, témoins, mémoire, recombinaison), ses lancements et ses lectures, le pont fiche → loi (conception seulement, pas le code `pont_v1.py`), et les hypothèses du programme.

## Pièces

| n° | pièce | chemin d'origine | sha256 recalculée (fichier entier) | mots (fichier entier) | servi |
|---|---|---|---|---|---|
{tab(1, 'dossier factuel de l\'organisme, § 1, § 6, § 9, § 10', 'dossier', 'extraits l. 18–97, 185–193, 242–280, 282–292')}
{tab(2, 'conception du pôle : intégration des proposeurs, § 1 (la boucle) et § 2', 'integ', 'extrait l. 40–98 (l. 42–98 citées, plus le titre de section)')}
{tab(3, 'programme de conception de l\'organisme v7, § 0', 'prog7', 'extrait l. 19–41 (l. 23–33 citées, paragraphe entier) ; aucun compagnon `.sha256` sur la branche (R11 : fichier présent, empreinte lue ce jour)')}
{tab(4, 'lecture du lancement réel « (a) bis »', 'abis', 'entière')}
{tab(5, 'lecture de la couche 1 v7, v2 (banque réelle, « pas de dents »)', 'c1', 'entière')}
{tab(6, 'lecture des démonstrations du cycle v5', 'cyc', 'entière')}
{tab(7, 'pont fiche de course → fiche-loi, conception v1 (rendu avant le lancement)', 'pont', 'entière, règle 2 appliquée au § h ; le code `pont_v1.py` et ses essais ne sont pas servis')}
{tab(8, 'pont, LISEZMOI v1 (état, essais, pièces lues)', 'pontl', 'entier')}
{tab(9, 'programme v2 (`main`), section 5 « Hypothèses » : H1 à H8, HC1 à HC6, H3 à H7 (H9 vient de N-035)', 'prog', 'extrait l. 88–115 ; le document fait 4 411 mots, seule cette section est servie')}
{tab(10, 'décision N-013 (`main`) : revendications précisées après le niveau 2 de l\'état de l\'art', 'n013', 'entière')}
{tab(11, 'décision N-035 (`main`) : H9, survie des contraintes de sécurité à la délégation', 'n035', 'entière')}

**Pièces listées mais absentes ou non servies** : aucune absente. Le dossier `pont-fiche-loi-v1/` contient aussi `pont_v1.py` et `essais/test_pont_v1.py` (code) : non servis, la question demande la conception seulement. Les sources que citent les pièces (brouillons B10, TI, registres [Dbr], [Dmain], lectures de génération 0, de la couche 1 bis, etc.) ne sont pas des pièces listées et ne sont pas servies.

---

"""
def P(n, titre, cle, ext, corps):
    ch, _ = src2[cle]
    return f"### Pièce {n} — {titre} (`{os.path.basename(ch)}`, `{H2[cle][:12]}…`, {ext})\n\n{corps.rstrip()}\n\n"

faits2 = ent2
faits2 += P(1, 'dossier factuel de l\'organisme — § 1 vue d\'ensemble', 'dossier', 'extrait l. 18–97', d_s1)
faits2 += P('1 (suite)', 'dossier factuel — § 6 les juges', 'dossier', 'extrait l. 185–193', d_s6)
faits2 += P('1 (suite)', 'dossier factuel — § 9 des idées aux hypothèses testées', 'dossier', 'extrait l. 242–280', d_s9)
faits2 += P('1 (suite)', 'dossier factuel — § 10 résultats déjà obtenus', 'dossier', 'extrait l. 282–292', d_s10)
faits2 += P(2, 'intégration des proposeurs dans l\'organisme — § 1 la boucle, § 2 les prises', 'integ', 'extrait l. 40–98', integ)
faits2 += P(3, 'programme de conception de l\'organisme v7 — § 0', 'prog7', 'extrait l. 19–41', prog7)
faits2 += P(4, 'lecture du lancement réel « (a) bis »', 'abis', 'entière', T2['abis'])
faits2 += P(5, 'lecture de la couche 1 v7, v2', 'c1', 'entière', T2['c1'])
faits2 += P(6, 'lecture des démonstrations du cycle v5', 'cyc', 'entière', T2['cyc'])
faits2 += P(7, 'pont fiche → loi, conception v1', 'pont', 'entière, règle 2 appliquée au § h', pont)
faits2 += P(8, 'pont fiche → loi, LISEZMOI v1', 'pontl', 'entier', T2['pontl'])
faits2 += P(9, 'programme v2 — section 5, hypothèses', 'prog', 'extrait l. 88–115', prog)
faits2 += P(10, 'décision N-013', 'n013', 'entière', T2['n013'])
faits2 += P(11, 'décision N-035', 'n035', 'entière', T2['n035'])

# ------------------------------------------------------------------ Q3 : vérification non circulaire
Q3P = '/tmp/claude-0/-home-user-controle-ia-travail/4ff7d1a3-3d12-504e-b550-a8bc2f8510b1/scratchpad/conv/q3/question-verification-non-circulaire-v1.md'
q3 = lire(Q3P); q3_sha = sha(Q3P)
src3 = {
 'lis': ('docs/notes/ideation-organisme-v1/orchestrateur-v56/LISEZMOI-orchestrateur-pole-v7-v48.md', EXTR+'q3/LISEZMOI-orchestrateur-pole-v7-v48.md'),
 'devis': ('docs/notes/ideation-organisme-v1/machine-jetable-v1/devis-et-plomberie-machine-jetable-v3.md', EXTR+'q3/devis-et-plomberie-machine-jetable-v3.md'),
 'rel': (PREF+'collisionneur-noeuds-31-octobre-v1/relecture-opus-synthese-n12-n13-v1.md', EXTR+'q3/relecture-opus-synthese-n12-n13-v1.md'),
 'ava': ('docs/notes/rlcr-v1/lecture-verifiee-avalon-m1-v1.md', EXTR+'q3/lecture-verifiee-avalon-m1-v1.md'),
}
T3 = {k: lire(v[1]) for k, v in src3.items()}
H3 = {k: sha(v[1]) for k, v in src3.items()}
M3 = {k: mots(T3[k]) for k in src3}

lis = T3['lis']
lis_ext = lignes(lis, 1, 12) + '\n\n[…]\n\n' + lignes(lis, 30, 48) + '\n\n[…]\n\n' + lignes(lis, 89, 102)
devis = T3['devis']
devis = retirer(devis, r"- \*\*D'où la voie recommandée \(inchangée\)\*\* : .*?\n(?=- \*\*Sortie réseau)", 3, 'devis § 0, « voie recommandée »', MARQUE + '\n')
devis = retirer(devis, r"\*\*Recommandation\*\* : \(A\), avec le remède \(R-a\).*?moins de 0,2 USD\.", 3, 'devis § 5, recommandation et confiance')
devis = retirer(devis, r"basse \(recommandé\) ;", 3, 'devis § 5, point 3 « (recommandé) »', 'basse (' + MARQUE + ') ;')
devis = retirer(devis, r"Je ne le recommande pas : \(A\) n'en a pas besoin, et la sonde relève du classifieur\.", 3, 'devis § 5, point 4')
# contenu hors niveau méthode : nom d'un procédé de sonde réseau classé « échappement de confinement »
nb_att = 0
for motif, rempl in [
    (r"puis un nom de domaine et un nom `sslip\.io`\)", "puis " + MARQUE_ATT + ")"),
    (r"\(un nom de domaine, puis un nom `sslip\.io`\)", "(" + MARQUE_ATT + ")"),
    (r"Puis un nom de domaine et un nom\n> `sslip\.io`, procédé qui sert à joindre une adresse arbitraire : refusés", "Puis " + MARQUE_ATT + " : refusés"),
]:
    devis, n = re.subn(motif, rempl, devis)
    if n == 0:
        raise SystemExit('motif attaque introuvable : ' + motif[:50])
    nb_att += n
rel = T3['rel']
rel_ext = lignes(rel, 1, 7) + '\n\n[…]\n\n' + lignes(rel, 25, 27) + '\n\n[…]\n\n' + lignes(rel, 166, 187)
rel_ext = retirer(rel_ext, r"- \*\*Recommandation\*\* : \(a\), et confirmer que N-053 .*?\Z", 3, 'relecture, carte N12, ligne « Recommandation … Confiance 0,65 »')
ava = T3['ava']
ava_ext = lignes(ava, 1, 7) + '\n\n[…]\n\n' + lignes(ava, 194, 194) + '\n\n[…]\n\n' + lignes(ava, 199, 204)

nb_ret3 = sum(n for _, n in retraits[3])
def tab3(n, titre, cle, extrait):
    ch, _ = src3[cle]
    return f"| {n} | {titre} | `{ch}` | `{H3[cle]}` | {M3[cle]:,} | {extrait} |"

ent3 = f"""# Faits servis — question « vérification non circulaire des artefacts produits en bac à sable par l'organisme » v1 — v1

Assemblés par un sous-agent neuf (assembleur), 1er novembre 2026, pour trois canaux (Argon seul, Kimi seul, collisionneur à quatre espèces). Dossier de travail hors git. Pièces tirées de `origin/canal/conv-audit-n04` ; empreintes recalculées par `sha256sum` sur le fichier entier, même quand un extrait seul est servi.

- **Question servie** : `question-verification-non-circulaire-v1.md` — `{q3_sha}` ({mots(q3)} mots).
- **Règle 2** : {nb_ret3} passages retirés — pièce 2 (devis v3) : la « voie recommandée » du verdict (§ 0), la « Recommandation : (A) … Confiance 0,6 » du § 5, « (recommandé) » et « Je ne le recommande pas … » du § 5 ; pièce 3 (relecture de la synthèse N12–N13) : la ligne « Recommandation : (a) … Confiance 0,65 » de la carte N12. Restent : les options avec avantage et inconvénient, les décisions de Lazar (R-533, R-776, R-640, R-821, R-822), les constats, les gardes, le devis chiffré.
- **Niveau méthode, défense seulement** : vérifié pièce par pièce. Les pièces décrivent un bac `bwrap` (drapeaux, montages, quotas), ses sondes d'étanchéité internes (écouteur sur la boucle locale, écriture hors dossier : un exécuteur qui laisse passer est refusé), une machine louée sans secret (pare-feu du nuage, `nftables`, sonde de sortie, gardes G1 à G13, destruction par identifiant), et la circularité relevée par Avalon. **Aucune suite publique d'étanchéité n'est nommée dans les pièces** (c'est précisément ce que la question demande aux espèces, Q6). {nb_att} mentions ont été retirées par l'assembleur dans la pièce 2 (§ 0.1 réserve 7, § 2.0 point 3, § 8) : le nom d'un service public et la phrase qui dit à quoi il sert, cités dans le récit d'une sonde réseau d'un sous-agent antérieur, classée « échappement de confinement » par le classifieur ; le reste du récit (constat, décision « ces sondes ne se renouvellent pas sans le mot de Lazar ») est gardé. La lecture d'Avalon, § 3.7 (comportements d'un optimiseur face à des contrôles de récompense, p. 77–80) n'est pas servie : hors des pièces listées et au-delà du niveau méthode.

## Pièces

| n° | pièce | chemin d'origine | sha256 recalculée (fichier entier) | mots (fichier entier) | servi |
|---|---|---|---|---|---|
{tab3(1, 'LISEZMOI de l\'orchestrateur v48 (dossier v56) : étage de tests de mort, bac à sable', 'lis', 'extraits l. 1–12 (identification), 30–48 (ce que fait la v48, l. 30–44 citées), 89–102 (ce qui n\'est pas vérifié en réel)')}
{tab3(2, 'machine jetable : devis et plomberie sans secret, v3 (dossier `machine-jetable-v1/`, R-868)', 'devis', 'entière, règle 2 et retraits de l\'assembleur (voir en-tête) ; les copies de documentation et de prix du dossier ne sont pas servies')}
{tab3(3, 'relecture indépendante (Opus) de la synthèse du collisionneur sur N12 et N13 — tenant lieu de la synthèse', 'rel', 'extraits l. 1–7, 25–27, 166–187 (carte N12, où le risque de circularité est nommé)')}
{tab3(4, 'lecture vérifiée d\'Avalon-M1 (source locale de la citation p. 76 et des « 25 environnements », PDF non servi)', 'ava', 'extraits l. 1–7, 194, 199–204')}

**Pièces listées mais absentes ou non servies** :
- `synthese-n12-n13-v1.md` (la synthèse elle-même, section N12 (2)) : **absente des références permises** (`origin/canal/conv-audit-n04` et `main` ne la portent pas ; la relecture la cite comme copie de bloc-notes, sha256 `b1d28f0d…`, et elle vit sous `donnees/`, non lu). Servie à sa place : la relecture indépendante (pièce 3), qui nomme le même risque (« une vérification faite dans le même bac à sable est circulaire, Avalon p. 76 ») et dit que la synthèse « tenue sous condition » exige un erratum avant de servir.
- Rapport Avalon-M1 (PDF `docs/sources/pdf/rlcr-v1/avalonm1-general-reasoning-2026-10-23-v1.pdf`, sha256 `6429a78f…` d'après la lecture vérifiée) : un PDF n'est pas servi ; la pièce 4 en donne les deux citations utiles (p. 76, p. 79), vérifiées par script d'après son en-tête.
- Les deux contre-lectures CL13 et CL14 (« jugé non sûr », voie vers le superutilisateur de l'hôte) et le durcissement v50 : non listées comme pièces, non servies ; leur existence est attestée par le dossier factuel (question 2, pièce 1, § 9.2) et par le devis (pièce 2, § 1.1, CL15 à CL17).

---

"""
def P3(n, titre, cle, ext, corps):
    ch, _ = src3[cle]
    return f"### Pièce {n} — {titre} (`{os.path.basename(ch)}`, `{H3[cle][:12]}…`, {ext})\n\n{corps.rstrip()}\n\n"

faits3 = ent3
faits3 += P3(1, 'LISEZMOI de l\'orchestrateur v48 — étage de tests de mort', 'lis', 'extraits l. 1–12, 30–48, 89–102', lis_ext)
faits3 += P3(2, 'machine jetable — devis et plomberie sans secret, v3', 'devis', 'entière, règle 2 et retraits de l\'assembleur', devis)
faits3 += P3(3, 'relecture indépendante de la synthèse N12–N13 — carte N12', 'rel', 'extraits l. 1–7, 25–27, 166–187', rel_ext)
faits3 += P3(4, 'lecture vérifiée d\'Avalon-M1 — pratiques de l\'annexe K', 'ava', 'extraits l. 1–7, 194, 199–204', ava_ext)

os.makedirs(OUT, exist_ok=True)
for nom, t in [('faits-convergence-v3-v1.md', faits1), ('faits-selection-generations-v1.md', faits2), ('faits-bac-a-sable-non-circulaire-v1.md', faits3)]:
    with open(OUT + nom, 'w', encoding='utf-8') as f:
        f.write(t)
    print(nom, mots(t), 'mots', sha(OUT + nom))
print('retraits :', retraits)
print('mentions attaque retirées (Q3) :', nb_att)
