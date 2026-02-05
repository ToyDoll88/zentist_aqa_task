# QA Automation Test Project

## Project Overview

This project contains automated UI tests written in **Python**
using **Pytest** and **Playwright**.

The goal of the project is to demonstrate:
- Page Object Model usage
- UI test design
- Playwright + Pytest integration
- Allure reporting

Target application:
https://the-internet.herokuapp.com

---

## Tech Stack

- Python
- Pytest
- Playwright
- Allure Report

---

## Requirements

- Python 3.13 (project is compatible with Python 3.10+)
- Java 8+ (for Allure reports)

> Note: Playwright uses bundled browser binaries.
> No system browser installation is required.


---

## Local Setup

### Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```
### Install Python dependencies
```bash
pip install -r requirements.txt
```
### Install Playwright browsers
```bash
playwright install
```

## Allure Report Setup

Recommended **Allure** version: 2.25.0

### Linux installation example:

```bash 
wget https://github.com/allure-framework/allure2/releases/download/2.25.0/allure-2.25.0.tgz
tar -zxvf allure-2.25.0.tgz
sudo mv allure-2.25.0 /opt/allure
sudo ln -s /opt/allure/bin/allure /usr/bin/allure
```

### Verify installation:

```bash
allure --version
```

## Run Tests

### Run all tests with detailed output
```bash
pytest -sv
```
### Run tests in parallel
```bash
pytest -n auto
```
### Run tests in headless mode
By default, tests run in **headed** mode
```bash
pytest --headless
```
### Run tests in a specific browser

By default, tests are executed in **Chromium**.
```bash
pytest --browser=firefox
```
Supported browsers:
- chromium
- webkit
- firefox

### Run tests with Allure report
```bash
pytest --alluredir=out
```
### View Allure report
```bash
allure serve out
```

## Test Scenarios Covered
- Main page UI content validation
- Navigation to login page
- Negative login scenarios
- Successful login
- Secure page content validation
- Logout flow