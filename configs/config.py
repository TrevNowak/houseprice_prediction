from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = 42
TARGET = "SalePrice"
RAW_DATA = ROOT / "data" / "raw" / "housepricewithlabel.csv"
PROCESSED_DIR = ROOT / "data" / "processed"
MODELS_DIR = ROOT / "models"
FIG_DIR = ROOT / "reports" / "figures"
EXPERIMENTS_CSV = ROOT / "experiments.csv"
TEST_SIZE = 0.2
CV_FOLDS = 5
