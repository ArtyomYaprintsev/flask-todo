# Todo app

Todo application with Flask

## Description

Filler.

## Development

### Using emoji into commits

| Emoji  | Code                  | Usage          | Description                              |
|--------|-----------------------|----------------|------------------------------------------|
| ✨     | `:sparkles:`           | New Feature    | Adding a new feature                     |
| 🐛     | `:bug:`                | Bug Fix        | Fixing a bug                             |
| ♻️     | `:recycle:`            | Refactoring    | Refactoring code without changing behavior |
| ⚡     | `:zap:`                | Code Optimization | Optimizing code for better efficiency |
| ✅     | `:white_check_mark:`   | Writing Tests  | Adding or updating tests                 |
| 📝     | `:memo:`               | Documentation  | Adding or updating documentation         |
| 🚀     | `:rocket:`             | Release        | Deploying or releasing changes           |
| 🎨     | `:art:`                | Style Changes  | Improving code format/structure, e.g., code style changes |
| 📦     | `:package:`            | Dependency Changes | Adding, updating, or removing dependencies |
| 🛠     | `:hammer_and_wrench:`  | Build or CI    | Changes related to build system or CI    |
| 🔥     | `:fire:`               | Removals       | Removing code or files                   |
| 🚑     | `:ambulance:`          | Critical Hotfix | Immediate fix for a critical issue      |
| 🔒     | `:lock:`               | Security       | Fixing security issues                   |
| 🚧     | `:construction:`       | Work in Progress | Ongoing development not yet complete   |
| 🔀     | `:twisted_rightwards_arrows:` | Merging Branches | Merging branches or resolving conflicts |
| ⏪     | `:rewind:`             | Reverts        | Reverting changes                        |
| 💥     | `:boom:`               | Breaking Changes | Introducing breaking changes             |

### Install requirements

Install requirements

```bash
pip install -r requirements.txt
```

### Install linter for commits messages

```bash
gitlint install-hook
```

### Alembic usage

Generate new version:

```bash
alembic revision --autogenerate -m "Message"
```

Run all migrations:

```bash
alembic upgrade head
```

## Roadmap

1. Project Initialization and Setup
    - **Task**: Set up the project structure.
    - **Result**:
      - Set up Flask project, virtual environment, and dependencies (Flask, SQLAlchemy, etc.).
      - Establish folder structure: `models`, `routes`, `services`, `auth`, `config`.

2. Basic Task Management
    - **Task**: Implement core task management functionality.
    - **Result**:
      - **Models**: Create `Task` model with fields: `id`, `header`, `description`, `created_at`, `completed`.
      - **Endpoints**: Create CRUD API endpoints for `Task`.
      - **Database**: Run migrations for `tasks` table.

3. User Authentication
    - **Task**: Implement user authentication via email and password.
    - **Result**:
      - **Models**:
        - `User` model: `id`, `email`, `password_hash`, `joined_at`, `last_login_at`.
        - `Token` model: `id`, `user_id`, `token`, `created_at`.
      - **Endpoints**: User signup, login, logout, JWT token handling.
      - **Security**: Protect routes using `@jwt_required`.

4. Relating Tasks with Users
    - **Task**: Associate tasks with users.
    - **Result**:
      - **Models**: Add `user_id` foreign key to `Task` model.
      - **Endpoints**: Modify `Task` endpoints to filter by authenticated user.
      - **Security**: Restrict task access to owners.

5. Task Lists Management with Privacy Control
    - **Task**: Add task list functionality with privacy settings.
    - **Result**:
      - **Models**:
        - `TaskList` model: `id`, `name`, `created_at`, `user_id`, `is_private`.
        - Modify `Task` model to include `task_list_id`.
      - **Endpoints**:
        - CRUD API for `TaskList`.
        - Default `is_private` to `False`, allowing public task lists.
        - Endpoint to update `is_private` to `True`.
      - **Security**: Enforce visibility restrictions based on `is_private`.

6. File Attachments for Tasks
    - **Task**: Add support for attaching files to tasks.
    - **Result**:
      - **Models**: `File` model with fields: `id`, `filename`, `path`, `task_id`.
      - **Endpoints**: Upload, list, and download file attachments for tasks.
      - **Security**: Restrict access based on task ownership.

7. OAuth2 Authentication
    - **Task**: Implement OAuth2 login with Google, GitHub, etc.
    - **Result**:
      - **Endpoints**: OAuth redirect and callback endpoints.
      - **Security**: Handle account creation or linking during OAuth login.

8. Account Linking
    - **Task**: Allow users to link multiple external accounts.
    - **Result**:
      - **Models**: `UserOAuth` model with fields: `id`, `user_id`, `provider`, `provider_user_id`.
      - **Endpoints**: Link external accounts to existing users.
      - **Security**: Ensure proper linking and account management.

9. Two-Factor Authentication (2FA)
    - **Task**: Add TOTP-based 2FA.
    - **Result**:
      - **Models**: Extend `User` model with `totp_secret`.
      - **Endpoints**: Enable and verify TOTP during login.
      - **Security**: Enforce 2FA where enabled.

10. User Avatar Management
    - **Task**: Implement user avatar management.
    - **Result**:
      - **Models**: Extend `User` model with `avatar` field.
      - Default avatar should be provided for all users.
      - On user image upload, save file inside `/media` folder on the server.
      - Generate and store 32x32, 64x64, and 128x128 formats.
      - **Endpoints**: Upload, retrieve, and update avatar.
      - **Security**: Ensure only the user can update their avatar.

11. Page Caching
    - **Task**: Implement page caching for user task-lists.
    - **Result**:
      - Create additional API endpoints with `GET` method to generate cached HTML page.
      - Page should list all user task-lists and include the date of caching.
      - Cache pages for optimized loading and retrieval.
      - **Security**: Ensure only the authenticated user can view their cached pages.

12. Tests Configuration with Pytest
    - **Task**: Set up testing infrastructure with pytest.
    - **Result**:
      - Configure pytest for the project.
      - Write unit tests for models, services, and API endpoints.
      - Integrate test coverage reporting.

13. User Notifications via Email
    - **Task**: Implement email notifications for user activities.
    - **Result**:
      - **Services**: Use Flask-Mail or a similar library to send emails.
      - Notify users of important actions like task deadlines or account changes.
      - Allow users to manage notification preferences.

14. OpenAPI Configuration (Swagger)
    - **Task**: Document the API using OpenAPI/Swagger.
    - **Result**:
      - Integrate Flask-Swagger or Flask-RESTPlus for auto-generating documentation.
      - Ensure all API endpoints are documented.
      - Make the documentation available via a `/docs` endpoint.

15. Deployment Configuration
    - **Task**: Prepare the application for deployment.
    - **Result**:
      - Create Dockerfile and Docker Compose for containerization.
      - Configure environment variables for production.
      - Set up CI/CD pipelines (e.g., GitHub Actions, GitLab CI).
      - Deploy to a cloud platform (e.g., AWS, Heroku, DigitalOcean).
      - Implement logging and monitoring.
