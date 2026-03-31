# 🧠 Neural Speech Decoding via EEG → sEEG Transfer

This project investigates the transfer of deep learning architectures from non-invasive EEG to invasive sEEG for neural speech decoding.

## 🚀 Overview

We propose a hybrid deep learning framework that integrates **Multi-Receptive Residual Blocks (MR-ResBlocks)** into a neural decoding pipeline for reconstructing mel-spectrograms from intracranial brain signals.

The study focuses on:
- Cross-modality transfer (EEG → sEEG)
- Handling heterogeneous electrode configurations
- Improving reconstruction performance (PCC & MSE)

---

## 📊 Key Results

- **PCC improvement:** 0.288 → 0.400  
- **MSE reduction:** 4.567 → 4.194  
- Consistent improvements across all subjects (p = 0.002)

---

## 🧠 Method

- Hybrid architecture combining:
  - CNN-based feature extraction
  - Temporal modeling
  - MR-ResBlocks transfer
- Progressive fine-tuning strategy
- Binary channel masking for multi-subject learning

---

## 📁 Project Structure
