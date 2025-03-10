from ticket import Ticket
from queue import Queue
from stack import Stack
from linkedlist import LinkedList
from ticket_array import Array  # Updated import


def display_available_tickets(available_tickets):
    print("\nAvailable Tickets:")
    for ticket in available_tickets:
        if ticket is not None:
            print(ticket)


def main():
    queue = Queue()
    stack = Stack()
    booked_tickets_list = LinkedList()

    # Create an array for available tickets
    available_tickets = Array(10)

    # Sample tickets
    sample_tickets = [
        Ticket(1, "Concert", 100),
        Ticket(2, "Movie", 50),
        Ticket(3, "Play", 75),
        Ticket(4, "Football Match", 120),
        Ticket(5, "Art Exhibition", 30),
        Ticket(6, "Comedy Show", 60),
        Ticket(7, "Dance Performance", 90),
        Ticket(8, "Opera", 150),
        Ticket(9, "Musical", 110),
        Ticket(10, "Festival", 80)
    ]

    # Adding sample tickets to the array
    for ticket in sample_tickets:
        available_tickets.append(ticket)

    while True:
        display_available_tickets(available_tickets)
        choice = input(
            "\nDo you want to book a ticket (b), cancel a ticket (c), view booked tickets (v), undo last booking (u), or exit (e)? ").strip().lower()

        if choice == 'b':
            ticket_id = int(input("Enter ticket ID to book: "))
            ticket = next((t for t in available_tickets.data if t and t.ticket_id == ticket_id), None)
            if ticket:
                queue.enqueue(ticket)
                booked_tickets_list.append(ticket)
                stack.push(ticket)  # Push the booked ticket onto the stack
                print(f"Ticket {ticket} booked successfully!")
                # Remove the booked ticket from the available tickets
                available_tickets.remove(ticket)
            else:
                print("Invalid ticket ID.")

        elif choice == 'c':
            if queue.is_empty():
                print("No tickets booked yet.")
            else:
                print("Booked Tickets:")
                booked_tickets = []
                while not queue.is_empty():
                    booked_tickets.append(queue.dequeue())

                for booked_ticket in booked_tickets:
                    print(booked_ticket)

                ticket_id = int(input("Enter ticket ID to cancel: "))
                canceled_ticket = next((t for t in booked_tickets if t.ticket_id == ticket_id), None)
                if canceled_ticket:
                    available_tickets.append(canceled_ticket)  # Add back to available tickets
                    print(f"Ticket {canceled_ticket} canceled successfully!")
                else:
                    print("Invalid ticket ID for cancellation.")

        elif choice == 'v':
            print("\nBooked Tickets:")
            current = booked_tickets_list.head
            if current is None:
                print("No tickets booked yet.")
            else:
                while current:
                    print(current.data)
                    current = current.next

        elif choice == 'u':
            if stack.is_empty():
                print("No bookings to undo.")
            else:
                last
                _ticket = stack.pop()
                available_tickets.append(last_ticket)  # Add back to available tickets
                print(f"Booking for ticket {last_ticket} has been undone.")

        elif choice == 'e':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please enter 'b', 'c', 'v', 'u', or 'e'.")


if __name__ == "__main__":
    main()