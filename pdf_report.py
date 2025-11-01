#!/usr/bin/env python3
"""
PDF report generation utilities
"""

def save_image_to_temp(image_data, filename="temp_image.png"):
    """Save image data to temporary file"""
    try:
        import base64
        import tempfile
        import os

        # Decode base64 image
        if image_data.startswith('data:image'):
            image_data = image_data.split(',')[1]

        image_bytes = base64.b64decode(image_data)

        # Save to temp file
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, filename)

        with open(temp_path, 'wb') as f:
            f.write(image_bytes)

        return temp_path
    except Exception as e:
        print(f"Error saving image to temp: {e}")
        return None

def generate_pdf_report(analysis_results, output_images, filename="heritage_analysis_report.pdf"):
    """Generate PDF report from analysis results"""
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
        from reportlab.lib.units import inch
        import io

        # Create PDF buffer
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        # Title
        title = Paragraph("Heritage Site Health Monitoring Report", styles['Title'])
        story.append(title)
        story.append(Spacer(1, 12))

        # Analysis Summary
        summary_text = f"""
        <b>Analysis Summary:</b><br/>
        Total Cracks Detected: {analysis_results.get('crack_detection', {}).get('count', 0)}<br/>
        Biological Growth Coverage: {analysis_results.get('biological_growth', {}).get('growth_percentage', 0)}%<br/>
        Primary Material: {analysis_results.get('material_analysis', {}).get('predicted_material', 'Unknown')}<br/>
        Structural Health Score: {analysis_results.get('data_science_insights', {}).get('statistical_summary', {}).get('structural_health_score', 0)}<br/>
        """

        story.append(Paragraph(summary_text, styles['Normal']))
        story.append(Spacer(1, 12))

        # Build PDF
        doc.build(story)

        # Get PDF data
        pdf_data = buffer.getvalue()
        buffer.close()

        return pdf_data

    except ImportError:
        print("ReportLab not available for PDF generation")
        return None
    except Exception as e:
        print(f"Error generating PDF report: {e}")
        return None
