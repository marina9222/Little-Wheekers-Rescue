# [LITTLE WHEEKERS RESCUE](https://little-wheekers-rescue-bfdb249eed00.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/marina9222/Little-Wheekers-Rescue)](https://github.com/marina9222/Little-Wheekers-Rescue/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/marina9222/Little-Wheekers-Rescue)](https://github.com/marina9222/Little-Wheekers-Rescue/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/marina9222/Little-Wheekers-Rescue)](https://github.com/marina9222/Little-Wheekers-Rescue)

## Description

Little Wheekers Rescue website is the ultimate platform for guinea pig lovers, dedicated to finding forever homes for these adorable creatures. With a clean, user-friendly interface, users can explore our adoption stories, learn about our adoption policy, and browse available guinea pigs ready for adoption.
The site also features a quick and easy donation process, testimonials, and a secure profile section for adopters. Whether you’re here to adopt, donate, or simply learn more, Little Wheekers Rescue ensures an engaging and hassle-free experience, that brings joy to both adopters and people who would like to help us raise money in order to keep the rescue sustainable.


![screenshot](documentation/mockup.png)
source: [amiresponsive](https://ui.dev/amiresponsive?url=https://little-wheekers-rescue-bfdb249eed00.herokuapp.com)


## UX


### Colour Scheme

- `#FBA80C` used for website background color.
- `#636B2F` used for primary color.
- `#323232` used for primary text color.
- `#FAFAFA` used primary highlights.

I used [coolors.co](https://coolors.co/e84610-009fe3-4a4a4f-445261-d63649-e6ecf0-000000) to generate my colour palette.

![screenshot](documentation/coolors.png)

I've used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

```css
:root {
    
    --primary-text-color:#323232;
    --primary-color: #636B2F;
    --primary-bg-color: #FAFAFA;
}
```

### Typography

- [Lato](https://fonts.google.com/specimen/Lato) was used for the primary headers and titles.

- [Roboto](https://fonts.google.com/specimen/Roboto) was used for all other secondary text.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as sign up and log in forms and in the footer.


## User Stories

### New Site Users

- As a new site user, I would like to be able to register an account quick and easy, so that I can use all the features of the website.
- As a new site user, I would like to be able to see a page with all the guinea pigs available for adoptions, so that I can browse and choose the best match for me.
- As a new site user, I would like to be able to make a donation quick and easy, so that I can help the rescue.
- As a new site user, I would like to read about adoption policy, so that I can feel more comfortable starting the process and feel informed.
- As a new site user, I would like to see a section with a bit more information about the rescue, so that I can feel comfortable donating or adopting.
- As a new site user, I would like to have a donation/adoption history, so I can track it.
- As a new site user, I would like to have a sort button, so I can sort the guinea pigs by age/gender.
- As a new site user, I would like to see if I guinea pig has been adopted , so I can know which one is available.

### Returning Site Users

- As a returning site user, I would like to see adopted or not option in the sorting menu, so that I can check easily which ones are adopted or not instead of scrolling all the way down.
- As a returning site user, I would like to see a picture and more information about the guinea pig I have adopted in my profile history, so that I can be able to remember the iformation about the guinea pig coming.
- As a returning site user, I would like to see more adoption stories, so that I can relate more.
- As a returning site user, I would like to get real life notifications when I'm logged in, so that I can track my adoption or donation or have some information about my chosen guinea pig.


### Site Admin

- As a site administrator, I should be able to add a new guinea pig easily, so that I can update the current available guinea pig database.
- As a site administrator, I should be able to edit a guinea pig, so that I can change any information anytime I want.
- As a site administrator, I should be able to delete a guinea pig.


## Wireframes

### Mobile Wireframes

<details>
<summary> Click here to see the Mobile Wireframes </summary >

Home
  - ![screenshot](documentation/wireframes/mobile-home.png)

Home Admin
  - ![screenshot](documentation/wireframes/mobile-home-admin.png)

About Us
  - ![screenshot](documentation/wireframes/mobile-about-us.png)

Adopt a Guinea pig
  - ![screenshot](documentation/wireframes/mobile-adopt-guinea-pig.png)

Adopt a Guinea pig Admin
  - ![screenshot](documentation/wireframes/mobile-adopt-guinea-pig-admin.png)

Adoption Policy
  - ![screenshot](documentation/wireframes/mobile-adoption-policy.png)

Donate
  - ![screenshot](documentation/wireframes/mobile-donate.png)

Sign Up
  - ![screenshot](documentation/wireframes/mobile-sign-up.png)

Sign In
  - ![screenshot](documentation/wireframes/mobile-sign-in.png)

My Profile
  - ![screenshot](documentation/wireframes/mobile-my-profile.png)

Management
  - ![screenshot](documentation/wireframes/mobile-management.png)



</details>


### Tablet Wireframes

<details>
<summary> Click here to see the Tablet Wireframes </summary >

Home
  - ![screenshot](documentation/wireframes/tablet-home.png)

About Us
  - ![screenshot](documentation/wireframes/tablet-about-us.png)

Adopt a Guinea pig
  - ![screenshot](documentation/wireframes/tablet-adopt-guinea-pig.png)

Adoption Policy
  - ![screenshot](documentation/wireframes/tablet-adoption-policy.png)

Donate
  - ![screenshot](documentation/wireframes/tablet-donate.png)

Sign Up
  - ![screenshot](documentation/wireframes/tablet-sign-up.png)

Sign In
  - ![screenshot](documentation/wireframes/tablet-sign-in.png)

My Profile
  - ![screenshot](documentation/wireframes/tablet-my-profile.png)

Management
  - ![screenshot](documentation/wireframes/tablet-management.png)



</details>

### Desktop Wireframes

<details>
<summary> Click here to see the Desktop Wireframes </summary >

Home
  - ![screenshot](documentation/wireframes/desktop-home.png)

About Us
  - ![screenshot](documentation/wireframes/desktop-about-us.png)

Adopt a Guinea pig
  - ![screenshot](documentation/wireframes/desktop-adopt-guinea-pig.png)

Adoption Policy
  - ![screenshot](documentation/wireframes/desktop-adoption-policy.png)

Donate
  - ![screenshot](documentation/wireframes/desktop-donate.png)

Sign Up
  - ![screenshot](documentation/wireframes/desktop-sign-up.png)

Sign In
  - ![screenshot](documentation/wireframes/desktop-sign-in.png)

My Profile
  - ![screenshot](documentation/wireframes/desktop-my-profile.png)

Management
  - ![screenshot](documentation/wireframes/desktop-management.png)



</details>


## Features


### Existing Features

- **Adopt a Guinea Pig Page**

    - The section of the website allowes users to take a look at the available guinea pigs for adoption so they can choose the perfect match.

![screenshot](documentation/features/feature01.png)

- **Adopt a Guinea Pig form**

    - Adoption form that the user needs to fill out in order to apply for an adoption of the chosen guinea pig.

![screenshot](documentation/features/feature02.png)

- **Donate section**

    - Users can choose the amount that they would like to donate to the rescue.

![screenshot](documentation/features/feature03.png)

- **Donate form**

    - Users can fill the form with their credit/debit card and submit the amount for donation.

![screenshot](documentation/features/feature04.png)

- **Adoption Stories**

    - A section of the website showing some of the adoption stories.

![screenshot](documentation/features/feature05.png)

- **Total amount raised section**

    - A section of the website showing real time sum of the amount donated to the rescue.

![screenshot](documentation/features/feature06.png)

- **Sign In Form**

    - Sign In form for users to be able to log in.

![screenshot](documentation/features/feature07.png)

- **Sign Up Form**

    - Sign Up form for users to register an account.

![screenshot](documentation/features/feature08.png)

- **Add a Guinea pig / Managemenet**

    - Feature allowing the admin to add a new guinea pig to the database.

![screenshot](documentation/features/feature09.png)

- **Edit a Guinea Pig / Managemenet**

    - Feature allowing the admin to add a new guinea pig to the database.

![screenshot](documentation/features/feature10.png)


- **Delete a Guinea pig / Managemenet**

    - Feature allowing the admin to add a new guinea pig to the database.

![screenshot](documentation/features/feature11.png)


- **My Profile**

    - My Profile section showing the users their history of adoption and donation.

![screenshot](documentation/features/feature12.png)

- **Sort Button**

    - Sort button allowing users to sort the guinea pigs available for adoption and already adopted ones by age and gender.

![screenshot](documentation/features/feature13.png)



### Future Features

- Adopted/Not choice to the sort button on avaialble guinea pigs page.
    - Adding additional adopted/not choice to the sort button.
- Add an image/information of the adopted guinea pig.
    - Addition to the my profile picture so the users can see the image again and the information of the guinea pig they applied for.
- More adoption stories
    - Add more stories from users adopted guinea pigs.
- Notifications
    - Real life notifications when user is logged in about donation/adoption or just an update.


## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-grey?logo=githubpages&logoColor=222222)](https://pages.github.com) used for hosting the deployed front-end site.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) used as the Python framework for the site.
- [![PostgreSQL by Code Institute](https://img.shields.io/badge/PostgreSQL_by_Code_Institute-grey?logo=okta&logoColor=F05223)](https://dbs.ci-dbs.net) used as the Postgres database from Code Institute.
- [![Cloudinary](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) used for online static file storage.
- [![WhiteNoise](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) used for serving static files with Heroku.
- [![Stripe](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) used for online secure payments of ecommerce products/services.
- [![Gmail API](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) used for sending emails in my application.
- [![Balsamiq](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) used for creating wireframes.
- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used for the icons.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.

