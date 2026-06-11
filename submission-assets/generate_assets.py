from __future__ import annotations

from pathlib import Path
import textwrap

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parent


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = []
    if bold:
        candidates.extend(
            [
                "arialbd.ttf",
                "seguisb.ttf",
                "calibrib.ttf",
            ]
        )
    candidates.extend(
        [
            "arial.ttf",
            "segoeui.ttf",
            "calibri.ttf",
        ]
    )
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def markdown_to_pdf(markdown_path: Path, pdf_path: Path, title: str) -> None:
    page_width, page_height = A4
    left = 48
    right = 48
    top = page_height - 56
    bottom = 48
    line_height = 15
    usable_width = page_width - left - right

    pdf = canvas.Canvas(str(pdf_path), pagesize=A4)
    pdf.setTitle(title)

    def start_page() -> float:
        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawString(left, page_height - 38, title)
        pdf.setFont("Helvetica", 10)
        pdf.drawRightString(page_width - right, page_height - 38, "RakshakAI Submission Pack")
        pdf.line(left, page_height - 44, page_width - right, page_height - 44)
        return top

    y = start_page()

    def ensure_space(required: int = line_height) -> None:
        nonlocal y
        if y - required < bottom:
            pdf.showPage()
            y = start_page()

    def draw_wrapped(text: str, font_name: str = "Helvetica", font_size: int = 11, indent: int = 0, gap: int = 4) -> None:
        nonlocal y
        pdf.setFont(font_name, font_size)
        char_width = max(55, int((usable_width - indent) / max(font_size * 0.52, 1)))
        wrapped = textwrap.wrap(text, width=char_width) or [""]
        for line in wrapped:
            ensure_space(line_height)
            pdf.drawString(left + indent, y, line)
            y -= line_height
        y -= gap

    for raw_line in markdown_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if not line:
            y -= 5
            continue
        if line.startswith("# "):
            ensure_space(26)
            pdf.setFont("Helvetica-Bold", 16)
            pdf.drawString(left, y, line[2:].strip())
            y -= 22
            continue
        if line.startswith("## "):
            ensure_space(22)
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(left, y, line[3:].strip())
            y -= 18
            continue
        if line.startswith("### "):
            ensure_space(20)
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(left, y, line[4:].strip())
            y -= 16
            continue
        if line.startswith("- "):
            draw_wrapped(f"• {line[2:].strip()}", indent=10, gap=2)
            continue
        if line[:3].isdigit() and line[1:3] == ". ":
            draw_wrapped(line, indent=0, gap=2)
            continue
        draw_wrapped(line)

    pdf.save()


def draw_box(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, body: list[str], fill: str, title_font, body_font) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=18, fill=fill, outline="#17324D", width=3)
    draw.text((x1 + 18, y1 + 14), title, fill="#0F2235", font=title_font)
    current_y = y1 + 52
    for line in body:
        wrapped = textwrap.wrap(line, width=25) or [line]
        for wrapped_line in wrapped:
            draw.text((x1 + 18, current_y), f"- {wrapped_line}", fill="#18364F", font=body_font)
            current_y += 22


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = "#C0392B") -> None:
    draw.line([start, end], fill=color, width=6)
    x1, y1 = start
    x2, y2 = end
    if abs(x2 - x1) >= abs(y2 - y1):
        direction = 1 if x2 >= x1 else -1
        draw.polygon(
            [
                (x2, y2),
                (x2 - 16 * direction, y2 - 9),
                (x2 - 16 * direction, y2 + 9),
            ],
            fill=color,
        )
    else:
        direction = 1 if y2 >= y1 else -1
        draw.polygon(
            [
                (x2, y2),
                (x2 - 9, y2 - 16 * direction),
                (x2 + 9, y2 - 16 * direction),
            ],
            fill=color,
        )


