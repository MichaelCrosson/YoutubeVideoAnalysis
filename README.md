# Tech Review Video Analysis Project

**Objective**: Identify key features contributing to the success of tech review videos using data from video, transcript, audio, and metadata. The project aims to create a **Weighted Popularity Score**.

## 🗂 Data Sources
- **YouTube API**: Metadata (likes, views, subscriber count, etc.).
- **Video Scraper**: Extract raw video files.
- **Transcript Analysis**: Sentiment (VADER), topic modeling (TF-IDF).
- **Audio Analysis**: Tone recognition (e.g., excitement, anger).
- **Background Data**: Posting times, creator's region.

## 🔍 Analysis Workflow
1. **Metadata Collection**: YouTube API and SocialBlade scraping.
2. **Video Analysis**: Extract video features and engagement metrics.
3. **Transcript Analysis**: Sentiment and topic insights.
4. **Audio Analysis**: Tone extraction.
5. **Final Model**: Combine features into a **Weighted Popularity Score** using a neural network.

## 📈 Tier System
Analyze 10 most recent videos (Sept 12 - Nov 12):
- **Diamond (10M+ subs)**: e.g., Marques Brownlee, Linus Tech Tips
- **Gold (1M+ subs)**
- **Silver (100k+ subs)**

## 🚀 Future Scope
- Expand to different video genres.
- Cross-platform analysis (e.g., Instagram/Twitter).
- Recommendations for mid-tier creators.

## 📦 Setup
Clone the repo and install dependencies:
```bash
git clone https://github.com/your-repo/tech-review-analysis.git
cd tech-review-analysis
pip install -r requirements.txt
```

## 📝 Contributors
- **Michael Crosson**: Video scraping
- **Neha**: Transcript analysis
- **Nico**: Background research
- **Alex**: Audio analysis
- **Mikala**: Metadata scraping
