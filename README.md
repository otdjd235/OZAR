# OZAR – Worship & Choir Management Platform

**OZAR** est une plateforme de gestion dédiée aux chorales et équipes de louange d’église.  
Le projet vise à centraliser les chants, les thèmes, les répertoires de culte, les événements et la coordination des musiciens dans une seule application moderne (Web + Mobile).
Il s'agit d'un projet personnel assisté par chatGPT, pour la mise en pratique des connaissances acquises en dev d'apk web , gestion des bases de données vectrorielles et intégration d'IA.

>  **Statut** : Projet en cours de développement (MVP backend déjà fonctionnel)

---

##  Objectifs du projet

- Centraliser un **répertoire de chants** avec tonalités, paroles et liens
- Classer les chants par **thèmes** (Louange, Adoration, Grâce, Foi…)
- Gérer des **répertoires de culte (setlists)** structurés par sections  
  (Louange, Adoration, Offrande, Célébration)
- Permettre à plusieurs leads de créer des répertoires pour un même événement
- Gérer des **événements** (culte spécial, concert, conférence, etc.)
- Implémenter un **système de rôles** (ADMIN, DIRECTOR, LEAD, CHANTRE, INSTRUMENTIST)
- Sécuriser l’accès via un **code d’invitation par église**
- Préparer une future **application mobile (APK)** pour les musiciens

---

##  Fonctionnalités déjà implémentées

### Authentification & Accès
- Inscription avec `invite_code` d’église
- Connexion JWT
- Gestion des rôles utilisateurs
- Accès multi-églises sécurisé (anti cross-church)

###  Chants & Thèmes
- CRUD Thèmes (avec vidéo d’exhortation par thème)
- CRUD Chants
- Association Chant ↔ Thèmes (many-to-many)
- Refus automatique des doublons de thèmes

###  Répertoires (Setlists)
- Création de répertoires de type :
  - `SERVICE` (culte normal)
  - `EVENT` (lié à un événement)
- Sections dynamiques :
  - SERVICE → Louange / Adoration / Offrande  
  - EVENT → Louange / Adoration / Célébration
- Ajout de chants dans une section avec :
  - position
  - note (instruction musicale, intro, transition…)
- Suppression d’un chant d’un répertoire
- Permissions par rôle (Admin / Director / Lead)

###  Événements
- Création d’événements
- Association de plusieurs répertoires à un événement
- Chaque lead peut gérer son propre répertoire

---

##  Stack technique

### Backend
- **Python 3.11**
- **FastAPI**
- **PostgreSQL 16**
- **SQLAlchemy ORM**
- **Alembic**
- **JWT Auth**
- **Docker** 
- **pgvector**, préparé pour IA future

### Frontend 
- Application mobile Android
- Web dashboard Admin / Director
- Reconnaissance audio IA pour l'identification d'un chant joué

---

##  Lancer le projet en local

### 1) Cloner le repo

git clone https://github.com/otdjd235/OZAR.git
cd OZAR/backend

### 2) Créer l'environnement virtuel
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\Activate.ps1 # Windows

### 3) Installer les dépendances
pip install -r requirements.txt

### 4) Lancer PostgreSQL via Docker
docker compose up -d

### 5) Appliquer les migrations
alembic upgrade head

### 6) Lancer l’API
uvicorn app.main:app --reload

### Accès API

Swagger UI :
 http://127.0.0.1:8000/docs

### Exemples de scénarios

- Créer un thème (Louange)
- Créer un chant
- Créer un événement
- Créer un setlist lié à l’événement
- Générer les sections par défaut
- Ajouter des chants dans chaque section
- Visualiser le répertoire complet groupé par sections

### Roadmap

- Upload d’images pour Dress Code
- Gestion des Dress Codes par événement
- Répertoires collaboratifs multi-leads
- Reconnaissance audio IA (chant joué → suggestion)
- Mode offline mobile
- Notifications (WhatsApp / Push)
- Version APK publique
