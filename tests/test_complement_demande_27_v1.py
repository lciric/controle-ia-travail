"""Essais du programme d'application du complément d'erratum de la demande 27 (R5 : cas sain et artefacts)."""
import importlib.util
import pathlib

import pytest

CHEMIN = (pathlib.Path(__file__).resolve().parents[1] / 'docs/notes/dossier-entretien-2026-12-01-v1'
          / 'application-a-blanc-demande-27-v1/appliquer_complement_demande_27_v1.py')
spec = importlib.util.spec_from_file_location('complement27', CHEMIN)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

PROG = 'programme-controle-ia-v3-application-a-blanc.md'
FICHIERS = {
    f'B/{PROG}': 'Titre.\nLe lemme tient.\nLa marge H6 reste.\n',
    'docs/table.md': 'ligne A : garantie (théorème)\n',
}


def lire(p):
    return FICHIERS[p]


def complement(*blocs, cible=f'docs/notes/x/{PROG}'):
    return f'Cible : `{cible}`\n\n' + '\n\n'.join(blocs) + '\n'


def bloc(ident, ancien, nouveau):
    return f'**{ident}.** ANCIEN : « {ancien} »\nNOUVEAU : « {nouveau} »\nRaison : essai.'


def test_cas_sain_applique_dans_l_ordre():
    c = complement(bloc('J-1', 'Le lemme tient.', 'Le lemme est retiré.'),
                   bloc('O-1', 'La marge H6 reste.', 'La marge H6 reste (retirée par N-077).'))
    c += '\nCible : docs/table.md\n\n' + bloc('E2-1', 'garantie (théorème)', 'à démontrer') + '\n'
    textes, rapport = m.appliquer(c, 'B', lire)
    assert textes[PROG] == 'Titre.\nLe lemme est retiré.\nLa marge H6 reste (retirée par N-077).\n'
    assert 'docs/table.md' not in textes and FICHIERS['docs/table.md'].startswith('ligne A')
    assert len(rapport) == 3


def test_ancien_absent_refuse():
    with pytest.raises(m.Echec, match='0 fois'):
        m.appliquer(complement(bloc('J-1', 'texte inexistant', 'x')), 'B', lire)


def test_ancien_double_refuse():
    FICHIERS[f'B/{PROG}'] += 'Le lemme tient.\n'
    try:
        with pytest.raises(m.Echec, match='2 fois'):
            m.appliquer(complement(bloc('J-1', 'Le lemme tient.', 'y')), 'B', lire)
    finally:
        FICHIERS[f'B/{PROG}'] = 'Titre.\nLe lemme tient.\nLa marge H6 reste.\n'


def test_identifiant_double_refuse():
    c = complement(bloc('J-1', 'Titre.', 'T.'), bloc('J-1', 'Le lemme tient.', 'z'))
    with pytest.raises(m.Echec, match='double'):
        m.appliquer(c, 'B', lire)


def test_chevauchement_refuse():
    c = complement(bloc('J-1', 'Le lemme tient.', 'Le lemme cède.'), bloc('O-1', 'Le lemme tient.', 'w'))
    with pytest.raises(m.Echec, match='0 fois'):
        m.appliquer(c, 'B', lire)


def test_guillemets_manquants_refuse():
    c = complement('**J-1.** ANCIEN : Le lemme tient.\nNOUVEAU : « x »\nRaison : essai.')
    with pytest.raises(m.Echec, match='guillemets'):
        m.appliquer(c, 'B', lire)


def test_cible_absente_refuse():
    with pytest.raises(m.Echec, match='Cible'):
        m.appliquer(bloc('J-1', 'Titre.', 'T.'), 'B', lire)


def test_second_erratum_sur_brouillon_refuse():
    with pytest.raises(m.Echec, match='second erratum'):
        m.appliquer(complement(bloc('E2-1', 'Titre.', 'T.')), 'B', lire)


def test_ancien_contenu_dans_nouveau_admis():
    c = complement(bloc('J-1', 'tient', 'tient tient'))
    textes, _ = m.appliquer(c, 'B', lire)  # ANCIEN contenu dans le NOUVEAU : admis
    assert 'tient tient' in textes[PROG]
