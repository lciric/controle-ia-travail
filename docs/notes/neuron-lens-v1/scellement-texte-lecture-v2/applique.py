import sys, difflib, hashlib
D = "/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/lentilles-v2-candidat/"
src = open(D + "brouillon6.md", encoding="utf-8").read()

R1_AV = ("principale : <<LIGNE_D_ACCORD_DES_NOEUDS_N12_ET_N17>> (cherchée par le rédacteur du brouillon 6 dans "
         "`registres/go.md` et")
R1_AP = ("principale : ligne **GO-2026-11-20-18** de `registres/go.md` (branche principale), dont l'objet est « Lentilles, "
         "texte de lecture v2 : nœuds N12 et N17 tranchés selon les recommandations, et départ du rédacteur du brouillon 6. N12 (a) : mot "
         "de Lazar postérieur à l'avertissement de l'écart mesuré (ligne NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS). N17 (a), aux deux "
         "paliers : ce texte vaut le texte de lecture neuf exigé par le critère d'identité, sans addendum de recopie. » ; mot relu à la "
         "source par la session principale (événement `3961f2f8-7eb1-48a4-974a-94796f174168`, 2026-11-20T05:20:51Z) ; inscrite par la "
         "ligne R-4104 de `registres/decisions.md` le **2026-11-20 à 05:34:13Z**, heure que recopie la pièce de `GO-LENTILLES-BBIS-V2` "
         "(« Lignes de registre » : « ligne d'accord GO-2026-11-20-18, 2026-11-20T05:34:13Z ») (cherchée par le rédacteur du brouillon 6 dans "
         "`registres/go.md` et")

R2_AV = ("il est donc consigné ici comme **mot rapporté** par la session des lentilles et sa note, citée\n"
         "  seule ; il ouvrait un travail sans dépense ; la session principale peut le consigner, comme elle l'a fait à la ligne\n"
         "  R-3994 pour le mot du brouillon 4 ; vérification des corrections du brouillon 5, M6)")
R2_AP = ("il était donc consigné ici comme mot rapporté ; **il a été consigné depuis** par la session principale, qui l'a relu à\n"
         "  la source (événement `a8e8cd06-decf-403f-911c-0664833286ff`, 2026-11-19T23:46:53Z) : ligne **GO-2026-11-20-17** de\n"
         "  `registres/go.md`, « départ du rédacteur Fable du brouillon 5 sans attendre les défauts de N12 et N17 », inscrite par la ligne\n"
         "  R-4104 de `registres/decisions.md` (2026-11-20T05:34:13Z) ; vérification des corrections du brouillon 5, M6)")

out = src
for nom, av, ap in (("R1", R1_AV, R1_AP), ("R2", R2_AV, R2_AP)):
    n = out.count(av)
    print(nom, "occurrences de l'avant :", n)
    if n != 1:
        print("ARRET"); sys.exit(1)
    out = out.replace(av, ap)

open(D + "lecture-sondes-bbis-par-lentilles-v2-candidat.md", "w", encoding="utf-8").write(out)
diff = "".join(difflib.unified_diff(src.splitlines(True), out.splitlines(True),
      "brouillon6", "candidat", n=0))
open(D + "differentiel-brouillon6-candidat.diff", "w", encoding="utf-8").write(diff)

# controle : le differentiel ne porte que sur les deux couples
import re
reconstruit = src.replace(R1_AV, R1_AP).replace(R2_AV, R2_AP)
print("candidat == brouillon6 avec les deux couples seuls :", reconstruit == out)
print("hunks :", len(re.findall(r"^@@", diff, re.M)))
for l in diff.splitlines():
    if l.startswith("@@"): print(l)
print("marqueur restant :", "<<LIGNE_D_ACCORD_DES_NOEUDS_N12_ET_N17>>" in out)

# bloc separable
deb = None
for nom in ("brouillon6.md",):
    pass
