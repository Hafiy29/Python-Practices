
monthConversions = [
    "Jan":"January",
    "Feb":"Febuary",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
    }


print(monthConversions["Mar"])
print(monthConversions.get("Jan"))
print(monthConversions.get("love","not a valid key"))
