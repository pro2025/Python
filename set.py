st = set("MISSISSIPPI")
print(st, type(st))

st = {"red", "green", "red", "blue", "green", "blue"}
print(st)

st = {"c", "cpp", "js", "python"}
fa = {"c", "cpp", "ml", "scala"}

print(st.union(fa))
print(st.intersection(fa))
print(st.difference(fa))
print(fa.difference(st))
print(st.symmetric_difference(fa))

st = {"js", "python"}
fa = {"ml", "scala"}
print(st.isdisjoint(fa))
