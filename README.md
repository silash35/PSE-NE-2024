# About this work

This repository contains the materials related to the paper entitled **“Implementação de PINN Embarcada em Ambiente Software-in-the-Loop como Analisador Virtual para um Sistema de Tanques Esféricos”**.

The work proposes the implementation of a Physics-Informed Neural Network (PINN) embedded in a Software-in-the-Loop (SiL) environment and applied as a virtual analyzer for a spherical tank system. By incorporating the governing physical equations of the process directly into the neural network training, the proposed approach ensures consistency with the system dynamics.

This work was presented at the **1º Seminário em Engenharia de Sistemas em Processos do Nordeste (PSE NE 2024)**, an academic and technical event focused on advancements in Process System Engineering. The event was held in 2024 in the city of Campina Grande, in the state of Paraíba, Brazil.

Please note that some parts of the code, such as comments and image generation functions, are written in Portuguese, as the visual outputs and documentation were tailored for a Portuguese-speaking audience.

## Citation

The **PSE NE 2024** was a technical and academic seminar and did not produce official published proceedings. Therefore, this work does not have a formal publication associated with the event.

For citation purposes, it is recommended to cite the related and extended work presented at [SBAI 2025](https://www.sba.org.br/web/eventos/view?id=96), which builds upon the same modeling framework and methodology. The related work is entitled **“Embarque de Rede Neural Recorrente Fenomenologicamente Informada para Controle de Nível em Tanques Esféricos”** and is available at: [https://github.com/silash35/SBAI-2025-2287](https://github.com/silash35/SBAI-2025-2287).

This SBAI 2025 contribution can be used as the primary reference for academic citation, as it represents a more complete and formally documented version of the methodology originally presented at PSE NE 2024.

## 📁 Folder Structure

This project organizes its components into distinct folders, with each containing a markdown file that provides detailed guidance when necessary.

### 📂 `Arduino/`

This folder contains the code that runs on the Arduino UNO microcontroller. It handles serial communication with TankSim and implements the PIRNN in C++.

### 📂 `LaTeX/`

> ⚠️ **Note:** All materials in this folder are written in **Portuguese**, as the event took place in Brazil.

This folder contains the LaTeX source files for the presentation slides and the technical article.

The article was made, but it was **not published**, as the seminar focused solely on oral presentations without formal proceedings.

### 📂 `PyTorch/`

This folder contains the code used to create and train the PIRNN using the PyTorch library.

### 📂 `TankSim/`

This folder contains the code for the TankSim software, developed in Python using the Qt framework. It simulates the tank system and communicates with the Arduino via serial connection.
