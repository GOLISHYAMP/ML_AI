# # from datetime import datetime

# # # Given timestamps
# # timestamps = [
# #     "2024-06-25 16:25:50",
# #     "2024-06-25 20:25:50",
# #     "2024-06-26 08:01:01.609000"
# # ]

# # # Extract dates and store them in a set to remove duplicates
# # unique_dates = {datetime.fromisoformat(timestamp).date() for timestamp in timestamps}

# # # Convert the set to a list and print the unique dates
# # unique_dates_list = list(unique_dates)
# # print(unique_dates_list)
# from datetime import datetime

# # Given timestamps
# timestamps = [
#     "2024-06-25 16:25:50",
#     "2024-06-25 20:25:50",
#     "2024-06-26 08:01:01.609000"
# ]

# # Extract dates and store them in a set to remove duplicates
# unique_dates = {datetime.fromisoformat(timestamp).date() for timestamp in timestamps}

# # Convert the set to a sorted list of strings in 'YYYY-MM-DD' format
# unique_dates_list = sorted(date.isoformat() for date in unique_dates)

# # Print the unique dates
# print(unique_dates_list)
l = ["P","A","R","T","H"]
print(''.join(l))