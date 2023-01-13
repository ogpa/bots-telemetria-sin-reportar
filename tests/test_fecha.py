from datetime import datetime, timedelta

d = datetime.today() - timedelta(days=0)


# dd/mm/YY
d1 = d.strftime("%Y%m%d")
print("d1 =", d1)
