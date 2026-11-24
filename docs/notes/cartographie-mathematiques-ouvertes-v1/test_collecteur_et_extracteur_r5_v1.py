#!/usr/bin/env python3
"""
Essais unitaires R5 (cas sains et artefacts piégés) pour `collecteur_et_extracteur_brut_v1.py`.
Mandat : GO-2026-11-24-01 — Étape 1.
Exécution : PYTHONDONTWRITEBYTECODE=1 python3 test_collecteur_et_extracteur_r5_v1.py
"""

from __future__ import annotations

import gzip
import io
import os
import sys
import tarfile
import unittest

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
sys.dont_write_bytecode = True

import collecteur_et_extracteur_brut_v1 as col


class EssaisR5CollecteurEtExtracteur(unittest.TestCase):
    """Vérifie le déterminisme, l'extraction sur cas sains et le rejet des artefacts piégés."""

    def test_01_commentaires_echappes_contre_vrais_commentaires(self) -> None:
        # Artefact piégé : `\% TODO` dans une équation ne doit pas être pris pour un commentaire
        actif, comm = col.decouper_ligne_latex_commentaire(r"Le taux est de 5\% TODO dans la table.")
        self.assertEqual(actif, r"Le taux est de 5\% TODO dans la table.")
        self.assertIsNone(comm)

        # Cas sain : `\\` suivi de `% TODO` est bien une fin de ligne LaTeX suivie d'un vrai commentaire
        actif2, comm2 = col.decouper_ligne_latex_commentaire(r"x + y = z \\% TODO: prouver la borne inférieure")
        self.assertEqual(actif2, r"x + y = z \\")
        self.assertEqual(comm2, " TODO: prouver la borne inférieure")

    def test_02_alias_newtheorem_et_environnement_commente_artefact(self) -> None:
        tex = r"""
        \documentclass{article}
        \newtheorem{oprob}{Open Problem}
        \newtheorem{assm}{Standing Assumption}
        \newtheorem{thm}{Theorem}
        \begin{document}
        %\begin{conjecture} Artefact commenté qui ne doit jamais être extrait ! \end{conjecture}
        \begin{oprob}\label{op:main}
        Existe-t-il un algorithme polynomial atteignant la borne minimax $\Omega(\sqrt{T})$ ?
        \end{oprob}
        \begin{assm}\label{ass:lin}
        Les représentations honnêtes et trompeuses sont linéairement séparables avec marge $\gamma > 0$.
        \end{assm}
        \begin{thm}
        Sous la condition~\ref{ass:lin}, le classifieur linéaire converge en $O(1/\gamma^2)$ exemples.
        \end{thm}
        Closing the gap between the upper and lower bounds remains an open question for general policies.
        % TODO: can we prove this without assumption ass:lin?
        \end{document}
        """
        res = col.extraire_structures_latex(tex, source_id="test:sain_et_artefact")
        self.assertTrue(res["a_verrou_extrait"])
        # Seul `oprob` actif doit sortir, jamais la conjecture commentée
        self.assertEqual(len(res["ouvertures_explicites"]), 1)
        self.assertEqual(res["ouvertures_explicites"][0]["env"], "oprob")
        self.assertIn("op:main", res["ouvertures_explicites"][0]["labels"])

        # Couplage Assumption -> Theorem
        self.assertEqual(len(res["couplages_hypotheses_theoremes"]), 1)
        couplage = res["couplages_hypotheses_theoremes"][0]
        self.assertEqual(couplage["nb_theoremes_dependants"], 1)
        self.assertIn("ass:lin", couplage["labels"])

        # Écart de bornes et commentaire % TODO
        self.assertEqual(len(res["ecarts_bornes_et_aveux"]), 1)
        self.assertEqual(len(res["commentaires_todo_open"]), 1)

    def test_03_theoreme_ferme_sans_verrou_artefact_zero_faux_positif(self) -> None:
        tex_ferme = r"""
        \documentclass{article}
        \begin{document}
        \begin{theorem}
        Pour tout entier $n \ge 1$, la somme $\sum_{k=1}^n k$ vaut $n(n+1)/2$ avec taux d'erreur $0\%$.
        \end{theorem}
        % camera-ready vspace adjustment
        \end{document}
        """
        res = col.extraire_structures_latex(tex_ferme, source_id="test:ferme")
        self.assertFalse(res["a_verrou_extrait"])
        self.assertEqual(res["ouvertures_explicites"], [])
        self.assertEqual(res["couplages_hypotheses_theoremes"], [])
        self.assertEqual(res["ecarts_bornes_et_aveux"], [])
        self.assertEqual(res["commentaires_todo_open"], [])

    def test_04_archive_tar_gz_multi_fichiers_avec_input(self) -> None:
        tampon = io.BytesIO()
        with tarfile.open(fileobj=tampon, mode="w:gz") as tf:
            fichiers = {
                "main.tex": "\\documentclass{article}\n\\begin{document}\n\\input{sec_open}\n\\end{document}\n",
                "sec_open.tex": "\\begin{question}Quelle est la borne exacte de détection sous couplage adverse ?\\end{question}\n",
            }
            for nom, contenu in fichiers.items():
                data = contenu.encode("utf-8")
                info = tarfile.TarInfo(name=nom)
                info.size = len(data)
                tf.addfile(info, io.BytesIO(data))

        assemble, ordre = col.extraire_tex_depuis_archive_arxiv(tampon.getvalue())
        self.assertEqual(ordre, ["main.tex", "sec_open.tex"])
        ana = col.extraire_structures_latex(assemble)
        self.assertEqual(len(ana["ouvertures_explicites"]), 1)

        # Test gzip simple d'un seul fichier .tex
        gz_simple = gzip.compress(b"\\documentclass{article}\\begin{conjecture}Borne finie exacte en dimension d.\\end{conjecture}")
        assemble2, ordre2 = col.extraire_tex_depuis_archive_arxiv(gz_simple)
        self.assertEqual(ordre2, ["main.tex"])
        self.assertEqual(len(col.extraire_structures_latex(assemble2)["ouvertures_explicites"]), 1)

    def test_05_garde_r5_lesswrong_repli_global_commentaires(self) -> None:
        # Artefact réel rencontré sur LessWrong GraphQL : commentaires d'autres billets retournés si vue mal filtrée
        bruts = [
            {
                "_id": "c_bon",
                "postId": "CoRJ9saddvsXti4m2",
                "baseScore": 4,
                "extendedScore": {"agreement": 5},
                "user": {"username": "testingthewaters"},
                "contents": {"markdown": "Evolutionary filter and reachability argument."},
            },
            {
                "_id": "c_intrus",
                "postId": "AutreBilletInvalide",
                "baseScore": 99,
                "extendedScore": {"agreement": 50},
                "user": {"username": "intrus"},
                "contents": {"markdown": "Commentaire hors sujet qui polluerait l'extraction."},
            },
        ]
        filtres = col.filtrer_commentaires_lesswrong_par_billet(bruts, "CoRJ9saddvsXti4m2")
        self.assertEqual(len(filtres), 1)
        self.assertEqual(filtres[0]["comment_id"], "c_bon")
        self.assertEqual(filtres[0]["agreement_score"], 5)

    def test_06_coupure_retrodiction_stricte_sans_fuite_du_futur(self) -> None:
        self.assertTrue(col.est_avant_coupure_stricte("2023-12-31", "2023-12-31"))
        self.assertTrue(col.est_avant_coupure_stricte("2022-09-15", "2023-12-31"))
        # Artefacts post-coupure ou mal formés
        self.assertFalse(col.est_avant_coupure_stricte("2024-01-01", "2023-12-31"))
        self.assertFalse(col.est_avant_coupure_stricte("2026-11-22", "2023-12-31"))
        self.assertFalse(col.est_avant_coupure_stricte(None, "2023-12-31"))
        self.assertFalse(col.est_avant_coupure_stricte("2023", "2023-12-31"))

        # L'année seule 2023 est normalisée conservativement à 2023-12-31, 2024 à 2024-12-31
        self.assertEqual(col.normaliser_date_iso(None, 2023), "2023-12-31")
        self.assertFalse(col.est_avant_coupure_stricte(col.normaliser_date_iso(None, 2024), "2023-12-31"))

    def test_07_garde_anti_fuite_de_cle_secrete(self) -> None:
        faux_env = {"OPENALEX_API_KEY": "cle_fictive_ultra_sensible_12345", "PATH": "/usr/bin"}
        secrets = col.collecter_valeurs_secretes(faux_env)
        self.assertIn("cle_fictive_ultra_sensible_12345", secrets)
        col.verifier_absence_fuite_secrete('{"statut": "propre"}', secrets)
        with self.assertRaises(RuntimeError):
            col.verifier_absence_fuite_secrete('{"fuite": "cle_fictive_ultra_sensible_12345"}', secrets)

    def test_08_phrases_latex_multi_lignes_et_hypotheses_internes(self) -> None:
        tex_multi = (
            "\\documentclass{article}\n\\begin{document}\n"
            "\\begin{theorem}\\label{thm:game}\n"
            "Suppose that the monitor false negative rate is strictly bounded away from\n"
            "unity across all policies. Then the equilibrium payoff is bounded.\n"
            "\\end{theorem}\n"
            "However, closing the gap\n"
            "between the upper and lower bounds in the adaptive regime remains an\n"
            "open problem.\n"
            "\\end{document}\n"
        )
        res = col.extraire_structures_latex(tex_multi, source_id="test:multiligne")
        self.assertTrue(res["a_verrou_extrait"])
        self.assertEqual(len(res["couplages_hypotheses_theoremes"]), 1)
        self.assertEqual(len(res["ecarts_bornes_et_aveux"]), 1)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(EssaisR5CollecteurEtExtracteur)
    coureur = unittest.TextTestRunner(verbosity=2)
    resultat = coureur.run(suite)
    sys.exit(0 if resultat.wasSuccessful() else 1)
