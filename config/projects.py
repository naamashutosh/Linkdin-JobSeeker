'''
Configure your projects list here.
The bot will use AI to select the best 3-4 projects from this list
for each job based on the job description.

Each project entry must have:
  - name         : Unique display name (used in resume heading)
  - description  : 1-2 sentence plain-English summary (used by AI for matching)
  - domains      : List of domain/role tags (e.g., "Machine Learning", "Embedded Systems")
  - tech_stack   : List of technologies / frameworks used
  - latex_entry  : The exact LaTeX block that will be inserted into the resume

HOW TO ADD YOUR PROJECTS:
  1. Copy the template entry below and fill in your own details.
  2. For latex_entry, use the same LaTeX commands your resume template uses
     for a project block (e.g., \resumeProjectHeading, \resumeItem, etc.).
  3. Wrap your projects section in resume_template.tex with:
         %%PROJECTS_START%%
         %%PROJECTS_END%%
     The bot will replace everything between those markers automatically.
'''

projects_list = [

    # ------------------------------------------------------------------ #
    #  MACHINE LEARNING / DEEP LEARNING                                   #
    # ------------------------------------------------------------------ #

    {
        "name": "Neural Network Image Classifier",
        "description": (
            "Built a deep convolutional neural network for multi-class image classification "
            "achieving 96% accuracy on a custom dataset of 50,000 images. "
            "Implemented data augmentation, transfer learning from ResNet-50, and deployed via Flask REST API."
        ),
        "domains": ["Machine Learning", "Deep Learning", "Computer Vision", "Python"],
        "tech_stack": ["Python", "PyTorch", "TensorFlow", "Flask", "OpenCV", "ResNet"],
        "latex_entry": r"""        \resumeProjectHeading
          {\textbf{Neural Network Image Classifier} $|$ \emph{Python, PyTorch, TensorFlow, Flask}}{2024}
          \resumeItemListStart
            \resumeItem{Built a deep CNN using ResNet-50 transfer learning achieving \textbf{96\% accuracy} on a 50k-image custom dataset}
            \resumeItem{Applied data augmentation (rotation, flipping, normalization) to reduce overfitting by 18\%}
            \resumeItem{Deployed model as a REST API with Flask; handled 200+ concurrent inference requests}
          \resumeItemListEnd"""
    },

    {
        "name": "Real-Time Object Detection System",
        "description": (
            "Developed a YOLOv8-based real-time object detection pipeline capable of processing "
            "30 FPS video streams. Used for traffic monitoring with custom-trained classes."
        ),
        "domains": ["Machine Learning", "Computer Vision", "Deep Learning", "Real-Time Systems"],
        "tech_stack": ["Python", "YOLOv8", "OpenCV", "CUDA", "NumPy"],
        "latex_entry": r"""        \resumeProjectHeading
          {\textbf{Real-Time Object Detection System} $|$ \emph{Python, YOLOv8, OpenCV, CUDA}}{2024}
          \resumeItemListStart
            \resumeItem{Trained YOLOv8 on a custom 8-class traffic dataset (12k annotated images) achieving \textbf{mAP@50 of 0.89}}
            \resumeItem{Optimized inference pipeline with CUDA for \textbf{30 FPS} real-time video processing}
            \resumeItem{Built post-processing module for lane-level vehicle counting and anomaly alerting}
          \resumeItemListEnd"""
    },

    # ------------------------------------------------------------------ #
    #  DATA SCIENCE / ANALYTICS                                           #
    # ------------------------------------------------------------------ #

    {
        "name": "Customer Churn Prediction Pipeline",
        "description": (
            "End-to-end machine learning pipeline to predict customer churn for a telecom dataset. "
            "Used feature engineering, SHAP explainability, and deployed via Streamlit dashboard."
        ),
        "domains": ["Data Science", "Machine Learning", "Analytics", "Python"],
        "tech_stack": ["Python", "Scikit-learn", "XGBoost", "SHAP", "Pandas", "Streamlit"],
        "latex_entry": r"""        \resumeProjectHeading
          {\textbf{Customer Churn Prediction Pipeline} $|$ \emph{Python, XGBoost, SHAP, Streamlit}}{2023}
          \resumeItemListStart
            \resumeItem{Built XGBoost churn classifier on 100k-row telecom dataset; achieved \textbf{F1-score 0.87} with hyperparameter tuning}
            \resumeItem{Applied SHAP for feature importance analysis; identified top 5 churn drivers for business stakeholders}
            \resumeItem{Deployed interactive Streamlit dashboard for real-time churn probability scoring}
          \resumeItemListEnd"""
    },

    {
        "name": "Sales Forecasting with Time Series",
        "description": (
            "Developed ARIMA and LSTM-based sales forecasting models for retail time series data, "
            "reducing forecast error by 22% compared to the baseline moving average model."
        ),
        "domains": ["Data Science", "Time Series", "Machine Learning", "Analytics"],
        "tech_stack": ["Python", "Statsmodels", "PyTorch", "Pandas", "Matplotlib", "ARIMA", "LSTM"],
        "latex_entry": r"""        \resumeProjectHeading
          {\textbf{Sales Forecasting with Time Series} $|$ \emph{Python, LSTM, ARIMA, Pandas}}{2023}
          \resumeItemListStart
            \resumeItem{Modeled 3-year retail sales data using ARIMA and LSTM; reduced MAPE from 14\% to \textbf{11\%}}
            \resumeItem{Engineered lag features, rolling statistics, and holiday indicators to capture seasonal patterns}
            \resumeItem{Visualized forecast confidence intervals with Matplotlib for executive reporting}
          \resumeItemListEnd"""
    },

    # ------------------------------------------------------------------ #
    #  AUDIO PROCESSING / SIGNAL PROCESSING                               #
    # ------------------------------------------------------------------ #

    {
        "name": "Automatic Speech Recognition System",
        "description": (
            "Fine-tuned OpenAI Whisper on domain-specific audio data for low-resource language ASR. "
            "Achieved WER of 8.2% on test set, outperforming baseline by 15%."
        ),
        "domains": ["Audio Processing", "Speech Recognition", "Machine Learning", "NLP"],
        "tech_stack": ["Python", "Whisper", "HuggingFace", "Torchaudio", "Librosa", "PyTorch"],
        "latex_entry": r"""        \resumeProjectHeading
          {\textbf{Automatic Speech Recognition System} $|$ \emph{Python, Whisper, HuggingFace, Torchaudio}}{2024}
          \resumeItemListStart
            \resumeItem{Fine-tuned OpenAI Whisper-base on 200h domain corpus; achieved \textbf{WER 8.2\%}, a 15\% improvement over baseline}
            \resumeItem{Built audio preprocessing pipeline with noise reduction (spectral gating) and VAD using Librosa}
            \resumeItem{Implemented CTC beam-search decoding with language model rescoring to improve transcript coherence}
          \resumeItemListEnd"""
    },

    {
        "name": "Environmental Sound Classification",
        "description": (
            "Designed a CNN-based classifier for urban environmental sound recognition using mel-spectrograms. "
            "Trained on ESC-50 dataset achieving 91% accuracy."
        ),
        "domains": ["Audio Processing", "Machine Learning", "Signal Processing", "Deep Learning"],
        "tech_stack": ["Python", "Librosa", "PyTorch", "Mel-spectrogram", "CNN"],
        "latex_entry": r"""        \resumeProjectHeading
          {\textbf{Environmental Sound Classification} $|$ \emph{Python, Librosa, PyTorch, CNN}}{2023}
          \resumeItemListStart
            \resumeItem{Converted raw audio to mel-spectrograms and trained a 6-layer CNN on ESC-50; reached \textbf{91\% accuracy}}
            \resumeItem{Applied SpecAugment (time/frequency masking) for data augmentation, improving accuracy by 4\%}
            \resumeItem{Compared CNN, ResNet, and MobileNet backbones; reported benchmark results on validation splits}
          \resumeItemListEnd"""
    },

    # ------------------------------------------------------------------ #
    #  EMBEDDED SYSTEMS / IoT                                             #
    # ------------------------------------------------------------------ #

    {
        "name": "IoT-Based Smart Home Monitoring System",
        "description": (
            "Designed an embedded sensor node on STM32 that streams temperature, humidity, and motion data "
            "over MQTT to a cloud dashboard. Achieved 3-month battery life with deep-sleep optimization."
        ),
        "domains": ["Embedded Systems", "IoT", "Firmware", "C/C++", "RTOS"],
        "tech_stack": ["C", "STM32", "FreeRTOS", "MQTT", "I2C", "SPI", "Python"],
        "latex_entry": r"""        \resumeProjectHeading
          {\textbf{IoT Smart Home Monitoring System} $|$ \emph{C, STM32, FreeRTOS, MQTT}}{2024}
          \resumeItemListStart
            \resumeItem{Programmed STM32F4 in C with FreeRTOS tasks for concurrent sensor polling over I2C/SPI at 1 Hz}
            \resumeItem{Implemented MQTT-based telemetry over Wi-Fi (ESP8266); visualized data on Node-RED dashboard}
            \resumeItem{Reduced power draw to \textbf{18 µA} in deep-sleep mode, achieving \textbf{3-month} coin-cell battery life}
          \resumeItemListEnd"""
    },

    {
        "name": "Edge ML Inference on Microcontroller",
        "description": (
            "Deployed a TinyML gesture recognition model on an ARM Cortex-M4 microcontroller "
            "using TensorFlow Lite for Microcontrollers. Achieved 94% accuracy at under 10ms latency."
        ),
        "domains": ["Embedded Systems", "Machine Learning", "TinyML", "Edge AI", "C++"],
        "tech_stack": ["C++", "TensorFlow Lite", "Arduino", "ARM Cortex-M4", "Python"],
        "latex_entry": r"""        \resumeProjectHeading
          {\textbf{Edge ML Inference on Microcontroller} $|$ \emph{C++, TensorFlow Lite, ARM Cortex-M4}}{2024}
          \resumeItemListStart
            \resumeItem{Quantized and deployed a gesture recognition CNN to STM32 using TFLite Micro; achieved \textbf{94\% accuracy}}
            \resumeItem{Reduced model size from 2.1 MB to \textbf{48 KB} via INT8 post-training quantization with $<$1\% accuracy drop}
            \resumeItem{Benchmarked inference latency at \textbf{8.4 ms} per sample on Cortex-M4 at 80 MHz}
          \resumeItemListEnd"""
    },

    # ------------------------------------------------------------------ #
    #  SOFTWARE ENGINEERING / BACKEND                                     #
    # ------------------------------------------------------------------ #

    {
        "name": "Scalable REST API with Microservices",
        "description": (
            "Built a production-grade REST API for an e-commerce platform using FastAPI and PostgreSQL. "
            "Containerized with Docker, orchestrated on Kubernetes, handling 10k+ requests per second."
        ),
        "domains": ["Software Engineering", "Backend", "Cloud", "API Development", "DevOps"],
        "tech_stack": ["Python", "FastAPI", "PostgreSQL", "Docker", "Kubernetes", "Redis", "Celery"],
        "latex_entry": r"""        \resumeProjectHeading
          {\textbf{Scalable REST API with Microservices} $|$ \emph{FastAPI, PostgreSQL, Docker, Kubernetes}}{2024}
          \resumeItemListStart
            \resumeItem{Designed RESTful microservices with FastAPI and PostgreSQL; achieved \textbf{10k+ RPS} under load testing}
            \resumeItem{Implemented JWT authentication, rate limiting, and Redis caching reducing DB load by 65\%}
            \resumeItem{Containerized services with Docker; deployed to Kubernetes with auto-scaling (HPA) and zero-downtime rollouts}
          \resumeItemListEnd"""
    },

    {
        "name": "Full-Stack Web Application",
        "description": (
            "Developed a full-stack project management tool with React frontend and Django REST backend. "
            "Supports real-time collaboration via WebSockets and CI/CD via GitHub Actions."
        ),
        "domains": ["Software Engineering", "Full Stack", "Web Development", "React", "Django"],
        "tech_stack": ["React", "Django", "PostgreSQL", "WebSocket", "Docker", "GitHub Actions"],
        "latex_entry": r"""        \resumeProjectHeading
          {\textbf{Full-Stack Project Management Tool} $|$ \emph{React, Django, PostgreSQL, WebSocket}}{2023}
          \resumeItemListStart
            \resumeItem{Built React SPA with Redux state management and Django REST Framework backend; \textbf{500+ active users}}
            \resumeItem{Implemented real-time task updates using Django Channels WebSockets; reduced page refresh by 100\%}
            \resumeItem{Set up CI/CD pipeline with GitHub Actions, Docker Compose, and automated pytest/Jest suites}
          \resumeItemListEnd"""
    },

    # ------------------------------------------------------------------ #
    #  NLP / LLM                                                          #
    # ------------------------------------------------------------------ #

    {
        "name": "LLM-Powered Document Q&A System",
        "description": (
            "Built a Retrieval-Augmented Generation (RAG) system using LangChain and OpenAI GPT-4 "
            "to answer questions over private PDF documents with source citations."
        ),
        "domains": ["NLP", "LLM", "Machine Learning", "Generative AI", "Python"],
        "tech_stack": ["Python", "LangChain", "OpenAI", "FAISS", "HuggingFace", "Streamlit"],
        "latex_entry": r"""        \resumeProjectHeading
          {\textbf{LLM-Powered Document Q\&A System} $|$ \emph{Python, LangChain, OpenAI, FAISS}}{2024}
          \resumeItemListStart
            \resumeItem{Implemented RAG pipeline with LangChain: chunked PDFs, embedded with text-ada-002, indexed in FAISS}
            \resumeItem{Integrated GPT-4 for response generation; achieved \textbf{87\% answer correctness} on internal eval set}
            \resumeItem{Built Streamlit UI with source-document highlighting; reduced manual document search time by 70\%}
          \resumeItemListEnd"""
    },

]

# ------------------------------------------------------------ #
# INSTRUCTIONS TO ADD YOUR OWN PROJECTS:
#
# 1. Copy one of the entries above.
# 2. Replace all fields with your actual project details.
# 3. For latex_entry, use the same LaTeX commands your
#    resume_template.tex uses for the projects section.
# 4. Make sure your latex_entry is a raw string (r"""...""")
#    to avoid issues with backslashes.
# ------------------------------------------------------------ #
