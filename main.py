import random
import time

class FinancialAgent:
    """
    A simple agent designed to monitor financial transactions and flag suspicious ones.
    This simulates a basic decision-making agent in a BFSI (Banking, Financial Services, Insurance) context.
    """
    def __init__(self, agent_id, high_value_threshold=5000):
        self.agent_id = agent_id
        self.high_value_threshold = high_value_threshold # Agent's internal parameter for high-value transactions
        self.transaction_history = [] # Agent's memory to potentially learn or detect patterns
        print(f"Agent {self.agent_id} initialized. Monitoring for suspicious activities.")

    def _analyze_transaction(self, transaction):
        """
        Internal method where the agent's 'intelligence' or decision logic resides.
        It applies rules to determine if a transaction is suspicious.
        """
        is_suspicious = False
        reasons = []

        # Rule 1: Check for unusually high transaction value
        # This demonstrates the agent making an automated decision based on a threshold.
        if transaction['amount'] > self.high_value_threshold:
            is_suspicious = True
            reasons.append(f"High value transaction (${transaction['amount']:.2f} exceeds ${self.high_value_threshold:.2f})")

        # Rule 2: Check for transactions from a 'risky' country (simplified example)
        # This shows the agent reacting to environmental data (transaction origin).
        if transaction['country'] in ['Nigeria', 'Russia', 'North Korea']:
            is_suspicious = True
            reasons.append(f"Transaction from a high-risk country ({transaction['country']})")

        # Rule 3: Simulate a pattern detection (e.g., frequent small transactions, or random anomaly)
        # A more advanced agent would analyze self.transaction_history for patterns.
        # For this simple example, we'll use a random chance to flag small transactions.
        if transaction['amount'] < 100 and random.random() < 0.15: # 15% chance to flag small transactions as potentially suspicious
             is_suspicious = True
             reasons.append("Unusual pattern of small transactions (simulated anomaly)")

        return is_suspicious, reasons

    def process_transaction(self, transaction):
        """
        The main method for the agent to perceive a new transaction and act upon it.
        This simulates the agent's interaction with its environment.
        """
        print(f"\nAgent {self.agent_id} perceiving transaction: {transaction['id']} - ${transaction['amount']:.2f} from {transaction['country']}")
        self.transaction_history.append(transaction) # Agent updates its internal state/memory

        is_suspicious, reasons = self._analyze_transaction(transaction) # Agent makes a decision

        if is_suspicious:
            print(f"  🚨 ALERT: Transaction {transaction['id']} FLAGGED as SUSPICIOUS!")
            for reason in reasons:
                print(f"    - Reason: {reason}")
            return "FLAGGED" # Agent takes an action
        else:
            print(f"  ✅ Transaction {transaction['id']} APPROVED.")
            return "APPROVED" # Agent takes an action

# --- Main simulation --- 
if __name__ == "__main__":
    # Initialize our financial agent
    fraud_agent = FinancialAgent(agent_id="FraudDetector-001", high_value_threshold=5000)

    # Simulate a series of transactions that the agent will process
    transactions = [
        {"id": "TRX001", "amount": 150.00, "country": "USA"},
        {"id": "TRX002", "amount": 7500.00, "country": "Canada"}, # High value
        {"id": "TRX003", "amount": 50.00, "country": "Germany"},
        {"id": "TRX004", "amount": 12000.00, "country": "UK"}, # High value
        {"id": "TRX005", "amount": 25.00, "country": "Nigeria"}, # Risky country
        {"id": "TRX006", "amount": 300.00, "country": "USA"},
        {"id": "TRX007", "amount": 80.00, "country": "Russia"}, # Risky country
        {"id": "TRX008", "amount": 4500.00, "country": "Australia"},
        {"id": "TRX009", "amount": 90.00, "country": "USA"}, # Small transaction, might get flagged by chance
        {"id": "TRX010", "amount": 1000.00, "country": "France"},
    ]

    print("\n--- Starting Transaction Processing Simulation ---")
    for i, trx in enumerate(transactions):
        fraud_agent.process_transaction(trx)
        time.sleep(0.3) # Simulate some processing time between transactions
    print("\n--- Simulation Complete ---")
