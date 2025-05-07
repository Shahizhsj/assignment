# AI Community Moderator MVP Challenge

## Overview
This project demonstrates an AI-powered community moderation system that integrates brand knowledge to provide accurate and conversational user interactions. It allows brands to upload files or provide website links for knowledge ingestion, enabling the AI agent to answer user queries while maintaining the brand's tone and voice.


## Features

### 1. Knowledge Integration
- **Website Crawling:** Processes content from brand-provided URLs to extract relevant information.  
- **Document Support:** Supports file uploads in formats like PDFs, Word documents, and text files.  
- **Efficient Search:** Enables seamless and accurate knowledge retrieval for AI-based responses.

### 2. Conversational Interface
- **Platform Integration:** Implemented on one communication platform, such as Telegram, Discord, or a website chat widget.  
- **Natural Language Understanding:** Allows users to interact with the AI agent in a conversational manner.  
- **Accurate Responses:** Provides context-aware answers based on the ingested knowledge.

### 3. Brand Alignment
- **Tone Consistency:** Ensures all responses adhere to the brand’s voice and guidelines.  
- **Source References:** Includes references to original knowledge sources where applicable.

### 4. Sample Knowledge Base
- Demonstrates the system’s functionality using a predefined set of knowledge resources.  
- Example sources include websites and uploaded documents to showcase versatility.

### 5. Deployment
- **Accessible Demo:** Hosted on a simple and scalable platform (e.g., Vercel) for immediate access and testing.  
- **Live Interaction:** Offers a working conversational interface for evaluation purposes.

## Technical Stack

- **LLM (Language Model):** [e.g., ChatGPT, Claude, Llama]  
- **Frameworks and Libraries:** [e.g., LangChain, FastAPI, Streamlit]  
- **Hosting Solution:** [e.g., Vercel, AWS, Azure]  
- **Communication Platform Integration:** [e.g., Telegram Bot API, Discord API]

# Sample outputs

## Here I uploaded a pdf file of apple and i asked a few questions regreading apple 

![File Summarization](https://github.com/Shahizhsj/assignment/blob/32ea589745e672030709779afb489a2bfd9c0af1/Screenshot%20(204).png)

![File Summarization](https://github.com/Shahizhsj/assignment/blob/32ea589745e672030709779afb489a2bfd9c0af1/Screenshot%20(205).png)

![File Summarization](https://github.com/Shahizhsj/assignment/blob/32ea589745e672030709779afb489a2bfd9c0af1/Screenshot%20(206).png)

![File Summarization](https://github.com/Shahizhsj/assignment/blob/32ea589745e672030709779afb489a2bfd9c0af1/Screenshot%20(207).png)




## Here is demo video 

[Demo video]([https://drive.google.com/file/d/1kgDjLkuWk2rHC7siZbaQ8DB-dYHRFpUf/view?usp=sharing](https://drive.google.com/file/d/1Z_4QgtV-QfjKuh1HYeZDBVJkcSMckgFb/view?usp=sharing))

# System architecture

![File Summarization](https://github.com/Shahizhsj/assignment/blob/b1b35c04972f12d3d5613a94d119837ffded41ff/assignment.drawio.png)


# Setup instructions

### Prerequisites
- **Python:** Version 3.9 or higher.
- **Internet Connection:** Required for API calls.
- **API Keys:**  
  - **Google Gemini API Key** for text processing.
  - **ElevenLabs API Key** for text-to-speech.
### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Shahizhsj/assignment
   cd assignment
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Launch the Application**
   ```bash
   python app.py
   ```

6. **Access the Interface**
   Open your browser and go to:  
   `http://localhost:7860` (default port).


# Improvements

### 1. Handling Diverse Knowledge Formats  
**Challenge:** Processing data from multiple formats like web pages, PDFs, and Word documents.  
**Solution:** Developed a preprocessing pipeline to standardize content for indexing and retrieval.  

### 2. Maintaining Brand Consistency  
**Challenge:** Ensuring the AI agent adheres to the brand’s tone and guidelines.  
**Solution:** Configured detailed AI prompts and templates to align responses with brand voice.  
