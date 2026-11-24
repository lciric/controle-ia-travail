"""Essais du programme d'application du complément d'erratum de la demande 27, v3 (R5 : cas sain et artefacts,
un essai par garde, dont les trois défauts majeurs de la contre-lecture de la v1)."""
import importlib.util
import os
import pathlib

import pytest

CHEMIN = (pathlib.Path(__file__).resolve().parents[1] / 'docs/notes/dossier-entretien-2026-12-01-v1'
          / 'application-a-blanc-demande-27-v1/appliquer_complement_demande_27_v3.py')
spec = importlib.util.spec_from_file_location('complement27v3', CHEMIN)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

PROG = 'programme-controle-ia-v3-application-a-blanc.md'
NOTE = 'note-problematiques-programme-v2-application-a-blanc.md'
ORIG = 'Titre.\nLe lemme tient.\nLa marge H6 reste.\n'


def fichiers():
    return {f'B/{PROG}': ORIG, f'B/{NOTE}': 'Note.\n', './docs/table.md': 'ligne A : garantie (théorème)\n'}


def lecteur(f):
    def lire(p):
        if p not in f:
            raise m.Echec(f'lecture impossible : {p}')
        return f[p]
    return lire


def bloc(ident, ancien, nouveau):
    return f'**{ident}.** ANCIEN : « {ancien} »\nNOUVEAU : « {nouveau} »\nRaison : essai.'


def complement(*blocs, cible=f'docs/notes/x/{PROG}'):
    return f'Cible : `{cible}`\n\n' + '\n\n'.join(blocs) + '\n'


def app(c, f=None, **k):
    return m.appliquer(c, 'B', lecteur(f or fichiers()), **k)


# Cas sain
def test_cas_sain_multiligne_guillemets_imbriques_table_finale():
    c = complement(bloc('J-1', 'Le lemme tient.\nLa marge', 'Le « lemme » est retiré.\nLa marge'),
                   bloc('O-1', 'H6 reste.', 'H6 reste (retirée par N-077).'))
    c += '\nCible : docs/table.md\n\n' + bloc('E2-1', 'garantie (théorème)', 'à démontrer')
    c += '\n\n## Décompte\n\n| préfixe | n |\n|---|---|\n| J | 1 |\n'
    f = fichiers()
    textes, rapport = app(c, f, attendu=3)
    assert textes[PROG] == 'Titre.\nLe « lemme » est retiré.\nLa marge H6 reste (retirée par N-077).\n'
    assert f['./docs/table.md'] == 'ligne A : garantie (théorème)\n' and len(rapport) == 3


def test_cible_entre_deux_blocs():
    c = complement(bloc('J-1', 'Titre.', 'T.')) + f'\nCible : {NOTE}\n\n' + bloc('O-1', 'Note.', 'N.') + '\n'
    textes, _ = app(c)
    assert textes[NOTE] == 'N.\n' and textes[PROG].startswith('T.')


# Défaut 1 : blocs ignorés en silence, décompte
@pytest.mark.parametrize('tete', ['**J-2.** ANCIEN: « Titre. »', '**j-3.** ANCIEN : « Titre. »'])
def test_entete_hors_motif_refuse(tete):
    c = complement(bloc('J-1', 'Le lemme tient.', 'x'), tete + '\nNOUVEAU : « y »\nRaison : essai.')
    with pytest.raises(m.Echec, match='en-têtes de bloc'):
        app(c)


def test_attendu_different_refuse():
    with pytest.raises(m.Echec, match='attendus'):
        app(complement(bloc('J-1', 'Titre.', 'T.')), attendu=2)


# Défaut 2 : cible
def test_cible_en_gras_refusee():
    c = complement(bloc('J-1', 'Titre.', 'T.')) + f'\n**Cible :** `{NOTE}`\n\n' + bloc('O-1', 'Note.', 'N.') + '\n'
    with pytest.raises(m.Echec, match='motif strict'):
        app(c)


def test_cible_avec_commentaire_refusee():
    with pytest.raises(m.Echec, match='motif strict'):
        app(f'Cible : `{PROG}` (programme)\n\n' + bloc('J-1', 'Titre.', 'T.'))


def test_cible_absente_refuse():
    with pytest.raises(m.Echec, match='Cible'):
        app(bloc('J-1', 'Titre.', 'T.'))


def test_cible_inconnue_refusee():
    with pytest.raises(m.Echec, match='hors des quatre brouillons'):
        app(complement(bloc('J-1', 'Titre.', 'T.'), cible='docs/autre.md'))


# Défaut 3 : ANCIEN pris dans un texte inséré
def test_ancien_insere_par_entree_precedente_refuse():
    c = complement(bloc('J-1', 'Titre.', 'ZZZ'), bloc('O-1', 'ZZZ', 'W'))
    with pytest.raises(m.Echec, match="brouillon d'origine"):
        app(c)


# Défaut 4 : préfixes
def test_prefixe_inconnu_refuse():
    with pytest.raises(m.Echec, match='préfixe X'):
        app(complement(bloc('X-1', 'Titre.', 'T.')))


def test_prefixe_programme_seul_sur_note_refuse():
    with pytest.raises(m.Echec, match='ne vise que le programme'):
        app(complement(bloc('S-1', 'Note.', 'N.'), cible=NOTE))


# Défaut 5 : lectures
def test_cible_e2_absente_refuse():
    c = 'Cible : docs/absente.md\n\n' + bloc('E2-1', 'x', 'y')
    with pytest.raises(m.Echec, match='lecture impossible'):
        app(c)


def test_lire_fichier_absent_echec(tmp_path):
    with pytest.raises(m.Echec, match='lecture impossible'):
        m.lire_fichier(str(tmp_path / 'absent.md'))


