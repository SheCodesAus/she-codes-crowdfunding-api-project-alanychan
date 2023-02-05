# {{ CrowdGift }}


{{ a paragraph detailing the purpose and target audience }}

#### Idea 1 - Let's get the Penguins on a summer holiday!!!
_"Funding for penguins Pierre & family to go on holidays in the tropics. They will need cold suitS to regulate their body temperature and have an amazing time holidaying in the Tropics!!! Let's get them what they need!!"_

_Target audience: everyone really, all animals lovers, penguins lovers, summer holidays lovers._

#### Idea 2 - A day in the forest for our children!
_"Funding for the classroom's next school trip to the forest!!! A change to the daily environment of our children, especially after the lockdown due to covid, and connect them to nature. A day in the forest can have positive impact on the wellbeing, physical and mental health of everyone! It helps reduce stress and anxiety, provides the excitement of going on an adventure and takes away from the pollution of modern technology."_

_Target audience: Parents/guardians of the children of our future, nature lovers, advocate for holistic education of children, etc._



## Features
- refer to API specifications.

### User Accounts

- [X] Username
- [X] Email Address
- [X] Password


### Project

- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Target Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created

- [X] Ability to post updates on a project by the owner (WIP)
  - [X] A comment
  - [X] When the comment was posted

- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy

- Project Updates
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [ ] Destroy
  
- Pledge
  - [X] Create
  - [X] Retrieve
  - [ ] Update
  - [ ] Destroy

- User
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy

### Implement suitable permissions

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Limit who can create
  - [ ] Limit who can retrieve
  - [X] Limit who can update
  - [X] Limit who can delete
- Project Updates
  - [X] Limit who can create
  - [x] Limit who can retrieve
  - [X] Limit who can update
  - [x] Limit who can delete
- Pledge
  - [X] Limit who can create
  - [ ] Limit who can retrieve
  - [X] Limit who can update
  - [x] Limit who can delete
- User
  - [ ] Limit who can retrieve 
  - [X] Limit who can update
  - [X] Limit who can delete

### Implement relevant status codes

- [X] Get returns 200
- [X] Create returns 201
- [X] Not found returns 404

### Handle failed requests gracefully 

- [X] 404 response returns JSON rather than text

### Use token authentication

- [X] implement /api-token-auth/

## Additional features

- [X] {Total of the amount of pledges for a project}

{{ Sum of the total amount of pledges for a project }}

- [X] {Pledges filter}

{{ Ability to filter the pledges by project or anonymous value}}

- [X] {Project Updates}

{{ Regular updates by the owner on the project. }}

### External libraries used

- [x] django-filter


## Part A Submission 

- [x] A link to the deployed project. 
        [Deployed Project](https://green-surf-5691.fly.dev/ "Deployed Project.")

- [x] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [x] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [x] A screenshot of Insomnia, demonstrating a token being returned.
        [All screenshots & API Specs.](https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-alanychan/blob/main/AlanyChan-Django-Crowdfunding-API-Project.docx "Screenshots & API Specs.")
        
- [x] Your refined API specification and Database Schema.
        [Database Schema](https://dbdiagram.io/d/63dbc3e6296d97641d7e00ca "Database Schema.")

### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).

1. Create User

```shell
curl --request POST \
  --url http://localhost:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '{
		"first_name": "Seb",
		"last_name": "dog",
		"username": "seb",
		"email": "seb@cfd.co",
		"password": "seb"
}'

2. Sign in User

```shell
curl --request POST \
  --url http://localhost:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username" : "seb",
	"password" : "seb"
}'
```

3. Create Project

```shell
curl --request POST \
  --url http://localhost:8000/projects/ \
  --header 'Authorization: Token 7377227d6a1efe6cbe1ef6c174401f995a73d10f' \
  --header 'Content-Type: application/json' \
  --data '{
	
	"title": "Project Penguins on holidays in Summer!!",
	"description": "Funding for penguins Pierre & family to go on holidays in the tropics. To do so, they need a cold suit that will regulate their body temperature which will alltogether cost $10,000.",
	"goal":10000,
	"image": "https://www.pinguins.info/Biologie/keu04_humpi001a.jpg",
	"is_open": true
}'
```
