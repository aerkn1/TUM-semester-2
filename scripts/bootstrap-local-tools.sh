#!/usr/bin/env bash
set -euo pipefail

# Recreate the local study-material parsing environment.
# This script intentionally does not commit .venv; it rebuilds it from requirements.txt.

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "This bootstrap is written for macOS/Homebrew. Install equivalent packages manually on this OS." >&2
  echo "Required binaries: soffice, pdftotext, pdftoppm, tesseract, magick, pandoc, ffmpeg" >&2
else
  if ! command -v brew >/dev/null 2>&1; then
    echo "Homebrew is required to install system parsing tools: https://brew.sh" >&2
    exit 1
  fi

  brew install libreoffice poppler tesseract imagemagick pandoc ffmpeg
fi

python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "Verifying required binaries..."
for bin in soffice pdftotext pdftoppm tesseract magick pandoc ffmpeg; do
  if ! command -v "${bin}" >/dev/null 2>&1; then
    echo "Missing required binary: ${bin}" >&2
    exit 1
  fi
  echo "${bin}: $(command -v "${bin}")"
done

echo "Verifying Python packages..."
python - <<'PY'
import fitz
import markdownify
import openpyxl
import pdfplumber
import PIL
import pptx
import pytesseract
print("Python parsing stack OK")
PY

echo "Bootstrap complete. Activate with: . .venv/bin/activate"
