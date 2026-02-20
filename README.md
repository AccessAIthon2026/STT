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

## 🚀 Building it (System Pipeline)

# AccessAIthon 2026 – Mobile App Version

## Step-by-Step Project Workflow

1. Decided to scrap the Arduino glove idea and turn it into a mobile app.  
2. The user opens the app on their phone.  
3. The app is ready to listen for a keyword.  
4. The user says a keyword; a musical note plays to demonstrate the app is listening.  
5. The user says "find my ..." into the phone mic.  
6. The app captures audio input from the microphone.  
7. Audio is processed in real-time using **Whisper AI (OpenAI)**.  
8. Speech is converted into text as the user speaks.  
9. The text is interpreted to extract the target object.  
10. The app activates the camera to see the surrounding environment.  
11. The live camera feed is displayed on the screen.  
12. The app uses **YOLOv8** to detect objects in the camera feed.  
13. Bounding boxes appear around all detected objects.  
14. The target object is highlighted differently (e.g., brighter color).  
15. The app estimates distance based on bounding box size.  
16. The screen shows approximate distances from the user to the target object.  
17. Haptic feedback is activated using the phone’s vibration motor.  
18. Vibration intensity increases as the user gets closer to the target.  
19. Different vibration patterns are used for different object categories.  
20. For example: person = double pulse, wall = continuous vibration, furniture = slow pulse.  
21. The vibration system mimics the tactile language originally planned for the glove.  
22. Optional: The user can select objects from a list for more precise detection.  
23. Optional: Audio feedback can be added for visual confirmation.  
24. The app backend uses **Python** for AI inference (YOLOv8 + Whisper).  
25. Real-time AI processing is enabled with **TensorFlow Lite** or **ONNX Runtime Mobile**.  
26. The app avoids additional hardware—everything runs on the phone.  
27. Users can interact with the app hands-free after giving a voice command.  
28. The haptic system is designed to be intuitive for visually impaired users.  
29. The live feed helps users understand AI decisions visually.  
30. The software pipeline is: **Voice Input → Whisper AI → Object Detection → Distance Estimation → Vibration Output**.  
31. Bounding boxes are updated in real-time to maintain continuous guidance.  
32. The system uses **Flutter** for cross-platform mobile deployment (Android/iOS).  
33. **Vibration / Haptic APIs** provide tactile feedback on the phone.  
34. **Shravan** handles distance estimation and vibration mapping.  
35. **Neslihan** manages camera integration, object detection logic, bounding box drawing, and real-time visual feedback.  
36. **Ishir** handles app integration, AI intercommunication, and overall project coordination.  
37. Voice-to-text conversion uses **OpenAI Whisper models** for accuracy.  
38. Object detection uses **YOLOv8 lightweight models** for mobile performance.  
39. The app UI shows bounding boxes, distances, and detection confidence.  
40. Users can test the app anywhere using just a phone.  
41. The system can detect multiple objects at once.  
42. Users receive continuous haptic feedback as they move closer or further from the target.  
43. The prototype is designed to be completed in 2 days.  
44. The app can be extended later for indoor navigation or multi-modal feedback.  
45. The system supports optional **speech command customization**.  
46. Audio cues (musical notes) confirm user input during voice commands.  
47. Real-time camera feed ensures accurate target detection.  
48. Haptic intensity is mapped dynamically using bounding box size.  
49. The app uses a **Python + mobile integration pipeline** for fast prototyping.  
50. The final prototype demonstrates a working **Vision-to-Touch Mobile App** that replaces the original glove, using phone haptics to guide visually impaired users.



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

- Phone

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
- Python ML libraries.
