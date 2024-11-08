# Personal Article Bookmark Tool

It is a Python (fastapi) web application using the Wikipedia API that allows users to
search for Wikipedia articles based on a keyword. It should display the results and allow
users to save their favorite articles.

## Following frameworks/modules are used it this project:
* Fastapi
* sqlAlchemy
* Pydentic

## Following external api’s are used it this project:
* Wikipedia Api
* Texteazor

## Project system design
![Flow](https://github.com/user-attachments/assets/c8021257-8381-477b-b54b-e38e4a990eb3)

## Setup the app on local machine
To run the application on local machine you should have installed the following:
* Python
* Git

## Download and run
### Clone the repo from github
Open command prompt and type the following commands:
  ```
  git clone https://github.com/LokeshJangid01/wiki-search-api
  ```
### Create virtual env or activate the env if already created
```
python -m venv v
v\Scripts\activate
```
### Install dependencies
```
pip install -r requirements.txt
```
### Run server
```
uvicorn app:app --reload
```
# To use the application 
 After running the server with command uvicorn app:app --reload use either postman or curl cli
## Root url [localhost](http://127.0.0.1:8000) or (http://127.0.0.1:8000)
### json response
```
{
    "greeting": "Welome to wiki search api"
}
```
## Search url (http://127.0.0.1:8000/search) 
### payload for search url 
```
{
  "keyword": "laptop computer"
}
```
### json response
```
{
    "title": "Ruby (programming language)",
    "summary": "Ruby is an interpreted, high-level, general-purpose programming language. It was designed with an emphasis on programming productivity and simplicity. In Ruby, everything is an object, including primitive data types. It was developed in the mid-1990s by Yukihiro \"Matz\" Matsumoto in Japan.\nRuby is dynamically typed and uses garbage collection and just-in-time compilation. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. According to the creator, Ruby was influenced by Perl, Smalltalk, Eiffel, Ada, BASIC, Java, and Lisp."
}
```
## Add to favorite url http://127.0.0.1:8000/favorites/ *post request*
### payload for favorite url
```
{
    "title": "Laptop",
    "summary": "A laptop computer or notebook computer, also known as a laptop or notebook, is a small, portable personal computer (PC). Laptops typically have a clamshell form factor with a flat-panel screen on the inside of the upper lid and an alphanumeric keyboard and pointing device on the inside of the lower lid. Most of the computer's internal hardware is fitted inside the lower lid enclosure under the keyboard, although many modern laptops have a built-in webcam at the top of the screen, and some even feature a touchscreen display. In most cases, unlike tablet computers which run on mobile operating systems, laptops tend to run on desktop operating systems, which were originally developed for desktop computers.\nLaptops can run on both AC power and rechargable battery packs and can be folded shut for convenient storage and transportation, making them suitable for mobile use. Laptops are used in a variety of settings, such as at work (especially on business trips), in education, for playing game"
}
```
### json response 
```
{
    "message": "Article 'Laptop' added to favorites",
    "article": {
        "title": "Laptop",
        "tags": "Laptop,Computer,Laptop,Computer,Laptop",
        "id": 6,
        "summary": "A laptop computer or notebook computer, also known as a laptop or notebook, is a small, portable personal computer (PC). Laptops typically have a clamshell form factor with a flat-panel screen on the inside of the upper lid and an alphanumeric keyboard and pointing device on the inside of the lower lid. Most of the computer's internal hardware is fitted inside the lower lid enclosure under the keyboard, although many modern laptops have a built-in webcam at the top of the screen, and some even feature a touchscreen display. In most cases, unlike tablet computers which run on mobile operating systems, laptops tend to run on desktop operating systems, which were originally developed for desktop computers.\nLaptops can run on both AC power and rechargable battery packs and can be folded shut for convenient storage and transportation, making them suitable for mobile use. Laptops are used in a variety of settings, such as at work (especially on business trips), in education, for playing game"
    }
}
```
## favorite arrical list http://127.0.0.1:8000/favorites/ *get request*
### json response
```
{
    "favorites": [
        {
            "summary": "Rajasthan (; Hindi: [raːdʒəsˈtʰaːn] ; lit. 'Land of Kings') is a state in northwestern India. It covers 342,239 square kilometres (132,139 sq mi) or 10.4 per cent of India's total geographical area. It is the largest Indian state by area and the seventh largest by population. It is on India's northwestern side, where it comprises most of the wide and inhospitable Thar Desert (also known as the Great Indian Desert) and shares a border with the Pakistani provinces of Punjab to the northwest and Sindh to the west, along the Sutlej-Indus River valley. It is bordered by five other Indian states: Punjab to the north; Haryana and Uttar Pradesh to the northeast; Madhya Pradesh to the southeast; and Gujarat to the southwest. Its geographical location is 23°.3' to 30°.12' North latitude and 69°.30' to 78°.17' East longitude, with the Tropic of Cancer passing through its southernmost tip.\nIts major features include the ruins of the Indus Valley civilisation at Kalibangan and Balathal, the Dilwara",
            "tags": "is,is,of",
            "id": 1,
            "title": "Rajasthan"
        },
]
}
```

