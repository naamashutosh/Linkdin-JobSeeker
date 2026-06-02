"""
Demo: Generate a custom resume for a realistic relevant job posting.
Run: python demo_job_test.py
"""
import sys, os, shutil
sys.path.insert(0, ".")
os.environ["PATH"] = os.environ.get("PATH", "") + ";C:/Users/rohit/AppData/Local/Programs/MiKTeX/miktex/bin/x64"

print("pdflatex:", shutil.which("pdflatex"))

from config.projects import projects_list, conditional_certifications
from modules.resume_customizer import generate_custom_resume, _keyword_select_projects

# ----------------------------------------------------------------
# Realistic job description — Audio/Speech ML Engineer
# (matches Ashutosh's research perfectly)
# ----------------------------------------------------------------
job_title = "AI/ML Engineer - Speech & Audio Processing"
company   = "HealthTech_Innovations"

job_description = """
We are hiring an AI/ML Engineer with strong expertise in speech and audio
processing, deep learning, and clinical AI systems.

Responsibilities:
- Design and develop deep learning models for audio classification,
  speech recognition, and signal processing pipelines.
- Build end-to-end ML systems using PyTorch, TensorFlow, and ONNX Runtime.
- Deploy inference pipelines on embedded systems (Raspberry Pi, ARM, edge devices).
- Work with multi-modal data (audio, image, clinical) for healthcare AI.

Requirements:
- Strong Python and C++ skills.
- Hands-on experience with PyTorch, TensorFlow, Whisper, MFCC, Mel Spectrograms.
- Experience with signal processing: FFT, STFT, WST, FIR/IIR filters.
- Knowledge of CNNs, Transformers, Attention mechanisms.
- Familiarity with ONNX Runtime, model quantization, edge deployment.
- Research or publication background is a strong plus.
- M.Tech / M.S. in ECE, CS, or related field preferred.
"""

print("\n" + "="*60)
print(f"JOB:     {job_title}")
print(f"COMPANY: {company}")
print("="*60)

selected = _keyword_select_projects(job_title, job_description, projects_list, 4)
print(f"\nAI-Selected Projects:")
for i, p in enumerate(selected, 1):
    print(f"  {i}. {p}")

pdf = generate_custom_resume(
    template_path="all resumes/template/resume_template.tex",
    projects_list=projects_list,
    selected_project_names=selected,
    company_name=company,
    job_title=job_title,
    output_base_dir="all resumes",
    job_description=job_description,
    conditional_certifications=conditional_certifications
)

if pdf:
    print(f"\nPDF generated: {pdf}")
    # Open it automatically
    import subprocess
    subprocess.Popen(["cmd", "/c", "start", "", pdf])
    print("PDF opened for review.")
else:
    print("\nPDF generation failed — check logs.")

print("="*60)
