from tkinter import *

root = Tk()
root.title('Weather App')
root.geometry("670x120")

# creating a frame which displays the entry box where user can enter the name of district
lookup_frame = LabelFrame(root, text="Look up Place Weather", padx=5, pady=5)
lookup_frame.grid(row=0, column=0, padx=10, pady=10, stick=W + E + N + S)
place = Entry(lookup_frame)
place.grid(row=0, column=1, stick=W + E + N + S)


def place_lookup():
    # function which returns the weather of certain district
    try:
        import requests
        import json
        # converting the user input into lowercase
        lookup_city = place.get().lower()
        # getting the data from the weather api and parsing it
        api_request = requests.get("https://nepal-weather-api.herokuapp.com/api/?place=" + lookup_city)
        api = json.loads(api_request.content)
        city = api['place']
        max_temp = api['max']
        min_temp = api['min']
        rain = api['rain']

        my_label = Label(root,
                         text=city + " " + "Maximum Temperature: " + str(
                             max_temp) + " " + "Minimum Temperature: " + str(
                             min_temp) + " " + "Rain: " + str(rain), font=("Helvetica", 12))
        my_label.grid(row=1, column=0, columnspan=2)

    except KeyError:
        my_label = Label(root, text="Place not found please enter the name of ths district correctly.",
                         font=("Helvetica", 12))
        my_label.grid(row=1, column=0, columnspan=2)

    except EXCEPTION:
        my_label = Label(root, text="Something went wrong. Try Again", font=("Helvetica", 12))
        my_label.grid(row=1, column=0, columnspan=2)


# creating and displaying the submit button
submitButton = Button(lookup_frame, text="Lookup", command=place_lookup)
submitButton.grid(row=0, column=2, stick=W + E + N + S)

root.mainloop()
