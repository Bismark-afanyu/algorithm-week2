import datetime

# The Promocode class represents a promotional code with properties such as discount, validity, type,
# activation date, expiry date, usage limit, usage count, and status.
class Promocode:
    def __init__(self, discount, validity, type_of_promocode, activation_date, expiry_date, usage_limit, used, status):
        self.discount = discount
        self.validity = validity
        self.type_of_promocode = type_of_promocode
        self.activation_date = activation_date
        self.expiry_date = expiry_date
        self.usage_limit = usage_limit
        self.used = used
        self.status = status

# The class "Owner" represents an owner with attributes such as city, quarter, account type, and usage
# period.
class Owner:
    def __init__(self, city, quarter, account_type, usage_period):
        self.city = city
        self.quarter = quarter
        self.account_type = account_type
        self.usage_period = usage_period

def get_eligible_owners(promocode, city, quarter, owners):
    """
    The function `get_eligible_owners` takes in a promocode, city, quarter, and a list of owners, and
    returns a list of owners who are eligible based on the promocode criteria.
    
    :param promocode: The promocode parameter is an object that represents a promotional code. It has a
    property called "type_of_promocode" which indicates the type of the promotional code. The possible
    values for "type_of_promocode" are "Town", "Group", "business_owner", and "Everybody"
    :param city: The city parameter represents the city for which the eligibility of owners is being
    checked
    :param quarter: The "quarter" parameter refers to a specific time period, typically divided into
    four quarters of a year (Q1, Q2, Q3, Q4). It is used to filter owners based on their quarter of
    activity or ownership
    :param owners: The "owners" parameter is a list of objects representing different owners. Each owner
    object has properties such as "city", "quarter", "usage_period", and "account_type"
    :return: a list of eligible owners based on the given promocode, city, quarter, and owners.
    """
    eligible_owners = []

    for owner in owners:
        if promocode.type_of_promocode == "Town":
            if owner.city == city or owner.quarter == quarter:
                eligible_owners.append(owner)
        elif promocode.type_of_promocode == "Group":
            if owner.usage_period == promocode.usage_period and owner.city == city and owner.quarter == quarter and owner.account_type == promocode.account_type:
                eligible_owners.append(owner)
        elif promocode.type_of_promocode == "business_owner":
            if owner.account_type == "business":
                eligible_owners.append(owner)
        elif promocode.type_of_promocode == "Everybody":
            eligible_owners.append(owner)

    return eligible_owners

def apply_discount(promocode, price):
    """
    The function applies a discount to a given price if the promo code is active, within the activation
    and expiry dates, and has not reached the usage limit.
    
    :param promocode: The promocode parameter is an object that represents a promotional code. It should
    have the following attributes:
    :param price: The original price of the item before applying any discount
    :return: the discounted price if the conditions for applying the discount are met. If the conditions
    are not met, it returns the original price.
    """
    if promocode.status == "active" and promocode.activation_date <= datetime.date.today() <= promocode.expiry_date and promocode.used < promocode.usage_limit:
        discount_price = price - (price * (promocode.discount / 100))
        promocode.used += 1
        return discount_price
    else:
        return price

# Example usage
promocode = Promocode(discount=10, validity=30, type_of_promocode="Town", activation_date=datetime.date(2023, 11, 1), expiry_date=datetime.date(2023, 12, 1), usage_limit=10, used=0, status="active")
owners = [
    Owner(city="Yaounde", quarter="Messase", account_type="normal", usage_period=1),
    Owner(city="Douala", quarter="Bonamoussadi", account_type="business", usage_period=1),
    Owner(city="Yaounde", quarter="Etoa Meki", account_type="normal", usage_period=3),
]

eligible_owners = get_eligible_owners(promocode, "Yaounde", "Messase", owners)

for owner in eligible_owners:
    print(f"Owner: {owner.city} {owner.quarter} {owner.account_type} {owner.usage_period}")

# Example usage of apply_discount
price = 100  # Initial price before discount

discounted_price = apply_discount(promocode, price)

print(f"The discounted price is: {discounted_price}")
