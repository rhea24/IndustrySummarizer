import cohere

print("Welcome to the industry landscape generator. When you enter the links to several companies in a particular industry, I will summarize the industry for you.")

try:
    numCompanies = int(input("How many companies would you like to enter? "))
except ValueError:
    print("That's not a valid number of companies.")

links = []

for i in range(numCompanies):
    links.append(input(f"Enter the link to company {i+1}'s website. "))


co = cohere.Client(api_key) # api_key variable stores Cohere API key (enter your own API key here to run the file as intended)

summarizePrompt = "Generate a 5-10 paragraph summary of the industry based on the following companies' websites: "

for i in range(numCompanies):
    summarizePrompt += f"\n {links[i]}"

response = co.chat(
	message=summarizePrompt
)

print(response.text)