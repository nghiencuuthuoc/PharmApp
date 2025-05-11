Để tạo một môi trường Conda mới có tên là `esm`, bạn có thể làm theo các bước sau:

### Bước 1: Cài đặt Conda (nếu chưa có)
Nếu bạn chưa cài đặt Conda, hãy tải và cài đặt **Miniconda** hoặc **Anaconda** từ:
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (gọn nhẹ)
- [Anaconda](https://www.anaconda.com/) (bao gồm nhiều gói sẵn có)

### Bước 2: Mở Terminal hoặc Anaconda Prompt
Trên **Windows**, mở **Anaconda Prompt** hoặc **Command Prompt**.  
Trên **Linux/macOS**, mở Terminal.

### Bước 3: Tạo môi trường Conda mới với tên `esm`
Chạy lệnh sau để tạo môi trường Conda có tên là `esm`:

```bash
conda create -n esm python=3.10
```

> **Giải thích:**
> - `-n esm`: Đặt tên môi trường là `esm`
> - `python=3.10`: Cài đặt Python phiên bản 3.10 (bạn có thể đổi phiên bản nếu muốn)

### Bước 4: Kích hoạt môi trường `esm`
Sau khi tạo xong, kích hoạt môi trường bằng lệnh:

```bash
conda activate esm
```

### Bước 5: Cài đặt các gói cần thiết (tuỳ chọn)
Nếu bạn muốn cài đặt các gói như **PyTorch**, **ESM Model (Evolutionary Scale Modeling)** từ Meta, bạn có thể chạy:

```bash
pip install torch torchvision torchaudio
pip install fair-esm
```

### Bước 6: Kiểm tra cài đặt
Kiểm tra xem ESM đã cài đặt đúng chưa bằng lệnh:

```python
import esm
print(esm.__version__)
```

Nếu không có lỗi, môi trường đã được thiết lập thành công! 🚀