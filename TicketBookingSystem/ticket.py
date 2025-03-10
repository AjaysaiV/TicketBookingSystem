class Ticket:
    def __init__(self, ticket_id, event_name, price):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.price = price

    def __str__(self):
        return f"Ticket ID: {self.ticket_id}, Event: {self.event_name}, Price: Rs{self.price}"