"""Inventaire en lecture seule d'un dossier : chemin, taille, empreinte sha256.

Bibliotheque standard seule. Ne suit aucun lien. N'ecrit rien dans le dossier
inventorie. Le contenu des fichiers n'est lu que pour calculer l'empreinte.

Usage :
  python3 -I -B inventorier_dossier_v1.py DOSSIER SORTIE_TSV_GZ \\
      SORTIE_RESUME_JSON SORTIE_DOSSIERS_TSV_GZ
  python3 -I -B inventorier_dossier_v1.py --verifier-tailles DOSSIER RESUME_JSON

Le second TSV (comptes par dossier, gzip deterministe de meme) a une ligne
d'en-tete commencant par #, puis une ligne par dossier (racine notee \".\") :
  chemin_dossier<TAB>fichiers_directs<TAB>taille_directe_octets
  <TAB>fichiers_recursifs<TAB>taille_recursive_octets

Format du TSV (une ligne par entree, UTF-8, fin de ligne \\n) :
  - fichiers ordinaires : chemin_relatif<TAB>taille_en_octets<TAB>sha256
    tries par chemin en octets UTF-8 ;
  - puis, a part, les liens symboliques et fichiers speciaux, tries de meme :
    #LIEN<TAB>chemin_relatif<TAB>cible
    #SPECIAL<TAB>chemin_relatif<TAB>type
    #ERREUR<TAB>chemin_relatif<TAB>message
Les octets \\, TAB, saut de ligne et retour chariot d'un chemin sont echappes
(\\\\, \\t, \\n, \\r) ; un octet non decodable en UTF-8 s'ecrit \\xHH.

Le second mode refait un parcours par lstat seul (aucun contenu lu) et compare
le nombre de fichiers, de dossiers, de liens et speciaux et la taille totale au
resume ; il n'ecrit rien.
"""

import datetime
import gzip
import hashlib
import io
import json
import os
import stat
import sys

TAMPON = 4 * 1024 * 1024
PARCOURS_DOSSIERS = []  # chemins relatifs des dossiers vus ("" = racine)


def gzip_deterministe(octets):
    tampon = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=tampon, mtime=0,
                       compresslevel=9) as gz:
        gz.write(octets)
    return tampon.getvalue()


def comptes_par_dossier(dossiers, fichiers_tailles):
    """Rend les lignes TSV par dossier, triees par chemin en octets.

    Colonnes : chemin_dossier (\".\" = racine), fichiers_directs,
    taille_directe_octets, fichiers_recursifs, taille_recursive_octets.
    """
    direct = {d: [0, 0] for d in dossiers}
    recur = {d: [0, 0] for d in dossiers}
    for rel, taille in fichiers_tailles:
        parent = os.path.dirname(rel)
        direct[parent][0] += 1
        direct[parent][1] += taille
        anc = parent
        while True:
            recur[anc][0] += 1
            recur[anc][1] += taille
            if anc == b"":
                break
            anc = os.path.dirname(anc)
    lignes = ["#chemin_dossier\tfichiers_directs\ttaille_directe_octets\t"
              "fichiers_recursifs\ttaille_recursive_octets\n"]
    for d in sorted(dossiers):
        lignes.append("%s\t%d\t%d\t%d\t%d\n" % (
            echapper(d) if d else ".", direct[d][0], direct[d][1],
            recur[d][0], recur[d][1]))
    return "".join(lignes).encode("utf-8")


def maintenant():
    return datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%S.%fZ")


def echapper(chemin_octets):
    def propre(part):
        return part.replace("\\", "\\\\").replace("\t", "\\t").replace(
            "\n", "\\n").replace("\r", "\\r")

    morceaux = []
    reste = chemin_octets
    while reste:
        try:
            morceaux.append(propre(reste.decode("utf-8")))
            break
        except UnicodeDecodeError as e:
            morceaux.append(propre(reste[:e.start].decode("utf-8")))
            morceaux.append("\\x%02x" % reste[e.start])
            reste = reste[e.start + 1:]
    return "".join(morceaux)


