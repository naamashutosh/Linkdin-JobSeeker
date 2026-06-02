'''
YOUR PROJECTS LIST — Ashutosh Verma (19 projects)
Full descriptions are kept for ATS keyword density.
The single-page enforcement in resume_customizer.py automatically
drops the least-relevant project if the resume exceeds 1 page.
'''

projects_list = [

    {
        "name": "Embedded Deployment of Oral Cancer Detection Model",
        "description": "TensorFlow/Keras oral cancer model ported to Raspberry Pi 4B with real-time audio pipeline, MFCC+Mel+WST-2D features, ONNX Runtime and PyTorch C++ for sub-200ms ARM inference. IEEE EMBC.",
        "domains": ["Embedded Systems", "Audio Processing", "Speech Processing", "Clinical AI", "Deep Learning", "Signal Processing", "Edge AI", "TinyML", "Healthcare AI"],
        "tech_stack": ["Python", "C++", "TensorFlow", "Keras", "ONNX Runtime", "PyTorch C++", "Raspberry Pi", "MFCC", "h5py"],
        "date_range": "2026-01",
        "latex_entry": r"""\resumeSubItem{Embedded Deployment of Oral Cancer Detection Model (Python/C++, Raspberry Pi 4B) \hfill {\normalsize Jan 2026 -- Present}}{
Ported a TensorFlow/Keras model to Raspberry Pi 4B by rebuilding the architecture with h5py weight loading, resolving critical version incompatibilities. Developed a real-time pipeline for USB microphone input at 48\,kHz resampled to 16\,kHz with MFCC + Mel + WST-2D feature extraction; optimized with ONNX Runtime and PyTorch C++ bindings for sub-200\,ms ARM inference. (IEEE EMBC)
}"""
    },

    {
        "name": "VMD-TriMCAN for Oral Cancer Detection",
        "description": "Variational Mode Decomposition with Tri-Modal Cross-Attention Network for speech-based oral cancer screening achieving ~95.12% accuracy. Accepted NCC 2026.",
        "domains": ["Signal Processing", "Audio Processing", "Speech Processing", "Clinical AI", "Deep Learning", "Machine Learning", "Healthcare AI", "Attention Mechanism"],
        "tech_stack": ["Python", "PyTorch", "VMD", "Attention Mechanism", "MFCC", "Mel Spectrogram", "Scikit-learn"],
        "date_range": "2025-10",
        "latex_entry": r"""\resumeSubItem{VMD-TriMCAN for Oral Cancer Detection (Signal Processing, Multi-Modal Attention) \hfill {\normalsize NCC 2026}}{
Developed a Variational Mode Decomposition with Tri-Modal Cross-Attention Network for speech-based oral cancer screening, achieving $\sim$95.12\% accuracy across multilingual datasets. Accepted at National Conference on Communications (NCC) 2026.
}"""
    },

    {
        "name": "Image-Based Oral Cancer Detection using Vision Transformers",
        "description": "ViT + CNN hybrid for early-stage oral lesion classification on 1,000+ clinical images achieving 90.6% accuracy with wavelet-based preprocessing and PyTorch C++ edge deployment.",
        "domains": ["Computer Vision", "Machine Learning", "Deep Learning", "Healthcare AI", "Image Classification", "Clinical AI", "Edge AI"],
        "tech_stack": ["Python", "PyTorch", "Vision Transformer (ViT)", "CNN", "OpenCV", "Wavelet Transform", "ONNX", "PyTorch C++"],
        "date_range": "2025-02",
        "latex_entry": r"""\resumeSubItem{Image-Based Oral Cancer Detection using Vision Transformers (Computer Vision, AI/ML) \hfill {\normalsize Feb -- April 2025}}{
Built a ViT + CNN hybrid model for early-stage oral lesion classification from 1{,}000+ annotated clinical and histopathological images, achieving 90.6\% accuracy. Applied wavelet-based texture enhancement and contrast normalization; optimized inference latency using PyTorch C++ bindings for edge deployment.
}"""
    },

    {
        "name": "5G NR L1/L2 Protocol Stack Mini-Simulator",
        "description": "NR modem stack in MATLAB/C++ covering PHY (LDPC, OFDM, DM-RS, HARQ) and MAC (CQI-based MCS, round-robin scheduling). BLER vs SNR KPIs verified against 3GPP 38.211/212/214/321.",
        "domains": ["Wireless Communication", "5G NR", "Telecommunications", "Signal Processing", "Embedded Systems", "Software Engineering"],
        "tech_stack": ["MATLAB", "C++", "LDPC", "OFDM", "HARQ", "3GPP", "PHY Layer", "MAC Layer"],
        "date_range": "2025-01",
        "latex_entry": r"""\resumeSubItem{5G NR L1/L2 Protocol Stack Mini-Simulator (3GPP 38.xxx) \hfill {\normalsize 2025 -- Present}}{
Implemented a Phase-1 NR modem stack covering PHY (LDPC encoder/decoder, OFDM modulator, DM-RS channel estimation, HARQ combining) and MAC (TB segmentation, CQI-based MCS selection, round-robin scheduling) in MATLAB/C++. Generated BLER vs SNR, throughput, and HARQ efficiency KPIs; verified compliance with 3GPP 38.211/212/214/321.
}"""
    },

    {
        "name": "NR/LTE RRC Signaling Simulator & Call Flow Debugger",
        "description": "Simulated RRC flows (Connection Setup, Reconfiguration, Security Mode, Handover) with PDCP/RLC AM retransmission. PCAP-like NAS/RRC message logging per 3GPP 38.300 & 36.331.",
        "domains": ["Wireless Communication", "5G NR", "LTE", "Telecommunications", "Networking", "Software Engineering", "Protocol Stack"],
        "tech_stack": ["Python", "C++", "RRC", "PDCP", "RLC", "3GPP", "PCAP", "Wireshark"],
        "date_range": "2024-10",
        "latex_entry": r"""\resumeSubItem{NR/LTE RRC Signaling Simulator \& Call Flow Debugger \hfill {\normalsize 2024 -- Present}}{
Simulated complete RRC flows (Connection Setup, Reconfiguration, Security Mode, Handover) with PDCP/RLC sequence numbering, reordering, and AM retransmission logic. Created PCAP-like NAS/RRC message logging utilities following 3GPP 38.300 \& 36.331 for state machine verification.
}"""
    },

    {
        "name": "Real-Time RF Signal Classification System",
        "description": "CNN classifier for 11 wireless modulation types achieving 92%+ accuracy on 220K I/Q samples from RadioML. Spectrogram-based neural pipeline for automatic modulation recognition.",
        "domains": ["Wireless Communication", "RF Signal Processing", "Machine Learning", "Deep Learning", "Spectrum Monitoring", "Signal Processing"],
        "tech_stack": ["Python", "PyTorch", "CNN", "RadioML", "I/Q Samples", "Spectrogram", "Scikit-learn"],
        "date_range": "2025-05",
        "latex_entry": r"""\resumeSubItem{Real-Time RF Signal Classification System (Deep Learning, Spectrum Monitoring) \hfill {\normalsize May -- July 2025}}{
Built a CNN-based classifier for 11 wireless modulation types achieving 92\%+ accuracy on 220K I/Q samples from the RadioML dataset. Implemented a spectrogram-based neural pipeline for automatic modulation recognition in real-time spectrum monitoring scenarios.
}"""
    },

    {
        "name": "Performance Analysis of Wireless Systems",
        "description": "MATLAB simulations of BPSK, QPSK, OFDM, BER vs SNR, Rayleigh fading, channel equalization, and 3x3 SVD-MIMO channel under AWGN and fading conditions.",
        "domains": ["Wireless Communication", "Signal Processing", "MIMO", "Telecommunications", "MATLAB", "DSP"],
        "tech_stack": ["MATLAB", "OFDM", "BPSK", "QPSK", "MIMO", "SVD", "Channel Equalization"],
        "date_range": "2025-01",
        "latex_entry": r"""\resumeSubItem{Performance Analysis of Wireless Systems (MATLAB, DSP, Communications) \hfill {\normalsize Jan -- April 2025}}{
Simulated BPSK, QPSK, OFDM, BER vs SNR curves, Rayleigh fading, and channel equalization in MATLAB; designed a $3\times3$ SVD-MIMO channel and verified analytical vs simulated SNR under AWGN and fading conditions. Supported 4G/5G physical layer understanding.
}"""
    },

    {
        "name": "Advanced RF & Microwave Design — ADS Projects",
        "description": "Designed Wilkinson Power Divider, Hybrid Coupler, and Binomial/Chebyshev multi-section transformers in ADS. Achieved target impedance matching and minimum reflection coefficient.",
        "domains": ["RF Engineering", "Microwave Design", "Wireless Communication", "Hardware Design", "Antenna Design", "Signal Processing"],
        "tech_stack": ["ADS (Advanced Design System)", "RF Design", "Microwave Engineering", "Filter Design", "S-Parameters"],
        "date_range": "2025-08",
        "latex_entry": r"""\resumeSubItem{Advanced RF \& Microwave Design --- ADS Projects \hfill {\normalsize Aug -- Dec 2025}}{
Designed Wilkinson Power Divider, Hybrid Coupler, and Binomial/Chebyshev multi-section impedance transformers in ADS. Achieved target impedance matching and minimum reflection coefficient across designed filter and coupler structures.
}"""
    },

    {
        "name": "Wi-Fi Security Protocol Analysis: WPA2 vs WPA3-SAE",
        "description": "Deployed WPA2/WPA3-SAE APs via hostapd on Raspberry Pi; captured EAPOL handshakes and SAE frames using airmon-ng and Wireshark; built scapy/pyshark pipeline to extract nonces and MIC fields.",
        "domains": ["Networking", "Cybersecurity", "Wireless Communication", "Linux", "Software Engineering", "Protocol Analysis"],
        "tech_stack": ["Python", "Linux", "Raspberry Pi", "hostapd", "Wireshark", "scapy", "pyshark", "airmon-ng"],
        "date_range": "2025-06",
        "latex_entry": r"""\resumeSubItem{Wi-Fi Security Protocol Analysis: WPA2 vs WPA3-SAE (Linux, Networking, Python) \hfill {\normalsize 2025}}{
Deployed WPA2-PSK and WPA3-SAE access points using hostapd on Raspberry Pi; captured EAPOL 4-way handshakes and SAE commit/confirm frames with airmon-ng and Wireshark. Built a scapy/pyshark pipeline to extract nonces, MIC fields, and timing statistics for comparative security analysis.
}"""
    },

    {
        "name": "ML-Driven 1-Bit Metasurface Optimization for Patch Antennas",
        "description": "GA + surrogate-model optimization for 1-bit Polarization Conversion Metasurface coding patterns, achieving 28 dB RCS reduction at 10.8 GHz and 0.9 polarization conversion ratio.",
        "domains": ["Antenna Design", "RF Engineering", "Machine Learning", "Microwave Design", "Wireless Communication", "Metasurface"],
        "tech_stack": ["MATLAB", "Python", "Genetic Algorithm", "Surrogate Modeling", "CST/HFSS", "Metasurface Design"],
        "date_range": "2021-01",
        "latex_entry": r"""\resumeSubItem{ML-Driven 1-Bit Metasurface Optimization for Patch Antennas \hfill {\normalsize B.Tech Major Project, 2021}}{
Implemented GA + surrogate-model optimization to generate 1-bit coding patterns for a Polarization Conversion Metasurface, achieving 28\,dB RCS reduction at 10.8\,GHz with 0.9 polarization conversion ratio when integrated with a 6.28\,GHz patch antenna.
}"""
    },

    {
        "name": "Embedded DSP Real-Time Pipeline on TI TMDSLCDK6748",
        "description": "FIR/IIR filter banks and FFT kernels in bare-metal Embedded C on TI C6748 with cycle-accurate execution; UART debug interface; CCS profiling reduced critical loop cycle count by ~30%.",
        "domains": ["Embedded Systems", "DSP", "Signal Processing", "Firmware", "Real-Time Systems", "C/C++"],
        "tech_stack": ["Embedded C", "TI C6748", "TI TMDSLCDK6748", "CCS", "UART", "FFT", "FIR/IIR"],
        "date_range": "2024-08",
        "latex_entry": r"""\resumeSubItem{Embedded DSP Real-Time Pipeline on TI TMDSLCDK6748 (C / Embedded C) \hfill {\normalsize Aug -- Dec 2024}}{
Implemented FIR/IIR filter banks and FFT kernels in bare-metal Embedded C on TI C6748 with cycle-accurate execution. Designed a UART debug interface with structured logging; profiled bottlenecks via CCS instrumentation, reducing critical loop cycle count by $\sim$30\%.
}"""
    },

    {
        "name": "FreeRTOS Multi-Task Sensor Scheduler",
        "description": "Priority-based FreeRTOS application on STM32 for concurrent sensor polling, data processing, and UART telemetry; inter-task queues and semaphores; validated deterministic latency with fault injection.",
        "domains": ["Embedded Systems", "RTOS", "Firmware", "IoT", "Real-Time Systems", "C/C++"],
        "tech_stack": ["C", "FreeRTOS", "STM32", "ARM Cortex-M", "UART", "Semaphores", "Queues"],
        "date_range": "2025-01",
        "latex_entry": r"""\resumeSubItem{FreeRTOS Multi-Task Sensor Scheduler (C, STM32 / ARM Cortex-M) \hfill {\normalsize Jan 2025}}{
Built a priority-based multi-task application on STM32 with FreeRTOS for concurrent sensor polling, data processing, and UART telemetry. Designed inter-task communication via queues and semaphores; validated deterministic latency with fault injection unit tests.
}"""
    },

    {
        "name": "Bare-Metal UART Bootloader for STM32",
        "description": "Custom bootloader in bare-metal C for in-field STM32 firmware updates over UART with CRC32 integrity, flash sector erase/write, VTOR relocation, jump-to-application, and power-loss recovery.",
        "domains": ["Embedded Systems", "Firmware", "Bootloader", "Real-Time Systems", "C/C++", "Microcontroller"],
        "tech_stack": ["Bare-Metal C", "STM32", "UART", "CRC32", "Flash Memory", "ARM Cortex-M"],
        "date_range": "2025-10",
        "latex_entry": r"""\resumeSubItem{Bare-Metal UART Bootloader for STM32 (Bare-Metal C) \hfill {\normalsize Oct 2025}}{
Designed a custom bootloader in bare-metal C supporting in-field firmware updates over UART with CRC32 integrity verification. Implemented flash sector erase/write, SCB VTOR relocation, jump-to-application, and power-loss recovery with partial-write detection.
}"""
    },

    {
        "name": "Multilingual Text & Audio Classification for Interactive Systems",
        "description": "Multimodal transformer fusing Wav2Vec2 (audio) and BERT (text) for multilingual intent recognition; 20% throughput improvement via ONNX quantization and dynamic batching; FastAPI endpoint.",
        "domains": ["NLP", "Audio Processing", "Machine Learning", "Transformers", "MLOps", "Speech Recognition", "Multimodal AI", "Software Engineering"],
        "tech_stack": ["Python", "Wav2Vec2", "BERT", "HuggingFace", "ONNX", "PyTorch", "FastAPI", "Docker"],
        "date_range": "2022-03",
        "latex_entry": r"""\resumeSubItem{Multilingual Text \& Audio Classification for Interactive Systems (NLP, Transformers, MLOps) \hfill {\normalsize Mar 2022 -- Sep 2023}}{
Developed a multimodal transformer fusing Wav2Vec2 (audio) and BERT (text) for multilingual intent recognition supporting real-time interactive workflows. Improved inference throughput by 20\% via ONNX quantization and dynamic batching; deployed via scalable FastAPI endpoint for low-latency integration.
}"""
    },

    {
        "name": "End-to-End NLP Pipeline for Multi-Domain Text Classification",
        "description": "Fine-tuned DistilBERT on AG News and 20 Newsgroups achieving 93%+ accuracy; SMOTE, data augmentation, SHAP + attention explainability; ONNX export and FastAPI deployment.",
        "domains": ["NLP", "Machine Learning", "Deep Learning", "Transformers", "Text Classification", "MLOps", "Data Science"],
        "tech_stack": ["Python", "DistilBERT", "HuggingFace", "ONNX Runtime", "FastAPI", "SHAP", "Scikit-learn", "PyTorch"],
        "date_range": "2025-01",
        "latex_entry": r"""\resumeSubItem{End-to-End NLP Pipeline for Multi-Domain Text Classification (NLP, Transformers) \hfill {\normalsize Jan -- Mar 2025}}{
Fine-tuned DistilBERT on AG News and 20 Newsgroups for multi-class classification achieving 93\%+ accuracy; applied data augmentation, SMOTE, and attention-weight + SHAP explainability layer. Exported via ONNX Runtime and deployed as a FastAPI REST service for scalable production NLP inference.
}"""
    },

    {
        "name": "Big Data Analytics Pipeline for Healthcare Insights",
        "description": "Scalable PySpark + SQL pipeline on MIMIC-III synthetic clinical records (2M+ patient records) with data governance, schema validation, lineage tracking, and AWS S3 analytical dashboards.",
        "domains": ["Data Engineering", "Big Data", "Cloud", "Healthcare AI", "Data Science", "SQL", "ETL", "Analytics"],
        "tech_stack": ["PySpark", "SQL", "AWS S3", "Python", "Pandas", "NumPy", "Data Governance", "ETL"],
        "date_range": "2025-05",
        "latex_entry": r"""\resumeSubItem{Big Data Analytics Pipeline for Healthcare Insights (PySpark, SQL, Data Engineering) \hfill {\normalsize May -- July 2025}}{
Designed a scalable ingestion and transformation pipeline using PySpark and SQL on a MIMIC-III synthetic clinical dataset, processing 2M+ patient records end-to-end. Applied data governance (schema validation, deduplication, lineage tracking) with analytical dashboards integrated on AWS S3.
}"""
    },

    {
        "name": "Vehicle Detection & Classification using YOLOv8",
        "description": "Fine-tuned YOLOv8s achieving mAP@0.5 of 0.89 at 60+ FPS; ONNX/TensorRT FP16 export for NVIDIA Jetson with ~2.5x speed-up over native PyTorch.",
        "domains": ["Computer Vision", "Object Detection", "Edge AI", "Deep Learning", "Machine Learning", "Embedded Systems"],
        "tech_stack": ["Python", "YOLOv8", "PyTorch", "ONNX", "TensorRT", "NVIDIA Jetson", "OpenCV"],
        "date_range": "2026-01",
        "latex_entry": r"""\resumeSubItem{Vehicle Detection \& Classification using YOLOv8 (Computer Vision, Edge Deployment) \hfill {\normalsize Jan -- Mar 2026}}{
Fine-tuned YOLOv8s on a multi-class vehicle dataset; achieved mAP@0.5 of 0.89 at 60+ FPS. Exported to ONNX/TensorRT FP16 for NVIDIA Jetson edge deployment with $\sim$2.5$\times$ speed-up over native PyTorch inference.
}"""
    },

    {
        "name": "Monocular Visual Odometry on KITTI Dataset",
        "description": "Monocular VO pipeline using ORB features, RANSAC essential matrix, and pose recovery on KITTI Sequence 00; ATE benchmarking with evo toolkit; ORB vs SIFT trade-off analysis for UAV deployment.",
        "domains": ["Computer Vision", "SLAM", "Robotics", "Deep Learning", "Machine Learning", "Edge AI"],
        "tech_stack": ["Python", "OpenCV", "ORB", "SIFT", "RANSAC", "evo toolkit", "KITTI Dataset"],
        "date_range": "2025-12",
        "latex_entry": r"""\resumeSubItem{Monocular Visual Odometry on KITTI Dataset (SLAM, Classical CV) \hfill {\normalsize Dec 2025 -- Feb 2026}}{
Built a monocular VO pipeline using ORB features, RANSAC-based essential matrix estimation, and pose recovery on KITTI Sequence 00; benchmarked trajectory against ground truth via ATE using the \textit{evo} toolkit. Compared ORB vs SIFT for repeatability and runtime relevant to real-time UAV deployment.
}"""
    },

    {
        "name": "Independent Audio Engineering & DSP Projects",
        "description": "Produced and mixed 100+ rap/vocal tracks in FL Studio with EQ, compression, reverb, mastering, and denoising. Real-time audio restoration chains in Python; strong psychoacoustics foundation.",
        "domains": ["Audio Processing", "Signal Processing", "DSP", "Music Production", "Speech Processing"],
        "tech_stack": ["Python", "FL Studio", "Librosa", "NumPy", "SciPy", "Audio DSP"],
        "date_range": "2018-01",
        "latex_entry": r"""\resumeSubItem{Independent Audio Engineering \& DSP Projects \hfill {\normalsize 2018 -- Present}}{
Produced and mixed 100+ rap/vocal tracks in FL Studio applying EQ, compression, reverb, mastering, and denoising. Implemented real-time audio restoration chains in Python; built strong understanding of psychoacoustics, spectral shaping, and frequency balance.
}"""
    },

]

# -----------------------------------------------------------------------
# TO ADD A NEW PROJECT:
# "latex_entry": r"""\resumeSubItem{Title (Tags) \hfill {\normalsize Date}}{
# Description — 1-2 sentences with measurable results and tech keywords.
# }"""
# -----------------------------------------------------------------------
