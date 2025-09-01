# sales-analysis

A tiny sales analysis project used throughout the course
*Git, Python Environments & Coding Best Practices* (MSA-DATB07-03).

This repository is the material for **TD1 -- Terminal & Git fundamentals**.

Contents

- `project/`   the sales-analysis code, built commit by commit (read the history!)
- `shell-lab/` a directory tree for the shell treasure hunt

## Usage

```bash
cd project
python -c "import analysis; rows = analysis.load_sales('data/sales.csv'); print(analysis.total_revenue(rows))"
```

## Reading the history

```bash
git log --oneline
git show HEAD~2
git diff HEAD~5 HEAD -- project/analysis.py
```
