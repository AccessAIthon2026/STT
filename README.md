# 🧤 Vision-to-Touch AI Glove  
### Edinburgh AccessAIthon Project  

> Converting computer vision into tactile feedback to enhance independence for visually impaired users.

---

## 📌 Overview

The **Vision-to-Touch AI Glove** is a wearable assistive system that translates visual object detection into haptic feedback.

Instead of relying solely on audio (which can be overwhelming in public environments), this system enables users to **feel nearby objects through vibration patterns**, creating a tactile sensory language powered by AI.

This project is being developed for the **Edinburgh AccessAIthon**, focusing on accessibility innovation for visually impaired individuals.

---

## 🎯 Problem Statement

Visually impaired individuals often face challenges when:

- Locating specific objects (e.g. *“Where is my glass?”*)
- Understanding spatial proximity of objects
- Navigating cluttered indoor environments

Audio-based assistive systems can:

- Overload hearing  
- Be impractical in noisy environments  
- Reduce situational awareness  

We aim to provide a **non-audio, tactile AI-based solution**.

---

## 🚀 Core Features

### 1️⃣ Find Mode (AI Object Search)

User says e.g. "Find my glass cup"


System pipeline:

1. Speech-to-text processes voice command  
2. Target object class is extracted  
3. YOLOv8 object detection runs on live camera feed  
4. The closest matching object is selected  
5. Distance is approximated via bounding box size  
6. Vibration intensity increases as user approaches the object  

This allows the user to scan their surroundings and physically feel proximity to their requested object.

---

### 2️⃣ Tactile Language System

Different vibration patterns represent different object categories:

| Object Type   | Vibration Pattern |
|--------------|------------------|
| Person       | Double pulse |
| Wall         | Continuous vibration |
| Furniture    | Slow pulse |
| Target object | Increasing intensity as distance decreases |

This creates a consistent, learnable tactile vocabulary.

---

## 🧠 AI Components

### 🔹 Object Detection
- Model: **YOLOv8** (pretrained on COCO dataset)
- Runs on laptop for real-time inference
- Detects relevant classes such as:
  - person
  - chair
  - table
  - cup
  - bottle
  - etc.

### 🔹 Speech Recognition
- Whisper-based speech-to-text
- Extracts object name from user command
- No large language model required (lightweight and reliable)

### 🔹 Distance Approximation
- Bounding box area used as proxy for depth
- Normalized to vibration intensity (0–255 scale)

---

## 🧰 Hardware Architecture

### Components

- USB Camera
- Arduino (Uno/Nano)
- 4–5 vibration motors
- NPN transistors (motor control)
- External power source
- Wearable glove platform

### Communication Flow

Python (AI inference)
↓
Serial (USB)
↓
Arduino firmware
↓
PWM motor control
↓
Vibration feedback


---

## 🏗️ System Architecture

Voice Input
↓
Speech-to-Text
↓
Target Object Extraction
↓
YOLOv8 Object Detection
↓
Closest Object Selection
↓
Distance Estimation
↓
Serial Communication
↓
Haptic Output (Glove)


---

## 👥 Team Roles

### 🤖 AI / ML Lead
- Object detection integration
- Speech-to-text pipeline
- Detection filtering logic
- Serial communication protocol
- System integration

### ⚡ Electrical Engineering Lead
- Glove hardware design
- Motor driver circuitry
- Arduino firmware
- PWM vibration control
- Physical assembly

### 📐 Maths / Systems Lead
- Distance normalization model
- Detection prioritization logic
- Haptic pattern design
- Testing & evaluation
- Ethical and accessibility framing

---

## 📅 Development Timeline (20 Days)

### Phase 1 — Parallel Development
- Object detection setup
- Glove circuit design
- Haptic language design

### Phase 2 — Independent Subsystems
- Working detection script
- Working vibration prototype

### Phase 3 — Integration
- Serial communication
- Real-time vibration response
- Latency optimization

### Phase 4 — Testing & Demo Preparation
- Blindfold testing
- Edge case handling
- Pitch refinement

---

## ⚖️ Ethical Considerations

- This device is **not intended to replace canes or guide dogs**
- It is designed to **augment spatial awareness**
- User autonomy and consent are central
- Avoids excessive audio interference in public spaces

---

## 🧪 Future Extensions

- Depth cameras for true distance estimation
- On-device inference (Jetson / Edge TPU)
- Indoor navigation mapping
- Multi-modal feedback (optional audio mode)
- Model upgrade (YOLOv9 or lightweight custom model)

---

## 🎥 Demo Plan

**Live demonstration:**

1. Blindfolded user wears glove  
2. Objects placed in room  
3. User says: *“Find my cup”*  
4. Vibration intensity increases as they approach the cup  
5. Real-time detection feed shown on screen  

---

## 🏁 Project Goal

To demonstrate that computer vision can be transformed into tactile feedback, offering a scalable and intuitive accessibility solution that enhances independence without overwhelming the user’s auditory senses.

---

## 🛠️ Tech Stack

- Python  
- YOLOv8 (Ultralytics)  
- Whisper (speech-to-text)  
- Arduino (C++)  
- Serial communication  
- PWM motor control  