def type_special(mode):
    if stat.S_ISFIFO(mode):
        return "fifo"
    if stat.S_ISSOCK(mode):
        return "socket"
    if stat.S_ISCHR(mode):
        return "peripherique_caractere"
    if stat.S_ISBLK(mode):
        return "peripherique_bloc"
    return "inconnu_%o" % stat.S_IFMT(mode)


def parcourir(racine_octets):
    """Rend (fichiers, dossiers, autres) ; chemins relatifs en octets.

    fichiers : liste de (rel, chemin_absolu, st) ; autres : (rel, kind, info).
    """
    fichiers = []
    autres = []
    nb_dossiers = 0
    PARCOURS_DOSSIERS[:] = [b""]
    pile = [b""]
    while pile:
        rel_dossier = pile.pop()
        abs_dossier = os.path.join(racine_octets, rel_dossier) if rel_dossier \
            else racine_octets
        try:
            with os.scandir(abs_dossier) as it:
                entrees = list(it)
        except OSError as e:
            autres.append((rel_dossier or b".", "ERREUR",
                           "scandir: %s" % e.strerror))
            continue
        for ent in entrees:
            rel = os.path.join(rel_dossier, ent.name) if rel_dossier \
                else ent.name
            try:
                st = os.lstat(ent.path)
            except OSError as e:
                autres.append((rel, "ERREUR", "lstat: %s" % e.strerror))
                continue
            m = st.st_mode
            if stat.S_ISLNK(m):
                try:
                    cible = os.readlink(ent.path)
                except OSError as e:
                    cible = b"?(" + str(e.strerror).encode() + b")"
                autres.append((rel, "LIEN", echapper(cible)))
            elif stat.S_ISDIR(m):
                nb_dossiers += 1
                PARCOURS_DOSSIERS.append(rel)
                pile.append(rel)
            elif stat.S_ISREG(m):
                fichiers.append((rel, ent.path, st))
            else:
                autres.append((rel, "SPECIAL", type_special(m)))
    fichiers.sort(key=lambda t: t[0])
    autres.sort(key=lambda t: (t[0], t[1]))
    return fichiers, nb_dossiers, autres


