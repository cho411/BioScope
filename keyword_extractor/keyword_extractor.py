# keyword_extractor.py

import re
from pathlib import Path
from typing import List, Set

# 경로 설정
BASE_DIR = Path(__file__).parent
STOPWORDS_FILE = BASE_DIR / "stopwords.txt"

# 불용어 로드 (파일 없으면 에러 → 강제로 관리 유도)
def load_stopwords() -> Set[str]:
    if not STOPWORDS_FILE.exists():
        raise FileNotFoundError(
            f"불용어 파일이 없습니다: {STOPWORDS_FILE}\n"
            "stopwords.txt 파일을 만들어서 불용어를 관리해주세요!"
        )
    stopwords = set()
    for line in STOPWORDS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            stopwords.add(line.lower())  # 모두 소문자로 정규화
    if not stopwords:
        raise ValueError(f"{STOPWORDS_FILE} 파일이 비어있습니다!")
    return stopwords

STOPWORDS = load_stopwords()

# Kiwi 필수
try:
    from kiwipiepy import Kiwi
    kiwi = Kiwi()
except ImportError:
    raise ImportError("kiwipiepy가 필요합니다: pip install kiwipiepy")

def extract_keywords(query: str, top_k: int = 10) -> List[str]:
    query = query.strip()
    if not query:
        return []

    terms = []

    # 1. 대문자 약어 (CRISPR, mRNA, COVID 등)
    terms.extend(re.findall(r'\b[A-Z]{2,}[A-Za-z0-9]*\b', query))

    # 2. 하이픈 복합어 (genome-wide, single-cell, RNA-seq 등)
    terms.extend(re.findall(r'\b[a-zA-Z]+(?:-[a-zA-Z0-9-]+)+\b', query))

    # 3. 일반 영어 + 숫자 포함 단어 (Pacbio, Covid19, 5GB 등)
    terms.extend(re.findall(r'\b[a-zA-Z]+[a-zA-Z0-9]*\b', query))

    # 4. 한국어 명사 + 외국어 + 어근 (Kiwi로 정확히)
    for token in kiwi.tokenize(query):
        if token.tag in ['NNG', 'NNP', 'SL', 'XR', 'VV', 'VA']:  # 명사, 고유명사, 외국어, 어근, 동사/형용사도 일부 포함
            if len(token.form) >= 2:
                terms.append(token.form)

    # 중복 제거 + 불용어 제거 (소문자 기준 매칭)
    seen = set()
    result = []
    for term in terms:
        if term.lower() in STOPWORDS:
            continue
        if len(term) < 2:
            continue
        if term not in seen:
            seen.add(term)
            result.append(term)

    return result[:top_k]

__all__ = ["extract_keywords"]