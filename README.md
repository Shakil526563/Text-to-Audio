# 🗣️ Streamlit Text-to-Speech App (Hugging Face VITS)

A simple Streamlit web app that converts text to speech using the Hugging Face `kakao-enterprise/vits-ljs` model.

---
![image](https://github.com/user-attachments/assets/b916f28e-5396-4bce-9608-319decd98681)


## 🚀 How to Run

### 1. Clone the Repository

```sh
git clone https://github.com/your-username/streamlit-tts-app.git
cd streamlit-tts-app
```

### 2. Build the Docker Image

```sh
docker build -t streamlit-tts-app .
```

### 3. Run the Docker Container

```sh
docker run -p 8502:8501 streamlit-tts-app
```

- The app will be available at [http://localhost:8502](http://localhost:8502)

---

## 📝 Local Development (without Docker)

1. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Install espeak-ng:**
    - **Ubuntu:** `sudo apt-get install espeak-ng`
    - **Windows:** [Download from releases](https://github.com/espeak-ng/espeak-ng/releases) and add to PATH

3. **Run the app:**
    ```sh
    streamlit run main.py
    ```

- The app will be available at [http://localhost:8501](http://localhost:8501)

---

## 📁 File Structure

```
.
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🏷️ Credits

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [kakao-enterprise/vits-ljs](https://huggingface.co/kakao-enterprise/vits-ljs)
- [Streamlit](https://streamlit.io/)

---