def empreinte_fichier(chemin):
    h = hashlib.sha256()
    lus = 0
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(
        os, "O_NOATIME", 0)
    try:
        fd = os.open(chemin, flags)
    except PermissionError:
        # O_NOATIME refuse si l'on n'est pas proprietaire
        fd = os.open(chemin, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    with os.fdopen(fd, "rb", buffering=0) as f:
        while True:
            bloc = f.read(TAMPON)
            if not bloc:
                break
            h.update(bloc)
            lus += len(bloc)
    return h.hexdigest(), lus


def inventorier(dossier, sortie_gz, sortie_json, sortie_dossiers_gz):
    debut = maintenant()
    racine = os.fsencode(os.path.abspath(dossier))
    if not os.path.isdir(racine) or os.path.islink(racine):
        print("erreur: dossier absent ou lien: %s" % dossier, file=sys.stderr)
        return 2
    fichiers, nb_dossiers, autres = parcourir(racine)
    dossiers = list(PARCOURS_DOSSIERS)
    lignes = []
    tailles = []
    taille_totale = 0
    modifies = []
    erreurs = []
    for rel, chemin, st_avant in fichiers:
        try:
            sha, lus = empreinte_fichier(chemin)
            st_apres = os.lstat(chemin)
        except OSError as e:
            erreurs.append((rel, "ERREUR", "lecture: %s" % e.strerror))
            continue
        if (st_apres.st_size != st_avant.st_size
                or st_apres.st_mtime_ns != st_avant.st_mtime_ns
                or lus != st_avant.st_size):
            modifies.append(echapper(rel))
        taille_totale += lus
        tailles.append((rel, lus))
        lignes.append("%s\t%d\t%s\n" % (echapper(rel), lus, sha))
    autres_tous = sorted(autres + erreurs, key=lambda t: (t[0], t[1]))
    nb_liens = sum(1 for a in autres_tous if a[1] == "LIEN")
    nb_speciaux = sum(1 for a in autres_tous if a[1] == "SPECIAL")
    nb_erreurs = sum(1 for a in autres_tous if a[1] == "ERREUR")
    for rel, kind, info in autres_tous:
        lignes.append("#%s\t%s\t%s\n" % (kind, echapper(rel), info))
    tsv = "".join(lignes).encode("utf-8")
    sha_tsv = hashlib.sha256(tsv).hexdigest()
    gz_octets = gzip_deterministe(tsv)
    sha_gz = hashlib.sha256(gz_octets).hexdigest()
    tsv_d = comptes_par_dossier(dossiers, tailles)
    sha_tsv_d = hashlib.sha256(tsv_d).hexdigest()
    gz_d = gzip_deterministe(tsv_d)
    sha_gz_d = hashlib.sha256(gz_d).hexdigest()
    with open(sortie_gz, "xb") as f:
        f.write(gz_octets)
    with open(sortie_dossiers_gz, "xb") as f:
        f.write(gz_d)
    fin = maintenant()
    resume = {
        "chemin_dossier": os.fsdecode(racine),
        "debut_utc": debut,
        "fin_utc": fin,
        "nombre_fichiers": len(lignes) - len(autres_tous),
        "nombre_dossiers_hors_racine": nb_dossiers,
        "taille_totale_octets": taille_totale,
        "nombre_liens_symboliques": nb_liens,
        "nombre_fichiers_speciaux": nb_speciaux,
        "nombre_erreurs": nb_erreurs,
        "fichiers_modifies_pendant_lecture": modifies,
        "sha256_tsv_non_compresse": sha_tsv,
        "taille_tsv_non_compresse_octets": len(tsv),
        "sha256_tsv_gz": sha_gz,
        "taille_tsv_gz_octets": len(gz_octets),
        "nom_tsv_gz": os.path.basename(sortie_gz),
        "comptes_par_dossier": {
            "nom_tsv_gz": os.path.basename(sortie_dossiers_gz),
            "nombre_lignes_dossiers_racine_comprise": len(dossiers),
            "sha256_tsv_non_compresse": sha_tsv_d,
            "taille_tsv_non_compresse_octets": len(tsv_d),
            "sha256_tsv_gz": sha_gz_d,
            "taille_tsv_gz_octets": len(gz_d),
        },
        "programme": "inventorier_dossier_v1.py",
    }
    with open(sortie_json, "x", encoding="utf-8") as f:
        json.dump(resume, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    print("fichiers=%d dossiers=%d taille=%d liens=%d speciaux=%d erreurs=%d "
          "modifies_pendant_lecture=%d" % (
              resume["nombre_fichiers"], nb_dossiers, taille_totale, nb_liens,
              nb_speciaux, nb_erreurs, len(modifies)))
    return 0


def verifier_tailles(dossier, resume_json):
    with open(resume_json, encoding="utf-8") as f:
        resume = json.load(f)
    racine = os.fsencode(os.path.abspath(dossier))
    fichiers, nb_dossiers, autres = parcourir(racine)
    taille = sum(st.st_size for _, _, st in fichiers)
    nb_liens = sum(1 for a in autres if a[1] == "LIEN")
    nb_speciaux = sum(1 for a in autres if a[1] == "SPECIAL")
    mtime_max = max((st.st_mtime_ns for _, _, st in fichiers), default=0)
    ok = (len(fichiers) == resume["nombre_fichiers"]
          and nb_dossiers == resume["nombre_dossiers_hors_racine"]
          and taille == resume["taille_totale_octets"]
          and nb_liens == resume["nombre_liens_symboliques"]
          and nb_speciaux == resume["nombre_fichiers_speciaux"])
    mtime_txt = datetime.datetime.fromtimestamp(
        mtime_max / 1e9, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("verification=%s fichiers=%d dossiers=%d taille=%d liens=%d "
          "speciaux=%d mtime_max_utc=%s" % (
              "IDENTIQUE" if ok else "DIFFERENT", len(fichiers), nb_dossiers,
              taille, nb_liens, nb_speciaux, mtime_txt))
    return 0 if ok else 1


def main(argv):
    if len(argv) == 4 and argv[1] == "--verifier-tailles":
        return verifier_tailles(argv[2], argv[3])
    if len(argv) == 5 and not argv[1].startswith("--"):
        return inventorier(argv[1], argv[2], argv[3], argv[4])
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
