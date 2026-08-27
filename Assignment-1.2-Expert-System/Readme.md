# Student Burnout Risk Expert System

A simple rule-based Expert System developed in **Prolog** to assess a student's burnout risk based on study and wellbeing factors.

## Problem Domain

Student wellbeing and burnout risk assessment.

The system analyzes factors such as:

- Sleep duration
- Study hours
- Stress level
- Focus level
- Screen time
- Study breaks
- Pending assignments

## Features

- Identifies individual burnout risk factors
- Classifies burnout risk as **Moderate, High, or Severe**
- Provides suitable recommendations
- Uses a knowledge base of facts and rules
- Demonstrates logical inference using Prolog

## Concepts Used

- Expert Systems
- Knowledge Base
- Facts and Rules
- Rule-Based Reasoning
- Backward Chaining

## Technology Used

- **Language:** Prolog
- **Platform:** SWI-Prolog
- **External Libraries:** None

## How It Works

1. Student information is stored as facts.
2. Rules identify individual risk factors.
3. Multiple risk factors are evaluated to determine burnout level.
4. The system displays the diagnosis and recommendations.

## How to Run

1. Install SWI-Prolog.
2. Open the Prolog file.
3. Load the program:

```prolog
?- [student_burnout].