## Projeyi Ayağa Kaldıran Terminal Komutları

2 ayrı terminalde komutları çalıştır:

### Terminal 1

1. curl -LsSf https://astral.sh/uv/install.sh | sh
2. uv sync
3. uv run uvicorn backend.main:app --port 8001 --reload

### Terminal 2

1. cd frontend
2. npm install
3. npm run dev
