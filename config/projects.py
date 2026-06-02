'''
YOUR PROJECTS LIST — Ashutosh Verma (19 projects)
Each latex_entry uses a SINGLE concise description line to keep the
generated resume strictly on 1 page.
'''

projects_list = [

    {
        "name": "Embedded Deployment of Oral Cancer Detection Model",
        "description": "TensorFlow/Keras oral cancer model on Raspberry Pi 4B with real-time audio pipeline, MFCC+Mel+WST-2D features, ONNX Runtime and PyTorch C++ for sub-200ms ARM inference. IEEE EMBC.",
        "domains": ["Embedded Systems", "Audio Processing", "Speech Processing", "Clinical AI", "Deep Learning", "Signal Processing", "Edge AI", "TinyML", "Healthcare AI"],
        "tech_stack": ["Python", "C++", "TensorFlow", "Keras", "ONNX Runtime", "PyTorch C++", "Raspberry Pi", "MFCC", "h5py"],
        "date_range": "2026-01",
        "latex_entry": r"""\resumeSubItem{Embedded Deployment of Oral Cancer Detection Model (Python/C++, Raspberry Pi 4B) \hfill {\normalsize Jan 2026 -- Present}}{Ported TF/Keras model to RPi 4B; real-time audio pipeline (48kHz, MFCC+Mel+WST-2D), ONNX Runtime + PyTorch C++ bindings for sub-200ms ARM inference. (IEEE EMBC)}"""
    },

    {
        "name": "VMD-TriMCAN for Oral Cancer Detection",
        "description": "Variational Mode Decomposition with Tri-Modal Cross-Attention Network for speech-based oral cancer screening achieving ~95.12% accuracy. Accepted NCC 2026.",
        "domains": ["Signal Processing", "Audio Processing", "Speech Processing", "Clinical AI", "Deep Learning", "Machine Learning", "Healthcare AI", "Attention Mechanism"],
        "tech_stack": ["Python", "PyTorch", "VMD", "Attention Mechanism", "MFCC", "Mel Spectrogram", "Scikit-learn"],
        "date_range": "2025-10",
        "latex_entry": r"""\resumeSubItem{VMD-TriMCAN for Oral Cancer Detection (Signal Processing, Multi-Modal Attention) \hfill {\normalsize NCC 2026}}{VMD + Tri-Modal Cross-Attention Network for speech-based oral cancer screening; achieved $\sim$95.12\% accuracy. Accepted NCC 2026.}"""
    },

    {
        "name": "Image-Based Oral Cancer Detection using Vision Transformers",
        "description": "ViT + CNN hybrid for early-stage oral lesion classification on 1,000+ clinical images achieving 90.6% accuracy with wavelet-based preprocessing and PyTorch C++ edge deployment.",
        "domains": ["Computer Vision", "Machine Learning", "Deep Learning", "Healthcare AI", "Image Classification", "Clinical AI", "Edge AI"],
        "tech_stack": ["Python", "PyTorch", "Vision Transformer (ViT)", "CNN", "OpenCV", "Wavelet Transform", "ONNX", "PyTorch C++"],
        "date_range": "2025-02",
        "latex_entry": r"""\resumeSubItem{Image-Based Oral Cancer Detection using Vision Transformers (Computer Vision, AI/ML) \hfill {\normalsize Feb -- April 2025}}{ViT + CNN hybrid on 1{,}000+ annotated histopathological images; 90.6\% accuracy with wavelet texture enhancement. Optimized via PyTorch C++ for edge deployment.}"""
    },

    {
        "name": "5G NR L1/L2 Protocol Stack Mini-Simulator",
        "description": "NR modem stack in MATLAB/C++ covering PHY (LDPC, OFDM, DM-RS, HARQ) and MAC (CQI-based MCS, round-robin scheduling). BLER vs SNR KPIs verified against 3GPP 38.211/212/214/321.",
        "domains": ["Wireless Communication", "5G NR", "Telecommunications", "Signal Processing", "Embedded Systems", "Software Engineering"],
        "tech_stack": ["MATLAB", "C++", "LDPC", "OFDM", "HARQ", "3GPP", "PHY Layer", "MAC Layer"],
        "date_range": "2025-01",
        "latex_entry": r"""\resumeSubItem{5G NR L1/L2 Protocol Stack Mini-Simulator (3GPP 38.xxx) \hfill {\normalsize 2025 -- Present}}{NR modem: PHY (LDPC, OFDM, DM-RS, HARQ) + MAC (CQI-based MCS, scheduling) in MATLAB/C++; BLER vs SNR and throughput KPIs verified vs 3GPP 38.211/212/214/321.}"""
    },

    {
        "name": "NR/LTE RRC Signaling Simulator & Call Flow Debugger",
        "description": "Simulated RRC flows (Connection Setup, Reconfiguration, Security Mode, Handover) with PDCP/RLC AM retransmission. PCAP-like NAS/RRC message logging per 3GPP 38.300 & 36.331.",
        "domains": ["Wireless Communication", "5G NR", "LTE", "Telecommunications", "Networking", "Software Engineering", "Protocol Stack"],
        "tech_stack": ["Python", "C++", "RRC", "PDCP", "RLC", "3GPP", "PCAP", "Wireshark"],
        "date_range": "2024-10",
        "latex_entry": r"""\resumeSubItem{NR/LTE RRC Signaling Simulator \& Call Flow Debugger \hfill {\normalsize 2024 -- Present}}{Simulated RRC flows (Setup, Reconfig, Security Mode, Handover) with PDCP/RLC AM retransmission; PCAP-like NAS/RRC logging per 3GPP 38.300 \& 36.331.}"""
    },

    {
        "name": "Real-Time RF Signal Classification System",
        "description": "CNN classifier for 11 wireless modulation types achieving 92%+ accuracy on 220K I/Q samples from RadioML. Spectrogram-based neural pipeline for automatic modulation recognition.",
        "domains": ["Wireless Communication", "RF Signal Processing", "Machine Learning", "Deep Learning", "Spectrum Monitoring", "Signal Processing"],
        "tech_stack": ["Python", "PyTorch", "CNN", "RadioML", "I/Q Samples", "Spectrogram", "Scikit-learn"],
        "date_range": "2025-05",
        "latex_entry": r"""\resumeSubItem{Real-Time RF Signal Classification System (Deep Learning, Spectrum Monitoring) \hfill {\normalsize May -- July 2025}}{CNN classifier for 11 modulation types; 92\%+ accuracy on 220K I/Q RadioML samples with spectrogram-based neural pipeline for automatic modulation recognition.}"""
    },

    {
        "name": "Performance Analysis of Wireless Systems",
        "description": "MATLAB simulations of BPSK, QPSK, OFDM, BER vs SNR, Rayleigh fading, channel equalization, and 3x3 SVD-MIMO channel under AWGN and fading conditions.",
        "domains": ["Wireless Communication", "Signal Processing", "MIMO", "Telecommunications", "MATLAB", "DSP"],
        "tech_stack": ["MATLAB", "OFDM", "BPSK", "QPSK", "MIMO", "SVD", "Channel Equalization"],
        "date_range": "2025-01",
        "latex_entry": r"""\resumeSubItem{Performance Analysis of Wireless Systems (MATLAB, DSP, Communications) \hfill {\normalsize Jan -- April 2025}}{Simulated BPSK/QPSK/OFDM BER vs SNR, Rayleigh fading, and $3\times3$ SVD-MIMO channel in MATLAB under AWGN and fading conditions.}"""
    },

    {
        "name": "Advanced RF & Microwave Design — ADS Projects",
        "description": "Designed Wilkinson Power Divider, Hybrid Coupler, and Binomial/Chebyshev multi-section transformers in ADS. Achieved target impedance matching and minimum reflection coefficient.",
        "domains": ["RF Engineering", "Microwave Design", "Wireless Communication", "Hardware Design", "Antenna Design", "Signal Processing"],
        "tech_stack": ["ADS (Advanced Design System)", "RF Design", "Microwave Engineering", "Filter Design", "S-Parameters"],
        "date_range": "2025-08",
        "latex_entry": r"""\resumeSubItem{Advanced RF \& Microwave Design --- ADS Projects \hfill {\normalsize Aug -- Dec 2025}}{Designed Wilkinson Power Divider, Hybrid Coupler, and Binomial/Chebyshev transformers in ADS; achieved target impedance matching and minimum reflection coefficient.}"""
    },

    {
        "name": "Wi-Fi Security Protocol Analysis: WPA2 vs WPA3-SAE",
        "description": "Deployed WPA2/WPA3-SAE APs via hostapd on Raspberry Pi; captured EAPOL handshakes and SAE frames using airmon-ng and Wireshark; built scapy/pyshark pipeline to extract nonces and MIC fields.",
        "domains": ["Networking", "Cybersecurity", "Wireless Communication", "Linux", "Software Engineering", "Protocol Analysis"],
        "tech_stack": ["Python", "Linux", "Raspberry Pi", "hostapd", "Wireshark", "scapy", "pyshark", "airmon-ng"],
        "date_range": "2025-06",
        "latex_entry": r"""\resumeSubItem{Wi-Fi Security Protocol Analysis: WPA2 vs WPA3-SAE (Linux, Networking, Python) \hfill {\normalsize 2025}}{Deployed WPA2/WPA3-SAE APs via hostapd on RPi; captured EAPOL handshakes and SAE frames (airmon-ng, Wireshark); scapy/pyshark pipeline to extract nonces and MIC fields.}"""
    },

    {
        "name": "ML-Driven 1-Bit Metasurface Optimization for Patch Antennas",
        "description": "GA + surrogate-model optimization for 1-bit Polarization Conversion Metasurface coding patterns, achieving 28 dB RCS reduction at 10.8 GHz and 0.9 polarization conversion ratio.",
        "domains": ["Antenna Design", "RF Engineering", "Machine Learning", "Microwave Design", "Wireless Communication", "Metasurface"],
        "tech_stack": ["MATLAB", "Python", "Genetic Algorithm", "Surrogate Modeling", "CST/HFSS", "Metasurface Design"],
        "date_range": "2021-01",
        "latex_entry": r"""\resumeSubItem{ML-Driven 1-Bit Metasurface Optimization for Patch Antennas \hfill {\normalsize B.Tech Major Project 2021}}{GA + surrogate-model optimization for 1-bit coding patterns; 28 dB RCS reduction at 10.8 GHz, 0.9 polarization conversion ratio integrated with a 6.28 GHz patch antenna.}"""
    },

    {
        "name": "Embedded DSP Real-Time Pipeline on TI TMDSLCDK6748",
        "description": "FIR/IIR filter banks and FFT kernels in bare-metal Embedded C on TI C6748 with cycle-accurate execution; UART debug interface; CCS profiling reduced critical loop cycle count by ~30%.",
        "domains": ["Embedded Systems", "DSP", "Signal Processing", "Firmware", "Real-Time Systems", "C/C++"],
        "tech_stack": ["Embedded C", "TI C6748", "TI TMDSLCDK6748", "CCS", "UART", "FFT", "FIR/IIR"],
        "date_range": "2024-08",
        "latex_entry": r"""\resumeSubItem{Embedded DSP Real-Time Pipeline on TI TMDSLCDK6748 (C / Embedded C) \hfill {\normalsize Aug -- Dec 2024}}{FIR/IIR filter banks and FFT kernels in bare-metal Embedded C on TI C6748; UART debug interface; CCS profiling reduced critical loop cycle count by $\sim$30\%.}"""
    },

    {
        "name": "FreeRTOS Multi-Task Sensor Scheduler",
        "description": "Priority-based FreeRTOS application on STM32 for concurrent sensor polling, data processing, and UART telemetry; inter-task queues and semaphores; validated deterministic latency with fault injection.",
        "domains": ["Embedded Systems", "RTOS", "Firmware", "IoT", "Real-Time Systems", "C/C++"],
        "tech_stack": ["C", "FreeRTOS", "STM32", "ARM Cortex-M", "UART", "Semaphores", "Queues"],
        "date_range": "2025-01",
        "latex_entry": r"""\resumeSubItem{FreeRTOS Multi-Task Sensor Scheduler (C, STM32 / ARM Cortex-M) \hfill {\normalsize Jan 2025}}{Priority-based FreeRTOS tasks on STM32 for concurrent sensor polling and UART telemetry; inter-task queues/semaphores; validated deterministic latency with fault injection tests.}"""
    },

    {
        "name": "Bare-Metal UART Bootloader for STM32",
        "description": "Custom bootloader in bare-metal C for in-field STM32 firmware updates over UART with CRC32 integrity, flash sector erase/write, VTOR relocation, jump-to-application, and power-loss recovery.",
        "domains": ["Embedded Systems", "Firmware", "Bootloader", "Real-Time Systems", "C/C++", "Microcontroller"],
        "tech_stack": ["Bare-Metal C", "STM32", "UART", "CRC32", "Flash Memory", "ARM Cortex-M"],
        "date_range": "2025-10",
        "latex_entry": r"""\resumeSubItem{Bare-Metal UART Bootloader for STM32 (Bare-Metal C) \hfill {\normalsize Oct 2025}}{In-field firmware update over UART with CRC32 integrity; flash erase/write, SCB VTOR relocation, jump-to-application, and power-loss recovery with partial-write detection.}"""
    },

    {
        "name": "Multilingual Text & Audio Classification for Interactive Systems",
        "description": "Multimodal transformer fusing Wav2Vec2 (audio) and BERT (text) for multilingual intent recognition; 20% throughput improvement via ONNX quantization and dynamic batching; FastAPI endpoint.",
        "domains": ["NLP", "Audio Processing", "Machine Learning", "Transformers", "MLOps", "Speech Recognition", "Multimodal AI", "Software Engineering"],
        "tech_stack": ["Python", "Wav2Vec2", "BERT", "HuggingFace", "ONNX", "PyTorch", "FastAPI", "Docker"],
        "date_range": "2022-03",
        "latex_entry": r"""\resumeSubItem{Multilingual Text \& Audio Classification for Interactive Systems (NLP, Transformers, MLOps) \hfill {\normalsize Mar 2022 -- Sep 2023}}{Multimodal transformer (Wav2Vec2 + BERT) for multilingual intent recognition; 20\% throughput gain via ONNX quantization and dynamic batching; deployed via FastAPI endpoint.}"""
    },

    {
        "name": "End-to-End NLP Pipeline for Multi-Domain Text Classification",
        "description": "Fine-tuned DistilBERT on AG News and 20 Newsgroups achieving 93%+ accuracy; SMOTE, data augmentation, SHAP + attention explainability; ONNX export and FastAPI deployment.",
        "domains": ["NLP", "Machine Learning", "Deep Learning", "Transformers", "Text Classification", "MLOps", "Data Science"],
        "tech_stack": ["Python", "DistilBERT", "HuggingFace", "ONNX Runtime", "FastAPI", "SHAP", "Scikit-learn", "PyTorch"],
        "date_range": "2025-01",
        "latex_entry": r"""\resumeSubItem{End-to-End NLP Pipeline for Multi-Domain Text Classification (NLP, Transformers) \hfill {\normalsize Jan -- Mar 2025}}{Fine-tuned DistilBERT on AG News and 20 Newsgroups; 93\%+ accuracy with SMOTE + SHAP explainability; ONNX export deployed as FastAPI REST service.}"""
    },

    {
        "name": "Big Data Analytics Pipeline for Healthcare Insights",
        "description": "Scalable PySpark + SQL pipeline on MIMIC-III synthetic clinical records (2M+ patient records) with data governance, schema validation, lineage tracking, and AWS S3 analytical dashboards.",
        "domains": ["Data Engineering", "Big Data", "Cloud", "Healthcare AI", "Data Science", "SQL", "ETL", "Analytics"],
        "tech_stack": ["PySpark", "SQL", "AWS S3", "Python", "Pandas", "NumPy", "Data Governance", "ETL"],
        "date_range": "2025-05",
        "latex_entry": r"""\resumeSubItem{Big Data Analytics Pipeline for Healthcare Insights (PySpark, SQL, Data Engineering) \hfill {\normalsize May -- July 2025}}{PySpark + SQL pipeline on 2M+ MIMIC-III clinical records; schema validation, deduplication, lineage tracking; AWS S3-integrated analytical dashboards.}"""
    },

    {
        "name": "Vehicle Detection & Classification using YOLOv8",
        "description": "Fine-tuned YOLOv8s achieving mAP@0.5 of 0.89 at 60+ FPS; ONNX/TensorRT FP16 export for NVIDIA Jetson with ~2.5x speed-up over native PyTorch.",
        "domains": ["Computer Vision", "Object Detection", "Edge AI", "Deep Learning", "Machine Learning", "Embedded Systems"],
        "tech_stack": ["Python", "YOLOv8", "PyTorch", "ONNX", "TensorRT", "NVIDIA Jetson", "OpenCV"],
        "date_range": "2026-01",
        "latex_entry": r"""\resumeSubItem{Vehicle Detection \& Classification using YOLOv8 (Computer Vision, Edge Deployment) \hfill {\normalsize Jan -- Mar 2026}}{Fine-tuned YOLOv8s; mAP@0.5 = 0.89 at 60+ FPS. ONNX/TensorRT FP16 export for NVIDIA Jetson with $\sim$2.5$\times$ speed-up over native PyTorch.}"""
    },

    {
        "name": "Monocular Visual Odometry on KITTI Dataset",
        "description": "Monocular VO pipeline using ORB features, RANSAC essential matrix, and pose recovery on KITTI Sequence 00; ATE benchmarking with evo toolkit; ORB vs SIFT trade-off analysis for UAV deployment.",
        "domains": ["Computer Vision", "SLAM", "Robotics", "Deep Learning", "Machine Learning", "Edge AI"],
        "tech_stack": ["Python", "OpenCV", "ORB", "SIFT", "RANSAC", "evo toolkit", "KITTI Dataset"],
        "date_range": "2025-12",
        "latex_entry": r"""\resumeSubItem{Monocular Visual Odometry on KITTI Dataset (SLAM, Classical CV) \hfill {\normalsize Dec 2025 -- Feb 2026}}{Monocular VO: ORB features, RANSAC essential matrix, pose recovery on KITTI Seq 00; ATE benchmarked via \textit{evo}; ORB vs SIFT trade-off analysis for real-time UAV deployment.}"""
    },

    {
        "name": "Independent Audio Engineering & DSP Projects",
        "description": "Produced and mixed 100+ rap/vocal tracks in FL Studio with EQ, compression, reverb, mastering, and denoising. Real-time audio restoration chains in Python; strong psychoacoustics foundation.",
        "domains": ["Audio Processing", "Signal Processing", "DSP", "Music Production", "Speech Processing"],
        "tech_stack": ["Python", "FL Studio", "Librosa", "NumPy", "SciPy", "Audio DSP"],
        "date_range": "2018-01",
        "latex_entry": r"""\resumeSubItem{Independent Audio Engineering \& DSP Projects \hfill {\normalsize 2018 -- Present}}{Produced and mixed 100+ tracks in FL Studio (EQ, compression, reverb, mastering, denoising); real-time audio restoration in Python; strong psychoacoustics and spectral shaping foundation.}"""
    },

]

# -----------------------------------------------------------------------
# TO ADD A NEW PROJECT — copy this block and fill it in:
#
# {
#     "name": "Your Project Title",
#     "description": "Plain-English 2-3 sentence summary for AI matching.",
#     "domains": ["Domain1", "Domain2"],
#     "tech_stack": ["Python", "Framework"],
#     "date_range": "YYYY-MM",
#     "latex_entry": r"""\resumeSubItem{Title (Tags) \hfill {\normalsize Date}}{ONE concise line description with key metrics.}"""
# },
# Keep latex_entry descriptions to 1 line (max ~120 chars) for single-page enforcement.
# -----------------------------------------------------------------------
