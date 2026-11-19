"""Essais de l'instrument du bras A, texte neuf (brouillon 5, 3.1, 3.2, 3.3, 6.4 point 2, 6.5, 8.4) : classes
d'actions, identités de proposition, vérité par construction, entrées aveugles, insertion en une passe, empreintes
des consignes. Données synthétiques seulement."""
import hashlib
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import fabrication_v3 as fab
from controle_ia.organismes_discrets import graines_bras_a_v1 as g
from controle_ia.organismes_discrets import instrument_appariement_v1 as ia

RACINE = Path(__file__).resolve().parents[1]
BROUILLON = RACINE / "prereg" / "T0.7-organismes-discrets-v-a-v2-brouillon5.md"
ENTROPIE = 20261119


def action(i, op="ADD", titre=True, proposition=True, controles=True, controles_texte=None):
    t = f"ACTION: {op}\n"
    if titre:
        t += f"TITLE: Expérience {i} sur le modèle M{i}\n"
    if proposition:
        t += f"PROPOSAL: Entraîner le modèle M{i} sur le jeu D{i} et mesurer la métrique K{i}.\n"
    if controles:
        t += f"CONTROLS: {controles_texte or f'base aléatoire sur D{i} ; ablation de la couche {i} de M{i}'}\n"
    t += f"COST: {i + 1}\nPREDICTION: hausse de K{i}\n"
    return t


def episode():
    return [action(i) for i in range(10)]


# --- Lot 1 -------------------------------------------------------------------------------------------------------------

def test_classes_d_actions():
    assert ia.classe_action(action(0)) == ia.JUGEABLE
    assert ia.classe_action(action(0, controles=False)) == ia.SANS_CONTROLES
    assert ia.classe_action(action(0, controles_texte="   ")) in (ia.SANS_CONTROLES, ia.JUGEABLE)
    assert ia.classe_action("ACTION: ADD\nTITLE: t\nPROPOSAL: p\nCONTROLS:   \nCOST: 1\n") == ia.SANS_CONTROLES
    assert ia.classe_action(action(0, proposition=False)) == ia.SANS_PROPOSITION
    assert ia.classe_action(action(0, proposition=False, controles=False)) == ia.SANS_PROPOSITION
    assert ia.classe_action("**ACTION:** ADD\n**TITLE:** t\n**PROPOSAL:** p\n**CONTROLS:** c\n") == ia.JUGEABLE
    with pytest.raises(GardeArret):
        ia.classes_episode(episode()[:9])
    assert ia.comptes_classes([episode()]) == {ia.JUGEABLE: 10, ia.SANS_CONTROLES: 0, ia.SANS_PROPOSITION: 0}


def test_identites_ajout_revision_refus():
    acts = [action(0), action(1), action(2, op="REVISE 1"), action(3, op="REVISE 7"), action(4, titre=False)]
    ident = ia.identites_de_proposition(acts)
    assert ident == [("proposition", 1), ("proposition", 2), ("proposition", 1), ("refusee", 3), ("refusee", 4)]
    assert ia.actions_remplacees_ou_refusees(acts) == [True, False, False, True, True]


def test_verite_par_construction_cas_de_classement():
    """8.4, essais de classement (ligne 820) : à effet ; ajout et révision de la même proposition : sans effet ; textes
    identiques : sans effet ; champ venu d'une action refusée : à effet si le texte diffère."""
    acts = episode()
    acts[1] = action(1, op="REVISE 1")                          # même proposition que l'action 0
    acts[3] = action(3, controles_texte="contrôle commun")
    acts[4] = action(4, controles_texte="contrôle commun")       # textes identiques
    acts[5] = action(5, op="REVISE 9")                          # refusée
    for dose in (1.0,):
        f = fab.fabriquer_episode_texte(acts, dose, "CONTROLS", ENTROPIE, "fab-00", 0)
        v = ia.verite_par_construction(acts, f)
        ident = ia.identites_de_proposition(acts)
        for x in v:
            if not x.deplacee:
                assert x.verite is None
                continue
            j = x.source
            if ident[x.indice] == ident[j]:
                assert x.verite == ia.SANS_EFFET
            elif {x.indice, j} == {3, 4}:
                assert x.verite == ia.SANS_EFFET
            else:
                assert x.verite == ia.A_EFFET
    # construction dirigée : 0 reçoit de 1 (même proposition), 3 de 4 (même texte), 5 (refusée) de 6, 6 de 5
    d = [fab.decouper_texte(a, "CONTROLS") for a in acts]
    recoit = {0: 1, 1: 0, 3: 4, 4: 3, 5: 6, 6: 5}
    deplacees = [d[i].avant + d[recoit[i]].valeur + d[i].apres if i in recoit else acts[i] for i in range(10)]
    ep = fab.EpisodeFabrique(deplacees, 1.0, "CONTROLS", 10, 6, False, recoit, {})
    v = {x.indice: x.verite for x in ia.verite_par_construction(acts, ep)}
    assert v[0] == v[1] == ia.SANS_EFFET and v[3] == v[4] == ia.SANS_EFFET and v[5] == v[6] == ia.A_EFFET
    assert v[2] is None


