
# Demand Flexibility - DeCharge Procurement Agent

## Problem statement

EV owners often struggle with inconsistent access to affordable and reliable public charging infrastructure. High demand during peak hours leads to increased costs and limited availability, making it difficult for EV users to plan efficient charging sessions. Additionally, there's a lack of tools to help users take advantage of variable pricing or grid-friendly charging behaviors.

At DeCharge, we aim to solve this by integrating demand flexibility programs into the public EV charging ecosystem. By enabling EV owners to shift their charging to off-peak hours or participate in grid-responsive incentives, we help reduce charging costs, improve charger availability, and support a more sustainable and balanced energy grid—ultimately enriching the overall EV charging experience.

## Solution

To further improve the EV charging experience and simplify participation in demand flexibility programs, DeCharge is building an AI-powered agent using the Google Agent Development Kit (ADK). This agent will act as a smart assistant for EV owners and energy stakeholders.

Leveraging multi-tool functionality, the agent will be capable of:

Understanding user intent through natural language conversations.

Suggesting personalized demand flexibility programs based on the user’s location, battery status, and preferences.

Publishing demand programs to the Beckn protocol network on behalf of the user.

Discovering and recommending matching offers from supply-side participants (e.g., charge point operators, utilities).

Facilitating real-time decisions like confirming participation, reserving a slot, or accepting incentive offers.

Tracking program status and notifications—all via a seamless, conversational experience.

By combining the open, interoperable Beckn protocol with a context-aware AI agent, DeCharge aims to create a truly intelligent and user-centric ecosystem for demand-side energy participation in the EV charging domain.

## Team Members
- Mohan Ponnada
- Prakash
- Tagore Navabothu

## Tech Stack
### 🔹 Python FastAPI
- High-performance backend API framework
- Manages business logic, session handling, and Beckn API calls
- Enables async communication and scalable microservice architecture

### 🔹 Beckn Protocol
- Open, interoperable protocol for decentralized commerce
- Facilitates seamless discovery and fulfillment of EV demand programs
- Ensures secure and standardized interaction between buyers (EV users) and sellers (CPOs, utilities)

### 🔹 Google ADK (Agent Development Kit)
- Builds an intelligent, multi-tool AI assistant
- Capable of multi-turn conversations and task execution
- Integrates user preferences, makes suggestions, and triggers actions such as:
  - Publishing demand programs
  - Matching supply offers
  - Confirming participation
  - Notifying users

## Setup Instructions

Follow these steps to get the DeCharge backend and AI agent running locally.
### 1. Clone the Repository
git clone https://github.com/techdecharge/team-16-energentic-hackathon
cd team-16-energentic-hackathon

### 2. Download the .env File
Download the environment configuration file from the link below and place it in the root directory of the project:
https://drive.google.com/file/d/1BSxNC5YsJg46c-H-FPjpKPEJQhN3juBj/view?usp=drive_link

### 3.  Create a Python Virtual Environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

### 4. Install Dependencies
pip install google-adk

### 5. Run the FastAPI Backend
python server.py

### 6. Launch the Google ADK Agent
adk web


## Demo video link
- https://www.loom.com/share/acf87152ad5d41af851ac24252e61bac

## Screenshots / Visuals

 ![WhatsApp Image 2025-05-16 at 10 15 56 AM](https://github.com/user-attachments/assets/c02dae4a-22fc-4dd5-a630-5fa66a329f12)

## Challenges & Learnings
- Using Google ADK with multi-tool functionality posed challenges like managing shared context, chaining tool responses, and debugging silent failures. Designing each tool with clear inputs and outputs was crucial.
- We learned to treat tools like APIs. This setup now enables our agent to perform complex EV charging tasks seamlessly.

## Useful Resources
- create a python virtaul envorminet 
    - https://docs.python.org/3/library/venv.html
- Google adk installation 
    - https://pypi.org/project/google-adk/
- Goole adk referenes
    - https://google.github.io/adk-docs/
    - https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/
    - https://cloud.google.com/vertex-ai/generative-ai/docs/agent-development-kit/quickstart
