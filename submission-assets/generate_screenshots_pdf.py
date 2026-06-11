from __future__ import annotations

from pathlib import Path

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "running-program-screenshots.pdf"

SCREENSHOTS = [
    ("Dashboard Login", ROOT / "dashboard-login.png", "Police dashboard sign-in screen with demo credentials."),
    ("Dashboard Overview", ROOT / "dashboard-overview.png", "Live police command hub showing overview and monitoring panels."),
    ("Dashboard Fraud Reports", ROOT / "dashboard-fraud-reports.png", "Fraud investigation screen with report review and evidence context."),
    ("Mobile Login", ROOT / "mobile-login-or-splash.png", "Senior citizen mobile login screen in Flutter web mode."),
    ("Mobile Home", ROOT / "mobile-home.png", "Senior home dashboard with SOS, scam check, and daily check-in actions."),
    ("Mobile SOS", ROOT / "mobile-sos.png", "Emergency SOS screen with one-tap distress trigger and emergency contacts."),
]


def draw_cover(pdf: canvas.Canvas, width: float, height: float) -> None:
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawString(48, height - 70, "RakshakAI Running Program Screenshots")
    pdf.setFont("Helvetica", 13)
    pdf.drawString(48, height - 100, "Live screenshots captured from the running dashboard and Flutter mobile app.")
    pdf.drawString(48, height - 122, "Prepared for hackathon submission.")

    pdf.setFont("Helvetica-Bold", 15)
    pdf.drawString(48, height - 170, "Included Screens")
    pdf.setFont("Helvetica", 12)
    y = height - 200
    for index, (title, _, caption) in enumerate(SCREENSHOTS, start=1):
        pdf.drawString(60, y, f"{index}. {title}")
        y -= 18
        pdf.setFont("Helvetica-Oblique", 11)
        pdf.drawString(78, y, caption)
        y -= 28
        pdf.setFont("Helvetica", 12)

    pdf.setFont("Helvetica", 11)
    pdf.drawString(48, 48, "Generated from files in submission-assets.")


def draw_image_page(pdf: canvas.Canvas, width: float, height: float, title: str, image_path: Path, caption: str) -> None:
    margin = 36
    header_y = height - 38
    footer_y = 34
    image_top = height - 90
    image_bottom = 74
    available_width = width - margin * 2
    available_height = image_top - image_bottom

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(margin, header_y, title)
    pdf.setFont("Helvetica", 11)
    pdf.drawRightString(width - margin, header_y, "RakshakAI")

    reader = ImageReader(str(image_path))
    img_width, img_height = reader.getSize()
    scale = min(available_width / img_width, available_height / img_height)
    draw_width = img_width * scale
    draw_height = img_height * scale
    x = (width - draw_width) / 2
    y = image_bottom + (available_height - draw_height) / 2
    pdf.drawImage(reader, x, y, width=draw_width, height=draw_height, preserveAspectRatio=True, mask="auto")

    pdf.setFont("Helvetica-Oblique", 11)
    pdf.drawString(margin, footer_y, caption)


def main() -> None:
    width, height = landscape(A4)
    pdf = canvas.Canvas(str(OUTPUT), pagesize=landscape(A4))
    pdf.setTitle("RakshakAI Running Program Screenshots")

    draw_cover(pdf, width, height)
    pdf.showPage()

    for title, image_path, caption in SCREENSHOTS:
        if not image_path.exists():
            continue
        draw_image_page(pdf, width, height, title, image_path, caption)
        pdf.showPage()

    pdf.save()


if __name__ == "__main__":
    main()
