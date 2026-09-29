# Elisa Tandra
undoneEvents = []

undoneEvents.append("Type Title")
undoneEvents.append("Insert Image")
undoneEvents.append("Change Color")
undoneEvents.append("Add Link")
undoneEvents.append("Remove Link")
undoneEvents.append("Increase Font Size")
undoneEvents.append("Change Font Style")
undoneEvents.append("Delete Item")
undoneEvents.append("Move Item")
undoneEvents.append("Resize Item")
print("Resetting item size...")
print("Redoing last undone event: " + undoneEvents[-1])
undoneEvents.pop()
print("Undone Events:" + str(undoneEvents))


# changing one list impacts the other list
undoneEvents2 = undoneEvents
undoneEvents2.append("Add Comment")
print("Deleting added comment...")
print("Redoing last undone event: " + undoneEvents[-1])

# Prevents changing one list from impacting the other list as we copy over the values of the first list into a new list
undoneEvents3 = undoneEvents[:]
undoneEvents3.append("Change Background Color")
print("Reseting background color...")
print("Redoing last undone event: " + undoneEvents[-1])
