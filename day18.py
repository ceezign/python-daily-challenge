# # Read from the input file
# with open("tex.txt", "r") as file:
#     lines = file.readlines()
#
# domains = []
#
# for line in lines:
#     line = line.strip()
#     if "@" in line:  # check if it's an email
#         domain = line.split("@")[1]
#         domains.append(domain)
#
# # Write the domains into a new file
# with open("text1.txt", "w") as outfile:
#     for d in domains:
#         outfile.write(d + "\n")
#
# print("Domains saved to text1.txt")


# Read from the input file
# with open("tex.txt", "r") as file:
#     lines = file.readlines()
#
# results = []
#
# for line in lines:
#     line = line.strip()
#     if "@" in line:  # check if it's an email
#         email = line
#         domain = line.split("@")[1]
#         results.append(f"{email}\n{domain}\n")  # keep email + domain together
#
# # Write to output file with a blank line between entries
# with open("text2.txt", "w") as outfile:
#     for item in results:
#         outfile.write(item + "\n")  # extra newline for spacing
#
# print("text2 saved to emails_and_domains.txt")
#


#  # Read from the input file
# with open("text1.txt", "r") as file:
#     lines = file.readlines()
#
# domains = []
#
# for line in lines:
#     line = line.strip()
#     if "@" in line:  # only process email lines
#         domain = "@" + line.split("@")[1]  # keep @ before the domain
#         domains.append(domain)
#
# # Write the results to a new file with a blank line after each domain
# with open("text2.txt", "w") as outfile:
#     for d in domains:
#         outfile.write(d + "\n\n")  # double newline for spacing
#
# print("Domains saved to domains.txt")


##### Read the input file
# with open("text.txt", "r") as file:
#     lines = [line.strip() for line in file.readlines() if line.strip()]
#
# blocks = []
# for i in range(0, len(lines), 2):  # process in pairs: name + email
#     if i + 1 < len(lines):
#         name = lines[i]
#         email = lines[i + 1]
#         blocks.append(f"{name}\n{email}")
#
# # Write to output file with an extra blank line between entries
# with open("text1.txt", "w") as outfile:
#     for block in blocks:
#         outfile.write(block + "\n\n\n")  # two blank lines after each block
#
# print("File saved as cleaned_data.txt with extra breaklines")

#
# # Open the input file
# with open("tex.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#
# # Clean each line (remove leading/trailing spaces + collapse multiple spaces)
# cleaned_lines = [" ".join(line.split()) for line in lines if line.strip()]
#
# # Write back to a new file
# with open("text1.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(cleaned_lines))
#
# print("Cleaning done!


# split_and_save.py
#
# def split_name_email_file(input_file, output_file):
#     with open(input_file, "r") as file:
#         lines = file.readlines()
#
#     with open(output_file, "w") as out:
#         for line in lines:
#             line = line.strip()
#             if not line:
#                 continue
#
#             parts = line.split()
#             email_idx = next((i for i, p in enumerate(parts) if "@" in p), None)
#
#             if email_idx is not None:
#                 name = " ".join(parts[:email_idx])
#                 email = parts[email_idx]
#                 out.write(f"{name}\n{email}\n\n")  # add a blank line after each pair
#
#
# # Example usage:
# split_name_email_file("tex.txt", "text.txt")