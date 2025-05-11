
## 🧪 Hướng dẫn cài đặt JupyterHub + Conda trên Ubuntu Server

JupyterHub là nền tảng mạnh mẽ cho phép nhiều người dùng chạy các notebook Python qua trình duyệt. Dưới đây là hướng dẫn từng bước để triển khai JupyterHub trên Ubuntu Server và tích hợp với môi trường Conda.

---

### ✅ Bước 1: Cài đặt hệ thống cơ bản

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nodejs npm
```

---

### ✅ Bước 2: Tạo môi trường ảo và cài đặt JupyterHub

```bash
mkdir -p ~/venvs/jupyterhub
cd ~/venvs/jupyterhub
python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install jupyterhub notebook jupyterlab
sudo npm install -g configurable-http-proxy
```

---

### ✅ Bước 3: Tạo file cấu hình `jupyterhub_config.py`

```python
# ~/jupyterhub_config.py
c = get_config()
c.JupyterHub.bind_url = 'http://0.0.0.0:8888'
c.JupyterHub.hub_bind_url = 'http://127.0.0.1:8081'
c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'
c.Authenticator.allowed_users = {'rd'}
c.Authenticator.admin_users = {'rd'}
c.Spawner.default_url = '/lab'
c.Spawner.notebook_dir = '/home/{username}/notebooks'
c.ConfigurableHTTPProxy.api_url = 'http://127.0.0.1:8010'
```

📁 Tạo thư mục notebook cho user:

```bash
sudo mkdir -p /home/rd/notebooks
sudo chown -R rd:rd /home/rd
```

---

### ✅ Bước 4: Cài đặt Miniconda và cấu hình

```bash
cd ~
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
conda config --set auto_activate_base false
```

---

### ✅ Bước 5: Tạo Conda Environment tích hợp Jupyter

```bash
conda create -n myenv python=3.10 -y
conda activate myenv
conda install ipykernel -y
python -m ipykernel install --user --name=myenv --display-name "Python (myenv)"
```

---

### ✅ Bước 6: Chạy JupyterHub

Tạo file khởi động nhanh:

```bash
nano ~/run_jupyterhub.sh
```

Nội dung:

```bash
#!/bin/bash
source ~/venvs/jupyterhub/venv/bin/activate
jupyterhub -f ~/jupyterhub_config.py
```

Chạy:

```bash
chmod +x ~/run_jupyterhub.sh
./run_jupyterhub.sh
```

---

### ✅ Kết quả

Truy cập tại `http://<ip-server>:8888`, đăng nhập bằng user hệ thống (`rd`) và chọn kernel `Python (myenv)` để bắt đầu.

---


