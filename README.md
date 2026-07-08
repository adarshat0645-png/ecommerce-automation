# 🛒 E-Commerce Web Automation Framework

A test automation framework built with **Selenium WebDriver + Python + Pytest**,
following the **Page Object Model (POM)** design pattern. It automates key
e-commerce workflows (login and cart) on the SauceDemo practice site.

---

## 🎯 Overview

This project demonstrates automated functional and regression testing of an
e-commerce web application, covering positive and negative scenarios with
clean, maintainable, reusable code.

**Application Under Test:** https://www.saucedemo.com

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.9+** | Programming language |
| **Selenium WebDriver 4** | Browser automation |
| **Pytest** | Test framework & assertions |
| **webdriver-manager** | Automatic browser driver management |
| **Page Object Model** | Design pattern for maintainability |

---

## ✅ Test Coverage

- **Login Tests**
  - Valid login with correct credentials
  - Invalid login shows an error message
  - Locked-out user is blocked from logging in
- **Cart Tests**
  - Add a product to the cart and verify cart badge count
  - Verify the product appears correctly in the cart

---

## 📁 Project Structure

