# Git Intro Project

# Task 0 – Basics of HTTP/HTTPS

## 1. HTTP vs HTTPS

### HTTP

HTTP (Hypertext Transfer Protocol) est un protocole de communication utilisé pour échanger des données entre un client (navigateur) et un serveur.

- Les données sont envoyées en clair (non chiffrées)
- Aucun mécanisme de sécurité
- Port par défaut : **80**
- URL commence par `http://`

HTTP ne protège pas les informations sensibles et peut être intercepté.

---

### HTTPS

HTTPS (HTTP Secure) est la version sécurisée de HTTP. Il utilise **TLS (Transport Layer Security)** pour chiffrer les données.

- Données chiffrées
- Authentifie le serveur (certificat SSL/TLS)
- Port par défaut : **443**
- URL commence par `https://`

HTTPS protège la confidentialité et l’intégrité des données.

---

### Tableau comparatif

| Critère | HTTP | HTTPS |
|----------|--------|---------|
| Sécurité | Non sécurisé | Sécurisé |
| Chiffrement | Aucun | TLS |
| Port | 80 | 443 |
| Certificat requis | Non | Oui |
| Protection des données | Non | Oui |

---

### Conclusion

La principale différence est la sécurité : **HTTPS chiffre les données et empêche les interceptions**.

Aujourd’hui, toutes les applications manipulant des données sensibles doivent utiliser HTTPS.

---

## 2. Structure d’une requête et d’une réponse HTTP

### Requête HTTP

Exemple :

GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html


#### Structure :

- **Request line** : méthode, chemin, version
- **Headers** : Host, User-Agent, Accept…
- **Body (optionnel)** : utilisé pour POST, PUT…

---

### Réponse HTTP

Exemple :


HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1024


#### Structure :

- **Status line** : version, code, message
- **Headers** : Content-Type, Content-Length…
- **Body** : HTML, JSON, image…

---

## 3. Méthodes HTTP courantes

- **GET** : récupérer une ressource (ex : page web)
- **POST** : envoyer des données pour créer une ressource (ex : formulaire)
- **PUT** : mettre à jour une ressource (ex : profil utilisateur)
- **DELETE** : supprimer une ressource (ex : commentaire)

---

## 4. Codes de statut HTTP

- **200 OK** : succès
- **301 Moved Permanently** : redirection permanente
- **400 Bad Request** : requête invalide
- **404 Not Found** : ressource introuvable
- **500 Internal Server Error** : erreur serveur

---



Task 1 – Consume Data from an API using curl
1. Background

curl is a command-line tool used to transfer data using protocols such as HTTP and HTTPS.

It is widely used to:

Test APIs

Debug HTTP requests

Interact with RESTful services

Inspect server responses

2. Objectives

Install and use curl

Execute GET and POST requests

Inspect HTTP headers

Interpret API responses

3. Procedure
a) Verify curl installation
curl --version

(Copy your terminal output in your report.)

b) GET posts from JSONPlaceholder
curl https://jsonplaceholder.typicode.com/posts

Returns a JSON array of posts. Each post contains:

userId

id

title

body

Example:

[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit..."
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae..."
  }
]
c) Fetch headers only
curl -I https://jsonplaceholder.typicode.com/posts

Shows only HTTP response headers (status, content-type, server info).

d) Make a POST request
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts

Example response:

{
  "title": "foo",
  "body": "bar",
  "userId": 1,
  "id": 101
}
4. Useful curl Options

-I → Fetch headers only

-X → Specify HTTP method

-d → Send data in request body

Pretty-print JSON:

curl https://jsonplaceholder.typicode.com/posts | jq
5. Expected Output

curl --version → Version info

GET request → JSON array

Headers request → Only headers

POST request → Simulated created post (id: 101)

6. Conclusion

Using curl you can:

Test GET/POST requests

Inspect headers

Debug API responses

Interact with REST APIs from the command line

It’s an essential tool for backend development and API testing.