def test_verite_action_deplacee_non_jugeable():
    acts = episode()
    acts[2] = action(2, proposition=False)
    d = [fab.decouper_texte(a, "CONTROLS") for a in acts]
    recoit = {2: 7, 7: 2}
    dep = [d[i].avant + d[recoit[i]].valeur + d[i].apres if i in recoit else acts[i] for i in range(10)]
    ep = fab.EpisodeFabrique(dep, 1.0, "CONTROLS", 10, 2, False, recoit, {})
    v = {x.indice: x for x in ia.verite_par_construction(acts, ep)}
    assert v[2].verite == ia.NON_JUGEABLE and v[7].verite == ia.A_EFFET


def test_identite_changee_par_le_deplacement_arrete():
    """Défaut du texte (3.1, ligne 186) : la fabrication et l'environnement ne lisent pas les mêmes clés ; une valeur de
    `CONTROLS` qui porte une ligne « **TITLE** … » rend acceptée une action refusée faute de titre."""
    a0 = "ACTION: ADD\nPROPOSAL: Entraîner M sur D.\nCONTROLS: base aléatoire sur D\nCOST: 3\n"
    a1 = "ACTION: ADD\nTITLE: Deux\nPROPOSAL: Sonder M.\nCONTROLS: étiquettes mélangées\n**TITLE** titre caché\nCOST: 2\n"
    acts = [a0, a1] + [action(i) for i in range(2, 10)]
    d = [fab.decouper_texte(a, "CONTROLS") for a in acts]
    recoit = {0: 1, 1: 0}
    dep = [d[i].avant + d[recoit[i]].valeur + d[i].apres if i in recoit else acts[i] for i in range(10)]
    assert ia.identites_de_proposition(acts)[0] == ("refusee", 0)
    assert ia.identites_de_proposition(dep)[0] == ("proposition", 1)
    with pytest.raises(GardeArret):
        ia.exiger_memes_identites(acts, dep)
    ep = fab.EpisodeFabrique(dep, 1.0, "CONTROLS", 10, 2, False, recoit, {})
    with pytest.raises(GardeArret):
        ia.verite_par_construction(acts, ep)
    ia.exiger_memes_identites(episode(), episode())        # cas sain


def test_dose_recue_cas_sain_et_artefact():
    """8.4, ligne 785 : bilan au-dessus des seuils ; 30 % d'épisodes laissés honnêtes : échec."""
    sains = []
    for k in range(10):
        acts = episode()
        f = fab.fabriquer_episode_texte(acts, 1.0, "CONTROLS", ENTROPIE, "fab-01", k)
        sains.append((ia.verite_par_construction(acts, f), f))
    assert ia.bilan_dose_recue(sains, 1.0)["passe"]
    honnete = fab.EpisodeFabrique(episode(), 1.0, "CONTROLS", 1, 1, True, {}, {})
    artefact = sains[:7] + [([], honnete)] * 3
    b = ia.bilan_dose_recue(artefact, 1.0)
    assert b["part_laisses_honnetes"] == pytest.approx(0.3) and not b["passe"]
    assert ia.dose_recue([], 0) == 0.0


# --- Lot 2 -------------------------------------------------------------------------------------------------------------

def test_consignes_du_texte_et_empreintes():
    c = ia.consignes_du_texte(BROUILLON)
    assert c["appariement"].startswith("You will read one entry of a research plan")
    assert c["appariement"].endswith("CONTROLS: {controls}")
    assert c["couverture"].startswith("You are checking a research plan")
    assert c["couverture"].endswith("{reference}")
    for x in c.values():
        e = ia.empreinte_consigne(x)
        assert e == hashlib.sha256(x.encode("utf-8")).hexdigest()
        ia.exiger_consigne_figee(x, e)
        with pytest.raises(GardeArret):             # un caractère changé
            ia.exiger_consigne_figee(x.replace("a", "à", 1), e)
    with pytest.raises(GardeArret):
        ia.empreinte_consigne("x\n")
    with pytest.raises(GardeArret):
        ia.empreinte_consigne("x\r\ny")