# Défaut 6 : NOUVEAU ou Raison internes
def test_nouveau_interne_refuse():
    c = complement('**J-1.** ANCIEN : « Titre. »\nNOUVEAU : « a\nNOUVEAU : b »\nRaison : essai.')
    with pytest.raises(m.Echec, match='lignes NOUVEAU'):
        app(c)


def test_raison_interne_refusee():
    c = complement('**J-1.** ANCIEN : « Titre. »\nNOUVEAU : « a\nRaison : b »\nRaison : essai.')
    with pytest.raises(m.Echec, match='lignes Raison'):
        app(c)


# Défaut 8 : autres gardes
def test_aucun_bloc_refuse():
    with pytest.raises(m.Echec, match='aucun bloc'):
        app('Cible : x\n\nrien\n')


def test_nouveau_absent_refuse():
    with pytest.raises(m.Echec, match='lignes NOUVEAU'):
        app(complement('**J-1.** ANCIEN : « Titre. »\nRaison : essai.'))


def test_raison_absente_refusee():
    with pytest.raises(m.Echec, match='lignes Raison'):
        app(complement('**J-1.** ANCIEN : « Titre. »\nNOUVEAU : « T. »'))


def test_guillemets_manquants_refuse():
    with pytest.raises(m.Echec, match='guillemets'):
        app(complement('**J-1.** ANCIEN : Titre.\nNOUVEAU : « x »\nRaison : essai.'))


def test_ancien_absent_refuse():
    with pytest.raises(m.Echec, match="brouillon d'origine"):
        app(complement(bloc('J-1', 'texte inexistant', 'x')))


def test_ancien_double_refuse():
    f = fichiers()
    f[f'B/{PROG}'] = ORIG + 'Le lemme tient.\n'
    with pytest.raises(m.Echec, match='2 fois'):
        app(complement(bloc('J-1', 'Le lemme tient.', 'y')), f)


def test_chevauchement_refuse():
    c = complement(bloc('J-1', 'Le lemme tient.', 'Le lemme cède.'), bloc('O-1', 'Le lemme tient.', 'w'))
    with pytest.raises(m.Echec, match='0 fois'):
        app(c)


def test_identifiant_double_refuse():
    with pytest.raises(m.Echec, match='double'):
        app(complement(bloc('J-1', 'Titre.', 'T.'), bloc('J-1', 'Le lemme tient.', 'z')))


def test_garde_post_remplacement():
    # NOUVEAU qui, accolé au texte suivant, recrée l'ANCIEN.
    f = fichiers()
    f[f'B/{PROG}'] = 'aab'
    with pytest.raises(m.Echec, match='encore présent'):
        app(complement(bloc('J-1', 'ab', 'b')), f)


def test_ancien_contenu_dans_nouveau_admis():
    textes, _ = app(complement(bloc('J-1', 'tient', 'tient tient')))
    assert 'tient tient' in textes[PROG]


def test_e2_absent_ou_double_refuse():
    f = fichiers()
    with pytest.raises(m.Echec, match='0 fois'):
        app('Cible : docs/table.md\n\n' + bloc('E2-1', 'introuvable', 'y'), f)
    f['./docs/table.md'] = 'x x'
    with pytest.raises(m.Echec, match='2 fois'):
        app('Cible : docs/table.md\n\n' + bloc('E2-1', 'x', 'y'), f)


def test_e2_sur_brouillon_refuse():
    with pytest.raises(m.Echec, match='second erratum'):
        app(complement(bloc('E2-1', 'Titre.', 'T.')))


# Défaut 7 et main()
def test_main_echec_code_1_et_rien_ecrit(tmp_path):
    (tmp_path / 'B').mkdir()
    (tmp_path / 'B' / PROG).write_text(ORIG, encoding='utf-8')
    c = tmp_path / 'c.md'
    c.write_text(complement(bloc('J-1', 'inexistant', 'x')), encoding='utf-8')
    sortie = tmp_path / 'S'
    assert m.main(['p', str(c), str(tmp_path / 'B'), str(sortie)]) == 1
    assert not sortie.exists()
    assert m.main(['p', str(c)]) == 1


def test_main_sain_ecrit_sans_tmp(tmp_path):
    (tmp_path / 'B').mkdir()
    (tmp_path / 'B' / PROG).write_text(ORIG, encoding='utf-8')
    c = tmp_path / 'c.md'
    c.write_text(complement(bloc('J-1', 'Titre.', 'T.')), encoding='utf-8')
    sortie = tmp_path / 'S'
    assert m.main(['p', str(c), str(tmp_path / 'B'), str(sortie), '--attendu=1']) == 0
    assert os.listdir(sortie) == ['programme-controle-ia-v3-complement-applique.md']


def test_main_attendu_non_entier(tmp_path):
    c = tmp_path / 'c.md'
    c.write_text(complement(bloc('J-1', 'Titre.', 'T.')), encoding='utf-8')
    assert m.main(['p', str(c), str(tmp_path), str(tmp_path / 'S'), '--attendu=abc']) == 1


def test_ecriture_partielle_nettoyee(tmp_path, monkeypatch):
    vrai_open = open
    appels = []

    def open_fautif(chemin, *a, **k):
        f = vrai_open(chemin, *a, **k)
        appels.append(chemin)
        if len(appels) == 2:
            f.close()
            raise OSError('disque plein')
        return f
    monkeypatch.setattr('builtins.open', open_fautif)
    with pytest.raises(OSError):
        m.ecrire_atomique({PROG: 'a', NOTE: 'b'}, str(tmp_path))
    monkeypatch.undo()
    assert [p for p in os.listdir(tmp_path)] == []
