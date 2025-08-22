# 📚 AI Storybook Generator  

An interactive **AI-powered storybook generator** built with **Streamlit**.  
It uses **Google Vertex AI (Gemini + Imagen)** to generate children’s stories and illustrations, then exports them into a polished **PDF storybook**.  

---

## 🚀 Features  
- ✨ Generate creative children’s stories from a concept prompt  
- 🌍 Choose your preferred language (English, Hindi, Telugu, French, Spanish)  
- 🎨 AI-powered illustrations using Vertex AI Imagen  
- 📖 Automatic story splitting into multiple pages  
- 🖼️ Each page includes story text + AI-generated illustration  
- 📥 Export the complete storybook as a **PDF download**  

---

## 🛠️ Tech Stack  
- **Frontend:** [Streamlit](https://streamlit.io/)  
- **AI Models:** Google Vertex AI  
  - `gemini-2.0-flash` → Story generation  
  - `imagegeneration@005` → Illustration generation  
- **PDF Export:** ReportLab  
- **Image Handling:** Pillow  

---

## 📂 Project Structure  

```
storybook-app/
│── app.py                      # Streamlit main app
│── requirements.txt             # Python dependencies
│── utils/
│     ├── text_processing.py     # Story generation (Gemini)
│     ├── image_generation.py    # Illustration generation (Imagen)
│     ├── pdf_export.py          # Export to PDF
```

---

## ⚙️ Setup  

### 1. Clone the repo  
```bash
git clone https://github.com/your-username/storybook-app.git
cd storybook-app
```

### 2. Install dependencies  
```bash
pip install -r requirements.txt
```

### 3. Configure Google Vertex AI credentials  

- In **Streamlit Cloud**:  
  Go to `App → Settings → Secrets` and paste your service account key like this:  

```toml
PROJECT_ID = ""
LOCATION = ""

[google_service_account]
type = "service_account"
project_id = ""
private_key_id = "xxxxxxxxxxxxxxxxxxxxx"
private_key = "-----BEGIN PRIVATE KEY-----

-----END PRIVATE KEY-----
"
client_email = ""
client_id = "xxxxxxxxxxxxxx"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/vertex-user%40my-project-8-465221.iam.gserviceaccount.com"
universe_domain = "googleapis.com"
```

⚠️ Make sure you paste the private key with **real line breaks** (not `\n`).  

---

## ▶️ Run the app  

```bash
streamlit run app.py
```

Locally it will open at: [http://localhost:8501](http://localhost:8501)  

---

## 🌐 Deployment  

1. Push your project to GitHub  
2. Go to [Streamlit Cloud](https://share.streamlit.io/) → **New app**  
3. Connect repo & branch  
4. Add **Secrets** (as shown above)  
5. Deploy 🚀  

---

## 📥 Example Workflow  

1. Enter a concept → *“A little red dragon learning to fly”*  
2. Choose a language (e.g., *English*)  
3. Click **Generate Storybook**  
4. Story is generated and split into multiple pages  
5. Each page gets an AI-generated illustration  
6. Download final **storybook.pdf**  

---

## 📸 Sample Output  

- **Cover Page:**  
  📖 AI Storybook  
  *A story about: A little red dragon learning to fly*  

- **Pages:**  
  - Story text (chunked into small paragraphs)  
  - AI illustration (child-friendly, colorful, cartoon style)  

---

## 🧑‍💻 Author  
Built by **Mummidivarapu Sri Sai Nikshith** ✨  
