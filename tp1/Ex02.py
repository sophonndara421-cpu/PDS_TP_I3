total_seconds = 3900
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print("totalsecond:", total_seconds)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
print(".....................................")
print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")