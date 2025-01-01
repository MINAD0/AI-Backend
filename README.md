
# 🍎 **Fruit Detection API Backend**

This is a Django backend for a fruit detection API. The backend uses a **TensorFlow Lite** model to classify fruit images uploaded by clients.

---

## 📚 **1. Prerequisites**

Ensure the following software is installed on your **server machine**:

- **Python 3.10+**
- **pip** (Python Package Manager)
- **virtualenv** (Python Virtual Environment Manager)
- **Django** (Version 5.1.4)
- **TensorFlow Lite**
- **CORS Headers** (For API communication across domains)

---

## 🛠️ **2. Clone the Repository**

On the **server machine**, clone the project repository:

```bash
git clone <repository-url>
cd fruit_api
```

Replace `<repository-url>` with your actual repository URL.

---

## 🐍 **3. Create a Virtual Environment**

Create and activate a virtual environment:

```bash
python -m venv venv
# Activate virtual environment:
# On Windows:
venv\Scripts\activate
# On Linux or macOS:
source venv/bin/activate
```

---

## 📦 **4. Install Dependencies**

Install all required Python packages:

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, create it:

```bash
pip freeze > requirements.txt
```

---

## 🧠 **5. TensorFlow Lite Model**

Ensure the **TensorFlow Lite** model exists at the following path:

```
detection/models/CNN_fruits.tflite
```

Place your `.tflite` model file in this directory.

---

## ⚙️ **6. Update Settings for Remote Access**

Edit `settings.py`:

- **Allowed Hosts:** Add the server IP or domain.

```python
ALLOWED_HOSTS = ['127.0.0.1', 'your.server.ip.address']
```

- **Static and Media Files:** Update paths if necessary:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

- **CORS Headers:** Ensure this setting is enabled.

```python
CORS_ALLOW_ALL_ORIGINS = True
```

---

## 🗄️ **7. Database Migration**

Apply Django database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🔑 **8. Create a Superuser (Optional)**

```bash
python manage.py createsuperuser
```

Provide username, email, and password when prompted.

---

## 🚀 **9. Run the Server**

Start the Django development server and allow external connections:

```bash
python manage.py runserver 0.0.0.0:8000
```

If you're running on a production server, use **Gunicorn**:

```bash
pip install gunicorn
gunicorn fruit_api.wsgi:application --bind 0.0.0.0:8000 --workers 4
```

---

## 🌐 **10. Access the API**

- Open a browser and visit: `http://your.server.ip.address:8000/api/predict/`
- You can test the API with tools like **Postman** or **curl**.

Example `curl` command:

```bash
curl -X POST -F "file=@/path/to/fruit_image.jpg" http://your.server.ip.address:8000/api/predict/
```

---

## 📁 **11. Serve Static and Media Files**

If you're running on a production server:

```bash
python manage.py collectstatic
```

Serve media files properly by configuring the web server (e.g., **Nginx**) to serve `/media/` and `/static/` directories.

---

## 🐞 **12. Troubleshooting**

### Common Errors:
1. **TensorFlow Error:** Ensure the `.tflite` model is in the correct path.
2. **CORS Error:** Verify `CORS_ALLOW_ALL_ORIGINS` is set to `True`.
3. **Server Access:** Ensure the firewall allows traffic on **port 8000**.

---

## 🎯 **13. Production Deployment (Optional)**

For production deployment, you can use:

- **Gunicorn** (WSGI Server)
- **Nginx** (Reverse Proxy)
- **SSL Certificates** (e.g., Let’s Encrypt)

---

## 🧹 **14. Clean Up**

When done, deactivate your virtual environment:

```bash
deactivate
```

---

## 📞 **15. Support**

For any issues, create a GitHub issue or contact the project maintainers.

---

**🎉 Your Django backend is now live and ready to serve requests! 🎉**
