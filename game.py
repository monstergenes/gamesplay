import os
from Jinja2 import Environment, FileSystemLoader
import markdown

# Set up Jinja2 environment
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
env = Environment(loader=FileSystemLoader(r"C:/Users/Mares/game/project_directory")
)  # noqa: F821

# Output directory for generated site
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process each page
pages_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pages")
for filename in os.listdir(pages_dir):
    if filename.endswith(".md"):
        # Read markdown content
        with open(os.path.join(pages_dir, filename), "r") as file:
            content = file.read()

        # Convert markdown to HTML
        html_content = markdown.markdown(content)

        # Get template
        template = env.get_template("base.html")

        # Render template with content
        output_html = template.render(title="My Static Site", content=html_content)

        # Write generated HTML to file
        output_filename = os.path.splitext(filename)[0] + ".html"
        with open(os.path.join(output_dir, output_filename), "w") as file:
            file.write(output_html)


class BitcoinGame:
    def __init__(self, initial_balance=10000, bitcoin_price=50000):
        self.balance = initial_balance
        self.bitcoin_price = bitcoin_price
        self.bitcoin_holdings = 0

    def display_menu(self):
        print("\n1. Buy Bitcoin")
        print("2. Sell Bitcoin")
        print("3. Check Balance")
        print("4. Quit")

    def buy_bitcoin(self):
        try:
            amount = float(input("Enter the amount to buy (USD): "))
            if amount <= 0 or amount * self.bitcoin_price > self.balance:
                print("Invalid amount or insufficient balance.")
                return

            self.bitcoin_holdings += amount / self.bitcoin_price
            self.balance -= amount
            print(f"Successfully bought {amount / self.bitcoin_price:.6f} Bitcoin.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def sell_bitcoin(self):
        try:
            amount = float(input("Enter the amount to sell (Bitcoin): "))
            if amount <= 0 or amount > self.bitcoin_holdings:
                print("Invalid amount or insufficient Bitcoin holdings.")
                return

            self.bitcoin_holdings -= amount
            self.balance += amount * self.bitcoin_price
            print(f"Successfully sold {amount:.6f} Bitcoin.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def check_balance(self):
        print(f"Balance: ${self.balance:.2f}")
        print(f"Bitcoin Holdings: {self.bitcoin_holdings:.6f} BTC")
        print(f"Bitcoin Price: ${self.bitcoin_price:.2f}")

    def play_game(self):
        print("Welcome to the Bitcoin Trading Game!")

        while True:
            self.display_menu()

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.buy_bitcoin()
            elif choice == "2":
                self.sell_bitcoin()
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                print("Thanks for playing. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    game = BitcoinGame()
    game.play_game()
