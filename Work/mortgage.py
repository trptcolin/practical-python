# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    updated_owed = principal * (1 + rate / 12)

    this_months_payment = payment
    if months >= extra_payment_start_month and months < extra_payment_end_month:
        this_months_payment += extra_payment

    if this_months_payment > updated_owed:
        this_months_payment = updated_owed

    principal = updated_owed - this_months_payment

    total_paid += payment
    months += 1
    print(f"{months:10d}\t{total_paid:10.2f}\t{principal:10.2f}")

print(f"Total paid ${total_paid:10.2f}", end=" ")
print("over", months, "months")
