```markdown
# Stochastic Calculus for Economics & Finance

A curated collection of lecture notes, examples, and code implementations in R and Python for stochastic calculus models and applications in economics and finance.

---

## 📂 Repository Structure

```

├── README.md
├── LICENSE
├── environment.yml         # Conda environment definition
├── requirements.txt        # Python dependencies
├── R-packages.R            # R package installation script
│
├── notes/                  # Lecture notes (PDF, LaTeX sources, slides)
│   ├── lec01\_introduction.pdf
│   ├── lec02\_brownian\_motion.pdf
│   └── …
│
├── python/                 # Python code examples
│   ├── data/               # sample data files (CSV, JSON)
│   ├── notebooks/          # Jupyter notebooks
│   │   ├── sim\_bm.ipynb
│   │   ├── pricing\_black\_scholes.ipynb
│   │   └── …
│   ├── src/                # reusable modules
│   │   ├── stochastic.py
│   │   └── finance\_models.py
│   └── requirements.txt    # (optional) specific to python/
│
└── R/                      # R code examples
├── data/               # sample data files
├── scripts/            # R scripts
│   ├── simulate\_bm.R
│   ├── bs\_pricing.R
│   └── …
└── README\_R.md         # R-specific instructions

````

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/stochastic-calculus-ecofin.git
cd stochastic-calculus-ecofin
````

### 2. Set up your environment

#### Python (recommended via Conda)

Create and activate the environment:

```bash
conda env create -f environment.yml
conda activate stoch-calc
```

Install any updates:

```bash
pip install --upgrade -r requirements.txt
```

#### R

Install the required R packages by running:

```bash
Rscript R-packages.R
```

Or inside an R session:

```r
source("R-packages.R")
```

---

## 📝 Lecture Notes

All lecture notes, slides, and LaTeX source files are stored under the `notes/` directory. Filenames are of the form:

```
lec{NN}_{topic}.pdf
```

Examples:

* `lec01_introduction.pdf` – Overview of probability spaces and filtrations
* `lec02_brownian_motion.pdf` – Construction & basic properties of Brownian motion

---

## 💻 Code Examples

### Python

* **Notebooks:**
  Interactive demonstrations in `python/notebooks/`, e.g.

  * `sim_bm.ipynb` – Simulating paths of Brownian motion
  * `pricing_black_scholes.ipynb` – Monte Carlo vs. analytic Black–Scholes

* **Modules:**
  Reusable functions for simulation and model evaluation in `python/src/`.

Run a notebook:

```bash
jupyter lab python/notebooks/sim_bm.ipynb
```

### R

* **Scripts:**
  Stochastic simulations and pricing routines in `R/scripts/`, e.g.

  * `simulate_bm.R` – sample Brownian paths
  * `bs_pricing.R` – Black–Scholes formulas and calibration

Run an R script:

```bash
Rscript R/scripts/simulate_bm.R
```

---

## 📊 Data

Sample datasets (historical prices, economic indicators) are stored in `python/data/` and `R/data/`. Feel free to replace them with your own CSV or JSON files.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

Please follow the existing code style conventions and include tests where appropriate.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

Enjoy exploring stochastic calculus in economics and finance! 🚀

```
```
