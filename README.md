# BioScope
my-bio-explorer/
│
├── data_ingestion/
│   ├── geo_fetch.py
│   ├── sra_fetch.py
│   └── ena_fetch.py
│
├── processing/
│   ├── metadata_parser.py
│   ├── ontology_mapper.py
│   └── dataset_normalizer.py
│
├── ai/
│   ├── embedder.py
│   ├── recommender.py
│   ├── summarizer.py
│   └── query_parser.py
│
├── web/
│   ├── api/
│   ├── frontend/
│   └── backend/
│
├── README.md
└── LICENSE

## Data Source
This project uses public datasets from:
- NCBI GEO (Gene Expression Omnibus)
- NCBI SRA (Sequence Read Archive)
- ENA European Nucleotide Archive

All data is used under the respective public access policies.