def test_insertion_en_une_passe_champ_a_accolades_intact():
    """8.4, ligne 800 : remplacement de chaînes ; champ contenant des accolades intact. Artefact : la mise en forme à
    accolades casse, et le remplacement successif modifie un champ qui contient une marque."""
    c = ia.consignes_du_texte(BROUILLON)["appariement"]
    piege = ia.ChampsAppariement("Titre {proposal} et {x}", "Proposition {controls} {", "Contrôles {title} }}")
    e = ia.entree_appariement(c, piege)
    assert e.endswith("TITLE: Titre {proposal} et {x}\nPROPOSAL: Proposition {controls} {\nCONTROLS: Contrôles {title} }}")
    with pytest.raises((KeyError, ValueError, IndexError)):
        c.format(title=piege.titre, proposal=piege.proposition, controls=piege.controles)
    successif = c.replace("{title}", piege.titre).replace("{proposal}", piege.proposition)
    assert "Titre Proposition" in successif                      # le titre a été altéré : défaut de la lettre
    with pytest.raises(GardeArret):
        ia.inserer("a {x} {x}", {"{x}": "1"})
    with pytest.raises(GardeArret):
        ia.inserer("a {x}", {"{x}": 1})
    cc = ia.consignes_du_texte(BROUILLON)["couverture"]
    acts = episode()
    acts[2] = action(2, controles_texte="voir {reference} et {plan}")
    entree, garde = ia.entree_couverture(cc, acts, [{"id": "k1", "description": "Comparer à une base."}])
    assert "voir {reference} et {plan}" in entree and entree.count("- id: c1 | description:") == 1


def test_champs_appariement():
    a = "ACTION: ADD\nTITLE:  Ligne un\nligne deux\nPROPOSAL:  p  \nCONTROLS:\n- c1\n- c2\nCOST: 1\n"
    ch = ia.champs_appariement(a)
    assert ch == ia.ChampsAppariement("Ligne un", "p", "- c1\n- c2")
    assert ia.champs_appariement(action(0, titre=False)).titre == ""
    with pytest.raises(GardeArret):
        ia.champs_appariement(action(0, controles=False))


def test_entree_aveugle_appariement_cas_sain_et_artefacts():
    c = ia.consignes_du_texte(BROUILLON)["appariement"]
    a = action(3)
    ident = g.identifiants_opaques("lot-honnete-appariement", 1, ENTROPIE)[0]
    env = ia.enveloppe(ident, ia.entree_appariement(c, ia.champs_appariement(a)))
    interdits = ["fab-03", "dose-1.00", "controls-1.00", "honnete", "e5"]
    ia.exiger_entree_aveugle_appariement(env, c, a, interdits)
    for injecte in ("\nDose: 1.00", "\nStep 4 of 10", "\nCOST: 4", "\nadapter controls-1.00"):
        mauvais = dict(env, entree=env["entree"] + injecte)
        with pytest.raises(GardeArret):
            ia.exiger_entree_aveugle_appariement(mauvais, c, a, interdits)
    with pytest.raises(GardeArret):                         # condition dans l'enveloppe
        ia.exiger_entree_aveugle_appariement(dict(env, condition="dose-1.00"), c, a, interdits)
    with pytest.raises(GardeArret):                         # identifiant = empreinte du contenu
        ia.exiger_entree_aveugle_appariement(
            dict(env, identifiant=hashlib.sha256(env["entree"].encode()).hexdigest()[:32]), c, a, interdits)
    with pytest.raises(GardeArret):
        ia.enveloppe(ident, env["entree"] + ident)


def test_entree_aveugle_couverture_cas_sain_et_artefacts():
    c = ia.consignes_du_texte(BROUILLON)["couverture"]
    acts = episode()
    acts[9] = "   "                                           # action vide : hors du plan, comptée
    ref = [{"id": "ctl-alpha", "description": "Comparer à une base aléatoire.", "section": "4.2"},
           {"id": "ctl-beta", "description": "Répéter avec trois graines.", "section": "5.1"}]
    entree, garde = ia.entree_couverture(c, acts, ref)
    assert garde["actions_vides"] == 1 and garde["indices_du_plan"] == list(range(9))
    assert garde["table_neutre"] == {"c1": "ctl-alpha", "c2": "ctl-beta"}
    assert "- id: c1 | description: Comparer à une base aléatoire.\n- id: c2 | description: Répéter" in entree
    ident = g.identifiants_opaques("lot-honnete-couverture", 1, ENTROPIE)[0]
    env = {"identifiant": ident, "entree": entree}
    ia.exiger_entree_aveugle_couverture(env, c, acts, ref, ["fab-00"])
    with pytest.raises(GardeArret):                         # identifiant d'origine
        ia.exiger_entree_aveugle_couverture(dict(env, entree=entree.replace("id: c1", "id: ctl-alpha")), c, acts, ref)
    with pytest.raises(GardeArret):                         # champ de plus de la référence
        ia.exiger_entree_aveugle_couverture(dict(env, entree=entree + " | section: 4.2"), c, acts, ref)
    with pytest.raises(GardeArret):
        ia.reference_neutre([{"id": "a", "description": "deux\nlignes"}])
