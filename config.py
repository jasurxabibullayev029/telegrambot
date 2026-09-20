import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

ADMIN_ID = int(os.getenv("ADMIN_ID", "1209491758"))
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "KHJ701")

DB_TYPE = os.getenv("DB_TYPE", "sqlite").lower()
DATABASE_PATH = DATA_DIR / "bot.db"

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
POSTGRES_DB = os.getenv("POSTGRES_DB", "prezent7ai")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
DATABASE_URL = os.getenv("DATABASE_URL", "")

PRESENTATIONS_DIR = DATA_DIR / "presentations"
PRESENTATIONS_DIR.mkdir(exist_ok=True)

FREE_MONTHLY_LIMIT = 3
FREE_MAX_PAGES = 10

SUBSCRIPTION_PLANS = {
    "1m": {
        "name": "1 oylik PRO",
        "days": 30,
        "price": 50_000,
        "quota": 5,
        "max_pages": 12,
        "tier": "pro",
    },
    "3m": {
        "name": "3 oylik PRO",
        "days": 90,
        "price": 120_000,
        "quota": 30,
        "max_pages": 15,
        "tier": "pro",
    },
    "6m": {
        "name": "6 oylik PRO",
        "days": 180,
        "price": 200_000,
        "quota": 80,
        "max_pages": 18,
        "tier": "pro",
    },
    "12m": {
        "name": "12 oylik VIP",
        "days": 365,
        "price": 350_000,
        "quota": 200,
        "max_pages": 20,
        "tier": "vip",
    },
}

PRESENTATION_STYLES = {
    "minimal": {
        "name": "Minimalist Premium",
        "emoji": "⚪",
        "description": "Sodda, toza va o'ta zamonaviy dizayn",
        "colors": {"bg": "F8FAFC", "card_bg": "FFFFFF", "title": "0F172A", "text": "334155", "accent": "2563EB", "subtext": "64748B"},
    },
    "modern": {
        "name": "Modern Neo-Dark",
        "emoji": "🔵",
        "description": "Zamonaviy toʻq ko'k va yorqin oltin uslub",
        "colors": {"bg": "0F172A", "card_bg": "1E293B", "title": "FFFFFF", "text": "E2E8F0", "accent": "F59E0B", "subtext": "94A3B8"},
    },
    "corporate": {
        "name": "Korporativ Biznes",
        "emoji": "💼",
        "description": "Rasmiy va nufuzli biznes uslubi",
        "colors": {"bg": "F0F4F8", "card_bg": "FFFFFF", "title": "0A2540", "text": "2A3B50", "accent": "0066FF", "subtext": "5A6E85"},
    },
    "creative": {
        "name": "Ijodiy Koral",
        "emoji": "🎨",
        "description": "Rang-barang, yorqin va ijodiy dizayn",
        "colors": {"bg": "FFF8F6", "card_bg": "FFFFFF", "title": "991B1B", "text": "1F2937", "accent": "FF4757", "subtext": "6B7280"},
    },
    "dark": {
        "name": "Qorong'u Kiber",
        "emoji": "🌙",
        "description": "To'q oniks fon va neon nurlar",
        "colors": {"bg": "0B0F19", "card_bg": "161F33", "title": "FFFFFF", "text": "D1D5DB", "accent": "38BDF8", "subtext": "9CA3AF"},
    },
    "nature": {
        "name": "Tabiat va Zumrad",
        "emoji": "🌿",
        "description": "Tazakor yashil va zumrad ranglar",
        "colors": {"bg": "F0FDF4", "card_bg": "FFFFFF", "title": "064E3B", "text": "166534", "accent": "10B981", "subtext": "4D7C0F"},
    },
    "luxury": {
        "name": "Luks / Qirollik Gold",
        "emoji": "👑",
        "description": "Qirollik binafsha va oltinrang uslub",
        "colors": {"bg": "120B20", "card_bg": "1E1430", "title": "FCD34D", "text": "E9D5FF", "accent": "F59E0B", "subtext": "C084FC"},
    },
    "cyberpunk": {
        "name": "Kiberpank Neon",
        "emoji": "⚡",
        "description": "Neonnli futuristik va yorqin dizayn",
        "colors": {"bg": "080810", "card_bg": "121220", "title": "06B6D4", "text": "E0F2FE", "accent": "EC4899", "subtext": "7DD3FC"},
    },
}

