# 📘 README — Chatbot with Deep Learning (Intent-Based)

## Project Overview

This project was developed as part of my industrial internship at **Obinno Resources Nigeria Limited**, with the objective of reducing **time wastage during factory machine breakdowns** caused by delays in fault diagnosis and maintenance decision-making.

In the factory environment, machine failures are frequent, and engineers often spend excessive time troubleshooting issues that may have occurred and been resolved previously. This project explores the use of **machine learning–based conversational systems** to assist engineers in quickly identifying known fault patterns and suggested resolutions.

---

## Problem Statement

* Machine faults and resolutions were **not centrally accessible**
* Engineers relied heavily on **manual recall or paper records**
* Similar faults were repeatedly diagnosed from scratch
* This led to **extended downtime and productivity loss**

The goal was to create a chatbot capable of answering questions such as:

* “What caused this fault before?”
* “Has this machine failed in a similar way?”
* “What solution was applied previously?”

---

## Scope of This Project

This first implementation uses:

* Natural Language Processing (NLP)
* Supervised Deep Learning
* Intent classification with TensorFlow/Keras

The chatbot:

* Classifies user input into predefined fault categories (intents)
* Returns **fixed, predefined responses**
* Works well for **known and frequently occurring faults**
* Provides fast, deterministic answers

---

## Why This Approach Was Chosen

As an initial solution:

* It is lightweight and easy to deploy
* Requires no external APIs
* Provides predictable and controlled outputs
* Demonstrates core NLP and ML engineering skills

This made it suitable as a **proof of concept** for applying AI to maintenance support.

---

## Limitations Identified

While effective for basic scenarios, this approach has critical limitations:

* Cannot retrieve detailed historical records from files
* Cannot reason over long or complex maintenance logs
* Cannot iteratively refine answers based on new context
* Does not scale well as fault records grow
* Responses are limited to predefined templates

As a result, this project **does not fully solve the factory maintenance problem**.

---

## Outcome and Next Step

This project validated the concept of AI-assisted maintenance support.
However, it revealed the need for a **more advanced system capable of reasoning, retrieval, and contextual understanding**, which directly motivated the second project.
