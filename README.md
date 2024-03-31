# Bitcoin Trading Game Description
The Bitcoin Trading Game is a simple command-line based game that simulates buying and selling Bitcoin in a dynamic market environment. Players are given an initial balance in USD and can make decisions to buy or sell Bitcoin based on the current Bitcoin price. The objective of the game is to maximize the player's balance by making strategic decisions in buying and selling Bitcoin.

# Features:
Buy Bitcoin: Players can enter the amount of USD they want to invest in Bitcoin. The game calculates the corresponding amount of Bitcoin based on the current Bitcoin price and deducts the invested amount from the player's balance.

# Sell Bitcoin:
Players can choose to sell a portion of their Bitcoin holdings. They enter the amount of Bitcoin they wish to sell, and the game calculates the equivalent USD amount based on the current Bitcoin price. The USD amount is added to the player's balance.

# Check Balance:
Players can check their current balance in USD, the amount of Bitcoin they hold, and the current price of Bitcoin.

# Dynamic Market: 
The game simulates a dynamic market environment where the price of Bitcoin fluctuates. This adds an element of unpredictability, requiring players to adapt their trading strategies.

# How to Play:
Start the Game: Run the Python script containing the BitcoinGame class. The game initializes with a default balance and Bitcoin price.

# Menu Navigation:
The game presents a menu with options to buy Bitcoin, sell Bitcoin, check balance, or quit.

# Buying Bitcoin: 
Choose the option to buy Bitcoin and enter the amount of USD you want to invest. The game calculates the equivalent amount of Bitcoin and deducts the invested USD from your balance.

# Selling Bitcoin: 
Select the option to sell Bitcoin and enter the amount of Bitcoin you want to sell. The game calculates the equivalent USD amount based on the current Bitcoin price and adds it to your balance.

# Checking Balance: 
Choose the option to check balance to view your current balance in USD, the amount of Bitcoin you hold, and the current price of Bitcoin.

 # Exiting the Game:
 Select the option to quit when you're done playing.

# Objective:
The goal of the Bitcoin Trading Game is to make strategic decisions to increase your balance by buying and selling Bitcoin at opportune moments. Navigate the market fluctuations wisely to maximize your profits and achieve the highest possible balance.

# Note:
The game is intended for educational and entertainment purposes only. It does not involve real financial transactions or actual ownership of Bitcoin.
The market dynamics and prices in the game are simulated and do not reflect real-world market conditions.
Enjoy the game responsibly and have fun exploring the world of Bitcoin trading in a risk-free environment!

## Installation and Usage Guide
### Setting up Jinja2 Environment
Ensure Python is installed on your system. If not, download and install Python from the official Python website.

Open a terminal or command prompt.

Clone or download the code repository to your local machine.

Navigate to the directory where the code is saved.

Open the Python script file where you intend to use the Jinja2 environment.

Add the following code snippet to set up the Jinja2 environment:
```
import os
from jinja2 import Environment, FileSystemLoader
import markdown

# Set up Jinja2 environment
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
env = Environment(loader=FileSystemLoader(r"C:/Users/project_directory"))  # noqa: F821
```
