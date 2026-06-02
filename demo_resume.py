"""
Demo: Generate custom resumes for 3 different job types
Run: python demo_resume.py
"""
import sys, os, shutil
sys.path.insert(0, ".")

# Add MiKTeX to PATH for pdflatex
miktex = r"C:\Users\rohit\AppData\Local\Programs\MiKTeX\miktex\bin\x64"
os.environ["PATH"] = os.environ.get("PATH", "") + ";" + miktex

print("pdflatex:", shutil.which("pdflatex"))

from config.projects import projects_list
from modules.resume_customizer import generate_custom_resume, _keyword_select_projects

jobs = [
    (
        "Machine Learning Engineer",
        "deep learning audio ML signal processing PyTorch MFCC spectrograms ONNX embedded C++ Python TensorFlow CNN transformers",
        "Demo_ML_Company"
    ),
    (
        "NLP Engineer",
        "BERT DistilBERT text classification ONNX FastAPI HuggingFace Python transformers NLP sentiment analysis",
        "Demo_NLP_Company"
    ),
    (
        "5G Wireless Systems Engineer",
        "5G NR PHY layer OFDM LDPC 3GPP MATLAB C++ protocol stack signal processing RF HARQ modem",
        "Demo_5G_Company"
    ),
    (
        "Embedded Systems Engineer",
        "embedded C STM32 FreeRTOS ARM bare metal UART bootloader microcontroller real-time DSP ONNX edge deployment",
        "Demo_Embedded_Company"
    ),
]

print("\n" + "="*60)
for job_title, job_desc, company in jobs:
    print(f"\nJOB: {job_title}")
    selected = _keyword_select_projects(job_title, job_desc, projects_list, 4)
    print(f"  Selected projects: {selected}")
    pdf = generate_custom_resume(
        template_path="all resumes/template/resume_template.tex",
        projects_list=projects_list,
        selected_project_names=selected,
        company_name=company,
        job_title=job_title,
        output_base_dir="all resumes"
    )
    if pdf:
        print(f"  PDF: {pdf}")
    else:
        print(f"  PDF generation failed — check pdflatex is installed")

print("\n" + "="*60)
print("Done! Open the PDFs above to verify.")
print(r"Folder: C:\Users\rohit\Auto_job_applier_linkedIn\all resumes\Demo_*")
