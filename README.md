# RedeemIt - Your Employee Recognition Platform

## 1. **Introduction**

[RedeemIt](https://redemption-website-ec86c7604627.herokuapp.com/) is a mock employee recognition platform inspired by the solutions offered by [Workhuman](https://www.workhuman.com). It allows employees to view their points balance, browse a catalogue of gift cards, and redeem rewards. Administrators can manage the catalogue and update employee point balances, ensuring a structured and efficient rewards process.  

Built using the **Django framework**, this project serves as a learning and portfolio exercise, demonstrating full-stack development skills in designing a functional and user-friendly web application.  

## **Table of Contents**

1. [Introduction](#introduction)  
2. [User Experience - UX](#2-user-experience---ux)  
    2.1. [Scope and Structure](#21-scope-and-structure)  
    2.2. [User Stories](#22-user-stories)  
    2.3. [Interface and Wireframes](#23-interface-and-wireframes)  
    2.4. [Visual Design](#24-visual-design)  
    2.5. [Project Planning and Agile Approach](#25-project-planning-and-agile-approach)  
3. [Platform Features](#3-platform-features)  
    3.1. [User Interactions](#31-user-interactions)  
    3.2. [Admin & Employee Functionalities](#32-admin--employee-functionalities)  
    3.3. [Database & CRUD Functionality](#33-database--crud-functionality)  
    3.4. [Future Enhancements](#34-future-enhancements)  
4. [Technology](#4-technology)  
    4.1. [Languages](#41-languages)  
    4.2. [Frameworks & Librairies](#42-frameworks--librairies)  
    4.3. [Development & Deployment Tools](#43-development--deployment-tools)  
    4.4. [Testing & Optimisation Tools](#44-testing--optimisation-tools)  
5. [Testing](#5-testing)  
    5.1. [Manual Testing](#51-manual-testing)  
    5.2. [Fixed Bugs](#52-fixed-bugs)  
    5.3. [Automated Testing](#53-automated-testing)  
6. [Deployment](#6-deployment)  
    6.1. [Heroku](#61-heroku)  
    6.2. [Database Migration](#62-database-migration)  
    6.3. [Forking and Cloning](#63-forking-and-cloning)  
7. [Credits](#7-credit)

## 2. **User Experience - UX**

### **2.1. Scope and Structure**

### Scope  

This project focuses on two main user roles:  

- **Employees** – Can view their **points balance**, browse the **gift card catalogue**, and **redeem rewards**.  
- **Administrators** – Can **manage the gift card catalogue** and **update employee point balances** through the admin panel.  

The platform is designed to provide a **clear redemption flow** and an **efficient management system** while ensuring an **intuitive user experience**.  

### Structure

The project is structured around three key areas:  

- **User Flow** – A simple and logical process for browsing, selecting, and redeeming gift cards.  
- **Admin Management** – A straightforward interface for adding, updating, and removing rewards.  
- **Clean & Responsive Design** – A structured layout that ensures clarity, accessibility, and ease of use across all devices.

### **2.2. User Stories**  

The project follows a user-centric approach, ensuring a smooth and intuitive experience for both employees and administrators. To structure the development process, **user stories are grouped into EPICs**, each focusing on a key aspect of the platform, such as employee interactions, reward redemption, and administrative management.  


#### EPIC - Catalogue Management
1. **Add New Reward** *(must have)*  
   Admins can add new items to the gift card catalogue, including details like name, description, points required, etc...

2. **Edit Existing Reward** *(should have)*  
   Admins can modify details of existing gift card, such as updating the item name, description, or point value.

3. **Delete Reward** *(should have)*  
   Admins can remove gift card from the catalogue to keep the list up-to-date and relevant.

---

#### EPIC - Admin Access

1. **Manage User's Points Balance** *(should have)*  
   Admins can view and update the points balance for individual employees, ensuring accurate tracking of rewards.

---

#### EPIC - Employee Access
1. **Employee Login** *(must have)*  
   Provides secure login functionality for employees to access the redemption platform.

2. **Employee Logout** *(must have)*  
   Allows employees to securely log out of their session once they are done using the platform.

3. **Site User View Profile Details** *(could have)*  
   Employees can view their profile details, including their current reward points balance and basic personal information.

---

#### EPIC - Redemption Process
1. **Browse Available Gift Card** *(must have)*  
   Employees can view the full list of available gift card.

2. **Access Detailed Page** *(should have)*  
   Employees can view detailed information about a specific gift card, including its description and points required.

3. **Add Gift Card to Cart** *(must have)*  
    Employees can add gift card to their cart before proceeding to redeem.

4. **View Cart** *(must have)*  
    Employees can review the list of gift card added to their cart, including the total points required.

5. **Modify Cart** *(should have)*  
    Employees can update the quantity or delete gift card from their cart before finalising the redemption.

6. **Redeem Items** *(must have)*  
    Employees can finalise the redemption process, confirming their selected gift cards and updating their points balance.

### **2.3. Interface and Wireframes**

#### Flowchart

The following flowchart illustrates the **employee (user) journey** within the platform. It maps out the key actions an employee can perform, such as logging in, browsing the catalogue, adding items to the cart, and redeeming rewards.  
It was created using [Lucidchart](https://www.lucidchart.com/pages/) to provide a clear visual representation of the redemption process.

<details>
  <summary>Click to view Flowchart</summary>

  ![Flowchart](images-documentation/readme_images/redemption_platform_flowchart.png)

</details>

---

#### Wireframes

Wireframes were designed to outline the layout and functionality of each page and to help visualise the user flow. This ensures the platform’s structure is logical, responsive, and user-friendly.  
[Balsamiq](https://balsamiq.com/?gad_source=1&gclid=CjwKCAiAm-67BhBlEiwAEVftNlJTamA65VQDctZEK7owZeyEq-JZFKrhXC3gEYcO3MafEUiVCTYcwBoCwXQQAvD_BwE) was utilised to craft the detailed wireframes. These initial sketches served as the foundation for the app’s final structure and layout.

#### Login Page
<details>
  <summary>Click to view the Login Page wireframe</summary>

  ![Login Page Wireframe](images-documentation/wireframes/log-in_page.png)

</details>

#### Redemption Platform (Catalogue Home page)
<details>
  <summary>Click to view the Redemption Platform wireframe</summary>

  ![Redemption Platform Wireframe](images-documentation/wireframes/plateform_landing_page.png)

</details>

#### Gift Card Details Page
<details>
  <summary>Click to view the Gift Card Details Page wireframe</summary>

  ![Gift Card Details Page Wireframe](images-documentation/wireframes/plateform_product_details_page.png)

</details>

#### Cart Page
<details>
  <summary>Click to view the Cart Page wireframe</summary>

  ![Cart Page Wireframe](images-documentation/wireframes/cart_page.png)

</details>

---

### **2.4. Visual Design**

#### UI Design Approach 

The platform follows a **modern, clean design** with an emphasis on usability and accessibility.  

- **Mobile-First Approach** – Optimized for all screen sizes.  
- **Workhuman-Inspired Colour Palette** – Uses corporate colours for branding consistency.  
- **Typography Choices** – Ensures readability and modern aesthetics.

---

#### Typography & Colours
For this project, I aimed to offer a **fresh and distinct** version of the existing platform while keeping the functionalities simple and user-friendly. To maintain a connection to the company’s identity, I incorporated branding colours from the **Workhuman** website to reflect the style and spirit of the company.  
The colour palette also draws inspiration from the tech industry and current design trends, creating a clean, professional, and modern aesthetic.  
The chosen typography ensures **readability** and enhances the overall user experience, while the colour scheme provides a visually appealing and accessible interface.


#### Colour Scheme
The chosen colour palette draws inspiration from **Workhuman**'s branding and aligns with a modern, tech-inspired aesthetic.

![Colour Inspiration](images-documentation/readme_images/color_scheme.png)

| **Colour** | **Name**             |  
|------------|----------------------|  
| #300E82  | Persian Indigo       |
| #586BBE  | Savoy Blue           |
| #9B6B82  | Mountbatten Pink     |
| #DECD62  | Citron               |
| #484848  | Davy's Grey          |

</br>


<details>
  <summary>Click to view inspiration from Workhuman website</summary>

  ![Colour Inspiration](images-documentation/readme_images/colours_inspiration_from_workhuman.png)

</details>

<details>
  <summary>Click to view inspiration from Unlocking Colour Communication</summary>

  ![Colour Inspiration](images-documentation/readme_images/trends.webp)

</details>

---

#### Typography
To ensure readability and maintain a clean, modern look, the following fonts were chosen:

- **Primary Font**: *Poppins*  
  - Applied to the **main body text** for a clean and professional look.  

- **Accent Font**: *Quicksand*  
  - Used for **decorative elements** and **highlighted text**, adding a modern touch.  

- **Footer Font**: *Montserrat*  
  - Applied to **footer text**, maintaining a subtle yet structured style. 

---

### **2.5. Project Planning and Agile Approach**

The development of **RedeemIt** followed an **Agile methodology**, allowing for incremental improvements, flexibility, and structured task management. 
By breaking the project into smaller **user stories**, it ensured a smooth workflow while staying aligned with user needs.  

#### Development Tools & Planning

To maintain an organised and efficient development process, the following tools and techniques were used:  

- **GitHub Projects** – Tracked tasks and iterations, ensuring a structured development cycle.  
- **Lucidchart** – Used to map out the user flow and database schema.  
- **MOSCOW Prioritization** – Applied to prioritise features, ensuring that essential functionalities were developed first.  

The **MOSCOW method** was used to categorise features into **Must Have, Should Have, and Could Have**:

| **Priority** | **Feature** |
|-------------|------------|
| **Must Have (54%)** | Employee Login |
|  | Employee Logout |
|  | Browse Available Gift Cards |
|  | Add Gift Card to Cart |
|  | View Cart |
|  | Redeem Items |
|  | Add New Reward (Admin) |
| **Should Have (38%)** | Access Detailed Page for Gift Card |
|  | Modify Cart (Update Quantity or Remove Item) |
|  | Edit Existing Reward (Admin) |
|  | Delete Reward (Admin) |
|  | Manage User’s Points Balance (Admin) |
| **Could Have (8%)** | Site User View and Manage Profile Details |
|

## 3. Platform Features

### **3.1. User Interactions**

Employees interact with the platform through an intuitive and structured redemption process:

- **Secure Authentication**  
  - Employees log in and out securely using **Django Allauth**.  

- **Browsing Rewards**  
  - Employees can view available gift cards, with access to detailed descriptions, stock and required points.  

- **Redemption Process**  
  - Employees can add items to their cart, modify quantities, and remove selections.  
  - The system ensures only users with sufficient points can redeem rewards.  
  - Upon redemption, points are deducted, and the cart is cleared.  

- **Responsive Feedback & Validation**  
  - Employees receive **instant feedback** when redeeming rewards or encountering errors (e.g., insufficient balance).

---

### **3.2. Admin & Employee Functionalities**

Admins have full control over the gift card catalogue and user point balances via the admin panel:

- **Manage Catalogue**  
  - Add new gift cards with details such as name, points required, stock quantity, and T&Cs.  
  - Edit existing gift cards to update descriptions, point values, or stock.  
  - Delete gift cards that are no longer available.  

- **Manage Employee Points**  
  - Admins can update employee points balances through the admin panel.

---

### **3.3. Database & CRUD Functionality**

The platform is structured around **CRUD (Create, Read, Update, Delete) principles**, ensuring efficient interaction between employees, admins, and stored data.  

#### Database Design & Structure 

| **Table**          | **Purpose** | **Key Fields** |  
|-------------------|---------------------------------|---------------------------|  
| **CatalogueItem** | Stores details of available rewards | `reward_name`, `points_cost`, `stock_quantity`, `image` |  
| **UserProfile**   | Tracks employees' points balance | `user_id`, `point_balance` |  
| **Cart & CartItem** | Manages user selections before redemption | `cart_id`, `user_id`, `reward_id`, `quantity` |  

---

#### CRUD in Action   

| **Action** | **Admin Functionalities** | **Employee Functionalities** |  
|------------|------------------|------------------|  
| **Create** | Add new gift cards to the catalogue | Add items to cart for redemption |  
| **Read**   | View and manage all gift cards | View available rewards and cart items |  
| **Update** | Modify gift card details | Adjust quantities in cart before redemption |  
| **Delete** | Remove gift cards from the system | Remove items from cart |  

---

#### MVC architecture

The **MVC architecture** (Model-View-Controller) was followed to maintain a structured flow:  

- **Model** – Handles database logic (e.g., `CatalogueItem`, `Cart`, `CartItem` models).  
- **View** – Renders templates like `catalogue.html` or `cart.html`.  
- **Controller** – Processes user input and manages data between models and templates.  

The **Entity Relationship Diagram (ERD)** below illustrates how the database models connect and interact:  

<details>
  <summary>Click to view ERD Diagram</summary>

  ![ERD Diagram](images-documentation/readme_images/redemption_platform_ERD.png)

</details>

### **3.4. Future Enhancements**

The current version of **RedeemIt** focuses on core functionality, but there is room for expansion and optimisation. Some potential enhancements include:

- **Redemption History**  
  - Employees can track past redemptions.  

- **Automated Email Notifications**  
  - Employees and admins receive confirmation emails for transactions.  

- **Admin Analytics Dashboard**  
  - A data-driven insights panel for tracking redemptions, employee engagement, and points distribution.  

These improvements would enhance the platform’s **efficiency and usability**, offering a more complete **employee recognition experience**.  

## 4. Technology

### **4.1. Languages**

- **Python** – Used for backend logic and database interactions.  
- **HTML** – Provides the structure and content of the web pages.  
- **CSS** – Handles the styling and layout.  
- **JavaScript** – Enables interactive elements. 

---

### **4.2. Frameworks & Librairies**
 
- **Django** – The main web framework used for handling authentication, database management, and routing.  
- **Bootstrap 5** – Used for responsive design and styling components.  
- **Django Allauth** – Handles user authentication, login, logout, and account management.  
- **PostgreSQL** – The database storing all user profiles, rewards, and transactions.  
- **dj-database-url** – Simplifies PostgreSQL database configuration via environment variables.  
- **psycopg2** – A PostgreSQL adapter allowing Django to interact with the database.  
- **Cloudinary** – Used for storing and managing media files.  
- **Whitenoise** – Enables serving static files in production.  
- **Gunicorn** – A WSGI HTTP server for running the Django application in production.

---

### **4.3. Development & Deployment Tools***

- **GitHub** – Version control system for storing the repository and managing project tasks.  
- **GitPod** – Cloud-based development environment used for initial coding.  
- **VSCode** – Local development environment used after switching from GitPod.  
- **Heroku** – Platform for **deploying and hosting the application** in a live environment.  

---

### **4.4. Testing & Optimisation Tools**

- **HTML Validator** – Checked for syntax errors in HTML files.  
- **W3C CSS Validator** – Ensured the CSS followed best practices and had no errors.  
- **JSHint** – Analysed JavaScript code to detect potential issues.  
- **Squoosh** – Optimised images by converting them to **WebP format**, improving loading speed.
- **ChatGPT & GitHub Copilot** – Assisted with debugging, code suggestions, and documentation refinements.

## 5. Testing

### **5.1. Manual Testing**

#### ADMIN - Catalogue Management

| TEST | EXPECTED OUTCOME | PASS/FAIL |
|:---:|:---:|:---:|
| Create a new item | Item is successfully created with all required fields and displayed on the platform | PASS |
| View list of existing items | All items are listed on the admin dashboard & the platform | PASS |
| Edit an existing item | Changes are saved and reflected on the admin dashboard & the platform | PASS |
| Delete an item | Item is removed from both the admin dashboard & the platform | PASS |

#### EMPLOYEE (User) - Add to Cart

| TEST | EXPECTED OUTCOME | PASS/FAIL |
|:---:|:---:|:---:|
| View detailed page of an item | Detailed information about the item is displayed | PASS |
| Click "Add to Cart" button | The item is added to the cart, and the cart page reflects the item | PASS |
| Add the same item again | The quantity of the item in the cart increases by 1 | PASS |
| View the cart page | The cart displays all added items, their quantity, and total points cost | PASS |

#### EMPLOYEE (User) - Cart Management

| TEST | EXPECTED OUTCOME | PASS/FAIL |
|:---:|:---:|:---:|
| Modify item quantity in cart | Quantity updates correctly, and total points cost is recalculated | PASS |
| Delete item by setting quantity to 0 | Item is removed from the cart, and total points cost updates | PASS |


#### EMPLOYEE (User) - Redemption Logic

| TEST | EXPECTED OUTCOME | PASS/FAIL |
|:---:|:---:|:---:|
| Redeem with sufficient balance | Balance is reduced, cart is cleared, and changes show in the admin dashboard | PASS |
| Redeem with insufficient balance | Button is disabled, and "Oops, xxx points short!" message is shown | PASS |
| Check cart after redemption | Cart shows "Your cart is empty," no items remain in admin dashboard | PASS |
| Check balance in admin dashboard | Updated balance shows correctly after redemption | PASS |

---

### **5.2. Fixed Bugs**

---

### **5.3. Automated Testing**

---

## 6. Deployment

### **6.1. Heroku**

The site was deployed successfully to [Heroku](https://redemption-website-ec86c7604627.herokuapp.com/) following the steps below:

1. In *Gitpod*, create a list of dependencies in `requirements.txt` file:
    - Run `pip3 freeze > requirements.txt` in the terminal.
2. In *Heroku* account, create the new App:
    - Select `New` and `Create a new app`.
    - Name the App and choose a region: `Europe` 
    - Click `Create App`.
3. In the new App page, access to the `Settings` section.
4. In `Config Var` add :
    - `DATABASE_URL` and its value.
    - `SECRET_KEY` and its value.
    - `CLOUDINARY_URL` and its value.
    - Click `Add`.
5. Access to the `Deploy` section.
6. Select the deployment method:
    - Select `GitHub`
    - Search for the repository by taping the name in the search barre.
    - Click on `Connect`
7. Once App deployed, the message *Your app was successfully deployed.*

The live link can be found here: [ReedemIt](https://redemption-website-ec86c7604627.herokuapp.com/)

---

### **6.2. Database Migration**

During development, I realised that I had mistakenly been using a database already associated with another project, which created unintended dependencies. To ensure a clean setup, I decided to migrate to a new database. While following an online guide, I encountered several challenges that required troubleshooting and manual intervention.   
This section outlines the steps taken, the issues faced, and how they were resolved with the valuable guidance and patience of a **Code Institute Tutor**.

#### **Steps Followed for Database Migration**  

1. **Backup Existing Data**  
  - Exported all catalogue items into a JSON file to prevent data loss:  
    ```powershell
    python manage.py dumpdata catalogue --indent 2 > catalogue/fixtures/catalogue_items.json
    ```  

2. **Create a New Database**  
  - Set up a **new PostgreSQL database** and updated the `DATABASE_URL` in both **Heroku** and the local `.env.py` file.  

3. **Reset Migrations & Apply to New Database**  
Since the new database is empty and Django does not recognize previous migrations, we had to reset migrations:  

  - **Fake-initialise migrations:**  
    ```powershell
    python manage.py migrate --fake
    ```  
    - This marks all migrations as applied without actually executing them.  
    - It prevents Django from trying to reapply migrations that were already used in the previous database.  
    - This step ensures Django recognises models without making any unwanted changes.  

  - **Delete existing migration files (except `__init__.py`) to reset migration history:**  
    ```powershell
    Get-ChildItem -Path .\* -Include "migrations" -Recurse | Remove-Item -Recurse -Force
    ```  
    - This removes all migration files across all apps, forcing Django to recreate migrations based on the current models.    

  - **Recreate migrations and apply them to the new database:**  
    ```powershell
    python manage.py makemigrations
    python manage.py migrate
    ```  

At this point, **everything started to break**, leading to migration failures.

---

#### **Issue Encountered & How We Fixed It**  

**Error Message:**  

    ```
    django.db.utils.ProgrammingError: relation "django_site" does not exist 
    LINE 1: SELECT 1 AS "a" FROM "django_site" LIMIT 1
    ```  

1. **Recreate Missing Migration Files**  
  - Manually recreated the `migrations` folders and added `__init__.py` inside each app:
    ```
    catalogue/migrations/__init__.py
    home/migrations/__init__.py
    ```  

2. **Fake-Migrate All Apps**  
  - Each app was individually fake-migrated to allow Django to recognize existing models, like with these examples below:
    ```
    python manage.py migrate home --fake
    python manage.py migrate admin --fake
    python manage.py migrate catalogue --fake
    ```  

3. **Verify Migration Status**  
  - After applying the migrations, checked the current migration status with:
    ```
    python manage.py showmigrations
    ```  

4. **Final Migration Execution**  
  - Once all migrations were properly listed, executed the final migration command:
    ```
    python manage.py migrate
    ```  

5. **Create a Superuser**  
  - Since this is a fresh database, the admin account must be recreated:  
    ```powershell
    python manage.py createsuperuser
    ```  

---

### **6.3. Forking and Cloning**

Forking the repository creates a copy of this project, allowing modifications without affecting the original code. Once the repository is forked, it can be cloned to a local machine for development.</br>
Follow these steps to fork, clone, and work on the project:

- **Fork the repository**
  - Go to the repository you want to fork on [GitHub](https://github.com/).
  - In the top-right corner of the page, click `Fork`.
  - Name the new forked repository, then click `Create Fork`.
  - This creates a copy of the repository under your own GitHub account.

- **Clone the forked repository**
  - In the forked repository on GitHub, above the list of files, click `Code`.
  - Copy the URL for the repository (either HTTPS or SSH).
  - Open a terminal (or Git Bash).
  - Type `git clone`, then paste the copied URL.
  - Press `Enter`.
  - Navigate to the newly cloned repository directory: `cd` and the repository name.

## 7. Credit