# Salafi Directory with Django & Postgres

>Salafi Directory web application or Salafi sources only. Intended to provide a central point of direction to Salafi organisation's, classes and lectures etc.

## Features

- Search the below in query forms
- Scholar's name and country
- Student's of knowledge name, country and twitter
- Classes information with timezone aware
- Lecture Information with timezone aware
- Centre information
- Store information
- Pilgrimage organisations information
- Interactive map
- Share website, class, lecture and organisation

## Intended usage of website

> Salafi organisations will be able to login to manage their own lisiting. Public can use the query forms to search for the information above.

- Version 1.0.0
- License MIT

## Application Specifications

> Details of application functions.

### Organanisations

- List all organisations based on type of organisation in the database
  - Pagination
  - Select specific fields in result
  - Limit number of results
  - Filter by fields
  - Use HERE maps to get exact location from address
- Get single organisation
- Create new organisation
  - Authenticated users only
  - Must have the role "Superuser"
  - Only one account per organisation
  - Field validation via Django validation
- Upload a logo for organisation
  - Administrator or Superuser
  - logo will be uploaded to local filesystem
- Update organisation
  - Administrator or Superuser
  - Validation on update
- Delete organisation
  - Publisher only

### Classes

- List all classes
- List all classes for centre
  - Pagination
  - Select specific fields in result
  - Limit number of results
  - Filter by fields
  - Timezone aware times
- Get single class
- Create new class
  - Authenticated users only
  - Must have the role "adminstrator"
- Update classes
  - Must have the role "adminstrator"
- Delete class
  - Must have the role "adminstrator"

### Lectures

- List all lectures
- List all lectures for centre
  - Pagination
  - Select specific fields in result
  - Limit number of results
  - Filter by fields
  - timezone aware times
- Get single lecture
- Create new lecture
  - Authenticated users only
  - Must have the role "adminstrator"
- Update lectures
  - Must have the role "adminstrator"
- Delete lecture
  - Must have the role "adminstrator"

### Users & Authentication
- Authentication using built in Django authentication system
- User registration
  - Registeration provided by superuser
  - Once registered a username and password will be provided
  - Passwords stored using PBKDF2 algorithm with a SHA256 hash by Django
- User login
  - User can login with email and password
  - Plain text password will compare with stored hashed password
  - Once logged in, a token will be sent along with a cookie (token = xxx)
- User logout
  - Cookie will be sent to set token = none
- Get user
  - Current logged in user data set with query set filter
- Password reset (lost password)
  - User can request to reset password by emailing Slafi Directory
  - A new password to the users registered email address
  - Password can be reset in the admin area.
- Update admininistrator user info
  - Superuser user only

### Security
- Django passwords stored with PBKDF2 algorithm and SHA256 hash
- Django SQL injections prevention
- Django Host header validation
- Django cross site scripting prevention - XSS
- Django Session security
- Django Clickjacking protection
- Django Cross site request forgery
- Django user uploaded-content protection
- API keys stored in environment variables
- SSL encryption with Lets Encrypt
- Enabled firewall (ufw) and open needed ports
- Stripe payment: https://stripe.com/docs/security
- Django: https://docs.djangoproject.com/en/3.0/topics/security/

### Performance
- Memory cache for website performance
- Limit image size

### Deployment
> Django with Postgres, Nginx, and Gunicorn on Ubuntu 18.04
- https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04