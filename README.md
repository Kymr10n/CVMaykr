Great question! To run the `cv_renderer` tool (the one you just downloaded as a `.tar.gz` bundle), you only need a minimal Python environment with [Jinja2](https://palletsprojects.com/p/jinja/) installed. Here's how to set it up cleanly:

---

## ✅ Step-by-Step: Python Runtime Setup

### 🔹 Option 1: Using `venv` (recommended)

1. **Extract the bundle**

   ```bash
   tar -xzf cv_renderer_bundle.tar.gz
   cd cv_renderer
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install jinja2
   ```

4. **Run the rendering script**

   ```bash
   python render_cv.py
   ```

   This will generate `custom_cv.tex`. If you have LaTeX installed, you can compile it:

   ```bash
   pdflatex custom_cv.tex
   ```

---

### 🔹 Option 2: Using `pipx` (for isolated usage)

If you don’t want to manually manage environments:

```bash
pipx run --spec jinja2 'python render_cv.py'
```

---

## 🛠 Required Tools

| Tool        | Purpose                  | Install Command (Ubuntu)                 |
| ----------- | ------------------------ | ---------------------------------------- |
| Python 3.8+ | Runtime                  | `sudo apt install python3 python3-venv`  |
| Jinja2      | Template engine          | `pip install jinja2` (inside virtualenv) |
| LaTeX       | PDF rendering (optional) | `sudo apt install texlive-latex-extra`   |

---

## 🧪 Bonus: Test it's working

After running:

```bash
python render_cv.py
```

You should see:

```bash
custom_cv.tex  # created
```

Run:

```bash
pdflatex custom_cv.tex
```

You should now have:

```bash
custom_cv.pdf
```

---