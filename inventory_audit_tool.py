import datetime

# --- CONFIGURATION ---
# Real-world pricing from your branch data
PRICES = {
    "Cement 25kg": 63.20,
    "Plywood Sheet": 245.50,
    "Box of Nails": 120.00,
    "Safety Vests": 55.00
}
MIN_ORDER_GLITCH = 3  # The central warehouse error threshold

def generate_audit_file(sales_data):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"Overstock_Audit_{timestamp}.txt"
    total_leak = 0
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write("--- 🛡️ BRANCH INVENTORY AUDIT REPORT ---\n")
        file.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        file.write("-" * 60 + "\n")
        file.write(f"{'Item':<20} | {'Sold':<5} | {'Invoiced':<10} | {'Loss (SEK)'}\n")
        file.write("-" * 60 + "\n")

        for item, sold in sales_data.items():
            invoiced = max(sold, MIN_ORDER_GLITCH)
            overbought = invoiced - sold
            price = PRICES.get(item, 0)
            loss = overbought * price
            total_leak += loss
            file.write(f"{item:<20} | {sold:<5} | {invoiced:<10} | {loss:>10.2f}\n")

        file.write("-" * 60 + "\n")
        file.write(f"TOTAL CAPITAL TIED UP: {total_leak:.2f} SEK\n")
        file.write("\nANALYSIS: Discrepancy detected in replenishment logic.")

    print(f"✅ Audit file created: {filename}")

# --- INTERACTIVE TERMINAL ---
all_sales = {}
print("🏗️  OFFICE-TO-WAREHOUSE AUDIT SYSTEM")
print("Type 'done' when finished.")

while True:
    item = input("\nArticle Name: ").strip()
    if item.lower() == 'done': break
    try:
        qty = int(input(f"Units of '{item}' sold: "))
        all_sales[item] = qty
    except ValueError:
        print("❌ Please enter a number.")

if all_sales:
    generate_audit_file(all_sales)