def create_roadmap_png(png_path: Path) -> None:
    width, height = 1800, 1100
    image = Image.new("RGB", (width, height), "#F6F7FB")
    draw = ImageDraw.Draw(image)

    title_font = load_font(44, bold=True)
    subtitle_font = load_font(22)
    box_title_font = load_font(24, bold=True)
    box_body_font = load_font(18)

    draw.text((70, 40), "RakshakAI Road Map and Flow Diagram", fill="#11263A", font=title_font)
    draw.text(
        (70, 100),
        "Integrated senior safety workflow from scam check and SOS trigger to family alerts and police action.",
        fill="#37556E",
        font=subtitle_font,
    )

    boxes = {
        "senior": (80, 180, 430, 390),
        "fraud": (500, 180, 850, 420),
        "sos": (920, 180, 1270, 420),
        "wellness": (1340, 180, 1690, 420),
        "backend": (360, 520, 840, 770),
        "notifications": (960, 520, 1440, 770),
        "dashboard": (660, 850, 1140, 1040),
    }

    draw_box(
        draw,
        boxes["senior"],
        "Senior Citizen App",
        ["Accessible home screen", "Check Scam", "Trigger SOS", "Daily check-in"],
        "#DCEEFF",
        box_title_font,
        box_body_font,
    )
    draw_box(
        draw,
        boxes["fraud"],
        "AI Scam Detection",
        ["Text analysis", "Screenshot OCR", "Risk score", "Simple explanation"],
        "#E3F8E8",
        box_title_font,
        box_body_font,
    )
    draw_box(
        draw,
        boxes["sos"],
        "Emergency SOS",
        ["One-tap alert", "Voice trigger", "GPS capture", "Incident creation"],
        "#FFE5E0",
        box_title_font,
        box_body_font,
    )
    draw_box(
        draw,
        boxes["wellness"],
        "Welfare Monitoring",
        ["Daily status log", "Medication reminders", "Inactivity risk", "Need-help flag"],
        "#FFF4D7",
        box_title_font,
        box_body_font,
    )
    draw_box(
        draw,
        boxes["backend"],
        "FastAPI + Realtime Backend",
        ["Auth, fraud, SOS, wellness APIs", "Evidence and notification storage", "Socket.IO live events", "Risk aggregation"],
        "#EAE3FF",
        box_title_font,
        box_body_font,
    )
    draw_box(
        draw,
        boxes["notifications"],
        "Family and Police Notifications",
        ["Fraud report escalation", "Live SOS feed", "High-risk senior alerts", "Case status updates"],
        "#DFF6F6",
        box_title_font,
        box_body_font,
    )
    draw_box(
        draw,
        boxes["dashboard"],
        "Police Dashboard and Response",
        ["Summary cards", "Incident monitor", "Fraud evidence review", "Heatmap and case tracking"],
        "#FDE7FF",
        box_title_font,
        box_body_font,
    )

    arrow(draw, (430, 250), (500, 250))
    arrow(draw, (430, 305), (920, 305))
    arrow(draw, (430, 360), (1340, 360))
    arrow(draw, (675, 420), (600, 520))
    arrow(draw, (1095, 420), (1110, 520))
    arrow(draw, (1515, 420), (1300, 520))
    arrow(draw, (840, 645), (960, 645))
    arrow(draw, (1200, 770), (1000, 850))

    footer = [
        "Phase 1: Build accessible MVP across mobile, backend, and dashboard",
        "Phase 2: Add AI integrations for Gemini, Tesseract, and Whisper",
        "Phase 3: Expand production readiness, multilingual support, and predictive analytics",
    ]
    footer_y = 108
    base_y = 1060
    for i, line in enumerate(footer):
        draw.text((90 + i * 550, base_y), line, fill="#304A60", font=load_font(16))

    image.save(png_path)


def image_to_pdf(image_path: Path, pdf_path: Path, title: str) -> None:
    page_width, page_height = landscape(A4)
    pdf = canvas.Canvas(str(pdf_path), pagesize=landscape(A4))
    pdf.setTitle(title)
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(32, page_height - 30, title)
    pdf.line(32, page_height - 36, page_width - 32, page_height - 36)

    available_width = page_width - 64
    available_height = page_height - 80
    pdf.drawImage(str(image_path), 32, 24, width=available_width, height=available_height, preserveAspectRatio=True, anchor="c")
    pdf.save()


def main() -> None:
    create_roadmap_png(ROOT / "roadmap-flow-diagram.png")
    image_to_pdf(ROOT / "roadmap-flow-diagram.png", ROOT / "roadmap-flow-diagram.pdf", "RakshakAI Road Map / Flow Diagram")
    markdown_to_pdf(ROOT / "solution-document.md", ROOT / "solution-document.pdf", "RakshakAI Solution Document")


if __name__ == "__main__":
    main()
