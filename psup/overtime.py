def calculate_overtime(hours_worked,hourly_wages):
    overtime_pay=0
    if hours_worked>40:
        extra_hours=hours_worked-40
    for i in range(extra_hours):
      overtime_pay+=hourly_wages*1.5
    return overtime_pay
    

hours_worked=int(input("enter total hours worked"))
hourly_wage=float(input("enter the wage"))

print("overtime pay is", calculate_overtime(hours_worked,hourly_wage))
