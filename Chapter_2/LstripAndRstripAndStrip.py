s = "    python"
print(s,len(s))

s = s.lstrip()
print(s,len(s))

s = "python     "
print(s,len(s))

s = s.rstrip()
print(s)


s = "    python     "
print(s,len(s))


s = s.strip()
print(s)


s = "Rohith  singh     "
print(s,len(s))
s = s.strip()
print(s,len(s))

s = "   ".join(s.split())
print(s)


s = "++++++++++++PYTHON++++++++"
s = s.strip("+")
print(s)

s = "**********python*********"
s = s.strip("*")
print(s)
