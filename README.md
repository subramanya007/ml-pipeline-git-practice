# ML Pipeline Project

A simple ML classification pipeline used to practice Git branching workflows.

## Structure
```
ml_project/
├── data/
│   └── raw.csv          # raw input data
├── src/
│   ├── data_cleaning.py # data prep
│   └── model.py         # model training
├── main.py              # pipeline entry point
└── requirements.txt
```

## How to Run
```bash
pip install -r requirements.txt
python main.py
```

## Branches
- `main` — stable production code
- `feature/data-cleaning` — improved data cleaning logic
- `feature/model-enhancement` — improved model with scaling & tuning
