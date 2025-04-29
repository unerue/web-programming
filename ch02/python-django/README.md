# Django 프로젝트 세팅 가이드 (uv 사용)

이 프로젝트는 [uv](https://github.com/astral-sh/uv)를 사용하여 Django 환경을 구성합니다.

---

## 1. uv 설치

최초 1회만 아래 명령어로 uv를 설치하세요.


---

## 3. Django 및 Django REST Framework 설치

```bash
uv pip install django djangorestframework
```

---

## 4. Django 프로젝트 및 앱 생성

```bash
django-admin startproject todoproject .
python manage.py startapp todoapp
```

---

## 5. settings.py 설정

`todoproject/settings.py`의 `INSTALLED_APPS`에 아래 항목을 추가하세요.

```python
'rest_framework',
'todoapp',
```

---

## 6. 마이그레이션 적용

```bash
python manage.py migrate
```

---

## 7. 서버 실행

```bash
python manage.py runserver
```

---

## 참고

- 의존성 관리는 `pyproject.toml`과 `requirements.txt`를 함께 사용합니다.
- 추가 패키지 설치 시에도 `uv pip install 패키지명`을 사용하세요. 