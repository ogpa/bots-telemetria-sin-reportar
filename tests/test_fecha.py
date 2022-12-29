from datetime import datetime, timedelta

d = datetime.today() - timedelta(days=1)


# dd/mm/YY
d1 = d.strftime("%Y%m%d")
print("d1 =", d1)
