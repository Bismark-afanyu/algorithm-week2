class PriceDetermination:
    def calculate_volume(self, size, quantity):
        try:
            volume = (size / 1000) * quantity  # Volume in cubic meters
            return volume
        except ZeroDivisionError:
            print("Error: Size or quantity cannot be zero.")
            return 0

    def calculate_price(self, volume, package):
        price = volume * 0.05  # Price in XAF
        if package == 1:
            return price
        else:
            price1 = 1.2 * price
            #print (price1)
            return price1

    def bid(self, biding_price, price):
        try:
            if biding_price < price:
                return 0, "Price too low."
            else:
                return 1, "Bid approved."
        except TypeError:
            print("Error: Invalid biding price.")
            return 0, "Invalid biding price"

    def determine_price_and_bid(self):
        try:
            package = int(input("Select a package (1 for pickup / 0 for pickup and cleaning): "))
            if package not in [0, 1]:
                print("Error: Invalid package type.")
                return

            print("Select a trash size:")
            print("1. Bucket-10L")
            print("2. Trash bag-27L")
            print("3. Wheelbarrow-80L")
            trash_size_option = int(input("Enter the number for the trash size: "))
            if trash_size_option not in [1, 2, 3]:
                print("Error: Invalid trash size option.")
                return

            quantity = int(input(f"How many of the selected trash size do you have? "))

            trash_sizes = {
                1: 10,  # Bucket size in liters
                2: 27,  # Trash bag size in liters
                3: 80   # Wheelbarrow size in liters
            }

            selected_size = trash_sizes.get(trash_size_option)
            if selected_size is None:
                print("Error: Invalid trash size option.")
                return

            if quantity > 1:
                volume = self.calculate_volume(selected_size, quantity)
                price_1 = self.calculate_price(volume, package)
            elif quantity == 1:
                volume = selected_size / 1000
                price_1 = self.calculate_price(volume, 1)  # Always use pickup package for single item
            else:
                print("Error: Set a trash quantity of at least one")
                return

            biding_price = float(input("How much do you have for this Trash: "))
            status, message = self.bid(biding_price, price_1)
            print("Status:", "Approved" if status else "Rejected", message)
        except ValueError:
            print("Error: Invalid input.")

# Create an instance of the PriceDetermination class
pd = PriceDetermination()
# Call the determine_price_and_bid method
pd.determine_price_and_bid()
