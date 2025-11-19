# test.py
from keyword_extractor import extract_keywords

queries = [
    "genome-wide, CRISPR 실험 관련 데이터셋 찾아줘",
    "obesity에 대해 연구한 데이터셋 찾아줘, Human cell line 사용한 실험 데이터",
    "microRNA 데이터 중에 Cancer와 관련된 연구 데이터 있어?",
    "Crispr 유전자가위 연구 중에 Pacbio 기기로 시퀀싱한 실험 데이터 있어? Genomic data",
    "Obesity 치료제 연구 중에 mouse model에서 실험한 연구데이터 찾아줘",
    "Covid 19 mRNA vaccine 관련된 연구 데이터 셋 찾아줘",
    "mRNA vaccine의 delivery efficiency를 확인한 실험 데이터셋 필요해",
    "single cell RNA-seq 데이터 중에 사이즈가 5GB 이하인 걸로만 보여줘",
    "gene expression 관련 RNA-seq data 보여줘",
    "Lung tissue에서 실험한 데이터 중 replicate이 2개 이상인 것만 보여줘",
    "UTR에 관한 실험 데이터 보여줘"
]

for q in queries:
    print(f"쿼리: {q}")
    print(f"키워드: {extract_keywords(q, top_k=8)}")
    print("-" * 70)