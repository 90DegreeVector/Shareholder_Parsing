import re


web = """
Amazon.com (NASDAQ: AMZN) CEO Jeff Bezos is famous for telling his competitors that "your margin is my opportunity." But who ever thought he would say that 
to  Amazon's own suppliers of shipping services, FedEx (NYSE: FDX) and UPS (NYSE: UPS)?

This morning, though, that's exactly what happened, when Amazon told The Wall Street Journal that it plans to launch a "Shipping With Amazon" (SWA)  
business-to-consumer delivery service in Los Angeles, Calif. Shares of FedEx and UPS promptly plunged (falling as much as 5.5% and 4.7%, respectively).  
Curiously, Amazon.com's own stock followed suit, falling 6.3%. As we'll see in a moment, that last fact doesn't make much sense.

All three stocks recovered somewhat, but FedEx was still down 1.7% for the day, UPS 2.6% -- and Amazon 0.8%.
"""
answer = "To Our vision is to be earth's most customer-centric company; to build a place " \
         "where people can come to find and discover anything they might want to buy online to."



# something = re.search(r'\d+\.\d%', web)
# print(something)
#
# something = re.search(r'\d+\.\d%.*\n', web)
# print(something)
#
# something = re.search(r'\d+\.\d%.*', web, re.DOTALL)
# print(something.group(0))
#
# something = re.search(r'\d+\.\d%.*%', web, re.DOTALL)
# print(something.group(0))
#
# something = re.search(r'\d+\.\d%.*?%', web, re.DOTALL)
# print(something.group(0))
#
# something = re.search(r'(?P<percent>\d+\.\d%) for', web, re.DOTALL)
# print(something.group(0))
# print(something.group("percent"))
# print(something.group(1))


# something = re.match(r'.*(?P<percent>\d+\.\d%) for', web, re.DOTALL)
# if something:
#     print(something.group(0))
#     print(something.group("percent"))
#     print(something.group(1))

# print(re.findall(r'to', answer))
# print(re.findall(r'to', answer, re.IGNORECASE))
# print(re.findall(r'\bto\b', answer, re.IGNORECASE))
# print(re.findall(r'\b\w{2,4}\b', answer, re.IGNORECASE))

# print(re.sub(r'\b[Tto]o\b', '2', answer))

theorem = "a = 5, b = 105"

print(theorem)

print(re.sub(r'(\w) = (\d), (\w) = (\d+)', r'\2 = \1, \4 = \3', theorem))

print(re.sub(r'(\w) = (\d+), (\w) = (\d+)', r'\2 = \1, \4 = \3', theorem))