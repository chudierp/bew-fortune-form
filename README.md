<h1>Fortune form</h1>
What happens when you press the “submit” button? Paste the full URL you are sent to on submit.

file:///action_page.php?firstname=CHUDIER&lastname=CHUOL&Siblings=2&animal=dog&city=omaha
Answer: the name fields from the form and user inputs shows in the query string when you hit the submit button.

What are the keys of this URL query string? How do they correspond to the “name” fields of your HTML form elements?
Answer: the keys are firstname, lastname, Siblings, animal and city and they are the name fields from my html forms.

what are the values of the URL query string? How do they correspond to what the user entered or typed?

Answer: the values are Chudier, Chuol, 2, dog, and omaha. They are what I put in or selected.

Stretch challenge question:

Is there a way to pass multiple values through the URL query string for a single key? How can we do so?
Answer: Yes there is, it will add a + sign to added values.
file:///action_page.php?firstname=chudier+yat+chuol&lastname=CHUOL&Siblings=2&animal=dog&city=omaha

<<<<<<< HEAD
<h1> Weather </h1>

<h4>Describe the data contained in the API response. What can we discern about the weather in the specified city?</h4>

There is more than one JSON dictionary with coordinates, weather, etc..

<h4>How would we obtain the temperature in the specified city? Describe using Python dictionary syntax. (HINT: Assume that the JSON response is stored in a variable called json_response.)</h4>

We would have to access the JSON dictionary with the variable name of "Main" then temp = request.args.get("temp")
=======

>>>>>>> 7d96ccfedac1a4bec0842c2e60d12e39d84dc530
