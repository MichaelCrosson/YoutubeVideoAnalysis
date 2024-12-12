# **Tech Review Video Popularity Analysis**

**Objective**: Identify the key features driving the success of tech review videos by analyzing video metadata, transcripts, audio, and visual content. The project focuses on building a comprehensive **Popularity Metric** using advanced machine learning models.

---

## **📊 Data Sources**
- **YouTube API**: Metadata including views, likes, comments, and subscriber counts.
- **Transcript API**: Extracted transcripts for sentiment and topic analysis.
- **Audio Analysis**: Emotion detection using Wav2Vec for tonal shifts.
- **Video Frames**: Visual feature extraction through CNNs and LLaVA models.

---

## **🔬 Analysis Workflow**
1. **Data Collection**:
   - Use the YouTube API to collect metadata.
   - Scrape video transcripts and segment audio for tonal analysis.
   - Extract video frames for visual aesthetic modeling.
2. **Text Analysis**:
   - Perform sentiment analysis on transcripts and hooks (first 75 words).
   - Use Non-Negative Matrix Factorization (NMF) for topic modeling.
3. **Audio Analysis**:
   - Detect emotions (happy, sad, neutral, angry) using Wav2Vec.
   - Segment tonal dynamics across 25 equal intervals.
4. **Visual Analysis**:
   - Extract brightness and color patterns through CNNs.
   - Perform PCA for dominant visual themes.
   - Apply LLaVA for scene and object interpretation.
5. **Modeling**:
   - Combine extracted features into a **Weighted Popularity Metric**.
   - Train predictive models (Random Forest, Linear Regression, etc.) to rank feature importance.

---

## **🎥 Creator Tier System**
Videos from the top tech YouTube channels were selected, categorized into three tiers:
- **Diamond Tier (10M+ subscribers)**:
  - @MKBHD, @UnboxTherapy, @Mrwhosetheboss
- **Gold Tier (1M+ subscribers)**:
  - @Dave2D, @MaryBautista, @JerryRigEverything
- **Silver Tier (100K+ subscribers)**:
  - @ThisIsTechToday, @CreatedbyEllaYT, @ChigzTech  

Each channel contributed 5 videos, ranging from 5 to 28 minutes, posted between July and November 2024.

---

## **📈 Popularity Metric**
The **Weighted Popularity Score** combines key metrics:
- **50% Views**  
- **30% Likes**  
- **20% Comments/Subscribers**  

This composite score balances engagement metrics with audience size, serving as the target variable for predictive modeling.

---

## **🚀 Future Scope**
1. **Expand Dataset**:
   - Include more creators across diverse niches (e.g., gaming, fashion).
2. **Refine Models**:
   - Experiment with advanced architectures like Transformers or XGBoost.
3. **Real-Time Feedback**:
   - Build tools for creators to optimize titles, thumbnails, and hooks before publishing.
4. **Cross-Platform Application**:
   - Extend analysis to other platforms like Instagram and TikTok.

---

## **📦 Setup**
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/MichaelCrosson/YoutubeVideoAnalysis.git
cd YoutubeVideoAnalysis
pip install -r requirements.txt
```

---

## **📝 Contributors**
- **Michael Crosson**: Video Analysis - CNN and LLaVa model
- **Neha Boinapalli**: Transcript topic and sentiment analysis | Data Collection
- **Alexander Schmelzeis**: Visual feature extraction  
- **Jose Currea**: Final Model Analysis
- **Mikala Lowrance**: Audio Analysis
