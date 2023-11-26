class AgentSalaryCalculator:
    '''this class takes in the agent details'''
    def __init__(self, agent_name, month, booking_type, residential_bookings, commercial_bookings, shifts_worked):
    
        self.agent_name = agent_name
        self.month = month
        self.booking_type = booking_type
        self.residential_bookings = residential_bookings
        self.commercial_bookings = commercial_bookings
        self.shifts_worked = shifts_worked

    def calculate_total_bonus(self):
        ''' this method iterates over the list of residential bookings and calculates the bonus for each booking. It then adds the bonus for each booking to the total bonus.'''
        total_bonus = 0
        for booking in self.residential_bookings:
            if booking["quantity"] >= 20:
                total_bonus += 170000
            elif booking["quantity"] >= 10:
                total_bonus += 5000
            elif booking["quantity"] >= 5:
                total_bonus += 1000
            else:
                total_bonus += booking["quantity"] * 50
        return total_bonus

    def calculate_total_salary(self):
        '''this method calculates the total salary by adding the total bonus to the product of the number of shifts worked and the shift pay.'''
        total_salary = self.shifts_worked * 500 + self.calculate_total_bonus()
        return total_salary

    def print_salary_summary(self):
        ''' this method prints a summary of the agent's salary, including the agent's name, month, booking type, residential bookings, commercial bookings, shifts worked, total bonus, and total salary.'''
        print("Agent:", self.agent_name)
        print("Month:", self.month)
        print("Booking type:", self.booking_type)
        print("Residential bookings:", self.residential_bookings)
        print("Commercial bookings:", self.commercial_bookings)
        print("Shifts worked:", self.shifts_worked)
        print(f"Total bonus:, {self.calculate_total_bonus()} XAF")
        print(f"Total salary:, {self.calculate_total_salary()} XAF")

agent_salary_calculator = AgentSalaryCalculator(
    agent_name="John Ndi",
    month="October 2023",
    booking_type="residential",
    residential_bookings=[
        {"type": "residential", "quantity": 25},
        {"type": "residential", "quantity": 12},
        {"type": "residential", "quantity": 8},
    ],
    commercial_bookings=[],
    shifts_worked=20
)

agent_salary_calculator.print_salary_summary()
