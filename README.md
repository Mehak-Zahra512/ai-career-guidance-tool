# AI Career Guidance Tool
A rule-based career recommendation system for
Pakistani intermediate students — built because
proper career counselling in Pakistan is scarce
and most students choose fields based on peer
pressure, not actual fit.

## The Problem
After intermediate, Pakistani students face one of
the most important decisions of their lives with
almost no structured guidance. Most choose medicine
or engineering because everyone else does.
This tool tries to change that.

## What I Built
A Python-based recommendation system that:
- Takes the student's intermediate percentage as input
- Takes their interest field as input
- Scores each career path against both inputs
- Ranks and displays the most suitable career options
  with match explanations

## Supported Interest Fields
- Computer Science
- Medical
- Business
- Arts
- Engineering

## Example Output
Enter your percentage: 78
Enter your interest: cs

Recommended Careers:
1. Software Engineer — High Match
2. Data Analyst — High Match
3. Business Analyst — Medium Match

## Tech Stack
Python · Rule-Based Logic · Scoring System

## How to Run
python ai_career_guidance_tool.py

## Why No ML?
No external libraries were used deliberately.
Every decision rule is explicitly defined and readable.
This makes the logic transparent — you can see
exactly why each career was recommended.

## Honest Limitation
Recommendations are based on predefined rules —
not trained on real student outcome data.
Next version: collect real data on student choices
and outcomes, then train an actual recommendation model.
