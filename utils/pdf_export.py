from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.units import inch
from xml.sax.saxutils import escape


def export_storybook(chunks, image_paths, output_path="storybook.pdf", font_size=14, concept=None):
    """
    Export the storybook with alternating text + illustration pages in a polished style.
    Adds a personalized cover page if `concept` is provided.
    """
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=60,
        bottomMargin=60,
    )

    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="StoryText",
        fontName="Times-Roman",
        fontSize=font_size,
        leading=font_size * 1.5,
        alignment=4, 
    ))
    styles.add(ParagraphStyle(
        name="StoryTitle",  
        fontName="Times-Bold",
        fontSize=22,
        leading=28,
        alignment=1, 
        spaceAfter=20,
    ))
    styles.add(ParagraphStyle(
        name="Caption",
        fontName="Times-Italic",
        fontSize=12,
        alignment=1, 
        spaceAfter=10,
    ))

    elements = []

   
    elements.append(Paragraph("📖 AI Storybook", styles["StoryTitle"]))
    elements.append(Spacer(1, 20))

    if concept:
        elements.append(Paragraph(f"A story about: <b>{escape(concept)}</b>", styles["Caption"]))
        elements.append(Spacer(1, 10))

    elements.append(Paragraph("Generated with Text + AI Illustrations", styles["Caption"]))
    elements.append(PageBreak())

    
    for i, chunk in enumerate(chunks):
        
        safe_chunk = escape(chunk).replace("\n", "<br/>")

        
        elements.append(Paragraph(safe_chunk, styles["StoryText"]))
        elements.append(PageBreak())

        
        if i < len(image_paths) and image_paths[i]:
            try:
                img = Image(image_paths[i], width=5*inch, height=4*inch)
                img.hAlign = "CENTER"
                elements.append(img)
                elements.append(Paragraph(f"Page {i+1} Illustration", styles["Caption"]))
                elements.append(PageBreak())
            except Exception as e:
                print(f"⚠️ Could not load image {image_paths[i]}: {e}")

  
    doc.build(elements)
    print(f"✅ Storybook exported successfully: {output_path}")

