# Building a Rule-Based AI System in Python – Movie Recommendation System

---

## Part 1: Initial Project Ideas

### 1. Project Idea 1: Movie Recommendation System
- **Description:**  
  A small AI program that recommends movies based on the user’s preferred genre. The user types in a genre like *action*, *comedy*, or *drama*, and the system replies with matching movie suggestions.  
- **Rule-Based Approach:**  
  - It uses simple `if-else` rules that check for keywords in the user’s input (like “action” or “comedy”).  
  - Each rule corresponds to a genre and outputs a preset list of movies.  
- **Example Rules:**  
  - If the input contains “action,” recommend *John Wick* and *Mad Max: Fury Road*.  
  - If the input contains “comedy,” recommend *Superbad* and *The Hangover*.  
  - If the input contains “drama,” recommend *The Shawshank Redemption*.  

---

### 2. Project Idea 2: Financial Advisor Assistant
- **Description:**  
  A basic text-based assistant that gives short financial tips depending on the user’s spending or saving habits.  
- **Rule-Based Approach:**  
  - The system applies logical `if-else` conditions to analyze user input about income and expenses.  
  - Each rule corresponds to a financial situation and gives advice.  
- **Example Rules:**  
  - If expenses > income, suggest creating a budget.  
  - If savings < 10% of income, advise saving more each month.  
  - If savings > 20% of income, praise the user’s financial management.  

---

### 3. Project Idea 3: Mental Health Support Bot
- **Description:**  
  A supportive chatbot that provides simple wellness advice based on how the user says they’re feeling.  
- **Rule-Based Approach:**  
  - It detects emotional keywords (like “stressed,” “tired,” or “lonely”) and uses predefined responses to offer comfort or self-care tips.  
- **Example Rules:**  
  - If the message contains “stressed,” respond with “Try taking a few deep breaths or a short walk.”  
  - If it contains “tired,” suggest resting or sleeping.  
  - If it contains “lonely,” recommend reaching out to a friend.  

---

### **Chosen Idea:** Movie Recommendation System  
**Justification:**  
I chose the movie recommendation system because I love movies and it sounds fun to work on. It’s a cool way to mix my interest in films with coding and see how basic AI rules can make simple suggestions.

---

## Part 2: Rules/Logic for the Chosen System

### **Basic Flow (How the System Works)**
1. Ask the user:  
   “What kind of movie are you in the mood for? (e.g., action, comedy, horror, romance, sci-fi)”  
2. Read their text input.  
3. Check the text for certain keywords.  
4. Based on which keyword appears, return a fixed set of movie suggestions.  
5. If nothing matches, return a default response.  

All of this is handled using classic `if / elif / else` logic.

---

### **Example Rules**

**Rule 1 – Action Movies**  
- **Condition / Keywords to check:** “action,” “fight,” “superhero”  
- **Action / Response:**  
  “You might like: *John Wick*, *Mad Max: Fury Road*, or *The Dark Knight*.”

---

**Rule 2 – Comedy Movies**  
- **Condition / Keywords to check:** “comedy,” “funny,” “laugh”  
- **Action / Response:**  
  “You might like: *Superbad*, *21 Jump Street*, or *The Hangover*.”

---

**Rule 3 – Horror Movies**  
- **Condition / Keywords to check:** “horror,” “scary,” “thriller”  
- **Action / Response:**  
  “You might like: *The Conjuring*, *Get Out*, or *A Quiet Place*.”

---

**Rule 4 – Romance Movies**  
- **Condition / Keywords to check:** “romance,” “love,” “relationship”  
- **Action / Response:**  
  “You might like: *La La Land*, *The Notebook*, or *Crazy Rich Asians*.”

---

**Rule 5 – Fallback (No Match)**  
- **Condition:** None of the above keywords are found.  
- **Action / Response:**  
  “I’m not sure what genre that is. Try words like *action*, *comedy*, *horror*, or *romance*.”  

---

## Part 3: Sample Input and Output

| **Input** | **Expected Output** |
|------------|--------------------|
| I’m in the mood for a funny movie. | You might like: *Superbad*, *21 Jump Street*, or *The Hangover.* |
| I want something scary. | You might like: *The Conjuring*, *Get Out*, or *A Quiet Place.* |
| Give me a space movie. | I’m not sure what genre that is. Try words like *action*, *comedy*, *horror*, or *romance.* |

---

## Part 4: Reflection

### **Project Overview:**
For this project, I created a simple rule-based AI system that recommends movies based on a user’s preferred genre. The system uses a series of `if-elif-else` statements to check for keywords in the user’s input and respond with corresponding movie suggestions. It’s a straightforward demonstration of how early AI systems worked before machine learning became common.

### **Challenges:**
- **Keyword Coverage:**  
  One of the main challenges was deciding which keywords should trigger each genre. For example, “funny” should also trigger a comedy response, not just “comedy.”  
- **Input Handling:**  
  I had to ensure that the system converts user input to lowercase before comparison, otherwise it wouldn’t recognize words like “Action” or “Comedy.”  
- **Fallback Rule:**  
  Designing a good fallback message was also important to make sure the system always responds, even when it doesn’t understand the input.  

### **Takeaways:**  
I already have experience with Python and LLMs, so this project was a good reminder of how simple rule-based AI works. It showed how a few if and else statements can still create smart behavior, and it made me appreciate how much AI has evolved from basic logic to modern models.
