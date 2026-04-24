# JEK Computing Project: Antibiotic Data Analysis

## Overview

This project analyzes microbiology experiment data to determine whether honey or garlic enhances the effectiveness of the antibiotic vancomycin against *Staphylococcus aureus*. The project combines laboratory experimentation with computational tools to organize, analyze, and visualize data.

---

## Objective

To evaluate how different treatments affect bacterial growth by comparing inhibition zones from a Kirby-Bauer disk diffusion test, and to use computational methods to process and interpret the data.

---

## Methods

### Experimental

* Bacteria: *Staphylococcus aureus*
* Method: Kirby-Bauer disk diffusion assay
* Treatments:

  * Vancomycin (control)
  * Vancomycin + honey
  * Vancomycin + garlic
* Measurement: Inhibition zone diameter (mm)

### Computational

* Data stored in a SQLite database
* Python used for analysis:

  * `pandas` for data manipulation
  * `matplotlib` for visualization

---

## Data Analysis

* Data was queried from the SQL database into a pandas DataFrame
* Average inhibition zones were calculated across trials
* A bar graph was generated to compare treatments

---

## Results

* Garlic treatment showed the largest inhibition zone (~28–29 mm)
* Control and honey treatments were both ~19 mm
* Garlic significantly increased antibiotic effectiveness

---

## Conclusion

Garlic enhances the effectiveness of vancomycin against *Staphylococcus aureus*, while honey does not show a meaningful improvement.

---

## Repository Contents

* `analysis.py` – Python script for data analysis and graph generation
* `database_setup.py` – Creates the SQL database
* `insert_data.py` – Inserts experimental data into the database
* `project-progress.qmd` – Quarto source document
* `project-progress.html` – Final rendered report
* `Data Set.txt` – Raw experimental data
* `Final-Presentation.pptx` – Presentation slides

---

## Contributors

* Kayla Easter – Data management, coding, and analysis
* Jlaine Tindall – Experimental design and data collection
* Emiy Eary – Data analysis and reporting

---

## Tools Used

* Python
* SQLite
* pandas
* matplotlib
* Quarto
* GitHub

---

## Summary

This project demonstrates how computational tools can be used alongside scientific experiments to efficiently organize data, perform analysis, and present clear results.
