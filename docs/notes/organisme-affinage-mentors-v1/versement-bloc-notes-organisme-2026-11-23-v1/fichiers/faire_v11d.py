"""Lanceur v11d = v11c (`fe7358b9…`) + correction R1 de la vérification (`contre-lecture-lanceur-v11c-verification-v1.md`).
Usage : python3 faire_v11d.py RACINE"""
import hashlib, sys
from pathlib import Path
racine = Path(sys.argv[1])
def r(s, a, b, n=1):
    assert s.count(a) == n, (s.count(a), a[:100]); return s.replace(a, b)
src = (racine / "scripts/lancer_course_affinage_mentors_v11c.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode()).hexdigest() == "fe7358b93fa00648c2e4612846789895d809d534c9e3ff8ebf10f33654175548"
src = r(src, '#!/usr/bin/env python3\n"""Lanceur v11c (dérivé du lanceur v11b,', '''#!/usr/bin/env python3
"""Lanceur v11d (dérivé du lanceur v11c, `fe7358b9…`, par remplacements exacts ; v11, v11b et v11c restent en place, R12).

Seul changement (régression R1 de la vérification des corrections du v11c, `course-v11/contre-lecture-lanceur-v11c-verification-v1.md`,
`525dc158…`) : l'essai à blanc écrit pour la clé LUC la ligne que `verifier_ligne_luc` exige (`solde_non_lu` vrai, `reference`
GO-2026-11-22-124, aucun montant) ; en v11c, il écrivait un solde et une recharge, refusés en moteur simulé aussi.

Texte du lanceur v11c :

Lanceur v11c (dérivé du lanceur v11b,''')
src = r(src, 'VERSION = "lancer_course_affinage_mentors_v11c"', 'VERSION = "lancer_course_affinage_mentors_v11d"')
src = r(src, '''                           **{CLE_CLAUDE: {"solde_console_usd": 0.0, "source": "essai à blanc : aucune lecture réelle",
                                           "recharge_declaree_usd": 100.0, "recharge_source": "essai à blanc : valeur factice"}}),''',
        '''                           **{CLE_CLAUDE: {"solde_non_lu": True, "reference": REFERENCE_LUC_SANS_SOLDE,  # v11d, R1
                                           "source": "essai à blanc"}}),''')
SHA_CONF = hashlib.sha256((racine / "docs/notes/organisme-affinage-mentors-v1/course-v11/configuration-course-affinage-mentors-v11d.json").read_bytes()).hexdigest()
src = r(src, '"configuration": (f"{COURSE}/configuration-course-affinage-mentors-v11c.json", "7615a31c8a5ea7a569368847323812685ce33abb929770e4a3f100355a84cb36"),',
        f'"configuration": (f"{{COURSE}}/configuration-course-affinage-mentors-v11d.json", "{SHA_CONF}"),  # v11d : notes de la commande v2, plafond inerte retiré')
src = r(src, "GO-2026-11-22-124, aucun montant) ; en v11c, il écrivait un solde et une recharge, refusés en moteur simulé aussi.\n",
        "GO-2026-11-22-124, aucun montant) ; en v11c, il écrivait un solde et une recharge, refusés en moteur simulé aussi.\n"
        "Configuration v11d (`configuration-course-affinage-mentors-v11d.json`) : notes `changements_v11.carbon` et `.argon` qui citent\n"
        "`commande_gemini_flux_v2.py` ; `relais_persistants_v4.plafond_relais_claude_usd` (150, lu par personne) retiré.\n")
(racine / "scripts/lancer_course_affinage_mentors_v11d.py").write_text(src, encoding="utf-8")
print("v11d écrit")
