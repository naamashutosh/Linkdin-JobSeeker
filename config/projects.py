'''
YOUR PROJECTS LIST — Ashutosh Verma
====================================
The bot reads this file for every job application.
AI selects the best 3–4 projects based on the job description,
then injects their latex_entry blocks between the
%%PROJECTS_START%% and %%PROJECTS_END%% markers in the template.

HOW TO ADD A NEW PROJECT:
  1. Copy any existing entry below as a template.
  2. Fill in: name, description, domains, tech_stack, date_range, latex_entry.
  3. The latex_entry must use your resume's exact LaTeX style:
       \textbf{Name} $|$ \textit{Tags} \hfill \textit{Date}
       \begin{itemize}
         \item ...
       \end{itemize}
  4. date_range is used only for sorting/display — the actual date shown on
     the resume comes from inside latex_entry.

IMPORTANT:
  - Keep latex_entry as a raw string  r"""..."""  (backslash-safe).
  - Each entry ends with \end{itemize} — no trailing blank line needed.
  - The bot inserts entries one after another; spacing is handled by LaTeX.
'''

projects_list = [

    {
        "name": "Audio-Based Oral Cancer Detection",
        "description": (
            "AI-driven clinical decision support system using Whisper Large embeddings, "
            "Mel Spectrograms, WST-2D features, and a CNN-Attention ensemble for "
            "binary/multi-class oral cancer classification from speech signals. "
            "Multi-modal feature fusion with production-grade inference pipeline."
        ),
        "domains": [
            "Audio Processing", "Speech Processing", "Clinical AI",
            "Deep Learning", "Machine Learning", "Signal Processing",
            "Healthcare AI", "Computer Vision"
        ],
        "tech_stack": [
            "Python", "PyTorch", "Whisper", "Mel Spectrogram",
            "WST-2D", "CNN", "Attention Mechanism", "Librosa"
        ],
        "date_range": "2025-07",   # YYYY-MM — used for chronological ordering
        "latex_entry": r"""\textbf{Audio-Based Oral Cancer Detection} $|$ \textit{Clinical AI, Deep Learning, Speech Processing} \hfill \textit{July 2025 -- Present}
\begin{itemize}
  \item Developed an AI-driven clinical decision support system using Whisper Large embeddings, Mel Spectrograms, WST-2D features, and a CNN-Attention ensemble for binary/multi-class oral cancer classification.
  \item Built robust preprocessing pipelines (noise reduction, normalization, framing) with multi-modal feature fusion, achieving high F1-score and ROC-AUC across multilingual patient datasets.
  \item Designed the inference system as a scalable service for real-time screening workflows with modular, production-grade components for data-driven clinical decision making.
\end{itemize}"""
    },

    {
        "name": "Big Data Analytics Pipeline for Healthcare Insights",
        "description": (
            "Scalable ingestion and transformation pipeline using PySpark and SQL "
            "on MIMIC-III synthetic clinical records (2M+ patient records). "
            "End-to-end data governance, schema validation, deduplication, lineage "
            "tracking, and AWS S3-integrated analytical dashboards."
        ),
        "domains": [
            "Data Engineering", "Big Data", "Cloud", "Healthcare AI",
            "Data Science", "SQL", "ETL", "Analytics"
        ],
        "tech_stack": [
            "PySpark", "SQL", "AWS S3", "Python",
            "Pandas", "NumPy", "Data Governance", "ETL"
        ],
        "date_range": "2025-05",
        "latex_entry": r"""\textbf{Big Data Analytics Pipeline for Healthcare Insights} $|$ \textit{PySpark, SQL, Data Engineering, Cloud} \hfill \textit{May 2025 -- July 2025}
\begin{itemize}
  \item Designed a scalable ingestion and transformation pipeline using PySpark and SQL on clinical records (MIMIC-III synthetic subset), processing 2M+ patient records end-to-end.
  \item Applied data governance (schema validation, deduplication, null-handling, lineage tracking); generated analytical dashboards integrated with AWS S3 from raw ingestion to business-ready reporting.
\end{itemize}"""
    },

    {
        "name": "Image-Based Oral Cancer Detection using Vision Transformers",
        "description": (
            "ViT + CNN hybrid model for early-stage oral lesion classification from "
            "1,000+ annotated clinical and histopathological images, achieving 90.6% accuracy. "
            "Wavelet-based texture enhancement, contrast normalization, and PyTorch C++ "
            "bindings for edge deployment."
        ),
        "domains": [
            "Computer Vision", "Machine Learning", "Deep Learning",
            "Healthcare AI", "Image Classification", "Clinical AI"
        ],
        "tech_stack": [
            "Python", "PyTorch", "Vision Transformer (ViT)",
            "CNN", "OpenCV", "Wavelet Transform", "ONNX"
        ],
        "date_range": "2025-02",
        "latex_entry": r"""\textbf{Image-Based Oral Cancer Detection using Vision Transformers} $|$ \textit{Computer Vision, AI/ML} \hfill \textit{Feb 2025 -- April 2025}
\begin{itemize}
  \item Built a ViT + CNN hybrid model for early-stage oral lesion classification from 1,000+ annotated clinical and histopathological images, achieving 90.6\% accuracy.
  \item Applied wavelet-based texture enhancement and contrast normalization; optimized inference latency using PyTorch C++ bindings for edge deployment.
\end{itemize}"""
    },

    {
        "name": "End-to-End NLP Pipeline for Multi-Domain Text Classification",
        "description": (
            "Fine-tuned DistilBERT on AG News and 20 Newsgroups for multi-class "
            "text classification achieving 93%+ accuracy. SMOTE, data augmentation, "
            "SHAP + attention explainability, ONNX export, and FastAPI deployment."
        ),
        "domains": [
            "NLP", "Machine Learning", "Deep Learning", "Transformers",
            "Text Classification", "MLOps", "Data Science", "Software Engineering"
        ],
        "tech_stack": [
            "Python", "DistilBERT", "HuggingFace", "ONNX Runtime",
            "FastAPI", "SHAP", "Scikit-learn", "PyTorch"
        ],
        "date_range": "2025-01",
        "latex_entry": r"""\textbf{End-to-End NLP Pipeline for Multi-Domain Text Classification} $|$ \textit{NLP, Transformers, Data Insights} \hfill \textit{Jan 2025 -- March 2025}
\begin{itemize}
  \item Fine-tuned DistilBERT on AG News and 20 Newsgroups for multi-class classification achieving 93\%+ accuracy; applied data augmentation, SMOTE, and attention-weight + SHAP explainability layer.
  \item Exported via ONNX Runtime and deployed as a FastAPI REST service, demonstrating scalable proof-of-concept production NLP analytics deployment.
\end{itemize}"""
    },

    {
        "name": "Multilingual Text & Audio Classification for Interactive Systems",
        "description": (
            "Multimodal transformer fusing Wav2Vec2 (audio) and BERT (text) for "
            "multilingual intent recognition in interactive applications. "
            "20% inference throughput improvement via ONNX quantization and dynamic batching. "
            "Deployed as a scalable low-latency API endpoint."
        ),
        "domains": [
            "NLP", "Audio Processing", "Machine Learning", "Transformers",
            "MLOps", "Speech Recognition", "Multimodal AI", "Software Engineering"
        ],
        "tech_stack": [
            "Python", "Wav2Vec2", "BERT", "HuggingFace",
            "ONNX", "PyTorch", "FastAPI", "Docker"
        ],
        "date_range": "2022-03",
        "latex_entry": r"""\textbf{Multilingual Text \& Audio Classification for Interactive Systems} $|$ \textit{NLP, Transformers, MLOps} \hfill \textit{Mar 2022 -- Sep 2023}
\begin{itemize}
  \item Developed a multimodal transformer fusing Wav2Vec2 (audio) and BERT (text) for multilingual intent recognition, supporting real-time interactive application workflows.
  \item Improved inference throughput by 20\% via ONNX quantization and dynamic batching; deployed via scalable API endpoint for low-latency client-facing system integration.
\end{itemize}"""
    },

]

# -----------------------------------------------------------------------
# TO ADD A NEW PROJECT — copy this block and fill it in:
#
# {
#     "name": "Your Project Title",
#     "description": (
#         "Plain-English summary for AI matching (2-3 sentences). "
#         "Include what you built, the domain, and key results."
#     ),
#     "domains": ["Domain1", "Domain2", "Technology"],
#     "tech_stack": ["Python", "Framework", "Tool"],
#     "date_range": "YYYY-MM",   # start date, e.g. "2024-08"
#     "latex_entry": r"""\textbf{Your Project Title} $|$ \textit{Tag1, Tag2} \hfill \textit{Mon YYYY -- Mon YYYY}
# \begin{itemize}
#   \item First achievement with metrics.
#   \item Second achievement with metrics.
# \end{itemize}"""
# },
# -----------------------------------------------------------------------
