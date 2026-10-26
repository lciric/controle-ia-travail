"""Extraction du sous-corpus arXiv pour la rétrodiction (conv-audit, 26 octobre 2026) : pour chaque article dont la
première version date de 2003 à 2016 inclus, garder id, année de première version, catégories, titre, résumé. Source :
jeu Hugging Face librarian-bots/arxiv-metadata-snapshot (fichiers parquet 0 à 10, révision consignée à côté)."""
import duckdb, sys
sortie = sys.argv[1]
con = duckdb.connect()
con.execute("INSTALL httpfs; LOAD httpfs;")
urls = [f"https://huggingface.co/api/datasets/librarian-bots/arxiv-metadata-snapshot/parquet/default/train/{i}.parquet" for i in range(11)]
liste = ", ".join("'" + u + "'" for u in urls)
con.execute(f"""
COPY (
  SELECT id,
         CAST(regexp_extract(versions[1].created, '(\\d{{4}}) \\d{{2}}:\\d{{2}}:\\d{{2}}', 1) AS INTEGER) AS annee,
         categories, title, abstract
  FROM read_parquet([{liste}])
  WHERE CAST(regexp_extract(versions[1].created, '(\\d{{4}}) \\d{{2}}:\\d{{2}}:\\d{{2}}', 1) AS INTEGER) BETWEEN 2003 AND 2016
  ORDER BY id
) TO '{sortie}' (FORMAT PARQUET, COMPRESSION ZSTD)
""")
n = con.execute(f"SELECT count(*), min(annee), max(annee) FROM read_parquet('{sortie}')").fetchone()
print("articles :", n[0], "; années", n[1], "à", n[2])
for r in con.execute(f"SELECT annee, count(*) FROM read_parquet('{sortie}') GROUP BY annee ORDER BY annee").fetchall(): print(r)
