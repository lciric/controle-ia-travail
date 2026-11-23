p = '/home/user/controle-ia-travail/.claude/worktrees/agent-a89be1d2701a117b9/tests/test_commande_lecture_v3.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert s.count(a) == 1, a
    s = s.replace(a, b)


rep('''        cl3.commit_v3_epingle(_reg(*lignes))


# --- le montage complet''', '''        cl3.commit_v3_epingle(_reg(*lignes))


@pytest.mark.parametrize("variante", ["accent_decompose", "espace_insecable", "barre_verticale"])
def test_d_prime_ligne_saine_plus_une_variante_normalisee_deux_candidates(variante):
    """Constat 1 de la contre-lecture du code : une ligne saine, plus une copie que seule la normalisation des candidates
    reconnaît (forme décomposée, espace insécable, « | » en tête) : deux candidates, refus « une et une seule »."""
    sain = epinglage("3" * 40)
    autre = {"accent_decompose": unicodedata.normalize("NFD", sain),
             "espace_insecable": sain.replace("(barreau 5) :", "(barreau 5)\\u00a0:"),
             "barre_verticale": "| " + sain}[variante]
    assert autre != sain and cl3.commit_v3_epingle(_reg(sain)) == "3" * 40
    with pytest.raises(GardeArret, match="une et une seule"):
        cl3.commit_v3_epingle(_reg(sain, autre))
    with pytest.raises(GardeArret, match="une et une seule"):
        cl3.commit_v3_epingle(_reg(autre, sain))


def test_amorce_embarquee_sha256_deux_segments_base64_refus():
    """Constat 2 de la contre-lecture du code : une commande à deux segments « base64 -d », dont l'un vise un autre
    fichier : refus (C12) ; le témoin à un seul segment rend l'empreinte corrigée."""
    corrigee = base64.b64encode(cl3.amorce_corrigee((RACINE / rv.AMORCE).read_bytes())).decode()
    sain = f'x --args -c "echo {corrigee} | base64 -d > /root/amorce_b5f_lecture_v1.sh && bash /root/amorce_b5f_lecture_v1.sh"'
    assert cl3.amorce_embarquee_sha256(sain) == CORRIGEE
    for deux in (sain + " && echo eA== | base64 -d > /root/autre.sh",
                 f'x --args -c "echo eA== | base64 -d > /root/autre.sh && echo {corrigee} | base64 -d > '
                 '/root/amorce_b5f_lecture_v1.sh"'):
        with pytest.raises(GardeArret, match="un et un seul segment"):
            cl3.amorce_embarquee_sha256(deux)


# --- le montage complet''')
rep('@pytest.mark.parametrize("segment", ["figee", "illisible", "deux"])',
    '@pytest.mark.parametrize("segment", ["figee", "illisible", "deux", "deux_lignes"])')
rep('''/root/amorce_b5f_lecture_v1.sh"}[segment]
    faux = tmp_path / "faux-python"
    faux.write_text(f"#!/usr/bin/env bash\\necho 'GO_ID=GO-2026-11-24-01 vastai create instance 1 --args -c \\"{s}\\"'\\n")''',
    '''/root/amorce_b5f_lecture_v1.sh",
         "deux_lignes": f"echo {corrigee} | base64 -d > /root/amorce_b5f_lecture_v1.sh"}[segment]
    faux = tmp_path / "faux-python"
    faux.write_text(f"#!/usr/bin/env bash\\necho 'GO_ID=GO-2026-11-24-01 vastai create instance 1 --args -c \\"{s}\\"'\\n"
                    + ("echo 'seconde ligne'\\n" if segment == "deux_lignes" else ""))''')
open(p, 'w', encoding='utf-8').write(s)
