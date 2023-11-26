class EcopointsManager:
    """
    Manages ecopoints for a user.
    """

    def __init__(self, initial_ecopoints, conversion_rate):
        """
        Initializes the ecopoints manager with the initial ecopoints and conversion rate.

        Args:
            initial_ecopoints (int): The initial number of ecopoints.
            conversion_rate (float): The conversion rate from price to ecopoints.
        """
        self.ecopoints = initial_ecopoints
        self.conversion_rate = conversion_rate

    def earn_ecopoints(self, price):
        """
        Earn ecopoints from a price.

        Args:
            price (float): The price to earn ecopoints from.

        Returns:
            int: The updated number of ecopoints.
        """
        try:
            price = float(price)
        except ValueError:
            raise ValueError("Invalid price")

        ecopoints = price / self.conversion_rate
        ecopoints = round(ecopoints)
        self.ecopoints += ecopoints
        return self.ecopoints

    def redeem_ecopoints(self, number_of_ecopoints, service, level):
        """
        Redeem ecopoints for a service.

        Args:
            number_of_ecopoints (int): The number of ecopoints to redeem.
            service (str): The service to redeem ecopoints for (voice, data, or electricity).
            level (int): The user's level.

        Returns:
            float: The redeemed value.
        """
        try:
            number_of_ecopoints = int(number_of_ecopoints)
            level = int(level)
        except ValueError:
            raise ValueError("Invalid number of ecopoints or level")

        service = service.lower()

        if service not in ['voice', 'data', 'electricity']:
            raise ValueError("Invalid service")

        redemption_rate = self.get_redemption_rate(service, level)

        if number_of_ecopoints > self.ecopoints:
            raise ValueError("Insufficient ecopoints")

        redeemed_value = number_of_ecopoints / redemption_rate
        self.ecopoints -= redeemed_value
        return redeemed_value

    def get_redemption_rate(self, service, level):
        """
        Gets the redemption rate for a service and level.

        Args:
            service (str): The service to get the redemption rate for (voice, data, or electricity).
            level (int): The user's level.

        Returns:
            float: The redemption rate.
        """
        redemption_rates = {
            'voice': {
                1: 10,
                2: 8,
                3: 6,
                4: 4,
            },
            'data': {
                1: 20,
                2: 16,
                3: 12,
                4: 8,
            },
            'electricity': {
                1: 30,
                2: 24,
                3: 18,
                4: 12,
            },
        }

        return redemption_rates[service][level]


ecopoints_manager = EcopointsManager(initial_ecopoints=200, conversion_rate=100)

# Earn ecopoints
price = 10.00
total_ecopoints = ecopoints_manager.earn_ecopoints(price)
print("Total ecopoints:", total_ecopoints)

# Redeem ecopoints
number_of_ecopoints = 200
service = "voice"
level = 3

try:
    redeemed_value = ecopoints_manager.redeem_ecopoints(number_of_ecopoints, service, level)
    print("Redeemed value:", redeemed_value)
    print("Remaining ecopoints:", ecopoints_manager.ecopoints)
except ValueError as error:
    print(error)
