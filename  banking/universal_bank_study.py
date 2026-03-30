# Adding Financial Logic to your Spotify Project
def calculate_subscription_revenue(users, fee_rate=0.15):
    """
    Calculates the 'Asset Management' fee Spotify takes from 
    Premium subscriptions.
    """
    try:
        total_revenue = users * 9.99
        # The 'Universal Bank' style cut
        spotify_cut = total_revenue * fee_rate
        print(f"Total Subscription Revenue: ${total_revenue:.2f}")
        print(f"Spotify Management Fee (15%): ${spotify_cut:.2f}")
    except TypeError:
        print("Error: User count must be a number!")

# Specialist Tip: Always use float formatting (:.2f) for money!
